---
title: "Expressions"
source_file: abenexpressions.html
section: "ABAP Programming Language > ABAP - Operands > Expressions in Operand Positions > Operators and Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Expressions

The following expressions can be specified in [expression positions](../../abap-glossary/abenexpression_position_glosry.md):

- Write positions

  - [Declaration expressions](../abap-declarations/abeninline_declarations.md)

  - Certain [constructor expressions](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md)

  - Certain [table expressions](../abap-processing-internal-data/abentable_expressions.md)

- Read positions

  - [Built-in Functions](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) and [functional method calls](../abap-calling-and-exiting-program-units/abapcall_method_functional.md)

  - [Logical expressions](../abap-program-flow-logic/abenlogexp.md)

  - [Constructor expressions](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md)

  - [Table expressions](../abap-processing-internal-data/abentable_expressions.md) and [mesh path expressions](../abap-processing-internal-data/abenmesh_path_expression.md)

  - [Arithmetic expressions](../abap-processing-internal-data/abapcompute_arith.md)

  - [String expressions](../abap-processing-internal-data/abapcompute_string.md)

  - [Bit expressions](../abap-processing-internal-data/abapcompute_bit.md)

An expression in a [write position](../../abap-glossary/abenwrite_position_glosry.md) has a result that is assigned a value.

An expression in a [read position](../../abap-glossary/abenread_position_glosry.md) has a result that is used as an operand in the statement. Logical expressions can contain [calculation expressions](../../abap-glossary/abencalculation_expression_glosry.md), that is, arithmetic expressions, string expressions, and bit expressions as operands of relational expressions. The three different calculation expression types cannot currently be mixed within a calculation expression.

## Hints

- Although the calculation expression types cannot be mixed directly, a different type of expression can be used as an argument of a allowed function in another expression. In the same way, logical expressions can occur as arguments of [Boolean functions](../../abap-glossary/abenboole_function_glosry.md) in calculation expressions.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), three other kinds of expressions are possible:

  - [SQL expressions](../../abap-glossary/abensql_expression_glosry.md)

  - [Aggregate expressions](../../abap-glossary/abenaggregate_expression_glosry.md)

  - [SQL path expressions](../../abap-glossary/abensql_path_expression_glosry.md)

    The ABAP expressions above can be used as [host expressions](../../abap-glossary/abenhost_expression_glosry.md) in ABAP SQL.
