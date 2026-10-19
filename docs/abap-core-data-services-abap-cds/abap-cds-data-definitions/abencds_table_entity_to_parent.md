---
title: "CDS DDL - CDS Table Entity, ASSOCIATION TO PARENT"
source_file: abencds_table_entity_to_parent.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Table Entities > CDS DDL - DEFINE TABLE ENTITY > CDS DDL - CDS Table Entity, element_list > CDS DDL - CDS Table Entity, element"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Table Entity, ASSOCIATION TO PARENT

## Syntax

``` abap
... ASSOCIATION TO PARENT target ON cds_cond ...  
```

[`cds_cond`](abencds_conditional_expression_v2.md)

## Description

Defines a [CDS to-parent association](../../abap-glossary/abento_parent_association_glosry.md) in the [element list](abencds_table_entity_element_list.md) of a [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md).

The CDS to-parent association associates the current CDS entity, as an [association source](../../abap-glossary/abenassociation_source_glosry.md), with the [association target](../../abap-glossary/abenassociation_target_glosry.md) `target` specified in the definition of the CDS to-parent association.

CDS to-parent associations are specialized [CDS associations](../../abap-glossary/abencds_association_glosry.md) and the same rules apply as described in topic [CDS DDL - CDS View Entity, `ASSOCIATION TO PARENT`](abencds_to_parent_assoc_v2.md). The only difference is that the addition `AS _assoc` is not used. The name of the to-parent association is declared using the name `_to_parent` in the element list of the table entity.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Demonstration of a simple CDS composition. The parent entity `DEMO_CDS_TE_COMPOS_1` defines a to-child association to the table entity `DEMO_CDS_TE_TO_PARENT_1`.

``` abap
@ClientHandling.type: #CLIENT_DEPENDENT
@AbapCatalog.deliveryClass: #APPLICATION_DATA
@AccessControl.authorizationCheck: #NOT_ALLOWED
@EndUserText.label: 'CDS table entity, composition'
define root table entity DEMO_CDS_TE_COMPOS_1
{
  key key_el : abap.int4;
      col1   : abap.char(1);
      _to_child: composition of exact one to many DEMO_CDS_TE_TO_PARENT_1;

}
```

The child entity `DEMO_CDS_TE_TO_PARENT_1` defines a to-parent association to the table entity `DEMO_CDS_TE_COMPOS_1`.

``` abap
@ClientHandling.type: #CLIENT_DEPENDENT
@AbapCatalog.deliveryClass: #APPLICATION_DATA
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS table entity, composition'
define table entity DEMO_CDS_TE_TO_PARENT_1
{
  key key_el : abap.int4;
      col1   : abap.char(1);
      _to_parent: association to parent DEMO_CDS_TE_COMPOS_1 
        on _to_parent.key_el = $projection.key_el;
}
```
