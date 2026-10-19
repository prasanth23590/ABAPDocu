---
title: "CONV, Conversion Operator"
source_file: abenconstructor_expression_conv.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CONV, Conversion Operator

## Syntax

``` abap
... CONV type( [let_exp] dobj ) ...  
```

[`let_exp`](../abap-declarations/abaplet.md)

## Description

A [constructor expression](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) with the conversion operator `CONV` [converts](../../abap-glossary/abentype_conversion_glosry.md) the operand `dobj` to the data type specified using `type` and creates an appropriate result. The following can be specified for `type`:

- A non-generic data type `dtype` (with the exception of [reference types](../../abap-glossary/abenreference_type_glosry.md)).

- The `#` character as a symbol for the [operand type](../../abap-glossary/abenoperand_type_glosry.md).

  - If the data type required in an operand position is unique and known completely, this type is used.

  - If the constructor expression is passed to an actual parameter with a generically typed formal parameter, the operand type is derived in accordance with [special rules](abenconv_constructor_inference.md).

  - In other cases, the character `#` cannot be specified.

The parentheses must contain exactly one operand `dobj` that can be converted to the data type `type`, with the following restriction: If `dobj` is specified as a [bit expression](../../abap-glossary/abenbit_expression_glosry.md), `type` must be byte-like or character-like with the type `c` or `string`. `dobj` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md).

The content of the result is determined by an assignment of the operand in accordance with the associated [conversion rule](abenconversion_rules.md). For [enumerated types](../../abap-glossary/abenenum_type_glosry.md), special [rules](abenconv_constructor_enum.md) apply. If `dobj` is compatible with the data type `type`, `CONV` does not need to be used and a syntax check warning is usually produced.

An optional `LET` expression [`let_exp`](../abap-declarations/abaplet.md) can be specified in front of the data object to define local helper fields. If a `LET` expression is specified, no warning is produced in conversions to compatible types, since `LET` can be used to construct new values using helper variables.

## Hints

- The conversion operator `CONV` is suitable for avoiding the declaration of helper variables that are only necessary to do the following, for example

  - specify type-compliant actual parameters.

  - affect the [calculation type](../../abap-glossary/abencalculation_type_glosry.md) of an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md) or the [comparison type](../../abap-glossary/abencomparison_type_glosry.md) of a [relational expression](../../abap-glossary/abenrelational_expression_glosry.md).

- The operand of `CONV` can itself be a [calculation expression](../../abap-glossary/abencalculation_expression_glosry.md), which means that `CONV` can be used within a calculation expression to transform results of partial calculations into a specific type.

- No empty parentheses can be specified after `CONV` to construct an initial value of the specified type. The expression [`VALUE #( )`](../abap-creating-objects-and-values/abenvalue_constructor_params_init.md) can be used to do this.

- The conversion operator `CONV` closes the gap where the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) cannot be used to construct values for elementary data objects except for the initial value.

- If a constructor expression with the conversion operator is used as a source field of an assignment in which the same conversion takes place, it is not necessary and is removed when the program is compiled.

- For reference types, the conversion operator `CONV` is not necessary, since these involve only castings and no conversions. The operator [`CAST`](abenconstructor_expression_cast.md) is used for castings.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The method `CONVERT` of the interface `IF_ABAP_CONV_OUT` of the object created using the class `CL_ABAP_CONV_CODEPAGE` expects the data type `string` for the input parameter `SOURCE`. `CONV` is used to convert a text field to this data type, directly in the operand position.

``` abap
DATA text TYPE c LENGTH 255. 
 
FINAL(xstr) = cl_abap_conv_codepage=>create_out( 
  )->convert( source = CONV string( text ) ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Even though the internal table `itab` in the method `meth1` has the same line type as the table type of the parameter `para` of the method `meth2`, it cannot be passed directly due to the different table type and key. `CONV` is used to convert `itab` to the required table type.

``` abap
CLASS class DEFINITION. 
  PUBLIC SECTION. 
    TYPES t_itab TYPE STANDARD TABLE OF i 
                 WITH EMPTY KEY. 
    METHODS meth1. 
  PRIVATE SECTION. 
    METHODS meth2 IMPORTING para TYPE t_itab. 
ENDCLASS. 
 
CLASS class IMPLEMENTATION. 
  METHOD meth1. 
    DATA itab TYPE SORTED TABLE OF i 
              WITH NON-UNIQUE DEFAULT KEY. 
    ... 
    meth2( CONV #( itab ) ). 
    ... 
  ENDMETHOD. 
  METHOD meth2. 
    ... 
  ENDMETHOD. 
ENDCLASS.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The two calculations produce different results. In the first case, the [calculation type](../../abap-glossary/abencalculation_type_glosry.md) is `f` and the end result is converted to `i`. In the second case, `CONV` converts each interim result to the calculation type `i`.

``` abap
DATA int TYPE i. 
 
int = sqrt( 5 ) + sqrt( 6 ). 
int = CONV i( sqrt( 5 ) ) + CONV i( sqrt( 6 ) ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first logical expression is false, as specified in the [comparison rules for character-like data types](../abap-program-flow-logic/abenlogexp_character.md). `CONV` is used to modify the comparison type of the second comparison so that the comparison is true.

``` abap
DATA txt TYPE abap_boolean. 
DATA str TYPE string. 
 
txt = ' '. 
str = ` `. 
 
IF txt = str. 
  ... 
ENDIF. 
 
IF txt = CONV abap_bool( str ). 
  ... 
ENDIF.
```
