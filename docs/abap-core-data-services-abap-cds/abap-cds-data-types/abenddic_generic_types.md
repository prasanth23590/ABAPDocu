---
title: "ABAP CDS - Generic Data Types"
source_file: abenddic_generic_types.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Generic Data Types

The following table shows the built-in [CDS generic types](../../abap-glossary/abencds_generic_type_glosry.md). A generic data type is like a placeholder that allows different built-in data types.

The following generic data types are available:

| **Type**  | **Includes the following built-in data types**                                                                                                                                              |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `any`     | `INT1`, `INT2`, `INT4`, `INT8`, `DEC`, `CURR`, `QUAN`, `DECFLOAT16`, `DECFLOAT34`, `FLTP`, `CHAR`, `NUMC`, `STRING`, `SSTRING`, `RAW`, `RAWSTRING`, `DATS`, `TIMS`, `CUKY`, `UNIT`, `CLNT`. |
| `numeric` | `INT1`, `INT2`, `INT4`, `INT8`, `DEC`, `DECFLOAT16`, `DECFLOAT34`, `QUAN`.                                                                                                                  |

Generic CDS data types are currently allowed only for typing the parameters of [CDS scalar functions](../../abap-glossary/abencds_scalar_function_glosry.md).

The generic type `any` is allowed only in [analytical scalar functions](../../abap-glossary/abencds_ana_scalar_glosry.md). It is not allowed in [SQL-based scalar functions](../../abap-glossary/abencds_sql_scalar_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS scalar function uses the built-in generic type `numeric` to type the input parameter `p1`. Parameters passed to `p1` must have a valid data type. Otherwise, a syntax check error occurs.

``` abap
DEFINE SCALAR FUNCTION demo_generic_ddic_type 
    WITH PARAMETERS 
      p1: numeric 
    RETURNS TYPE OF p1
```
