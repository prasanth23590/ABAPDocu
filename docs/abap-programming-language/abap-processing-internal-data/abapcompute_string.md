---
title: "String Expressions (string_exp)"
source_file: abapcompute_string.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# String Expressions (string_exp)

## Syntax

``` abap
... { |string_tmpl| } 
  | { operand1 && operand2 [&&  operand3 ... ] } ...  
```

[`|string_tmpl|`](abenstring_templates.md) · [`&&`](abenstring_operators.md) · [`&&`](abenstring_operators.md)

## Description

A string expression formulates an operation (calculation) with character-like operands. The result of a string expression is a character string. A string expression consists of

- exactly one [string template](../../abap-glossary/abenstring_template_glosry.md) [`|string_tmpl|`](abenstring_templates.md) or

- two or more operands `operand1`, `operand2` ... that are concatenated as a character string using the [string operator](../../abap-glossary/abenstring_operator_glosry.md) [`&&`](abenstring_operators.md), where one of the operands can itself be a string template.

String expressions can occur in the read positions of [certain statements](../abap-syntax-elements-of-an-abap-program/abenexpression_positions.md) and, in particular, on the right side of an [assignment](abenequals_string_expr.md) with the [assignment operator `=`](abenequals_operator.md).

The operands of string expressions must be elementary and convertible to [character-like data types](../../abap-glossary/abencharlike_data_type_glosry.md). Structures with purely character-like flat components cannot, however, be specified.

If [constructor expressions](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) are specified as operands of string expressions, their data type is not determined by the string expression. The `#` character can be specified for the data type of the constructor expression only if the type can be determined from the constructor expression itself.

## Hints

- String expressions and [arithmetic expressions](../../abap-glossary/abenarithmetic_expression_glosry.md) cannot be mixed. Arithmetic expressions can, however, also be specified as [embedded expressions](abenstring_templates_expressions.md) of [string templates](abenstring_templates.md). Furthermore, in the [formatting options](abapcompute_string_format_options.md) of embedded expressions or [string functions](abenstring_functions.md) in operand positions, arithmetic expressions can be passed as arguments.

- The conversion operator [`CONV`](abenconstructor_expression_conv.md) can be applied to a structure with character-like-only components to use it as an operand of a string expression.

- Due to their special [conversion rules](abenconversion_enumerated.md), [enumerated objects](../../abap-glossary/abenenumerated_object_glosry.md) can be used as operands of string expressions regardless of their base type, which can produce unwanted results. This is why an extended program check message can be produced in this case. A special rule for the conversion operator [`CONV`](abenconv_constructor_enum.md) can be implemented to use the name of the enumerated object instead of the actual enumerated value.

- If, on the right side of an [assignment](abenequals_string_expr.md), strings are appended to a variable specified with the type `string` on the left side of the assignment, the variable is used directly in [specific cases](abenstring_expr_perfo.md) without producing an interim result. It should be ensured that this optimization is not undone, especially in loops.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Output of a string expression. The expression concatenates a text string literal with a string template that contains an embedded expression.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
out->write( 
 
   `Hello ` && |{ sy-uname }!| 
 
   ). 
 
out->display( ).
```
