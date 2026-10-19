---
title: "rel_exp - Comparison Type of Calculation Expressions"
source_file: abenlogexp_rules_expressions.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules > rel_exp - Comparing Elementary Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparison Type of Calculation Expressions

Any [calculation expression](../../abap-glossary/abencalculation_expression_glosry.md) can be specified as an operand of a [comparison expression](../../abap-glossary/abencomparison_expression_glosry.md).

The table below summarizes the combinations in which calculation expressions can be listed in comparison expressions:

| **One side**                                                                                                                                   | **Comparison operator**                                                                                                                                                                                                                  | **Other side**                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Single operand with [numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md) or [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md)   | [`=`, `EQ`, `<>`, `NE`, `<`, `LT`, `>`, `GT`, `<=`, `LE`, `>=`, `GE`](abenlogexp_any_operand.md)                                                                                                                                       | [Arithmetical expression](../../abap-glossary/abenarithmetic_expression_glosry.md) |
| Single operand with any [elementary data type](../../abap-glossary/abenelementary_data_type_glosry.md) or [string expression](../../abap-glossary/abenstring_expression_glosry.md) | [`=`, `EQ`, `<>`, `NE`, `<`, `LT`, `>`, `GT`, `<=`, `LE`, `>=`, `GE`](abenlogexp_any_operand.md), [`CO`, `CN`, `CA`, `NA`, `CS`, `NS`, `CP`, `NP`](abenlogexp_strings.md)                                                            | [String expression](../../abap-glossary/abenstring_expression_glosry.md)           |
| Single operand with [byte-like data type](../../abap-glossary/abenbyte_like_data_typ_glosry.md) or [bit expression](../../abap-glossary/abenbit_expression_glosry.md)              | [`=`, `EQ`, `<>`, `NE`, `<`, `LT`, `>`, `GT`, `<=`, `LE`, `>=`, `GE`](abenlogexp_any_operand.md), [`BYTE-CO`, `BYTE-CN`, `BYTE-CA`, `BYTE-NA`, `BYTE-CS`, `BYTE-NS`](abenlogexp_bytes.md), [`O`, `Z`, `M`](abenlogexp_bitmasks.md) | [Bit expression](../../abap-glossary/abenbit_expression_glosry.md)                 |

The [comparison type](../../abap-glossary/abencomparison_type_glosry.md) is determined differently depending on the type of calculation expression.

- [Comparison type of arithmetic expressions](abenlogexp_rules_expr_arith.md)

- [Comparison type of string expressions](abenlogexp_rules_expr_char.md)

- [Comparison type of bit expressions](abenlogexp_rules_expr_bit.md)

In comparison expressions with the comparison operators [`BETWEEN`](abenlogexp_between.md) and [`IN`](abenlogexp_select_option.md), which are converted internally to combinations of comparisons with the binary operators above, the rules of the respective comparisons apply.

## Hints

- [Relational expression](../../abap-glossary/abenrelational_expression_glosry.md) cannot yet be compared. Instead, they can be combined using [Boolean operators](../../abap-glossary/abenboolean_operator_glosry.md), where the combination with the operator [`EQUIV`](abenlogexp_equiv.md) corresponds to the comparison of the resulting [truth values](../../abap-glossary/abentruth_value_glosry.md) for equality.

- A [calculation expression](../../abap-glossary/abencalculation_expression_glosry.md) cannot be specified as the operand of a [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md).
