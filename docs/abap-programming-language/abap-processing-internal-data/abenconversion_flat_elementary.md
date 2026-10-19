---
title: "Conversion Between Flat Structures and Single Fields"
source_file: abenconversion_flat_elementary.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Structures"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Conversion Between Flat Structures and Single Fields

The following rules apply when converting a [flat](../../abap-glossary/abenflat_glosry.md) structure to a single field and vice versa:

- If a structure is purely character-like, it is handled like a data object of the type `c` (casting) during conversion. The single field can have any elementary data type, except for an [enumerated type](../../abap-glossary/abenenum_type_glosry.md).

- If the structure is not completely character-like, the single field must have the type `c` and the structure must begin with a character-like [fragment](abenunicode_fragment_view.md) that is at least as long as the single field. The assignment takes place only between this fragment and the single field. The character-like fragment of the structure is handled like a data object of the type `c` (casting) during assignment. If the structure is the target field, the remaining character-like fragments are filled with blanks and all other components with the type-dependent [initial value](../../abap-glossary/abeninitial_value_glosry.md).

No conversion rule is defined for any other cases, and assignments are not possible.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conversion of the character-like `abcde` to a flat structure of character-like components. After this, each component contains a letter.

``` abap
TYPES: 
  BEGIN OF characters, 
    a TYPE c LENGTH 1, 
    b TYPE c LENGTH 1, 
    c TYPE c LENGTH 1, 
    d TYPE c LENGTH 1, 
    e TYPE c LENGTH 1, 
    f TYPE c LENGTH 1, 
    g TYPE c LENGTH 1, 
    h TYPE c LENGTH 1, 
    i TYPE c LENGTH 1, 
    j TYPE c LENGTH 1, 
    k TYPE c LENGTH 1, 
    l TYPE c LENGTH 1, 
    m TYPE c LENGTH 1, 
    n TYPE c LENGTH 1, 
    o TYPE c LENGTH 1, 
    p TYPE c LENGTH 1, 
    q TYPE c LENGTH 1, 
    r TYPE c LENGTH 1, 
    s TYPE c LENGTH 1, 
    t TYPE c LENGTH 1, 
    u TYPE c LENGTH 1, 
    v TYPE c LENGTH 1, 
    w TYPE c LENGTH 1, 
    x TYPE c LENGTH 1, 
    y TYPE c LENGTH 1, 
    z TYPE c LENGTH 1, 
  END OF characters. 
 
FINAL(abcde) = 'abcdefghijklmnopqrstuvwxyz'. 
FINAL(result) = CONV characters( abcde ).
```
