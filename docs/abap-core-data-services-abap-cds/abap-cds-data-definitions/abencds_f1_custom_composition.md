---
title: "CDS DDL - DEFINE CUSTOM ENTITY, COMPOSITION"
source_file: abencds_f1_custom_composition.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Custom Entities > CDS DDL - DEFINE CUSTOM ENTITY > CDS DDL - DEFINE CUSTOM ENTITY, element_list > CDS DDL - DEFINE CUSTOM ENTITY, element"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE CUSTOM ENTITY, COMPOSITION

## Syntax

``` abap
... COMPOSITION [cardinality] [OF] target ...  
```

[`cardinality`](abencds_cardinality_v2.md)

## Description

Defines a [to-child association](../../abap-glossary/abento_child_association_glosry.md) in the [element list](abencds_f1_custom_element_list.md) of a [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md).

The to-child association associates the current CDS entity, as a [composition source](../../abap-glossary/abencomposition_source_glosry.md), with the [composition target](../../abap-glossary/abencomposition_target_glosry.md) `target` specified in the definition of the to-child association.

To-child associations are specialized [CDS associations](../../abap-glossary/abencds_association_glosry.md) and they work in the same way as described in topic [CDS DDL - CDS View Entity, `COMPOSITION`](abencds_composition_v2.md). The only difference is that in CDS to-child associations in CDS custom entities, the addition `AS` is not used. The name of the to-child association is declared using the name `_compos` in the element list of the CDS custom entity.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following DDL source code shows a CDS custom entity that defines a CDS to-child association to another CDS custom entity:

``` abap
@EndUserText.label: 'SO Custom Entity with association'
define root custom entity DEMO_SALES_CUSTOM_COMPOSITION
  {
    key id            : abap.char(20);
        seller_id     : abap.char(20);
        buyer_id      : abap.char(20);
        act_indicator : abap.char( 1 );
        type_code     : abap.char( 5 );
        _items        : composition of exact one to one 
                          DEMO_SALES_CUSTOM_CHILD;
  }
```
