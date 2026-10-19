---
title: "CDS DDL - element, Analytical Query"
source_file: abencds_element_apv.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Analytical Queries > CDS DDL - element_list, Analytical Query"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - element, Analytical Query

## Syntax

``` abap
... [@element_annot1] 
    [@element_annot2] 
    ... 
                { field                [AS alias]             } 
      |         { path_expr.element    [AS alias][: LOCALIZED]} 
      |         { arith_expr            AS alias              } 
      |         { builtin_func          AS alias              } 
      |         { Analytical Scalar Functions 
                                        AS alias              } 
      |         { case_expr             AS alias              } 
      | { VIRTUAL calculated unit       AS alias              } 
      |         { parameter             AS alias              } 
      |         { session_variable      AS alias              } 
      |         { typed_literal         AS alias              } 
      |         { cast_expr             AS alias              } 
      |         { $projection.reuse_exp AS alias              }  
```

[`@element_annot1`](abencds_element_annotations_v2.md) · [`@element_annot2`](abencds_element_annotations_v2.md) · [`path_expr`](abencds_path_expr_apv.md) · [`LOCALIZED`](abencds_localized.md) · [`arith_expr`](abencds_arithmetic_expression_v2.md) · [`builtin_func`](abencds_builtin_functions_v2.md) · [`Analytical Scalar Functions`](abencds_ana_scalar_function.md) · [`case_expr`](abencds_case_expression_apv.md) · [`calculated unit`](../abap-cds-data-types/abencds_calculated_quantity.md) · [`parameter`](abencds_parameter_list_apv.md) · [`session_variable`](abencds_session_variable_v2.md) · [`typed_literal`](abencds_typed_literal_v2.md) · [`cast_expr`](abencds_cast_expression_v2.md) · [`$projection.reuse_exp`](abencds_reusable_expression_v2.md)

### Addition

[1. `... AS alias`](abencds_element_apv.md#addition-1)

[2. `... LOCALIZED`](abencds_element_apv.md#addition-2)

[3. `... VIRTUAL`](abencds_element_apv.md#addition-3)

## Overview

### Description

Defines an element in the element list of a [CDS analytical projection view](../../abap-glossary/abencds_analytical_pv_glosry.md).

Elements in the element list of an analytical projection view can be [analytical formulas](../../abap-glossary/abencds_formula_glosry.md), [selections](../../abap-glossary/abencds_selection_glosry.md), dimension fields, text fields or attributes, or CDS amount and quantity fields. See the topic about [the conceptual background of analytical queries](abencds_measure_dimension_apv.md) for further details.

- The rules for [propagation of element annotations in CDS projection views](abencds_element_annotations_pv.md) apply.

- `field` exposes an element from the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md). `AS` can be used to define an alternative element name `alias`.

  In analytical projection views, [measure](../../abap-glossary/abencds_measure_glosry.md) fields can be exposed multiple times with different alias names. [Dimension fields](../../abap-glossary/abencds_dimension_glosry.md) can be exposed only once. Analytical measure fields and analytical dimension fields from the projected entity remain analytical measures and dimensions and their type must not be changed in the projection layer.

- [`path_expr`](abencds_path_expr_apv.md).element exposes an element of an association target of the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md). If no alternative element name `alias` is defined, the original element name of the element picked by the path expression is reused. For details, see the topic about [path expressions in analytical queries](abencds_path_expr_apv.md).

- [`arith_expr`](abencds_arithmetic_expression_v2.md) can be used to specify an [arithmetic expression](abencds_arithmetic_expression_v2.md). The annotation `Aggregation.default: #FORMULA` is mandatory when an arithmetic expression is included as a field in the element list. Arithmetic expressions are evaluated by the analytical engine when the analytical query is accessed. An alternative element name `alias` must be defined with the keyword `AS`.

  **Note:** Arithmetic expressions must not have any path fields specified using `path_expr.element` as operands.

- The following built-in functions [`builtin_func`](abencds_builtin_functions_v2.md) are supported:

  [`CURR_TO_DECFLOAT_AMOUNT`](abencds_conv_func_unit_curr_v2.md) [`GET_NUMERIC_VALUE`](abencds_conv_func_unit_curr_v2.md) [`DATS_DAYS_BETWEEN`](abencds_date_functions_v2.md) [`DATS_ADD_DAYS`](abencds_date_functions_v2.md) [`CURRENCY_CONVERSION`](abencds_conv_func_unit_curr_v2.md): The following special rules apply:

  - `amount` can be either a field of the [CDS projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md), or the function `CURR_TO_DECFLOAT_AMOUNT` with a field of the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md) as argument `arg`. No other expression or operand is allowed as operand for `amount`.

  - `source_currency` must be a field of the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md).

  - `target_currency` must not be a reuse expression specified using [`$projection`](abencds_reusable_expression_v2.md).

  - The following optional parameters are not supported: `client`, `round`, `decimal_shift`, `decimal_shift_back`, and `error_handling`.

    [`UNIT_CONVERSION`](abencds_conv_func_unit_curr_v2.md): The following special rules apply:

  - `quantity` and `source_unit` must be defined as a field of the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md).

  - `target_unit` must not be a reuse expression specified using [`$projection`](abencds_reusable_expression_v2.md).

  - The following optional parameters are not supported: `client`, `error_handling`.

    The annotation `Aggregation.default: #FORMULA` is mandatory for built-in functions.

- [Analytical scalar functions](abencds_ana_scalar_function.md) can be specified as elements. An alias name is mandatory.

- [`case_exp`](abencds_case_expression_apv.md) can be used to specify [case distinctions](abencds_case_expression_apv.md). In an analytical query, case distinctions define [analytical formulas](../../abap-glossary/abencds_formula_glosry.md) or [restricted measures](../../abap-glossary/abencds_selection_glosry.md). See topic [CDS DDL - `case_expr`, Analytical Query](abencds_case_expression_apv.md) for further details.

- [Calculated units](../abap-cds-data-types/abencds_calculated_quantity.md) can be defined using the keyword `VIRTUAL` in CDS analytical projection views. By that, the analytical runtime automatically fills in the required value for the unit.

- `parameter` can be used to specify a parameter from the [parameter list](abencds_parameter_list_apv.md). An alternative element name using the keyword ` AS` must be defined and it cannot be the name of the parameter. In analytical queries, parameters must have either a numeric data type (except for `NUMC`), or a unit or currency key. The annotation `Aggregation.default: #FORMULA` is mandatory when a parameter of a numeric data type is included as a field in the element list. No annotation is required when a parameter is used as an operand in a [formula](../../abap-glossary/abencds_formula_glosry.md).

- [`session_variable`](abencds_session_variable_v2.md) can be used to specify a [session variable](../../abap-glossary/abensession_variable_glosry.md). `AS` must be used to define an alternative element name `alias`. The following session variables are supported in the element list of analytical queries: `system_date` and `user_date`. The annotation ` Aggregation.default: #FORMULA` is mandatory when a session variable is included as a field in the element list. No annotation is required when a session variable is used as an operand in a [formula](../../abap-glossary/abencds_formula_glosry.md) or [selection](../../abap-glossary/abencds_selection_glosry.md).

- [`typed_literal`](abencds_typed_literal_v2.md) can be used to declare a [typed literal](../../abap-glossary/abentyped_literal_glosry.md). `AS` must be used to define an alternative element name `alias`. In analytical queries, typed literals must have either a numeric data type (except for `NUMC`), or a unit or currency key. The annotation `Aggregation.default: #FORMULA` is mandatory when a numeric typed literal is included as a field in the element list. No annotation is required when a typed literal is used as an operand in a [formula](../../abap-glossary/abencds_formula_glosry.md) or [selection](../../abap-glossary/abencds_selection_glosry.md).

  **Note:** [untyped literals](abencds_untyped_literal_v2.md) are not supported in the element list of analytical projection views.

- [`cast_expr`](abencds_cast_expression_v2.md) can be used to specify [cast expressions](abencds_cast_expression_v2.md). For a cast expression, an alias name must be specified with the keyword `AS`.

- [`$projection.reuse_exp`](abencds_reusable_expression_v2.md) reuses an expression defined in the `SELECT` list in another operand position of the same analytical projection view. An alternative element name specified using `AS` is required.

## Restrictions

- Exposing associations from the projected entity is not allowed.

- The definition of key fields using `KEY` is not allowed.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS analytical projection view `DEMO_ANALYTICAL_QUERY_ELEM` defines an analytical query. It is based on the cube view `DEMO_CDS_CUBE_VIEW`.

``` abap
@EndUserText.label: 'CDS projection view, analytical query'
@AccessControl.authorizationCheck: #NOT_ALLOWED
define transient view entity DEMO_ANALYTICAL_QUERY_ELEM
  provider contract analytical_query
  with parameters
    p_preferred_currency : abap.cuky
  as projection on DEMO_CDS_CUBE_VIEW
{
          @AnalyticsDetails.query.axis: #FREE
          so_key                           as SalesOrderKey,

          @AnalyticsDetails.query.axis: #ROWS
          lifecycle_status                 as LifecycleStatus,

          _Currency._Text.CurrencyName : localized,
          //
          @AnalyticsDetails.query.axis: #COLUMNS
          quantity_sum                     as QuantitySum,
          //
          uom_sum                          as UnitOfQuantity,

          currency_sum                     as CurrCode,

          _Currency.AlternativeCurrencyKey as Currency,

          //typed literal
          @Aggregation.default: #FORMULA
          abap.decfloat34'0.05'            as Discount,

          //calculated unit
          @Aggregation.default: #FORMULA
          @Semantics.quantity.unitOfMeasure: 'AmPerQuanUnit'
          curr_to_decfloat_amount( amount_sum )
          / $projection.QuantitySum        as AmountPerQuantity,

          //calculated unit, defined as virtual element
  virtual AmPerQuanUnit : dd_cds_calculated_unit,

          //session variable
          @Aggregation.default: #FORMULA
          $session.system_date             as sysdat,

          @Aggregation.default: #FORMULA
          @Semantics.amount.currencyCode: 'CurrCode'
          currency_conversion(
            amount => amount_sum,
            source_currency => currency_sum,
            target_currency => $parameters.p_preferred_currency,
            exchange_rate_date => created_on
          )                                as convertedAmount
}
```

## Addition 1

`... AS alias`

### Description

Defines an alternative element name for the projected element. The alternative element name replaces the actual name of the element from the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md). The view field is created under the alternative element name in the CDS projection view. Accordingly, the alternative element name must comply with the general syntax rules for [names](../abap-cds-syntax/abencds_general_syntax_rules.md).

## Addition 2

`... LOCALIZED`

### Description

The keyword [`LOCALIZED`](abencds_localized.md) defines a [SQL path target field](../../abap-glossary/abensql_target_field_glosry.md) as [CDS localized field](../../abap-glossary/abencds_localized_field_glosry.md). The effect is that the field in question is automatically and implicitly filtered to the current system language. See the topic [CDS DDL - `LOCALIZED`](abencds_localized.md) for further details.

## Addition 3

`... VIRTUAL`

### Description

The keyword `VIRTUAL` defines a [CDS virtual element](../../abap-glossary/abencds_virtual_element_glosry.md) in a CDS projection view. In general, CDS virtual elements calculate field values during runtime, see topic [CDS DDL - `VIRTUAL`](abencds_proj_view_virtual_element.md).

In analytical queries, a virtual element is mostly used to define a [calculated unit](../abap-cds-data-types/abencds_calculated_quantity.md) for a [calculated quantity](../abap-cds-data-types/abencds_calculated_quantity.md). By using `VIRTUAL`, the analytical runtime automatically fills in the required value for the unit by interpreting the referred calculated quantity.

**Note:** In an analytical query, the annotation [`@ObjectModel.virtualElementCalculatedBy`](abencds_f1_element_annotation.md), which connects the virtual element to an ABAP class that calculates a value at runtime, is not supported.
