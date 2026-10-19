---
title: "initial value"
source_file: abeninitial_value_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# initial value

[ABAP Language](../abap-programming-language/abenabala_glossary.md) [DDIC](../abap-dictionary-ddic/abenddic_glossary.md)

## Definition

The ABAP runtime framework defines an initial value for each [data type](abendata_type_glosry.md). The initial values of the [elementary data types](abenelementary_data_type_glosry.md) depend on the corresponding [built-in ABAP type](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md). The initial value of [reference types](abenreference_type_glosry.md) is the [null reference](abennull_reference_glosry.md). The initial value of an [internal table](abeninternal_table_glosry.md) is an empty table without lines. The initial value of [structured types](abenstructured_type_glosry.md) is produced from the initial values of the individual [structure components](abenstructure_component_glosry.md). The statement [`CLEAR`](../abap-programming-language/abap-processing-internal-data/abapclear.md) with no additions sets a [data object](abendata_object_glosry.md) to the appropriate initial value for its type. Initial values are also assigned to most [built-in data types](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) in [ABAP Dictionary](abenabap_dictionary_glosry.md), but those are not evaluated in ABAP programs.
