---
title: "CDS DDL - CDS View Entity, parameter"
source_file: abencds_parameter_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Elementary CDS Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, parameter

## Syntax

``` abap
... $parameters.pname ...  
```

## Description

Specifies an input parameter `pname` from the parameter list [`parameter_list`](abencds_parameter_list_v2.md) in an operand position of a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md).

The name of the parameter `pname` must be prefixed by `$parameters.`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The view shown below defines two parameters, `p1` and `p2`, and uses them in the `SELECT` list.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@AbapCatalog.entityBuffer.propagationAllowed:true
define view entity DEMO_CDS_PARAM_VE
  with parameters
    p_p1 : abap.int4,
    p_p2 : abap.int4
  as select from scarr
{
  key carrid,
      $parameters.p_p1 as param1,
      $parameters.p_p2 as param2
}
```
