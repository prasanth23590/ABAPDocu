---
title: "CDS DDL - CDS View Entity, COMPOSITION"
source_file: abencds_composition_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - CDS View Entity, SELECT, Associations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, COMPOSITION

## Syntax

``` abap
... COMPOSITION [cardinality] [OF] target [AS _compos] ...  
```

[`cardinality`](abencds_cardinality_v2.md)

## Description

Defines a [to-child association](../../abap-glossary/abento_child_association_glosry.md) in [ABAP CDS](../../abap-glossary/abenabap_core_data_services_glosry.md). A to-child association is a specialized [CDS association](../../abap-glossary/abencds_association_glosry.md) that defines the current [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) as [parent entity](../../abap-glossary/abenparent_entity_glosry.md) of the [composition target](../../abap-glossary/abencomposition_target_glosry.md). The composition target is the [child entity](../../abap-glossary/abenchild_entity_glosry.md) and it must define a [to-parent association](../../abap-glossary/abento_parent_association_glosry.md) to its parent entity. [To-child associations](../../abap-glossary/abento_child_association_glosry.md) and [to-parent associations](../../abap-glossary/abento_parent_association_glosry.md) together define [CDS compositions](../../abap-glossary/abencds_composition_glosry.md) that in turn define the [CDS composition tree](../../abap-glossary/abencds_composition_tree_glosry.md) of a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) in the context of the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md).

A to-child association is defined in a [`SELECT` statement](abencds_select_statement_v2.md) of a CDS view entity using the keyword `COMPOSITION`. A to-child association associates the current CDS entity, as a [composition source](../../abap-glossary/abencomposition_source_glosry.md), with the [composition target](../../abap-glossary/abencomposition_target_glosry.md) `target` specified in the definition of the to-child association.

## Prerequisite

The child entity (composition target) must already have a [to-parent association](abencds_to_parent_assoc_v2.md) to the composition parent before a to-child association can be defined in the parent.

**Rules**

To-child associations are defined similarly to CDS associations. Here are the similarities and differences:

- Similarities

  - For the name of the to-child association `AS _compos`, the same rules apply as for a regular CDS association, see topic [CDS DDL - CDS View Entity, `ASSOCIATION`](abencds_simple_association_v2.md).

  - The [cardinality](../../abap-glossary/abencardinality_glosry.md) can be specified written in words or using numeric syntax, as described in topic [CDS DDL - CDS View Entity, cardinality](abencds_cardinality_v2.md). If the cardinality syntax written in words is used, the [source cardinality](../../abap-glossary/abensource_cardinality_glosry.md) must be `EXACT ONE`. It can also be left out and is then implicitly set to `EXACT ONE`.

- Differences:

  - No `ON` condition is defined explicitly for a to-child association. The `ON` condition is generated automatically using the `ON` condition of the to-parent association of the composition target.

  - A default filter cannot be defined for a to-child association. The syntax `... WITH DEFAULT FILTER ...` is not allowed.

The following applies to the composition target target:

- The composition target can be another [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), an [abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md), or a [custom entity](../../abap-glossary/abencds_custom_entity_glosry.md).

- A child entity can be the target of exactly one to-child association. This means that a child entity can have exactly one parent entity.

- The target of a to-child association must not be a [root entity](../../abap-glossary/abenroot_entity_glosry.md).

- The composition target cannot be specified using a [path expression](abencds_path_expression_v2.md). The following is **not** allowed:

  `COMPOSITION OF _path._to_child`

- It must be a [CDS entity](../../abap-glossary/abencds_entity_glosry.md). If `target` is a [CDS transient entity](../../abap-glossary/abencds_non_sql_entity_glosry.md), the way the to-child association can be used is restricted.

- Self-to-child associations are not allowed. The target of a to-child association cannot be the CDS entity in which this to-child association is defined.

Exposure:

- The name of the to-child association `_compos` must be added exactly once to the [`select_list`](abencds_select_list_v2.md) of the CDS view entity it is defined in, without attributes and alias. If no name is defined for the to-child association, the name of the to-child association is the name of the target entity `target` and this name must be made available in the `SELECT` list.

Usage:

- Fields from a composition target **cannot** be used locally in path expressions. Fields from the composition target cannot be used in the `SELECT` list, `WHERE` clause, or any other position of the view entity in which it is defined.

  This also applies to CDS view extensions. A field from a composition target cannot be added to a CDS view entity via [`EXTEND VIEW ENTITY`](abencds_extend_view_entity.md).

- A to-child association can be propagated in data definitions other than the one in which it is defined. In this case, the to-child association loses its special semantics and is handled like a regular CDS association.

- When a to-child association is used in another data definition, metadata extension, or view extension other than the one in which it is defined, then it can be used in a path expression. Parameter passing and defining attributes is also possible in this case.

- To-child associations can be used in annotation values (such as `AnnotationRef` or `ElementRef`) in the CDS entities that define them, since this does not lead to an SQL join.

Compositions and joins:

- The use cases and generation of joins described in topic [`CDS DDL - CDS View Entity, Associations and Joins`](abencds_assoc_join_v2.md) also apply to to-child associations, with the exception of use cases 3 and 4.

## Hints

- [Cyclical dependencies](abencds_cycle_problems.md) should be avoided when using to-child associations to prevent problems occurring in mass activations of CDS entities.

- To-child associations can be given annotations in the element list `element_list` of the CDS entity in which they are defined.

- Defining new to-child associations is not supported in views with [set operators](abencds_set_operators.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS view entity `DEMO_SALES_CDS_SO_I_VE` shown below returns information about sales order items. It defines three associations, one of them being a to-child association. The composition target (i.e. the child entity) is the CDS view entity `DEMO_SALES_CDS_SO_I_SL_VE`.

Explanation: Each sales order item can have one or more schedule lines, but schedule lines can exist only in connection with sales order items.

In the `SELECT` list, the to-child association `_ScheduleLine` is exposed, so it can be accessed from external CDS entities.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_SALES_CDS_SO_I_VE
  as select from
    demo_sales_so_i
    association        to parent DEMO_SALES_CDS_SO_VE as _SalesOrder
      on $projection.parent_key = _SalesOrder.so_key
    composition of exact one to many DEMO_SALES_CDS_SO_I_SL_VE   
                                                      as _ScheduleLine
    
    
    association of many to one DEMO_SALES_CDS_MATERIAL_VE  
                                                      as _Material
      on $projection.material = _Material.material
    {
      key so_item_key,
          parent_key,
          posnr,
          material,
          @Semantics.amount.currencyCode: 'currency'
          gross_amount,
          currency,
          @Semantics.quantity.unitOfMeasure: 'unit'
          quantity,
          unit,
          _SalesOrder,
          _ScheduleLine,
          _Material.material_type as Type
    }

    
    
    
```
