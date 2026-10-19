---
title: "CDS DDL - DEFINE TABLE FUNCTION, element"
source_file: abencds_f1_return_list_element.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Table Functions > CDS DDL - DEFINE TABLE FUNCTION > CDS DDL - DEFINE TABLE FUNCTION, element_list"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE TABLE FUNCTION, element

## Syntax

``` abap
... [@element_annot1] 
    [@element_annot2] 
    ... 
      [KEY] name : typing 
    [@<element_annot1] 
    [@<element_annot2] ...  
```

[`@element_annot1`](abencds_f1_return_list_annotation.md) · [`@element_annot2`](abencds_f1_return_list_annotation.md) · [`typing`](abencds_typing.md) · [`@<element_annot1`](abencds_f1_return_list_annotation.md) · [`@<element_annot2`](abencds_f1_return_list_annotation.md)

### Addition

[1. `... @element_annot ... @<element_annot`](abencds_f1_return_list_element.md#addition-1)

[2. `... KEY`](abencds_f1_return_list_element.md#addition-2)

## Overview

### Description

Specifies an element in the [list of elements](abencds_f1_return_list.md) of a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md). `name` expects a unique element name that complies with the [naming rules](../abap-cds-syntax/abencds_general_syntax_rules.md). The names of the elements are in the same namespace as the [parameters](abencds_f1_func_parameter_list.md) of the table function. Furthermore, `name` cannot contain any slash (/) characters and cannot be a reserved name in ABAP Dictionary. The reserved names that cannot be used are specified in the DDIC database table `TRESE`.

Each element must be typed with an elementary data type [`typing`](abencds_typing.md). This typing determines the data type of the corresponding component of the structured data type represented by the CDS table function and the associated column of the tabular return value `result` of the associated AMDP function implementation.

It is not case-sensitive. The blanks in the comma-separated list are ignored and can be omitted.

## Addition 1

`... @element_annot ... @<element_annot`

### Description

Specifies annotations for the element. The annotations can be specified before the element using [`@element_annot`](abencds_f1_return_list_annotation.md) or after the element using [`@<element_annot`](abencds_f1_return_list_annotation.md).

### Hint

An [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) can be used to assign further technical and semantic properties to an element for evaluation by the ABAP runtime framework. [Framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be used to give the element specific semantic properties for other SAP frameworks.

## Addition 2

`... KEY`

### Description

`KEY` is used to define the current element as a key element of the current [CDS table function](../../abap-glossary/abencds_table_function_glosry.md). Elements of the [element list](abencds_f1_return_list.md) can be defined as key elements, which are coherently grouped at the beginning of the list, whereby the client field of a [client-dependent](abencds_func_client_handling.md) CDS table function is ignored. The key elements of the CDS entity are evaluated as follows if they are used as a data source of a [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) statement in ABAP SQL:

- By the addition [`ORDER BY PRIMARY KEY`](../../abap-programming-language/abap-database-access/abaporderby_clause.md).

- In implicit [access control](../../abap-glossary/abencds_access_control_glosry.md).

  If a CDS role defined for a CDS entity is evaluated when the entity is accessed, its key elements must identify a unique row in the result set. If this is not the case, the internal instance of access control can produce duplicate entries or even incorrect results when aggregate functions are used. If a unique key cannot be determined for a CDS entity, no key element should be defined. A different instance of access control is then produced internally, which is less efficient.

Apart of that, the key elements of the CDS entity are used to document the semantics of the data model. The addition `KEY` is then ignored when the CDS table function is activated and when other accesses are performed in program executions.

**Caution**

The key elements of a CDS entity do not define unique lines in its result with regard to the key. An application or framework accessing a CDS entity must expect duplicate entries for the key fields in the result set. If the lines of a result set should be unique in respect to a set of key elements, it is the task of the application or framework that provides the CDS entity to define them appropriately and to document the view accordingly.

### Hints

- In the ABAP SQL syntax check, the key elements are used in places where the key is respected.

- The key elements are not relevant for the uniqueness of rows within the result set of the CDS table function, which means that exceptions can be raised when making assignments to internal tables with appropriately unique table keys.
