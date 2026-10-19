---
title: "FORM, parameters"
source_file: abapform_parameters.html
section: "ABAP Programming Language > ABAP - Obsolete Language Elements > Obsolete Modularization > Subroutines > FORM"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FORM, parameters

## Obsolete, deprecated Syntax

``` abap
... { VALUE(p1) | p1 } [`typing`|`structure`]   
    { VALUE(p2) | p2 } [`typing`|`structure`]   
    ...  
```

[`typing`](../abap-declarations/abentyping_syntax.md) · [`structure`](abapform_structure.md) · [`typing`](../abap-declarations/abentyping_syntax.md) · [`structure`](abapform_structure.md)

**Caution**

***This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.***

## Description

Defines the formal parameters `p1 p2 ...` for subroutines.

The addition `typing` types a formal parameter `p1 p2 ...`. The syntax of `typing` is described in [Typing](../abap-declarations/abentyping_syntax.md). The typing of a formal parameter causes the data type to be [checked](../abap-declarations/abentyping_check.md) against the typing when an actual parameter is passed. In addition, the typing specifies at which operand positions the formal parameter can be used in the subroutine. If no explicit typing is specified, a formal parameter is typed with the fully generic type `any`.

`VALUE` can be used to specify how [values are passed](../../abap-glossary/abenpass_by_value_glosry.md) for a formal parameter `p1 p2 ...`. If `VALUE` is not specified, values are [passed by reference](../../abap-glossary/abenpass_by_reference_glosry.md).

The addition [`structure`](abapform_structure.md) can also be used to implement an obsolete form of typing.

## Hint

Without an explicit typing, a formal parameter is typed implicitly with the fully generic type `any`.
