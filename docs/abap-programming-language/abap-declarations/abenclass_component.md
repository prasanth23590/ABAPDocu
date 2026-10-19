---
title: "CLASS, components"
source_file: abenclass_component.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > CLASS > CLASS, DEFINITION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS, components

The components of the classes are defined in the [visibility sections](../../abap-glossary/abenvisibility_section_glosry.md). The following declaration statements are possible for `components`:

- [`TYPES`](abaptypes.md), [`DATA`](abapdata.md), [`CLASS-DATA`](abapclass-data.md), and [`CONSTANTS`](abapconstants.md) for data types and data objects

- [`METHODS`](abapmethods.md), [`CLASS-METHODS`](abapclass-methods.md), [`EVENTS`](abapevents.md), and [`CLASS-EVENTS`](abapclass-events.md) for methods and events

- [`INTERFACES`](abapinterfaces.md) for implementing interfaces and [`ALIASES`](abapaliases.md) for alias names for interface components

## Hint

All the components in a class are in the same namespace. Within a class, the name of a component must be unique, regardless of its type (data type, attribute, method, event, or alias name). The components of an implemented interface are marked with the prefix `intf~` (the name of the interface with interface component selector).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of various components in the public and private visibility section of a class.

``` abap
INTERFACE intf. 
  ... 
ENDINTERFACE. 
 
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES intf. 
    TYPES: 
      data_type TYPE i. 
    CLASS-METHODS: 
      factory RETURNING VALUE(ref) TYPE REF TO cls. 
    METHODS: 
      constructor, 
      meth ... 
  PRIVATE SECTION. 
    DATA: 
      attr TYPE i. 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD factory. 
    ... 
  ENDMETHOD. 
  METHOD constructor. 
    ... 
  ENDMETHOD. 
  METHOD meth. 
    ... 
  ENDMETHOD. 
ENDCLASS.
```
