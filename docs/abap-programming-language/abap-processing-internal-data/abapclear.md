---
title: "CLEAR"
source_file: abapclear.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Initializations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLEAR

## Syntax

``` abap
CLEAR dobj [ {WITH val [IN {CHARACTER|BYTE} MODE] } 
 ].  
```

### Addition

[`... WITH val [IN {CHARACTER|BYTE} MODE]`](abapclear.md#addition)

## Overview

### Description

Without the optional additions, `dobj` is assigned the type-dependent [initial value](../../abap-glossary/abeninitial_value_glosry.md). `dobj` is a [result position](../../abap-glossary/abenresult_position_glosry.md), that is, either a variable or a [writable expression](../../abap-glossary/abenwritable_expression_glosry.md) can be specified.

- Elementary data objects are assigned initial values in accordance with the [tables](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) of [built-in ABAP types](../../abap-glossary/abenbuiltin_abap_type_glosry.md).

- [Enumerated variables](../../abap-glossary/abenenumerated_variable_glosry.md) are assigned to initial values in accordance with the elementary [base type](../../abap-glossary/abenbase_type_glosry.md).

- Reference variables are assigned the [null reference](../../abap-glossary/abennull_reference_glosry.md).

- Structures are set to their initial values component by component.

- All lines of an internal table are deleted. The memory space required for the lines of the table is released except the [initial memory requirement](../../abap-glossary/abeninitial_mem_req_glosry.md). The statement [`FREE`](abapfree_dataobject.md) can be used for releasing also the initial memory requirement if necessary.

The optional additions enable `dobj` to be filled with values other than the initial value.

### Hints

- If `dobj` is an internal table with a [header line](../../abap-glossary/abenheader_line_glosry.md), `dobj[]` must be specified to delete the lines, otherwise only the header line is deleted.

- In the case of `CLEAR`, the initial memory request of an internal table is not released, which can have a positive effect on performance when inserting new lines in the internal table. The statement [`FREE`](abapfree_dataobject.md) is required only if as much memory as possible needs to be released.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After initialization with `CLEAR`, the internal table `itab` no longer contains any lines.

``` abap
DATA itab TYPE STANDARD TABLE OF i WITH EMPTY KEY. 
 
itab = VALUE #( FOR i = 1 UNTIL i > 10 ( i ) ). 
ASSERT lines( itab ) = 10. 
 
CLEAR itab. 
ASSERT lines( itab ) = 0.
```

## Addition

`... WITH val [IN {CHARACTER|BYTE} MODE]`

### Description

If the addition `WITH val` is used and `CHARACTER` or `BYTE MODE` specified, all places in `dobj` are replaced either with the first character or the first byte in `val`. `val` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md). If `dobj` is of the type `string` or `xstring`, the string is processed in its current length.

If the `MODE` addition is not specified, the addition `IN CHARACTER MODE` applies. Depending on the addition, the data object `dobj` must be either character-like or byte-like. Depending on the addition, the operand `val` must be character-like or byte-like and have the length 1. If this is not the case, a syntax error occurs, or a uncatchable exception is raised.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The byte string `hexstring` is assigned a specific byte value across the entire current length.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: hexstring TYPE xstring, 
      hex       TYPE x LENGTH 1 VALUE 'FF'. 
... 
hexstring = '00000000'. 
... 
CLEAR hexstring WITH hex IN BYTE MODE. 
 
out->write( hexstring ). 
 
out->display( ).
```
