---
title: "rel_exp - Binary Comparison Operators"
source_file: abenlogexp_any_operand.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Operators > rel_exp - Comparison Operators for All Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Binary Comparison Operators

The following table shows the binary comparison operators for comparisons between two operands (data objects or return values or [calculation expressions](../../abap-glossary/abencalculation_expression_glosry.md)) of any data types in [comparison expressions](../../abap-glossary/abencomparison_expression_glosry.md).

| **`operator`** | **Meaning**                                                                                          |
|----------------|------------------------------------------------------------------------------------------------------|
| `=`, `EQ`      | Equal: True, if the value of `operand1` is equal to the value of `operand2`.                         |
| `<>`, `NE`     | Not Equal: True, if the value of `operand1` is not equal to the value of `operand2`.                 |
| `<`, `LT`      | Less Than: True, if the value of `operand1` is less than the value of `operand2`.                    |
| `>`, `GT`      | Greater Than: True, if the value of `operand1` is greater than the value of `operand2`.              |
| `<=`, `LE`     | Less Equal: True, if the value of `operand1` is less than or equal to the value of `operand2`.       |
| `>=`, `GE`     | Greater Equal: True, if the value of `operand1` is greater than or equal to the value of `operand2`. |

The values are compared in accordance with the [comparison rules](abenlogexp_rules.md).

## Hints

- The operators `=`, `<>`, `<`, `>`, `<=`, and `>=` are equivalent to `EQ`, `NE`, `LT`, `GT`, `LE`, and `GE` respectively. It is recommended that only one or the other set of operators is used within the context of a program. If in doubt, the variant with the characters `=`, `<`, and `>` is considered to be more up-to-date, however this also contributes to the overload of these characters. Comparison operators that consist of two letters, on the other hand, are better suited to other comparison operators such as [`CO`](abenlogexp_strings.md), [`CN`](abenlogexp_strings.md), and so on, for which there are no alternative forms.

- Due to the [comparison rules](abenlogexp_rules.md), the size comparisons shown here are not suitable for determining the textual order of character-like data objects.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Logical expression as a termination condition of an unlimited [`DO`](abapdo.md) loop.

``` abap
CONSTANTS limit TYPE i VALUE 1000. 
DATA variable TYPE i. 
 
... 
 
DO. 
  IF variable > limit. 
    EXIT. 
  ENDIF. 
  ... 
ENDDO.
```
