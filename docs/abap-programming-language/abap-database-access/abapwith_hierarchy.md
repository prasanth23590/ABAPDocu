---
title: "WITH, HIERARCHY"
source_file: abapwith_hierarchy.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > WITH"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# WITH, HIERARCHY

## Syntax

``` abap
... WITH HIERARCHY hierarchy 
                 | (hierarchy_syntax)  
```

## Description

The addition `WITH HIERARCHY` exposes a common table expression as a [CTE hierarchy](../../abap-glossary/abencte_hierarchy_glosry.md). Under its name, a common table expression like this can be used in the subsequent queries of the current [`WITH`](abapwith.md) statement as an [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) [`hierarchy`](abenselect_hierarchy.md).

Only a single data source can be accessed in the subquery of the common table expression and this data source must be an [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) [`hierarchy`](abenselect_hierarchy.md). The SQL hierarchy used as the data source of the subquery can be specified either statically or dynamically after `HIERARCHY`.

- `hierarchy` is used to specify either the name of the SQL hierarchy or its alias name defined using [`AS`](abapfrom_clause.md). When the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](abenselect_hierarchy_generator.md) is used, it must have an alias name and this name must be specified.

- A parenthesized data object `hierarchy_syntax` can be specified. When the statement is executed, this data object must either contain the static syntax specifying the SQL hierarchy or be initial. In this case, the common table expression can be used only in other dynamic tokens of the `WITH` statement. The data object `hierarchy_syntax` can be a character-like data object or a [standard table](../../abap-glossary/abenstandard_table_glosry.md) with a character-like row type. The syntax in `hierarchy_syntax`, as in the static syntax, is not case-sensitive. Invalid syntax raises a catchable exception of the class `CX_SY_DYNAMIC_OSQL_ERROR`. If `hierarchy_syntax` is initial, the common table expression is not exposed as an SQL hierarchy.

The result set of a common table expression exposed as a CTE hierarchy includes the [hierarchy columns](abenddddl_hierarchy.md) of the SQL hierarchy specified in the subquery. The [`SELECT`](abapselect_list.md) list of the subquery must not contain any columns with the same name or alias name as a hierarchy column.

## Hint

If `hierarchy_syntax` is specified dynamically, it is possible to decide at runtime whether a common table expression is exposed as a CTE hierarchy.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This excerpt from the class `CL_DEMO_HIERARCHY_CTE` accesses CTE hierarchies in two hierarchy navigators [`HIERARCHY_DESCENDANTS`](../../abap-glossary/abenhierarchy_navigator_glosry.md) joined in the main query of a [`WITH`](abapwith.md) statement using a left outer join. The first CTE hierarchy represents the [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md) `DEMO_CDS_PARENT_CHILD`, which is accessed in its subquery. The second CTE hierarchy represents the result set of the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](abenselect_hierarchy_generator.md), which is used in its subquery. The `ON` condition of the join compares two [hierarchy columns](../../abap-glossary/abenhierarchy_column_glosry.md) of the CTE hierarchies. Executing `CL_DEMO_HIERARCHY_CTE` shows the result.

``` abap
WITH +hierarchy1 AS ( 
        SELECT FROM demo_cds_parent_child( p_id = 'A' ) 
               FIELDS id AS id1, 
                      parent AS parent1 ) 
        WITH HIERARCHY demo_cds_parent_child, 
     +hierarchy2 AS ( 
        SELECT FROM HIERARCHY( SOURCE demo_cds_parent_child_source 
                               CHILD TO PARENT ASSOCIATION _relat 
                               START WHERE id = 'U' ) AS hierarchy 
               FIELDS id AS id2, 
                      parent AS parent2 ) 
        WITH HIERARCHY hierarchy 
  SELECT FROM HIERARCHY_DESCENDANTS( 
                SOURCE +hierarchy1 
                START WHERE hierarchy_parent_rank = 0 
                DISTANCE FROM 1 ) AS h1 
           LEFT OUTER JOIN 
             HIERARCHY_DESCENDANTS( 
               SOURCE +hierarchy2 
               START WHERE hierarchy_parent_rank = 0 
               DISTANCE FROM 1 ) AS h2 
                 ON h1~hierarchy_rank = h2~hierarchy_rank 
         FIELDS h1~id1, 
                h2~id2, 
                h1~parent1, 
                h2~parent2 
         INTO TABLE @FINAL(result).
```
