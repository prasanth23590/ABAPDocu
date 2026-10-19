---
title: "CDS DDL - DDIC-Based View, cds_cond, NULL"
source_file: abencds_cond_expr_null_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, cds_cond"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, cds_cond, NULL

## Syntax

``` abap
.... lhs IS [NOT] NULL ...  
```

## Description

Identifies the [null value](../../abap-glossary/abennull_value_glosry.md) in a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). The relational expression is true if the value of `lhs` is (not) the [null value](../../abap-glossary/abennull_value_glosry.md).

The operand `lhs` must stick to the context-dependent rules listed in topic [CDS DDL - DDIC-based View, `cds_cond`, Operands](abencds_cond_expr_operands_v1.md).

`lhs` can have any data type except for `STRING`, `RAWSTRING`, and `GEOM_EWKB`.
