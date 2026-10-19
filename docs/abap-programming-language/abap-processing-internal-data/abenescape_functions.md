---
title: "cstring_func - escape"
source_file: abenescape_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Processing Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - escape

## Syntax

``` abap
... escape( val = text format = format ) ...  
```

[`val = text`](abenstring_functions_val.md)

## Description

This [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) returns the content of the character string in [`text`](abenstring_functions_val.md), and escapes certain special characters with escape characters according to a rule specified in `format`.

The possible values of `format` are defined as constants with the prefix *E\_* in the class `CL_ABAP_FORMAT`. Each value defines which special characters are replaced, and how. There are rules for special characters in markup languages (XML and HTML), in URIs and URLs, in JSON, as well as in regular expressions and string templates. It is also important to prevent attacks using Cross Site Scripting (XSS) on Web applications.

`format` expects data objects of the type `i`. An invalid value for `format` raises an exception of the class `CX_SY_STRG_PAR_VAL`.

This function can be specified in [general](../../abap-glossary/abengeneral_expr_position_glosry.md) and [character-like expression positions](../../abap-glossary/abencharlike_expr_position_glosry.md). The return value has the type `string`.

- [Rules for Markup Languages (Including JavaScript)](abenescape_functions.md#rules-for-markup-languages-including-javascript)

- [Rules for URLs and URIs](abenescape_functions.md#rules-for-urls-and-uris)

- [Rules for JSON](abenescape_functions.md#rules-for-json)

- [Rules for Regular Expressions](abenescape_functions.md#rules-for-regular-expressions)

- [Rules for String Templates](abenescape_functions.md#rules-for-string-templates)

- [Rules for Cross Site Scripting](abenescape_functions.md#rules-for-cross-site-scripting)

## Rules for Markup Languages (Including JavaScript)

Formats with *\_JS* in their name are intended for content with JavaScript components. The following table summarizes the replacement rules:

| **Format**       | **&** | **\<** | **\>** | **"** | **'**   | **TAB** | **LF**  | **CR**  | **BS** | **FF** | **\\** | **ctrl-char** |
|------------------|-------|--------|--------|-------|---------|---------|---------|---------|--------|--------|--------|---------------|
| `E_XML_TEXT`     | *&*   | *\<*   | \-     | \-    | \-      | \-      | \-      | \-      | \-     | \-     | \-     | \-            |
| `E_XML_ATTR`     | *&*   | *\<*   | \-     | *"*   | *'*     | *&#9;*  | *&#xA;* | *&#xD;* | \-     | \-     | \-     | \-            |
| `E_XML_ATTR_DQ`  | *&*   | *\<*   | \-     | *"*   | \-      | *&#9;*  | *&#xA;* | *&#xD;* | \-     | \-     | \-     | \-            |
| `E_XML_ATTR_SQ`  | *&*   | *\<*   | \-     | \-    | *'*     | *&#9;*  | *&#xA;* | *&#xD;* | \-     | \-     | \-     | \-            |
| `E_HTML_TEXT`    | *&*   | *\<*   | *\>*   | \-    | \-      | \-      | \-      | \-      | \-     | \-     | \-     | \-            |
| `E_HTML_ATTR`    | *&*   | *\<*   | *\>*   | *"*   | *&#39;* | \-      | \-      | \-      | \-     | \-     | \-     | \-            |
| `E_HTML_ATTR_DQ` | *&*   | *\<*   | *\>*   | *"*   | \-      | \-      | \-      | \-      | \-     | \-     | \-     | \-            |
| `E_HTML_ATTR_SQ` | *&*   | *\<*   | *\>*   | \-    | *&#39;* | \-      | \-      | \-      | \-     | \-     | \-     | \-            |
| `E_HTML_JS`      | \-    | \-     | \-     | *"*   | *\\*    | *\t*    | *\n*    | *\r*    | *\b*   | *\f*   | *\\*   | *\xhh*        |
| `E_HTML_JS_HTML` | *&*   | *\<*   | *\>*   | *"*   | *&#39;* | *\t*    | *\n*    | *\r*    | *\b*   | *\f*   | *\\*   | *\xhh*        |

### Description

The first column contains the names of the formats from the class `CL_ABAP_FORMAT`. The remaining columns show the escape characters that replace the special characters in the first line. All other characters remain unchanged. *TAB*, *LF*, *CR*, *BS*, and *FF* are the [control characters](../../abap-glossary/abencontrol_character_glosry.md) for tabulator, Line Feed, Carriage Return, Backspace, and Form Feed, to which the codes *x09*, *x0A*, *x0D*, *x08*, and *x0C* are assigned in 7-Bit ASCII. *ctrl-char* stands for all [control characters](../../abap-glossary/abencontrol_character_glosry.md) with codes less than *x20* that are not covered by those characters listed explicitly. Some of these can be converted to *\xhh*, where *hh* is the hexadecimal value of the code. If there is no value in a field (-), the special character remains unchanged.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following escaping is *IF a \< b*.

``` abap
cl_demo_output=>display( 
  escape( val    = 'IF a < b.' 
          format = cl_abap_format=>e_xml_text ) ).
```

### Executable Example

[String Functions, `escape` for HTML](abenstring_function_escape_abexa.md)

## Rules for URLs and URIs

All characters with codes between *x00* and *7F* are converted to *%hh*, except for the characters listed in the following table, where *hh* is the hexadecimal value of the code. In *URI_1* format, quotation marks are not converted to *%hh*, but are doubled.

| **Format**   | **Unconverted Characters**                                                                                                                          |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `E_URL`      | *\[0-9\]*, *\[a-z\]*, *\[A-Z\]*, *!*, *\$*, *'*, *(*, *)*, *\**, *+*, *,*, *-*, *.*, *\_*, *&*, */*, *:*, *;*, *=*, *?*, *@*                        |
| `E_URL_FULL` | *\[0-9\]*, *\[a-z\]*, *\[A-Z\]*, *!*, *\$*, *'*, *(*, *)*, *\**, *+*, *,*, *-*, *.*, *\_*                                                           |
| `E_URI`      | *\[0-9\]*, *\[a-z\]*, *\[A-Z\]*, *!*, *\$*, *'*, *(*, *)*, *\**, *+*, *,*, *-*, *.*, *\_*, *&*, */*, *:*, *;*, *=*, *?*, *@*, *~*, *\#*, *\[*, *\]* |
| `E_URI_FULL` | *\[0-9\]*, *\[a-z\]*, *\[A-Z\]*, *-*, *.*, *\_*, *~*                                                                                                |
| `E_URI_1`    | *\[0-9\]*, *\[a-z\]*, *\[A-Z\]*, *!*, *\$*, *(*, *)*, *\**, *+*, *,*, *-*, *.*, *\_*, *;*, *=*, *@*, *~*, *\[*, *\]*                                |

### Description

All characters with codes from *x80* are converted to their [UTF-8](../../abap-glossary/abenutf8_glosry.md) representation. Depending on the character, one to four bytes are represented in the form *%hh*, where *hh* is the hexadecimal value of a byte.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following escaping is *Numbers%3A%201,%202*.

``` abap
cl_demo_output=>display( 
  escape( val    = 'Numbers: 1, 2' 
          format = cl_abap_format=>e_url_full ) ).
```

## Rules for JSON

### Description

The special characters *"* and *\\* are prefixed with the escape character *\\*. [Control characters](../../abap-glossary/abencontrol_character_glosry.md) with the codes *x08*, *x09*, *x0A*, *x0C*, and *x0D* are escaped using *\b*, *\t*, *\n*, *\f*, and *\r* respectively. All other characters with codes less than *x20* are converted to a four-character hexadecimal representation and prefixed by *\u*. None of the other characters are affected.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following escaping is *This is a backslash: "\\"*.

``` abap
cl_demo_output=>display( 
  escape( val    = 'This is a backslash: "\"' 
          format = cl_abap_format=>e_json_string ) ).
```

## Rules for Regular Expressions

### Description

There are different formats for the different flavors of [regular expression syntax](abenregex_syntax.md) supported by ABAP. The special characters of regular expressions are prefixed by the associated escape character *\\*. [Control characters](../../abap-glossary/abencontrol_character_glosry.md) with codes such as *x08*, *x09*, *x0A*, *x0B*, *x0C*, and *x0D* are replaced by the special characters as *\b*, *\t*, *\n*, *\v*, *\f*, and *\r* respectively.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following escaping is *"\\" matches one, "\\" matches many"*.

``` abap
cl_demo_output=>display( 
  escape( val    = '"." matches one, "*" matches many"' 
          format = cl_abap_format=>e_pcre ) ).
```

## Rules for String Templates

### Description

The special characters of [string templates](abenstring_templates.md) (*\|*, *\\*, *{*, *}*) are prefixed by the associated escape character *\\*. [Control characters](../../abap-glossary/abencontrol_character_glosry.md) with the codes *x09*, *x0A*, and *x0D* are replaced by *\t*, *\n*, and *\r* respectively.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following escaping is *Special characters: \\, \\, \\, \\*.

``` abap
cl_demo_output=>display( 
  escape( val    = 'Special characters: |, \, {, }' 
          format = cl_abap_format=>e_string_tpl ) ).
```

## Rules for Cross Site Scripting

### Description

The escaping prevents attacks using Cross Site Scripting ([XSS](../../abap-glossary/abenxss_glosry.md)) on Web applications. There are rules for XML/HTML content, JavaScript content, Cascading Style Sheets (CSS), and URL content.

The rules for XSS include all the rules for individual formats and go beyond these. They are particularly distinct from the rules for markup languages, including JavaScript (see above). These extended rules should be used to protect ABAP programs from Cross Site Scripting, when content is constructed from unsafe sources. The transformations listed above are replaced or enhanced as follows:

- **Markup languages**: Format `E_XSS_ML`. All characters except *\[0-9\]*, *\[a-z\]*, *\[A-Z\]*, *,*, *-*, *.*, *\_*, and [control characters](../../abap-glossary/abencontrol_character_glosry.md) are transformed to *&#xhh;* or *&#xhhhh;*, where *hh* or *hhhh* is the hexadecimal value of the code. All [control characters](../../abap-glossary/abencontrol_character_glosry.md) are transformed to *&#xfffd;*.

- **JavaScript**: Format `E_XSS_JS`. All characters except *\[0-9\]*, *\[a-z\]*, *\[A-Z\]*, *,*, *.*, and *\_* are transformed to *\xhh* or *\uhhhh*, where *hh* or *hhhh* is the hexadecimal value of the code.

- **URLs and URIs**: Format `E_XSS_URL`. All characters except *\[0-9\]*, *\[a-z\]*, *\[A-Z\]*, *\**, *-*, *.*, and *\_* are transformed to *%hh*, where *hh* is the hexadecimal value of the code. All characters with codes from x80 are converted to their [UTF-8](../../abap-glossary/abenutf8_glosry.md) representation. Depending on the character, one to four bytes are represented in the form *%hh*, where *hh* is the hexadecimal value of a byte.

- **CSS**: Format `E_XSS_CSS`. All characters except *\[0-9\]*, *\[a-z\]*, and *\[A-Z\]* are transformed to *\hh* or *\hhhh*, where *hh* or *hhhh* is the hexadecimal value of the code. A blank is inserted after *hh* or *hhhh* if the following character is a valid hexadecimal digit.

If the format from the class `CL_ABAP_FORMAT` has the additional ending *\_NU*, all characters with codes greater than *xFF* are converted to a four-character hexadecimal representation, which is identified differently depending on the type of the content. The additional ending *"\_7B"* means 7 bit and also affects characters with codes greater than *xFF*.

### Hints

- The class `CL_ABAP_DYN_PRG` contains methods `ESCAPE_XSS_...` that wrap calls of the built-in function `escape` with the formats `E_XSS_...`. It is generally advisable to use the built-in function directly.

- `escape` used with rules for XSS is recommended as protection against cross site scripting, but might not be sufficient in some cases. For example, it may be best to use an include list to check an unsafe URL, so that phishing attacks can be detected in addition to XSS. To completely prevent code injections, JavaScript should never be created dynamically from unsafe sources.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following escaping is *German&#x20;umlauts&#x3a;&#x20;&#x22;&#xe4;&#xf6;&#xfc;&#x22;*.

``` abap
cl_demo_output=>display( 
  escape( val    = 'German umlauts: "&#x00E4;&#x00F6;&#x00FC;"' 
          format = cl_abap_format=>e_xss_ml ) ).
```

### Executable Example

String Functions, `escape` for XSS

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_CONVERSION_CODEPAGE_EX`

- *Cause:* A character cannot be converted in a conversion to UTF-8. This can only occur with characters from the [surrogate area](../../abap-glossary/abensurrogate_area_glosry.md). The position and code of the character is specified in the exception object.

  *Runtime error:* `CONVT_CHARACTER`

`CX_SY_STRG_PAR_VAL`

- *Cause:* Invalid value in `format`.

  *Runtime error:* `STRG_ILLEGAL_PAR`
