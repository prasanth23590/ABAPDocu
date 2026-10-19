---
title: "Character Literals"
source_file: abenuntyped_character_literals.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects > Literals"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Character Literals

## Syntax

``` abap
... 'c[c[c[...]]]' | `[c[c[c[...]]]]` ...  
```

## Description

Character literals can be either text field literals or text string literals.

- A text field literal is a string of characters `c` enclosed in single quotes (`'`).

- A text string literal is a string of characters `c` enclosed in single backquotes (\`\`\`).

The following table lists the properties of these literals:

| **Syntax**  | **Name**                                                   | **Properties**                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `'...'`     | [Text field literal](../../abap-glossary/abentext_field_literal_glosry.md)   | String of characters. The data type is `c` with the length of the enclosed characters, including trailing blanks. A text field literal is between 1 and 255 characters long. There is no empty text field literal: The text field literal `''` has the same meaning as the text field literal `' '` with length 1, containing one blank. To represent a quotation mark in a text field literal, two consecutive quotation marks `''` must be specified. |
| `` `...` `` | [Text string literal](../../abap-glossary/abentext_string_literal_glosry.md) | String of characters. The data type is `string`. A text string literal can have a maximum of 255 characters. The empty text string literal \`\` represents an empty string with length 0. To represent a backquote in a text string literal, two consecutive backquotes \`\`\`\` must be specified.                                                                                                                                                     |

Character literals that span multiple lines are not allowed. The [literal operator](abenliteral_operator.md) `&` can, however, be used to combine multiple literals with the same type into a literal of this type.

If a text field literal is specified at an operand position at which a [text symbol](../../abap-glossary/abentext_symbol_glosry.md) is possible, the three-digit identifier `idf` of a text symbol can be appended in round brackets.

`... 'Literal'(idf) ...`

If the text symbol exists in the currently loaded [text pool](../../abap-glossary/abentext_pool_glosry.md), then the content of the text symbol is used instead of the literal, otherwise the literal is used. Text string literals cannot be combined with text symbols.

## Hints

- Only text field literals, not text string literals, can be used if a literal is to be combined with a text symbol.

- Trailing blanks in text field literals use memory, but are [generally](../abap-processing-internal-data/abenstring_processing_trail_blanks.md) ignored in operand positions, like all data objects of the type `c`. In text string literals they are always relevant, as is the case for all data objects of type `string`.

- Quotation marks can be represented directly in text string literals and backquotes in text field literals.

- [String templates](../../abap-glossary/abenstring_template_glosry.md), which only contain literal text, behave like text string literals, but are not evaluated until runtime. For standalone operands that are not part of an expression, only real text string literals with backquotes should be used for performance reasons.

- The characters that can be contained in character literals are restricted to those that can be used in ABAP source code.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Representation of quotation marks and backquotes in character literals. The first two and the last two literals have the same result.

``` abap
cl_demo_output=>write_text( 'This is John''s bike' ). 
cl_demo_output=>write_text( `This is John's bike` ). 
cl_demo_output=>write_text( 'This is a backquote: `' ). 
cl_demo_output=>write_text( `This is a backquote: ``` ). 
cl_demo_output=>display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

If quotation marks and backquotes are required within a string, [string templates](../../abap-glossary/abenstring_template_glosry.md) are also suitable, whose special characters are uniformly escaped with `\`.

``` abap
cl_demo_output=>display( |Quote: ', Backquote: `, Bar: \| | ).
```
