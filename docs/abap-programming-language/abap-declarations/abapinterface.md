---
title: "INTERFACE"
source_file: abapinterface.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INTERFACE

## Syntax Forms

**[Declaration of Interfaces](abapinterface_definition.md)**

``` abap
1. INTERFACE intf [PUBLIC]. 
    [components] 
  ENDINTERFACE.
```

**[Deferred Interfaces](abapinterface_deferred.md)**

``` abap
2. INTERFACE intf DEFERRED [PUBLIC].
```

[`components`](abeninterface_component.md)

## Description

The statement `INTERFACE` defines [interfaces](../../abap-glossary/abenoo_intf_glosry.md) in ABAP Objects or defers their declaration.

- The definition of an interface consists of a [declaration section](abapinterface_definition.md) that starts with `INTERFACE` and is closed using `ENDINTERFACE`. Unlike classes, an interface does not have an implementation part.

- The variant of `INTERFACE` without `ENDINTERFACE` is used for [deferring interfaces](abapinterface_deferred.md) in a program.

The statements `INTERFACE` and associated statements `ENDINTERFACE` can only be specified in the global context of a program. `INTERFACE` and `ENDINTERFACE` cannot be specified within classes, procedures,. This applies in particular to the variant of `INTERFACE` specified here, which is not closed using `ENDINTERFACE`.

## Hints

- The definition or deferral of an interface is handled like other declaration statements (`DATA`, `TYPE`, ...). In a processing block without a local context, they are handled like global program declarations and do not close the processing block.
