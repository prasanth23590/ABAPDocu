---
title: "Text Symbols"
source_file: abentext_symbols.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Text Symbols

A text symbol is a [named data object](../../abap-glossary/abennamed_data_object_glosry.md) of an [ABAP program](../../abap-glossary/abenabap_program_glosry.md) that is not declared in the program itself but is maintained as a part of the [text elements](../../abap-glossary/abentext_element_glosry.md) of the program. A text symbol has the [data type](../../abap-glossary/abendata_type_glosry.md) [`c`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) and the length defined in the text elements by `mlen`.

A text symbol behaves like a [constant](../../abap-glossary/abenconstant_glosry.md) and can be specified in [read positions](../../abap-glossary/abenread_position_glosry.md) using its names as follows:

`... text-idf ...`

Here, `idf` is the three-character ID of the text symbol, which can be composed of all alphanumeric characters including *\_*. The text symbol is then taken from the currently loaded [text pool](../../abap-glossary/abentext_pool_glosry.md).

If the text symbol does not exist in the currently loaded [text pool](../../abap-glossary/abentext_pool_glosry.md), `text-idf` is handled like an initial single-character [text field](../../abap-glossary/abentext_field_glosry.md).

A text symbol can be linked to [text field literals](../../abap-glossary/abentext_field_literal_glosry.md) using the following syntax:

`... 'Literal'(idf) ...`

If the text symbol exists in the currently loaded text pool, it replaces the literal. If the text symbol does not exist, the literal is used.

## Hints

- Like all text elements, text symbols are linked to the translation environment. They can be used in all locations where translated texts are to be displayed by the program.

- The maximum length of a text symbol should be chosen so that there is enough space available for the translation. For example, the German translation of the six-character English word *window* requires seven characters (*Fenster*).

- The identifier `text-idf` is reserved for text symbols. A structure called `text` cannot have any components with three-character names. It is best never to call a structure `text`. This can cause syntax errors, particularly in structures that reference global data types.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Access to the text symbol `exa` of the current program. If available, its text is displayed. If not, the text field literal is used in the first case and a blank is used in the second case.

``` abap
cl_demo_output=>new( 
  )->write( 'Text in text symbol'(exa) 
  )->write( TEXT-exa 
  )->display(  ).
```
