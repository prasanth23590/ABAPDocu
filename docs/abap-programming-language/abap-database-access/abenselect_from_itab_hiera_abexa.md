---
title: "SELECT, Internal Table as a Data Source of the Hierarchy Generator"
source_file: abenselect_from_itab_hiera_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM @itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Internal Table as a Data Source of the Hierarchy Generator

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how an internal table is accessed in a common table expression with self association and how the table is used as a data source of the hierarchy generator.

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
CLASS cl_demo_select_from_itab_hiera DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    TYPES: 
      BEGIN OF parent_child, 
        cnt       TYPE i, 
        id        TYPE c LENGTH 2, 
        parent_id TYPE c LENGTH 2, 
      END OF parent_child. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_from_itab_hiera IMPLEMENTATION. 
  METHOD main. 
    DATA(start_id) = CONV  demo_parent_chld-id( 'A' ). 
    cl_demo_input=>new( )->request( CHANGING field = start_id ). 
 
    DATA parent_child_tab TYPE HASHED TABLE OF parent_child 
                          WITH UNIQUE KEY cnt. 
 
    parent_child_tab = VALUE #( 
            ( cnt = 1 id = 'A'  parent_id = ' ' ) 
            ( cnt = 2 id = 'B'  parent_id = 'A' ) 
            ( cnt = 3 id = 'C'  parent_id = 'A' ) 
            ( cnt = 4 id = 'D'  parent_id = 'C' ) 
            ( cnt = 5 id = 'D'  parent_id = 'B' ) 
            ( cnt = 6 id = 'D'  parent_id = 'A' ) ). 
 
    WITH 
      +parent_child_source AS 
         ( SELECT FROM @parent_child_tab AS parent_child_tab 
                  FIELDS id, 
                         parent_id AS parent ) 
            WITH ASSOCIATIONS ( 
              JOIN MANY TO MANY +parent_child_source AS _relat 
                ON +parent_child_source~parent = _relat~id ) 
      SELECT FROM HIERARCHY( SOURCE +parent_child_source 
                             CHILD TO PARENT ASSOCIATION _relat 
                             START WHERE id = @start_id 
                             SIBLINGS ORDER BY id 
                             MULTIPLE PARENTS ALLOWED ) 
             FIELDS id, 
                    parent, 
                    hierarchy_rank, 
                    hierarchy_tree_size, 
                    hierarchy_parent_rank, 
                    hierarchy_level, 
                    hierarchy_is_cycle, 
                    hierarchy_is_orphan, 
                    node_id, 
                    parent_id 
             INTO TABLE @FINAL(result) ##itab_db_select. 
 
    out->write( result ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

An internal table `parent_child_tab` is used as a data source of the common table expression `+parent_child_source` in a [`WITH`](abapwith.md) statement. A [CTE association](../../abap-glossary/abencte_association_glosry.md) `_relat` is [defined and exposed](abapwith_associations_defining.md) for the common table expression. The CTE association is a [self-association](../../abap-glossary/abenself_association_glosry.md). The common table expression can be used as a data source and the CTE association can be used as a [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md) of the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](abenselect_hierarchy_generator.md) used in the main query of the `WITH` statement. [Hierarchy functions](../../abap-glossary/abenhierarchy_function_glosry.md) cannot be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md) and the internal table must be transported to the database.
