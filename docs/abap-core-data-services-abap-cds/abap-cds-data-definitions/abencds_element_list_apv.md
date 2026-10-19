---
title: "CDS DDL - element_list, Analytical Query"
source_file: abencds_element_list_apv.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Analytical Queries"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - element_list, Analytical Query

## Syntax

``` abap
... element1, element2, ...  
```

[`element1`](abencds_element_apv.md) · [`element2`](abencds_element_apv.md)

## Description

Defines the [elements](abencds_element_apv.md) of a [CDS analytical projection view](../../abap-glossary/abencds_analytical_pv_glosry.md). The elements are specified in a comma-separated list in curly brackets { }.

The names of the elements of an analytical projection view must be unique. These are either

- the names of the elements taken from the data sources, or

- alternative element names specified using `AS`.
