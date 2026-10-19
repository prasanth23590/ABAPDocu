---
title: "SELECT, Hierarchy Generator, BULK vs. INCREMENTAL"
source_file: abenselect_hierarchy_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy > SELECT, FROM HIERARCHY > SELECT, FROM HIERARCHY, CHILD TO PARENT ASSOCIATION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Hierarchy Generator, BULK vs. INCREMENTAL

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how the addition [`LOAD INCREMENTAL`](abenselect_hierarchy_generator.md) can speed up the generation of a hierarchy.

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
CLASS cl_demo_hrrchy_bulk_increment DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    DATA: 
      all_lines   TYPE i VALUE 100000, 
      hiera_lines TYPE i VALUE 10, 
      start_node  TYPE demo_guid_hiera-id. 
    METHODS fill_table. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_hrrchy_bulk_increment IMPLEMENTATION. 
  METHOD main. 
    cl_demo_input=>new( 
      )->add_field( CHANGING field = all_lines 
      )->add_field( CHANGING field = hiera_lines 
      )->request( ). 
    IF all_lines < 10 OR hiera_lines > all_lines. 
      out->write( 
        |ALL_LINES mus be at least 10\n| && 
        |HIERA_LINES cannot be greater than ALL_LINES| ). 
      RETURN. 
    ENDIF. 
 
    fill_table( ). 
 
    SELECT FROM HIERARCHY( SOURCE demo_cds_guid_hiera_source 
                           CHILD TO PARENT ASSOCIATION _relat 
                           START WHERE id = @start_node 
                           SIBLINGS ORDER BY id 
                           LOAD BULK ) 
           FIELDS id, 
                  parent, 
                  field 
           INTO TABLE @DATA(bulk_result). 
 
    FINAL(t1_bulk) = utclong_current( ). 
    DO 10 TIMES. 
      SELECT FROM HIERARCHY( SOURCE demo_cds_guid_hiera_source 
                             CHILD TO PARENT ASSOCIATION _relat 
                             START WHERE id = @start_node 
                             SIBLINGS ORDER BY id 
                             LOAD BULK ) 
             FIELDS id, 
                    parent, 
                    field 
             INTO TABLE @bulk_result. 
    ENDDO. 
    FINAL(t2_bulk) = utclong_current( ). 
 
    SELECT FROM HIERARCHY( SOURCE demo_cds_guid_hiera_source 
                           CHILD TO PARENT ASSOCIATION _relat 
                           START WHERE id = @start_node 
                           SIBLINGS ORDER BY id 
                           LOAD INCREMENTAL ) 
           FIELDS id, 
                  parent, 
                  field 
           INTO TABLE @DATA(inc_result). 
    FINAL(t1_inc) = utclong_current( ). 
    DO 10 TIMES. 
      SELECT FROM HIERARCHY( SOURCE demo_cds_guid_hiera_source 
                             CHILD TO PARENT ASSOCIATION _relat 
                             START WHERE id = @start_node 
                             SIBLINGS ORDER BY id 
                             LOAD INCREMENTAL ) 
             FIELDS id, 
                    parent, 
                    field 
             INTO TABLE @inc_result. 
    ENDDO. 
    FINAL(t2_inc) = utclong_current( ). 
 
    ASSERT inc_result = bulk_result. 
 
    cl_abap_utclong=>diff( EXPORTING high  = t2_bulk 
                                     low   = t1_bulk 
                           IMPORTING seconds = DATA(tdelta1) ). 
 
    cl_abap_utclong=>diff( EXPORTING high  = t2_inc 
                                     low   = t1_inc 
                          IMPORTING seconds = DATA(tdelta2) ). 
 
    FINAL(factor) = tdelta1 / tdelta2. 
 
    out->write( inc_result 
      )->write( 
        |Bulk time/Incremental time: { factor DECIMALS = 2 }| ). 
  ENDMETHOD. 
  METHOD fill_table. 
    DELETE FROM demo_guid_hiera.                        "#EC CI_NOWHERE 
 
    TRY. 
        INSERT demo_guid_hiera FROM TABLE @( 
          VALUE #( FOR i = 1 UNTIL i > all_lines 
            LET uuid1 = cl_system_uuid=>create_uuid_x16_static( ) 
                uuid2 = cl_system_uuid=>create_uuid_x16_static( ) IN 
            ( id        = uuid1 
              parent_id = uuid2 
              field = uuid1 && '-' && uuid2 ) ) ). 
      CATCH cx_uuid_error. 
        RETURN. 
    ENDTRY. 
 
    FINAL(rnd) = cl_abap_random_int=>create( 
      seed = + cl_demo_date_time=>get_system_time( ) 
      min  = 1 
      max  = all_lines ). 
    DATA lines TYPE TABLE OF i. 
    DO. 
      FINAL(line) = rnd->get_next( ). 
      IF NOT line_exists( lines[ table_line = line ] ). 
        lines = VALUE #( BASE lines ( line ) ). 
        IF lines( lines ) = hiera_lines. 
          EXIT. 
        ENDIF. 
      ELSE. 
        CONTINUE. 
      ENDIF. 
    ENDDO. 
 
    LOOP AT lines ASSIGNING FIELD-SYMBOL(<line>). 
      FINAL(idx) = sy-tabix. 
      SELECT id FROM demo_guid_hiera 
             ORDER BY id 
             INTO @FINAL(node) 
             OFFSET @<line> UP TO 1 ROWS. 
      ENDSELECT. 
      IF idx = 1. 
        start_node = node. 
        DATA(parent_node) = node. 
      ELSE. 
        UPDATE demo_guid_hiera SET parent_id = @parent_node 
               WHERE id = @node. 
        parent_node = node. 
      ENDIF. 
    ENDLOOP. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The table `DEMO_GUID_HIERA` serves as data source for a hierarchy. The user can enter how many rows in total are inserted, and how many of them are part of the hierarchy. Then, the table is filled with GUIDs and the rows that build a hierarchy tree are chosen randomly.

Based on this table, a hierarchy is generated, once with the addition `LOAD BULK` and once with `LOAD INCREMENTAL`. The time of hierarchy generation, which is done in `DO`-loops with 10 repetitions, is measured and compared.

When using the default values for the formal parameters, `LOAD INCREMENTAL` is many times faster than `LOAD BULK`. This positive effect is minimized when the total number of rows is decreased and the number of rows that are part of the hierarchy is increased.
