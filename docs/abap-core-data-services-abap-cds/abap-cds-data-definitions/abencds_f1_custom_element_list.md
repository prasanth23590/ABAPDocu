---
title: "CDS DDL - DEFINE CUSTOM ENTITY, element_list"
source_file: abencds_f1_custom_element_list.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Custom Entities > CDS DDL - DEFINE CUSTOM ENTITY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE CUSTOM ENTITY, element_list

## Syntax

``` abap
... { element1; element2; ...; } ...  
```

[`element1`](abencds_f1_custom_element.md) · [`element2`](abencds_f1_custom_element.md)

## Description

Defines the elements of a [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md). The elements are specified in a semicolon-separated list [`element1`](abencds_f1_custom_element.md); [`element2`](abencds_f1_custom_element.md); ...; in curly brackets `{ }`. The final element must also be followed by a semicolon.

The elements either determine the components of the structured data type represented by the CDS custom entity with respect to ABAP, or they define and expose a [CDS association](abencds_f1_custom_association.md), a [CDS to-child association](../../abap-glossary/abento_child_association_glosry.md), or a [CDS to-parent association](abencds_f1_custom_tp_association.md).

The ABAP data types of the components of the structured data type are derived from the dictionary types of the elements in accordance with the associated [mapping rules](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).
