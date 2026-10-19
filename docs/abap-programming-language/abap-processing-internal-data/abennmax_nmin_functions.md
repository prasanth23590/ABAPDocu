---
title: "num_func - nmax, nmin"
source_file: abennmax_nmin_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Numeric Functions (num_func)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# num_func - nmax, nmin

## Syntax

``` abap
... nmax|nmin( val1 = arg1 val2 = arg2 [val3 = arg3] ... [val9 = arg9] ) ...  
```

## Description

These [built-in functions](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) return the value of the largest or smallest of the passed arguments. A minimum of two arguments, `arg1` and `arg2` must, and a maximum of nine arguments can be passed. Here, the optional input parameters `val3` to `val9` must be filled in ascending order without gaps. The arguments `arg1` to `arg9` are [numeric expression positions](../../abap-glossary/abennumerical_expr_position_glosry.md).

The following applies to the data type of the return value:

- Outside of an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md), a [calculation type](../../abap-glossary/abencalculation_type_glosry.md) is determined from all arguments and used to perform the comparison. The calculation type is determined just like an [arithmetic expression](abenarith_type.md) and also determines the data type of the return value.

- Within an arithmetic expression, the arguments of the function contribute to the [calculation type](../../abap-glossary/abencalculation_type_glosry.md) of the entire expression and the function is calculated using the calculation type. If an argument itself is an arithmetic expression, its operands contribute to the entire calculation type and the argument is also calculated using this type.

## Hints

- The extremum functions [`cmax`](abencmax_cmin_functions.md) and [`cmin`](abencmax_cmin_functions.md) can be used to determine character-like extreme values.

- When using two input parameters:

  `result = nmax|nmin( val1 = arg1 val2 = arg2 )`

the evaluation of the functions is equivalent to:

``` abap
IF num1 >= num2 | num1 <= num2. 
  result = num1. 
ELSE. 
  result = num2. 
ENDIF.
```

When using more than two input parameters, an equivalent control structure would be more complex.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Determination of the smaller of two UTC time stamps in packed numbers, whereby the initial value of the conditional operator [`COND`](../abap-program-flow-logic/abenconditional_expression_cond.md) is not regarded as the smallest value.

``` abap
CONSTANTS max_ts TYPE timestamp VALUE 999999999999999. 
 
DATA: ts1 TYPE timestamp, 
      ts2 TYPE timestamp. 
 
GET TIME STAMP FIELD ts1. 
 
FINAL(min_ts) = 
  nmin( val1 = COND timestamp( WHEN ts1 IS INITIAL 
                               THEN max_ts ELSE ts1 ) 
        val2 = COND timestamp( WHEN ts2 IS INITIAL 
                               THEN max_ts ELSE ts2 ) ) ##type.
```

## Executable Example

[Extremum Functions `nmax`, `nmin`](abennmax_nmin_function_abexa.md)
