---
title: "cstring_func - Processing Functions"
source_file: abenprocess_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - Processing Functions

The following processing functions have a character-like result. They can be declared at [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md) and [character-like expression positions](../../abap-glossary/abencharlike_expr_position_glosry.md). The return values have the type `string`.

- [`cmax`, `cmin` - Character-Like Extreme Value Functions](abencmax_cmin_functions.md)

- [`condense` - Condense Function](abencondense_functions.md)

- [`concat_lines_of` - Concatenation Function](abenconcatenation_functions.md)

- [`escape` - Escape Function](abenescape_functions.md)

- [`insert`- Insert Function](abeninsert_functions.md)

- [`match` - Match Function](abenmatch_functions.md)

- [`repeat` - Repeat Function](abenrepeat_functions.md)

- [`replace` - Replace Function](abenreplace_functions.md)

- [`reverse` - Reverse Function](abenreverse_functions.md)

- [`segment` - Segment Function](abensegment_functions.md)

- [`shift_left`, `shift_right` - Shift Functions](abenshift_functions.md)

- [`substring`, `substring_...` - Substring Functions](abensubstring_functions.md)

- [`to_upper`, `to_lower`, `to_mixed`, `from_mixed` - Case Functions](abencase_functions.md)

- [`translate` - Translate Function](abentranslate_functions.md)

The function [`boolc`](../abap-program-flow-logic/abenboole_functions.md) also has a return value of the type `string` and in principle is also one of these functions. It is handled, however, in accordance with its role as a [logical function](../../abap-glossary/abenlogic_function_glosry.md).

## Hints

- The processing functions for character-like arguments ignore the trailing blanks for input parameters with fixed lengths.

- The processing functions for character-like arguments cannot be used directly as operands of [arithmetic expressions](../../abap-glossary/abenarithmetic_expression_glosry.md) but can be used as operands of [descriptive functions](abendescriptive_functions.md).

- The type `string` of the return values must be respected mainly when using functions in comparisons.
