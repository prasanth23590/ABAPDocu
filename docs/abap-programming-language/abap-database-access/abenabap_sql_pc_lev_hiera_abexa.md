---
title: "ABAP SQL - Parent-child-based Hierarchy vs. Level-based Hierarchy"
source_file: abenabap_sql_pc_lev_hiera_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy > SELECT, FROM HIERARCHY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Parent-child-based Hierarchy vs. Level-based Hierarchy

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example compares [parent-child-based hierarchies](../../abap-glossary/abenpc_based_hiera_glosry.md) with [level-based hierarchies](../../abap-glossary/abenlevel_based_hiera_glosry.md).

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
CLASS cl_demo_sql_leveld_vs_pc_hiera DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
      REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sql_leveld_vs_pc_hiera IMPLEMENTATION. 
  METHOD main. 
 
    DATA parent_child_data TYPE TABLE OF demo_simple_tree 
                                WITH EMPTY KEY. 
 
    parent_child_data = VALUE #( 
            ( id = 1  parent_id = 0  name = 'AA'          ) 
            ( id = 2  parent_id = 1  name = 'AA-AA'       ) 
            ( id = 3  parent_id = 2  name = 'AA-AA-AA'    ) 
            ( id = 4  parent_id = 3  name = 'AA-AA-AA-AA' ) 
            ( id = 5  parent_id = 3  name = 'AA-AA-AA-BB' ) 
            ( id = 6  parent_id = 3  name = 'AA-AA-AA-CC' ) 
            ( id = 7  parent_id = 3  name = 'AA-AA-AA-DD' ) 
            ( id = 8  parent_id = 1  name = 'AA-BB'       ) 
            ( id = 9  parent_id = 8  name = 'AA-BB-AA'    ) 
            ( id = 10 parent_id = 9  name = 'AA-BB-AA-AA' ) 
            ( id = 11 parent_id = 1  name = 'AA-CC'       ) 
            ( id = 12 parent_id = 11 name = 'AA-CC-AA'    ) 
            ( id = 13 parent_id = 12 name = 'AA-CC-AA-AA' ) 
            ( id = 14 parent_id = 12 name = 'AA-CC-AA-BB' ) ). 
 
    INSERT demo_simple_tree FROM TABLE @parent_child_data. 
 
    DATA leveled_data TYPE TABLE OF demo_leveld_tree 
                      WITH EMPTY KEY. 
 
    leveled_data = VALUE #( 
           ( level1 = 1 level2 = 1 level3 = 1 level4 = 1 
             name = 'AA-AA-AA-AA' ) 
           ( level1 = 1 level2 = 1 level3 = 1 level4 = 2 
             name = 'AA-AA-AA-BB' ) 
           ( level1 = 1 level2 = 1 level3 = 1 level4 = 3 
             name = 'AA-AA-AA-CC' ) 
           ( level1 = 1 level2 = 1 level3 = 1 level4 = 4 
             name = 'AA-AA-AA-DD' ) 
           ( level1 = 1 level2 = 2 level3 = 1 level4 = 1 
             name = 'AA-BB-AA-AA' ) 
           ( level1 = 1 level2 = 3 level3 = 1 level4 = 1 
             name = 'AA-CC-AA-AA' ) 
           ( level1 = 1 level2 = 3 level3 = 1 level4 = 2 
             name = 'AA-CC-AA-BB' ) ). 
 
    INSERT demo_leveld_tree FROM TABLE @leveled_data. 
 
    SELECT FROM HIERARCHY( SOURCE demo_cds_simple_tree_source 
                           CHILD TO PARENT ASSOCIATION _tree 
                           START WHERE id = 1 
                           SIBLINGS ORDER BY parent 
                           MULTIPLE PARENTS NOT ALLOWED ) 
           FIELDS node_id, 
                  parent_id, 
                  name, 
                  hierarchy_rank, 
                  hierarchy_parent_rank, 
                  hierarchy_tree_size, 
                  hierarchy_level 
           INTO TABLE @FINAL(parent_child_based_hiera). 
 
    SELECT FROM HIERARCHY( SOURCE demo_leveld_tree 
                           LEVELS ( level1, level2, level3, level4 ) 
                           SIBLINGS ORDER BY level2, level3, level4 ) 
           FIELDS node_id, 
                  parent_id, 
                  name, 
                  hierarchy_rank, 
                  hierarchy_parent_rank, 
                  hierarchy_tree_size, 
                  hierarchy_level, 
                  hierarchy_level_name 
           INTO TABLE @FINAL(level_based_hiera). 
 
    WITH 
          +cte_source AS 
            ( SELECT FROM @level_based_hiera AS level_based_hiera 
                     FIELDS 
                       node_id AS hiera_node_id, 
                       parent_id AS hiera_parent_id, 
                       name, 
                       hierarchy_rank AS hiera_rank, 
                       hierarchy_parent_rank AS hiera_parent_rank, 
                       hierarchy_tree_size AS hiera_tree_size, 
                       hierarchy_level AS hiera_level, 
                       hierarchy_level_name AS hiera_level_name ) 
               WITH ASSOCIATIONS ( 
                 JOIN MANY TO MANY +cte_source AS _tree 
                   ON +cte_source~hiera_parent_rank 
                     = _tree~hiera_rank ), 
          +cte_hiera AS 
            ( SELECT FROM HIERARCHY( 
                SOURCE +cte_source 
                CHILD TO PARENT ASSOCIATION _tree 
                START WHERE hiera_rank = 1 
                SIBLINGS ORDER BY hiera_rank ) AS cte_hierarchy 
                FIELDS * ) 
                WITH HIERARCHY cte_hierarchy 
          SELECT FROM +cte_hiera 
                 FIELDS node_id, 
                        parent_id, 
                        name, 
                        hierarchy_rank, 
                        hierarchy_parent_rank, 
                        hierarchy_tree_size, 
                        hierarchy_level 
                 INTO TABLE @FINAL(pc_based_from_lvl_based_hiera) 
                 ##ITAB_DB_SELECT. 
 
    "GTT! 
    DELETE FROM demo_simple_tree.                       "#EC CI_NOWHERE 
    DELETE FROM demo_leveld_tree.                       "#EC CI_NOWHERE 
 
    out->write( parent_child_data 
      )->write( leveled_data 
      )->write( parent_child_based_hiera 
      )->write( level_based_hiera 
      )->write( pc_based_from_lvl_based_hiera ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The two variants of the hierarchy generator [`HIERARCHY`](abenselect_hierarchy_generator.md) are used with DDIC database tables as data sources to generate a [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md) and a [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md). Both database tables represent similar hierarchical data that are organized differently:

- The three columns of `DEMO_SIMPLE_TREE` are filled with data where the columns `ID` and `PARENT_ID` are suitable for a parent-child relationship for a tree hierarchy and column `NAME` represents arbitrary data.

- The four columns of `DEMO_LEVELD_TREE` are filled with data where the first four columns are suitable as paths of a tree hierarchy consisting of four levels and column `NAME` represents arbitrary data.

For the [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md), the hierarchy generator `HIERARCHY` is used with [`CHILD TO PARENT ASSOCIATION`](abenselect_hierarchy_gen_assoc.md). The CDS view `DEMO_SIMPLE_TREE` is used as the data source. It accesses `DEMO_SIMPLE_TREE` and exposes a hierarchy association for the parent-child relationship between `ID` and `PARENT_ID`.

For the [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md), the hierarchy generator `HIERARCHY` is used with [`LEVELS`](abenselect_hierarchy_gen_level.md). The database table `DEMO_LEVELD_TREE` is used directly as data source. Its first four columns are specified as level columns.

The results in internal tables `parent_child_based_hiera` and `level_based_hiera` show similarities as well as differences between the generated SQL hierarchies.

- The hierarchy columns `HIERARCHY_RANK`, `HIERARCHY_PARENT_RANK`, `HIERARCHY_TREE_SIZE` and `HIERARCHY_LEVEL` are filled in exactly the same way, showing that both results represent similar hierarchies.

- The hierarchy columns `NODE_ID` and `PARENT_ID` are filled differently.

  - In the parent-child-based hierarchy, they represent the parent-child relationship used for generating the hierarchy.

  - In the level-based hierarchy, they represent the content of the level columns that represent the parent-child relationships for the current an its preceding node.

- The data column `NAME` has the same content only in the nodes of the highest level 4. For the lower levels:

  - In the parent-child-based hierarchy, the data content is read from the database table.

  - In the level-based hierarchy, the respective rows are not available in the database table but added to the SQL hierarchy. The data column of these rows are set to the null value.

- The level-based hierarchy has an additional hierarchy column ` HIERARCHY_LEVEL_NAME` with the name of the level column that defines the current level.

Finally, another parent-child-based hierarchy is generated in a [`WITH`](abapwith.md) statement from the internal table `level_based_hiera`. In that result of a level-based hierarchy, The hierarchy columns `HIERARCHY_RANK` and `HIERARCHY_PARENT_RANK` can be used in a parent-child relationship. The respective hierarchy association is exposed by CTE `+cte_source` from which in CTE `+cte_hiera` a parent-child-based hierarchy is generated. The final `SELECT` statement reads the result. In that parent-child-based hierarchy, all hierarchy columns have the same content as in `parent_child_based_hiera`. Only the content of the data column is different.
