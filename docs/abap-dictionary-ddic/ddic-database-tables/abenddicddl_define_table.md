---
title: "DDIC DDL - DEFINE TABLE"
source_file: abenddicddl_define_table.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Dictionary DDL for Defining Database Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC DDL - DEFINE TABLE

## Syntax

``` abap
structure_annos 
ext_annos 
table_annos 
DEFINE TABLE dbtab { 
  ... 
  field; 
  ... 
  include; 
  ... 
 }  
```

[`structure_annos`](../ddic-data-types/abenddicddl_define_struct_props.md) · [`ext_annos`](../ddic-data-types/abenddicddl_define_ext_annos.md) · [`table_annos`](abenddicddl_define_table_props.md) · [`field;`](abenddicddl_define_table_comps.md) · [`include;`](abenddicddl_define_table_incl.md)

## Description

[Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md) statement for defining an ABAP Dictionary [DDIC database table](abenddic_database_tables.md) `dbtab` in the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md).

- A DDIC database table is defined using the statement `DEFINE TABLE`. The name `dbtab` must comply with the naming rules for DDIC database tables.

- In front of the statement `DEFINE TABLE`,

  - the same mandatory structure properties must be specified as [annotations](../../abap-glossary/abenddic_annotation_glosry.md) [`structure_annos`](../ddic-data-types/abenddicddl_define_struct_props.md) as in the statement [`DEFINE STRUCTURE`](../ddic-data-types/abenddicddl_define_structure.md).

  - the same optional extensibility annotations [`ext_annos`](../ddic-data-types/abenddicddl_define_ext_annos.md) as in the statement [`DEFINE STRUCTURE`](../ddic-data-types/abenddicddl_define_structure.md) are available for [C0 developer extensibility](../../abap-glossary/abendev_extensibility_glosry.md).

  - any mandatory table properties must be specified as annotations [`table_annos`](abenddicddl_define_table_props.md). Any other properties are optional.

- The table fields are defined in a semicolon-separated list in curly brackets `{ }` using one of the following methods:

  - by defining single fields [`field`](abenddicddl_define_table_comps.md)

  - by including include structures [`include`](abenddicddl_define_table_incl.md).

## Hints

- As in the [CDS syntax](../../abap-core-data-services-abap-cds/abap-cds-syntax/abencds_general_syntax_rules.md), an ABAP Dictionary structure definition can contain comments after `//` and between `/* ... */`.

- For a more detailed description of the syntax, see the `ADT` documentation [Syntax of ABAP Dictionary Objects](https://help.sap.com/docs/ABAP_PLATFORM_NEW/c238d694b825421f940829321ffa326a/fc6cd6f7d02f4546a33feb3f5fc9dd66).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of DDIC database table `DEMO_BLOB_TABLE` in the [Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md) of the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md).

``` abap
@EndUserText.label : 'Table with a BLOB Column'
@AbapCatalog.enhancement.category : #NOT_EXTENSIBLE
@AbapCatalog.tableCategory : #TRANSPARENT
@AbapCatalog.deliveryClass : #A
@AbapCatalog.dataMaintenance : #RESTRICTED
define table demo_blob_table {

  key name : abap.sstring(255) not null;
  picture  : abap.rawstring(0);

}
```
