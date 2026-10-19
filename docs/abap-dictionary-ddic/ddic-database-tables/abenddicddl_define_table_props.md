---
title: "DDIC DDL - DEFINE TABLE, table_annos"
source_file: abenddicddl_define_table_props.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Dictionary DDL for Defining Database Tables > DDIC DDL - DEFINE TABLE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC DDL - DEFINE TABLE, table_annos

## Syntax

``` abap
@AbapCatalog.tableCategory : table_cat 
@AbapCatalog.dataMaintenance : data_maint 
@AbapCatalog.deliveryClass : deliv_class 
 
[@AbapCatalog.activationType : act_type] 
[@AbapCatalog.replacementObject : '...'] 
[@AbapCatalog.primaryKey.invertedIndividualIndex: true | false]  
```

## Description

Annotations for specifying table properties in the definition of a DDIC database table using the statement [`DEFINE TABLE`](abenddicddl_define_table.md) in the [Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md).

**Mandatory Definitions**

- `@AbapCatalog.tableCategory` defines the [table category](abenddic_database_tables_tab_cat.md). `table_cat` can be specified as:

  - `#TRANSPARENT` - [transparent table](../../abap-glossary/abentransparent_table_glosry.md)

  - `#GLOBAL_TEMPORARY` - [Global Temporary Table (GTT)](../../abap-glossary/abenglobal_temporary_table_glosry.md)

- `@AbapCatalog.dataMaintenance` defines how [the DDIC database table is displayed and maintained](abenddic_database_tables_maint.md). `data_maint` can be specified as:

  - `#NOT_ALLOWED` - [Display/maintenance not allowed](abenddic_database_tables_maint.md)

  - `#RESTRICTED` - [Display/maintenance allowed with restrictions](abenddic_database_tables_maint.md)

  - `#ALLOWED` - [Display/maintenance allowed](abenddic_database_tables_maint.md)

  - `#DISPLAY` - [Only display allowed](abenddic_database_tables_maint.md)

- `@AbapCatalog.deliveryClass` defines the [delivery class of the database table](abenddic_database_tables_delivery.md). `deliv_class` can be specified as:

  - `#A` - [delivery class A](abenddic_database_tables_delivery.md)

  - `#C` - [delivery class C](abenddic_database_tables_delivery.md)

  - `#L` - [delivery class L](abenddic_database_tables_delivery.md)

  - `#G` - [delivery class G](abenddic_database_tables_delivery.md)

  - `#E` - [delivery class E](abenddic_database_tables_delivery.md)

  - `#S` - [delivery class S](abenddic_database_tables_delivery.md)

  - `#W` - [delivery class W](abenddic_database_tables_delivery.md)

**Optional Definitions**

- `@AbapCatalog.activationType` defines the [activation type of the database table](abenddic_database_tables_act_type.md). This setting is not relevant for DDIC database tables in application programming. `act_type` can be specified as:

  - `#NOT_CLASSIFIED` - [activation type 00](abenddic_database_tables_act_type.md)

  - `#NAMETAB_GENERATION_OFFLINE` - [activation type 01](abenddic_database_tables_act_type.md)

  - `#ADAPT_C_STRUCTURES` - [activation type 02](abenddic_database_tables_act_type.md)

  - `#INITIAL_TABLE_REQUIRED` - [activation type 10](abenddic_database_tables_act_type.md)

- `@AbapCatalog.replacementObject` defines the name of a [replacement object](../../abap-glossary/abenreplacement_object_glosry.md) in quotation marks.

- `@AbapCatalog.primaryKey.invertedIndividualIndex` defines the type of the [primary index](../../abap-glossary/abenprimary_index_glosry.md):

  - `true` - [`INVERTED INDIVIDUAL`](abenddic_database_tables_index.md) as of HANA2, SPS 03, [`INVERTED HASH`](abenddic_database_tables_index.md) before HANA2, SPS 03

  - `false` - [`INVERTED VALUE`](abenddic_database_tables_index.md) (default)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Annotations in the definition of the DDIC database table `DEMO_SUMDIST` in the [Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md) of the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md). This table has the CDS view `DEMO_CDS_SUMDIST` as its [replacement object](../../abap-glossary/abenreplacement_object_glosry.md).

``` abap
@EndUserText.label : 'Aggregation Table with Replacement Object' 
@AbapCatalog.enhancement.category : #NOT_EXTENSIBLE 
@AbapCatalog.tableCategory : #TRANSPARENT 
@AbapCatalog.deliveryClass : #A 
@AbapCatalog.dataMaintenance : #LIMITED 
@AbapCatalog.replacementObject : 'demo_cds_sumdist' 
define table demo_sumdist { 
  key client   : mandt not null; 
  key carrname : s_carrname not null; 
  key distid   : s_distid not null; 
  @Semantics.quantity.unitOfMeasure : 'demo_sumdist.distid' 
  sum_distance : s_distance; }
```
