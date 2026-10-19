---
title: "itab - Table Reduction, String Processing"
source_file: abenreduce_text_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations > itab - Examples of Table Reductions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Table Reduction, String Processing

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a reduction of the columns of a character-like table to a text string.

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
CLASS cl_demo_reduce_text DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_reduce_text IMPLEMENTATION. 
  METHOD main. 
    TYPES strings TYPE STANDARD TABLE OF string WITH EMPTY KEY. 
    FINAL(words) = VALUE strings( 
      ( `All` ) 
      ( `ABAP` ) 
      ( `constructs` ) 
      ( `are` ) 
      ( `imperative` ) ). 
    out->write( words ). 
 
    "Table comprehension into helper table 
    FINAL(switched_words) = VALUE strings( 
          FOR word IN words 
           ( SWITCH #( word WHEN `All`        THEN `Some` 
                            WHEN `imperative` THEN `functional` 
                            ELSE word ) ) ). 
    out->write_data( switched_words ). 
 
    "Table reduction of helper table 
    FINAL(sentence) = 
      REDUCE string( INIT text = `` sep = `` 
        FOR word IN switched_words 
        NEXT text = |{ text }{ sep }{ word }| sep = ` ` ) && '.'. 
    out->write_data( sentence ). 
 
    "Obfuscation - all in one 
    ASSERT sentence = 
      REDUCE string( INIT text = `` sep = `` 
        "Table reduction 
        FOR word IN VALUE strings( 
          "Table comprehension 
          FOR word IN words 
           ( SWITCH #( word WHEN `All`        THEN `Some` 
                            WHEN `imperative` THEN `functional` 
                            ELSE word ) ) ) 
        NEXT text = |{ text }{ sep }{ word }| sep = ` ` ) && '.'. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

A [table comprehension](../../abap-glossary/abentable_comprehension_glosry.md) is used to construct a new internal table `switched_words` from the content of an internal table `words`, where the condition operator [`SWITCH`](../abap-program-flow-logic/abenconditional_expression_switch.md) replaces certain lines of the existing internal table with other lines. This table is specified in the [`FOR` expression](abenfor_in_itab.md) of the [`REDUCE`](../abap-program-flow-logic/abenconstructor_expression_reduce.md) expression and its lines are reduced to a text string using a concatenation after `NEXT` and then assigned to the variable `sentence`. Here, the helper variable `sep` declared after `INIT` is initial for the first read line and is filled with a blank for the evaluation of further lines.

This example also demonstrates an alternative implementation in which the table comprehension is embedded directly in the table reduction. Here, the helper variable `switched_words` is not required, but the source code is much harder to read. A human reader, for example, can hardly tell that the `FOR` expressions are not sequential and that the table comprehension is executed first, followed by the table reduction for the result.
