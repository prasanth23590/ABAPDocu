---
title: "Meshes - Loops Across Mesh Paths"
source_file: abenmesh_loops_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Using Mesh Paths > LOOP AT mesh_path"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Meshes - Loops Across Mesh Paths

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates loops across mesh paths.

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
CLASS cl_demo_mesh_loop_at_flights DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor . 
 
  PRIVATE SECTION. 
    TYPES: 
      t_scarr    TYPE HASHED TABLE OF scarr 
                 WITH UNIQUE KEY carrid, 
      t_spfli    TYPE HASHED TABLE OF spfli 
                 WITH UNIQUE KEY carrid connid 
                 WITH NON-UNIQUE SORTED KEY carrid 
                                 COMPONENTS carrid, 
      t_sflight  TYPE HASHED TABLE OF sflight 
                 WITH UNIQUE KEY carrid connid fldate 
                 WITH NON-UNIQUE SORTED KEY carrid_connid 
                                 COMPONENTS carrid connid, 
      t_sairport TYPE HASHED TABLE OF sairport 
                 WITH UNIQUE KEY id, 
      BEGIN OF MESH t_flights, 
        scarr    TYPE t_scarr 
          ASSOCIATION _spfli TO spfli 
                   ON carrid = carrid USING KEY carrid, 
        spfli    TYPE t_spfli 
          ASSOCIATION _sflight TO sflight 
                   ON carrid = carrid AND 
                      connid = connid USING KEY carrid_connid 
          ASSOCIATION _sairport TO sairport 
                   ON id = airpfrom, 
        sflight  TYPE t_sflight, 
        sairport TYPE t_sairport, 
      END OF MESH t_flights. 
    DATA: 
      flights TYPE t_flights, 
      in      TYPE REF TO if_demo_input, 
      o       TYPE REF TO if_demo_output, 
      name    TYPE scarr-carrname VALUE 'United Airlines', 
      country TYPE spfli-countryto VALUE 'US', 
      plane1  TYPE sflight-planetype VALUE '747-400', 
      plane2  TYPE sflight-planetype VALUE 'A310-300'. 
    METHODS: 
      input. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_mesh_loop_at_flights IMPLEMENTATION. 
  METHOD main. 
    input( ). 
 
    TRY. 
        out->begin_section( 
          'Initial Association SCARR\_spfli' ). 
        LOOP AT 
          flights-scarr\_spfli[ flights-scarr[ carrname = name ] 
                                  WHERE countryto = country  ] 
             INTO FINAL(spfli_wa). 
          out->write( spfli_wa ). 
        ENDLOOP. 
 
        out->next_section( 
          'Chained Association SCARR\_spfli\_sairport' ). 
        LOOP AT 
          flights-scarr\_spfli[ flights-scarr[ carrname = name ] 
                                  WHERE countryto = country 
                                ]\_sairport[ USING KEY primary_key ] 
             INTO FINAL(sairport_wa). 
          out->write( sairport_wa ). 
        ENDLOOP. 
 
        out->next_section( 
          'Chained Association' && 
          ' SCARR\_spfli\_sflight\^_sflight~spfli' ). 
        LOOP AT 
          flights-scarr\_spfli[ flights-scarr[ carrname = name ] 
                                  WHERE countryto = country 
                                ]\_sflight[ 
                                  WHERE planetype = plane1 OR 
                                        planetype = plane2 
                                ]\^_sflight~spfli[ ] 
             ASSIGNING FIELD-SYMBOL(<spfli_wa>). 
          out->write( <spfli_wa> ). 
        ENDLOOP. 
 
      CATCH cx_sy_itab_line_not_found. 
        out->write( 'Exception!' ). 
    ENDTRY. 
  ENDMETHOD. 
  METHOD input. 
    in->add_field( CHANGING field = name 
     )->add_field( CHANGING field = country 
     )->add_field( CHANGING field = plane1 
     )->add_field( CHANGING field = plane2 
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

Loops are performed across the following mesh paths:

- Mesh path with forward association as its initial mesh association. The source in the square brackets is a table expression, supplemented by a `WHERE` condition.

  `flights-scarr\_spfli[ flights-scarr[ carrname = name ] WHERE countryto = country ]` The result set consists of all lines of the node `spfli` that meet the condition.

- Mesh path with forward associations as its initial mesh association and path extension. The source in the square brackets of the initial mesh association is a table expression, supplemented by a `WHERE` condition. A key is specified in the square brackets of the path extension for evaluating the mesh association.

  `flights-scarr\_spfli[ flights-scarr[ carrname = name ] WHERE countryto = country ]\_sairport[ USING KEY primary_key ]` The result set consists of all lines of the node `sairport` that match the column `airpfrom` in the result set of the entry node `spfli`. Duplicate lines are removed automatically.

- Mesh path with forward associations as its initial mesh association and two path extensions. The last path extension is an inverse mesh association that leads back to the entry node.

  `flights-scarr\_spfli[ flights-scarr[ carrname = name ] WHERE countryto = country ]\_sflight[ WHERE planetype = plane1 OR planetype = plane2 ]\^_sflight~spfli[ ]` The result set consists of all lines of the node `spfli` for which the lines in the result set of `sflight` have specific values in the column `plane_type`.

See also the executable example for [table comprehensions for meshes](abenmesh_for_abexa.md).
