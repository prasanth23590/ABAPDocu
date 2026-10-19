---
title: "regex - XPath Regular Expression"
source_file: abenxpath_regex_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Regular Expressions (regex) > regex - Syntax > regex - XPath Syntax"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# regex - XPath Regular Expression

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates an XPath regular expression.

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
CLASS cl_demo_xpath_regex DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_xpath_regex IMPLEMENTATION. 
  METHOD main. 
    FINAL(xml) = 
      `<xml><Hello type="cheerful" lang="EN"></Hello>` && 
      `<World text='world'><Ocean color="blue" /></World></xml>`. 
 
    FINAL(matcher) = cl_abap_regex=>create_xpath2( 
      pattern = 
        `<(\i\c*)((?:\s+\i\c*\s*=\s*(?:'[^']*'|"[^"]*"))*)\s*/?>` 
        )->create_matcher( text = xml ). 
 
    TYPES matches TYPE TABLE OF string WITH EMPTY KEY. 
    DATA o TYPE REF TO if_demo_output. 
    o = REDUCE #( 
            INIT o1 = out 
            FOR <match> IN matcher->find_all( ) 
            NEXT o1 = o1->write( 
      name = `Matches` 
      data = VALUE matches( 
        ( |Full Match: '{ 
        substring( val = xml 
                   off = <match>-offset 
                   len = <match>-length ) }'| ) 
        ( |Tag Name:   '{ 
        substring( val = xml 
                   off = <match>-submatches[ 1 ]-offset 
                   len = <match>-submatches[ 1 ]-length ) }'| ) 
        ( |Attributes: '{ condense( 
        substring( val = xml 
                   off = <match>-submatches[ 2 ]-offset 
                   len = <match>-submatches[ 2 ]-length ) ) }'| ) ) ) 
      ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example uses the special characters `\i` and `\c` in an XPath regular expression that match any character that can be the first character of an XML name or any character that can occur after the first character of an XML name. The regular expression extracts the name of tags and the attributes from an XML file.
