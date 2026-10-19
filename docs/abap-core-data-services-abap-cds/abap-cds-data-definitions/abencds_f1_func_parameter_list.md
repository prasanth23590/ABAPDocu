---
title: "CDS DDL - DEFINE TABLE FUNCTION, parameter_list"
source_file: abencds_f1_func_parameter_list.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Table Functions > CDS DDL - DEFINE TABLE FUNCTION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE TABLE FUNCTION, parameter_list

## Syntax

``` abap
... WITH PARAMETERS parameter1, parameter2, ...  
```

[`parameter1`](abencds_f1_param.md) · [`parameter2`](abencds_f1_param.md)

## Description

Defines [CDS parameters](../../abap-glossary/abencds_parameter_glosry.md) [`parameter1`](abencds_f1_param.md), [`parameter2`](abencds_f1_param.md), ... as input parameters of a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md) in a comma-separated list.

A parameter must be typed with an elementary data type. All data types listed in topic [`Typing`](abencds_typing.md) are allowed, except for `abap.accp`, `abap.geom_ewkb`, and `abap.rawstring`.

The input parameters of the [AMDP function implementation](../../abap-programming-language/abap-database-access/abenamdp_function_methods.md) `amdp_function` specified after [`IMPLEMENTED BY METHOD`](abencds_f1_define_table_function.md) are generated from the input parameters specified here. The ABAP data types of the input parameters of the AMDP function implementation are derived from the [built-in data types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) in ABAP Dictionary specified by the [`typing`](abencds_typing.md), in accordance with the associated mapping rules for type references to ABAP Dictionary.

In the case of [client-dependent](abencds_func_client_handling.md) CDS table functions, each input parameter with the built-in dictionary type `CLNT` must be annotated with the annotation [`@Environment.systemField`](abencds_f1_parameter_annotations.md) and the predefined value [`#CLIENT`](abencds_f1_parameter_annotations.md).
