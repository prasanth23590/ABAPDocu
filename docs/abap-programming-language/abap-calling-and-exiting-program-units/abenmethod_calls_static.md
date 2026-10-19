---
title: "Static Method Calls"
source_file: abenmethod_calls_static.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > Method Calls"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Static Method Calls

There are two types of static method call, standalone static method calls and functional static method calls. Method chainings are a special form of static method call.

- [`meth( ... )` - Standalone Method Call](abapcall_method_static_short.md)

- [`meth( ... )` - Functional Method Call](abapcall_method_functional.md)

- [`... meth1( ... )->meth2( ... )->...` - Method Chaining](abapcall_method_static_chain.md)

## System Fields

Each method call sets the system field `sy-subrc` to 0 in the moment the method is called. Handling [non-class-based exceptions](../abap-program-flow-logic/abenexceptions_non_class.md) can change this value.

## Hint

The static method call described here must not be confused with the call of [static methods](../../abap-glossary/abenstatic_method_glosry.md). A static method call is the static specification of an [instance method](../../abap-glossary/abeninstance_method_glosry.md) or a static method. In addition, there is the [dynamic method call](abenmethod_calls_dynamic.md), for which the methods are specified dynamically.

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_NO_HANDLER`

- See [Class-Based Exceptions in Procedures](../abap-program-flow-logic/abenexceptions_procedures.md).

`CX_SY_REF_IS_INITIAL`

- *Cause:* Reference variable is initial

  *Runtime error:* `OBJECTS_OBJREF_NOT_ASSIGNED`
