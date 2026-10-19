---
title: "itab - Built-in Functions (itab_func)"
source_file: abenitab_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Built-in Functions (itab_func)

The following [built-in functions](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) work with internal tables as arguments:

- [`lines` - Line Function](abendescriptive_functions_table.md)

- [`line_index` - Index Function](abenline_index_function.md)

Furthermore, the string function [`concat_lines_of`](abenconcatenation_functions.md) expects an internal table as an argument and the predicate function [`line_exists`](../abap-program-flow-logic/abenline_exists_function.md) expects a [table expression](../../abap-glossary/abentable_expression_glosry.md) or a [mesh path expression](../../abap-glossary/abenmesh_path_expression_glosry.md).

## Hints

- Built-in functions for internal tables can be used in suitable [operand positions](../abap-syntax-elements-of-an-abap-program/abenexpression_positions.md), for example directly as an operand of [arithmetic](../../abap-glossary/abenarithmetic_expression_glosry.md) or [relational expressions](../../abap-glossary/abenrelational_expression_glosry.md).

- The term [table function](../../abap-glossary/abentable_function_glosry.md) is generally used for functions that return tabular data as a result. But the above functions might also be called table functions similar to [string functions](../../abap-glossary/abenstring_function_glosry.md) that work with strings as arguments.
