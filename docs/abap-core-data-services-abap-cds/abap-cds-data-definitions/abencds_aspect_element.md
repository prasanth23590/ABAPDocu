---
title: "CDS DDL - CDS Aspect, element"
source_file: abencds_aspect_element.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Aspects > CDS DDL - DEFINE ASPECT > CDS DDL - CDS Aspect, element_list"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Aspect, element

## Syntax

``` abap
... {  [@element_annot1] 
       [ @element_annot2] 
       ... 
       { [KEY]      element1 : element1_type; } 
     | { [VIRTUAL]  element2 : arith_expr;    } 
     | {            element4 : case_expr;     } 
     | {            element5 : builtin_func;  } 
                   ... 
    } ...  
```

[`@element_annot1`](abencds_element_annotations_aspect.md) · [`@element_annot2`](abencds_element_annotations_aspect.md) · [`element1_type`](abencds_typing.md) · [`arith_expr`](abencds_arithmetic_expression_v2.md) · [`case_expr`](abencds_case_expression_v2.md) · [`builtin_func`](abencds_builtin_functions_v2.md)

## Overview

### Description

Defines an element of a [`element list`](abencds_ddl_aspect_element_list.md) of a [CDS DDL aspect](abencds_ddl_aspect_glosry.md). The names of the elements in an `element` list must be unique and they are in the same namespace as the [parameters](abencds_parameter_list_v2.md) and [element list](abencds_select_list_entry_v2.md) of the view that the CDS DDL aspect is to be included in.

The types available in CDS aspects are listed in [ABAP CDS - Built-In Data Types](../abap-cds-data-types/abencds_overview_builtin_types.md).

### Addition

[1. `... @element_annot ...`](abencds_aspect_element.md#addition-1)

[2. `... KEY`](abencds_aspect_element.md#addition-2)

[3. `... VIRTUAL`](abencds_aspect_element.md#addition-3)

## Addition 1

`... @element_annot ...`

### Description

Specifies annotations for the element. The annotations must be specified before the element using ` @element_annot`. All possible element annotations are listed in topic [element annotations](abencds_element_annotations_v2.md).

### Hint

An annotation can be used to assign further technical and semantic properties to an element for evaluation by the ABAP runtime framework. [Framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be used to give the element specific semantic properties that are evaluated by other SAP frameworks.

## Addition 2

`... KEY`

### Description

The keyword `KEY` is used to define the current element as a key element of the current CDS aspect. All key elements must be placed without gaps at the start of the `element` list and cannot be virtual elements.

## Addition 3

`... VIRTUAL`

### Description

The keyword `VIRTUAL` is used to define the current element as a virtual element of the current CDS aspect. A virtual element cannot also be a key element.
