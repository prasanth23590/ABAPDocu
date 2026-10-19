---
title: "EXACT, Lossless Operator"
source_file: abenconstructor_expression_exact.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Lossless Assignments"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EXACT, Lossless Operator

## Syntax

``` abap
... EXACT type( [let_exp] dobj ) ...  
```

[`let_exp`](../abap-declarations/abaplet.md)

## Description

A [constructor expression](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) with the lossless operator `EXACT` performs either a [lossless assignment](abenlossless_move.md) or a [lossless calculation](abenlossless_calculation.md), depending on the specified operand `dobj`, and creates a result with the data type `type`. The following can be specified for `type`:

- A non-generic data type `dtype`, apart from [reference types](../../abap-glossary/abenreference_type_glosry.md).

- The `#` character for a data type that is determined in accordance with the following hierarchy:

  - If the data type required in an operand position is unique and known completely, the [operand type](../../abap-glossary/abenoperand_type_glosry.md) is used. The operand type can also be generic, and the current type is used at runtime.

  - If the data type cannot be derived from the context, the calculation type `decfloat34` is used in lossless calculations and the data type of the operand is used in lossless assignments.

The parentheses must contain exactly one operand `dobj` that can be converted to the data type `type`. `dobj` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md). The content of the result is determined as follows:

- If the operand `dobj` is specified as an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md), the expression is calculated in accordance with the rules for a [lossless assignment](abenlossless_calculation.md) and the result with the calculation type `decfloat34` is converted to the data type `type`.

- In all other cases, the content of the result is determined by an assignment of the operand in accordance with the associated [conversion rules](abenconversion_rules.md), during which a check is performed in accordance with the [rules of lossless assignments](abapmove_exact.md).

In the case of a value loss, the corresponding exception is raised in both cases. If the operand is compatible with the data type `type` in a lossless assignment, `EXACT` does not perform any checks and a syntax check warning occurs. For [enumerated types](../../abap-glossary/abenenum_type_glosry.md), additional special [rules](abenexact_constructor_enum.md) apply.

An optional `LET` expression [`let_exp`](../abap-declarations/abaplet.md) can be specified before the operand to define local helper fields.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Lossless assignment. Here, the exception `CX_SY_CONVERSION_ERROR` is raised, because the operand contains an invalid value.

``` abap
TYPES numtext TYPE n LENGTH 255. 
 
TRY. 
    FINAL(number) = EXACT numtext( '4 Apples + 2 Oranges' ). 
  CATCH cx_sy_conversion_error INTO FINAL(exc). 
    ... 
ENDTRY.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Lossless assignment with generic types. The first method call produces a successful assignment and the second raises the exception `CX_SY_CONVERSION_EXACT_NOT_SUP`. If the assignment is replaced with `p2 = EXACT #( + p1 )`, a lossless calculation is produced and no exception is raised.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS m1 IMPORTING p1 TYPE data 
                     EXPORTING p2 TYPE data. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD m1. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    DATA arg TYPE i. 
    TRY. 
        p2 = EXACT #( p1 ) ##operator. 
        out->write_data( p2 ). 
      CATCH cx_sy_conversion_exact_not_sup 
            cx_sy_conversion_error INTO FINAL(err). 
        out->write_text( err->get_text( ) ). 
    ENDTRY. 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA: date TYPE d, 
          text TYPE string. 
 
    FINAL(time) = cl_demo_date_time=>get_user_time( ). 
    c1=>m1( EXPORTING p1 = time 
            IMPORTING p2 = text ). 
 
    c1=>m1( EXPORTING p1 = time 
            IMPORTING p2 = date ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Lossless calculation. Here, the exception `CX_SY_CONVERSION_ROUNDING` is raised, because the calculation is not lossless. The rounded result is assigned to the inline declared variable `rounded_result`.

``` abap
TRY. 
    FINAL(exact_result) = EXACT #( 3 * ( 1 / 3 ) ). 
  CATCH cx_sy_conversion_rounding INTO FINAL(exc). 
    FINAL(rounded_result) = exc->value. 
ENDTRY.
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_CONVERSION_EXACT_NOT_SUP`

- *Cause:* Invalid combination of types or lengths.

  *Runtime error:* `CONVT_NOT_SUPPORTED`
