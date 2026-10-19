---
title: "CREATE OBJECT"
source_file: abapcreate_object.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CREATE OBJECT

## Syntax Forms

**[Specifying the Class Implicitly](abapcreate_object_implicit.md)**

``` abap
1. CREATE OBJECT oref [parameter_list].
```

**[Specifying the Class Explicitly](abapcreate_object_explicit.md)**

``` abap
2. CREATE OBJECT oref 
                     TYPE { class [parameter_list] } 
                        | { (name) [parameter_list|parameter_tables] }.
```

[`parameter_list`](abapcreate_object_parameters.md) · [`parameter_list`](abapcreate_object_parameters.md) · [`parameter_list`](abapcreate_object_parameters.md) · [`parameter_tables`](abapcreate_object_para_tables.md)

## Description

The statement `CREATE OBJECT` creates an object as an instance of a class and assigns the reference to the object to the reference variable `oref`. The instance constructor of the class is called directly after the object is created.

By default, the object is created in the [internal session](../../abap-glossary/abeninternal_session_glosry.md) (or [heap](../../abap-glossary/abenheap_glosry.md)) of the current program and is preserved there for as long as it is required. If no more [heap references](../../abap-glossary/abenheap_reference_glosry.md) point to the object, the following applies:

- No more object references point to the object.

- No data reference and no field symbol points to an instance attribute or to a part of an instance attribute,

Also, if no more methods of the object are registered as event handlers, it is deleted by the [Garbage Collector](../../abap-glossary/abengarbage_collector_glosry.md).

The reference variable `oref` must be declared as an object reference variable. Instance components of an object created using `CREATE OBJECT` can only be accessed using object reference variables (see [Data Objects in Operand Positions](../abap-operands/abenoperands_data_objects.md)).

The addition `TYPE` can be used to specify the class of the created object. The static type of the object reference variables must be more general than or identical to the class of the created object, in accordance with the rules for [Assignments Between Object Reference Variables](../abap-processing-internal-data/abenconversion_references_objects.md).

Instances of a class can be created only where it is allowed by the addition `CREATE` of the statement [`CLASS DEFINITION`](../abap-declarations/abapclass.md). It can be a local class of the same ABAP program or a global class of the class library allowed by the package check.

The additions [`parameter_list`](abapcreate_object_parameters.md) and [`parameter_tables`](abapcreate_object_para_tables.md) must be used to fill the non-optional input parameters of the first explicitly implemented instance constructor that is on the path of the inheritance tree between the instantiated class and the root class `object`. These additions can also be used to assign return values to the non-class-based exceptions of the instance constructor.

If a catchable exception is raised when the object is created in the runtime framework, the object is not created and the object reference variable `oref` is initialized. If a catchable exception is raised when the object is created in the instance constructor of the class, the created object is deleted and the object reference variable `oref` is initialized.

## System Fields

If the `CREATE OBJECT` statement is executed successfully, `sy-subrc` is set to 0. Values other than 0 can occur when specifying `EXCEPTIONS` in `parameter_spec` when non-class-based exceptions of the instance constructor are handled.

## Hints

- If the reference variable `oref` specified after `CREATE OBJECT` is passed simultaneously to the instance constructor, it already points to the new object when it is executed. To pass a reference to an existing object to the instance constructor, a different reference variable must be used.

- The statement `CREATE OBJECT` creates a [heap reference](../../abap-glossary/abenheap_reference_glosry.md). All references that point to the object or its parts are also heap references and keep the object alive. The same applies to field symbols that point to instance attributes or to their parts.

- If a class is used, the [instance operator](../../abap-glossary/abeninstance_operator_glosry.md) [`NEW`](abenconstructor_expression_new.md) acts like the statement `CREATE OBJECT oref TYPE class` and can be used in [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md).

- The return code `sy-subrc` is set to 0 if the statement is successful because the instance constructor is called. `sy-subrc` is set each time a [method is called](../abap-calling-and-exiting-program-units/abapcall_method_static_short.md).

- A RAP-specific variant [`CREATE OBJECT, FOR TESTING`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapcreate_object_for_testing.md) is available for [unit tests](../../abap-glossary/abenunit_test_glosry.md) of an [ABAP behavior implementation](../../abap-glossary/abenbehavior_pool_glosry.md).

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_CREATE_OBJECT_ERROR`

- *Cause:* An attempt was made to instantiate an abstract class.

  *Runtime error:* `CREATE_OBJECT_CLASS_ABSTRACT`

- *Cause:* The class specified in the addition `TYPE` does not exist.

  *Runtime error:* `CREATE_OBJECT_CLASS_NOT_FOUND`

- *Cause:* The class specified dynamically in `TYPE` does not match the type of the reference variable.

  *Runtime error:* `MOVE_OREF_NOT_CONVERTIBLE`

- *Cause:* An attempt was made to instantiate a private class externally.

  *Runtime error:* `CREATE_OBJECT_CREATE_PRIVATE`

- *Cause:* An attempt was made to instantiate a protected class externally.

  *Runtime error:* `CREATE_OBJECT_CREATE_PROTECTED`
