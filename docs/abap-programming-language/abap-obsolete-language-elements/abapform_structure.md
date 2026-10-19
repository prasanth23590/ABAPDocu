---
title: "FORM, STRUCTURE"
source_file: abapform_structure.html
section: "ABAP Programming Language > ABAP - Obsolete Language Elements > Obsolete Modularization > Subroutines > FORM"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FORM, STRUCTURE

## Obsolete, deprecated Syntax

``` abap
... STRUCTURE struc ...  
```

**Caution**

***This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.***

## Description

A formal parameter `p1 p2 ...` of a subroutine can be specified with the addition `STRUCTURE` instead of [`typing`](../abap-declarations/abentyping_syntax.md), where `struc` must be a program-local structure (data object, no data type) or a [flat structure](../../abap-glossary/abenflat_structure_glosry.md) from the ABAP Dictionary. This structure is then applied to the formal parameter ([casting](../../abap-glossary/abencast_casting_glosry.md)) and individual components can be accessed in the subroutine.

When an actual parameter is passed to a formal parameter typed using `STRUCTURE`, the actual parameter must be at least as long as the formal parameter:

- In the case of a structured actual parameter, its [fragment view](../../abap-glossary/abenunicode_fragment_view_glosry.md) must match the fragment view of the corresponding initial part of `struc`.

- An elementary actual parameter must be character-like and flat and the corresponding initial part of `struc` can contain only components of this type.

## Hint

Formal parameters typed with `STRUCTURE` can usually be replaced by formal parameters typed with `TYPE` or `LIKE`. If a casting is necessary, generic formal parameters should be used and assigned to field symbols using the statement [`ASSIGN`](../abap-processing-internal-data/abapassign.md) and the addition `CASTING`.
