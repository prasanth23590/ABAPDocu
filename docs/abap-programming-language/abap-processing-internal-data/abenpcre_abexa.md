---
title: "Find a PCRE Regular Expression"
source_file: abenpcre_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing > FIND"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Find a PCRE Regular Expression

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates how to search for a regular expression in PCRE syntax.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_find_pcre DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_find_pcre IMPLEMENTATION. 
  METHOD main. 
    DATA(regex) = `\b.at\b`. 
    DATA(text)  = `Cathy's cat with the hat sat on Matt's mat.`. 
    cl_demo_input=>new( 
      )->add_field( CHANGING field = text 
      )->add_field( CHANGING field = regex 
      )->request( ). 
 
    TRY. 
        FIND PCRE regex IN text. 
 
        IF sy-subrc = 0. 
          out->write_html( 
            `<html><body>` && 
            replace( 
              val = text 
              pcre = regex 
              with = `<font color="#FF0000"><b>$0</b></font>` ) && 
                    `</body></html>` ). 
        ELSE. 
          out->write( `Not found` ). 
        ENDIF. 
      CATCH cx_sy_invalid_regex INTO FINAL(exc). 
        out->write( exc->get_text( ) ). 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In the example, a line of text and a regular expression can be entered. The class searches the text line `text` for the first match of the search pattern defined in the regular expression `regex` and highlights this section in the result display. The search expects a PCRE regular expression and is case-sensitive. The statement [`FIND`](abapfind.md) is used to search the statement, while the statement [`REPLACE`](abapreplace.md) is used to mark the result. Here, the operator `$0` serves as a placeholder for the match in the replacement text.

The predefined example text is:

*Cathy's cat with the hat sat on Matt's mat.*

and the predefined regular expression is:

`(\b.at\b)`

The regular expression describes a word consisting of three characters, where the first is any single character and the other two are *at*.

The case-sensitive search for the first occurrence finds the word *cat*.
