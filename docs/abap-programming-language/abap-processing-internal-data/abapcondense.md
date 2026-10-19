---
title: "CONDENSE"
source_file: abapcondense.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CONDENSE

## Syntax

``` abap
CONDENSE text [NO-GAPS].  
```

## Description

The `CONDENSE` statement removes any leading and trailing blanks from the variable `text` and handles blanks within the remaining character string as follows:

- Without the optional `NO-GAPS` addition, all substrings of the remaining character string that contain nothing but blanks are replaced by exactly one blank.

- With the optional `NO-GAPS` addition, all substrings of the remaining character string that contain nothing but blanks are removed completely.

The data object `text` must be character-like. If the data object has a fixed length, the space created by condensing is padded with blanks on the right. If the data object is of the type `string`, its length is adapted to the result of the condensing.

## Hint

A character string can also be condensed in an operand position using a [condense function](abencondense_functions.md) that includes the functionality of the statement `CONDENSE`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The [flat structure](../../abap-glossary/abenflat_structure_glosry.md) `sentence` contains only character-like components and can therefore be assigned to the string `text`. After the condensing using the statement `CONDENSE`, `text` contains *She feeds you tea and oranges*. Before condensing, the words in `text` are 30 places apart from one another.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: BEGIN OF sentence, 
        word1 TYPE c LENGTH 30 VALUE 'She', 
        word2 TYPE c LENGTH 30 VALUE 'feeds', 
        word3 TYPE c LENGTH 30 VALUE 'you', 
        word4 TYPE c LENGTH 30 VALUE 'tea', 
        word5 TYPE c LENGTH 30 VALUE 'and', 
        word6 TYPE c LENGTH 30 VALUE 'oranges', 
      END OF sentence, 
      text TYPE string. 
 
text = sentence. 
out->write( text ). 
 
CONDENSE text. 
out->write( text ). 
 
out->display( ).
```
