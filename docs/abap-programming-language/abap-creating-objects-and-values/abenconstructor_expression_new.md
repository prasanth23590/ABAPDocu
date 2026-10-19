---
title: "NEW, Instance Operator"
source_file: abenconstructor_expression_new.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# NEW, Instance Operator

## Syntax

``` abap
... NEW type( ... ) ...  
```

## Description

A [constructor expression](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) with the instance operator `NEW` creates an [anonymous data object](../../abap-glossary/abenanonymous_data_object_glosry.md) or an [instance](../../abap-glossary/abeninstance_glosry.md) of a class and assigns values to the new object. The result is a reference variable that points to the created object. The following can be specified for `type`:

- A non-generic data type `dtype`.

  The operator `NEW` creates an anonymous data object of data type `dtype`. The result of `NEW` is a data reference variable of [static type](../../abap-glossary/abenstatic_type_glosry.md) `dref` that points to the anonymous data object. The operator `NEW` works in the same way as the statement [`CREATE DATA dref TYPE dtype`](abapcreate_data_existing.md) where `dref` corresponds to the result of the expression. A constructor expression of this type cannot be extended using a [component selector](../../abap-glossary/abencomponent_selector_glosry.md).

- A class `class`.

  The operator `NEW` creates an object of the class `class`. The result of `NEW` is a object reference variable of [static type](../../abap-glossary/abenstatic_type_glosry.md) `class` that points to the object. The operator `NEW` works in the same way as the statement [`CREATE OBJECT oref TYPE class`](abapcreate_object_explicit.md) where `oref` corresponds to the result of the expression.

  - In [general expression positions](../abap-syntax-elements-of-an-abap-program/abengeneral_expression_positions.md), [functional positions](../abap-syntax-elements-of-an-abap-program/abenfunctional_positions.md) and [result positions](../../abap-glossary/abenresult_position_glosry.md) an object component selector `->` can be placed behind `NEW( ... )` and point to an attribute of the class:

    ` ... NEW class( ... )->attr|('attr_name') ...` The attribute can be specified statically as `attr` or dynamically as content of a character-like data object `attr_name` in parentheses. A single expression that points to an attribute of the class using exactly one subsequent object component selector can also be used as the target field of assignments.

  - [Standalone](../abap-calling-and-exiting-program-units/abapcall_method_static_short.md) and [functional](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) method calls, including [chained method calls](../../abap-glossary/abenchained_method_call_glosry.md), can be introduced:

    ` ... NEW class( ... )->meth( ... ) ...` The method must be specified statically.

- The `#` character.

  If the data type required in an operand position is unique and can be identified completely, the `#` character can be used instead of an explicit type specification `type` and the [operand type](../../abap-glossary/abenoperand_type_glosry.md) is used. If the operand type is not known completely, the `#` character cannot be used, with the following exception: The operand can be evaluated after `BASE` when a [structure](abennew_constructor_params_struct.md) or an [internal table](abennew_constructor_params_itab.md) is constructed.

The same descriptions apply as to the `CREATE` statements. After an object is created successfully, it is supplied with values using the parameters specified in parentheses. The syntax of the parameter passing depends on the type used. There are specialized types of parameter passing for complex types.

- [Initial value for all types](abennew_constructor_params_initial.md)

- [Initial value for all data types](abennew_constructor_params_single.md)

- [Structures](abennew_constructor_params_struct.md)

- [Internal tables](abennew_constructor_params_itab.md)

- [Classes](abennew_constructor_params_class.md)

If a constructor expression is [assigned](../abap-processing-internal-data/abenequals_operator.md) to a reference variable using `NEW`, the information in the parentheses is evaluated before the created object is bound to the target variable.

## System Fields

If an instance of a [class](abennew_constructor_params_class.md) is created successfully, the instance operator `NEW` sets `sy-subrc` to 0. Since non-class-based exceptions of the instance constructor cannot be handled, `sy-subrc` is never set to a value other than 0. The return code `sy-subrc` is not set when anonymous data objects are created.

## Hints

- To create the values for a new data object, the instance operator `NEW` uses mainly the same syntax as the value operator [`VALUE`](abenconstructor_expression_value.md).

- The instance operator `NEW` always creates a new temporary reference variable that points to the created object. The reference variable is used as the operand of a statement and then deleted. It is deleted when the current statement is closed or after the evaluation of a relational expression once the truth value is determined. The created object is passed to the Garbage Collector if it is not received by a [heap reference](../../abap-glossary/abenheap_reference_glosry.md) or a field symbol after the temporary reference variable has been deleted.

- [Assignments](../abap-processing-internal-data/abenequals_operator.md) to a reference variable also always create a temporary reference variable that is only assigned to the target variable afterwards. This means that the object to which the target variable points before the assignment can be addressed using it throughout the entire expression. This is the difference between `NEW` and the value operator [`VALUE`](abenconstructor_expression_value.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of an anonymous data object of the type `i` with the value 555 and an instance of a local class `cls` whereby this is derived implicitly from the static type of `oref`. In this case, the last statement could be written explicitly as `oref = NEW cls( )` or as `DATA(oref) = NEW cls( )`, using an inline declaration instead of the preceding `DATA` statement.

``` abap
CLASS cls DEFINITION. 
  ... 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA: dref TYPE REF TO data, 
          oref TYPE REF TO cls. 
 
    dref = NEW i( 555 ). 
    oref = NEW #( ). 
  ENDMETHOD. 
ENDCLASS.
```
