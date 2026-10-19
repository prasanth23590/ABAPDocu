---
title: "Line Feeds in Character String Processing"
source_file: abenline_feed.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Character String and Byte String Processing, Overview"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Line Feeds in Character String Processing

A line feed (`LF`) is a [control character](../../abap-glossary/abencontrol_character_glosry.md) that positions the cursor when writing an output. Other of such control characters are return (`CR` from carriage return) or a tabulator. There are also combinations possible as `CRLF` for return plus line feed. If a character string contains control characters, it depends on the framework handling the character string how these are interpreted. While, for example, most notepad applications or text editors handle control characters as such, HTML or XML browsers handle control characters as whitespace characters.

- [Control Characters in ABAP](abenline_feed.md#control-characters-in-abap)

- [Using the Line Feed Character in ABAP](abenline_feed.md#using-the-line-feed-character-in-abap)

  - [Line Feed in Outputs](abenline_feed.md#line-feed-in-outputs)

  - [Replacing Line Feeds](abenline_feed.md#replacing-line-feeds)

## Control Characters in ABAP

In ABAP, some control characters, especially the line feed character, can easily obtained by using the respective [string template](abenstring_templates_separators.md):

- `|...\n...|` for a linefeed among other content

- `|\n|` for a single line feed character

There are also constants for control characters in `CL_ABAP_CHAR_UTILITIES` but those contain the same code as the respective string templates and there is no need to use them any more:

``` abap
ASSERT cl_abap_char_utilities=>newline        = |\n|. 
ASSERT cl_abap_char_utilities=>horizontal_tab = |\t|. 
ASSERT cl_abap_char_utilities=>cr_lf          = |\r\n|.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The actual code of a control character can be determined (as for all characters) as follows:

``` abap
FIELD-SYMBOLS <lf> TYPE x. 
DATA lf type c LENGTH 1. 
lf =  |\n|. 
 
ASSIGN lf to <lf> casting. 
cl_demo_output=>display( <lf> ).
```

In an Unicode system this gives *0A00* which is the Unicode code for a line feed.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In another way around, any control character of any code page can be included in a character string, here again the Unicode line feed:

``` abap
CONSTANTS lf TYPE x LENGTH 4 VALUE '0A00'. 
FIELD-SYMBOLS <lf> TYPE c. 
 
ASSIGN lf TO <lf> CASTING. 
cl_demo_output=>display( |aaa{ <lf> }bbb| ).
```

## Using the Line Feed Character in ABAP

The line feed character and other control characters are needed when sending character strings to frameworks that can handle them. Examples are different output media or writing to files.

### Line Feed in Outputs

The following are examples for line feeds in common output media.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The text control of the SAP GUI Control Framework handles control characters.

``` abap
cl_demo_text=>display_string( 
  |<html>| && 
  |  <body>| && 
  |    Hello!| && 
  |  </body>| && 
  |</html>| ). 
 
cl_demo_text=>display_string( 
  |<html>\n| && 
  |  <body>\n| && 
  |    Hello!\n| && 
  |  </body>\n| && 
  |</html>\n| ).
```

The first output is:

`<html> <body> Hello! </body></html>`

The second output is:

``` abap
<html> 
  <body> 
    Hello! 
  </body> 
</html>
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first output of `string` handles its content as text and the line feeds are respected. The second output of `string` browses its content as an HTML file and the line feeds are handled as whitespace characters.

``` abap
FINAL(string) = 
    |<html>\n| && 
    |  <body>\n| && 
    |    Hello!\n| && 
    |  </body>\n| && 
    |</html>\n|. 
 
cl_demo_output=>new( 
 )->write( string 
 )->write_html( string 
 )->display( ).
```

### Replacing Line Feeds

It is a common task to remove line feeds and other control characters from character strings that are received from outside of ABAP.

This can be easily done as follows:

`REPLACE ALL OCCURRENCES OF |\n| IN text_with_lf WITH ` `.`

Another pattern is

`SPLIT text AT |\r\n| INTO TABLE DATA(text_table).`

For doing so, it must be checked If the code pages match. If the code page of the AS ABAP does not match the code page of the control characters in the text, field symbols must be used as shown above to represent the control characters of the code page of the text.
