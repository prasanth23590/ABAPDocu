---
title: "CDS DDL - DDIC-Based View, path_expr, join_type"
source_file: abencds_path_expr_jointype_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, path_expr > CDS DDL - DDIC-Based View, path_expr, attributes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, path_expr, join_type

## Syntax

``` abap
... INNER|{LEFT OUTER} ...  
```

## Description

Defines the [join type](../../abap-glossary/abenjoin_type_glosry.md) with which the current CDS association is implemented:

- `INNER` determines an [inner join](../../abap-glossary/abeninner_join_glosry.md)

- `LEFT OUTER` determines a [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md)

If the join type is not specified explicitly, the type depends on the place where the path expression is used:

- After [`FROM`](abencds_select_statement_v1.md), it is an inner join (`INNER JOIN`)

- In all other locations, it is a left outer join (`LEFT OUTER JOIN`)

## Hint

In the DDL source text editor of the [ADT](../../abap-glossary/abenadt_glosry.md), you can view the configuration of the join in the display of the generated SQL DDL statement.

## Executable Example

[Joins of CDS Associations](abencds_assoc_join_v1_abexa.md)
