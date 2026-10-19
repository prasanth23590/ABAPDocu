---
title: "ABAP CDS - Amount Fields"
source_file: abencds_amount_field.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Types > ABAP CDS - Built-In Data Types > ABAP CDS - Special Data Types > ABAP CDS - Amounts and Quantities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Amount Fields

An [ABAP CDS amount field](../../abap-glossary/abencds_amount_field_glosry.md) is a component of a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) used to store an amount in a specific currency. An amount is an integer in the smallest unit of the currency. The integer is constructed from all figures in an amount field while ignoring the position of the decimal separator.

Possible [built-in DDIC data types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are `CURR`, `DECFLOAT34`, `DEC`, and `FLTP`. In case of data type `CURR`, a field is automatically interpreted as amount field and a reference to a [currency key](../../abap-glossary/abencurrency_key_glosry.md) using the annotation [`@Semantics.amount.currencyCode`](../abap-cds-data-definitions/abencds_f1_element_annotation.md) is mandatory. In case of the other data types, this reference is not mandatory but if used, it turns the field into an amount field.

A CDS amount field must be linked with a currency key that specifies the currency and the number of decimal places. A currency key is a component of a DDIC structure, DDIC database table, DDIC view, or of a CDS entity which has the type `CUKY`, and can contain a [currency ID](../../abap-glossary/abencurrency_id_glosry.md) from the DDIC database table `TCURC`.

By default, the number of decimal places for an amount is always two. Currencies with a different number of decimal places must also be entered in the table `TCURX`, where the number of decimal places can be defined explicitly.

For handling of CDS amount fields in ABAP Dictionary, handling in dynpros, and handling in ABAP programs, the same rules apply as for currency fields in DDIC, see topic [DDIC - Currency Fields](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_currency_field.md).

**Handling of CDS Amount Fields in Expressions in CDS View Entities**

In [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), special handling for CDS amount fields is implemented:

When used in [expressions](../abap-cds-data-definitions/abencds_expressions_v2.md), [`UNION` views](../abap-cds-data-definitions/abencds_union_v2.md), or [`INTERSECT`](../abap-cds-data-definitions/abencds_intersect_v2.md) views, the reference annotation of a CDS amount field to a currency key is considered. Special rules apply concerning how amounts and quantities can be combined in calculations, compatibility of data types, and result types. A new result type is available: the [CDS calculated quantity](../../abap-glossary/abencds_calculated_quantity_glosry.md). The rules are documented in the respective sections:

- [Amounts and quantities in arithmetic expressions](../abap-cds-data-definitions/abencds_arit_exp_calc_v2.md)

- [Amounts and quantities in aggregate functions](../abap-cds-data-definitions/abencds_aggregate_functions_v2.md)

- Amounts and quantities in [simple](../abap-cds-data-definitions/abencds_simple_case_expression_v2.md) and [complex case expressions](../abap-cds-data-definitions/abencds_searched_case_expr_v2.md)

- [Amounts and quantities in `UNION` views](../abap-cds-data-definitions/abencds_union_v2.md)

- [Amounts and quantities in `INTERSECT` views](../abap-cds-data-definitions/abencds_intersect_v2.md)

- Amounts and quantities in [comparisons](../abap-cds-data-definitions/abencds_cond_expr_types_v2.md).

**Note:** [Cast expressions](../abap-cds-data-definitions/abencds_cast_expression_v2.md) do not handle amounts. Only the target type CURR requires a reference to a currency key.

The following two conversion functions are available for amounts in CDS view entities:

- [`GET_NUMERIC_VALUE`](../abap-cds-data-definitions/abencds_conv_func_unit_curr_v2.md): removes the reference to a currency key and returns the numeric value of a field.

- [`CURR_TO_DECFLOAT_AMOUNT`](../abap-cds-data-definitions/abencds_conv_func_unit_curr_v2.md): converts an amount field of data type `CURR` into an amount field of data type `DECFLOAT34`.

- **Note:** The function [`DECIMAL_SHIFT`](../abap-cds-obsolete-language-elements/abencds_conv_func_unit_curr_v1.md) is not available in CDS view entities.

## Hints

- Reference annotations that assign a currency key to a field are propagated in CDS entities selecting from DDIC database tables or other CDS entities. It is possible, but not mandatory, to redefine them. This is true for all CDS entities except for CDS DDIC-based views (obsolete).

- Currently, the handling of CDS amount fields in expressions is only available in CDS view entities and not in any other [CDS entity](../../abap-glossary/abencds_entity_glosry.md).

- Currencies are handled as specified by the data saved in the database tables `TCUR...` of the package `SFIB`. The exchange rates and other settings can be maintained in transaction `OB08`.
