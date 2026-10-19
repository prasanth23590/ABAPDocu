---
title: "rel_exp - Predicate Function matches"
source_file: abenpred_function_matches_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > rel_exp - Predicates > rel_exp - Predicate Functions > rel_exp - Predicate Functions for Character-Like Arguments"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Predicate Function matches

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the predicate function [`matches`](abenmatches_functions.md).

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
CLASS cl_demo_matches DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_matches IMPLEMENTATION. 
  METHOD main. 
    DATA email TYPE string VALUE `abc.def@ghi.jkl`. 
    cl_demo_input=>new( )->request( CHANGING field = email ). 
    IF matches( val   = email 
                regex = `\w+(\.\w+)*@(\w+\.)+(([a-z]|[A-Z]){2,4})` ) 
                ##REGEX_POSIX. 
      out->write( 'Format OK' ). 
    ELSEIF matches( 
             val  = email 
             pcre = `[[:alnum:],!#\$%&'\*\+/=\?\^_``\{\|}~-]+`      & 
                    `(\.[[:alnum:],!#\$%&'\*\+/=\?\^_``\{\|}~-]+)*` & 
                    `@[[:alnum:]-]+(\.[[:alnum:]-]+)*`              & 
                    `\.([[:alpha:]]{2,})` ). 
      out->write( 'Syntax OK but unusual' ). 
    ELSE. 
      out->write( 'Wrong format!' ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The class checks the formal correctness of an entered e-mail address by comparing it with regular expressions.

The first regular expression checks for standard e-mail addresses without special characters, whereas the second regular expression performs a more lenient syntax check in accordance with RFC 822.

Even the second check, which uses a relatively simple regular expression for the example, is not always compatible with all e-mail addresses that would be possible in accordance with RFC 822.

The class `CL_DEMO_VALIDATE_RFC_822_ADDR` uses a regular expression taken from the Internet, which is designed to recognize all e-mail addresses allowed by RFC 822. The regular expression here was written originally for Perl and has more than 6000 characters. The class is therefore an example of how not to use regular expressions in ABAP.
