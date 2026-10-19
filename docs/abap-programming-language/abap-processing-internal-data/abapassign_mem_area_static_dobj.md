---
title: "ASSIGN, static_dobj"
source_file: abapassign_mem_area_static_dobj.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Field Symbols > ASSIGN > ASSIGN, mem_area"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ASSIGN, static_dobj

## Syntax

``` abap
... dobj[+off][(len)]  ...  
```

## Description

Static variant for specifying the memory area [`mem_area`](abapassign_mem_area.md) of the statement [`ASSIGN`](abapassign.md). In the static variant, a data object `dobj` with an optional offset/length `+off(len)` can be specified in accordance with the rules described in the section [Data Objects in Operand Positions](../abap-operands/abenoperands_data_objects.md), with the following exception: A data reference dereferenced using the dereferencing operator -\>\* belongs to the [dynamic variants](abapassign_mem_area_dynamic_dobj.md). `dobj` specified using a field symbol, on the other hand, is a static variant.

The memory area is determined by the specified offset/length `+off(len)` as follows:

- If no offset/length specification is made, the assigned memory area corresponds exactly to the memory area of the data object. The entire data object `dobj` is assigned to the field symbol, and statements that contain the field symbol in operand positions work with the data object.

- If an offset/length is specified, the memory area is determined from the memory address of the data object and the offset/length specifications. The general rules for [substring accesses](../abap-operands/abenoffset_length.md) apply. If these are met, memory outside the `dobj` field limits can also be addressed. The addressable memory is based on the specification [`range_spec`](abapassign_range.md). If an offset `off` is specified without a length `len`, the length of the data object `dobj` is used implicitly for `len`. If a field symbol is specified for `dobj`, to which a memory area is already assigned, the content of the offset specification can be negative, as long as the area specified in `range_spec` is not exited. The following restrictions apply when offsets/lengths are specified:

  - No inline declaration of a field symbol with [`FIELD-SYMBOL(<fs>)`](../abap-declarations/abenfield-symbol_inline.md) can be made.

  - The data type of `dobj` cannot be `string` or `xstring`, which means that `len` can never be less than or equal to zero.

  - If the name of a data object is specified for `dobj` and if no explicit [`RANGE`](abapassign_range.md) addition is used, no offset `off` can be specified without the length `len`. If the name of a field symbol is specified for `dobj`, its data type must be [flat](../../abap-glossary/abenflat_glosry.md) and elementary whenever an offset `off` is specified without length `len`.

The return code `sy-subrc` is not set for this variant. If the assignment is not successful, no memory area is assigned to the field symbol after the `ASSIGN` statement. The addition [`ELSE UNASSIGN`](abapassign_else_unassign.md) is used implicitly and cannot be specified.

In an inline declaration of the field symbol with [`FIELD-SYMBOL(<fs>)`](../abap-declarations/abenfield-symbol_inline.md), this symbol is typed with the exact data type that can be determined statically for `mem_area`. If `mem_area` is a generically typed field symbol or a generically typed formal parameter, the generic type is used.

## Hints

- Ensure that the system field `sy-subrc` is not evaluated by mistake after the static variant. The value of the system field in this case is always the same as it was before the `ASSIGN` statement was executed and therefore does not indicate whether the statement was successful.

- In order to check the success of the assignment, the [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md) [`<fs> IS ASSIGNED`](../abap-program-flow-logic/abenlogexp_assigned.md) can be used.

- Even the static variant is dynamic in the sense that the offset and length specifications may be dynamic. However, dynamic offset/length specifications do not lead to the system field `sy-subrc` being set.

- If a generically typed field symbol or a generically typed formal parameter is specified for `dobj`, its current type at runtime determines the behavior, for example whether offsets/lengths can be specified or not.

- In the `ASSIGN` statement, the special rule that offset/length specifications that address the complete data object are omitted does not apply.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Assignment of the memory area of the individual characters of a data object `text` to a field symbol `<char>`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA text TYPE c LENGTH 10 VALUE '0123456789'. 
 
FIELD-SYMBOLS <char> TYPE c. 
 
DATA off TYPE i. 
 
DO 10 TIMES. 
  off = sy-index - 1. 
  ASSIGN text+off(1) TO <char>. 
  out->write_text( |{ <char> }| ). 
ENDDO. 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A field symbol `<fs1>` points to the component `col1` of the structure `struct`. In the first assignment of `<fs1>` to a field symbol `<fs2>`, an offset without length is specified and therefore the length 10 of the component `col1` is used implicitly. This assignment is not possible, since the assigned memory area is outside of the allowed range. In the second assignment, the allowed memory area is expanded to the entire structure using the assignment [`RANGE`](abapassign_range.md) and the assignment is successful.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: 
  BEGIN OF struct, 
    col1 TYPE c LENGTH 10 VALUE 'aaaaaaaaaa', 
    col2 TYPE c LENGTH 10 VALUE 'bbbbbbbbbb', 
  END OF struct. 
 
FIELD-SYMBOLS: <fs1> TYPE c, 
               <fs2> TYPE c. 
 
ASSIGN struct-col1 TO <fs1>. 
ASSIGN <fs1>+5 TO <fs2>. 
IF <fs2> IS NOT ASSIGNED. 
  out->write( `No assignment without sufficient RANGE` ). 
ENDIF. 
ASSIGN <fs1>+5 TO <fs2> RANGE struct. 
IF <fs2> IS ASSIGNED. 
  out->write( `Assignment with sufficient RANGE` ). 
ENDIF. 
 
out->display( ).
```
