---
title: "FIND, section_of"
source_file: abapfind_section_of.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing > FIND"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FIND, section_of

## Syntax

``` abap
... SECTION [OFFSET off] [LENGTH len] OF ...  
```

## Description

This addition restricts the search of the statements [`FIND`](abapfind.md) and [`REPLACE`](abapreplace_in_pattern.md) in `dobj` to the section from the [offset](../../abap-glossary/abenoffset_glosry.md) specified in `off` with the length specified in `len`. Without the addition `SECTION`, the entire data object is searched. With `SECTION`, at least one of the additions `OFFSET` or `LENGTH` must be specified. If an offset is specified without specifying the length, the data object `dobj` is searched from the offset `off` to its end. If a length is specified but no offset, the offset 0 is used implicitly.

`off` and `len` are [numeric expression positions](../../abap-glossary/abennumerical_expr_position_glosry.md) with the operand type `i`. Apart from one exception, the values of `off` and `len` must be greater than or equal to 0 and the section specified by `off` and `len` must be within the length of `dobj`. As an exception, the value of `len` can also be `-1` and this value has the same effect as omitting the addition `LENGTH`.

## Hint

The specification `-1` for `len` works in the same way as not using the addition `LENGTH` by passing a value to the statement.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The `FIND` statement searches from offset 12 and finds the *html* substring at offset 20.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FIND 'html' IN SECTION OFFSET 12 
            OF `<html><body>This is html</body></html>` 
            MATCH OFFSET FINAL(moff). 
out->write( moff ). 
 
out->display( ).
```
