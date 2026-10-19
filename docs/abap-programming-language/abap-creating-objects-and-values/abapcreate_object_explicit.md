---
title: "CREATE OBJECT, TYPE"
source_file: abapcreate_object_explicit.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > CREATE OBJECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CREATE OBJECT, TYPE

## Syntax

``` abap
CREATE OBJECT oref 
                   TYPE { class  [parameter_list] } 
                      | { (name) [parameter_list|parameter_tables] }.  
```

[`parameter_list`](abapcreate_object_parameters.md) · [`parameter_list`](abapcreate_object_parameters.md) · [`parameter_tables`](abapcreate_object_para_tables.md)

## Description

Creation of an instance of an explicitly specified class. A [concrete](../../abap-glossary/abenconcrete_glosry.md) class that is more specific than or identical to the static type of the object reference variable `oref` can be specified. The reference variable `oref` can be a class reference variable or an interface reference variable. The name of the class can be specified as follows:

- `class`

  Direct static specification as `class`.

- `(name)`

  Specification as the content of a character-like data object `name`. The data object `name` must contain the name of the class in uppercase letters when the statement is executed. The class name in `name` can also be an [absolute type name](../../abap-glossary/abenabsolute_typename_glosry.md). The following can be specified for `name`:

  - Literal or constant

    If the data object `name` is specified as a character literal or as a constant, it can be evaluated statically and the specified class is recognized as the used object.

  - Variable

    If the data object `name` is specified as a variable, it is specified only dynamically and the content is not evaluated statically. When the statement is executed, `name` is not evaluated until runtime (in both cases).

The class must be usable at the current position:

- The addition [`CREATE`](../abap-declarations/abapclass_options.md) of the class definition must allow objects to be created.

- The package check must allow an object of a global class to be created.

## Hints

- If the class is specified dynamically, the parameters can either be specified statically in [`parameter_list`](abapcreate_object_parameters.md) or dynamically in [`parameter_tables`](abapcreate_object_para_tables.md).

- When a class is used, the [instance operator](../../abap-glossary/abeninstance_operator_glosry.md) [`NEW`](abenconstructor_expression_new.md) acts like the statement `CREATE OBJECT oref TYPE class` and can be used in [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md). The dynamic specification of `name` is not possible here.

## Security Hint

Dynamic object creation can present a serious security risk if used incorrectly. Names of classes that are passed to a program from the outside must be checked thoroughly before being used in dynamic statements. The system class `CL_ABAP_DYN_PRG`, for example, is used to do this.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of an instance of a class `cls` using an explicit reference to the class. The static type of the reference variable is the root class `object` and is therefore more general than any other class. Components must be accessed dynamically or a cast must be performed as shown here.

``` abap
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    DATA attr TYPE string VALUE 'Object'. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    DATA oref TYPE REF TO object. 
    CREATE OBJECT oref TYPE cls. 
    out->write( CAST cls( oref ) ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```
