---
title: "string_tmpl - control_characters"
source_file: abenstring_templates_separators.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > String Expressions (string_exp) > string_exp - String Templates (string_tmpl)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# string_tmpl - control_characters

## Syntax

``` abap
 ... \n ... \r ... \t ...  
```

## Description

String templates interpret the character combinations `\n`, `\r`, and `\t` as [control characters](../../abap-glossary/abencontrol_character_glosry.md).

| **Control Character** | **Meaning** | **Hexadecimal value (UTF-8)** |
|-----------------------|-------------|-------------------------------|
| `\n`                  | Line feed   | 0A                            |
| `\r`                  | Return      | 0D                            |
| `\t`                  | Tabulator   | 09                            |

In place of a control character, its hexadecimal value according to the current code page is inserted into the character string created by the string template.

## Hints

- If a control character is to be included as literal text, its special meaning can be removed by prefixing it with the escape character `\`.

- The control characters in string templates replace the use of some attributes of the class [`CL_ABAP_CHAR_UTILITIES`](abencl_abap_char_utilities.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example generates in `code` the representation of the results of a string template with the three possible control characters in the code page UTF-8, namely `0A0D09`. The hexadecimal values `0A`, `0D`, and `09` stand for line feed, return, and tabulator.

``` abap
FINAL(code) = 
  cl_abap_conv_codepage=>create_out(  )->convert( |\n\r\t| ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example produces a three line output in the textedit control.

``` abap
cl_demo_text=>display_string( |1\n2\n3| ).
```

## Executable Example

[String Templates, Control Characters](abenstring_template_ctrlchar_abexa.md)
