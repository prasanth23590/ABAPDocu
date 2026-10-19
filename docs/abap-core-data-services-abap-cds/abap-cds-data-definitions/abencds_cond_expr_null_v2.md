---
title: "CDS DDL - CDS View Entity, cds_cond, NULL"
source_file: abencds_cond_expr_null_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, cds_cond"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, cds_cond, NULL

## Syntax

``` abap
.... lhs IS [NOT] NULL ...  
```

## Description

Identifies the [null value](../../abap-glossary/abennull_value_glosry.md) in a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). The relational expression is true if the value of `lhs` is (not) the [null value](../../abap-glossary/abennull_value_glosry.md).

The operand `lhs` must stick to the context-dependent rules listed in topic [CDS DDL - View Entity, `cds_cond`, Operands](abencds_cond_expr_operands_v2.md).

`lhs` can have any data type except for `STRING`, `RAWSTRING`, and `GEOM_EWKB`.
