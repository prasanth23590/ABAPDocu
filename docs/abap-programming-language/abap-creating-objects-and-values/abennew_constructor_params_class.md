---
title: "NEW, Classes"
source_file: abennew_constructor_params_class.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > NEW, Instance Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# NEW, Classes

## Syntax

``` abap
... NEW class|#( [let_exp] p1 = a1 p2 = a2 ... ) ...  
```

[`let_exp`](../abap-declarations/abaplet.md)

## Description

If a class `class` is specified or `#` stands for a class like this, the non-optional input parameters `p1 p2 ...` of the instance constructor of the instantiated class must be filled with the type-compliant actual parameters `a1 a2 ...` The optional input parameters do not need to but can be filled. The description of the statement [`CREATE OBJECT`](abapcreate_object_parameters.md) specifies how parameters are passed and which classes can be used. [No parameters](abennew_constructor_params_initial.md) are passed for a class without an explicit instance constructor. An optional `LET` expression [`let_exp`](../abap-declarations/abaplet.md) can be specified in front of the parameter to define local helper fields.

Like an object reference variable of the type `class`, a constructor expression `NEW class( ... )` can be specified in front of the [object component selector](../../abap-glossary/abenobject_component_select_glosry.md) `->` and in [chained attribute accesses](../../abap-glossary/abenchained_attribute_acc_glosry.md) and [chained method calls](../../abap-glossary/abenchained_method_call_glosry.md).

` ... NEW class( ... )->attr|('attr_name') ...`

` ... NEW class( ... )->meth( ... ) ...`

An attribute can be specified [statically](../abap-operands/abenobject_component_selector.md) as `attr` or [dynamically](../abap-operands/abenobject_component_selector.md) as content of a character-like data object `attr_name` in parentheses. If a dynamically specified attribute is not found, an exception of class `CX_SY_ASSIGN_ILLEGAL_COMPONENT` is raised. A method `meth` can be specified statically only.

A chained method call of this type can be specified as a [standalone statement](../abap-calling-and-exiting-program-units/abapcall_method_static_chain.md) or a [functional method call](../abap-calling-and-exiting-program-units/abapcall_method_functional.md). The result is then preserved for the duration of the statement. Even a single expression without a subsequent object component selector can be executed as a standalone statement. In this case, only the constructor that has a reference to the created object elsewhere is executed if this object needs to be preserved.

In the case of an attribute access `NEW class( ... )->attr`, the following applies specifically:

- It can be specified as a [writable expression](../../abap-glossary/abenwritable_expression_glosry.md) in a [result position](../../abap-glossary/abenresult_position_glosry.md).

- If the data type is suitable, an [offset/length specification](../../abap-glossary/abenoffset_length_specific_glosry.md) [`+off(len)`](../abap-operands/abenoffset_length.md) can be appended unless the chaining is used as [memory area](../abap-processing-internal-data/abapassign_mem_area_writable_exp.md) in the statement `ASSIGN`.

[Method chainings](../../abap-glossary/abenmethod_chaining_glosry.md) cannot be specified between the constructor expression and the attribute here.

## Hints

- This is a functional call of the instance constructor. As in [functional calls](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) of [functional methods](../abap-declarations/abapmethods_functional.md), no [non-class-based exceptions](../abap-program-flow-logic/abenexceptions_non_class.md) can be handled.

- When the instance constructor is called, the return code `sy-subrc` is set to 0. Values other than 0 are not possible, since non-class-based exceptions cannot be handled.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of an instance of the class `c1` when the method `m2` of the class `c2` is called, which requires an input parameter of this type.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    METHODS constructor IMPORTING p1 TYPE i p2 TYPE i. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD constructor. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS c2 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS m2 IMPORTING oref TYPE REF TO c1. 
ENDCLASS. 
 
CLASS c2 IMPLEMENTATION. 
  METHOD m2. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    c2=>m2( NEW #( p1 = 1 p2 = 2 ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of a constructor expression with `NEW` in various positions. The temporary reference variable created using `NEW` is persisted during each statement. The example also shows dynamic specifications and the exception that is raised in case of an invalid attribute.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    DATA     a1 TYPE i. 
    METHODS: m1 RETURNING VALUE(p) TYPE i, 
      m2. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD m1. 
    ... 
  ENDMETHOD. 
  METHOD m2. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
 
    DATA num TYPE i. 
 
    num = NEW c1( )->a1. 
    NEW c1( )->a1 = num. 
    num = NEW c1( )->m1( ). 
    NEW c1( )->m2( ). 
    NEW c1( ). 
 
    TRY. 
        num = NEW c1( )->('a1'). 
      CATCH cx_sy_assign_illegal_component. 
        DATA(exc) = 'X'. 
    ENDTRY. 
    ASSERT exc IS INITIAL. 
 
    TRY. 
        num = NEW c1( )->('x1'). 
      CATCH cx_sy_assign_illegal_component. 
        exc = 'X'. 
    ENDTRY. 
    ASSERT exc IS NOT INITIAL. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Display of an UTC time stamp created in a constructor that only exists while the statement is being executed.

``` abap
CLASS utc DEFINITION. 
  PUBLIC SECTION. 
    DATA ts TYPE utclong. 
    METHODS constructor. 
ENDCLASS. 
 
CLASS utc IMPLEMENTATION. 
  METHOD constructor. 
    ts = utclong_current( ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    cl_demo_output=>display_text( 
      |{ NEW utc( )->ts TIMESTAMP = ISO }| ). 
  ENDMETHOD. 
ENDCLASS.
```

## Executable Example

[Instance Operator `NEW` on the Left](abennew_on_the_left_abexa.md)
