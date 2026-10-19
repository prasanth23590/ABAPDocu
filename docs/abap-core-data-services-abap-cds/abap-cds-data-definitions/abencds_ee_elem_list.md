---
title: "CDS DDL - DEFINE EXTERNAL ENTITY, element_list"
source_file: abencds_ee_elem_list.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - External Entities > CDS DDL - DEFINE EXTERNAL ENTITY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE EXTERNAL ENTITY, element_list

## Syntax

``` abap
... { element1; element2; ...; } ...  
```

[`element1`](abencds_ee_element.md) · [`element2`](abencds_ee_element.md)

## Description

Defines the elements of a [CDS external entity](../../abap-glossary/abencds_external_entity_glosry.md). The elements are specified in a semicolon-separated list [`element1`](abencds_ee_element.md); [`element2`](abencds_ee_element.md); ...; in curly brackets `{ }`. The last element must also be followed by a semicolon.

The elements must reflect the structure of the remote data source. The (external) names of the elements must be identical to the element names of the remote database object and the data types must match. The elements determine the components of the structured data types represented by a CDS external entity with respect to ABAP.

The ABAP data types of the components of the structured data type are derived from the dictionary types of the elements in accordance with the corresponding [mapping rules](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).
