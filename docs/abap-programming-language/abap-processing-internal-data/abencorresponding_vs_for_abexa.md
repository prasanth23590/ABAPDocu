---
title: "Component Operator, Comparison with FOR Expression"
source_file: abencorresponding_vs_for_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > Assigning Components, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Component Operator, Comparison with FOR Expression

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example compares the [component operator](abenconstructor_expr_corresponding.md) with [table comprehensions](../../abap-glossary/abentable_comprehension_glosry.md),

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
CLASS cl_demo_crrspndng_vs_for DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor . 
 
  PRIVATE SECTION. 
    TYPES: 
      BEGIN OF struct, 
        carrier     TYPE spfli-carrid, 
        connection  TYPE spfli-connid, 
        departure   TYPE spfli-cityfrom, 
        destination TYPE spfli-cityto, 
      END OF struct. 
    DATA: 
      itab    TYPE HASHED TABLE OF spfli 
              WITH UNIQUE KEY carrid connid, 
      result1 TYPE HASHED TABLE OF struct 
              WITH UNIQUE KEY carrier connection, 
      result2 TYPE HASHED TABLE OF struct 
              WITH UNIQUE KEY carrier connection, 
      result3 TYPE HASHED TABLE OF struct 
              WITH UNIQUE KEY carrier connection. 
    CONSTANTS iterations TYPE i VALUE 1000. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_crrspndng_vs_for IMPLEMENTATION. 
  METHOD main. 
 
    DO iterations TIMES. 
 
      DATA t1 TYPE decfloat34. 
      FINAL(t11) = utclong_current( ). 
      result1 = CORRESPONDING #( 
                 itab MAPPING carrier     = carrid 
                              connection  = connid 
                              departure   = cityfrom 
                              destination = cityto ). 
      FINAL(t12) = utclong_current( ). 
 
      cl_abap_utclong=>diff( EXPORTING high    = t12 
                                       low   = t11 
                           IMPORTING seconds = DATA(t13) ). 
 
      t1 += t13. 
 
      DATA t2 TYPE decfloat34. 
      FINAL(t21) = utclong_current( ). 
      result2 = VALUE #( FOR wa IN itab ( carrier     = wa-carrid 
                                          connection  = wa-connid 
                                          departure   = wa-cityfrom 
                                          destination = wa-cityto ) ). 
      FINAL(t22) = utclong_current( ). 
      cl_abap_utclong=>diff( EXPORTING high    = t22 
                                       low   = t21 
                           IMPORTING seconds = DATA(t23) ). 
      t2 += t23. 
 
      DATA t3 TYPE decfloat34. 
      FINAL(t31) = utclong_current( ). 
      result3 = VALUE #( FOR wa IN itab ( 
                           CORRESPONDING #( 
                             wa MAPPING carrier     = carrid 
                                        connection  = connid 
                                        departure   = cityfrom 
                                        destination = cityto ) ) ). 
      FINAL(t32) = utclong_current( ). 
      cl_abap_utclong=>diff( EXPORTING high    = t32 
                                      low   = t31 
                          IMPORTING seconds = DATA(t33) ). 
      t3 += t33. 
 
    ENDDO. 
 
    IF result1 = result2 AND result1 = result3. 
      out->write( 
       |CORRESPONDING:     { 
          t1 / iterations 
              WIDTH = 10 ALIGN = RIGHT }\n| && 
       |FOR:               { 
          t2 / iterations 
              WIDTH = 10 ALIGN = RIGHT }\n| && 
       |FOR CORRESPONDING: { 
         t3 / iterations 
              WIDTH = 10 ALIGN = RIGHT }\n| 
      )->line( 
      )->write( result1 ). 
    ELSE. 
      out->write( `What?` ). 
    ENDIF. 
 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
 
    SELECT * 
           FROM spfli 
           INTO TABLE @itab. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The columns of an internal table can be assigned to columns with different names in a different table in three different ways:

- Constructor expression with component operator `CORRESPONDING` and mapping rule

- Explicit assignment of the individual components behind a `FOR` expression of a table comprehension.

- `FOR` expression with evaluation of a constructor expression with component operator for each line.

Each method provides the same results. The component operator is quicker than the table comprehension when there are more than approximately 10 iterations. Using the component operator for each line is always the slowest solution.
