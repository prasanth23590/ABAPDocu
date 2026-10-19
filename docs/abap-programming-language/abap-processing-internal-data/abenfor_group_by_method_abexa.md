---
title: "itab - Grouping with FOR Using a Method"
source_file: abenfor_group_by_method_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations > itab - Examples of Grouping with FOR"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping with FOR Using a Method

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the construction of the group key using the assignment of return values.

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
CLASS cl_demo_for_grps_by_method DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    TYPES: 
      spfli_tab    TYPE STANDARD TABLE OF spfli    WITH EMPTY KEY, 
      sairport_tab TYPE STANDARD TABLE OF sairport WITH EMPTY KEY. 
    DATA: 
      flights  TYPE spfli_tab, 
      airports TYPE sairport_tab. 
    METHODS 
      get_time_zone IMPORTING id               TYPE sairport-id 
                    RETURNING VALUE(time_zone) TYPE sairport-time_zone. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_for_grps_by_method IMPLEMENTATION. 
  METHOD main. 
    TYPES ot TYPE REF TO if_demo_output. 
 
    out = REDUCE #( 
      INIT ol TYPE ot 
      FOR GROUPS <group> OF wa IN flights 
            GROUP BY ( tz_from = get_time_zone( wa-airpfrom ) 
                       tz_to   = get_time_zone( wa-airpto ) 
                       size    = GROUP SIZE index = GROUP INDEX ) 
      LET members = VALUE spfli_tab( 
                      FOR <member> IN GROUP <group> ( <member> ) ) IN 
      NEXT ol = out->write( name = `Group key` 
                           data = <group> 
               )->write( members )->line( ) ). 
 
  ENDMETHOD. 
  METHOD get_time_zone. 
    TRY. 
        time_zone = airports[ id = id ]-time_zone. 
      CATCH cx_sy_itab_line_not_found. 
        time_zone = 'ERROR'. 
    ENDTRY. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    SELECT * FROM spfli    INTO TABLE @flights. 
    SELECT * FROM sairport INTO TABLE @airports. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example works in the same way as the corresponding [executable example](abenloop_group_by_method_abexa.md) for [`LOOP AT ... GROUP BY`](abaploop_at_itab_group_by.md), but uses the expression [`FOR GROUPS ... OF`](abenfor_groups_of.md) for a [table reduction](../../abap-glossary/abentable_reduction_glosry.md) with [`REDUCE`](../abap-program-flow-logic/abenconstructor_expression_reduce.md) instead of the [group loop](../../abap-glossary/abengroup_loop_glosry.md). In both cases, the group key after `GROUP BY` is constructed in exactly the same way.

The result of the table reduction is a reference to an object of the class `CL_DEMO_OUTPUT` to which the results of the grouping are written. The group members are written to a local auxiliary table `members` using a [table comprehension](../../abap-glossary/abentable_comprehension_glosry.md) with [`VALUE`](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md). This table comprehension could also be used in the [executable example](abenloop_group_by_method_abexa.md) for `LOOP AT ... GROUP BY` instead of the [member loop](../../abap-glossary/abenmember_loop_glosry.md).
