---
title: "rel_exp - Comparing Elementary Data Types"
source_file: abenlogexp_rules_operands.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparing Elementary Data Types

If `operand1` and `operand2` of a [comparison expression](../../abap-glossary/abencomparison_expression_glosry.md) have elementary data types, they are used to determine a common elementary [comparison type](../../abap-glossary/abencomparison_type_glosry.md). Every comparison type has [comparison rules](abencomparison_type.md) used to perform the comparison. Operands that are not compatible with the comparison type are converted to this type. The following sections show how the comparison type is determined for the various comparisons:

- [Comparison type of elementary data objects](abenlogexp_rules_operands_dobj.md)

- [Comparison type of calculation expressions](abenlogexp_rules_expressions.md)

The return values or results of functional methods, built-in functions, constructor expressions, and table expressions are handled like elementary data objects.

## Hints

- Previous assignments to helper variables of certain types or the conversion operator [`CONV`](../abap-processing-internal-data/abenconstructor_expression_conv.md) can be used to force comparison types and conversions other than a direct comparison of the operands.

- It should be noted that some built-in functions operate have the same effect as an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md) if they are passed a [numeric expression](../../abap-glossary/abennumerical_expression_glosry.md) as an argument.

- For [enumerated types](../../abap-glossary/abenenum_type_glosry.md), a special [rule](abenlogexp_rules_operands_enum.md) applies.
