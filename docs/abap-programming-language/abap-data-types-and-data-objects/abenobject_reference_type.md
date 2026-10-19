---
title: "Object References"
source_file: abenobject_reference_type.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > References"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Object References

Object references can point to instances of [classes](../../abap-glossary/abenclass_glosry.md). The static type of their reference variables is either a class or an interface. Both types can be used to create objects with the statement [`CREATE OBJECT`](../abap-creating-objects-and-values/abapcreate_object.md).

- Class reference variables allow access to all visible components of a class.

- Interface reference variables restrict the view of the [interface components](../../abap-glossary/abeninterface_component_glosry.md) of a class.

If an attempt is made to access an instance attribute using an object reference variable that contains the [null reference](../../abap-glossary/abennull_reference_glosry.md), an uncatchable exception is raised. A catchable exception is raised when an instance method is called.

Object references are always [heap references](../../abap-glossary/abenheap_reference_glosry.md).

## Hint

For more information, see [Object References](../abap-abap-objects/abenreferences.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Inline declaration of an object reference variable `out` with the static type `IF_DEMO_OUTPUT` on the left side of an object of the class `CL_DEMO_OUTPUT` created using its factory method `NEW`. Calling of the method `DISPLAY` using the object component selector.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
out->display( `Hello` ).
```
