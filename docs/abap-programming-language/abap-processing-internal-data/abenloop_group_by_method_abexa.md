---
title: "itab - Grouping with LOOP Using a Method"
source_file: abenloop_group_by_method_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, GROUP BY > Examples of Grouping with LOOP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping with LOOP Using a Method

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
CLASS cl_demo_loop_grp_by_method DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      flights  TYPE TABLE OF spfli    WITH EMPTY KEY, 
      airports TYPE TABLE OF sairport WITH EMPTY KEY. 
    METHODS 
      get_time_zone IMPORTING id               TYPE sairport-id 
                    RETURNING VALUE(time_zone) TYPE sairport-time_zone. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_loop_grp_by_method IMPLEMENTATION. 
  METHOD main. 
 
    DATA members LIKE flights. 
    LOOP AT flights INTO FINAL(wa) 
         GROUP BY ( tz_from = get_time_zone( wa-airpfrom ) 
                    tz_to   = get_time_zone( wa-airpto ) 
                    size = GROUP SIZE index = GROUP INDEX ) 
         ASSIGNING FIELD-SYMBOL(<group>). 
      out->write( name = `Group key` 
                  data = <group> ). 
      CLEAR members. 
      LOOP AT GROUP <group> ASSIGNING FIELD-SYMBOL(<member>). 
        members = VALUE #( BASE members ( <member> ) ). 
      ENDLOOP. 
      out->write( members )->line( ). 
    ENDLOOP. 
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

[Grouping](abaploop_at_itab_group_by.md) of an internal table `flights` with [group key binding](abaploop_at_itab_group_by_binding.md). The group key of the [group loop](../../abap-glossary/abengroup_loop_glosry.md) is constructed as a structure. The return values of the functional method `get_time_zone` are assigned to the components `tz_from` and `tz_to`. The values of the columns `airpfrom` or `airpto` are passed to the input parameter of the method. This creates groups of lines that have the same combinations of time zones for the departure and destination airport.

In the simple case shown here, the table expression from the method could of course also be specified directly:

``` abap
LOOP AT flights INTO DATA(wa) 
     GROUP BY ( tz_from = airports[ id = wa-airpfrom ]-time_zone 
                tz_to   = airports[ id = wa-airpto   ]-time_zone ) 
     ASSIGNING FIELD-SYMBOL(<group>).
```

Furthermore, the components `size` and `index` are created for the special language elements `GROUP SIZE` or `GROUP INDEX` to determine the size and index of each group.

The group key that is bound to a field symbol `<group>` and the additional components are produced in the group loop. In a [member loop](../../abap-glossary/abenmember_loop_glosry.md), the lines of each group are placed in an internal table `members` using the [value operator](../../abap-glossary/abenvalue_operator_glosry.md) with the addition [`BASE`](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md). This table is also displayed.

`members` could also be filled by evaluating a table comprehension using [`FOR ... IN GROUP`](abenfor_in_group.md), instead of in a [member loop](../../abap-glossary/abenmember_loop_glosry.md) [`LOOP AT GROUP`](abaploop_at_group.md):

`members = VALUE #( FOR <member> IN GROUP <group> ( <member> ) ).`

The executable example for [grouping with `FOR`](abenfor_group_by_method_abexa.md) demonstrates how the entire group loop can be implemented using expressions.
