---
title: "CDS DDL - DDIC-Based View, path_expr"
source_file: abencds_path_expression_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, path_expr

## Syntax

``` abap
... [source.]_assoc1[parameters][attributes] 
           [._assoc2[parameters][attributes] ... ] ...  
```

[`parameters`](abencds_select_parameters_v1.md) · [`attributes`](abencds_path_expr_attr_v1.md) · [`parameters`](abencds_select_parameters_v1.md) · [`attributes`](abencds_path_expr_attr_v1.md)

## Description

Specifies an [SQL path expression](../../abap-glossary/abensql_path_expression_glosry.md) that can be used in a `SELECT` statement of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). A path expression of the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) is a sequence of [CDS associations](../../abap-glossary/abencds_association_glosry.md) separated by periods (`.`) whose names are specified using `_assoc1`, `_assoc2`, and so on. The name of the CDS entity `source` in which the first CDS association is defined or exposed can be specified in front of this CDS association. The first CDS association of a path expression must be either:

- Defined in the current CDS view.

- Exposed as an element of the `SELECT` list or of the [element list](../abap-cds-data-definitions/abencds_f1_hiera_element_list.md) in a CDS view or CDS hierarchy that is a data source of the current view.

All further CDS associations must be exposed in the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the directly prefixed CDS association in the path expression. It is not possible to use a CDS association in a path expression that is defined in a [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) or in a [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md).

[`attributes`](abencds_path_expr_attr_v1.md) can be used to specify attributes in angle brackets after every CDS association. These attributes define the following further properties of this section of the path expression:

- [Cardinality](abencds_path_expr_card_v1.md)

- [Join type](abencds_path_expr_jointype_v1.md) implemented when used

- [Filter conditions](abencds_path_expression_filter_v1.md)

If the [association target](../../abap-glossary/abenassociation_target_glosry.md) of a specified [CDS association](../../abap-glossary/abencds_association_glosry.md) is a CDS entity with [input parameters](../abap-cds-data-definitions/abencds_f1_param.md), then actual parameters must be passed to them, using [`parameters`](abencds_select_parameters_v1.md) after the name `_assoc`. No parameters can be specified for a CDS association exposed as an [element](abencds_select_list_entry_v1.md) of a [`SELECT`](abencds_select_list_v1.md) list.

**Use of Path Expressions**

Path expressions can be used as follows in the CDS DDL in ABAP CDS:

- They can [expose](abencds_select_list_association_v1.md) their final CDS associations as [elements](abencds_select_list_entry_v1.md) of [`SELECT` lists](abencds_select_list_v1.md) for use in other CDS entities or in ABAP SQL.

- Path expressions with CDS associations whose [association target](../../abap-glossary/abenassociation_target_glosry.md) is not an [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) or a [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md) can be used as follows:

  - To specify the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the final CDS association as the data source [`data_source`](abencds_data_source_v1.md) after [`FROM`](abencds_select_statement_v1.md). The path expression represents an [inner join](../../abap-glossary/abeninner_join_glosry.md) by default.

  - To specify an element `.element` of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the last CDS association as an [element](abencds_select_list_entry_v1.md) of a [`SELECT` list](abencds_select_list_v1.md). The path expression represents a [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md) by default.

  - To specify an element `.element` of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the last CDS association as an operand of [`WHERE`](abencds_where_clause_v1.md), [`HAVING`](abencds_having_clause_v1.md), or [`WHEN`](abencds_searched_case_expr_v1.md) conditions. The path expression represents a [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md) by default.

  - To specify an element `.element` of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the last CDS association after `GROUP BY`. The path expression represents a [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md) by default.

  - To specify an element `.element` of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the last CDS association as an operand of an [aggregate expression](abencds_aggregate_functions_v1.md), a [built-in function](abencds_builtin_functions_v1.md), a [case expression](abencds_case_expression_v1.md), or a [cast expression](abencds_cast_expression_v1.md). The path expression represents a [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md) by default.

    In the case of self associations in which the [association target](../../abap-glossary/abenassociation_target_glosry.md) is the same as the [association source](../../abap-glossary/abenassociation_source_glosry.md), these usages are not possible in the CDS entity where they are defined.

For a non-aggregated element of a `SELECT` list that contains [aggregate expressions](abencds_aggregate_functions_v1.md), as well as in a `WHERE` and `HAVING` condition, the result of the path expression must be unique. This means that the [cardinality](../../abap-glossary/abencardinality_glosry.md) of all CDS associations used must be either to-one or the path expression can contain only [filter conditions](abencds_path_expr_attr_v1.md) that are declared as unique using the addition `1:`.

The following is evaluated when a CDS entity is accessed using a path expression:

- The joins defined by the CDS associations, from left to right.

- All other conditions of the CDS entities involved.

The path expression addresses the full result of this evaluation or a single element `.element`.

## Hints

- The most simple path expression is the name of a single CDS association.

- For joins of CDS associations used in path expressions, note that their left side is always the CDS entity that exposes the CDS association. This applies particularly to CDS associations that are exposed in data sources of CDS entities and passed on.

- CDS DDL path expressions can also be used in the ABAP [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md) of ABAP CDS to specify [conditions](../abap-cds-access-control/abencds_dcl_role_conditions.md).

- A CDS association whose [association target](../../abap-glossary/abenassociation_target_glosry.md) does not expose a CDS association cannot be followed by any further associations in a path expression. More specifically, for CDS associations whose association targets are DDIC database tables or DDIC views, no further CDS associations can be specified in a path expression.

- When the CDS associations of the path expressions of a view are implemented as joins, they are mapped to as few join expressions as possible. The [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) [`AbapCatalog.compiler.compareFilter`](abencds_view_anno_v1.md) can serve as support. It this annotation is used with the value `true`, it guarantees that CDS associations with semantically identical [filter conditions](abencds_path_expr_attr_v1.md) do not produce differing join expressions.

- Path expressions with CDS associations whose [association target](../../abap-glossary/abenassociation_target_glosry.md) is a [CDS transient entity](../../abap-glossary/abencds_non_sql_entity_glosry.md) cannot be used anywhere where they could produce instances of join expressions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following DDIC-based view contains the simple path expression `_scarr[inner].carrname` in its `SELECT` list. The attribute [`INNER`](abencds_path_expr_attr_v1.md) controls the [join type](../../abap-glossary/abenjoin_type_glosry.md). The class `CL_DEMO_FROM_JOIN_TO_ASSCTN` demonstrates that this view returns the same result as a directly programmed inner join in ABAP CDS or in ABAP SQL.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_JN2'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_join2
  as select from spfli
  association to scarr as _scarr on
    spfli.carrid = _scarr.carrid
  {
    _scarr[inner].carrname as carrier,
    spfli.connid           as flight,
    spfli.cityfrom         as departure,
    spfli.cityto           as arrival
  } 
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example shows three CDS views, `demo_sales_order_old`, `demo_business_partner_old1`, and `demo_invoice`. The CDS view `demo_invoice` uses its own CDS association and CDS associations from the other two views in path expressions:

- The CDS association `demo_sales_order` of the CDS view `demo_business_partner_old1` is specified as a data source after `FROM`. A filter condition guarantees that only certain orders can be used as data sources.

- The CDS association `invoice_header`, which is defined by the view `demo_invoice` itself, is used in a path expression as an operand in the `WHERE` condition.

- The CDS association `note_header` of the CDS view `demo_sales_order_old` is addressed using the alternative name `bpa` in `demo_business_partner_old1` and defined as an element of the `SELECT` list. This means this CDS association can also be used in CDS views that use `demo_invoice` as a data source.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_SO_VW_A'
define view DEMO_SALES_ORDER_OLD as
  select from snwd_so
         association [0..1] to snwd_text_key as _note_header
           on snwd_so.note_guid = _note_header.node_key
  { * } // Include all fields from snwd_text_key

```abap
@AbapCatalog.sqlViewName: 'DEMO_BPA_VW_OLD1'
define view DEMO_BUSINESS_PARTNER_OLD1 as
  select from snwd_bpa
         association [0..*] to DEMO_SALES_ORDER_OLD
           on snwd_bpa.node_key = DEMO_SALES_ORDER_OLD.BUYER_GUID
  { * }

```abap
  @AbapCatalog.sqlViewName: 'SALESO_INV_VW'
  define view demo_invoice as
    select from 
          /* Association "sales_order" with filter as data source */
           DEMO_BUSINESS_PARTNER_OLD1.DEMO_SALES_ORDER_OLD[
             LIFECYCLE_STATUS <> 'C' and LIFECYCLE_STATUS <> 'X']
             as bpa_so //alias for data source
           /* Association only used in this view definition */
           /*+[hideWarning] { "IDS" : [ "CARDINALITY_CHECK" ] }*/
           association [0..1] to snwd_so_inv_head as _invoice_header  
             on bpa_so.NODE_KEY = _invoice_header.so_guid
          { key bpa_so.NODE_KEY, //Field from ON-condition in_invoice_header
                bpa_so.SO_ID,
                bpa_so.NOTE_GUID, //Field from ON-condition in note_header
                bpa_so.LIFECYCLE_STATUS,
                /* Association is not exposed, but its element */
                _invoice_header.dunning_level,
                /* Association from data source is exposed here */
                bpa_so._note_header }
            /* Path expression in WHERE clause */
            where _invoice_header.dunning_level > '0';

 
```

## Executable Example

[Path Expressions, Use in the `SELECT` List](../../abap-programming-language/abap-database-access/abenpath_expr_in_colspec_abexa.md)
