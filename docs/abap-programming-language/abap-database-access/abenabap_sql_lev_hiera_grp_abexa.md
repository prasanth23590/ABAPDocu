---
title: "ABAP SQL - Level-based Hierarchy vs. Grouping"
source_file: abenabap_sql_lev_hiera_grp_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy > SELECT, FROM HIERARCHY > SELECT, FROM HIERARCHY, LEVELS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Level-based Hierarchy vs. Grouping

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example compares the generation of a [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md) to general grouping.

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
CLASS cl_demo_sql_leveld_vs_grp_v5 DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
      REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sql_leveld_vs_grp_v5 IMPLEMENTATION. 
  METHOD main. 
 
    TYPES: 
      BEGIN OF level_struc, 
        col1 TYPE i, 
        col2 TYPE i, 
        col3 TYPE i, 
        data TYPE c LENGTH 1, 
      END OF level_struc, 
      level_tab TYPE TABLE OF level_struc WITH EMPTY KEY. 
 
 
    DATA(level_tab) = VALUE level_tab( 
      ( col1 = 1 col2 = 11 col3 = 111 data = `A` ) 
      ( col1 = 1 col2 = 11 col3 = 112 data = `B` ) 
      ( col1 = 1 col2 = 11 col3 = 113 data = `C` ) 
      ( col1 = 1 col2 = 12 col3 = 121 data = `D` ) 
      ( col1 = 1 col2 = 12 col3 = 122 data = `E` ) 
      ( col1 = 1 col2 = 12 col3 = 123 data = `F` ) 
      ( col1 = 2 col2 = 21 col3 = 211 data = `G` ) 
      ( col1 = 2 col2 = 21 col3 = 212 data = `H` ) 
      ( col1 = 2 col2 = 21 col3 = 213 data = `I` ) 
      ( col1 = 2 col2 = 22 col3 = 221 data = `J` ) 
      ( col1 = 2 col2 = 22 col3 = 222 data = `K` ) 
      ( col1 = 2 col2 = 22 col3 = 223 data = `L` ) 
      ). 
 
    SELECT FROM HIERARCHY( 
                  SOURCE @level_tab AS lt 
                  LEVELS ( lt~col1, lt~col2, lt~col3 ) 
                  SIBLINGS ORDER BY lt~col1, lt~col2, lt~col3 ) 
           FIELDS col1, col2, col3, data 
           INTO TABLE @DATA(result) ##ITAB_DB_SELECT. 
 
    out->write( result ). 
 
    DATA grouped LIKE result. 
    LOOP AT level_tab INTO DATA(col1_group) 
            GROUP BY col1_group-col1. 
      APPEND VALUE #( col1 = col1_group-col1 ) TO grouped. 
      LOOP AT GROUP col1_group INTO DATA(col2_group) 
                    GROUP BY col2_group-col2. 
        APPEND VALUE #( col1 = col2_group-col1 
                        col2 = col2_group-col2 ) TO grouped. 
        LOOP AT GROUP col2_group INTO DATA(col2_member). 
          APPEND VALUE #( col1 = col2_member-col1 
                          col2 = col2_member-col2 
                          col3 = col2_member-col3 
                          data = col2_member-data ) TO grouped. 
        ENDLOOP. 
      ENDLOOP. 
    ENDLOOP. 
    ASSERT result = grouped. 
 
    DATA wx LIKE LINE OF result. 
    DATA wy LIKE LINE OF result. 
    DATA wz LIKE LINE OF result. 
    CLEAR grouped. 
    SELECT col1 
           FROM @level_tab AS lt 
           GROUP BY col1 
           ORDER BY col1 
           INTO CORRESPONDING FIELDS OF @wx ##ITAB_DB_SELECT. 
      APPEND wx TO grouped. 
      SELECT col1, col2 
           FROM @level_tab AS lt 
           GROUP BY col1, col2 
           HAVING col1 = @wx-col1 
           ORDER BY col1, col2 
           INTO CORRESPONDING FIELDS OF @wy ##ITAB_DB_SELECT. 
        APPEND wy TO grouped. 
        SELECT col1, col2, col3, data 
             FROM @level_tab AS lt 
             GROUP BY col1, col2, col3, data 
             HAVING col1 = @wy-col1 AND col2 = @wy-col2 
             ORDER BY col1, col2, col3 
             INTO CORRESPONDING FIELDS OF @wz ##ITAB_DB_SELECT. 
          APPEND wz TO grouped. 
        ENDSELECT. 
      ENDSELECT. 
    ENDSELECT. 
    ASSERT result = grouped. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example shows that the generation of a [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md) can be explained by the grouping of data:

- By using the addition [`GROUP BY`](../abap-processing-internal-data/abaploop_at_itab_group_by.md) of the `LOOP` statement for the data source `level_tab`, the same result can be produced as by the hierarchy generator.

- By using the [`GROUP BY`](abapgroupby_clause.md) clause of the `SELECT` statement for the data source `level_tab`, the same result can be produced as by the hierarchy generator.

This example is for demonstration purposes only. The results of the grouping are no SQL hierarchies and cannot be used as such. There are no additional hierarchy columns and they cannot be used in [hierarchy navigators](abenselect_hierarchy_navigators.md). The performance of the hierarchy generator based on a built-in HANA function is better by far.
