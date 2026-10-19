---
title: "Conversion Rules for Elementary Data Objects"
source_file: abenconversion_elementary.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Conversion Rules for Elementary Data Objects

The programming language ABAP contains a set of [built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) [elementary data types](../../abap-glossary/abenelementary_data_type_glosry.md). It also supports automatic type conversions and length adjustments for assignments between all these data types except for [date fields](../../abap-glossary/abendate_field_glosry.md), [time fields](../../abap-glossary/abentime_field_glosry.md), and [time stamp fields](../../abap-glossary/abentimestamp_field_glosry.md), where conversions do not make sense.

The conversion tables in the following sections define the rules for converting all possible elementary target fields for

- [Numeric source fields](abennumeric_source_fields.md)

- [Character-like source fields](abencharacter_source_fields.md)

- [Byte-like source fields](abenbyte_source_fields.md)

- [Date fields, time fields, and time stamp fields as source fields](abendate_time_source_fields.md)

In all conversions, it must be possible to create a value from the type-specific value range from the content of the source field; otherwise an exception is raised that is defined in one of the subclasses of the class `CX_SY_CONVERSION_ERROR`. Conversion errors can usually be handled using [`CATCH`](../abap-program-flow-logic/abapcatch_try.md). There are some statements in which assignments take place whose conversion errors are either handled implicitly or lead to a runtime error directly.

After an exception, the content of the target field is undefined and should not be used. After an exception, the target field can contain either the previous value or an invalid value (the latter is the case after an overflow of a floating point number, for example).

## Hint

[Enumerated types](../../abap-glossary/abenenum_type_glosry.md) are elementary data types, but special [conversion rules](abenconversion_enumerated.md) apply, which ensure that only allowed values can be assigned to an [enumerated variable](../../abap-glossary/abenenumerated_variable_glosry.md).
