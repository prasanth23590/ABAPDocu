---
title: "rel_exp - Comparison Type of Elementary Data Objects"
source_file: abenlogexp_rules_operands_dobj.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules > rel_exp - Comparing Elementary Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparison Type of Elementary Data Objects

The following sections describe which [comparison types](../../abap-glossary/abencomparison_type_glosry.md) results from the combinations of different elementary data objects. They also list the rules that determine the length in which the comparison is performed for comparison types with generic lengths.

- [Comparison type of numeric data objects](abenlogexp_numeric.md)

- [Comparison type of character-like data objects](abenlogexp_character.md)

- [Comparison type of byte-like data objects](abenlogexp_byte.md)

- [Comparison Type of Date Fields, Time Fields, and Time Stamp Fields](abenlogexp_date_time.md)

## Hint

When converting between directly specified elementary data objects with different data types, all exceptions listed [here](../abap-processing-internal-data/abenconversion_elementary.md) can be raised. In comparisons, these are either handled implicitly or produce a runtime error. They cannot, however, be handled using [`CATCH`](abapcatch_try.md). In comparisons of expressions, it is possible to handle the exceptions partially.
