---
title: "SELECT, Restriction of the Rows in the Result Set"
source_file: abenselect_up_to_offset_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, UP TO, OFFSET"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Restriction of the Rows in the Result Set

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the additions [`UP TO` and `OFFSET`](abapselect_up_to_offset.md) of the statement [`SELECT`](abapselect.md).

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
CLASS cl_demo_select_up_to_offset DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    DATA: 
      o TYPE int8, 
      n TYPE int8. 
    METHODS 
      setup. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_up_to_offset IMPLEMENTATION. 
  METHOD main. 
    setup( ). 
 
    SELECT FROM demo_expressions 
           FIELDS id, num1 AS number, numlong1 AS result 
           ORDER BY id, num1 
           INTO TABLE @FINAL(itab) 
           OFFSET @o 
           UP TO @n ROWS. 
 
    out->write( itab ). 
 
    DELETE FROM demo_expressions.                       "#EC CI_NOWHERE 
  ENDMETHOD. 
  METHOD setup. 
    cl_demo_input=>new( 
       )->add_field( CHANGING field = o 
       )->request(   CHANGING field = n ). 
    IF NOT ( ( o BETWEEN 0 AND 2147483646 ) AND 
             ( n BETWEEN 0 AND 2147483646 ) ). 
      out->write( 
        `Input not in allowed interval!` ). 
      RETURN. 
    ENDIF. 
 
    DELETE FROM demo_expressions.                       "#EC CI_NOWHERE 
    FINAL(abcde) = 'abcdefghijklmnopqrstuvwxyz'. 
    DO strlen( abcde ) TIMES. 
      INSERT demo_expressions FROM @( 
        VALUE #( id       = substring( val = abcde 
                                       off = sy-index - 1 
                                       len = 1 ) 
                 num1     = sy-index 
                 numlong1 = ipow( base = 2 exp = sy-index ) ) ). 
    ENDDO. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

An offset and a maximum number of rows can be entered for the result set of a `SELECT` statement.
