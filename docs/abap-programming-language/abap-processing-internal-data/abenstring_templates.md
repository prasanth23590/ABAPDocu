---
title: "string_exp - String Templates (string_tmpl)"
source_file: abenstring_templates.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > String Expressions (string_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# string_exp - String Templates (string_tmpl)

## Syntax

``` abap
|[literal_text][embedded_expressions][control_characters]|  
```

[`literal_text`](abenstring_templates_literals.md) · [`embedded_expressions`](abenstring_templates_expressions.md) · [`control_characters`](abenstring_templates_separators.md)

## Description

A string template is enclosed by two characters `|` and creates a character string that is used by the string expression at the operand position of the string template. The characters in this character string are determined by any sequence of the following syntax elements of the string template:

- Literal text [`literal_text`](abenstring_templates_literals.md)

- Embedded expressions [`embedded_expressions`](abenstring_templates_expressions.md)

- Control characters [`control_characters`](abenstring_templates_separators.md)

A string template that starts with `|` must be closed with `|` within the same line of source code. The only exceptions to this rule are line breaks in [embedded expressions](abenstring_templates_expressions.md). However, a string template is not subject to any length restrictions. The [literal operator](../../abap-glossary/abenliteral_operator_glosry.md) `&` or the [concatenation operator](../../abap-glossary/abenconcatenation_operator_glosry.md) `&&` can be used to combine multiple string templates into a single string template. A string template can be defined across multiple lines of source code and be given [comments](../../abap-glossary/abencomment_glosry.md).

## Hints

- To display the delimiters `|` within [literal text](abenstring_templates_literals.md) of a string template, it must be prefixed with the escape symbol `\`.

- Using the string function [`escape`](abenescape_functions.md), all special characters for string templates can be prefixed with their escape character.

- When string templates are combined, the literal operator [`&`](../abap-declarations/abenliteral_operator.md) behaves differently than with literals. This operator is executed at runtime in the same way as the concatenation operator [`&&`](abenstring_operators.md) and not just once during compilation. This means, however, that the restriction of 255 characters for literals no longer applies. The two combinations

  `|...| & |...|` `|...| && |...|` are identical for string templates. For purely literal content, they are the same as `` `...` && `...` `` However, they are different to `` `...` & `...` `` `'...' & '...'` `'...' && '...'` In the first two cases, a length restriction of 255 characters applies. In the third case, trailing blanks are ignored.

- If on the right side of an [assignment](abenequals_string_expr.md), strings are appended to a variable specified with the type `string` on the left side of the assignment, the variable is used directly in [specific cases](abenstring_expr_perfo.md) without producing an interim result. It should be ensured that this optimization is not undone, especially in loops.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

String template with literal text and an embedded expression. The result is made up of the content of the literal text and the result of the embedded expression.

``` abap
FINAL(result) = |Hello { sy-uname }!|.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following section of source code shows three identical string templates, all of which represent the character string *Hello World!*. The first string template contains the entire character string as literal text. The next two string expressions distribute the literal text across multiple parts of the string template and these are combined into the same character string using the literal operator `&` as in the first string template.

``` abap
FINAL(result1) = |Hello World!|. 
 
FINAL(result2) = |Hello| & | | & |World| & |!|. 
 
FINAL(result3) = |Hello| & "sub template 1 
                | |     & 
                |World| & "sub template 3 
* sub template 4: 
                |!|.
```
