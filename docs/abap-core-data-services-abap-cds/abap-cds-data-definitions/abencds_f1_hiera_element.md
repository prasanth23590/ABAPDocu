---
title: "CDS DDL - DEFINE HIERARCHY, element"
source_file: abencds_f1_hiera_element.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Hierarchies > CDS DDL - DEFINE HIERARCHY > CDS DDL - DEFINE HIERARCHY, element_list"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE HIERARCHY, element

## Syntax

``` abap
... [@element_annot1] 
    [@element_annot2] 
    ... 
       [KEY] { _assoc                   [AS alias] } 
           | { element                  [AS alias] } 
           | { $node.hierarchy_attribute AS alias  } 
    [@<element_annot1] 
    [@<element_annot2]  ...  
```

[`@element_annot1`](abencds_f1_hiera_elem_annotation.md) · [`@element_annot2`](abencds_f1_hiera_elem_annotation.md) · [`@<element_annot1`](abencds_f1_hiera_elem_annotation.md) · [`@<element_annot2`](abencds_f1_hiera_elem_annotation.md)

### Alternative

[1. `... _assoc`](abencds_f1_hiera_element.md#alternative-1)

[2. `... element`](abencds_f1_hiera_element.md#alternative-2)

[3. `... $node.hierarchy_attribute`](abencds_f1_hiera_element.md#alternative-3)

### Addition

[1. `... @element_annot ... @<element_annot`](abencds_f1_hiera_element.md#addition-1)

[2. `... KEY`](abencds_f1_hiera_element.md#addition-2)

[3. `... AS alias`](abencds_f1_hiera_element.md#addition-3)

## Overview

### Description

Specifies an element in the [element list](abencds_f1_hiera_element_list.md) of a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md). The names of the elements in a CDS hierarchy must be unique and must be in the same namespace as the [parameters](abencds_f1_hiera_parameter_list.md) of the CDS hierarchy.

## Alternative 1

`... _assoc`

### Description

`_assoc` can be used to make the CDS hierarchy expose a [CDS association](../../abap-glossary/abencds_association_glosry.md) that itself is exposed by the CDS view `cds_view` specified after [`SOURCE`](abencds_f1_define_hierarchy.md) in its `SELECT` list. The name of a CDS association can be specified for `_assoc` but path expressions are not possible.

The CDS hierarchy exposes the CDS association for use in CDS views or in ABAP SQL:

- A CDS view can evaluate the CDS association in its path expressions ([CDS DDIC-based view (obsolete)](../abap-cds-obsolete-language-elements/abencds_path_expression_v1.md), [CDS view entity](abencds_path_expression_v2.md)).

- The CDS association can be used in ABAP SQL [path expressions](../../abap-programming-language/abap-database-access/abenabap_sql_path.md).

The current CDS hierarchy is the [association source](../../abap-glossary/abenassociation_source_glosry.md) of the exposed CDS association and any join expressions created for a path expression from the CDS association use the current CDS hierarchy as their left side. All fields of the [association source](../../abap-glossary/abenassociation_source_glosry.md) of the CDS association that occur in the `ON` condition must also be specified as elements of the current element list.

A CDS association exposed in this way is, like any element, part of the element list. It is not, however, part of the result set or a component of a type defined in ABAP with respect to the CDS hierarchy. If no alternative element name `alias` is defined, the element name is defined by the name of the CDS association.

### Hint

When a CDS association is exposed, care should be taken that the exposing hierarchy itself is the [association source](../../abap-glossary/abenassociation_source_glosry.md) of the exposed CDS association and not the data source of the view. More specifically, when CDS associations are exposed that were already exposed by the source of the hierarchy, the hierarchy replaces the original view as the [association source](../../abap-glossary/abenassociation_source_glosry.md) of the CDS association. The left side of an instance of a join expression created for the exposed CDS association is the result set of the hierarchy.

## Alternative 2

`... element`

### Description

`element` can be used to specify an element of the CDS view `cds_view` specified after [`SOURCE`](abencds_f1_define_hierarchy.md). This element is part of the result set of the CDS hierarchy and a component of a type defined in ABAP with respect to the CDS hierarchy.

### Hint

When the hierarchy is accessed in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), the element is a regular component of the [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) in the results list, if `*` or `...~*` are used in the `SELECT` list.

## Alternative 3

`... $node.hierarchy_attribute`

### Description

`$node.hierarchy_attribute` can be used to specify a [hierarchy attribute](../../abap-glossary/abenhierarchy_attribute_glosry.md) `hierarchy_attribute` after the prefix `$node`. The names of all [hierarchy attributes](abencds_hierarchy_attributes.md) can be specified for `hierarchy_attribute`. In this case, `AS ALIAS` must be used to define an alternative element name, which cannot be the name of a hierarchy attribute.

This element is part of the result set of the CDS hierarchy and a component of a type defined in ABAP with respect to the CDS hierarchy. When the CDS hierarchy is accessed, the element contains the respective value of the hierarchy attribute for each row.

### Hints

- When the hierarchy is defined in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), the element is a regular component of the [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) in the results list, if `*` or `...~*` are used in the `SELECT` list.

- When the hierarchy is accessed in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), the associated additional [hierarchy column](../../abap-glossary/abenhierarchy_column_glosry.md) can be used to access the hierarchy attribute.

- It is practical to include a hierarchy attribute in the element list of a CDS hierarchy explicitly either if it is required when other CDS entities access the CDS hierarchy, or if it is a component of a structured type in ABAP that references the CDS hierarchy.

## Addition 1

`... @element_annot`

### Description

Specifies annotations for the element. The annotations can be specified before the element using [`@element_annot`](abencds_f1_hiera_elem_annotation.md) or after the element using [`@<element_annot`](abencds_f1_hiera_elem_annotation.md).

### Hint

Element annotations can be used to annotate the elements and CDS associations of a CDS hierarchy with semantic properties.

## Addition 2

`... KEY`

### Description

`KEY` is used to define the current element as a key element of the current [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md). Those elements of the [element list](abencds_f1_hiera_element_list.md) can be defined as key elements that are placed without gaps at the start of the list. The key elements of the CDS entity are evaluated as follows if they are used as a data source of a [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) statement in ABAP SQL:

- By the addition [`ORDER BY PRIMARY KEY`](../../abap-programming-language/abap-database-access/abaporderby_clause.md).

- In implicit [access control](../../abap-glossary/abencds_access_control_glosry.md).

  If a CDS role defined for a CDS entity is evaluated when the entity is accessed, its key elements must identify a unique row in the result set. If this is not the case, the internal instance of access control can produce duplicate entries or even incorrect results when aggregate functions are used. If a unique key cannot be determined for a CDS entity, no key element should be defined. A different instance of access control is then produced internally, which is less efficient.

Otherwise, the key elements of the CDS entity are used to document the semantics of the data model. The addition `KEY` is then ignored when the CDS hierarchy is activated and when other accesses are performed in program executions.

**Caution**

The key elements of a CDS entity do not define unique lines in its result with regard to the key. An application or framework accessing a CDS entity must expect duplicate entries for the key fields in the result set. If the lines of a result set should be unique in respect to a set of key elements, it is the task of the application or framework that provides the CDS entity to define them appropriately and to document the view accordingly.

### Hints

- In the ABAP SQL syntax check, the key elements are used in places where the key is respected.

- The key elements are not relevant for the uniqueness of rows within the result set of the CDS hierarchy, which means that exceptions can be raised when making assignments to internal tables with appropriately unique table keys.

## Addition 3

`... AS alias`

### Description

Defines an alternative element name for the current element. The alternative element name replaces the actual name of the element. When the current CDS hierarchy is accessed, the alternative element names must be used instead of the actual name.
