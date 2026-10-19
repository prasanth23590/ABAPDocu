---
title: "sql_func - Geometry Conversion Function"
source_file: abensql_geo_conv_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - Special Functions > sql_func - Conversion Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Geometry Conversion Function

## Syntax

``` abap
... AS_GEO_JSON( geom ) ...  
```

## Description

The function `AS_GEO_JSON` reads geometry input in the [Extended Well-Known Binary (EWKB) representation](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_geo_data.md) and returns a geometry object in [JSON](../../abap-glossary/abenjson_glosry.md) format. `geom` must be a table column of type [`GEOM_EWKB`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) containing a valid geometry. The result is a geometry object in [JSON](../../abap-glossary/abenjson_glosry.md) format with data type [`STRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

If `geom` is null, then null is returned.

## Hints

- The geodata type [`GEOM_EWKB`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_geo_data.md) is mapped to the ABAP type [`xstring`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). During the conversion to [JSON](../../abap-glossary/abenjson_glosry.md) format, a type conversion to the ABAP type [`string`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is carried out.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A geometry is inserted into the DDIC database table `DEMO_GEOM_EWKB` with the spatial reference ID *4326*. Within the `SELECT` statement, the column is read with the built-in function `AS_GEO_JSON`. The data type is converted from [`xstring`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to [`string`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and the coordinates of a polygon in [JSON](../../abap-glossary/abenjson_glosry.md) format are returned as output.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DELETE FROM demo_geom_ewkb. 
INSERT demo_geom_ewkb FROM @( VALUE #( 
  id = 'X' 
  geom_ewkb_4326 = 
    '0103000020E6100000010000000500000000000000000000000000000000000' & 
    '0000000000000000000000000000000F03F000000000000F03F000000000000' & 
    'F03F000000000000F03F0000000000000000000000000000000000000000000' & 
    '00000' ) ). 
 
SELECT SINGLE 
       as_geo_json( geom_ewkb_4326 ) 
       FROM demo_geom_ewkb 
       WHERE id = 'X' 
       INTO (@FINAL(geo_json)). 
 
out->write_json( geo_json ). 
out->display( ).
```
