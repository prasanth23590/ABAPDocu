---
title: "itab - Grouping with FOR in Packages"
source_file: abenfor_group_by_packages_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations > itab - Examples of Grouping with FOR"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping with FOR in Packages

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a construction of the group key that does not depend on the line content.

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
CLASS cl_demo_for_grps_by_packages DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    TYPES 
      i_tab TYPE STANDARD TABLE OF decfloat34 WITH EMPTY KEY. 
    DATA: 
      itab TYPE i_tab, 
      n    TYPE i VALUE 10, 
      idx  TYPE i. 
    METHODS 
      group RETURNING VALUE(group_key) TYPE i. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_for_grps_by_packages IMPLEMENTATION. 
  METHOD main. 
    TYPES ot TYPE REF TO if_demo_output. 
 
    cl_demo_input=>new( 
      )->request( EXPORTING text  = `Package size` 
                  CHANGING  field = n ). 
    IF n <= 0. 
      RETURN. 
    ENDIF. 
 
    out->begin_section( |Packages of { n }| ). 
 
    out = REDUCE #( 
      INIT ol TYPE ot 
      FOR GROUPS OF wa IN itab GROUP BY group( ) 
      LET group = VALUE i_tab( FOR <wa> IN GROUP wa ( <wa> ) ) IN 
      NEXT ol = out->write( group ) ). 
 
  ENDMETHOD. 
  METHOD group. 
    idx += 1. 
    group_key = ( idx - 1 ) DIV n + 1. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    itab = VALUE #( FOR j = 1 UNTIL j > 100 ( 1 / j ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example works in the same way as the corresponding [executable example](abenloop_group_by_packages_abexa.md) for [`LOOP AT ... GROUP BY`](abaploop_at_itab_group_by.md), but uses the expression [`FOR GROUPS ... OF`](abenfor_groups_of.md) for a [table reduction](../../abap-glossary/abentable_reduction_glosry.md) with [`REDUCE`](../abap-program-flow-logic/abenconstructor_expression_reduce.md) instead of the [group loop](../../abap-glossary/abengroup_loop_glosry.md). The group key after `GROUP BY` cannot be constructed in the same way in this case, since the system field `sy-tabix` is not available during grouping in expressions. The addition `INDEX INTO` cannot be used either, since it sets a value for each group but not for each evaluated line. This is why a user-defined method, `group`, is called here to count the lines.

The result of the table reduction is a reference to an object of the class `CL_DEMO_OUTPUT` to which the results of the grouping are written. The group members are written to a local auxiliary table `members` using a [table comprehension](../../abap-glossary/abentable_comprehension_glosry.md) with [`VALUE`](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md). This table comprehension could also be used in the [executable example](abenloop_group_by_overlap_abexa.md) for `LOOP AT ... GROUP BY` instead of the [member loop](../../abap-glossary/abenmember_loop_glosry.md).
