---
title: "FREE"
source_file: abapfree_dataobject.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Initializations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FREE

## Syntax

``` abap
FREE dobj.  
```

## Description

The statement `FREE` deletes all lines from an internal table and releases the complete memory area that was occupied by the lines, including the [initial memory requirement](../../abap-glossary/abeninitial_mem_req_glosry.md).

On other data objects, `FREE` works like the statement [`CLEAR`](abapclear.md).

If `dobj` is a structure with tabular components, the memory of all the tabular components is released.

## Hints

- If `dobj` is an internal table with a [header line](../../abap-glossary/abenheader_line_glosry.md), `FREE` only affects the [table body](../../abap-glossary/abentable_body_glosry.md) and not the header line.

- Unlike `CLEAR`, the [initial memory requirement](../../abap-glossary/abeninitial_mem_req_glosry.md) does not remain occupied when `FREE` is used. This can become necessary when there is a lack of memory.

- In general, `FREE` should only be used if the entire memory is to be released completely and the internal table is no longer needed or at the least not filled again immediately.

- See also [Memory Requirements of Deep Data Objects](../abap-data-types-and-data-objects/abenmemory_consumption_1.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

At the breakpoints in the *memory analysis* of the ABAP debugger, it can be observed that `FREE` releases more allocated bound memory than `CLEAR`. Note that in the restricted language scope breakpoints are not allowed but left here as comments for more clarity.

``` abap
DATA itab TYPE STANDARD TABLE OF i WITH EMPTY KEY 
          INITIAL SIZE 10000. 
 
itab = VALUE #( FOR i = 1 UNTIL i > 10000 ( i ) ). 
 
CLEAR itab. 
*BREAK-POINT. 
 
FREE itab. 
*BREAK-POINT.
```
