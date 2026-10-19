---
title: "cstring_func - cmax, cmin"
source_file: abencmax_cmin_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Processing Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - cmax, cmin

## Syntax

``` abap
... cmax|cmin( val1 = text1  val2 = text2 
              [val3 = text3] ... [val9 = text9] ) ...  
```

[`val1 = text1`](abenstring_functions_val.md) · [`val2 = text2`](abenstring_functions_val.md) · [`val3 = text3`](abenstring_functions_val.md) · [`val9 = text9`](abenstring_functions_val.md)

## Description

These [built-in functions](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) return the value of the biggest or the smallest of the character-like arguments [`text1`](abenstring_functions_val.md), [`text2`](abenstring_functions_val.md), ... passed. The content of the arguments is compared from left to right in the evaluation. The first different character from the left determines which operand is bigger or smaller based on the order in the [code page](../../abap-glossary/abencodepage_glosry.md) used.

At least two arguments, [`text1`](abenstring_functions_val.md) and [`text2`](abenstring_functions_val.md), and a maximum of nine arguments must be passed. Here, the optional input parameters `val3` through `val9` must be filled in ascending order without gaps.

The return value has the type `string`.

## Hints

- The extremum functions [`nmax`](abennmax_nmin_functions.md) and [`nmin`](abennmax_nmin_functions.md) can be used to determine numeric extreme values.

- Character-like extremum functions, like numeric extremum functions, can be traced back to the equivalent control structures using comparison operators. Remember that, unlike with the usual [ABAP comparison rules](../abap-program-flow-logic/abenlogexp_rules_operands.md), shorter arguments of fixed lengths are not padded to the length of longer arguments by padding them with blanks.

- As in comparisons with comparison operators, the current [locale](../../abap-glossary/abenlocale_glosry.md) is not significant when determining the extreme values.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates how to find the smallest and largest letters of a random set, which is represented here by the lines of an internal table. Of course, in this case the result can also be achieved by sorting the internal table, which is used here for verification.

``` abap
TYPES itab TYPE TABLE OF c WITH EMPTY KEY. 
 
FINAL(t) = cl_demo_date_time=>get_utc_time( ). 
FINAL(abcde) = 'abcdefghijklmnopqrstuvwxyz'. 
FINAL(rnd) = cl_abap_random_int=>create( 
  seed = CONV i( t ) min = 0 max = strlen( abcde ) - 1 ). 
 
DATA(itab) = VALUE itab( FOR i = 1 UNTIL i > 9 
                         LET off = rnd->get_next( ) IN 
                         ( abcde+off(1) ) ). 
 
FINAL(min) =  cmin( val1 = itab[ 1 ] 
                   val2 = itab[ 2 ] 
                   val3 = itab[ 3 ] 
                   val4 = itab[ 4 ] 
                   val5 = itab[ 5 ] 
                   val6 = itab[ 6 ] 
                   val7 = itab[ 7 ] 
                   val8 = itab[ 8 ] 
                   val9 = itab[ 9 ] ). 
 
FINAL(max) =  cmax( val1 = itab[ 1 ] 
                   val2 = itab[ 2 ] 
                   val3 = itab[ 3 ] 
                   val4 = itab[ 4 ] 
                   val5 = itab[ 5 ] 
                   val6 = itab[ 6 ] 
                   val7 = itab[ 7 ] 
                   val8 = itab[ 8 ] 
                   val9 = itab[ 9 ] ). 
 
SORT itab BY table_line. 
 
ASSERT min = itab[ 1 ]. 
ASSERT max = itab[ lines( itab ) ].
```

## Executable Example

[String functions `cmax`, `cmin`, and `segment`](abencmax_cmin_function_abexa.md).
