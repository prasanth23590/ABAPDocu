---
title: "Meshes - Mesh Path Expressions"
source_file: abenmesh_table_expressions_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Using Mesh Paths > Meshes - Mesh Path Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Meshes - Mesh Path Expressions

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how mesh paths can be used as standalone expressions.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_mesh_exprssns_flights DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    TYPES: 
      t_scarr    TYPE HASHED TABLE OF scarr 
                 WITH UNIQUE KEY carrid, 
      t_spfli    TYPE HASHED TABLE OF spfli 
                 WITH UNIQUE KEY carrid connid , 
      t_sflight  TYPE HASHED TABLE OF sflight 
                 WITH UNIQUE KEY carrid connid fldate, 
      t_sairport TYPE HASHED TABLE OF sairport 
                 WITH UNIQUE KEY id, 
      BEGIN OF MESH t_flights, 
        scarr    TYPE t_scarr 
          ASSOCIATION _spfli TO spfli 
                   ON carrid = carrid, 
        spfli    TYPE t_spfli 
          ASSOCIATION _sflight TO sflight 
                   ON carrid = carrid AND 
                      connid = connid 
          ASSOCIATION _sairport TO sairport 
                   ON id = airpfrom, 
        sflight  TYPE t_sflight, 
        sairport TYPE t_sairport, 
      END OF MESH t_flights. 
    DATA: 
      flights    TYPE t_flights, 
      in         TYPE REF TO if_demo_input, 
      name       TYPE scarr-carrname VALUE 'Lufthansa', 
      id         TYPE spfli-carrid   VALUE 'LH', 
      connection TYPE spfli-connid   VALUE '0400', 
      date       TYPE sflight-fldate. 
    METHODS: 
      input. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_mesh_exprssns_flights IMPLEMENTATION. 
  METHOD main. 
    input( ). 
 
    TRY. 
 
        out->begin_section( 
          'Forward Association scarr\_spfli' ). 
        FINAL(spfli_wa) = 
          flights-scarr\_spfli[ flights-scarr[ carrname = name ] 
                                  connid = connection ]. 
        out->write( spfli_wa ). 
 
        out->next_section( 
          'Inverse Association spfli\^_spfli~scarr' ). 
        FINAL(scarr_wa) = 
          flights-spfli\^_spfli~scarr[ 
            flights-spfli[ carrid = id connid = connection ] ]. 
        out->write( scarr_wa ). 
 
        out->next_section( 
          'Chained Association scarr\_spfli\_sflight' ). 
        FINAL(sflight_wa) = 
          flights-scarr\_spfli[ flights-scarr[ carrname = name ] 
                                  connid = connection 
                                ]\_sflight[ fldate = date ]. 
        out->write( sflight_wa ). 
 
        out->next_section( 
          'Addressing Component' ). 
        FINAL(price) = 
          flights-scarr\_spfli[ flights-scarr[ carrname = name ] 
                                  connid = connection 
                                ]\_sflight[ fldate = date ]-price. 
        out->write( price ). 
 
        out->next_section( 
          'Assigning to Field Symbol' ). 
        ASSIGN 
          flights-scarr\_spfli[ flights-scarr[ carrname = name ] 
                                  connid = connection 
                                ]\_sflight[ fldate = date ] 
          TO FIELD-SYMBOL(<sflight_wa>). 
        IF sy-subrc = 0. 
          out->write( 'Field symbol OK' ). 
        ENDIF. 
 
        out->next_section( 
          'Write Access and Check Existence' ). 
        flights-scarr\_spfli[ flights-scarr[ carrname = name ] 
                                connid = connection 
                              ]\_sflight[ fldate = date 
                              ]-price = price - 10. 
        IF line_exists( 
          flights-scarr\_spfli[ flights-scarr[ carrname = name ] 
                                  connid = connection 
                                ]\_sflight[ fldate = date 
                                              price = price - 10 ] ). 
          out->write( 'Line found!' ). 
        ENDIF. 
      CATCH cx_sy_itab_line_not_found. 
        out->write( 'Exception!' ). 
    ENDTRY. 
  ENDMETHOD. 
  METHOD input. 
    TRY. 
        date = flights-sflight[ carrid = id 
                                connid = connection ]-fldate. 
      CATCH cx_sy_itab_line_not_found. 
        RETURN. 
    ENDTRY. 
    in->add_field( CHANGING  field = name 
     )->add_field( CHANGING  field = connection 
     )->add_field( CHANGING  field = id 
     )->add_field( CHANGING  field = date 
     )->request( ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
 
    in  = cl_demo_input=>new( ). 
 
    SELECT * 
           FROM scarr 
           INTO TABLE @flights-scarr. 
    SELECT * 
           FROM spfli 
           INTO TABLE @flights-spfli. 
    SELECT * 
           FROM sflight 
           INTO TABLE @flights-sflight. 
    SELECT * 
           FROM sairport 
           INTO TABLE @flights-sairport. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The following mesh paths are used as mesh path expressions:

- Mesh path with forward association as an initial mesh association on the right side of an assignment. The source in the square brackets is a table expression supplemented by a condition.

  `flights-scarr\_spfli[ flights-scarr[ carrname = name ] connid = connection ]`

- Mesh path with mesh inverse association as an initial mesh association on the right side of an assignment. The source in the square brackets is a table expression.

  `flights-spfli\^_spfli~scarr[ flights-spfli[ carrid = ID connid = CONNECTION ] ]`

- Mesh path with path extension after the initial mesh association on the right side of an assignment.

  `flights-scarr\_spfli[ flights-scarr[ carrname = name ] connid = connection ]\_sflight[ fldate = date ]`

The mesh path with path extension is also used to demonstrate the addressing of a component using the structure component selector, assignments to a field symbol, write access, and usage in the predicate function `line_exists`.
