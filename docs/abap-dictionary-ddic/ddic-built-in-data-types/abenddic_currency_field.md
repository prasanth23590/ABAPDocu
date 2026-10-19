---
title: "DDIC - Currency Fields"
source_file: abenddic_currency_field.html
section: "ABAP Dictionary (DDIC) > DDIC - Built-In Data Types > DDIC - Properties of the Built-In Dictionary Types > DDIC - Special Dictionary Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Currency Fields

A currency field is a component of a DDIC structure, DDIC database table, or DDIC view used to store an amount in a specific currency. A currency amount is an integer in the smallest unit of the currency. The integer is constructed from all figures in a currency field while ignoring the position of the decimal separator.

A currency field can have data type `CURR`, `DECFLOAT16`, or `DECFLOAT34`. In case of data type `CURR`, a field is automatically interpreted as currency field and a reference to a currency key is mandatory. In case of the other data types, this reference is not mandatory, but if it is assigned, it turns the field into a currency field.

The currency key specifies the currency and the number of decimal places of a currency field. It is a component of a DDIC structure, DDIC database table, or DDIC view, has the type `CUKY`, and can contain a [currency ID](../../abap-glossary/abencurrency_id_glosry.md) from the DDIC database table `TCURC`.

By default, the number of decimal places for a currency is always two. Currencies with a different number of decimal places must also be entered in the table `TCURX`, where the number of decimal places can be defined explicitly.

- [Handling in ABAP Dictionary](abenddic_currency_field.md#handling-in-abap-dictionary)

- [Handling in ABAP Programs](abenddic_currency_field.md#handling-in-abap-programs)

## Hints

- Currencies are handled according to the rules defined in the database tables `TCUR...` of the package `SFIB`. The exchange rates and other settings can be maintained in transaction `OB08`.

- ABAP CDS has its own handling of currency fields, see topic [ABAP CDS - Amount Fields](../../abap-core-data-services-abap-cds/abap-cds-data-types/abencds_amount_field.md).

## Handling in ABAP Dictionary

A data element of data type [`CURR`](abenddic_builtin_types.md) is handled as a field of data type [`DEC`](abenddic_builtin_types_int_pack.md) and is stored in DDIC database tables in the [BCD](../../abap-glossary/abenbcd_glosry.md) format. When creating a data element or a structure component of the data type `CURR` in an ABAP Dictionary tool, a number of decimal places other than zero must be defined. The standard value is two decimal places.

A currency field of data type `DECFLOAT16` or `DECFLOAT34` is handled according to its data type.

For every structure component of data type `CURR`, a component of the same structure or of a different DDIC structure, DDIC database table, or DDIC view must be specified as a [reference field](../ddic-data-types/abenddic_structures_sema.md) with the data type [`CUKY`](abenddic_builtin_types.md). This field is the [currency key](../../abap-glossary/abencurrency_key_glosry.md) that defines the actual currency. From a technical perspective, the data type `CUKY` is handled like a type `CHAR` with length 5.

### Hints

- The conversion function `CURRENCY_CONVERSION` ([CDS view entity](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_conversion_functions_v2.md), [CDS DDIC-based view (obsolete)](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_conversion_functions_v1.md)) in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) also assumes two decimal places for currency fields. If the function for currency fields is used with other amounts of decimal places, unexpected behavior may arise.

- As in [general packed numbers](abenddic_builtin_types_int_pack.md), the number of places in type `CURR` should be odd.

## Handling in ABAP Programs

The ABAP type that corresponds to the data type `CURR` is `p`. An ABAP data object declared with reference to a dictionary type of type `CURR` has the number of decimal places defined there (greater than or equal to one and the default is two). These decimal places are respected for all operations and calculations, as for all packed numbers. The only exceptions are the programs for which the program property [*fixed point arithmetic*](../../abap-glossary/abenfixed_point_arithmetic_glosry.md) was not set. When reading currency fields with [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), no special handling takes place.

To work correctly with a currency field, all digits in the number must be taken as the currency amount in the smallest possible currency units, regardless of the number of decimal places. This occurs automatically sometimes, for example, if `CURRENCY` is used after `WRITE [TO]` (this is possible for currency fields of data types `CURR`, `DECFLOAT16`, and `DECFLOAT34`) or the formatting option [`CURRENCY`](../../abap-programming-language/abap-processing-internal-data/abapcompute_string_format_options.md) in an [embedded expression](../../abap-programming-language/abap-processing-internal-data/abenstring_templates_expressions.md) of a [string template](../../abap-programming-language/abap-processing-internal-data/abenstring_templates.md). For other operations, the following restrictions apply:

- Comparison, addition, subtraction, and division of two currency fields with the same number of decimal places are not critical.

- Multiplication with and division by a non-currency-dependent number is not critical.

- All other operations are critical, for example:

  - Multiplication of two currency fields.

  - Operations between two fields with different currencies that include assignments.

  - Assignments of non-currency-dependent numbers to currency fields.

Accurate results should not be expected when performing critical operations if the number of decimal places in the program does not match the number in the currency.

### Hints

- The methods `CONVERT_CURR_TO_DECFLOAT` and `CONVERT_DECFLOAT_TO_CURR` of the system class [`CL_ABAP_DECFLOAT`](../../abap-programming-language/abap-processing-internal-data/abencl_abap_decfloat_doc.md) convert currency amounts to decimal floating point numbers (and back) as specified by a currency key.

- For currencies, one of the data types for [decimal floating point numbers](abenddic_decimal_floating_point.md) is recommended rather than the data type `CURR`.
