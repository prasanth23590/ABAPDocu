---
title: "string_exp - &&"
source_file: abenstring_operators.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > String Expressions (string_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# string_exp - &&

## Syntax

``` abap
... operand1 && operand2 ...  
```

## Description

The [concatenation operator](../../abap-glossary/abenconcatenation_operator_glosry.md) `&&` concatenates two operands in a string expression into one character string.

The operand positions `operand` are enhanced [character-like expression positions](../abap-syntax-elements-of-an-abap-program/abenstring_expression_positions.md), which means that [character-like data objects](../../abap-glossary/abencharlike_data_object_glosry.md), [string expressions](../../abap-glossary/abenstring_expression_glosry.md), and [built-in functions](../../abap-glossary/abenbuiltin_function_glosry.md), or [functional methods](../../abap-glossary/abenfunctional_method_glosry.md) and [method chainings](../../abap-glossary/abenmethod_chaining_glosry.md) whose return value has a [character-like data type](../../abap-glossary/abencharlike_data_type_glosry.md), can be specified. Furthermore, apart from built-in functions, generic expressions with non-character-like data types can also be specified, which can be converted to the type `string`. The operand `operand` must be elementary. Structures with character-like-only flat components cannot be specified.

In the case of character-like operands with a fixed length, trailing blanks are ignored. An operand that does not have a character-like data type is regarded implicitly as an [embedded expression](../../abap-glossary/abenembedded_expression_glosry.md) of a [string template](../../abap-glossary/abenstring_template_glosry.md) and formatted as a text string before the concatenation in accordance with the associated [predefined format](abenstring_templates_predef_format.md).

## Hints

- In particular, [string templates](abenstring_templates.md) can be specified as operands.

- [Character string functions](../../abap-glossary/abencstring_function_glosry.md) with character-like return values are particularly suitable when specifying built-in functions as operands.

- The concatenation operator `&&` must not be confused with the [literal operator `&`](../abap-declarations/abenliteral_operator.md), which combines two [character literals](../../abap-glossary/abencharacter_literal_glosry.md) to one literal. The literal operator is generally used if a literal is to be defined across multiple program lines. The operator is executed only once when the program is compiled, and trailing blanks of character literals are always respected. A string expression with a concatenation operator, on the other hand, is recalculated each time, like all expressions, and can be used to concatenate any number of character-like operands.

- If on the right side of an [assignment](abenequals_string_expr.md), strings are appended using `&&` to a variable specified with the type `string` on the left side of the assignment, the variable is used directly in [some cases](abenstring_expr_perfo.md) without producing an interim result. It should be ensured that this optimization is preserved, especially in loops.

- It should be noted that the handling of non-character-like operands as [embedded expressions](../../abap-glossary/abenembedded_expression_glosry.md) can have different results than simple [conversions](abenconversion_elementary.md).

- A calculation assignment with the operator [`&&=`](abencalculation_assignment_string.md) can be used as a short form for assignments of concatenations.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Concatenation of four operands into the character string *Hello world!*. The last operand is a [string template](../../abap-glossary/abenstring_template_glosry.md) that has only literal content.

``` abap
DATA text TYPE string VALUE `Hello`. 
 
text  = text && ` ` &&  'world' && |!|.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates that a non-character-like operand in a concatenation is handled like an [embedded expression](../../abap-glossary/abenembedded_expression_glosry.md) and is not converted in accordance with the [conversion rules](abenconversion_elementary.md). After handling as an embedded expression, the minus sign is placed to the left of the number. After the conversion, it is placed to the right of the number.

``` abap
ASSERT `` && -1 
     = `` && |{ -1 }|. 
 
ASSERT `` && -1 
    <> `` && CONV string( -1 ).
```
