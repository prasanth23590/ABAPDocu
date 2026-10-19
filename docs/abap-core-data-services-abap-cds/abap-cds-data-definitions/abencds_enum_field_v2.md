---
title: "CDS DDL - CDS View Entity, EnumConstant"
source_file: abencds_enum_field_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Elementary CDS Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, EnumConstant

## Syntax

``` abap
... EnumType.#EnumConstant ...  
```

## Description

Specifies an [enumerated constant](../../abap-glossary/abenenumerated_constant_glosry.md) `EnumConstant` of a [CDS enumerated type](../../abap-glossary/abencds_enum_type_glosry.md) `EnumType` in the `SELECT` list of a CDS view entity. An enumerated constant `EnumConstant` defines a value of the value set of an enumerated type. A CDS enumerated constant is specified using the name of the enumerated type `EnumType`, followed by a period (.), a hash character (#), and the name of an enumerated constant `EnumConstant`. An enumerated constant has the data type `ENUM`.

## More Information

- [ABAP CDS - Enumerated Types](abencds_enumeration_types.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS view entity shown below specifies the element `friday` as enumerated constant in the `SELECT` list.

``` abap
@EndUserText.label: 'CDS view entity, enumerated types'

define view entity DEMO_CDS_ENUM_TYPE_USAGE_1
  as select from demo_expressions
{
  key id                       as Id,
  num1 as integer1,
      DEMO_CDS_ENUM_STACK.#FRI as friday
}
```
