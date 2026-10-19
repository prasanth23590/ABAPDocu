---
title: "string_tmpl - literal_text"
source_file: abenstring_templates_literals.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > String Expressions (string_exp) > string_exp - String Templates (string_tmpl)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# string_tmpl - literal_text

## Syntax

``` abap
c...c  
```

## Description

Within a string template `|...|`, a literal text `c...c` represents the exact character string it displays. Literal text consists of all characters in `c` that

- are not enclosed in curly brackets `{ }`

- are not [control characters](../../abap-glossary/abencontrol_character_glosry.md)

- are not the special characters `|`, `{`, `}`, or `\`.

In particular, blanks in string templates are always significant. To display a special character `|`, `{`, `}`, or `\` as a literal character, it can be prefixed with the escape character `\`.

## Hint

A standalone string template that contains nothing but literal text is not handled like a literal but evaluated as an expression during runtime, even if it is not part of an expression. For such operands, a [text string literal](../../abap-glossary/abentext_string_literal_glosry.md) with backquotes should be used instead, for performance reasons.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following string template creates the character string shown below it.

``` abap
FINAL(txt) = 
  |Characters \|, \{, and \} have to be escaped by \\ in literal text.|.
```

Characters \|, {, and } have to be escaped by \\ in literal text.
