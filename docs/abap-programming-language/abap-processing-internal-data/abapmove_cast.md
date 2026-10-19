---
title: "=, ?=, Upcast and Downcast"
source_file: abapmove_cast.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Reference Variables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# =, ?=, Upcast and Downcast

## Syntax

``` abap
destination_ref =|?= source_ref.  
```

## Description

Assignment between two reference variables. The reference in `source_ref` is assigned `destination_ref`. After a successful assignment, `destination_ref` points to the same object as `source_ref` ([reference semantics](../../abap-glossary/abenreference_semantics_glosry.md)). The assignment of reference variables is a special form of [assignments of data objects](abapmove.md), whereby two assignment operators are available for assignments between reference variables and are used in accordance with the [assignment rules for reference variables](abenconversion_references.md):

- In assignments between reference variables, the general [assignment operator `=`](abenequals_operator.md) can only be used for [upcasts](../../abap-glossary/abenup_cast_glosry.md) in which the static type of `source_ref` is more specific than or the same as the static type of `destination_ref`.

- The special [casting operator](../../abap-glossary/abencasting_operator_glosry.md) `?=` can only be used for assignments between reference variables. If the static type of `source_ref` is more general than the static type of `destination_ref`, `?=` must be used to produce a [downcast](../../abap-glossary/abendown_cast_glosry.md). If this is known statically, it is checked by the syntax check, otherwise it is checked at runtime. The actual downcast, that is, the check to see whether assignments are possible in accordance with the [assignment rules](abenconversion_references.md) for reference variables, only takes place at runtime. Then, if the static type of `destination_ref` is not more general or is the same as the dynamic type of `source_ref`, a catchable exception is raised and the target variable keeps its original value.

The same applies to the right side and left side as when [assigning data objects](abapmove.md), with the following restrictions:

- The data types of the source and target are [reference types](../../abap-glossary/abenreference_type_glosry.md), which means that [functional method calls](../../abap-glossary/abenfunctional_method_call_glosry.md), and [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md) and [table expressions](../../abap-glossary/abentable_expression_glosry.md) can be specified on the right side whose return value has a reference type. [Built-in functions](../../abap-glossary/abenbuiltin_function_glosry.md) and [calculation expressions](../../abap-glossary/abencalculation_expression_glosry.md) do not return any reference variables and are not possible here.

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md) is possible only on the left side of `=`, and not on the left side of `?=`. The static types of the reference variable `source_ref` is used, which must be known statically.

## Hints

- The casting operator `?=` can always be specified, even for upcasts. This is, however, not usually necessary.

- If it is possible to know statically that an assignment is not possible, neither `=` nor `?=` can be used. This is the case, for example, when the static types of source variables and target variables are classes from different paths of the inheritance tree.

- The [null reference](../../abap-glossary/abennull_reference_glosry.md) of an initial reference variable can be assigned to every target variable in a downcast that can be specified here. The same applies to a non-initial invalid reference that no longer points to an object.

- For non-initial reference variables, the predicate expression [`IS INSTANCE OF`](../abap-program-flow-logic/abenlogexp_instance_of.md) or the case distinction [`CASE TYPE OF`](../abap-program-flow-logic/abapcase_type.md) can be used to check whether a downcast is possible on specific classes or interfaces.

- In addition to `?=`, the [casting operator](../../abap-glossary/abencasting_operator_glosry.md) [`CAST`](abenconstructor_expression_cast.md) also enables downcasts in operand positions, which helps to reduce helper variables.

- Downcasts are also possible using the `INTO` addition of the statement [`WHEN TYPE`](../abap-program-flow-logic/abapwhen_type.md) of a case distinction using [`CASE TYPE OF`](../abap-program-flow-logic/abapcase_type.md).

- The casting operator `?=` cannot be used in [multiple assignments](abapmove_multiples.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first two assignments in the following source code section are upcasts:

- The instance operator `NEW` creates a result with the static and dynamic type `c2`, which can be assigned to the more general reference variable `oref1`.

- Any reference variable can be assigned to the reference variable `oref` with the most general static type `object`.

The next two assignments are downcasts:

- It is only possible to check at runtime whether the general reference variable `oref` points to an object that can also point to `oref2`. This is the case in the example.

- The downcast of `oref2` to `oref3`, however, fails at runtime and raises the caught exception.

``` abap
CLASS c1 DEFINITION INHERITING FROM object. 
ENDCLASS. 
 
CLASS c2 DEFINITION INHERITING FROM c1. 
ENDCLASS. 
 
CLASS c3 DEFINITION INHERITING FROM c2. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA oref  TYPE REF TO object. 
    DATA oref1 TYPE REF TO c1. 
    DATA oref2 TYPE REF TO c2. 
    DATA oref3 TYPE REF TO c3. 
 
    oref1 = NEW c2( ). 
 
    oref = oref1. 
 
    IF oref IS INSTANCE OF c2. 
      oref2 ?= oref. 
    ENDIF. 
 
    TRY. 
        oref3 ?= oref2. 
      CATCH cx_sy_move_cast_error. 
        ... 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_MOVE_CAST_ERROR`

- *Cause:* Type conflict in downcast

  *Runtime error:* `MOVE_CAST_ERROR`

- *Cause:* Source variable or target variable is not a reference variable

  *Runtime error:* `MOVE_CAST_REF_ONLY`

- *Cause:* Dynamic type conflict in assignment of references

  *Runtime error:* `MOVE_CAST_ERROR_DYN`
