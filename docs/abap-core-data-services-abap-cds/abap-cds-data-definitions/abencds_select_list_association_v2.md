---
title: "CDS DDL - CDS View Entity, SELECT, expose_assoc"
source_file: abencds_select_list_association_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - CDS View Entity, SELECT, select_list > CDS DDL - CDS View Entity, SELECT, element"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, SELECT, expose_assoc

## Syntax

``` abap
... path_expr [AS alias]  
```

[`path_expr`](abencds_path_expression_v2.md)

## Description

Uses a path expression [`path_expr`](abencds_path_expression_v2.md) to expose a [CDS association](../../abap-glossary/abencds_association_glosry.md) as an [element](abencds_select_list_entry_v2.md) of the [`SELECT` list](abencds_select_list_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). A path expression can consist of one or more associations, and the final CDS association is exposed for use in other [CDS views](../../abap-glossary/abencds_view_glosry.md) or in ABAP SQL:

- A different CDS view can evaluate the CDS association in its [path expressions](abencds_path_expression_v2.md).

- The CDS association can be used in [ABAP SQL path expressions](../../abap-programming-language/abap-database-access/abenabap_sql_path.md).

The current view is the [association source](../../abap-glossary/abenassociation_source_glosry.md) of the exposed CDS association and any join expression created for a path expression from the CDS association uses the current CDS view entity as its left side.

All fields of the association source that are used in the `ON` condition must also be specified as elements of the current `SELECT` list. Such an element must be specified by exactly the same path expression as used for exposing the association. It must contain the same associations in the same sequence and with the same [attributes](abencds_path_expr_attr_v2.md).

A CDS association can be exposed multiple times with various alternative element names `alias` defined using the keyword `AS` (see example below). This makes it possible to use different [filter conditions](abencds_path_expression_filter_v2.md) `cds_cond`. However, this is only possible for simple CDS associations and not for to-child and to-parent associations.

An exposed CDS association is part of the `SELECT` list. It is not, however, part of the result set, nor a component of the type defined in ABAP with respect to the CDS view entity.

The names of the elements of a `SELECT` list must be unique. This applies in particular also for the publication of a [CDS association](../../abap-glossary/abencds_association_glosry.md) using a path expression. There must be no other element with this name. If necessary, `AS` must be used to define an alternative element name `alias` for the CDS association. If no alternative element name `alias` is defined, the element name is defined by the name of the CDS association used in the path expression. When a CDS association with a [filter condition](abencds_path_expression_filter_v2.md) `cds_cond` is exposed, an alternative element name `alias` using `AS` is mandatory.

## Hints

- When a CDS association is exposed, the exposing view itself is the [association source](../../abap-glossary/abenassociation_source_glosry.md) of the exposed CDS association - not the data source of the exposing view. Especially when CDS associations are exposed that were already exposed by the data source of the current view, the current view replaces the original view as the association source. When a join expression is created for the current view, the left side of the join expression is the result set of the current view.

- When exposing a [CDS association](../../abap-glossary/abencds_association_glosry.md) using a path expression [`path_expr`](abencds_path_expression_v2.md) in the `SELECT` list, it is not possible to pass actual parameters to any [input parameters](abencds_parameter_list_v2.md) of the [association target](../../abap-glossary/abenassociation_target_glosry.md) to assign start values to the input parameters.

- Special rules apply to the publication of CDS associations in `SELECT` statements joined with a [set operator](abencds_set_operators.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity exposes its own CDS association `_spfli` and the CDS association `_sflight` exposed by its [association target](../../abap-glossary/abenassociation_target_glosry.md) `demo_cds_assoc_spfli`. The fields of the [association source](../../abap-glossary/abenassociation_source_glosry.md), which are used in the `ON` conditions of the CDS associations, are specified in the `SELECT` list. In the case of the CDS association exposed using `_spfli._sflight`, path expressions `_spfli.carrid` and `_spfli.connid` are specified accordingly. The element `carrid` occurs twice, therefore, an alternative element name must be defined using `AS`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_EXPOSE_ASSOC_VE
  as select from scarr
  association of one to many demo_cds_assoc_spfli as _spfli 
    on scarr.carrid = _spfli.carrid
{
      _spfli,
  key scarr.carrid as scarr_carrid,
      _spfli._sflight,
      _spfli.carrid,
      _spfli.connid  
}
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity exposes its own CDS association `_spfli` with a filter condition. The fields of the [association source](../../abap-glossary/abenassociation_source_glosry.md), which are used in the `ON` condition of the CDS association, are specified in the `SELECT` list using the same filter condition. Once this has been done, the same association can be exposed again with different filter conditions. New alias names are required.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_EXPOSE_ASSOC_FILTER
  as select from scarr 
  association of one to many demo_cds_assoc_spfli as _spfli  
    on scarr.carrid = _spfli.carrid 
{ 
//Association with filter condition
      _spfli[  carrid = ''  ] as airline, 
  key scarr.carrid as scarr_carrid, 
      _spfli[  carrid = ''  ]._sflight, 
      _spfli[  carrid = ''  ].carrid, 
      _spfli[  carrid = ''  ].connid,
      
//same association with different filter condition and new alias name
      _spfli[ carrid = 'A' ] as airline_A,
      _spfli.airpfrom as airport  
}
```

## Executable Example

[Exposing CDS Associations](abencds_expose_assoc_v2_abexa.md)
