---
title: "CDS DDL - WHERE, Transactional Interface"
source_file: abencds_interface_cond_expr.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Interface > CDS DDL - DEFINE VIEW ENTITY AS PROJECTION ON, Transactional Interface"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - WHERE, Transactional Interface

## Syntax

``` abap
... WHERE cds_cond ...  
```

## Description

Defines a `WHERE` condition for the result set of a [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md). When the transactional interface is accessed, the result set contains only the data from the projected entity [`cds_entity`](abencds_define_view_as_interface.md) that meets the condition `cds_cond` specified after `WHERE`.

The condition is either a single relational expression `rel_expr` or an expression constructed from the Boolean operators `NOT`, `AND`, and `OR`.

In transactional interfaces, the following rules apply to the operands and syntax of the `WHERE` condition:

- Comparison operators, `BETWEEN`, `LIKE`, and `IS [NOT] INITIAL` are allowed as operators.

- The Boolean operators `NOT`, `AND`, and `OR` are supported.

- `lhs` expects a field of the projected entity. The field does not necessarily have to be included in the projection list.

- `rhs` can be a field of the projected entity, a [CDS literal](../../abap-glossary/abencds_literal_glosry.md), or a [session variable](abencds_session_variable_v2.md). When using the operator `LIKE`, `rhs` must be a character literal.
