---
title: "INTERFACE, components"
source_file: abeninterface_component.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > INTERFACE > INTERFACE intf"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INTERFACE, components

The following declaration statements are possible in interfaces for `components`:

- [`TYPES`](abaptypes.md), [`DATA`](abapdata.md), [`CLASS-DATA`](abapclass-data.md), and [`CONSTANTS`](abapconstants.md) for data types and data objects

- [`METHODS`](abapmethods.md), [`CLASS-METHODS`](abapclass-methods.md), [`EVENTS`](abapevents.md), and [`CLASS-EVENTS`](abapclass-events.md) for methods and events

- [`INTERFACES`](abapinterfaces.md) for the inclusion of component interfaces and [`ALIASES`](abapaliases.md) for alias names for their components

The only interface components that can be addressed without implementing the interface in classes are data types and constants. These can be addressed using the name of the interface and the [class component selector](../abap-operands/abenoperands_names.md) (`=>`).

## Hints

- All components of an interfaces are in one namespace. Within an interface, the name of a component must be unique regardless of its type (data type, attribute, method, event, or alias name). The components of an included interface are identified by the prefix `intf~` (name of the interface with interface component selector).

- Interfaces provide fewer variants than classes for declarations of methods using [`METHODS`](abapmethods.md) and [`CLASS-METHODS`](abapclass-methods.md). More specifically, no [constructors](../../abap-glossary/abenconstructor_glosry.md), [test methods](../../abap-glossary/abentest_method_glosry.md), or [AMDP function implementations](../../abap-glossary/abenamdp_function_method_glosry.md) can be declared in interfaces for CDS table functions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of various components in an interface.

``` abap
INTERFACE intf1. 
  ... 
ENDINTERFACE. 
 
INTERFACE intf2. 
    INTERFACES intf1. 
    TYPES: 
      type ... 
    DATA: 
      attr TYPE ... 
    CLASS-METHODS: 
      factory RETURNING VALUE(ref) TYPE REF TO intf2. 
    METHODS: 
      meth ... 
ENDINTERFACE.
```
