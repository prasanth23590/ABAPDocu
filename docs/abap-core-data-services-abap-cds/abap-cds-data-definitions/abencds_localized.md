---
title: "CDS DDL - LOCALIZED"
source_file: abencds_localized.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Queries > CDS DDL - projection_list, Transactional Query > CDS DDL - proj_element, Transactional Query"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - LOCALIZED

## Syntax

``` abap
... _assoc1[._assoc2][._assoc3].field_name [AS alias]: LOCALIZED  
```

## Description

Defines a [CDS localized field](../../abap-glossary/abencds_localized_field_glosry.md) `field_name` in the [projection list](abencds_proj_view_element_list.md) of a [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md). CDS localized fields are [SQL path target field](../../abap-glossary/abensql_target_field_glosry.md) whose original data source is a [CDS text provider view](../../abap-glossary/abencds_text_provider_glosry.md). CDS localized fields are text fields for which for which translations in different languages are maintained. The keyword `LOCALIZED` causes automatic and implicit filtering to the current system language using the [session variable](../../abap-glossary/abensession_variable_glosry.md) [`system_language`](abencds_session_var_builtin_v2.md), so the text elements are displayed in the current system language.

The following rules apply to the field `field_name`:

- It must be a [SQL path target field](../../abap-glossary/abensql_target_field_glosry.md).

- It must have a character-like data type, more specifically, [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`SSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- The original data source of the field `field_name`, here `_assoc3`, must be a [CDS text provider view](../../abap-glossary/abencds_text_provider_glosry.md) whose [primary key](../../abap-glossary/abenprimary_key_glosry.md) consists of multiple [key fields](../../abap-glossary/abenkey_field_glosry.md), one of which is of data type [`LANG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and length 1. A text provider view is used to store texts with translations in different languages.

The [CDS association path](../../abap-glossary/abencds_association_path_glosry.md) that precedes the field `field_name` can consist of one or more associations `_assoc1[._assoc2][._assoc3] ...`. It must satisfy the following conditions:

- The last association, here `_assoc3`, must be a [CDS text association](../../abap-glossary/abencds_text_association_glosry.md). This means, it must be a regular CDS association whose [association target](../../abap-glossary/abenassociation_target_glosry.md) is a [CDS text provider view](../../abap-glossary/abencds_text_provider_glosry.md). The [target cardinality](../../abap-glossary/abentarget_cardinality_glosry.md) of the CDS text association must be `TO MANY`. If the association path consists of exactly one association, this association must be a CDS text association.

- The text association must bind all the key fields of its association target in the `ON` condition, except for the language key of type [`LANG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The key fields must be bound in a comparison with the [comparison operator](abencds_cond_expr_comp_v2.md) *=*. The second operand of the comparison can be a field of the association source or a [literal](../../abap-glossary/abencds_literal_glosry.md). No other operands are allowed.

- The first and intermediate associations, here `_assoc1` and `_assoc2`, must have the target cardinality [`TO ONE`](abencds_cardinality_v2.md) or [`TO EXACT ONE`](abencds_cardinality_v2.md). These associations can be regular or specialized, i.e. to-parent or to-child associations are possible.

The syntax `LOCALIZED` can be used for a [cast expression](abencds_cast_expression_v2.md) with the addition `PRESERVING TYPE`, under the condition that the field and the CDS association path fulfill the requirements explained above. For example, the following is supported:

`CAST( _assoc1.field_name as data_element PRESERVING TYPE) : localized`

## More Information

Developer guide for the ABAP RESTful Programming Model, section about [text associations](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/ab8283b2064d474fa160871fc23825df?version=sap_cross_product_abap).

## Hint

The keyword `LOCALIZED` has the same effect as filtering a text association with the filter condition `[to exact one:Language=$session.system_language]`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS transactional query defines the field `MaterialName` as CDS localized field. All prerequisites are met:

- `MaterialName` has the data type `CHAR`.

- The association `_Text` has a text provider view as its association target and it has the cardinality `TO MANY`.

- The first association `_Material` has the target cardinality `TO ONE`.

``` abap
@EndUserText.label: 'Projection View Sales Order Item List'
@AccessControl.authorizationCheck: #NOT_REQUIRED
@AbapCatalog.entityBuffer.propagationAllowed: true
define root view entity DEMO_SALES_PV_SO_I_LIST1
  provider contract transactional_query
  as projection on DEMO_SALES_CDS_SO_I1
{
  key material                      as MaterialId,
      posnr                         as PositionNumber,
      _Material._Text.material_name as MaterialName : localized
}
```

The SQL statement that is generated on the database contains a nested join expression with a filter condition on the current session language.

So the keyword `LOCALIZED` is a realization of the path expression `_Material._Text[to exact one:Language=$session.system_language].material_name`.
