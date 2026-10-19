---
title: "ABAP CDS - Calculated Quantity with Calculated Unit"
source_file: abencds_calculated_quantity.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Types > ABAP CDS - Built-In Data Types > ABAP CDS - Special Data Types > ABAP CDS - Amounts and Quantities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Calculated Quantity with Calculated Unit

A [CDS calculated quantity](../../abap-glossary/abencds_calculated_quantity_glosry.md) is a component of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) or of a [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md) in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) used to store a quantity in a specific unit. A calculated quantity is always the result type of a calculation using [ABAP CDS amount fields](../../abap-glossary/abencds_amount_field_glosry.md) and/or [ABAP CDS quantity fields](../../abap-glossary/abencds_quantity_glosry.md). The DDIC data type of a calculated quantity is [`DECFLOAT34`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). A calculated quantity must be linked with a [ABAP CDS calculated unit](../../abap-glossary/abencds_calculated_unit_glosry.md) using the annotation [`@Semantics.quantity.unitOfMeasure: 'calculatedUnit'`](../abap-cds-data-definitions/abencds_f1_element_annotation.md). A calculated unit is a component of the same CDS view entity of data type `CHAR` that specifies a user-defined unit which is not contained in any list of pre-defined values. The DDIC data element `DD_CDS_CALCULATED_UNIT` and DDIC domain `DD_CDS_CALCULATED_UNIT` can be used to type a calculated unit, but this is not mandatory.

In CDS view entities, the following functions are available for amount and quantity fields:

- [`GET_NUMERIC_VALUE`](../abap-cds-data-definitions/abencds_conv_func_unit_curr_v2.md) removes reference information from an amount or quantity field.

- [`CURR_TO_DECFLOAT_AMOUNT`](../abap-cds-data-definitions/abencds_conv_func_unit_curr_v2.md) converts an amount field of data type `CURR` to data type `DECFLOAT34`, including shifting. The result remains an amount.

Calculated quantities can be the result type of the following expressions in CDS view entities:

- [Arithmetic expressions](../abap-cds-data-definitions/abencds_arit_exp_calc_v2.md)

- [Aggregate functions](../abap-cds-data-definitions/abencds_aggregate_functions_v2.md)

- [Simple](../abap-cds-data-definitions/abencds_simple_case_expression_v2.md) and [complex case expressions](../abap-cds-data-definitions/abencds_searched_case_expr_v2.md)

- **Note:** [Cast expressions](../abap-cds-data-definitions/abencds_cast_expression_v2.md) do not handle calculated quantities.

Moreover, special rules apply in the following operand positions in CDS view entities:

- [`UNION` views](../abap-cds-data-definitions/abencds_union_v2.md)

- [`INTERSECT` views](../abap-cds-data-definitions/abencds_intersect_v2.md)

- [Comparisons](../abap-cds-data-definitions/abencds_cond_expr_types_v2.md)

## Hints

- Reference annotations to currency or unit of measurement keys are propagated in CDS entities selecting from DDIC database tables or other CDS entities. It is possible, but not mandatory, to redefine them.

- Currently, CDS calculated quantities are only available in CDS view entities and in CDS projection views. They are not supported in any other [CDS entity](../../abap-glossary/abencds_entity_glosry.md).

- If a field is a calculated quantity, this characteristic is inherited when a view entity selects from another view entity.

- A calculated unit can be used as reference only once in a view. If a view contains several calculated quantity fields, each field needs a different calculated unit.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following CDS view entity, the field `rent_per_size` divides the amount of the rent for an apartment by the apartment size. The result is the cost per square meter. The calculated unit is `EUR/MTK`, `MTK` being the unit ID for square meter.

``` abap
@AccessControl.authorizationCheck: #NOT_ALLOWED
@EndUserText.label: 'CDS view entity, calculated quantity'

define view entity DEMO_CDS_CALCULATED_QUANTITY
  as select from demo_rent
{
  key apartment_id                     as ApartmentId,
      apartment_size                   as ApartmentSize,
      apartment_unit                   as ApartmentUnit,
      currency                         as Currency,
      
      // currency field and unit field in arith expression
      @Semantics.quantity.unitOfMeasure: 'calculatedUnit'
      rent_decfloat34 / apartment_size as rent_per_size,
      concat( concat(currency, '/' ), apartment_unit ) 
                                       as calculatedUnit
}
```

The class `CL_DEMO_CDS_CALCULATED_QUNTTY` accesses the view, inserts values into the underlying database table, and displays the result.
