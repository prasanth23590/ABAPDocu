---
title: "rel_exp - Comparison Operators for Bit Patterns"
source_file: abenlogexp_bitmasks.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Operators"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparison Operators for Bit Patterns

The table below shows the comparison operators for comparisons of operands (single data objects or return values or [bit expressions](../../abap-glossary/abenbit_expression_glosry.md)) with bit patterns in byte-like operands in [comparison expressions](../../abap-glossary/abencomparison_expression_glosry.md). The data type of the right operand `operand2` must be byte-like (`x` or `xstring`). It contains the bit pattern with which the left operand `operand1` is compared. If `operand1` is shorter than `operand2`, hexadecimal zeros are appended to the right of `operand1` in accordance with the [comparison rules](abenlogexp_rules_operands.md) to lengthen it appropriately. No further conversion takes place. The data type of `operand1` must also be byte-like (`x` or `xstring`).

| **`operator`** | **Meaning**                                                                                                                                                                       |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `O`            | Ones: True, if the bits that are 1 in `operand2`, are also 1 in `operand1`. If `operand2` contains only zeros, the comparison expression is always true.                          |
| `Z`            | Zeros: True, if the bits that are 1 in `operand2` are 0 in `operand1`. If `operand2` contains only zeros, the comparison expression is always true.                               |
| `M`            | Mixed: True, if of the bits that are 1 in `operand2`, at least one is 1 and one is 0 in `operand1`. If `operand2` contains only zeros, the comparison expression is always false. |

## Hint

For the result of the comparisons, it is irrelevant whether the bits that are 0 in `operand2`, are 1 or 0 in `operand1`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The logical expression in the `IF` statement is false because `00` is appended to the right of `hex1` before the comparison. If the content of `hex2` were `111100`, the comparison would be true.

``` abap
DATA: hex1 TYPE xstring, 
      hex2 TYPE xstring. 
 
hex1 = 'FFFF'. 
hex2 = '111111'. 
 
IF hex1 O hex2. 
  ... 
ENDIF.
```
