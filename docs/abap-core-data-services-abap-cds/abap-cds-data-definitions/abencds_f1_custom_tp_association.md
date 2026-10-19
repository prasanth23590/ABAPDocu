---
title: "CDS DDL - DEFINE CUSTOM ENTITY, To-Parent Association"
source_file: abencds_f1_custom_tp_association.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Custom Entities > CDS DDL - DEFINE CUSTOM ENTITY > CDS DDL - DEFINE CUSTOM ENTITY, element_list > CDS DDL - DEFINE CUSTOM ENTITY, element"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE CUSTOM ENTITY, To-Parent Association

## Syntax

``` abap
... ASSOCIATION TO PARENT target ON $projection.cds_cond ...  
```

[`cds_cond`](abencds_conditional_expression_v2.md)

## Description

Defines a [CDS to-parent association](../../abap-glossary/abento_parent_association_glosry.md) in the [element list](abencds_f1_custom_element_list.md) of a [CDS custom entity](abencds_f1_define_custom_entity.md).

The CDS to-parent association associates the current CDS entity, as a [association source](../../abap-glossary/abenassociation_source_glosry.md), with the [association target](../../abap-glossary/abenassociation_target_glosry.md) `target` specified in the definition of the CDS to-parent association.

CDS to-parent associations are specialized [CDS associations](../../abap-glossary/abencds_association_glosry.md) and the same rules apply as described in topic [CDS DDL - CDS View Entity, `ASSOCIATION TO PARENT`](abencds_to_parent_assoc_v2.md). The only difference is that the addition `AS_assoc` is not used. The name of the to-parent association is declared using the name `_to_parent` in the [element list](abencds_f1_custom_element.md) of the CDS custom entity.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following DDL source code shows a CDS custom entity that defines a CDS to-parent association to another CDS custom entity:

``` abap
@EndUserText.label: 'Child custom entity'
define custom entity DEMO_SALES_CUSTOM_CHILD
  {
    key id          : abap.char(20);
        parent_id   : abap.char(20);
        item_number : abap.char(20);
        type_code   : abap.char(5);
        _items      : 
          association to parent demo_sales_custom_composition
          on _items.id = $projection.id;
  }
```
