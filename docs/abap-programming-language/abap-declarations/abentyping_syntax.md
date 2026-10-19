---
title: "typing Addition"
source_file: abentyping_syntax.html
section: "ABAP Programming Language > ABAP - Declarations > Typing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# typing Addition

## Syntax

``` abap
... generic_type | complete_type  ...  
```

[`generic_type`](abentyping_generic.md) · [`complete_type`](abentyping_complete.md)

## Description

The addition `typing` is part of the definition of formal parameters and field symbols in the following statements:

- [`[CLASS-]METHODS`](abapmethods.md)

- [`[CLASS-]EVENTS`](abapevents.md)

- [`FORM`](../abap-obsolete-language-elements/abapform.md)

- [`FIELD-SYMBOLS`](abapfield-symbols.md)

The addition allows generic typing with [`generic_type`](abentyping_generic.md) and complete typing with [`complete_type`](abentyping_complete.md). In positions where the addition `typing` does not have to be specified, implicit typing with the generic type [`any`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) takes place if no typing is specified explicitly.

## Hints

- For more information about typing parameters of function modules, see [Function Module Interface](../abap-program-structure/abenfunction_parameters.md).

- When formal parameters are typed, the addition `LIKE` can be used to reference formal parameters of the same procedure that have already been declared.
