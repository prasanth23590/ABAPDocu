---
title: "let_exp, LET ... IN"
source_file: abaplet.html
section: "ABAP Programming Language > ABAP - Declarations > Local Declarations in Constructor Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# let_exp, LET ... IN

## Syntax

``` abap
 ... LET {var1 = rhs1}|{<fs1> = wrexpr1} 
        {var2 = rhs2}|{<fs2> = wrexpr2} ... IN ...  
```

### Alternative

[1. `... var = rhs ...`](abaplet.md#alternative-1)

[2. `... <fs> = wrexp ...`](abaplet.md#alternative-2)

## Overview

### Description

A `LET` expression defines variables `var1`, `var2`, ... or field symbols `<fs1>`, `<fs2>`, ... as local helper fields in an expression and assigns values to them. The helper fields can be used from their declaration in the operand positions of the expression. There is no way of accessing a helper field statically outside of its expression. The documentation of each expression lists whether and in which lines it contains a `LET` expression. Any `LET` expressions in an expression or subexpression are evaluated first.

A helper field specified in a `LET` expression is valid in the context in which the `LET` expression is specified. This can be a full expression or just part of an expression. All helper fields of a full expression are in the same namespace. A previously specified helper field cannot be specified in a further `LET` expression of the same expression. Furthermore, the helper fields are in the same namespace as the data objects or field symbols of the current procedure or program. Helper fields cannot be defined in a `LET` expression if a data object or field symbol with the same name already exists in the procedure or program of the expression. Conversely, no data objects or field symbols with names assigned to helper fields can be declared after an expression with a `LET` expression.

When reusing helper fields in different expressions, the following applies:

- If a helper field is defined for the first time in the current procedure or program, it is declared as with an [inline declaration](abeninline_declarations.md) and the data type is derived accordingly.

- If a helper field in the current procedure or program is defined again in a `LET` expression of a different expression and the derived data type matches, the helper field is bound to this expression and can be used there.

- If a helper field in the current procedure or program is defined again in a `LET` expression of a different expression and the derived data type does not match, the helper field cannot be used there and a syntax error occurs.

### Hints

- `LET` expressions can currently only be used in [constructor expressions](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md). Subexpressions in which `LET` expressions can be used are [iteration expressions](../../abap-glossary/abeniteration_expression_glosry.md) using [`FOR`](../abap-program-flow-logic/abenfor.md) and results specified after `THEN` and `ELSE` in the [conditional expressions](../../abap-glossary/abenconditional_expression_glosry.md) [`COND`](../abap-program-flow-logic/abenconditional_expression_cond.md) and [`SWITCH`](../abap-program-flow-logic/abenconditional_expression_switch.md).

- In the assignment of a value operator `VALUE` to [structures](../abap-creating-objects-and-values/abenvalue_constructor_params_struc.md) or [internal tables](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md), values on the left side can be saved to helper fields using a `LET` expression before the left side is overwritten.

- A helper field defined in a `LET` expression can be addressed dynamically in the entire current context. This is not recommended, however, since expressions should be free of side effects.

- It is a good idea to use `LET` expressions whenever helper fields are required for performance (avoiding multiple calculations) or the readability of an expression or whenever values from the left side of an assignment in a `VALUE` operator are needed on the right side.

### Executable Example

[`LET` expression](abenlet_abexa.md).

## Alternative 1

`... var = rhs ...`

### Description

Definition of a local helper variable `var` as a helper field in a `LET` expression. The value of the right side `rhs` is assigned to the helper variable as an initial value.

For the right side `rhs` the same can be specified as in a regular assignment using the [assignment operator `=`](../abap-processing-internal-data/abenequals_operator.md). The data type of the helper variable is determined from the right side `rhs` as when an inline declaration [`DATA(var)`](abendata_inline.md) or [`FINAL(var)`](abenfinal_inline.md) is specified on the left side of an assignment operator using the [assignment operator `=`](../abap-processing-internal-data/abenequals_operator.md). It must be possible to determine the data type completely from the right side to avoid syntax errors.

### Hints

- The helper variables declared in a `LET` expression generally keep the value defined by `rhs` while the expression is calculated. It is possible to change the value of a helper variable in the expression, for example by binding to a `CHANGING` parameter of a method, but this would be unusual.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a helper variable `bias` in the context of a `VALUE` expression in front of `FOR` loop and of three local helper variables `x`, `y`, and `z` in the context of the `FOR` loop. construct the values of a structure. The values of the helper variables are used to construct the components of an internal table. While `bias` is constant in the `FOR` loop, `x`, `y`, and `z` are assigned new values within each loop pass.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF struc, 
    col1 TYPE i, 
    col2 TYPE i, 
  END OF struc, 
  itab TYPE SORTED TABLE OF struc WITH NON-UNIQUE KEY col1. 
 
FINAL(t) = cl_demo_date_time=>get_utc_time( ). 
FINAL(rnd) = cl_abap_random_int=>create( 
  seed = CONV i( t ) min = 1 max = 10 ). 
 
 
FINAL(itab) = VALUE itab( 
   LET bias = 100000 IN 
   FOR i = 1 UNTIL i > 5 
     LET x = rnd->get_next( ) 
         y = x * x 
         z = i * 1000 IN 
          ( col1 = bias + x + z 
            col2 = bias + y + z ) ). 
 
out->write( itab ). 
 
out->display( ).
```

## Alternative 2

`... <fs> = wrexp ...`

### Description

Definition of a local field symbol `<fs>` as a helper field in a `LET` expression. The result of the [writable expression](../../abap-glossary/abenwritable_expression_glosry.md) `wrexp` is assigned to the field symbol. The same applies here as to assignments of writable expressions using [`ASSIGN`](../abap-processing-internal-data/abapassign_mem_area_writable_exp.md), which means that only the expressions listed there can be specified. The typing of the field symbol depends on the type of `wrexp` and is performed in the same way as in inline declarations of a field symbol using the statement [`FIELD-SYMBOL`](abenfield-symbol_inline.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a field symbol and a variable as helper fields in a `LET` expression in a conversion expression. The lines of an internal table are assigned to the field symbol.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
   BEGIN OF date, 
     year  TYPE c LENGTH 4, 
     month TYPE c LENGTH 2, 
     day   TYPE c LENGTH 2, 
   END OF date, 
   dates TYPE TABLE OF date WITH EMPTY KEY. 
 
FINAL(dates) = VALUE dates( 
  ( year = '2013' month = '07' day = '16' ) 
  ( year = '2014' month = '08' day = '31' ) 
  ( year = '2015' month = '09' day = '07' ) ). 
 
DO lines( dates ) TIMES. 
  FINAL(isodate) = CONV string( 
    LET <date>  = dates[ sy-index ] 
        sep   =   '-' 
     IN  <date>-year && sep && <date>-month && sep && <date>-day  ). 
  out->write( isodate ). 
ENDDO. 
 
out->display( ).
```
