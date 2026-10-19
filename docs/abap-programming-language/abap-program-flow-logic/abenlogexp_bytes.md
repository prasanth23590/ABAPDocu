---
title: "rel_exp - Comparison Operators for Byte-Like Data Types"
source_file: abenlogexp_bytes.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Operators"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparison Operators for Byte-Like Data Types

The following table shows the comparison operators for comparisons between byte-like operands (single data objects or return values or [bit expressions](../../abap-glossary/abenbit_expression_glosry.md)) in [comparison expressions](../../abap-glossary/abencomparison_expression_glosry.md).

| **operator** | **Meaning**                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BYTE-CO`    | Contains Only: True, if `operand1` only contains bytes from `operand2`. If `operand2` is of type `xstring` and initial, the comparison expression is false, unless `operand1` is also of type `xstring` and initial, in which case the comparison expression is always true. If the comparison is false, `sy-fdpos` contains the offset of the first byte in `operand1`, which is not contained in `operand2`. If the comparison is true, `sy-fdpos` contains the length of `operand1`. |
| `BYTE-CN`    | Contains Not Only: True, if a comparison expression with `BYTE-CO` is false, provided that `operand1` does not only contain bytes from `operand2`. If the comparison is true, `sy-fdpos` contains the offset of the first byte in `operand1` that is not contained in `operand2`. If the comparison is false, `sy-fdpos` contains the length of `operand1`.                                                                                                                             |
| `BYTE-CA`    | Contains Any: True, if `operand1` contains at least one byte from `operand2`. If `operand1` or `operand2` are of the type `xstring` and initial, the comparison expression is always false. If the comparison is true, `sy-fdpos` contains the offset of the first byte in `operand1` that is also contained in `operand2`. If the comparison is false, `sy-fdpos` contains the length of `operand1`.                                                                                   |
| `BYTE-NA`    | Contains Not Any: True, if a comparison expression with `BYTE-CA` is false, provided that `operand1` does not contain a byte from `operand2`. If the comparison is false, `sy-fdpos` contains the offset of the first byte in `operand1` that is also contained in `operand2`. If the comparison is true, `sy-fdpos` contains the length of `operand1`.                                                                                                                                 |
| `BYTE-CS`    | Contains String: True, if the content of `operand2` is contained in `operand1`. If `operand1` is of type `xs` and initial, the comparison expression is false, unless `operand2` is also of type `xstring` and initial, in which case the comparison expression is always true. If the comparison is true, `sy-fdpos` contains the offset of `operand2` in `operand1`. If the comparison is false, `sy-fdpos` contains the length of `operand1`.                                        |
| `BYTE-NS`    | Contains No String: True, if a comparison expression with `BYTE-CS` is false, provided that `operand1` does not contain the content of `operand2`. If the comparison is false, `sy-fdpos` contains the offset of `operand2` in `operand1`. If the comparison is true, `sy-fdpos` contains the length of `operand1`.                                                                                                                                                                     |

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The logical expression in the `IF` statement is true, if the second half-byte is not filled for any of the bytes in `hex1`.

``` abap
DATA: hex1 TYPE xstring, 
      hex2 TYPE xstring. 
 
hex1 = ... 
hex2 = '000102030405060708090A0B0C0D0E0F'. 
 
IF hex1 BYTE-CO hex2. 
  ... 
ENDIF.
```
