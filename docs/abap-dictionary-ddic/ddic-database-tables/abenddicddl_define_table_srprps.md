---
title: "DDIC DDL - DEFINE TABLE, geo_annos"
source_file: abenddicddl_define_table_srprps.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Dictionary DDL for Defining Database Tables > DDIC DDL - DEFINE TABLE > DDIC DDL - DEFINE TABLE, field"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC DDL - DEFINE TABLE, geo_annos

## Syntax

``` abap
@AbapCatalog.geo.spatialRefSystem : 'id'  
```

## Description

Specifies a property for table fields with the [geodata type](../../abap-glossary/abengeo_data_type_glosry.md) `GEOM_EWKB`.

Currently, the annotation `@AbapCatalog.geo.spatialRefSystem` is available. This annotation is used to specify the ID `id` of a [spatial reference system](abenddic_database_tables_sptlrf.md) as an integer value in quotation marks. If the annotation is not specified, the default value 0 is used implicitly and the annotation inserted accordingly. The spatial reference system can no longer be modified after activation.

## Hints

- The program `ABAP_DOCU_SHOW_SPATIAL_REF_SYS` shows the spatial reference systems that are available in the current system.

- Spatial reference systems are not managed by ABAP. A spatial reference system that is available in one system is not necessarily available in a follow-up system.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Annotation `@AbapCatalog.geo.spatialRefSystem` for a table field `LOCATION` of a DDIC database table.

``` abap
... 
define table ... { 
  ... 
  @AbapCatalog.geo.spatialRefSystem : '4326' 
  location  : abap.geom_ewkb; 
  ... 
}
```
