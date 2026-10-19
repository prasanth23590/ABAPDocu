---
title: "CDS DDL - CDS Table Entity, element_list"
source_file: abencds_table_entity_element_list.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Table Entities > CDS DDL - DEFINE TABLE ENTITY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Table Entity, element_list

## Syntax

``` abap
... { element1; element2; ... }  
```

[`element1`](abencds_table_entity_element.md) · [`element2`](abencds_table_entity_element.md)

## Description

Defines the elements of a [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md). The elements can be specified in a list separated by semicolons: [`element1`](abencds_table_entity_element.md); [`element2`](abencds_table_entity_element.md) ... in curly brackets `{ }`.

The elements either determine the components of the structured data type represented by the table entity with respect to ABAP, or they define and expose a [CDS association](abencds_table_entity_assoc.md), a [CDS to-child association](abencds_table_entity_compos.md), or a [CDS to-parent association](abencds_table_entity_to_parent.md).

The ABAP data types of the components of the structured data type are derived from the CDS types of the elements in accordance with the associated [mapping rules](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The names of the elements of a CDS table entity must be unique and comply with the naming rules described in the topic [ABAP CDS - General Syntax Rules](../abap-cds-syntax/abencds_general_syntax_rules.md).
