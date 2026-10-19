---
title: "ABAP Objects - Interface Parameters in Methods"
source_file: abenmethod_parameters.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Classes > ABAP Objects - Components of Classes > ABAP Objects - Methods of Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Interface Parameters in Methods

The interface parameters in methods are input parameters (`IMPORTING` and `CHANGING` parameters) and output parameters (`EXPORTING`, `CHANGING`, and `RETURNING` parameters). Declarations using the statements

- [`METHODS`](../abap-declarations/abapmethods.md)

- [`CLASS-METHODS`](../abap-declarations/abapclass-methods.md)

- [`EVENTS`](../abap-declarations/abapevents.md)

- [`CLASS-EVENTS`](../abap-declarations/abapclass-events.md)

define the following attributes:

## Passing Parameters by Reference or by Value

With the exception of the return value (`RETURNING` parameters), parameters can be passed both by value and by reference. Passing by reference is the default in methods. If only a name `p` is specified in the parameter declaration, the parameter is passed implicitly as a reference. If `VALUE(p)` is specified instead, the parameter is passed as a value. The return value may only be passed as a value. Pass by reference can also be specified explicitly in other parameters using `REFERENCE(p)`. An `IMPORTING` parameter passed by reference cannot be modified in the method.

## Typing of Parameters

All parameters must be [typed](../../abap-glossary/abentyping_glosry.md) when declared using `TYPE` or `LIKE` additions.

## Optional Parameters

All input parameters (`IMPORTING` and `CHANGING` parameters) can be defined in the declaration as optional parameters using the additions `OPTIONAL` or `DEFAULT`. These parameters then do not always have to be transferred when the method is called. The parameter remains initial and type-compliant when the addition `OPTIONAL` is specified, whereas the addition `DEFAULT` makes it possible to specify a [start value](../../abap-glossary/abenstart_value_glosry.md).
