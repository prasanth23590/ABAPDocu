---
title: "SELECT, FROM cds_hierarchy"
source_file: abenselect_cds_hierarchy.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FROM cds_hierarchy

## Syntax

``` abap
... cds_hierarchy[sql_para] ...  
```

[`sql_para`](abenabap_sql_parameters.md)

## Description

Specifies a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md) `cds_hierarchy` as an [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) [`hierarchy`](abenselect_hierarchy.md) in an ABAP SQL query. The CDS hierarchy is specified using its name `cds_hierarchy` defined after [`DEFINE HIERARCHY`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_define_hierarchy.md). If the CDS hierarchy has input parameters, actual parameters must be assigned to these in a parenthesized list [`sql_para`](abenabap_sql_parameters.md).

The rows of the tabular result set of a CDS hierarchy specified as a data source are the [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md) of the SQL hierarchy and their columns are composed of the elements of the CDS hierarchy and the additional [hierarchy columns](abenddddl_hierarchy.md) that can be used to access the [hierarchy attributes](../../abap-glossary/abenhierarchy_attribute_glosry.md) of the data source of the CDS hierarchy.

## Hint

When a CDS hierarchy is accessed, the hierarchy columns are read regardless of whether hierarchy attributes are listed in the [element list](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_hiera_element_list.md). If a hierarchy attribute is defined as an explicit element of the CDS hierarchy, it is possible to access both the element and the additional hierarchy column in ABAP SQL.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specifies a CDS hierarchy `DEMO_CDS_SIMPLE_TREE` as a data source of a `SELECT` statement in the class `CL_DEMO_HIERARCHY_TREE` with parameter passing and explicit access to the hierarchy columns.

``` abap
FINAL(start_id) = 1. 
 
SELECT FROM demo_cds_simple_tree( p_id = @start_id ) 
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
       INTO TABLE @FINAL(cds_result).
```
