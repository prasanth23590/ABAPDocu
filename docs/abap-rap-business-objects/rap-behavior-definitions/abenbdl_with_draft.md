---
title: "RAP - with draft"
source_file: abenbdl_with_draft.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - BehaviorDefinitionHeader > RAP - DraftHandling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - with draft

## Syntax

``` abap
... 
with draft; 
 ...  
```

## Description

The addition `with draft` enables [RAP draft handling](../../abap-glossary/abenrap_draft_handling_glosry.md) for a [business object](../../abap-glossary/abenbusiness_object_glosry.md). It is added in the [behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md) as it draft-enables the entire business object. It enables the business object to have [exclusive draft](../../abap-glossary/abenrap_exclusive_draft_glosry.md) capabilities. It is not possible to implement draft capabilities for individual [entities](../../abap-glossary/abenrap_bo_entity_glosry.md) within a business object.

RAP draft handling is in all scenarios completely managed by the [RAP transactional engine](../../abap-glossary/abenrap_transac_engine_glosry.md). The application developer is not responsible for how draft data is written to the [draft database table](../../abap-glossary/abendraft_table_glosry.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, topic [Draft](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/a81081f76c904b878443bcdaf7a4eb10?version=sap_cross_product_abap).

## Executable Example

- [RAP BDL - draft actions Edit, Discard, Prepare](abenbdl_draft_action2_abexa.md)

- [RAP BDL - draft action Activate](abenbdl_draft_action1_abexa.md)
