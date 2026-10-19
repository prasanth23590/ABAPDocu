---
title: "CDS DDL - DDIC-Based View, cds_cond, INITIAL"
source_file: abencds_cond_expr_initial_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, cds_cond"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, cds_cond, INITIAL

## Syntax

``` abap
.... lhs IS [NOT] INITIAL ...  
```

## Description

Determines the initial value. This expression is true if the value of `lhs` is (is not) the [initial value](../../abap-glossary/abeninitial_value_glosry.md) of its [built-in dictionary type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The operand `lhs` must stick to the context-dependent rules listed in topic [CDS DDL - DDIC-based View, `cds_cond`, Operands](abencds_cond_expr_operands_v1.md).

`lhs` can have any data type except for `CLNT`, `DECFLOAT16`, `DECFLOAT34`, `DF16_DEC`, `DF34_DEC`, `DF16_RAW`, `DF34_RAW`, `LCHR`, `STRING`, `RAW`, `RAWSTRING`, `DATN`, `TIMN`, `UTCL`, and `GEOM_EWKB`.

## Hints

- The expression `IS [NOT] INITIAL` is suitable for checking the type-dependent initial value, instead of comparing it with a type-compliant operand that contains the initial value.

- The expression `IS [NOT] INITIAL` must not be confused with the expression [`IS [NOT] NULL`](abencds_cond_expr_null_v1.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following DDIC-based view reads all rows from the DDIC database table `DEMO_DDIC_TYPES` in which the column `INT8` does not contain its initial value 0.

``` abap
@AbapCatalog.sqlViewName: 'DEMOCDSISINI'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view Demo_Cds_Is_Initial
  as select from  
    demo_ddic_types
    {
      *
    }
    where
      int8 is not initial
```
