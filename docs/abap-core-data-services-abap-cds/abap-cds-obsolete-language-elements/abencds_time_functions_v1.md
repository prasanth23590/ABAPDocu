---
title: "CDS DDL - DDIC-Based View, Time Functions"
source_file: abencds_time_functions_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions > CDS DDL - DDIC-Based View, Built-In Functions > CDS DDL - DDIC-Based View, Special Functions > CDS DDL - DDIC-Based View, Date Functions and Time Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, Time Functions

## Syntax

``` abap
... TIMS_IS_VALID(time) ...  
```

### Variant

[1. `... TIMS_IS_VALID(time)`](abencds_time_functions_v1.md#variant-1)

## Overview

### Description

In a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), these functions execute operations with arguments of the built-in data type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The functions have [positional parameters](../../abap-glossary/abenpositional_parameter_glosry.md) to which arguments need to be assigned when called. There are currently no optional parameters. Suitable fields of a [data source](abencds_data_source_v1.md), [literals](abencds_literal_v1.md), [parameters](abencds_parameter_v1.md), [path expressions](abencds_path_expression_v1.md), built-in functions, or expressions can all be specified as arguments. If an argument contains the [null value](../../abap-glossary/abennull_value_glosry.md), every function except `TIMS_IS_VALID` returns a null value.

### Hint

It is not currently possible to access the current system time directly in a CDS view. Instead, a CDS view can be given an appropriate [input parameter](abencds_parameter_list_v1.md). The special annotation [`@Environment.systemField`](../abap-cds-data-definitions/abencds_f1_parameter_annotations.md) makes it possible to pass the value of the [ABAP system field](../../abap-glossary/abensystem_field_glosry.md) `sy-uzeit` to this parameter.

## Variant 1

`... TIMS_IS_VALID(time)`

### Description

The function `TIMS_IS_VALID` determines whether `time` (if specified) contains a valid time in the format `HHMMSS`. The argument must have the built-in data type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The result has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). A valid date produces the value 1 and all other input values (including the null value) produce the value 0.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view applies time functions in the `SELECT` list to columns of the DDIC database table `DEMO_EXPRESSIONS`. The class `CL_DEMO_CDS_TIME_FUNCTIONS` uses `SELECT` to access the view. The column `TIMS1` of the DDIC database table can be given any values.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_TIMFNC'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_time_functions
  as select from demo_expressions
{
  key id,
      tims1                as time1,
      tims_is_valid(tims1) as valid1
}
```
