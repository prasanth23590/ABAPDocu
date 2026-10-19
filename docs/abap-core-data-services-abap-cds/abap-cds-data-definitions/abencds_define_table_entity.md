---
title: "CDS DDL - DEFINE TABLE ENTITY"
source_file: abencds_define_table_entity.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Table Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE TABLE ENTITY

## Syntax

``` abap
[@entity_annot1] 
[@entity_annot2] 
... 
[@table_entity_annot1] 
[@table_entity_annot2] 
... 
[DEFINE] [ROOT] TABLE ENTITY table_entity 
          element_list[;]  
```

[`@entity_annot1`](abencds_f1_entity_annotations.md) · [`@entity_annot2`](abencds_f1_entity_annotations.md) · [`@table_entity_annot1`](abencds_table_entity_anno.md) · [`@table_entity_annot2`](abencds_table_entity_anno.md) · [`element_list`](abencds_table_entity_element_list.md)

## Description

Defines an [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md) `table_entity` in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md).

- A CDS table entity is defined using the statement `DEFINE TABLE ENTITY`. The name `table_entity` must follow the naming rules for CDS objects that are described in the topic [ABAP CDS - General Syntax Rules](../abap-cds-syntax/abencds_general_syntax_rules.md) with one constraint: the name of a table entity can have no more than 25 characters.

- The CDS table entity can be enriched with [entity annotations](abencds_f1_entity_annotations.md) `entity_annot1`, `entity_annot2`, ... (these are annotations that can be used in all CDS entities) or with [table entity annotations](abencds_table_entity_anno.md) `table_entity_annot1`, `table_entity_annot2`, ... (these are annotations that are only available for CDS table entities).

- The addition [`ROOT`](abencds_define_root_view_v2.md) is optional. It defines the table entity as root entity of a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) in the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md). For further details, see topic [CDS DDL - CDS View Entity, `ROOT`](abencds_define_root_view_v2.md).

- [`element_list`](abencds_table_entity_element_list.md) defines the elements of the table entity.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code shows a CDS table entity:

``` abap
@ClientHandling.type: #CLIENT_INDEPENDENT
@AbapCatalog.deliveryClass: #APPLICATION_DATA
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS table entity, client independent'
define table entity DEMO_CDS_TE
{
  key key_element : abap.char(10);
      col1        : abap.char(3);
      col2        : abap.int4;
      col3        : abap.char(1);
      col4        : abap.int4; 

}
```

The class `CL_DEMO_CDS_TABLE_ENTITY` manipulates data of the CDS table entity using different ABAP SQL DML statements.

The following method is from that class.

``` abap
DELETE FROM demo_cds_te. 
 
INSERT demo_cds_te 
  FROM TABLE @( 
  VALUE #( ( key_element = 'A' col1 = 'aaa' col2 = 8  col3 = 'A' ) 
           ( key_element = 'B' col1 = 'bbb' col2 = 9  col3 = 'B' ) 
           ( key_element = 'C' col1 = 'ccc' col2 = 10 col3 = 'C' ) 
           ( key_element = 'D' col1 = 'ddd' col2 = 11 col3 = 'D' ) ) ). 
 
UPDATE demo_cds_te 
  SET col1 = 'XXX' 
  WHERE key_element = 'A'. 
 
MODIFY demo_cds_te FROM @( VALUE #( key_element = 'B' 
                                    col1 = 'XXX' ) ). 
 
SELECT * 
  FROM demo_cds_te 
  ORDER BY key_element 
  INTO TABLE @DATA(modify). "#EC CI_NOWHERE
```
