---
title: "CDS DDL - CDS View Entity, cds_cond, INITIAL"
source_file: abencds_cond_expr_initial_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, cds_cond"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, cds_cond, INITIAL

## Syntax

``` abap
.... lhs IS [NOT] INITIAL ...  
```

## Description

Determines the initial value. This expression is true if the value of `lhs` is (is not) the [initial value](../../abap-glossary/abeninitial_value_glosry.md) of its [built-in dictionary type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The operand `lhs` must stick to the context-dependent rules listed in topic [CDS DDL - View Entity, `cds_cond`, Operands](abencds_cond_expr_operands_v2.md).

`lhs` can have any data type except for `CLNT`, `DF16_DEC`, `DF34_DEC`, `DF16_RAW`, `DF34_RAW`, `DF16_SCL`, `DF34_SCL`, `LANG`, `LCHR`, `LRAW`, `STRING`, `RAWSTRING`, and `GEOM_EWKB`.

## Hints

- The expression `IS [NOT] INITIAL` is suitable for checking the type-dependent initial value, instead of comparing it with a type-compliant operand that contains the initial value.

- The expression `IS [NOT] INITIAL` must not be confused with the expression [`IS [NOT] NULL`](abencds_cond_expr_null_v2.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity reads all rows from the DDIC database table `DEMO_DDIC_TYPES` in which the column `INT8` does not contain its initial value 0.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_IS_INITIAL_VE
  as select from demo_ddic_types
{
  key id,
      int8
}
where
  int8 is not initial
```
