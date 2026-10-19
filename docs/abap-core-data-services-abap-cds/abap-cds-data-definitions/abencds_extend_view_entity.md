---
title: "CDS DDL - EXTEND VIEW ENTITY"
source_file: abencds_extend_view_entity.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entity Extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - EXTEND VIEW ENTITY

## Syntax

``` abap
 
EXTEND VIEW ENTITY cds_view_entity | projection_view 
       WITH 
            [association1 
             association2 ...] 
            { select_list_extension } 
            [GROUP BY field1, field2, ...  ] 
            [EXCEPT   | INTERSECT   | UNION [ALL]  { ... }] [;]  
```

### Addition

[1. `... GROUP BY field1, field2, ...`](abencds_extend_view_entity.md#addition-1)

[2. ... EXCEPT\|INTERSECT\|UNION \[ALL\] { ... }](abencds_extend_view_entity.md#addition-2)

## Overview

### Description

Extends an existing [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) `cds_view_entity` or an existing [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md) `projection_view` using a [CDS view entity extension](../../abap-glossary/abencds_view_entity_extend_glosry.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). An existing CDS view can have one or more CDS view entity extensions.

## Prerequisite

As a prerequisite for the extension of the CDS entity with the statement `EXTEND VIEW ENTITY`, the elements of the [annotation array](../../abap-glossary/abenannotation_array_glosry.md) [`AbapCatalog.viewEnhancementCategory[ ]`](abencds_view_entity_anno.md) must be specified accordingly in its definition with [`DEFINE VIEW ENTITY`](abencds_define_view_entity.md):

- By default or if only the value `#PROJECTION_LIST` is specified, views without [aggregate expressions](abencds_aggregate_functions_v2.md) in the `SELECT` list and without a [set-operator](abencds_set_operators.md) clause can be extended.

- In order to extend views that have [aggregate expressions](abencds_aggregate_functions_v2.md) in the `SELECT` list, the annotation array must contain the value `#GROUP_BY` alongside `#PROJECTION_LIST`.

- In order to extend views that contain set-operator clauses, the annotation array must contain the value `#UNION` alongside `#PROJECTION_LIST`.

  **Note:** The annotation array value `#UNION` allows extensions not only for union views, but for views including any set operator (also [`EXCEPT`](abencds_except_v2.md) and [`INTERSECT`](abencds_intersect_v2.md)). The annotation array value `#UNION` is a known misnomer.

- If the annotation array contains the value `#NONE`, the view cannot be extended.

Additionally, the annotation [`AbapCatalog.extensibility.extensible`](abencds_f1_entity_annotations.md) must not be set to ` false`.

**Components of a View Entity Extension**

View entity extensions can make additions to the original view, but they cannot modify, overwrite, or delete elements from the original view. The following components are possible in a CDS view entity extension:

- New associations `association1`, `association2` can be defined and exposed in the CDS view entity extension. The same rules apply that are described in topic [CDS DDL - CDS view entity, `ASSOCIATION`](abencds_simple_association_v2.md).

  **Note:** It is **not** allowed to define new [CDS to-parent associations](../../abap-glossary/abento_parent_association_glosry.md) in a view entity extension. New [to-child associations](../../abap-glossary/abento_child_association_glosry.md) are allowed under the condition that the association target is also defined as composition child and has the required to-parent association.

- When extending a CDS projection view, the view entity extension can specify all features that are possible in a projection view, such as [CDS virtual elements](../../abap-glossary/abencds_virtual_element_glosry.md), [CDS localized field](../../abap-glossary/abencds_localized_field_glosry.md), and [redefined](abencds_proj_view_redefined_assoc.md) and [redirected associations](abencds_pv_assoc_redirected.md). See topic [CDS DDL - `projection_list`, Transactional Query](abencds_proj_view_element_list.md) for a complete list.

- When extending a CDS view entity, the view entity extension can specify all features that are possible in a view entity, such as [path expressions](abencds_path_expression_v2.md), [elementary operands](abencds_operands_v2.md), [expressions](abencds_expressions_v2.md) and [functions](abencds_builtin_functions_v2.md). See topic [CDS DDL - CDS View Entity, `SELECT`, `element`](abencds_select_list_entry_v2.md) for a complete list.

- Each appended element must have a unique name. If an appended element already occurs in the existing `SELECT` list or in a different extension, the element must be given an alternative element name using `AS`.

## Restrictions

- CDS view entity extensions themselves cannot be extended.

- It is not possible to specify new [input parameters](abencds_parameter_v2.md) in a view entity extension.

- No addition [`ROOT`](../abap-cds-obsolete-language-elements/abencds_define_root_view_v1.md) can be specified in the statement `EXTEND VIEW ENTITY` to transform a regular view to a [root entity](../../abap-glossary/abenroot_entity_glosry.md).

- An appended field cannot be defined as a [`KEY`](abencds_builtin_functions_v2.md) field.

- In a view entity extension, header annotations are not supported. That means that no annotations are allowed in front of the statement `EXTEND VIEW ENTITY`.

- For views that have an element of data type `LRAW` or `LCHR` in the `SELECT` list, no view extension is possible and the annotation `AbapCatalog.viewEnhancementCategory[#NONE]` is enforced. The reason is that elements of data types `LRAW` or `LCHR` must always be in the last position of the `SELECT` list.

- It is not possible enable both [buffering](abencds_v2_view_buffering.md) and extensions for a view entity. If the annotation [`@AbapCatalog.entityBuffer.definitionAllowed`](abencds_view_entity_anno.md) is set to `true`, extensions are not allowed.

- CDS view entity extensions **cannot** append fields of CDS projection views, CDS custom entities, or CDS abstract entities to a CDS view entity. Fields of CDS projection views, CDS abstract entities, or CDS custom entities can - generally - **not** be used in path expressions and this also holds true for path expressions in CDS view entity extensions.

  This is **not** valid: `extend view entity MyExtension with { _assocToAbstract.field1 as Alias1 _assocToCustom.field2 as Alias2 _assocToProjection.field3 as Alias3 }`

### Hint

It is not allowed to use inner joins in extensions, since it would affect the result cardinality of the extended view and would therefore represent a modification, which is not allowed. Inner joins, for example in the form of path expressions with a join attribute, lead to syntax check errors.

## Addition 1

`... GROUP BY field1, field2, ...`

### Description

This addition must be specified if elements not defined using aggregate expressions are added to a view with [aggregate expressions](abencds_aggregate_functions_v2.md). These elements must be specified after `GROUP BY` and they extend the [`GROUP-BY`](abencds_group_by_v2.md) clause of the original view. With respect to the extended view, the extended `GROUP-BY` clause must follow the general rules for a `GROUP-BY` clause.

As a prerequisite, the definition of the original view must contain at least one aggregate expression in its `SELECT` list.

### Hint

Extensions of a view with aggregate expressions require it to contain the annotation array `viewEnhancementCategory[ ]` with the values `#PROJECTION` and `#GROUP_BY`.

## Addition 2

` ... EXCEPT | INTERSECT | UNION [ALL]`

### Description

This addition must be specified when a view entity with a [set operator](../../abap-glossary/abencds_set_operators_glosry.md) ([`EXCEPT`](abencds_except_v2.md), [`INTERSECT`](abencds_intersect_v2.md), or [`UNION`](abencds_union_v2.md)) is extended. A corresponding addition ([`EXCEPT`](abencds_except_v2.md), [`INTERSECT`](abencds_intersect_v2.md), or [`UNION`](abencds_union_v2.md)) must be specified for each clause of the original view. The curly brackets can contain elements that extend the `SELECT` list of the associated set-operator clause of the original view. As specified by the `SELECT` list extended using `select_list_extension`, the set-operator clauses must be extended so that the rules for set-operator clauses are not broken in the extended view.

The addition `ALL` is available only for `UNION` views and it must be specified each time it is specified in the associated `UNION` clause of the original view.

As a prerequisite, the original view must have a set-operator clause.

### Hint

Extensions of a view with set-operator clauses require it to contain the annotation array `viewEnhancementCategory[ ]` with the values`#PROJECTION_LIST` and `#UNION`.
