---
title: "CDS DDL - projection_list, Transactional Query"
source_file: abencds_proj_view_element_list.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Queries"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - projection_list, Transactional Query

## Syntax

``` abap
... element1, element2, ...  
```

[`element1`](abencds_proj_view_element.md) · [`element2`](abencds_proj_view_element.md)

## Description

Defines the [elements](abencds_proj_view_element.md) of a CDS projection view of type transactional query. The elements are specified in a comma-separated list in curly brackets { }.

The names of the elements of a projection view must be unique. These are either

- the names of the elements taken from the data sources, or

- alternative element names specified using `AS`.
