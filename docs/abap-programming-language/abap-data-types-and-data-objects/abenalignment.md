---
title: "Alignment of Data Objects"
source_file: abenalignment.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Alignment of Data Objects

Data objects with certain data types cannot be stored in random addresses in the main memory:

- [Numeric data objects](../../abap-glossary/abennumeric_data_object_glosry.md)

  The memory address of ABAP fields with the following numeric types must be divisible as follows:

  - `s` by 2

  - `i` by 4

  - `int8`, `decfloat16`, `f` by 8

  - `decfloat34` by 16

- [Character-like data objects](../../abap-glossary/abencharlike_data_object_glosry.md)

  The memory address of character-like data objects must be divisible by 2 for the character representation [UCS-2](../../abap-glossary/abenucs2_glosry.md) used by the ABAP programming language.

- [Time stamp fields](../../abap-glossary/abentimestamp_field_glosry.md)

  The memory address of time stamp fields of the type `utclong` must be divisible by eight.

- [Deep data objects](../../abap-glossary/abendeep_glosry.md)

  The memory address of deep data objects such as strings or reference variables must be divisible by 4.

An elementary data object is aligned when it has an address that corresponds to its data type.

- A structure is aligned if:

  - Its start address meets the strictest alignment requirements of its components and

  - The [offsets](../../abap-glossary/abenoffset_glosry.md) of all components meet the same type-specific divisibility requirements.

Normally, the correct alignment of data objects is not normally an issue, because they are automatically created correctly during declaration. This can cause [alignment gaps](../../abap-glossary/abenalignment_gap_glosry.md) in structures with components of different data types.

However, correct alignment must be checked in the following cases:

- In assignments and comparisons of structures where the [structure fragment view](../../abap-glossary/abenunicode_fragment_view_glosry.md) that splits a structure into fragments in accordance with its alignment gaps must be considered.

- When a data object is handled using explicit or implicit [casting](../../abap-glossary/abencast_casting_glosry.md) with a different data type.

- When a work area that has a different type from the database table is used in an [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statement.

If a statement expects a specific alignment of a data object, an exception is raised when there is insufficient alignment.

## Hints

- Components that are included in structures using [`INCLUDE TYPE|STRUCTURE`](../abap-declarations/abapinclude_type.md) behave like real [substructures](../../abap-glossary/abensubstructure_glosry.md) in regard to alignment.

- The binary content of alignment gaps is not defined and must not be evaluated.

- Trailing alignment gaps can also occur at the end of structures, since the overall length of the structure is determined by the component with the largest alignment requirement.

- Alignment gaps are part of the length of a structure.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following alignment gaps (A) appear in the following structure:

\[a \| A \| b \| A \| cccccccccccc \| A \| dddd\]

The first alignment gap is constructed as a result of the alignment of the substructure `struc2`, the second gap due to the alignment of the component `c` of type `c`, and the third due to the component `d` of type `i`.

``` abap
DATA: 
  BEGIN OF struc1, 
    a TYPE x LENGTH 1, 
    BEGIN OF struc2, 
      b TYPE x LENGTH 1, 
      c TYPE c LENGTH 6, 
    END OF struc2, 
    d    TYPE i, 
  END OF struc1.
```
