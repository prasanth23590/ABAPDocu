---
title: "packed number type"
source_file: abenpacked_number_type_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# packed number type

[ABAP Language](../abap-programming-language/abenabala_glossary.md) [DDIC](../abap-dictionary-ddic/abenddic_glossary.md) [General](abenabap_glossary.md)

## Definition

[Numeric data type](abennumeric_data_type_glosry.md) for saving [fixed point numbers](abenfixed_point_number_glosry.md) with a fixed number of [decimal places](abendecimal_place_glosry.md) The associated [built-in ABAP type](abenbuiltin_abap_type_glosry.md) is [`p`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md). The [built-in DDIC type](abenbuiltin_ddic_type_glosry.md) is [`DEC`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The number of decimal places is a property of the data type and not, as with [floating point numbers](abenfloating_point_number_glosry.md), a property of the data itself. Calculations with packed numbers are performed using [fixed point arithmetic](abenfixed_point_arithmetic_glosry.md). The internal representation uses the [BCD](abenbcd_glosry.md) format. A [data object](abendata_object_glosry.md) of a packed number type is a [packed number](abenpacked_number_glosry.md).

[***-\>* More about**](../abap-programming-language/abap-processing-internal-data/abennumber_types.md)
