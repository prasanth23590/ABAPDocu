---
title: "CDS DDL - CDS View Entity, WRITABLE"
source_file: abencds_define_wrtbl_view_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, WRITABLE

## Syntax

``` abap
... WRITABLE ...  
```

## Description

The addition `WRITABLE` defines a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) as [writable](../../abap-glossary/abenwritable_v2_glosry.md).

CDS view entities cannot be defined as writable if they contain:

- selects from more than one data source

- joins

- unions

- aggregations

- parameters

- calculated fields

Further restrictions:

Writable view entities can only select from [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md) and [CDS table entities](abencds_table_entities.md).

DML modifications that are available to be performed on writable view entities are:

- [`INSERT`](../../abap-programming-language/abap-database-access/abapinsert_dbtab.md)

- [`UPDATE`](../../abap-programming-language/abap-database-access/abapupdate.md)

- [`MODIFY`](../../abap-programming-language/abap-database-access/abapmodify_dbtab.md)

- [`DELETE`](../../abap-programming-language/abap-database-access/abapdelete_dbtab.md)

## Hint

Writable view entities can only select from [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md) and [CDS table entities](abencds_table_entities.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following view entity is defined as writable.

``` abap
@AbapCatalog.viewEnhancementCategory: [#NONE]
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Writable CDS View Entity'
@Metadata.ignorePropagatedAnnotations: true

define writable view entity DEMO_CDS_WRITABLE_VE
  as select from demo_ddic_types
{
  key id     as Id,
      int1   as Int1,
      int2   as Int2,
      char10 as Char10
}
```

The class `CL_DEMO_CDS_WRITABLE_VES` manipulates data of the CDS view entity using different ABAP SQL DML statements.

The following method is from that class.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DELETE FROM demo_cds_writable_ve. 
INSERT demo_cds_writable_ve 
  FROM TABLE @( 
    VALUE #( 
    ( id = 01 int1 = 4 int2 = 8 char10 = 'INSERT' ) 
    ( id = 02 int1 = 8 int2 = 16 char10 = 'MODIFY' ) 
    ( id = 03 int1 = 8 int2 = 16 char10 = 'UPDATE' ) 
    ( id = 04 int1 = 8 int2 = 16 char10 = 'DELETE' ) 
                                     ) ). 
 
SELECT * 
  FROM demo_cds_writable_ve 
  INTO TABLE @DATA(insert).                           "#EC CI_NOWHERE 
 
out->write( insert ). 
 
UPDATE demo_cds_writable_ve SET char10 = 'UPDATE2' WHERE id = 03. 
 
SELECT * 
  FROM demo_cds_writable_ve 
  ORDER BY id 
  INTO TABLE @DATA(update).                          "#EC CI_NOWHERE 
 
out->write( update ). 
 
MODIFY demo_cds_writable_ve FROM @( 
VALUE #( id = 02 char10 = 'MODIFY2' ) ). 
 
SELECT * 
  FROM demo_cds_writable_ve 
  ORDER BY id 
  INTO TABLE @DATA(modify).                          "#EC CI_NOWHERE 
 
out->write( modify ). 
 
DELETE FROM demo_cds_writable_ve 
  WHERE id = 04. 
 
SELECT * 
  FROM demo_cds_writable_ve 
  ORDER BY id 
  INTO TABLE @DATA(delete).                          "#EC CI_NOWHERE 
 
out->write( delete ).
```
