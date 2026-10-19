---
title: "Runtime Type Services (RTTS)"
source_file: abenrtti.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Properties of Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Runtime Type Services (RTTS)

The [RTTS](../../abap-glossary/abenrun_time_type_services_glosry.md) are implemented using a hierarchy of [type description classes](../../abap-glossary/abentype_class_glosry.md) that contain the methods for [Runtime Type Creation (RTTC)](../../abap-glossary/abenrun_time_type_creation_glosry.md) and [Runtime Type Identification (RTTI)](../../abap-glossary/abenrun_time_type_identific_glosry.md). Using these system classes, it is possible to

- determine type information of existing [instances](../../abap-glossary/abeninstance_glosry.md) and [type names](../abap-data-types-and-data-objects/abentype_names.md) in the [ABAP type hierarchy](../abap-data-types-and-data-objects/abentype_hierarchy.md) at runtime.

- define new data types at runtime.

## Concept

The properties of the types are represented by the attributes of [type description objects](../../abap-glossary/abentype_object_glosry.md). For each type there is exactly one type description object. The attributes of the type description object contain information about the properties of the type. For each type category (elementary type, table, class, and so on), there is a type description class with special attributes for the special type properties. The class hierarchy of the type description classes corresponds to the hierarchy of the type categories in the [ABAP type hierarchy](../abap-data-types-and-data-objects/abentype_hierarchy.md).

In addition, type description classes for complex types, references, classes, and interfaces have special methods for determining references to partial types. These methods can be used to navigate to all partial types using a composite type.

Type description objects can only be created using the methods of type description classes. To get a reference to a type description object of a type, the static methods of the class `CL_ABAP_TYPEDESCR` can be used or methods of the special type description classes can be called.

### Hints

- The RTTS type description classes use constants to refer to data types.

## Hierarchy of Type Description Classes

``` abap
 CL_ABAP_TYPEDESCR 
  | 
  |--CL_ABAP_DATADESCR 
  |   | 
  |   |--CL_ABAP_ELEMDESCR 
  |   |   | 
  |   |   |--CL_ABAP_ENUMDESCR 
  |   | 
  |   |--CL_ABAP_REFDESCR 
  |   |--CL_ABAP_COMPLEXDESCR 
  |       | 
  |       |--CL_ABAP_STRUCTDESCR 
  |       |--CL_ABAP_TABLEDESCR 
  | 
  |--CL_ABAP_OBJECTDESCR 
     | 
     |--CL_ABAP_CLASSDESCR 
     |--CL_ABAP_INTFDESCR
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of the type properties of an elementary type from a type object generated with the method `DESCRIBE_BY_DATA`.

``` abap
TYPES my_type TYPE p LENGTH 16 DECIMALS 6. 
 
DATA  my_data TYPE my_type. 
 
FINAL(descr) = cl_abap_typedescr=>describe_by_data( my_data ). 
 
cl_demo_output=>display( 
  |Typename: { descr->absolute_name }\n| && 
  |Kind:     { descr->type_kind     }\n| && 
  |Length:   { descr->length        }\n| && 
  |Decimals: { descr->decimals      }\n| ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of the properties of the components of a structure. The reference to the type object is assigned using a downcast to a reference variable of type `CL_ABAP_STRUCTDESCR`.

``` abap
cl_demo_output=>display( CAST cl_abap_structdescr( 
  cl_abap_typedescr=>describe_by_name( 'SYST' ) )->components ).
```
