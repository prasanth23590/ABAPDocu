---
title: "DDIC - Spatial Reference System"
source_file: abenddic_database_tables_sptlrf.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Semantic Properties of Database Tables > DDIC - Table-Specific Semantic Properties of Database Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Spatial Reference System

The definition of a [spatial reference system](../../abap-glossary/abenspatial_ref_system_glosry.md) is mandatory for table fields with the [geodata type](../../abap-glossary/abengeo_data_type_glosry.md) [`GEOM_EWKB`](../ddic-built-in-data-types/abenddic_builtin_types.md). For other data types, this property is not available. The [spatial reference identifiers](../../abap-glossary/abenspatial_ref_identifier_glosry.md) of spatial reference systems that are available in the current [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) are provided by the HANA view `ST_SPATIAL_REFERENCE_SYSTEMS`. Once a table (or structure) is activated, the definition of the spatial reference system of a geodata type must not be modified.

## Hints

- Spatial reference systems are not managed by ABAP. There is no guarantee that a spatial reference system which is available in one system is also available in a follow-on system. An application that works with spatial reference systems is responsible for providing spatial references in all affected systems by using native HANA functions.
