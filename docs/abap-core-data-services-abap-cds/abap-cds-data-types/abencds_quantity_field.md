---
title: "ABAP CDS - Quantity Fields"
source_file: abencds_quantity_field.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Types > ABAP CDS - Built-In Data Types > ABAP CDS - Special Data Types > ABAP CDS - Amounts and Quantities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Quantity Fields

An [ABAP CDS quantity field](../../abap-glossary/abencds_quantity_glosry.md) is a component of a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) used to store a quantity in a specific unit.

Possible [built-in ABAP Dictionary data types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are `QUAN`, `DECFLOAT16`, `DECFLOAT34`, `DEC`, `FLTP`, `INT1`, `INT2`, or `INT4`. In the case of data type `QUAN`, the field is automatically interpreted as quantity field and a reference to a [unit of measurement key](../../abap-glossary/abenunit_glosry.md) using the annotation [`@Semantics.quantity.unitOfMeasure`](../abap-cds-data-definitions/abencds_f1_element_annotation.md) is mandatory. In the case of the other data types, this reference is not mandatory but if used, it turns the field into a quantity field.

A quantity field must be linked with a unit key that defines the unit and the number of decimal places. A unit key is a component of a structure, DDIC database table, DDIC view or of another CDS entity of type `UNIT` and it can contain a [unit ID](../../abap-glossary/abenunit_id_glosry.md) from the DDIC database table `T006`.

For handling of CDS quantity fields in ABAP Dictionary, handling in dynpros, and handling in ABAP programs, the same rules apply as for currency fields in DDIC, see topic [ABAP DDIC - Quantity Fields](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_quantity_field.md).

**Handling of CDS Quantity Fields in Expressions in CDS View Entities**

In CDS view entities, special handling for CDS quantity fields is implemented:

When used in [expressions](../abap-cds-data-definitions/abencds_expressions_v2.md), [`UNION` views](../abap-cds-data-definitions/abencds_union_v2.md), or [`INTERSECT`](../abap-cds-data-definitions/abencds_intersect_v2.md) views, the reference annotation of a CDS quantity field to a unit key is considered. Special rules apply concerning how amounts and quantities can be combined in calculations, compatibility of data types, and result types. A new result type is available: the [CDS calculated quantity](../../abap-glossary/abencds_calculated_quantity_glosry.md). The rules are documented in the respective sections:

- [Amounts and quantities in arithmetic expressions](../abap-cds-data-definitions/abencds_arit_exp_calc_v2.md)

- [Amounts and quantities in aggregate functions](../abap-cds-data-definitions/abencds_aggregate_functions_v2.md)

- Amounts and quantities in [simple](../abap-cds-data-definitions/abencds_simple_case_expression_v2.md) and [complex case expressions](../abap-cds-data-definitions/abencds_searched_case_expr_v2.md)

- [Amounts and quantities in `UNION` views](../abap-cds-data-definitions/abencds_union_v2.md)

- [Amounts and quantities in `INTERSECT` views](../abap-cds-data-definitions/abencds_intersect_v2.md)

- Amounts and quantities in [comparisons](../abap-cds-data-definitions/abencds_cond_expr_types_v2.md).

**Note:** [Cast expressions](../abap-cds-data-definitions/abencds_cast_expression_v2.md) do not handle quantities. Only the target type QUAN requires a reference to a unit key.

The following conversion function is available for quantities in CDS view entities:

- [`GET_NUMERIC_VALUE`](../abap-cds-data-definitions/abencds_conv_func_unit_curr_v2.md): removes the reference to a unit key and returns the numeric value of a field.

## Hints

- Reference annotations that assign a unit key to a field are propagated in CDS entities selecting from DDIC database tables or other CDS entities. It is possible, but not mandatory, to redefine them. This is true for all CDS entities except for CDS DDIC-based views (obsolete).

- Currently, the handling of CDS quantity fields in expressions is only available in CDS view entities and not in any other [CDS entity](../../abap-glossary/abencds_entity_glosry.md).

- Integer types, although technically possible, might not be suitable as quantity fields in some cases, since many units of measurement require decimal places.
