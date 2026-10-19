---
title: "CDS DDL - DEFINE ABSTRACT ENTITY, composition"
source_file: abencds_absent_composition.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Abstract Entities > CDS DDL - DEFINE ABSTRACT ENTITY > CDS DDL - DEFINE ABSTRACT ENTITY, element_list > CDS DDL - DEFINE ABSTRACT ENTITY, element"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE ABSTRACT ENTITY, composition

## Syntax

``` abap
... COMPOSITION [cardinality] [OF] target ...  
```

[`cardinality`](abencds_cardinality_v2.md)

## Description

Defines a [CDS to-child association](../../abap-glossary/abento_child_association_glosry.md) in the [element list](abencds_f1_absent_list_element.md) of a [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md).

The CDS to-child association associates the current CDS abstract entity, as an [association source](../../abap-glossary/abenassociation_source_glosry.md), with the [association target](../../abap-glossary/abenassociation_target_glosry.md) `target` specified in the definition of the to-child association.

CDS to-child associations are specialized [CDS associations](../../abap-glossary/abencds_association_glosry.md) and they work in the same way as described in topic [CDS DDL - CDS View Entity, `COMPOSITION`](abencds_composition_v2.md). The only difference is that in to-child associations in CDS abstract entities, the addition `AS` is not used. The name of the to-child association is declared using the name `_compos` in the element list of the CDS abstract entity.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following DDL source code shows a CDS abstract entity that defines a to-child association to another CDS abstract entity:

``` abap
@EndUserText.label: 'CDS abstract entity, composition'
define root abstract entity DEMO_CDS_ABSTRACT_COMPOSITION
{
  key key_field  : abap.char(1);
      data_field : abap.int4;
      _compos    : composition [0..1] of DEMO_CDS_ABSTRACT_CHILD;
}
```
