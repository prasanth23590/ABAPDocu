---
title: "CDS DDL - CDS View Entity, Elementary CDS Operands"
source_file: abencds_operands_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, Elementary CDS Operands

## Syntax

``` abap
... literal 
  | field 
  | EnumType.#EnumConstant 
  | $parameters.pname 
  | $session.vname ...  
```

[`literal`](abencds_literal_v2.md) · [`field`](abencds_field_v2.md) · [`EnumType.#EnumConstant`](abencds_enum_field_v2.md) · [`$parameters.pname`](abencds_parameter_v2.md) · [`$session.vname`](abencds_session_variable_v2.md)

## Description

Specifies a literal [`literal`](abencds_literal_v2.md), a field [`field`](abencds_field_v2.md), an [enumerated constant](../../abap-glossary/abenenumerated_constant_glosry.md) [`EnumType.#EnumConstant`](abencds_enum_field_v2.md), a parameter [`$parameters.pname`](abencds_parameter_v2.md), or a session variable [`$session.vname`](abencds_session_variable_v2.md) as an elementary [CDS operand](../../abap-glossary/abencds_operand_glosry.md) in a CDS DDL operand position.
