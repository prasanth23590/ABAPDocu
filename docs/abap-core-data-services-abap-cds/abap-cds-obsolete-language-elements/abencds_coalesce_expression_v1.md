---
title: "CDS DDL - DDIC-Based View, coalesce"
source_file: abencds_coalesce_expression_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions > CDS DDL - DDIC-Based View, Built-In Functions > CDS DDL - DDIC-Based View, sql_functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, coalesce

## Syntax

``` abap
... COALESCE( arg1, arg2 ) ...  
```

## Description

[Coalesce function](../../abap-glossary/abencoalesce_glosry.md) in a [`SELECT` statement](abencds_select_statement_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). Can be used to check whether `arg1` contains a [null value](../../abap-glossary/abennull_value_glosry.md). In ABAP CDS, the coalesce function has two mandatory [positional parameters](../../abap-glossary/abenpositional_parameter_glosry.md) for arguments `arg1` and `arg2`. It checks whether `arg1` contains a null value. If yes, then it returns the value of `arg2`. If no, then it returns the value of `arg1`. If both `arg1` and `arg2` are null, then the null value is returned.

The following can be specified as the arguments `arg`:

- [Literals](abencds_literal_v1.md) of a suitable type. The literal can be prefixed with the name of a domain.

- Suitable [fields](abencds_field_v1.md) of a data source [`data_source`](abencds_data_source_v1.md) of the current CDS view.

- [Path expressions](abencds_path_expression_v1.md) that identify a suitable field of a data source [`data_source`](abencds_data_source_v1.md).

- [Input parameters](abencds_parameter_v1.md) from the parameter list [`parameter_list`](abencds_parameter_list_v1.md).

- The following built-in functions and expressions (if they return a matching type):

  - Other built-in [SQL functions](abencds_sql_functions_v1.md)

  - [Arithmetic expressions](abencds_arithmetic_expression_v1.md)

  - Type modifications using [`CAST`](abencds_cast_expression_v1.md)

The valid argument types of `arg1` and `arg2` are all [dictionary types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) except `ACCP`, `DF16_DEC`, `DF34_DEC`, `DF16_RAW`, `DF34_RAW`, `LCHR`, `LRAW`, `PREC`, `RAWSTRING`, `STRING`, and `GEOM_EWKB`.

The data types of both arguments must either be the same or the data type of one argument must represent the value of the other data type. The result has the dictionary type of the argument with the largest value range.

## Hint

A coalesce function is a short form of the following [complex case distinction](../abap-cds-data-definitions/abencds_case_expression_v2.md):

``` abap
CASE WHEN arg1 IS NOT NULL THEN arg1 
     ELSE arg2 
END
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following DDIC-based CDS view demonstrates the syntax of the coalesce function.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_COAL_V1'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view DEMO_CDS_COALESCE_V1 
as select from demo_ddic_types 
{
  key id,
  coalesce(int1, int2) as coalesced
}
```
