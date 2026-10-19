---
title: "string_tmpl - embedded_expressions"
source_file: abenstring_templates_expressions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > String Expressions (string_exp) > string_exp - String Templates (string_tmpl)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# string_tmpl - embedded_expressions

## Syntax

``` abap
{ embd_exp [format_options] }  
```

[`format_options`](abapcompute_string_format_options.md)

## Description

Within a string template, an opening and a closing curly bracket `{ ... }` define a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md), `embd_exp`, at which the following can be specified in ABAP syntax:

- [Data objects](../../abap-glossary/abendata_object_glosry.md)

- [Calculation expressions](../../abap-glossary/abencalculation_expression_glosry.md)

- [Constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md)

- [Table expressions](../../abap-glossary/abentable_expression_glosry.md)

- [Built-in functions](../../abap-glossary/abenbuiltin_function_glosry.md)

- [Functional methods](../../abap-glossary/abenfunctional_method_glosry.md) and [method chainings](../../abap-glossary/abenmethod_chaining_glosry.md)

At least one blank must be included on the right of the opening bracket and one the left of the closing bracket. An embedded expression must be complete within the current string template. An embedded expression within the curly brackets is handled in accordance with regular ABAP syntax:

- Tokens must be separated by at least one blank or line break.

- In other cases, blanks and line breaks between tokens are not significant.

- No distinction is made between uppercase and lowercase letters.

- [Comments](../../abap-glossary/abencomment_glosry.md) can be specified.

The data type of the expression must be an [elementary data type](../../abap-glossary/abenelementary_data_type_glosry.md) and the value of the expression must be character-like or be convertible to a character string. When a string template is evaluated, the value of each embedded expression is converted to a character string and inserted at the corresponding position. The string is formatted either using

- [Predefined formats](abenstring_templates_predef_format.md)

- Formatting options [`format_options`](abapcompute_string_format_options.md)

The embedded expressions in a string template are evaluated from left to right. If [functional methods](../../abap-glossary/abenfunctional_method_glosry.md) are specified, they are executed during the analysis.

## Hints

- To display the curly brackets `{` and `}` in the [literal text](abenstring_templates_literals.md) of a string template, they must be prefixed with the escape character `\`.

- Curly brackets cannot be nested directly. If `embd_expr` is itself a string expression, or contains a string expression, it can also contain embedded expressions.

- [Character string functions](../../abap-glossary/abencstring_function_glosry.md) with character-like return values are particularly suited when embedded functions are specified.

- Unlike [arithmetic expressions](abapcompute_arith.md) and [bit expressions](abapcompute_bit.md), embedded functional methods are not executed before the entire expression is evaluated. If an embedded functional method modifies the value of data objects that are also used as embedded operands, the change only affects data objects on the right of the method.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The string template in the method `main` uses embedded expressions to represent the text *Hello world!*. The first embedded expression is the attribute `attr` of the class. The return value of the method `func` is used in the second embedded expression. The third embedded expression is again the attribute `attr`, whose value has been changed in the method `func` in the meantime. The second embedded expression includes a line break and a comment is specified.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS: main, 
      func RETURNING VALUE(p) TYPE string. 
  PRIVATE SECTION. 
    CLASS-DATA attr TYPE string VALUE `Hello`. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD main. 
    DATA txt TYPE string. 
    txt = |{ attr }{ func( ) "a function call 
                     WIDTH = 6 ALIGN = RIGHT }{ attr }|. 
    cl_demo_output=>display( txt ). 
  ENDMETHOD. 
  METHOD func. 
    p = `world`. 
    attr = '!'. 
  ENDMETHOD. 
ENDCLASS.
```
