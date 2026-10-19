---
title: "CDS DDL - DEFINE ABSTRACT ENTITY, association"
source_file: abencds_f1_absent_association.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Abstract Entities > CDS DDL - DEFINE ABSTRACT ENTITY > CDS DDL - DEFINE ABSTRACT ENTITY, element_list > CDS DDL - DEFINE ABSTRACT ENTITY, element"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE ABSTRACT ENTITY, association

## Syntax

``` abap
... ASSOCIATION [cardinality] [TO] target ON cds_cond 
                [ WITH DEFAULT FILTER cds_cond ] ...  
```

[`cardinality`](abencds_cardinality_v2.md) · [`cds_cond`](abencds_conditional_expression_v2.md) · [`cds_cond`](abencds_conditional_expression_v2.md)

## Description

Defines a [CDS association](../../abap-glossary/abencds_association_glosry.md) in the [element list](abencds_f1_absent_element_list.md) of an [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md). The CDS association uses an `ON` condition to associate the current CDS entity with a [association target](../../abap-glossary/abenassociation_target_glosry.md) `target`. The same rules apply that are described in topic [`CDS view entity, ASSOCIATION`](abencds_simple_association_v2.md) with the following differences:

- The addition `AS _assoc` is not used. The CDS association is declared using the name `_assoc`, after which the addition `ASSOCIATION` is specified in the element list.

- No [session variables](../../abap-glossary/abensession_variable_glosry.md) can be used in the conditions [`cds_cond`](abencds_conditional_expression_v2.md).

A CDS association defined using the addition `ASSOCIATION` in the element list of a CDS abstract entity is always exposed. It cannot, however, be used in any [SQL path expressions](../../abap-glossary/abensql_path_expression_glosry.md), neither in ABAP CDS or in ABAP SQL.

## Hints

- A CDS association of a CDS abstract entity cannot be used anywhere where it could produce instances of join expressions.

- For an overview of all possible association targets of all CDS entities that can define associations, see [Data Source Matrix](abencds_data_source_matrix.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following DDL source code shows a CDS abstract entity that exposes a CDS association with another CDS abstract entity:

``` abap
define abstract entity demo_cds_abstract_entity_assoc
  { 
    key key_col: abap.char(3);
        _assoc : association of many to one demo_cds_abstract_entity on
                   demo_cds_abstract_entity_assoc.key_col = _assoc.col1;
  }
```
