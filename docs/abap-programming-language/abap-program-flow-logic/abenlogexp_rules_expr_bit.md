---
title: "rel_exp - Comparison Type of Bit Expressions"
source_file: abenlogexp_rules_expr_bit.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules > rel_exp - Comparing Elementary Data Types > rel_exp - Comparison Type of Calculation Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparison Type of Bit Expressions

[Bit expressions](../../abap-glossary/abenbit_expression_glosry.md) can be used as operands of comparison expressions with the following:

- [Comparison operators for all data types](abenlogexp_compare_all.md)

- [Comparison operators for byte-like data types](abenlogexp_bytes.md)

- [Comparison operators for bit patterns](abenlogexp_bitmasks.md)

A [bit expression](../abap-processing-internal-data/abapcompute_bit.md) can be compared with a single operand of a [byte-like data type](../../abap-glossary/abenbyte_like_data_typ_glosry.md) or with a different bit expression.

Each bit expression of a comparison expression is calculated based on the length of the single longest operand, for which shorter operands are padded on the right with hexadecimal 0. All operands of the entire comparison expression are considered. The result of the involved bit expressions is contained in this length and, if necessary, a single operand is padded with hexadecimal 0 on the right before comparison. The comparison is then performed according to the [comparison rule](abencomparison_type.md) for a byte-like [comparison type](../../abap-glossary/abencomparison_type_glosry.md).

## Hint

A bit expression cannot be specified as the operand of a [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example shows the different ways lengths are handled in comparisons between byte fields and bit expressions. The bit expression in the first comparison is evaluated with length 4 and produces the value hexadecimal 1100. The single operand on the right is lengthened to the value hexadecimal 1100 by filling with hexadecimal 00 and the equality comparison is true. In the second comparison, on the other hand, the operand on the left is converted to the type `xstring` and the operand on the right is not lengthened, which is why the inequality comparison is true.

``` abap
IF x`FFFF` BIT-AND x`11` = xstring`11`. 
  ... 
ENDIF. 
 
IF x`1100` <> xstring`11`. 
  ... 
ENDIF.
```
