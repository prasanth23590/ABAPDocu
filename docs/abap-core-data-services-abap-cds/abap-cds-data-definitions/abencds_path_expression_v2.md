---
title: "CDS DDL - CDS View Entity, path_expr"
source_file: abencds_path_expression_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, path_expr

## Syntax

``` abap
... [source.]_assoc1[parameters][attributes] 
           [._assoc2[parameters][attributes] ... ] ...  
```

[`parameters`](abencds_select_parameters_v2.md) · [`attributes`](abencds_path_expr_attr_v2.md) · [`parameters`](abencds_select_parameters_v2.md) · [`attributes`](abencds_path_expr_attr_v2.md)

## Description

Specifies an [SQL path expression](../../abap-glossary/abensql_path_expression_glosry.md) that can be used in a `SELECT` statement of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). A path expression of the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) is a sequence of [CDS associations](../../abap-glossary/abencds_association_glosry.md) separated by periods (`.`) whose names are specified using `_assoc1`, `_assoc2`, and so on. If the first CDS association is exposed in another CDS entity, the name of this CDS entity can be specified as `source.` in front of the path expression.

A path expression may consist of a mixture of to-child associations, to-parent associations, and regular CDS associations.

The first CDS association of a path expression must be either defined in the current CDS view entity, or exposed as an element of the `SELECT` list or of the [element list](abencds_f1_hiera_element_list.md) in a CDS view entity or CDS hierarchy that is a data source of the current view.

All further CDS associations must be exposed in the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the directly prefixed CDS association in the path expression. It is not possible to use a CDS association in a path expression that is defined in a [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) or in a [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md).

[`attributes`](abencds_path_expr_attr_v2.md) can be used to specify attributes in angle brackets after every CDS association. These attributes define the following further properties of this section of the path expression:

- [Cardinality](abencds_path_expr_card_v2.md)

- [Join type](abencds_path_expr_jointype_v2.md) implemented when used

- [Filter conditions](abencds_path_expression_filter_v2.md)

If the association target of a specified CDS association is a CDS entity with [input parameters](abencds_f1_param.md), then actual parameters must be passed to them, using [`parameters`](abencds_select_parameters_v2.md) after the name `_assoc`. Only in one use case, it is not possible to specify values for the actual parameters, namely when a CDS association is exposed in a path expression as an [element](abencds_select_list_entry_v2.md) of a [`SELECT`](abencds_select_list_v2.md) list.

**Use of Path Expressions**

Path expressions can be used as follows in the CDS DDL in ABAP CDS:

- They can [expose](abencds_select_list_association_v2.md) their final CDS associations as [elements](abencds_select_list_entry_v2.md) of [`SELECT` lists](abencds_select_list_v2.md) for use in other CDS entities or in ABAP SQL.

- Path expressions with CDS associations whose [association target](../../abap-glossary/abenassociation_target_glosry.md) is not a [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) or a [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md) can be used as follows:

  - To specify the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the final CDS association as the data source [`data_source`](abencds_data_source_v2.md) after [`FROM`](abencds_select_statement_v2.md). The path expression represents an [inner join](../../abap-glossary/abeninner_join_glosry.md) by default.

  - To specify an element `.element` of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the last CDS association as an [element](abencds_select_list_entry_v2.md) of a [`SELECT` list](abencds_select_list_v2.md). In this case, the element is referred to as [SQL path target field](../../abap-glossary/abensql_target_field_glosry.md). The path expression represents a [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md) by default.

  - To specify an element `.element` of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the last CDS association as an operand of [`WHERE`](abencds_where_clause_v2.md), [`HAVING`](abencds_having_clause_v2.md), or [`WHEN`](abencds_searched_case_expr_v2.md) conditions. The path expression represents a [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md) by default.

  - To specify an element `.element` of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the last CDS association after `GROUP BY`. The path expression represents a [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md) by default.

  - To specify an element `.element` of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the last CDS association as an operand of an [aggregate expression](abencds_aggregate_functions_v2.md), a [built-in function](abencds_builtin_functions_v2.md), a [case expression](abencds_case_expression_v2.md), or a [cast expression](abencds_cast_expression_v2.md). The path expression represents a [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md) by default.

    In the case of self associations in which the [association target](../../abap-glossary/abenassociation_target_glosry.md) is the same as the [association source](../../abap-glossary/abenassociation_source_glosry.md), these usages are not possible in the CDS entity where they are defined.

For a non-aggregated element of a `SELECT` list that contains [aggregate expressions](abencds_aggregate_functions_v2.md), as well as in a `WHERE` and `HAVING` condition, the result of the path expression must be unique. This means that the [cardinality](../../abap-glossary/abencardinality_glosry.md) of all CDS associations used must be either to-one or the path expression can contain only [filter conditions](abencds_path_expr_attr_v2.md) that are declared as unique using the addition `1:`.

When a CDS entity with a path expression is accessed, the following is evaluated:

- The joins defined by the CDS associations, from left to right.

- All other conditions of the CDS entities involved.

The path expression addresses the full result of this evaluation or a single element `.element`.

## Hints

- The most simple path expression is the name of a single CDS association.

- For joins of CDS associations used in path expressions, note that their left side is always the CDS entity that exposes the CDS association. This applies particularly to CDS associations that are exposed in data sources of CDS entities and passed on.

- CDS DDL path expressions can also be used in the ABAP [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md) of ABAP CDS to specify [conditions](../abap-cds-access-control/abencds_dcl_role_conditions.md).

- A CDS association whose [association target](../../abap-glossary/abenassociation_target_glosry.md) does not expose a CDS association cannot be followed by any further associations in a path expression. More specifically, for CDS associations whose association targets are DDIC database tables or DDIC views, no further CDS associations can be specified in a path expression.

- When the CDS associations of the path expressions of a view are implemented as joins, they are automatically mapped to as few join expressions as possible. CDS associations with semantically identical filter conditions are automatically summarized into one single join expression.

- Path expressions with CDS associations whose [association target](../../abap-glossary/abenassociation_target_glosry.md) is a [CDS transient entity](../../abap-glossary/abencds_non_sql_entity_glosry.md) cannot be used anywhere where they could produce instances of join expressions.

- When a path expression of a `TO EXACT ONE` association is used with [attributes](abencds_path_expr_attr_v2.md), then the join is rewritten to a `TO ONE` join on the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) to avoid potential cardinality conflicts. This is indicated by a syntax check warning. The syntax check warning can be suppressed by explicitly specifying the current association as `TO EXACT ONE`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity contains the simple path expression `_scarr[inner].carrname` in its `SELECT` list. The attribute [`INNER`](abencds_path_expr_attr_v2.md) controls the [join type](../../abap-glossary/abenjoin_type_glosry.md). The class `CL_DEMO_FROM_JOIN_TO_ASSOC_VE` demonstrates that this view returns the same result as a directly programmed inner join in ABAP CDS or in ABAP SQL.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_JOIN2_VE
  as select from spfli
  association to scarr as _scarr on spfli.carrid = _scarr.carrid
{
  key carrid, 
      _scarr[inner].carrname as carrier,
      spfli.connid           as flight,
      spfli.cityfrom         as departure,
      spfli.cityto           as arrival,
      _scarr
}
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS view entity `DEMO_SALES_CDS_PATH_EXPR` uses its own association and associations from other CDS entities in path expressions:

- The CDS association `_SalesOrder` of the DDIC-based view `DEMO_SALES_CDS_SO_I` is specified as a data source after ` FROM`. A filter condition guarantees that only certain orders can be used as data sources.

- The CDS association `invoice_header`, which is defined by the view `DEMO_SALES_CDS_PATH_EXPR` itself, is used in a path expression as an operand in the `WHERE` condition.

- The CDS association `_Buyer` of the CDS view `DEMO_SALES_CDS_SO` is exposed via a path expression in the `SELECT` list. This means that this CDS association can also be used in CDS view entities that use `DEMO_SALES_CDS_PATH_EXPR` as a data source.

``` abap
@AccessControl.authorizationCheck: #CHECK
define view entity DEMO_SALES_CDS_PATH_EXPR
  as select from DEMO_SALES_CDS_SO_I._SalesOrder[
                 lifecycle_status <> 'C' and lifecycle_status <> 'X']
  association to exact one demo_so_inv_he as _invoice_header
    on DEMO_SALES_CDS_SO.id = _invoice_header.buyer_id
  {
    key so_key as soKey,
        lifecycle_status,
        _invoice_header.dunning_level,
        DEMO_SALES_CDS_SO._Buyer,
        DEMO_SALES_CDS_SO.buyer_id,
        DEMO_SALES_CDS_SO.id
  }
  where
    _invoice_header.dunning_level > '0'
```

## Executable Example

[Path Expressions, Use in the `SELECT` List](../../abap-programming-language/abap-database-access/abenpath_expr_in_colspec_abexa.md)
