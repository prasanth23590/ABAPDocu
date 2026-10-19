---
title: "CDS DDL - DEFINE HIERARCHY, parameter_list"
source_file: abencds_f1_hiera_parameter_list.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Hierarchies > CDS DDL - DEFINE HIERARCHY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE HIERARCHY, parameter_list

## Syntax

``` abap
... WITH PARAMETERS parameter1, parameter2, ...  
```

[`parameter1`](abencds_f1_param.md) · [`parameter2`](abencds_f1_param.md)

## Description

Defines [CDS parameters](../../abap-glossary/abencds_parameter_glosry.md) [`parameter1`](abencds_f1_param.md), [`parameter2`](abencds_f1_param.md), ... as input parameters of a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md) in a comma-separated list.

An input parameter called `pname` can be used as an operand in the following places of the [`DEFINE HIERARCHY`](abencds_f1_define_hierarchy.md) statement using the same syntax [`:pname`](../abap-cds-obsolete-language-elements/abencds_parameter_v1.md) or [`$parameters.pname`](../abap-cds-obsolete-language-elements/abencds_parameter_v1.md) as in CDS DDIC-based views (obsolete):

- As operands after [`VALID FROM ... TO`](abencds_f1_define_hierarchy.md) in the addition `PERIOD`.

- As an operand on the right side of the start condition after [`START WHERE`](abencds_f1_define_hierarchy.md).

- As an operand on the right side of the directory condition after [`DIRECTORY FILTER BY`](abencds_f1_define_hierarchy.md).

- As an operand after [`DEPTH`](abencds_f1_define_hierarchy.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Defines an input parameter in a CDS hierarchy and its use after `START WHERE`. The class `CL_DEMO_HIERARCHY_TREE` accesses the CDS hierarchy and passes an actual parameter to the input parameter.

``` abap
define hierarchy DEMO_CDS_SIMPLE_TREE
  with parameters
    p_id : abap.int4
  as parent child hierarchy(
    source
      DEMO_CDS_SIMPLE_TREE_SOURCE
      child to parent association _tree
      start where
        id = :p_id
      siblings order by
        id ascending
    )
    {
      id,
      parent,
      name
    }
```
