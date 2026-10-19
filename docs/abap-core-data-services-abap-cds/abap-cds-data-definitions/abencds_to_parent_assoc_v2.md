---
title: "CDS DDL - CDS View Entity, ASSOCIATION TO PARENT"
source_file: abencds_to_parent_assoc_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - CDS View Entity, SELECT, Associations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, ASSOCIATION TO PARENT

## Syntax

``` abap
... ASSOCIATION TO PARENT target [AS _assoc] ON $projection.cds_cond ...  
```

[`cds_cond`](abencds_conditional_expression_v2.md)

## Description

A [CDS to-parent association](../../abap-glossary/abento_parent_association_glosry.md) in [ABAP CDS](../../abap-glossary/abenabap_core_data_services_glosry.md) is a specialized [CDS association](../../abap-glossary/abencds_association_glosry.md). In combination with a [CDS to-child association](../../abap-glossary/abento_child_association_glosry.md), they define a [CDS composition](../../abap-glossary/abencds_composition_glosry.md) relationship. A CDS to-parent association in defined in the child entity and points to the parent entity. CDS compositions define the [CDS composition tree](../../abap-glossary/abencds_composition_tree_glosry.md) of a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) in the context of the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md).

A to-parent association is defined in a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) using the keyword ` ASSOCIATION TO PARENT`. A to-parent association associates the current CDS entity, as [association source](../../abap-glossary/abenassociation_source_glosry.md), with the [association target](../../abap-glossary/abenassociation_target_glosry.md) `target` specified in the definition of the association.

The child entity must always define a to-parent association first and only afterwards can a to-child association be defined in the parent entity. The other way around results in a syntax error. The to-parent association cannot be deleted as long as the child entity is the target of the to-child association. The to-child association must be deleted first and then the to-parent association can be deleted.

**Rules**

CDS to-parent associations are defined similarly to CDS associations. Here are the similarities and differences:

- Similarities

  - For the name `AS _assoc`, the same rules apply as for normal CDS associations, see topic [CDS DDL - CDS View Entity, `ASSOCIATION`](abencds_simple_association_v2.md).

  - An `ON` condition must be defined. The rules for `ON` conditions of to-parent associations are listed below.

- Differences

  - A default filter cannot be defined for a to-parent association. The syntax `... WITH DEFAULT FILTER ...` is not allowed.

  - The [cardinality](../../abap-glossary/abencardinality_glosry.md) cannot be defined explicitly for to-parent associations and is generated as to-one.

The following applies to the association target target:

- The association target can be another [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), an [abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md), or a [custom entity](../../abap-glossary/abencds_custom_entity_glosry.md).

- The [association target](../../abap-glossary/abenassociation_target_glosry.md) of a to-parent association cannot be the CDS entity in which the to-parent association is defined. This means that to-parent associations cannot be [self associations](../../abap-glossary/abenself_association_glosry.md).

- The target entity of a CDS to-child association and a to-parent association defined in the same data definition must be different entities.

General rules for child entities:

- A child entity must define exactly one to-parent association to its parent entity.

- A child entity that is the target of a to-child association can itself be a parent entity and define further to-child associations.

- A [root entity](../../abap-glossary/abenroot_entity_glosry.md) cannot define any to-parent associations.

- The child entity in which the to-parent association is defined must have at least one [key field](../../abap-glossary/abenkey_field_glosry.md).

Exposure:

- The name of the to-parent association `_assoc` must be added exactly once to the [`select_list`](abencds_select_list_v2.md) of the CDS view entity it is defined in, without attributes and alias. If no name is defined for the to-parent association, the name of the to-parent association is the name of the target entity `target` and this name must be made available in the `SELECT` list.

Usage:

- A to-parent association can be propagated in data definitions other than the one in which it is defined. In this case, the to-parent association uses its special semantics and is handled like a normal CDS association.

- To-parent associations can be used in [path expressions](abencds_path_expression_v2.md) locally and also in other CDS entities in which they are propagated.

- To-parent associations can be specified as values for `AssociationRef` associations. These to-parent associations are then handled as associations.

To-parent associations and joins:

- All use cases and details about join generation described in topic [`CDS DDL - CDS View Entity, Associations and Joins`](abencds_assoc_join_v2.md) also apply to to-parent associations.

Restrictions:

- To-parent associations cannot be defined in a CDS view extension, neither with [`EXTEND VIEW`](abencds_extend_view.md), nor with [`EXTEND VIEW ENTITY`](abencds_extend_view.md).

**`ON` Condition**

A to-parent association must define an ON condition. This ON condition is automatically used for the respective CDS to-child association in the parent entity.

The following rules apply to the operands and syntax of the ON condition:

- Only [key fields](../../abap-glossary/abenkey_field_glosry.md) of the parent entity can be used in the `ON` condition.

- The `ON` condition must use all key fields of the parent entity. Each one can be used only once in the `ON` condition.

- Key fields of the parent entity can only be compared with fields of the child entity.

- A field of the child entity can be used only once.

- The fields of the association source must be prefixed by ` $projection`.

- The fields of the association target must be prefixed by the name of the CDS to-parent association (prefix `_assoc.` separated by a period).

- Only the [comparison operator](abencds_cond_expr_comp_v2.md) *=* is allowed. No other [relational operator](../../abap-glossary/abenrel_operator_glosry.md) or comparison operator is allowed.

- Only the [Boolean operator](../../abap-glossary/abenboolean_operator_glosry.md) `AND` is allowed. Negations using `NOT` are not allowed.

- `lhs` can be a field of the association source or association target.

- `rhs` can be a field of the association source or association target.

- Path expressions, expressions, built-in functions, and elementary operands are not allowed.

- All fields that are used in the `ON` condition must be listed in the `SELECT` list.

Special rules apply when the operands of the ON condition are [CDS enumerated elements](../../abap-glossary/abencds_enum_element_glosry.md). These rules are described in the topic [CDS DDL - Using CDS Enumerated Types](abencds_use_enum_type.md).

## Hints

- A node that defines a to-parent association is not automatically a child entity of the business object. A node is only a child entity of the business object when it is the target of a to-child association.

- To-parent associations can be given annotations in the [element list](abencds_select_list_entry_v2.md) of the CDS entity in which they are defined.

- In a CDS abstract entity, if the association target of a to-parent association is another CDS abstract entity, then the `ON` condition is not mandatory and can optionally be left out. See topic [CDS DDL - `DEFINE ABSTRACT ENTITY`, `to-parent association`](abencds_absent_to_parent_assoc.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS view entity `DEMO_SALES_CDS_SO_I_SL_VE` shown below returns information about schedule lines of sales order items. It defines a to-parent association to the CDS view entity `DEMO_SALES_CDS_SO_I_VE` that contains information about sales orders.

In the `SELECT` list, the to-parent association `_SalesOrderItem` is exposed, so it can be accessed from external CDS entities.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_SALES_CDS_SO_I_SL_VE
  as select from demo_sales_so_sl
  association to parent DEMO_SALES_CDS_SO_I_VE as _SalesOrderItem
    on $projection.parent_key = _SalesOrderItem.so_item_key
  association of many to one DEMO_SALES_CDS_SO_VE          as _SalesOrder
    on $projection.parent_key = _SalesOrder.so_key
  {
    key schedule_line_key,
        so_item_key as parent_key,
        parent_key  as root_key,
        _SalesOrderItem,
        _SalesOrder
  }
```
