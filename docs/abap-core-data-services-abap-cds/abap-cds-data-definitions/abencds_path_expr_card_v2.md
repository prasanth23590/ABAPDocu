---
title: "CDS DDL - CDS View Entity, path_expr, cardinality"
source_file: abencds_path_expr_card_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, path_expr > CDS DDL - CDS View Entity, path_expr, attributes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, path_expr, cardinality

## Syntax Forms

**Cardinality Syntax Written in Words**

``` abap
     ...[ {{EXACT ONE} | MANY | ONE} ] TO {{EXACT ONE} |MANY | ONE }: 
```

**Numeric Syntax**

``` abap
      ... 1|*: ...
```

## Description

Specifies the [cardinality](../../abap-glossary/abencardinality_glosry.md) of the current CDS association as unique or non-unique. The cardinality can be specified in words or in numbers. The syntax written in words is recommended.

The syntax written in words can specify the [source](../../abap-glossary/abensource_cardinality_glosry.md) and [target cardinalities](../../abap-glossary/abentarget_cardinality_glosry.md). However, it is also possible to specify only the target cardinality. The source cardinality can be omitted. The following combinations are possible:

- `EXACT ONE TO EXACT ONE`

- `EXACT ONE TO MANY`

- `EXACT ONE TO ONE`

- `MANY TO EXACT ONE`

- `MANY TO MANY`

- `MANY TO ONE`

- `ONE TO EXACT ONE`

- `ONE TO MANY`

- `ONE TO ONE`

- `TO ONE`

- `TO EXACT ONE`

- `TO MANY`

The numeric syntax only specifies the target cardinality. The target cardinality can be specified either as `1` (to-one), or as `*` (to-many). The source cardinality is implicitly set to `MANY`.

A colon (`:`) must be placed at the end of the cardinality specification.

If the target cardinality is specified as to-one (using the syntax additions `TO EXACT ONE:`, `TO ONE:`, or `1:`), it is possible to use filter conditions in path expressions, which are used in [`WHERE`](abencds_where_clause_v2.md) clauses or [`HAVING`](abencds_having_clause_v2.md) clauses. In a clause like this, it overwrites the [cardinality](../../abap-glossary/abencardinality_glosry.md) of the [CDS association](abencds_association_v2.md).

The cardinality cannot be specified as the only addition in square brackets. It must always be combined with a [filter condition](abencds_path_expression_filter_v2.md).

## Hints

- Specifying the cardinality as to-one cardinality prevents a syntax error if a path specified with filter conditions or with a non-unique cardinality is used in a [`WHERE`](abencds_where_clause_v2.md) clause or [`HAVING`](abencds_having_clause_v2.md) clause. However, at runtime, there is no check to validate whether the condition achieves the required unique cardinality.

- When a path expression of a `TO EXACT ONE` association is used with [attributes](abencds_path_expr_attr_v2.md), then the join is rewritten to a `TO ONE` join on the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) to avoid potential cardinality conflicts. This is indicated by a syntax check warning. The syntax check warning can be suppressed by explicitly specifying the current association as `TO EXACT ONE`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity filters the association `_Text` using the cardinality specification written in words.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, card in path_expr'

define view entity DEMO_CDS_PATH_EXP
  as select from demo_sales_mat

  association of exact one to many DEMO_SALES_CDS_MAT_TEXT as _Text 
    on  $projection.material = _Text.material
{
  key matnr as material,
      mtart as material_type,
      mtgrp as material_group,
      _Text,
      _Text[to exact one: inner where language = 'D' ].material_name
}
```

The class `CL_DEMO_CDS_PATH_EXPRESSION` first enters data into the database tables using `INSERT`, and then selects data from the CDS view entity `DEMO_CDS_PATH_EXP` using a `SELECT` statement.

Due to the path expression with filter condition, the result set consists of three rows. Without filter condition, the result set would contain more rows.
