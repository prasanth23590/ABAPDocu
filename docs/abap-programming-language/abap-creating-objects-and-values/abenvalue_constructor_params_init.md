---
title: "VALUE, Initial Value for All Types"
source_file: abenvalue_constructor_params_init.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > VALUE, Value Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# VALUE, Initial Value for All Types

## Syntax

``` abap
... VALUE dtype|#( ) ...  
```

## Description

If no parameters are specified in the parentheses, the return value is set to its type-specific initial value. This is possible for any non-generic data types `dtype`. The `#` character can stand for corresponding statically recognizable operand types. When `VALUE #( )` is passed to a generically typed formal parameter, the type is also derived from its generic type as follows:

- `string` for `csequence` and `clike`

- `xstring` for `xsequence`

- `decfloat34` for `numeric` and `decfloat`

- `p` with the length 8 and no decimal places for generic `p`

- The [standard key](../../abap-glossary/abenstandard_key_glosry.md) for a standard table type with generic primary table key

Generic data types other than table types that are explicitly generic with respect to their secondary table keys cannot be made more concrete and produce a syntax error. This applies in particular to the types `c`, `n`, and `x` with generic lengths.

## Hints

- While `VALUE` with pass by value is used only to construct certain complex values (structures and internal tables), `VALUE` without pass by value, on the other hand, is a general method for creating type-dependent initial values in any operand positions.

- The rules for derivations of the type where `#` is specified for actual parameters that are passed to generically typed formal parameters can prevent syntax errors in programs that call a procedure and in which the complete typing of a formal parameter is subsequently generalized by converting to a generic type.

- If `dtype` or `#` stand for an [enumerated type](../../abap-glossary/abenenum_type_glosry.md), its initial value is created according to its [base type](../../abap-glossary/abenbase_type_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of a suitable initial structure for a non-optional input parameter of a method.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    TYPES: BEGIN OF t_struct, 
             col1 TYPE i, 
             col2 TYPE i, 
           END OF t_struct. 
    CLASS-METHODS m1 IMPORTING p TYPE t_struct. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD m1. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    c1=>m1(  VALUE #( ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Executable Example

[Value Operator, Type Inference](abenvalue_type_inference_abexa.md)
