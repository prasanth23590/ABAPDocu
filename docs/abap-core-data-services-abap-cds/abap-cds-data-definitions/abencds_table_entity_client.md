---
title: "ABAP CDS - Client Handling in CDS Table Entities"
source_file: abencds_table_entity_client.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Table Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Client Handling in CDS Table Entities

The [CDS annotation](../../abap-glossary/abencds_annotation_glosry.md) [`ClientHandling.type`](../abap-cds-annotations/abencds_613831553_anno.md) is used to define the [client dependency](../../abap-glossary/abenclient_dependency_glosry.md) for a [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md).

- The value `#CLIENT_DEPENDENT` declares a table entity as [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md).

- The value `#CLIENT_INDEPENDENT` declares a table entity as [client-independent](../../abap-glossary/abenclient_independent_glosry.md).

The value `#INHERITED` is not permitted for table entities.

If a table entity is declared as client-dependent, client handling takes place implicitly. The table is generated with a client column on the SAP HANA database. This client column is the first component of the primary key, if the table entity defines a primary key.

During read access using ABAP SQL, an implicit filter condition that filters the result set to the current session client is added.

During write access using ABAP SQL, the client column is implicitly set to the value of the current session client.

It is not allowed to explicitly define a client field in the `SELECT` list. The built-in type `abap.clnt` is forbidden, as well as the field name `CLIENT`.

Table entities are [client-safe](../../abap-glossary/abenclient_safe_glosry.md) by default.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS table entity is declared as client-dependent.

``` abap
@EndUserText.label: 'Demo: CDS table entity'
@ClientHandling.type: #CLIENT_DEPENDENT
@AbapCatalog.deliveryClass: #APPLICATION_DATA
@AccessControl.authorizationCheck: #NOT_REQUIRED
define table entity demo_cds_table_entity
{
  key key_field             : abap.int8;
      char_field_not_null   : abap.char(20);
      char_field_null       : abap.char(10) null;
      numc_field            : abap.numc(10);
      string_field          : abap.string null;
      decimal_field         : demo_occ;
      decfloat_field        : abap.decfloat34;
      timestamp_field       : abap.utcl;
      enum_field            : DEMO_CDS_ENUM_CHAR;
}
```

For this table entity, the following SQL statement is sent to the SAP HANA database: ![figure](images_abdoc_clienthandlingte.png)

A client column is added and it is also included in the primary key.

Client field:

"CLIENT" NVARCHAR(000003) DEFAULT '000' NOT NULL

Filter condition:

``` abap
ALTER TABLE "SAPUIA"."DEMO_CDS_TABLE_ENTITY" ADD CONSTRAINT 
"DEMO_CDS_TABLE_ENTITY~0" PRIMARY KEY ( 
  "CLIENT", 
  "KEY_FIELD"
```
