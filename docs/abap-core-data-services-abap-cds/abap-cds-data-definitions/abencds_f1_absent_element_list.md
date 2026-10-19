---
title: "CDS DDL - DEFINE ABSTRACT ENTITY, element_list"
source_file: abencds_f1_absent_element_list.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Abstract Entities > CDS DDL - DEFINE ABSTRACT ENTITY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE ABSTRACT ENTITY, element_list

## Syntax

``` abap
... { element1; element2; ...; } ...  
```

[`element1`](abencds_f1_absent_list_element.md) · [`element2`](abencds_f1_absent_list_element.md)

## Description

Defines the elements of an [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md). The elements are specified in a semicolon-separated list [`element1`](abencds_f1_absent_list_element.md); [`element2`](abencds_f1_absent_list_element.md); ...; in curly brackets `{ }`. The final element must also be followed by a semicolon.

The elements either determine the components of the structured data type represented by a CDS abstract entity with respect to ABAP or they expose a CDS association, a CDS to-child association, or a CDS-to-parent association.

The ABAP data types of the components of the structured data type are derived from the dictionary types of the elements in accordance with the associated [mapping rules](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).
