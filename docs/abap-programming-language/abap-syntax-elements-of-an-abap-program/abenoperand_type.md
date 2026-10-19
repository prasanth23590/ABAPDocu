---
title: "Operand Type"
source_file: abenoperand_type.html
section: "ABAP Programming Language > ABAP - Syntax Elements of an ABAP Program > ABAP Statements > Operand Positions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Operand Type

An operand position (read or write position) is typed by an operand type, which can be complete or generic and can also be dependent on other operand positions, for example in assignments. When a statement is executed, an operand with a suitable data type is expected. If an operand specified at an operand position has a different data type than the operand type, an attempt is usually made to convert the content of the operand to the operand type according to the [conversion rules](../abap-processing-internal-data/abenconversion_rules.md) at [read positions](../../abap-glossary/abenread_position_glosry.md), and in the other direction at [write positions](../../abap-glossary/abenwrite_position_glosry.md). Here, it should be noted that every conversion incurs increased runtime costs. If no corresponding conversion rule is defined, or the content cannot be converted, a syntax error occurs or an exception is raised. Any deviations from this rule, for example that the operand must exactly match the operand type or the operand is [cast](../../abap-glossary/abencast_casting_glosry.md) to the operand type regardless of its actual type, are described in the documentation of the individual statements.

- [Operand Positions with Elementary Data Type](abenoperand_type.md#operand-positions-with-elementary-data-type)

- [Operand Positions with Structured Data Type](abenoperand_type.md#operand-positions-with-structured-data-type)

- [Operand Positions with Tabular Data Type](abenoperand_type.md#operand-positions-with-tabular-data-type)

- [Operand Positions with Reference Data Type](abenoperand_type.md#operand-positions-with-reference-data-type)

## Operand Positions with Elementary Data Type

At operand positions for [elementary data objects](../../abap-glossary/abenelementary_data_object_glosry.md), the following must be specified when the statement is executed, depending on the operand type:

- [Character-like data objects](../../abap-glossary/abencharlike_data_object_glosry.md)

- [Numeric data objects](../../abap-glossary/abennumeric_data_object_glosry.md)

- [Byte-like data objects](../../abap-glossary/abenbyte_like_data_object_glosry.md)

Generically [typed](../../abap-glossary/abentyping_glosry.md) formal parameters or field symbols can also be specified statically if they are typed more generally than the expected type.

[Flat structures](../../abap-glossary/abenflat_structure_glosry.md) with only character-like components of the types `c`, `n`, `d`, or `t` can also be used in all operand positions where elementary fields are expected. Such structures are handled in the same way as a single data object of type `c` (implicit casting).

### Hint

An operand position with an elementary data type must not be confused with an [elementary operand](../../abap-glossary/abenelementary_operand_glosry.md).

## Operand Positions with Structured Data Type

Structures must be specified at operand positions for [structures](../../abap-glossary/abenstructure_glosry.md) when the statement is executed. Formal parameters or field symbols of the generic types `data` or `any` can also be specified statically.

## Operand Positions with Tabular Data Type

[Internal tables](../../abap-glossary/abeninternal_table_glosry.md) must be specified at operand positions for internal tables both when the statement is executed. There are also operand positions, where internal tables must be known statically. At these positions, generic formal parameters and field symbols can only be specified if they are typed with at least the generic type [`any table`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md). Only index tables can be specified at operand positions where index access occurs, and generic formal parameters and field symbols must be typed with at least the generic type [`index table`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md).

## Operand Positions with Reference Data Type

Depending on the operand type, either data or object reference variables must be specified at operand positions for [reference variables](../../abap-glossary/abenreference_variable_glosry.md) when the statement is executed. Formal parameters or field symbols of the generic types `data` or `any` can also be specified statically.
