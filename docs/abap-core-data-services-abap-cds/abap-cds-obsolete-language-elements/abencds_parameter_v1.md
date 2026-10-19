---
title: "CDS DDL - DDIC-Based View, parameter"
source_file: abencds_parameter_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Elementary CDS Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, parameter

## Syntax

``` abap
... :pname|$parameters.pname ...  
```

## Description

Specifies an input parameter `pname` from the parameter list [`parameter_list`](abencds_parameter_list_v1.md) in an operand position of a [`SELECT` statement](abencds_select_statement_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md).

The name of the parameter `pname` must be prefixed by a colon (`:`) or `$parameters.`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specifies the parameters `p1` and `p2` using both syntax options in the [`SELECT` list](abencds_select_list_v1.md).

``` abap
@AbapCatalog.sqlViewName: 'DEMO_SPFLI_PROJ'
define view DEMO_SPFLI_PROJECTION_V1
  with parameters p1 : abap.int4,
                  p2 : abap.int4 as
  select from scarr
         { key carrid,
               :p1 as para1,
               $parameters.p2 as para2
         };
```
