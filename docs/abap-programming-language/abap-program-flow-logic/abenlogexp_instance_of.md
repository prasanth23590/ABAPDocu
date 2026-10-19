---
title: "rel_exp - IS INSTANCE OF"
source_file: abenlogexp_instance_of.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > rel_exp - Predicates > rel_exp - Predicate Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - IS INSTANCE OF

## Syntax

``` abap
... oref IS [NOT] INSTANCE OF class|intf  
```

## Description

The predicate expression `IS INSTANCE OF` checks whether

- for a non-initial [object reference variable](../../abap-glossary/abenobject_refer_variable_glosry.md) `oref` the [dynamic type](../../abap-glossary/abendynamic_type_glosry.md)

- for an initial [object reference variable](../../abap-glossary/abenobject_refer_variable_glosry.md) `oref` the [static type](../../abap-glossary/abenstatic_type_glosry.md)

is more specific or equal to a comparison type. The comparison type must be an [object type](../../abap-glossary/abenobject_type_glosry.md), that is, a class specified using `class` or an interface specified using `intf` that can be used here. `oref` expects an object reference variable with the static type of a class or of an interface. `oref` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md).

The expression is true in the following cases or false if `NOT` is specified:

- The object reference variable `oref` is not initial and points to an object whose class either:

  - Is the class specified using `class` or one of its subclasses

  - Implements the interfaces specified using `intf`

- The object reference variable `oref` is initial and the static type of `oref` either:

  - Is the same class or subclass of `class`

  - Contains the interface `intf` as a component

If a field symbol or a formal parameter is specified for `oref`, its type can be fully generic, which means it can be typed with [`any`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) and it must be an object reference variable at runtime. If a generically typed field symbol or a generically typed formal parameter is specified for `oref`, the static type of the object reference variable is used that is represented by the field symbol or formal parameter at runtime.

A syntax error occurs if it is known statically that the result of the expression is false.

## Hints

- The predicate expression `IS INSTANCE OF` checks whether a cast from `oref` to an object reference variable with the static type `class` or `intf` is possible.

  - If `IS INSTANCE OF` is true for a non-initial object reference variable `oref`, a [downcast](../../abap-glossary/abendown_cast_glosry.md) is possible. This means that the predicate expression `IS INSTANCE OF` can be used as condition for a [downcast](../../abap-glossary/abendown_cast_glosry.md) instead of the corresponding exception handler.

  - If a predicate expression `IS INSTANCE OF` is true for an initial object reference variable `oref`, an [upcast](../../abap-glossary/abenup_cast_glosry.md) is possible. Checks of this type are generally suitable for generically typed field symbols or formal parameters. In this way, it is possible to detect at runtime whether the field symbol or the formal parameter represents an object reference variable of a certain static type.

- If the static type of `oref` is an interface and a class `class` is specified as the comparison type, the result of the expression is always false if the reference variable is initial.

- When a subclass is instantiated, the predicate expression `IS INSTANCE OF` is false when the associated object reference to the subclass is checked until the [instance constructors](../../abap-glossary/abeninstance_constructor_glosry.md) of all superclasses have been executed. When an instance constructor of a superclass is executed, `IS INSTANCE OF` is true for the current superclass.

- The special case distinction [`CASE TYPE OF`](abapcase_type.md) makes it possible to abbreviate consecutive predicate expressions `IS INSTANCE OF`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

All of the following predicate expressions are true, since the dynamic type of the object reference variable `oref` is more specific than or equal to the specified object type.

``` abap
INTERFACE intf. 
ENDINTERFACE. 
 
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES intf. 
ENDCLASS. 
 
CLASS c2 DEFINITION INHERITING FROM c1. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA oref TYPE REF TO object. 
 
    oref = NEW c1( ). 
    ASSERT oref IS INSTANCE OF c1. 
    ASSERT oref IS INSTANCE OF intf. 
 
    oref = NEW c2( ). 
    ASSERT oref IS INSTANCE OF c2. 
    ASSERT oref IS INSTANCE OF c1. 
    ASSERT oref IS INSTANCE OF intf. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows how the predicate expression `IS INSTANCE OF` can be used to check the feasibility of a [downcast](../../abap-glossary/abendown_cast_glosry.md). This makes the exception handler, which is also shown, superfluous.

``` abap
CLASS c1 DEFINITION. 
ENDCLASS. 
 
CLASS c2 DEFINITION INHERITING FROM c1. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
 
    DATA: ref1 TYPE REF TO c1, 
          ref2 TYPE REF TO c2. 
 
    ref1 = NEW c2( ). 
 
    IF ref1 IS INSTANCE OF c2. 
      ref2 ?= ref1. 
    ENDIF. 
 
    TRY. 
        ref2 ?= ref1. 
      CATCH cx_sy_move_cast_error. 
    ENDTRY. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Executable Example

[Predicate Expression `IS INSTANCE OF`](abeninstance_of_abexa.md)
