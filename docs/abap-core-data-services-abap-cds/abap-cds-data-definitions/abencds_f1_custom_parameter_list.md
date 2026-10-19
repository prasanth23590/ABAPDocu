---
title: "CDS DDL - DEFINE CUSTOM ENTITY, parameter_list"
source_file: abencds_f1_custom_parameter_list.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Custom Entities > CDS DDL - DEFINE CUSTOM ENTITY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE CUSTOM ENTITY, parameter_list

## Syntax

``` abap
... WITH PARAMETERS parameter1, parameter2, ...  
```

[`parameter1`](abencds_f1_param.md) · [`parameter2`](abencds_f1_param.md)

## Description

Defines [CDS parameters](../../abap-glossary/abencds_parameter_glosry.md) [`parameter1`](abencds_f1_param.md), [`parameter2`](abencds_f1_param.md), ... as input parameters of a CDS custom entity in a comma-separated list.

An input parameter called `pname` is used to model the interface of a CDS custom entity. It cannot be used in the [element list](abencds_f1_custom_element_list.md) of the CDS custom entity.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following DDL source code shows a CDS custom entity with an input parameter:

``` abap
@EndUserText.label: 'CDS custom entity, query implementation'
@ObjectModel.query.implementedBy: 'ABAP:CL_DEMO_CUSTOM_ENTITY_QUERY'
define custom entity DEMO_CDS_CUSTOM_ENTITY
  with parameters
    p_number : int1
  {
    key id   : int4;
        uuid : abap.char(32);
  }
```

This CDS custom entity is used in the [executable example for implementing a custom entity](abencds_custom_query_abexa.md).
