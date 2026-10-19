---
title: "CDS DDL - CDS Simple Type, simple_type"
source_file: abencds_simple_type.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Type Definitions > CDS DDL - DEFINE TYPE > ABAP CDS - Simple Types > CDS DDL - DEFINE TYPE simple_type"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Simple Type, simple_type

## Syntax

``` abap
... simple_type  ...  
```

## Description

A [CDS simple type](../../abap-glossary/abencds_simple_type_glosry.md) can be typed using another CDS simple type. The annotations of the underlying simple type are inherited. It is possible to overwrite these annotations using locally defined annotations in the overlying simple type.

When stacking CDS simple types, the maximum nesting depth is five. This means that a stack of simple types can have a maximum of five layers, from base to top-most.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS simple type is created with reference to another CDS simple type. It inherits all the properties and annotations of the referenced simple type.

`define type DEMO_SIMPLE_TYPE_2 : DEMO_SIMPLE_TYPE;`
