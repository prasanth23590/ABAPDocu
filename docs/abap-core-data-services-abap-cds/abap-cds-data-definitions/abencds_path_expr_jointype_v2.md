---
title: "CDS DDL - CDS View Entity, path_expr, join_type"
source_file: abencds_path_expr_jointype_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, path_expr > CDS DDL - CDS View Entity, path_expr, attributes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, path_expr, join_type

## Syntax

``` abap
... INNER|{LEFT OUTER} ...  
```

## Description

Defines the [join type](../../abap-glossary/abenjoin_type_glosry.md) with which the current CDS association is implemented:

- `INNER` determines an [inner join](../../abap-glossary/abeninner_join_glosry.md)

- `LEFT OUTER` determines a [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md)

If the join type is not specified explicitly, the type depends on the place where the path expression is used:

- After [`FROM`](abencds_select_statement_v2.md), it is an inner join

- In all other locations, it is a left outer join

## Hints

- In the DDL source text editor of the [ADT](../../abap-glossary/abenadt_glosry.md), you can view the configuration of the join in the display of the generated SQL DDL statement.

- For the last CDS association of a path expression, the specification of a join type property is not allowed. If a path expression consists of one single CDS association, then the join type cannot be specified.

## Executable Example

[Joins of CDS Associations](abencds_assoc_join_v2_abexa.md)
