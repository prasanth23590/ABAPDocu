---
title: "table_exp - default"
source_file: abentable_exp_optional_default.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > itab - Table Expressions (table_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# table_exp - default

## Syntax

``` abap
... OPTIONAL|{DEFAULT def} ...  
```

## Description

Specifies a default value for table lines not found. If the [type of the result](abentable_exp_result.md) of a table expression [`table_exp`](abentable_expressions.md) is defined using the value operator `VALUE` or the reference operator `REF`, a default value can be specified after the table expression. If the line [`itab_line`](abentable_exp_itab_line.md) specified in the table expression is not found, an exception of the class `CX_SY_ITAB_LINE_NOT_FOUND` is not raised if a default value is specified and the result is determined by the default value instead.

- `OPTIONAL`

  - If `VALUE` is used, the default value is an initial data object with the data type of the table expression.

  - If `REF` is used, the default value is an initial reference variable with the static type of the table expression.

- `DEFAULT`

  - If `VALUE` is used, the default value is specified using a data object `def`, which must be convertible to the data type of the table expression, If `def` is not compatible with the data type of the result of the expression, a conversion is made to this data type in accordance with the [conversion rules](abenconversion_rules.md).

  - If `REF` is used, the default value is specified using a reference variable `def`, whose static type is the data type of the table expression.

`def` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md).

If the operand of `VALUE` or `REF` is a single table expression, the default value applies to a single line in the corresponding table. If the operand is a [chaining](abentable_exp_chaining.md) of table expressions, the default value applies to the result of the chaining, that is, to its right end, which can express a structure component or a table line. A default value specified explicitly must match the result of the chaining accordingly. When a default value is specified for a chaining, the first exception for a missing line across the entire chaining is caught and the default value is returned as a result.

## Hints

- In addition to the functions [`line_exists`](../abap-program-flow-logic/abenline_exists_function.md) and [`line_index`](abenline_index_function.md), a characteristic default value specified for missing lines also enables the existence of lines to be checked without catching an exception or checking the return value after the statement `ASSIGN`.

- A default value `def` specified after `DEFAULT` can itself be a table expression with default value. This enables alternative searches to be performed within an expression.

- There is no operator for the default behavior of a table expression in which the [result](abentable_exp_result.md) is usually a temporary field symbol, which means that no default value can be specified here.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

If no line of the specified key is found, the table expression returns a line in which the component `carrid` has the value *NUL* and all other components are initial.

``` abap
DATA spfli_tab TYPE SORTED TABLE OF spfli 
               WITH UNIQUE KEY carrid connid. 
 
SELECT * 
       FROM spfli 
       INTO TABLE @spfli_tab. 
 
cl_demo_output=>display( VALUE #( spfli_tab[ carrid = 'LH' 
                                             connid = '400' ] 
                                  DEFAULT VALUE #( carrid = 'NUL' ) ) ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the difference between specifying the default value for the value operator `VALUE` and the reference operator `REF`. Once this source code section is executed, `var1` is an initial structure with the type `SCARR` and `dref1` is an initial reference variable with the static type of this structure. The reference variable `dref1` does not point to an initial structure. In the case of the default value specified using `DEFAULT`, a reference variable must be specified for `REF`. This is done here using the instance operator `NEW`, not `VALUE`.

``` abap
DATA itab TYPE TABLE OF scarr WITH EMPTY KEY. 
 
FINAL(var1) = VALUE #( itab[ 1 ] OPTIONAL ). 
FINAL(var2) = VALUE #( itab[ 1 ] DEFAULT VALUE #( carrid   = 'XXX' 
                                                 carrname = 'xxx' ) ). 
 
FINAL(dref1) = REF #( itab[ 1 ] OPTIONAL ). 
FINAL(dref2) = REF #( itab[ 1 ] DEFAULT NEW #( carrid   = 'XXX' 
                                              carrname = 'xxx' ) ). 
 
ASSERT var1  IS INITIAL. 
ASSERT dref1 IS INITIAL. 
 
ASSERT var2 = dref2->*.
```

## Executable Example

[Table Expressions, Default Value](abentable_exp_default_abexa.md)
