---
title: "CDS DDL - DEFINE HIERARCHY, element_list"
source_file: abencds_f1_hiera_element_list.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Hierarchies > CDS DDL - DEFINE HIERARCHY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE HIERARCHY, element_list

## Syntax

``` abap
... { element1, element2, ..., } ...  
```

[`element1`](abencds_f1_hiera_element.md) · [`element2`](abencds_f1_hiera_element.md)

## Description

Defines the elements of a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md). The elements are specified in a comma-separated list enclosed in curly brackets `{ }`.

The elements determine either the components of the result set of the CDS hierarchy and of the structured data type represented by the CDS hierarchy with respect to ABAP or they expose a CDS association.

The ABAP data types of the components of the structured data type are derived from the dictionary types of the elements in accordance with the associated [mapping rules](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Element list of a CDS hierarchy in which all possible [hierarchy attributes](abencds_hierarchy_attributes.md) are listed after the prefix [`$node.`](abencds_f1_hiera_element.md). The class `CL_DEMO_HRRCHY_TREE_HIER_ATTR` accesses the CDS hierarchy and uses ABAP SQL to read all elements of the element list plus the additional [hierarchy columns](../../abap-glossary/abenhierarchy_column_glosry.md). When executed, `CL_DEMO_HRRCHY_TREE_HIER_ATTR` demonstrates that the values of the hierarchy attributes and of the associated hierarchy columns are the same.

``` abap
define hierarchy DEMO_CDS_SIMPLE_TREE_HIER_ATTR
  as parent child hierarchy(
    source
      DEMO_CDS_SIMPLE_TREE_SOURCE
      child to parent association _tree
      start where
        id = 1
      siblings order by
        id ascending
    )
    {
      id,
      parent,
      $node.hierarchy_rank        as h_rank,
      $node.hierarchy_tree_size   as h_tree_size,
      $node.hierarchy_parent_rank as h_parent_rank,
      $node.hierarchy_level       as h_level,
      $node.hierarchy_is_cycle    as h_is_cycle,
      $node.hierarchy_is_orphan   as h_is_orphan,
      $node.node_id               as h_node_id,
      $node.parent_id             as h_parent_id
    }
```
