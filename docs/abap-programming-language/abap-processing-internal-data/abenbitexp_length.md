---
title: "bit_exp - Calculation Length"
source_file: abenbitexp_length.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Byte Chain Processing > Bit Expressions (bit_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# bit_exp - Calculation Length

A bit expression is assigned a calculation length in which the operation is executed.

The calculation length is the length of the longest bit expression operand involved. Unlike in the [calculation type](../../abap-glossary/abencalculation_type_glosry.md) of an arithmetic expression, the type of the result is not included.

Before the entire expression is evaluated, all operands involved are converted to the length of the longest operand based on the [rules for the source field type `x`](abenconversion_type_x.md) and [`xstring`](abenconversion_type_xstring.md). This means that shorter operands are padded with hexadecimal 0 on the right.

The result in the calculation length is handled as follows:

- If used in the statement [`COMPUTE`](abenequals_bit_expr.md), the final result of the entire expression is converted to the length of the data object `result` based on the rules for source field type `x` and `xstring`. In assignments to an inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md) the result of type `xstring` is in the calculation length.

- If used in [relational expressions](../../abap-glossary/abenrelational_expression_glosry.md), the result is used as an operand in the length resulting from the calculation.

- If used as an argument of [built-in functions](../../abap-glossary/abenbuiltin_function_glosry.md) or [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md), the result is used as an operand in the length resulting from the calculation.

- If used as an [actual parameter](../abap-declarations/abentyping_arith_expr.md) for [input parameters](../../abap-glossary/abeninput_parameter_glosry.md) of [methods](../../abap-glossary/abenmethod_glosry.md), the final result of the entire expression is converted to the length of the formal parameter based on the rules for source field type `x` and `xstring`. If the formal parameter is typed generically, it is set to the type `x` in the length determined by the operands.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following bit expression is hexadecimal `11111010` with a length of 4 bytes.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA hex1 TYPE xstring VALUE '10101010'. 
DATA hex2 TYPE xstring VALUE '0101'. 
out->write( 
  |{ hex1 BIT-OR hex2 }\n{ 
     xstrlen( CONV xstring( hex1 BIT-OR hex2 ) ) }| ). 
 
out->display( ).
```
