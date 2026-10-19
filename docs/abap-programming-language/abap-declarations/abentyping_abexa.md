---
title: "Generic Typing and Complete Typing"
source_file: abentyping_abexa.html
section: "ABAP Programming Language > ABAP - Declarations > Typing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Generic Typing and Complete Typing

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how generically and completely typed formal parameters are accessed.

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
CLASS cl_demo_typing DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    TYPES: BEGIN OF struc1, 
             cola TYPE i, 
             colb TYPE i, 
           END OF struc1, 
           BEGIN OF struc2, 
             colb TYPE i, 
             cola TYPE i, 
           END OF struc2, 
           itab1g TYPE STANDARD TABLE OF struc1, 
           itab2g TYPE STANDARD TABLE OF struc2, 
           itab2c TYPE STANDARD TABLE OF struc2 
                       WITH NON-UNIQUE DEFAULT KEY. 
    METHODS sort_itab IMPORTING VALUE(pg) TYPE itab2g 
                                VALUE(pc) TYPE itab2c. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_typing IMPLEMENTATION. 
  METHOD main. 
 
    DATA: tab TYPE itab1g, 
          wa  LIKE LINE OF tab. 
    tab = VALUE #( 
      FOR j = 1 UNTIL j > 5 
        ( cola = j colb = 6 - j ) ). 
    sort_itab( pg = tab 
               pc = tab ). 
  ENDMETHOD. 
  METHOD sort_itab. 
    SORT pg BY cola. 
    out->write_data( pg ). 
    SORT pg BY ('COLA'). 
    out->write_data( pg ). 
    SORT pc BY cola. 
    out->write_data( pc ). 
    SORT pc BY ('COLA'). 
    out->write_data( pc ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Three table types are declared in the class `demo_typing`:

- `itab1g` has the line type `struc1` with the components `cola` and `colb`. It is generic since the primary table key is not specified.

- `itab2g` has the line type `struc2` with the components `colb` and `cola`. It is generic since the primary table key is not specified.

- `itab2c` has the line type `struc2` with the components `cola` and `colb`. It is complete since the primary table key is specified.

The method `sort_itab` has two formal parameters:

- `pg` is typed generically with `itab2g`.

- `pc` is typed completely with `itab2c`.

In the method `start`, an internal table `tab` is declared with reference to `itab1g`. The key specification is added implicitly. This table is filled and passed to the formal parameters of `sort_itab`.

In `sort_itab`, both formal parameters are sorted twice. In the first sort, the column `cola` is specified statically and dynamically in the second sort as a sort criterion. The behavior is as follows:

- The first `SORT` statement accesses the generically typed formal parameter `pg` statically. In this case, the typing with `itab2g` takes place, where `cola` is the second column.

- The second `SORT` statement accesses the generically typed formal parameter `pg` dynamically. In this case, the type of the actual parameter `itab1g` takes place, where `cola` is the first column.

- The third and fourth `SORT` statements access the completely typed formal parameter `pc` dynamically or statically. In these cases, the typing with `itab2c` takes place, where `cola` is the second column.

If components of generically typed formal parameters are accessed dynamically, a runtime error can also occur if the components do not exist in the actual parameter.
