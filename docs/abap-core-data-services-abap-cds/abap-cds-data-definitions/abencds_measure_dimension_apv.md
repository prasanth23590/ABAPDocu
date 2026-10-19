---
title: "CDS DDL - Conceptual Background, Analytical Query"
source_file: abencds_measure_dimension_apv.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Analytical Queries"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - Conceptual Background, Analytical Query

This topic explains some of the conceptual background of analytical data models.

- [Analytical Cube View and Analytical Dimension View](abencds_measure_dimension_apv.md#analytical-cube-view-and-analytical-dimension-view)

- [Analytical Query](abencds_measure_dimension_apv.md#analytical-query)

## Analytical Cube View and Analytical Dimension View

The projected entity of a [CDS analytical projection view](../../abap-glossary/abencds_analytical_pv_glosry.md) must be an [analytical cube view](../../abap-glossary/abencds_analytical_cube_glosry.md) or an [analytical dimension view](../../abap-glossary/abencds_anal_dim_view_glosry.md). The fields of an analytical cube view and an analytical dimension view are interpreted as [analytical measure fields](../../abap-glossary/abencds_measure_glosry.md) and [analytical dimension fields](../../abap-glossary/abencds_dimension_glosry.md).

- Analytical dimension field:

  Field that describes a characteristic or attribute and that can be used for [grouping](abencds_group_by_v2.md) or filtering. For example if a view describes a sales order, the following columns can be dimension fields: customer, date, region. Dimension fields can have a [foreign key](../../abap-glossary/abenforeign_key_glosry.md) association with a dimension view or a text view as association target. A dimension field must have one of the following data types: [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`NUMC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT1`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT2`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT8`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`UNIT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CUKY`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`LANG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CLNT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`SSTR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`RAW(16)`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Analytical measure field:

  Field that contains measurable data. In other words, an analytical measure can be any element that contains quantifiable data that can be calculated and aggregated, for example, the total price of all sales order positions. The aggregation behavior is defined via the annotation [`@Aggregation.default`](abencds_f1_element_annotation.md). Measures can have a reference to a [unit key](../../abap-glossary/abenunit_glosry.md) or [currency key](../../abap-glossary/abencurrency_key_glosry.md). The following data types are possible: [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DECFLOAT16`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DECFLOAT34`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT1`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT2`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT8`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DF16_DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DF34_DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DF16_RAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

## Analytical Query

The fields of a CDS analytical projection view can be classified into the following categories:

- [Analytical formula](../../abap-glossary/abencds_formula_glosry.md):

  Field of a CDS analytical projection view that is added in the projection layer as a new field. A formula can be an [arithmetic expression](abencds_arithmetic_expression_v2.md), a [currency conversion](abencds_conv_func_unit_curr_v2.md) using the built-in function [`CURRENCY_CONVERSION`](abencds_conv_func_unit_curr_v2.md), a [unit conversion](abencds_conv_func_unit_curr_v2.md) using the built-in function [`UNIT_CONVERSION`](abencds_conv_func_unit_curr_v2.md), or a [formula-related case expression](abencds_case_expression_apv.md). The annotation `Aggregation.default: #FORMULA` is mandatory.

- [Analytical selection](../../abap-glossary/abencds_selection_glosry.md):

  Field of a CDS analytical projection view that is newly added in the projection layer. A selection is defined by means of a [selection-related case expression](abencds_case_expression_apv.md), also called restricted measure.

- Dimension field: field of an analytical projection view that is defined as dimension field in the underlying [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md).

- Text fields and attributes relating to a dimension. Such fields are included via [path expressions](abencds_path_expr_apv.md).

- [CDS amount fields](../../abap-glossary/abencds_amount_field_glosry.md), [CDS quantity fields](../../abap-glossary/abencds_quantity_glosry.md), [currency key](../../abap-glossary/abencurrency_key_glosry.md) fields, and [unit key](../../abap-glossary/abenunit_glosry.md) fields.

## More Information

Development guide for [ABAP Analytics](https://help.sap.com/docs/ABAP_Cloud/67127c83ae1a4917b6b65ec222416894/4ae5db4d9bfd472ba70613b358dbb16b?version=sap_cross_product_abap)
