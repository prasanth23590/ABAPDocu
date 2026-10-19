---
title: "TYPES, REF TO"
source_file: abaptypes_references.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, REF TO

## Syntax

``` abap
TYPES ref_type { {TYPE REF TO type}   
               | {LIKE REF TO dobj} }.  
```

## Description

The addition `REF TO` defines a data type for a [reference variable](../../abap-glossary/abenreference_variable_glosry.md). The static type of the reference variable is specified after `REF TO`. The static type restricts the object quantity to which a reference variable can point. The dynamic type of a reference variable is the data type and the object class to which it points. The static type is always more general or the same as the dynamic type (see also [assignment rules for reference variables](../abap-processing-internal-data/abenconversion_references.md)).

Apart from `data` and `object`, no [generic data types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified after `TYPE REF TO`.

**Types for Data Reference Variables**

If the predefined generic data type [`data`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) is specified for `type`, a data type for a data reference variable of the generic static type `data` is created. Reference variables like these can point to any data objects.

If a non-generic data type is specified for `type` (meaning a non-generic data type from the ABAP Dictionary, from ABAP CDS, or from the public visibility section of a global class, a non-generic local program type already defined using `TYPES`, or a non-generic [built-in ABAP type](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md)), a data type is created for a data reference variable with the corresponding static type. Reference variables like these can point to all data objects of the same type.

The same applies to `dobj` as to [`TYPES ... LIKE`](abaptypes_referring.md). A data type is created for a data reference variable whose static type is inherited from the data type of the specified data object. Reference variables like these can point to all data objects of the same type.

A data reference variable can be dereferenced in different ways, depending on its static type:

- A data reference variable typed generically with `TYPE REF TO data` can be dereferenced only in the statement [`ASSIGN`](../abap-processing-internal-data/abapassign_mem_area_dynamic_dobj.md) with the [dereferencing operator](../../abap-glossary/abendereferencing_operat_glosry.md) `->*`.

- A data reference variable typed fully with `TYPE REF TO complete_type` or `LIKE REF TO dobj` can be dereferenced in all suitable operand positions using the dereferencing operator `->*`. If the static data type is structured, the [object component selector](../../abap-glossary/abenobject_component_select_glosry.md) enables access to the components of the structure with `dref->comp`.

**Types for Data Reference Variables**

If the predefined generic data type [`object`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) is specified for `type`, a data type for a class reference variable of the generic static type `data` is created. Reference variables like these can point to instances of any class.

If a global or local class is specified for `type`, a data type for a class reference variable whose static type is the specified class is created. Reference variables like these can point to all instances of the class and its subclasses. A class reference variable can be used to access all components of an object. If the static type is the superclass of the dynamic type, the components that can be accessed statically are a subset of the components of the dynamic type. All attributes and methods of the dynamic type can be accessed using a class reference variable and the dynamic access to object attributes (see `ASSIGN`) and the dynamic method call (see [`CALL METHOD`](../abap-calling-and-exiting-program-units/abapcall_method_dynamic.md)).

If a global or local interface is specified for `type`, a data type for an interface reference variable whose static type is the specified interface is created. Reference variables like these can point to objects of all classes that implement the interface. When using interface references to access components of objects, the name of the static type is always implicitly placed in front of the component. An interface reference variable can only be used to access those interface components of an object that are known in the static type. This applies to both dynamic and static access.

## Hints

- The `TYPE` addition can be used to define data types for data reference variables and object reference variables. Only data types for data reference variables can be defined using the `LIKE` addition.

- The predefined generic data type `any` can only be specified after `TYPE`, like all other [generic types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) apart from `data` and `object`, but not after `REF TO`.

- Data reference variables can also be declared with the static type of an [enumerated type](abaptypes_enum.md) and can then point to data objects of the corresponding type.

- Since the global [object types](../../abap-glossary/abenobject_type_glosry.md) of the [class library](../../abap-glossary/abenclass_library_glosry.md) are in the same namespace as all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP, the specification of `type` is always unique.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example shows how data types are defined for an interface reference variable and for a class reference variable and how a data reference is defined with the static type of the interface reference variable.

``` abap
INTERFACE i1. 
... 
ENDINTERFACE. 
 
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES i1. 
ENDCLASS. 
 
TYPES: iref TYPE REF TO i1, 
       cref TYPE REF TO c1, 
       dref TYPE REF TO iref.
```
