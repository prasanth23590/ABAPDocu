---
title: "CDS DDL - DEFINE TABLE FUNCTION, element_list"
source_file: abencds_f1_return_list.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Table Functions > CDS DDL - DEFINE TABLE FUNCTION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE TABLE FUNCTION, element_list

## Syntax

``` abap
... RETURNS { element1; element2; ...; } ...  
```

[`element1`](abencds_f1_return_list_element.md) · [`element2`](abencds_f1_return_list_element.md)

## Description

Defines the elements of a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md). The elements are specified in a semicolon-separated list [`element1`](abencds_f1_return_list_element.md); [`element2`](abencds_f1_return_list_element.md); ...; in curly brackets `{ }`. The final element must also be followed by a semicolon.

These elements have the following meaning:

- They determine the components of the structured data types represented by a CDS table function with respect to ABAP.

- This structured data type is the row type of the tabular return value `result` of the [AMDP function implementation](../../abap-programming-language/abap-database-access/abenamdp_function_methods.md) `amdp_function` specified after [`IMPLEMENTED BY METHOD`](abencds_f1_define_table_function.md).

The ABAP data types of the components of the structured data type are derived from the dictionary types of the elements in accordance with the associated [mapping rules](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

In a [client-dependent](abencds_func_client_handling.md) CDS table function, the first element must be typed with the built-in dictionary type `CLNT`. This element is the client field of the CDS table function. It is a column of the tabular return value of the associated AMDP function implementation and is not a component of the structured data type represented by the table function.

## Hint

In a [client-dependent](abencds_func_client_handling.md) CDS table function, the structured data type of the table function and the row type of the return value of the AMDP function implementation are not compatible. The AMDP function implementation [cannot](../../abap-programming-language/abap-database-access/abenamdp_function_methods.md) be called as a regular function method in ABAP anyway, which means that no correspondingly structured target variable needs to be declared.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The class `CL_DEMO_AMDP_FUNCTION_TYPE` uses [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md) to show the following for various CDS table functions:

- The components of the structured data type

- The parameters of the associated AMDP function implementation

- The row type of the return value of the associated AMDP function implementation

For client-dependent table functions, a client field is defined after `RETURNS`. This field is a column of the return value of the AMDP function implementation and is not part of the structured data type.
