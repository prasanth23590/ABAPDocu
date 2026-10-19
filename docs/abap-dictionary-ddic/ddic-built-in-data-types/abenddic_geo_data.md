---
title: "DDIC - Geodata Types"
source_file: abenddic_geo_data.html
section: "ABAP Dictionary (DDIC) > DDIC - Built-In Data Types > DDIC - Properties of the Built-In Dictionary Types > DDIC - Special Dictionary Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Geodata Types

The [geodata type](../../abap-glossary/abengeo_data_type_glosry.md) [`GEOM_EWKB`](abenddic_builtin_types.md) is a built-in data type in ABAP Dictionary that describes the geometric position in a given coordinate reference system.

It represents fields in the database that contain geometric data in the EWKB (Extended Well-Known Binary) format. This type is currently only supported on [SAP HANA databases](../../abap-glossary/abenhana_database_glosry.md) and references the database type `ST_GEOMETRY`.

The internal representation of the geodata type `GEOM_EWKB` is a [BLOB](../../abap-glossary/abenblob_glosry.md) (Binary Large Object) and the same rules and restrictions apply as to the type [`RAWSTRING`](abenddic_builtin_types.md). The type `GEOM_EWKB` is mapped to the ABAP type [`xstring`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md).

At ABAP level, there is no semantic representation for geometric data. ABAP only allows geometric data to be passed between the application and the SAP HANA database. The SAP HANA database functions for geometric data types can be accessed using [AMDP](../../abap-programming-language/abap-database-access/abenamdp.md).

If the data type `GEOM_EWKB` is used for a structure component or a table field of a DDIC database table, the type must be assigned a [spatial reference system](../ddic-database-tables/abenddic_database_tables_sptlrf.md). This system cannot be changed once activated. The system has the ID 0 by default.

## Hints

- Columns of the data type `GEOM_EWKB` are not supported as [BLOBs](../../abap-glossary/abenblob_glosry.md) in [streaming and locators in ABAP SQL](../../abap-programming-language/abap-database-access/abenstreams_locators.md). To use columns of the data type `GEOM_EWKB` in streaming and locators, they have to be converted to [JSON](../../abap-glossary/abenjson_glosry.md) format first. This can be done with the conversion function [`AS_GEO_JSON`](../../abap-programming-language/abap-database-access/abensql_geo_conv_func.md).

- [`NOT NULL`](../ddic-database-tables/abenddic_database_tables_init.md) cannot be set for a column of the type `GEOM_EWKB`.
