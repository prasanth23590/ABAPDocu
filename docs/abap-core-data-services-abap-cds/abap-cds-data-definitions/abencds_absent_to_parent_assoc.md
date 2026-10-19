---
title: "CDS DDL - DEFINE ABSTRACT ENTITY, to-parent association"
source_file: abencds_absent_to_parent_assoc.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Abstract Entities > CDS DDL - DEFINE ABSTRACT ENTITY > CDS DDL - DEFINE ABSTRACT ENTITY, element_list > CDS DDL - DEFINE ABSTRACT ENTITY, element"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE ABSTRACT ENTITY, to-parent association

## Syntax

``` abap
... ASSOCIATION TO PARENT target [ON $projection.cds_cond] ...  
```

[`cds_cond`](../abap-cds-obsolete-language-elements/abencds_conditional_expression_v1.md)

## Description

Defines a [CDS to-parent association](../../abap-glossary/abento_parent_association_glosry.md) in the [element list](abencds_f1_absent_list_element.md) of an [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md).

The CDS to-parent association associates the current CDS entity, as a [association source](../../abap-glossary/abenassociation_source_glosry.md), with the [association target](../../abap-glossary/abenassociation_target_glosry.md) `target` specified in the definition of the CDS to-parent association.

CDS to-parent associations are specialized [CDS associations](../../abap-glossary/abencds_association_glosry.md) and the same rules apply as described in topic [CDS DDL - CDS View Entity, `ASSOCIATION TO PARENT`](abencds_to_parent_assoc_v2.md). There is only one exception to the rules described in topic [CDS DDL - CDS View Entity, `ASSOCIATION TO PARENT`](abencds_to_parent_assoc_v2.md): If the association target of a to-parent association is another CDS abstract entity, then the `ON` condition is not mandatory and can be left out.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following DDL source code shows a CDS abstract entity that defines a CDS to-parent association to another CDS abstract entity:

``` abap
@EndUserText.label: 'CDS abstract entity, to-parent assoc'
define abstract entity DEMO_CDS_ABSTRACT_CHILD
{
  key key_field  : abap.char(1);
      data_field : abap.int4;
      _to_parent : association to parent DEMO_CDS_ABSTRACT_COMPOSITION 
                     on _to_parent.key_field = $projection.key_field;
}
```
