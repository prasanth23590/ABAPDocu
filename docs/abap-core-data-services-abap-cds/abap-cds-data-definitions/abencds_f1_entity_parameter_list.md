---
title: "CDS DDL - DEFINE ABSTRACT ENTITY, parameter_list"
source_file: abencds_f1_entity_parameter_list.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Abstract Entities > CDS DDL - DEFINE ABSTRACT ENTITY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE ABSTRACT ENTITY, parameter_list

## Syntax

``` abap
... WITH PARAMETERS parameter1, parameter2, ...  
```

[`parameter1`](abencds_f1_param.md) · [`parameter2`](abencds_f1_param.md)

## Description

Defines [CDS parameters](../../abap-glossary/abencds_parameter_glosry.md) [`parameter1`](abencds_f1_param.md), [`parameter2`](abencds_f1_param.md), ... as input parameters of an [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) in a comma-separated list.

Currently, input parameters called `pname` are used only to model the interface of an abstract entity. They cannot be used as operands in the CDS abstract entity.

## Hint

An input parameter cannot be specified as an element in the element list.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following DDL source code shows a CDS abstract entity with input parameters:

``` abap
define abstract entity demo_cds_abstract_entity_para
  with parameters
    @EndUserText.label: 'Date parameter'
    p1 : abap.dats,
    @EndUserText.label: 'Integer parameter'
    p2 : abap.int4,
    @EndUserText.label: 'Simple type parameter'
    p3 : DEMO_BT_CHAR_TEXT
  {
    key col1 : abap.char(3);
        col2 : abap.int4;
  }
```

The class `CL_DEMO_CDS_ABSTRCT_ENTTY_PARA` shows that the parameter annotations of the CDS abstract entity can be evaluated using the class `CL_DD_DDL_ANNOTATION_SERVICE`.
