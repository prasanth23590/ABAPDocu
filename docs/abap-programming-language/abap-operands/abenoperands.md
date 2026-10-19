---
title: "ABAP - Operands"
source_file: abenoperands.html
section: "ABAP Programming Language"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP - Operands

[ABAP operands](../../abap-glossary/abenabap_operand_glosry.md) whose values can be evaluated in [read positions](../../abap-glossary/abenread_position_glosry.md) or modified in [write positions](../../abap-glossary/abenwrite_position_glosry.md) are:

- [Elementary operands](../../abap-glossary/abenelementary_operand_glosry.md)

  Elementary operands are [data objects](../../abap-glossary/abendata_object_glosry.md) that can be specified in various ways, either directly or using [field symbols](../../abap-glossary/abenfield_symbol_glosry.md) or [reference variables](../../abap-glossary/abenreference_variable_glosry.md) and so on.

- [Expressions](../../abap-glossary/abenexpression_glosry.md)

  At many read positions and some write positions, expressions can be specified instead of data objects. The statement then works with the result of the expression.

The following topics provide a detailed description of data objects and expressions as operands in [operand positions](../../abap-glossary/abenoperand_position_glosry.md).

- [Data Objects in Operand Positions](abenoperands_data_objects.md)

- [Expressions in Operand Positions](abenoperands_expressions.md)

Besides data objects and expression, there are also other kinds of operands that are specified in other operand positions than read and write positions. Examples of those are:

- Type specifications

  Statements can refer to types such as data types, classes, or interfaces. Examples are [declarations](../abap-declarations/abenabap_declarations.md), [typings](../abap-declarations/abentyping.md), or when [addressing components](abenoperands_names.md).

- Callable units from the same program or the repository

  Statements can call units such as [procedures](../../abap-glossary/abenprocedure_glosry.md) or ABAP programs. See [Calling and Exiting Program Units](../abap-calling-and-exiting-program-units/abenabap_execution.md).

- Resources

  Statements can access resources such as CDS entities, DDIC database or other resources. Examples are the statements of [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md).
