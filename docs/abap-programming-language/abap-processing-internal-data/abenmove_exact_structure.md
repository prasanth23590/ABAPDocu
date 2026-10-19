---
title: "Checking Structures"
source_file: abenmove_exact_structure.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Lossless Assignments > Lossless Assignments, Rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Checking Structures

The operator [`EXACT`](abenconstructor_expression_exact.md) can only be used to convert structures to [compatible](../abap-data-types-and-data-objects/abencompatibility.md) structures. Full compatibility is not required for the following deep components, for which the specified requirements apply:

- For components that have a [reference type](../../abap-glossary/abenreference_type_glosry.md), [upcasts](../../abap-glossary/abenup_cast_glosry.md) but not [downcasts](../../abap-glossary/abendown_cast_glosry.md) are allowed.

- For table-like components, it is sufficient if the [line type](../../abap-glossary/abenrow_type_glosry.md) is compatible. This means that the full [compatibility](../abap-data-types-and-data-objects/abencompatibility.md), which includes [table categories](../../abap-glossary/abentable_category_glosry.md) and [table keys](../../abap-glossary/abentable_key_glosry.md), is not required here.

## Hints

- The operator `EXACT` ensures that the [conversion rules](abenconversion_struc.md) for flat structures are the same as those for deep structures. It is not possible to make conversions between structures and elementary data objects.

- If the structured types are compatible, no further checks are performed on the content. If the source structure already contains invalid data, this data is assigned to a compatible return value despite the addition `EXACT`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Unlike simple conversion, the lossless assignment leads to a syntax error.

``` abap
DATA: 
  BEGIN OF struc, 
    col1 TYPE d, 
    col2 TYPE t, 
  END OF struc. 
 
DATA(result1) = CONV string( struc ).  "Possible 
 
DATA(result2) = EXACT string( struc ). "Not possible
```
