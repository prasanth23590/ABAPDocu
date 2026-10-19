---
title: "CDS DDL - DDIC-Based View, SELECT, expose_assoc"
source_file: abencds_select_list_association_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, select_list > CDS DDL - DDIC-Based View, SELECT, element"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, SELECT, expose_assoc

## Syntax

``` abap
... path_expr [AS alias]  
```

[`path_expr`](abencds_path_expression_v1.md)

## Description

Uses a path expression [`path_expr`](abencds_path_expression_v1.md) to expose a [CDS association](../../abap-glossary/abencds_association_glosry.md), a [to-child association](../../abap-glossary/abento_child_association_glosry.md), or a [CDS to-parent association](../../abap-glossary/abento_parent_association_glosry.md) as an [element](abencds_select_list_entry_v1.md) of the [`SELECT` list](abencds_select_list_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). A path expression can consist of one or more associations, and the final CDS association is exposed for use in other [CDS views](../../abap-glossary/abencds_view_glosry.md) or in ABAP SQL:

- A different CDS view can evaluate the CDS association in its [path expressions](abencds_path_expression_v1.md).

- The CDS association can be used in ABAP SQL [path expressions](../../abap-programming-language/abap-database-access/abenabap_sql_path.md).

The current view is the [association source](../../abap-glossary/abenassociation_source_glosry.md) of the exposed CDS association and any join expressions created for a path expression from the CDS association use the current CDS view as their left side.

All fields of the association source of the CDS association that occur in the `ON` condition must also be specified as elements of the current `SELECT` list. Such an element must be specified by exactly the same path expression as used for exposing the association. It must contain the same associations in the same sequence and with the same [attributes](abencds_path_expr_attr_v1.md).

A CDS association can be exposed multiple times with various alternative element names `alias` defined using the keyword `AS`. This makes it possible to use different [filter conditions](abencds_path_expression_filter_v1.md) `cds_cond`. However, this is only possible for simple CDS associations and not for to-child and to-parent associations.

Like every element, a CDS association exposed in this way is part of the `SELECT` list and must also be specified in a [name list](abencds_name_list_v1.md). It is not, however, part of the result set, a field of the [CDS-managed DDIC view](../../abap-glossary/abencds_mngdddic_view_glosry.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), or a component of a type defined in ABAP with respect to the CDS view. If no alternative element name `alias` is defined, and there is no [name list](abencds_name_list_v1.md), the element name is defined by the name of the CDS association named by the path expression.

## Hints

- When a CDS association is exposed, the exposing view itself is the [association source](../../abap-glossary/abenassociation_source_glosry.md) of the exposed CDS association and not the data source of the exposing view. Especially when CDS associations are exposed that were already exposed by the data source of the current view, the current view replaces the original view as the association source. When a join expression is created for the current view, the left side of the join expression is the result set of the current view.

- When a CDS association with a [filter condition](abencds_path_expression_filter_v1.md) `cds_cond` is exposed, an alternative element name `alias` using `AS` must be defined in the `SELECT` list.

- When exposing a [CDS association](../../abap-glossary/abencds_association_glosry.md) using a path expression [`path_expr`](abencds_path_expression_v1.md) in the `SELECT` list, it is not possible to pass actual parameters to any [input parameters](abencds_parameter_list_v1.md) of the [association target](../../abap-glossary/abenassociation_target_glosry.md) to assign start values to the input parameters.

- The name of the elements of a `SELECT` list must be unique. This applies in particular also for the publication of a [CDS association](../../abap-glossary/abencds_association_glosry.md) using a path expression. There must be no other element with this name. If necessary, `AS` must be used to define an alternative element name `alias` for the CDS association.

- Special rules apply to the publication of CDS associations in `SELECT` statements joined with [`UNION`](abencds_union_v1.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view exposes its own CDS association `_spfli` and the CDS association `_sflight` exposed by its [association target](../../abap-glossary/abenassociation_target_glosry.md) `demo_cds_assoc_spfli`. The fields of the [association source](../../abap-glossary/abenassociation_source_glosry.md), which are used in the `ON` conditions of the CDS associations, are specified in the `SELECT` list. In the case of the CDS association exposed using `_spfli._sflight`, path expressions `_spfli.carrid` and `_spfli.connid` are specified accordingly. The element `carrid` occurs twice, which means that an alternative element name must be defined using `AS`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_EXPOSE_ASSOC
  as select from scarr
  association [1..*] to demo_cds_assoc_spfli as _spfli 
    on scarr.carrid = _spfli.carrid
{
      _spfli,
  key scarr.carrid as scarr_carrid,
      _spfli._sflight,
      _spfli.carrid,
      _spfli.connid  
}
```

## Executable Example

[Exposing CDS Associations](abencds_expose_assoc_v1_abexa.md)
