---
title: "cstring_func - count, find, and match"
source_file: abenstring_function_find_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - count, find, and match

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the string functions [`count`](abencount_functions.md), [`find`](abensearch_functions.md), and [`match`](abenmatch_functions.md).

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
CLASS cl_demo_find_and_match DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_find_and_match IMPLEMENTATION. 
  METHOD main. 
    DATA: text TYPE c LENGTH 120 
               VALUE `Cathy's cat with the hat sat on Matt's mat.`, 
          regx TYPE c LENGTH 120 
               VALUE `\b.at\b`. 
    DATA: result TYPE i, 
          substr TYPE string. 
    DATA o TYPE c LENGTH 120. 
    cl_demo_input=>new( 
     )->add_field( CHANGING field = text 
     )->request(   CHANGING field = regx ). 
    out->write( text ). 
    TRY. 
        result = count( val  = text 
                        pcre = regx ). 
        IF result = 0. 
          out->write( 'Nothing found' ). 
          RETURN. 
        ENDIF. 
        DO result TIMES. 
          result = find( val  = text 
                         pcre = regx 
                         occ   = sy-index ). 
          substr = match( val  = text 
                          pcre = regx 
                          occ  = sy-index ). 
          DATA(len) = strlen( substr ). 
          IF len <> 0. 
            o+result(len) = substr. 
          ELSE. 
            o+result(1) = '&#x00B0;' ##STRING_OK. 
          ENDIF. 
        ENDDO. 
      CATCH cx_sy_invalid_regex INTO FINAL(exc). 
        out->write( exc->get_text( ) ). 
        RETURN. 
    ENDTRY. 
    out->write( o ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In the text field `text`, all occurrences are found using `count` and `find` that match a regular expression. When a search is successful, the substring found is read and displayed using the function `match`.

Instead of using the function `count`, it is also possible to use an unlimited `DO` loop that is exited using `EXIT` if the result of `find` has the value -1.
