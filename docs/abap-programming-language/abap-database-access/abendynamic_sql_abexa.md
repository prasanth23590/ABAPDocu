---
title: "SELECT, Dynamic Token Specification"
source_file: abendynamic_sql_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Dynamic Token Specification

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how tokens are specified dynamically in ABAP SQL for the statement [`SELECT`](abapselect.md).

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
CLASS cl_demo_dynamic_sql DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_dynamic_sql IMPLEMENTATION. 
  METHOD main. 
 
    CONSTANTS left TYPE tabname VALUE 'SFLIGHT'. 
 
    TYPES include_list TYPE HASHED TABLE OF string 
                       WITH UNIQUE KEY table_line. 
 
    TYPES editor_line TYPE c LENGTH 72. 
 
    DATA: right    TYPE tabname VALUE 'SPFLI', 
          select   TYPE TABLE OF editor_line, 
          sublist  TYPE editor_line, 
          from     TYPE string, 
          first_on TYPE abap_bool VALUE abap_true, 
          tref     TYPE REF TO data. 
 
    cl_demo_input=>new( )->request( 
      EXPORTING text  = `Right Table of Join` 
      CHANGING  field = right ). 
 
    FINAL(include_list) = VALUE include_list( ( `SPFLI` ) 
                                              ( `SCARR` ) 
                                              ( `SAPLANE` ) ). 
 
    TRY. 
        right = cl_abap_dyn_prg=>check_whitelist_tab( 
                  val = to_upper( right ) 
                  whitelist = include_list ). 
      CATCH cx_abap_not_in_whitelist. 
        out->write( 
          `Only the following tables are allowed:` ). 
        out->write( include_list ). 
        RETURN. 
    ENDTRY. 
 
    first_on = abap_true. 
    CLEAR select. 
    CLEAR sublist. 
    CLEAR from. 
 
    DATA(comp_tab1) = 
      CAST cl_abap_structdescr( cl_abap_typedescr=>describe_by_name( 
                                  left ) )->get_components( ). 
    DATA(comp_tab2) = 
      CAST cl_abap_structdescr( cl_abap_typedescr=>describe_by_name( 
                                  right ) )->get_components( ). 
 
    DELETE comp_tab1 WHERE name = 'MANDT'. 
    DELETE comp_tab2 WHERE name = 'MANDT'. 
 
    from = left && ` join ` && right && ` on `. 
 
    LOOP AT comp_tab1 INTO DATA(comp1) WHERE name IS NOT INITIAL. 
      sublist = left && '~' && comp1-name && ','. 
      APPEND sublist TO select. 
    ENDLOOP. 
 
    LOOP AT comp_tab2 INTO FINAL(comp2) WHERE name IS NOT INITIAL. 
      TRY. 
          comp1 = comp_tab1[ KEY primary_key name = comp2-name ]. 
          IF first_on = abap_false. 
            from = from && ` and `. 
          ELSE. 
            first_on = abap_false. 
          ENDIF. 
          from = from && left  && `~` && comp2-name && 
                ` = ` && right && `~` && comp2-name. 
        CATCH cx_sy_itab_line_not_found. 
          APPEND comp2 TO comp_tab1. 
          sublist = right && '~' && comp2-name && ','. 
          APPEND sublist TO select. 
      ENDTRY. 
    ENDLOOP. 
 
    FINAL(struct_type) = cl_abap_structdescr=>create( comp_tab1 ). 
    FINAL(table_type) = cl_abap_tabledescr=>create( struct_type ). 
    CREATE DATA tref TYPE HANDLE table_type. 
 
    ASSIGN select[ lines( select ) ] TO FIELD-SYMBOL(<comp>). 
    REPLACE `,` IN <comp>  WITH ``. 
    TRY. 
        SELECT (select) FROM (from) INTO TABLE @tref->* UP TO 1000 ROWS. 
        out->write( tref->* ). 
      CATCH cx_sy_dynamic_osql_syntax 
            cx_sy_dynamic_osql_semantics INTO FINAL(exc). 
        out->write( exc->get_text( ) ). 
    ENDTRY. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

When executing the class, the name of one of the DDIC database tables `SPFLI`, `SCARR`, or `SAPLANE` can be entered. The table entered is then joined with the table `SFLIGHT` in accordance with its foreign key dependency. It is simply assumed that all fields with the same name have a foreign key relationship with each other.

The selected table name is assigned to the field `right`. The RTTS class `CL_ABAP_TYPEDESCR` is used to determine the type description for the columns in the left and right table of the join. The method `GET_COMPONENTS` is used to store these in two type description tables `comp_tab1` or `comp_tab2`, which contain an entry for each column of the respective DDIC database table.

Then, a fragment of the `FROM` clause is created, which contains the names of the tables to be joined; the `FROM` clause is later completed using the `ON` conditions.

All columns of the left table should be included in the `SELECT` list, as well as those columns of the right table for which no columns with the same name exist in the left table. The content of the type description tables is processed in loops.

Initially, the columns of the left table are processed. The current column is incorporated first into the dynamic `SELECT` list, which should be specified in the internal table `select`. The column name `comp1-name` is prefixed with the table name in `left`, to ensure its uniqueness. The statement `MOVE-CORRESPONDING` is used to copy the column description from `comp_tab1` to an internal table `comp_tab_join` whose type is suitable for creating objects later.

The columns of the right table are searched for in the left table. If the column `comp2-name` only exists in the right table, it is, for the time being, included in the type description table `comp_tab_join`. After that, it is added to all columns of the left table of the `SELECT` list `select`, just like before.

If the column in `comp2-name` exists in both tables, an `ON` condition that compares columns with the same name from the left and the right table, is added to the dynamic `FROM` clause `from`.

The type description table `comp_tab_join` and the static method `CREATE` of the class `CL_ABAP_STRUCTDESCR` can now be used to create a suitable type description object for the structure of the target area of the statement `SELECT`. This type description object could now be specified after the addition `TYPE HANDLE` of the statement `CREATE DATA` to create a structured work area. However, the next step uses the method `CREATE` of the class `CL_ABAP_TABLEDESCR` to create a type description object for an internal table of this row type and creates this table using `CREATE DATA`. The dynamically created internal tables can be used by dereferencing the anonymous data object with `tref->*` in operand positions.

The data is then read with a fully dynamic statement `SELECT`. The content of the anonymous internal table is displayed.

## Security Hint

If used incorrectly, dynamic programming techniques can present a serious security risk. Any dynamic content that is passed to a program from the outside must be checked thoroughly or escaped before it is used in dynamic statements. This can be done using the system class `CL_ABAP_DYN_PRG` or the built-in function [`escape`](../abap-processing-internal-data/abenescape_functions.md).
