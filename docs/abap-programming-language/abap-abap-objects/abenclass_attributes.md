---
title: "ABAP Objects - Attributes of Classes"
source_file: abenclass_attributes.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Classes > ABAP Objects - Components of Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Attributes of Classes

Attributes are internal data objects of a class of any ABAP data type. The content of the attributes determines the state of the object. Reference variables can also be defined, which can then be used to create and address objects. This allows objects to be accessed within classes.

Attributes are defined in the declaration part of a class. Public attributes are visible from outside the class without restrictions and as such are part of the interface between objects and their users. To encapsulate the state of the object, protected, package-visible, or private attributes must be used. In addition to the visibility, the modifiability of non-private attributes can also be restricted using the addition [`READ-ONLY`](../abap-declarations/abapdata_options.md) in the declaration.

- [Instance Attributes](abenclass_attributes.md#instance-attributes)

- [Static Attributes](abenclass_attributes.md#static-attributes)

- [Data Types of Attributes](abenclass_attributes.md#data-types-of-attributes)

- [Boxed Components](abenclass_attributes.md#boxed-components)

## Instance Attributes

The content of instance attributes represents the instance-dependent state of the object. Instance attributes are declared using the [`DATA`](../abap-declarations/abapdata.md) statement. The addition `COMMON PART` cannot be used in classes.

### Hints

- The attempt to access an instance attribute via an initial [object reference variable](../../abap-glossary/abenobject_refer_variable_glosry.md), in contrast to the call of an instance method, results in an exception that is not catchable.

- The data types of all class attributes belong to the static properties of a class. A `LIKE` addition enables the visible class attributes to be referenced using the class component selector or reference variables without first creating an object.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Referring to an instance attribute behind `LIKE` with the object component selector without creating an instance of the class of the attribute.

``` abap
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    DATA attr TYPE i. 
ENDCLASS. 
 
CLASS user DEFINITION. 
  PUBLIC SECTION. 
    METHODS meth. 
ENDCLASS. 
 
CLASS user IMPLEMENTATION. 
  METHOD meth. 
    DATA oref TYPE REF TO cls. 
    TYPES typ LIKE oref->attr. 
  ENDMETHOD. 
ENDCLASS.
```

## Static Attributes

The content of static attributes represents the instance-independent state of the class that is valid for all instances. Static attributes exist once for each class. They are declared using the statement [`CLASS-DATA`](../abap-declarations/abapclass-data.md) and are preserved for the entire runtime. All the objects of a class can access its static attributes. Changes to a static attribute in an object are visible to all other objects of that class.

## Data Types of Attributes

The data types of all attributes, including instance attributes and, in particular, [bound data types](../../abap-glossary/abenbound_data_type_glosry.md), belong to the static properties of a class. Therefore, in a `LIKE` addition, the class component selector or reference variables can be used to refer to the visible attributes of a class, without first creating an object. In this way, the public static properties of global classes can be accessed in every program.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reference to the data type of an instance attribute `attr` of a global class `cl_global`.

``` abap
DATA dref TYPE REF TO cl_global. 
 
DATA:  f1 LIKE cl_global=>attr, 
       f2 LIKE dref->attr.
```

## Boxed Components

Like substructures of nested structures, attributes declared as structures can be declared as [static boxes](../../abap-glossary/abenstatic_box_glosry.md) using the addition [`BOXED`](../abap-declarations/abapdata_boxed.md). In static boxes, [initial value sharing](../../abap-glossary/abeninitial_value_sharing_glosry.md) takes effect, which leads to fewer memory requirements for little used structures of frequently used objects. A static box used as a [boxed component](../../abap-glossary/abenboxed_component_glosry.md) is a deep component that is managed using an internal reference, such as strings and internal tables.
