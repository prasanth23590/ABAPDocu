---
title: "CDS DDL - CDS View Entity, Time Functions"
source_file: abencds_time_functions_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions > CDS DDL - CDS View Entity, Built-In Functions > CDS DDL - CDS View Entity, Special Functions > CDS DDL - CDS View Entity, Date Functions and Time Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, Time Functions

## Syntax

``` abap
... TIMS_IS_VALID(time) ...  
```

## Description

In a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), the function `TIMS_IS_VALID` determines whether the [positional parameter](../../abap-glossary/abenpositional_parameter_glosry.md) `time` contains a valid time in the format `HHMMSS`. The actual parameter must have the built-in data type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). `time` can be specified as [literal](abencds_literal_v2.md), field of a [data source](abencds_data_source_v2.md), [parameter](abencds_parameter_v2.md), [path expression](abencds_path_expression_v2.md), [reuse expression](abencds_reusable_expression_v2.md) using `$projection`, an [SQL-based scalar function](abencds_sql_scalar_function.md), or [built-in function](abencds_builtin_functions_v2.md). The result has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). A valid date produces the value 1 and all other input values (including the null value) produce the value 0.

## Hint

It is not currently possible to access the current system time directly in a CDS view entity. Instead, a CDS view entity can be given an appropriate [input parameter](abencds_parameter_list_v2.md). The special annotation [`@Environment.systemField`](abencds_f1_parameter_annotations.md) makes it possible to pass the value of the [ABAP system field](../../abap-glossary/abensystem_field_glosry.md) `sy-uzeit` to this parameter.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity demonstrates how to use the time function `TIMS_IS_VALID`. The class `CL_DEMO_CDS_TIME_FUNC_VE` uses `SELECT` to access the view. You can assign any value to the column `TIMS1` of the DDIC database table `DEMO_EXPRESSIONS`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_TIME_FUNC_VE
  as select from demo_expressions
{
  key id,
      tims1                                        as time1,
      tims_is_valid(120102)                        as valid,
      tims_is_valid(tims_from_timn(timn1, 'FAIL')) as valid1,
      tims_is_valid(tims1)                         as valid2
}
```
