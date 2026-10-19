---
title: "Meshes - FOR Expressions for Mesh Paths"
source_file: abenmesh_for_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Using Mesh Paths > FOR ... IN mesh_path"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Meshes - FOR Expressions for Mesh Paths

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates table comprehensions and table reductions for mesh paths.

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
CLASS cl_demo_mesh_for_flights DEFINITION 
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
CLASS cl_demo_mesh_for_flights IMPLEMENTATION. 
  METHOD main. 
    input( ). 
 
    TRY. 
 
        out->begin_section( 
          'Initial Association SCARR\_spfli' ). 
        DATA(spfli_tab) = VALUE t_spfli( 
          FOR spfli_wa IN 
            flights-scarr\_spfli[ flights-scarr[ carrname = name ] 
                                    WHERE countryto = country ] 
             ( spfli_wa ) ). 
        out->write( spfli_tab ). 
        FINAL(distance) = REDUCE spfli-distance( 
          INIT d TYPE spfli-distance 
          FOR spfli_wa IN 
            flights-scarr\_spfli[ flights-scarr[ carrname = name ] 
                                    WHERE countryto = country ] 
             NEXT d += SWITCH spfli-distance( spfli_wa-distid 
                                WHEN 'KM' 
                                  THEN spfli_wa-distance * '1.60934' 
                                WHEN 'MI' 
                                  THEN spfli_wa-distance 
                                ELSE 0 ) ). 
        out->write( |Sum of distances in miles: { distance }| ). 
 
        out->next_section( 
          'Chained Association SCARR\_spfli\_sairport' ). 
        FINAL(sairport_tab) = VALUE t_sairport( 
          FOR sairport_wa IN 
            flights-scarr\_spfli[ flights-scarr[ carrname = name ] 
                                    WHERE countryto = country 
                                   ]\_sairport[ 
                                     USING KEY primary_key ] 
            ( sairport_wa ) ). 
        out->write( sairport_tab ). 
 
        out->next_section( 
          'Chained Association' && 
          ' SCARR\_spfli\_sflight\^_sflight~spfli' ). 
        spfli_tab = VALUE t_spfli( 
          FOR spfli_wa IN 
            flights-scarr\_spfli[ flights-scarr[ carrname = name ] 
                                    WHERE countryto = country 
                                  ]\_sflight[ 
                                    WHERE planetype = plane1 OR 
                                          planetype = plane2 
                                  ]\^_sflight~spfli[ ] 
             ( spfli_wa ) ). 
        out->write( spfli_tab ). 
 
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

This example uses the same mesh paths as the executable example for [`LOOP AT`](abenmesh_loops_abexa.md) and thus produces the same result sets. Unlike [`LOOP AT`](abenmesh_loop.md), the lines in the result set are produced in a results table using [table comprehensions](../../abap-glossary/abentable_comprehension_glosry.md) and not as individual lines.

For the first mesh path, a [table reduction](../../abap-glossary/abentable_reduction_glosry.md) is also performed using the reduction operator [`REDUCE`](../abap-program-flow-logic/abenconstructor_expression_reduce.md). This totals the distances, with the conversion from kilometers to miles using a [`SWITCH`](../abap-program-flow-logic/abenconditional_expression_switch.md) expression.
