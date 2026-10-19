---
title: "Properties of Interface Parameters"
source_file: abenfunction_parameters.html
section: "ABAP Programming Language > ABAP - Program Structure > Modularization Statements > Procedures > Function Modules > FUNCTION > Function Module Interface"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Properties of Interface Parameters

When an interface parameter `p1`, `p2`... is defined its properties are determined that are reflected in the syntax of `parameters` and `table_parameters`.

## Syntax

``` abap
... { VALUE(p1) | REFERENCE(p1) }   
         [ {TYPE [REF TO] type} | like_structure   
           [OPTIONAL|{DEFAULT def1}] ]   
    { VALUE(p2) | REFERENCE(p2) }   
         [ {TYPE [REF TO] type} | like_structure   
           [OPTIONAL|{DEFAULT def2}] ]   
    ...  
```

## Description

The syntax and semantics of `VALUE`, `TYPE`, `OPTIONAL`, and `DEFAULT` are mainly the same as in the definition of method interfaces with [`[CLASS-]METHODS`](../abap-declarations/abapmethods_parameters.md). In addition, there is also the obsolete option `like_structure`, which uses `LIKE` or `STRUCTURE` to type interface parameters.

**Type of Parameter Passing**

There are two types of pass by parameters: [pass by reference](../../abap-glossary/abenpass_by_reference_glosry.md) and [pass by value](../../abap-glossary/abenpass_by_value_glosry.md). Pass by value differs from pass by reference in the above syntax, which is indicated by `REFERENCE( )`, by the specification of `VALUE( )`. If only one name `p1 p2 ...` is specified, the parameter is passed by reference by default.

- In pass by reference, the formal parameter points directly to the actual parameter, so that changes to the formal parameters have an immediate effect on the actual parameter.

- In pass by value, the formal parameter is created as a copy of the actual parameter (in `IMPORTING` and `CHANGING` parameters) or as an initial parameter (in `EXPORTING` parameters) on the stack when the function module is called and for `CHANGING` and `EXPORTING` parameters, the formal parameter is copied to the actual parameter when returning from the function module.

Note the following for the different types of parameter:

- In `IMPORTING`, `EXPORTING`, and `CHANGING` parameters, pass by reference and pass by value are possible; for `TABLES` parameters, only pass by reference is possible.

- `IMPORTING` parameters passed by reference must not be overwritten in the function module.

- An `EXPORTING` parameter passed by reference behaves like a `CHANGING` parameter, that is, `EXPORTING` parameters passed by reference are not initialized when the function module is called. Therefore, no read access to these parameters should take place before the first write access. In addition, care must be taken when adding content to such parameters as, for example, when inserting lines into internal tables.

## Hint

The time the function module was last edited specifies whether a parameter passed by reference is shown with or without `REFERENCE( )`. `REFERENCE( )` is shown for function modules that have been modified since ABAP release 7.31.

### Typing of Interface Parameters

The parameter interface of a function module is public throughout the system. Interface parameters can therefore only be typed with reference to data types from the ABAP Dictionary or from the public visibility section of global classes. Interface parameters can be typed using `TYPE`, `TYPE REF TO` or `LIKE`.

Typing with `TYPE [REF TO]` is the only recommended typing for interface parameters of function modules. It takes place when `TYPE` or `TYPE REF TO` is used. For `IMPORTING`, `EXPORTING`, and `CHANGING` parameters, any [built-in ABAP type](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types.md) (complete or generic), or any data type of the ABAP Dictionary or from the public visibility section of a global class can be specified after `TYPE`. After `TYPE REF TO`, the generic data type [`data`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md), a non-generic data type, or an [object type](../../abap-glossary/abenobject_type_glosry.md) can be specified, and the interface parameter is typed as a [reference variable](../../abap-glossary/abenreference_variable_glosry.md). The [typing check](../abap-declarations/abentyping_check.md) is performed in the same way as for methods.

## Hint

Without an explicit typing, a formal parameter is typed implicitly with the fully generic type `any`.

### Optional Parameters

`IMPORTING`, `CHANGING`, and `TABLES` parameters can be made optional by using *optional*. `EXPORTING` parameters are always optional. `IMPORTING` and `CHANGING` parameters can be assigned a replacement parameter. In the above syntax, this is expressed using the additions `OPTIONAL` or `DEFAULT`. For an optional parameter, no actual parameter must be specified when the function module is called. While a formal parameter with the addition `OPTIONAL` is then initialized as a type-compliant parameter, a formal parameter with the addition `DEFAULT` assumes the value and type of the replacement parameter `def1 def2 ...`

If no actual parameter is specified for a generically typed formal parameter with the addition `OPTIONAL` when it is called, the type of the formal parameter is completed according to [fixed rules](../abap-declarations/abentyping_generic.md).

## Hint

Within a function module, the [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md) [`IS SUPPLIED`](../abap-program-flow-logic/abenlogexp_supplied.md) can be used to check whether an optional formal parameter was assigned an actual parameter when it was called.
