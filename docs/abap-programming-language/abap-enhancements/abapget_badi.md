---
title: "GET BADI"
source_file: abapget_badi.html
section: "ABAP Programming Language > ABAP - Enhancements > Enhancements Using BAdIs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# GET BADI

## Syntax

``` abap
GET BADI { badi [FILTERS f1 = x1 f2 = x2 ...] }   
       | { badi TYPE (name)   
              [ {FILTERS f1 = x1 f2 = x2 ...}   
              | {FILTER-TABLE ftab}] }   
              [CONTEXT con].  
```

### Addition

[1. `... FILTERS f1 = x1 f2 = x2 ...`](abapget_badi.md#addition-1)

[2. `... FILTER-TABLE ftab`](abapget_badi.md#addition-2)

[3. `... CONTEXT con`](abapget_badi.md#addition-3)

## Overview

### Description

This statement creates a new [BAdI object](../../abap-glossary/abenbadi_object_glosry.md) and sets the [BAdI reference](../../abap-glossary/abenbadi_reference_glosry.md) to the object in a [BAdI reference variable](../../abap-glossary/abenbadi_reference_variable_glosry.md) `badi`. This statement has a static and a dynamic variant.

- In the case of the static variant, the addition `TYPE` is not specified. The static type of the reference variable `badi` must be a [BAdI](../../abap-glossary/abenbadi_glosry.md) and determines which BAdI is used.

- In the case of the dynamic variant, a character-like data object `name` is specified for the addition `TYPE`. When the statement is executed, this object must contain the name of a BAdI. The static type of the reference variable `badi` must be the superclass `CL_BADI_BASE` of all BAdI classes.

To specify values for the filters of the BAdI, the addition `FILTERS` can be specified in the static variant, or the addition `FILTER-TABLE` in the dynamic variant.

In the case of a context-free BAdI, the addition `CONTEXT` cannot be specified. In the case of a context-dependent BAdI, however, it must be specified.

After instantiation, the system searches for [BAdI implementation classes](../../abap-glossary/abenbadi_implement_class_glosry.md) for the BAdI as follows:

1.  Only BAdI implementation classes are selected that are assigned to a [BAdI implementation](../../abap-glossary/abenbadi_implementation_glosry.md) that is in the state *active*.

2.  Only BAdI implementation classes are selected that are assigned to a BAdI implementation, that is, to an [enhancement](../../abap-glossary/abenenhancement_glosry.md) whose [switch](../../abap-glossary/abenswitch_glosry.md) is in the state *on*. If no switch is assigned to a BAdI implementation, it is handled in the same way as an implementation with a switch in the state *on*.

3.  All BAdI implementation classes are selected that satisfy the above requirements and for which the filter condition of the BAdI implementation matches the values specified after `FILTERS` or in `ftab`. If no BAdI implementations are found with the filter specifications, the system searches for BAdI implementations that are marked as standard implementations. If non are found, the fallback BAdI implementation class of the BAdI is used (if available).

4.  If multiple BAdI implementation classes with matching filter conditions were found for a BAdI defined for single use, [conflict resolution](../../abap-glossary/abenconflict_resolution_glosry.md) is performed. A successful conflict resolution produces exactly one priority [conflict-resolving enhancement implementation](../../abap-glossary/abenconflict_resol_impl_glosry.md) and only its BAdI implementation class is selected. If multiple conflict-solving enhancement implementations have the same priority or if there are no conflict-solving enhancement implementations at all, then a correct conflict solution is not possible and multiple BAdI implementation classes will remain in the hit list.

If the resulting hit list matches the definition of the BAdI which means:

- For a BAdI defined for single use, the hit list must contain exactly one BAdI implementation class,

- For a BAdI defined for multiple use, the hit list may contain multiple or no BAdI implementation classes,

references to [object plug-ins](../../abap-glossary/abenobject_plugin_glosry.md) of the found BAdI implementations are stored in the BAdI object. [Object plug-ins](../../abap-glossary/abenobject_plugin_glosry.md) that do not yet exist are created for this purpose. Whether an existing object plug-in is reused or whether a new object plug-in is created depends on whether the BAdI is context-free or context-dependent, and also depends on the addition `CONTEXT`. The precise semantics are described in the addition.

If the hit list contains no or multiple BAdI implementations although the BAdI is defined for single use, an exception occurs. If the BAdI reference variable `badi` contained a valid BAdI reference before the statement in an exception case, this is retained, otherwise it is initialized.

### Hints

- It is not possible to access BAdI objects directly using BAdI references. The references are only used to call the [BAdI methods](../../abap-glossary/abenbadi_method_glosry.md) in the referenced object plug-ins with the statement [`CALL BADI`](abapcall_badi.md). Otherwise, BAdI reference variables can be used in the same operand positions as regular [object reference variables](../../abap-glossary/abenobject_refer_variable_glosry.md). In particular, this means that assignments and comparisons are possible.

- The method `NUMBER_OF_IMPLEMENTATIONS` of the class `CL_BADI_QUERY` returns the number of BAdI implementations that are stored in a BAdI object.

- To prevent the exception for BAdIs that are defined for single use in systems in which no corresponding enhancement is made, it is recommended that a fallback BAdI implementation class is specified for these BAdIs. The fallback BAdI implementation class is part of the BAdI and is independent of enhancements.

- To access object plug-ins directly requires the corresponding references. These can be returned, for example, by BAdI methods.

- The BAdI reference cannot be used to handle any instance events of a BAdI. Instead, when the [event handler](../../abap-glossary/abenevent_handler_glosry.md) is registered, either the addition `FOR ALL INSTANCES` must be specified using [`SET HANDLER`](../abap-calling-and-exiting-program-units/abapset_handler.md), or a reference to an object plug-in must be specified directly.

## Addition 1

`... FILTERS f1 = x1 f2 = x2 ...`

### Description

After the addition `FILTERS`, the elementary data objects `x1`, `x2`, ... must be specified for all `f1`, `f2`, ... filters of the BAdI. If a filter in the BAdI has the property *Constant Filter Value at Call*, only [literals](../../abap-glossary/abenabap_literal_glosry.md) and [constants](../../abap-glossary/abenconstant_glosry.md) can be specified. The data objects must be compatible with the data type of the filters. `FILTERS` cannot be specified for a BAdI without filters.

## Addition 2

`... FILTER-TABLE ftab`

### Description

Using the special internal table `ftab`, this addition assigns values to the filters of a dynamically specified BAdI. The internal table must have table type `BADI_FILTER_BINDINGS` from the ABAP Dictionary. When the statement `GET BADI` is executed, the table must contain exactly one line for each of the filters of the BAdI. The table columns are:

- `NAME` of type `c` and length 30

  for the name of the filter in uppercase letters. Declaring a nonexistent filter raises an uncatchable exception.

- `VALUE` of the type `REF TO data`

  As a pointer to a matching data object. The value of the data object to which the reference variable in `VALUE` refers is assigned to the filter specified in `NAME`.

The column `NAME` is the unique key of the sorted table `ftab`.

## Addition 3

`... CONTEXT con`

### Description

Using the addition `CONTEXT`, an [object reference variable](../../abap-glossary/abenobject_refer_variable_glosry.md) `con` must be specified for context-dependent BAdIs, whose static type is or includes the [tag interface](../../abap-glossary/abentag_interface_glosry.md) `IF_BADI_CONTEXT`, and which contains a reference to a [BAdI context object](../../abap-glossary/abenbadi_context_object_glosry.md). If `con` is initial, an exception is raised. The addition `CONTEXT` cannot be entered for context-free BAdIs.

The addition `CONTEXT` controls how the object plug-ins are created as follows:

- Without the addition `CONTEXT`, that is, for context-free BAdIs, the way the object plug-ins are created is based on the setting of the BAdI. Either new plug-ins are created every time the statement `GET BADI` is executed, or an object plug-in that has already been created in the current [internal session](../../abap-glossary/abeninternal_session_glosry.md) is reused, if it is required again. An object plug-in of this type is a singleton in terms of its BAdI implementation class.

- Using the addition `CONTEXT`, that is, for context-dependent BAdIs, the same object plug-ins are always used for the same content of `con`. These object plug-ins are singletons in terms of their BAdI implementation class and a BAdI context object.

If a BAdI implementation class implements multiple [BAdI interfaces](../../abap-glossary/abenbadi_interface_glosry.md) and `GET BADI` is executed within an internal session for multiple of these BAdIs, multiple BAdI objects can point to the same object plug-in. This enables the sharing of data between different BAdIs. For context-free BAdIs, this is only the case for reuse. For context-dependent BAdIs, multiple BAdI objects from the same context can point to the same object plug-ins.

### Hints

- The fact that object plug-ins can either be newly generated or reused can also be expressed in terms of an object plug-in being stateful or stateless with reference to a BAdI or a context.

- The tag interface `IF_BADI_CONTEXT` can be implemented by any class. Possible applications range from the implementation in a local class without other components that have the sole purpose of enabling internal program context administration for BAdIs, to the implementation in a global application class in which the objects are specifically enhanced.

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_BADI_CONTEXT_ERROR`

- *Cause:* A context error has occurred in the dynamic variant of the statement.

`CX_BADI_FILTER_ERROR`

- *Cause:* Incorrect information was specified for the filters of the BAdI in the dynamic variant of the statement.

`CX_BADI_INITIAL_CONTEXT`

- *Cause:* The reference variable specified after `CONTEXT` is initial.

`CX_BADI_MULTIPLY_IMPLEMENTED`

- *Cause:* Multiple BAdI implementation classes were found, although the BAdI is defined for single use. Subclass of `CX_BADI_NOT_SINGLE_USE`.

`CX_BADI_NOT_IMPLEMENTED`

- *Cause:* No BAdI implementation class was found, although the BAdI is defined for single use. Subclass of `CX_BADI_NOT_SINGLE_USE`.

`CX_BADI_UNKNOWN_ERROR`

- *Cause:* The BAdI specified in the dynamic variant of the statement does not exist.
