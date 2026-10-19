---
title: "Structure Fragment View"
source_file: abenunicode_fragment_view.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Structures"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Structure Fragment View

The structure fragment view splits a structure into fragments. A fragment is a grouping of structure components of the same or similar data types. In nested structures, the elementary components on the lowest nesting depth are considered when forming fragments. The following parts of a structure are each grouped to form fragments:

- Consecutive [flat](../../abap-glossary/abenflat_glosry.md) character-like components of the types `c`, `n`, `d`, and `t`, between which there are no [alignment gaps](../../abap-glossary/abenalignment_gap_glosry.md), form character-like fragments.

- Consecutive flat byte-like components of the type `x`, between which there are no alignment gaps, form byte-like fragments.

- Consecutive, similar numeric components of type (`b`, `s`), `i`, `int8`, `decfloat16`, `decfloat34`, or `f`, between which there are no alignment gaps, each form a common fragment.

- Consecutive time stamp fields of the type `utclong`, between which there are no alignment gaps, form a separate fragment.

- Each individual numeric type `p` component forms a separate fragment. For this type of fragment, the length is important, but not the number of decimal places.

- In [deep](../../abap-glossary/abendeep_glosry.md) structures, each deep component (reference) forms a separate fragment.

- Each component with an [enumerated type](../../abap-glossary/abenenum_type_glosry.md) forms a separate fragment of this type.

- Each alignment gap is considered a fragment.

## Hints

- In nested structures, alignment gaps can occur before and after aligned substructures.

- When structure components are transferred using [`INCLUDE`](../abap-declarations/abapinclude_type.md), an additional alignment gap can be created in front of the included components.

- The fragment view of structures with components of type `p` can match, even when the number of decimal places in the components concerned is different.

- An [enumerated structure](../../abap-glossary/abenenumerated_structure_glosry.md) of an [enumerated type](../../abap-glossary/abenenum_type_glosry.md) is a special structure in which each component has an enumerated type and forms a separate fragment.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Structure with fragments.

``` abap
DATA: 
  BEGIN OF struc, 
    a TYPE c LENGTH 3, 
    b TYPE n LENGTH 4, 
    c TYPE d, 
    d TYPE t, 
    e TYPE decfloat16, 
    f TYPE x LENGTH 2, 
    g TYPE x LENGTH 4, 
    h TYPE i, 
    i TYPE i, 
    j TYPE i, 
    k TYPE i, 
  END OF struc.
```

The structure `struc` contains the following fragments for the character representation [UCS-2](../../abap-glossary/abenucs2_glosry.md) used by the ABAP programming language, in which character-like fields are represented by two bytes per character. Alignment gaps are marked with an *A*.

| **Fragment** | **Components**     | **Bytes** |
|--------------|--------------------|-----------|
| 1            | `a`, `b`, `c`, `d` | 6+8+16+12 |
| 2            | *A*                | 6         |
| 3            | `e`                | 8         |
| 4            | `f`, `g`           | 2+4       |
| 5            | *A*                | 2         |
| 6            | `h`, `i`, `j`, `k` | 4+4+4+4   |
