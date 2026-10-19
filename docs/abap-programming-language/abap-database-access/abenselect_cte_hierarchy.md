---
title: "SELECT, FROM cte_hierarchy"
source_file: abenselect_cte_hierarchy.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FROM cte_hierarchy

## Syntax

``` abap
... +cte_hierarchy  
```

## Description

Specifies a [CTE hierarchy](../../abap-glossary/abencte_hierarchy_glosry.md) `+cte_hierarchy` as a an SQL hierarchy [`hierarchy`](abenselect_hierarchy.md) in an ABAP SQL query of a [`WITH`](abapwith.md) statement. A CTE hierarchy is a common table expression defined as an SQL hierarchy using the addition [`WITH HIERARCHY`](abapwith_hierarchy.md).

The rows of the tabular result set of a CTE hierarchy are the [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md) of the SQL hierarchy accessed in its subquery, including their [hierarchy columns](abenddddl_hierarchy.md).

## Hint

More specifically, a CTE hierarchy can be specified as a source of the [hierarchy navigators](../../abap-glossary/abenhierarchy_navigator_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specification of a CTE hierarchy as a data source of a `SELECT` statement in the class `CL_DEMO_HIERARCHY_TREE` with explicit access to the hierarchy columns. The data source of the subquery of the CTE hierarchy is a CDS hierarchy.

``` abap
FINAL(start_id) = 1. 
 
WITH +tree AS ( 
        SELECT FROM demo_cds_simple_tree( p_id = @start_id ) 
               FIELDS * ) 
      WITH HIERARCHY demo_cds_simple_tree 
  SELECT FROM  +tree 
         FIELDS id, 
                parent, 
                name, 
                hierarchy_rank, 
                hierarchy_tree_size, 
                hierarchy_parent_rank, 
                hierarchy_level, 
                hierarchy_is_cycle, 
                hierarchy_is_orphan, 
                node_id, 
                parent_id 
         INTO TABLE @FINAL(cte_result).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

See also the example under [`WITH - hierarchy`](abapwith_hierarchy.md).
