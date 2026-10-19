---
title: "DDIC DDL - DEFINE TABLE, field"
source_file: abenddicddl_define_table_comps.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Dictionary DDL for Defining Database Tables > DDIC DDL - DEFINE TABLE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC DDL - DEFINE TABLE, field

## Syntax

``` abap
[component_annos] 
[foreign_key_annos] 
[geo_annos] 
[KEY] field : {data_element [foreign_key] 
 [value_help]} 
              |abap.type[(n)|(n,m)] 
              [NOT NULL];  
```

[`component_annos`](../ddic-data-types/abenddicddl_define_struct_cmpprps.md) · [`foreign_key_annos`](abenddicddl_define_table_fkprps.md) · [`geo_annos`](abenddicddl_define_table_srprps.md) · [`foreign_key`](abenddicddl_define_table_forkey.md) · [`value_help`](../ddic-data-types/abenddicddl_define_struct_valuhelp.md) · [`type`](../ddic-built-in-data-types/abenddic_builtin_types.md)

## Description

Defines a single [database field](abenddic_database_tables_techstruc.md) in the definition of a DDIC database table using the [Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md) statement [`DEFINE TABLE`](abenddicddl_define_table.md).

- In front of the field, annotations [`component_annos`](../ddic-data-types/abenddicddl_define_struct_cmpprps.md) can be used to specify the same optional component properties as in the definition of a structure using [`DEFINE STRUCTURE`](../ddic-data-types/abenddicddl_define_structure.md).

- [`foreign_key_annos`](abenddicddl_define_table_fkprps.md) can be used to specify the properties of a foreign key dependency defined with [`foreign_key`](abenddicddl_define_table_forkey.md).

- [`geo_annos`](abenddicddl_define_table_srprps.md) specify the properties of a component with the [geodata type](../../abap-glossary/abengeo_data_type_glosry.md) `GEOM_EWKB`.

- The addition `KEY` defines the table field as a [key field](abenddic_database_tables_key.md).

- `field` defines the name of the database field.

- `data_element` or `abap.type` is used to define the data type of the table field. The same rules apply as in the definition of a [structure component](../ddic-data-types/abenddicddl_define_struct_comps.md), except that only elementary types can be specified here.

- The addition `NOT NULL` is used to set the [flag for initial values](abenddic_database_tables_init.md).

- The addition [`foreign_key`](abenddicddl_define_table_forkey.md) can be used to define a [foreign key dependency](abenddic_database_tables_forkeyrel.md) for a table field. As a prerequisite, the table field must be typed using a data element.

- The addition [`value_help`](../ddic-data-types/abenddicddl_define_struct_valuhelp.md) can be used to assign a search help to a table field whose data type is defined using a data element.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of DDIC database table `DEMO_EXPRESSIONS` in the [Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md) of the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md). The types of all fields are determined directly using built-in data types in the ABAP Dictionary.

``` abap
 @EndUserText.label : 'Database table for Expression Examples' 
@AbapCatalog.enhancement.category : #NOT_EXTENSIBLE 
@AbapCatalog.tableCategory : #TRANSPARENT 
@AbapCatalog.deliveryClass : #A 
@AbapCatalog.dataMaintenance : #ALLOWED 
define table demo_expressions { 
  key mandt  : mandt not null; 
  key id     : char1 not null; 
  num1       : abap.int4; 
  num2       : abap.int4; 
  numlong1   : abap.int8; 
  numlong2   : abap.int8; 
  dec1       : abap.dec(31,0); 
  dec2       : abap.dec(31,10); 
  dec3       : abap.dec(10,3); 
  fltp1      : abap.fltp; 
  fltp2      : abap.fltp; 
  decf1      : abap.df34_dec(31,0); 
  decf2      : abap.df34_dec(31,0); 
  char1      : abap.char(10); 
  char2      : abap.char(10); 
  numc1      : abap.numc(10); 
  numc2      : abap.numc(10); 
  string1    : abap.string(0); 
  string2    : abap.string(0); 
  raw1       : abap.raw(10); 
  raw2       : abap.raw(10); 
  xstring1   : abap.rawstring(0); 
  xstring2   : abap.rawstring(0); 
  dats1      : abap.dats; 
  dats2      : abap.dats; 
  tims1      : abap.tims; 
  tims2      : abap.tims; 
  timestamp1 : abap.dec(15,0); 
  timestamp2 : abap.dec(15,0); }
```
