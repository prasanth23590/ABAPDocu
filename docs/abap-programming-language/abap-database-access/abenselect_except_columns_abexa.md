---
title: "SELECT, Remove Columns from the SELECT List"
source_file: abenselect_except_columns_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, select_clause > SELECT, select_list"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Remove Columns from the SELECT List

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how all columns except some specific ones can be read with a dynamic token.

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
CLASS cl_demo_select_except_columns DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC FINAL. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* CCIMP 
CLASS select_list DEFINITION. 
  PUBLIC SECTION. 
    METHODS: 
    constructor IMPORTING dbtab TYPE string 
    except TYPE string, 
    get_token RETURNING VALUE(token) TYPE string, 
    get_target RETURNING VALUE(target) TYPE REF TO data. 
  PRIVATE SECTION. 
    DATA 
    components TYPE cl_abap_structdescr=>component_table. 
ENDCLASS. 
 
CLASS select_list IMPLEMENTATION. 
  METHOD constructor. 
    components = CAST cl_abap_structdescr( 
    cl_abap_typedescr=>describe_by_name( to_upper( dbtab ) ) 
    )->get_components( ). 
    SPLIT except AT `,` INTO TABLE FINAL(columns). 
    LOOP AT columns ASSIGNING FIELD-SYMBOL(<column>). 
      DELETE components WHERE name = to_upper( condense( <column> ) ). 
    ENDLOOP. 
  ENDMETHOD. 
  METHOD get_token. 
    token = 
    REDUCE string( INIT s = `` 
    FOR <wa> IN components 
    NEXT s &&= COND #( WHEN s = `` THEN <wa>-name 
    ELSE `, ` && <wa>-name ) ). 
  ENDMETHOD. 
  METHOD get_target. 
    FINAL(itab_type) = 
    cl_abap_tabledescr=>get( 
    p_line_type = cl_abap_structdescr=>get( 
    p_components = components ) 
    p_table_kind = cl_abap_tabledescr=>tablekind_std ). 
    CREATE DATA target TYPE HANDLE itab_type. 
  ENDMETHOD. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_except_columns IMPLEMENTATION. 
  METHOD main. 
    FINAL(sel_list) = NEW select_list( dbtab  = 'scarr' 
                                       except = 'carrid, url' ). 
 
    FINAL(token)  = sel_list->get_token( ). 
    FINAL(target) = sel_list->get_target( ). 
 
    SELECT (token) 
           FROM scarr 
           INTO TABLE @target->*. 
 
    out->write( target->* ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Using a helper class, a dynamic token and an appropriate target area are created, that enable the selection of all columns of a database table except a given list. This simple example omits the handling of possible exceptions and does not exclude the client column.
