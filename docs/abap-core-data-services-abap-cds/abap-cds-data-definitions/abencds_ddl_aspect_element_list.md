---
title: "CDS DDL - CDS Aspect, element_list"
source_file: abencds_ddl_aspect_element_list.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Aspects > CDS DDL - DEFINE ASPECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Aspect, element_list

## Syntax

``` abap
... { element1; element2; ... }  
```

[`element1`](abencds_aspect_element.md) · [`element2`](abencds_aspect_element.md)

## Description

Defines an element of a [CDS DDL aspect](abencds_ddl_aspect_glosry.md). The elements can be specified in a list separated by semicolons: `element1`; `element2` ...

The names of the elements of a CDS aspect must be unique to the fields included in the CDS DDL aspect as well as the entities that the aspect is to be included in.
