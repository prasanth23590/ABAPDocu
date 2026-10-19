---
title: "sql_func - Spatial Functions"
source_file: abensql_spatial_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - SQL Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Spatial Functions

## Syntax

``` abap
... func( arg1[, arg2] ... ) ...  
```

## Description

Calls a [spatial function](../../abap-glossary/abenspatial_func_glosry.md) `func` as an [SQL expression](abapsql_expr.md) or operand of an expression in ABAP SQL. The arguments `arg1`, `arg2`, ... of the function are specified as a comma-separated list in parentheses. A blank must be placed after the opening parenthesis and in front of the closing parenthesis.

Using spatial functions, [spatial data](../../abap-glossary/abenspatial_data_glosry.md) can be accessed, manipulated, and analyzed. The implemented functions in ABAP SQL are mapped to the methods, functions, and constructors for spatial data in [SAP HANA](../../abap-glossary/abensap_hana_glosry.md). For more information refer to the [SAP HANA Spatial Reference](https://help.sap.com/docs/SAP_HANA_PLATFORM/cbbbfc20871e4559abfd45a78ad58c02/e1c934157bd14021a3b43b5822b2cbe9).

The spatial functions are listed and described in the following tables:

- [Spatial Constructors](abensql_spatial_func_c.md)

- [Spatial Methods](abensql_spatial_func_m.md)

- [Spatial Functions](abensql_spatial_func_f.md)

- [Aggregate Spatial Functions](abensql_spatial_func_a.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Calculation of the distance between two spatial points.

``` abap
DELETE FROM demo_geo_point. 
INSERT demo_geo_point FROM @( VALUE #( 
  point1 = `010100002000000000E561A1D634A748400D71AC8BDB482140` 
  point2 = `0101000020000000006919A9F754BC49408A20CEC3090C1F40` ) ). 
 
SELECT st_distance( point1, point2 ) 
       FROM demo_geo_point 
       INTO TABLE @FINAL(distance).
```
