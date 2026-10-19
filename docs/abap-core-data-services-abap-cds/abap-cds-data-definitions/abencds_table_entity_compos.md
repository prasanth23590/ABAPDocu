---
title: "CDS DDL - CDS Table Entity, COMPOSITION"
source_file: abencds_table_entity_compos.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Table Entities > CDS DDL - DEFINE TABLE ENTITY > CDS DDL - CDS Table Entity, element_list > CDS DDL - CDS Table Entity, element"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Table Entity, COMPOSITION

## Syntax

``` abap
... COMPOSITION [cardinality] OF target ...  
```

[`cardinality`](abencds_cardinality_v2.md)

## Description

Defines a [to-child association](../../abap-glossary/abento_child_association_glosry.md) in the [element list](abencds_table_entity_element_list.md) of a [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md).

The to-child association associates the current CDS entity, as a [composition source](../../abap-glossary/abencomposition_source_glosry.md), with the [composition target](../../abap-glossary/abencomposition_target_glosry.md) `target` specified in the definition of the to-child association.

To-child associations are specialized [CDS associations](../../abap-glossary/abencds_association_glosry.md) and they work in the same way as described in topic [CDS DDL - CDS View Entity, `COMPOSITION`](abencds_composition_v2.md) with the following differences:

- In CDS to-child associations in table entities, the addition `AS` is not used. The name of the to-child association is declared using the name `_compos` in the element list of the CDS table entity.

- The cardinality must be written in words. The numeric notation is not available in table entities.

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
