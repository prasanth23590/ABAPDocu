---
title: "CALL BADI"
source_file: abapcall_badi.html
section: "ABAP Programming Language > ABAP - Enhancements > Enhancements Using BAdIs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CALL BADI

## Syntax

``` abap
CALL BADI { badi->meth parameter_list } 
        | { badi->(meth_name) {parameter_list 
                              |parameter_tables} }.  
```

[`parameter_list`](../abap-calling-and-exiting-program-units/abapcall_method_parameters.md) · [`parameter_list`](../abap-calling-and-exiting-program-units/abapcall_method_parameters.md) · [`parameter_tables`](../abap-calling-and-exiting-program-units/abapcall_method_parameter_tables.md)

## Description

Calls a [BAdI method](../../abap-glossary/abenbadi_method_glosry.md). The statement has a static and a dynamic variant. In both variants, a [BAdI reference variable](../../abap-glossary/abenbadi_reference_variable_glosry.md) must be specified for `badi`.

- In the static variant, a [BAdI reference variable](../../abap-glossary/abenbadi_reference_variable_glosry.md) of the static type of a concrete [BAdI class](../../abap-glossary/abenbadi_class_glosry.md) must be specified for `badi`, and for `meth` a BAdI method of the corresponding [BAdI](../../abap-glossary/abenbadi_glosry.md) must be specified directly.

- In the dynamic variant, a [BAdI reference variable](../../abap-glossary/abenbadi_reference_variable_glosry.md) of the static type of the abstract superclass `CL_BADI_BASE` must be specified for `badi`. For `meth_name`, a character-like data object must be specified that must contain the name of a BAdI method in uppercase letters when the statement is executed.

With respect to the addressing of BAdI methods, the BAdI reference variable behaves statically as well as dynamically like an [interface reference variable](../../abap-glossary/abeninterface_ref_variable_glosry.md) with the static type of the affected [BAdI interface](../../abap-glossary/abenbadi_interface_glosry.md). A BAdI method that is declared as a component of the corresponding BAdI interface is addressed directly using its name. BAdI methods declared in [component interfaces](../../abap-glossary/abencomponent_interface_glosry.md) of the BAdI interface can be addressed using the [interface component selector](../../abap-glossary/abeninterface_comp_selector_glosry.md) or any [alias names](../../abap-glossary/abenalias_glosry.md).

The additions [`parameter_list`](../abap-calling-and-exiting-program-units/abapcall_method_parameters.md) or [`parameter_tables`](../abap-calling-and-exiting-program-units/abapcall_method_parameter_tables.md) assign actual parameters to the formal parameters of the BAdI method or handle non-class-based exceptions exactly as described in the [method call](../abap-calling-and-exiting-program-units/abenmethod_calls.md). The exceptions that can occur in dynamic accesses are also the same as those of [`CALL METHOD`](../abap-calling-and-exiting-program-units/abapcall_method_dynamic.md).

The statement `CALL BADI` calls the specified method in all [object plug-ins](../../abap-glossary/abenobject_plugin_glosry.md) to which the [BAdI object](../../abap-glossary/abenbadi_object_glosry.md) referenced by the `badi` refers.

- If the BAdI is defined for single use, `badi` must contain a valid [BAdI reference](../../abap-glossary/abenbadi_reference_glosry.md) for a static BAdI call. If `badi` is initial, a catchable exception is raised.

- If the BAdI is defined for multiple use, `badi` must contain a valid [BAdI reference](../../abap-glossary/abenbadi_reference_glosry.md) for a static BAdI call or can be initial. If the referenced BAdI object refers to multiple object plug-ins, the call order is the same for every `CALL BADI` statement. The exact call order can be determined in the definition of the associated [BAdI implementations](../../abap-glossary/abenbadi_implementation_glosry.md). If the referenced BAdI object does not reference object plug-ins, or the `badi` is initial, the statement has no effect.

- In a dynamic BAdI call, a catchable exception is always raised if there is an invalid BAdI reference in `badi`.

If a method is added to a BAdI afterwards, it may be missing in a BAdI implementation. In this case the call is executed as if the method existed with an empty implementation. Actual parameters that are bound to `EXPORTING` or `RETURNING` parameters passed by value are initialized. All other actual parameters remain unchanged.

## System Fields

With a regular method call, the system field `sy-subrc` is either set to 0 or, when handling non-class-based exceptions, it is set to the value specified after `EXCEPTIONS`.

## Hints

- BAdI objects and BAdI references can only be created using the statement [`GET BADI`](abapget_badi.md).

- The call of a BAdI method of a BAdI defined for single use behaves like a method call with `meth( ...)`: the called method must exist. In contrast, calls of a BAdI method defined for multiple use are more like raising an event using `RAISE EVENT`: One or more methods can exist, or no methods at all.

- The addition [`DEFAULT`](../abap-declarations/abapmethods_default.md) can be used when defining a BAdI method in a BAdI interface to define the behavior for methods that are not implemented.

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_BADI_INITIAL_REFERENCE`

- *Cause:* The reference variable `badi` is initial either for the static call, although the BAdI was defined for single use, or for the dynamic call.

`CX_SY_DYN_CALL_ILLEGAL_METHOD`

- *Cause:* Method does not exist at the dynamic call

  *Runtime error:* `DYN_CALL_METH_NOT_FOUND`
