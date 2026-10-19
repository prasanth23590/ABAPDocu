---
title: "APPEND"
source_file: abapappend.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# APPEND

## Syntax

``` abap
APPEND line_spec TO itab [SORTED BY comp] [result].  
```

[`line_spec`](abapappend_linespec.md) · [`result`](abapappend_result.md)

### Addition

[`... SORTED BY comp`](abapappend.md#addition)

## Overview

### Description

This statement appends one or more lines [`line_spec`](abapappend_linespec.md) to an internal index table `itab`. It is appended so that a new last line is created with regard to the primary table index.

If `itab` is a [standard table](../../abap-glossary/abenstandard_table_glosry.md), `SORTED BY` can be used to sort the table in a specified way. [`result`](abapappend_result.md) can be used when inserting a single line to set a reference to the inserted line in the form of a field symbol or a data reference.

For the individual table types, appending is done as follows:

- To standard tables, lines are appended directly and without checking the content of the internal table.

- Lines are appended to [sorted tables](../../abap-glossary/abensorted_table_glosry.md) only if they match the sort order and do not create duplicate entries if the primary table key is unique.

- No lines can be appended to [hashed tables](../../abap-glossary/abenhashed_table_glosry.md).

Exceptions are raised in the following cases:

- If a line to be appended would produce a duplicate entry in a unique primary table key, an uncatchable exception is raised.

- If a line to be appended would produce a duplicate entry in a unique secondary table key, a catchable exception of the class `CX_SY_ITAB_DUPLICATE_KEY` is raised.

- If a block of lines to be appended would produce a duplicate entry in a unique secondary table key, an uncatchable exception is raised.

- If a line to be appended would destroy the sort sequence of sorted tables, an uncatchable exception is raised (the secondary index of a sorted secondary key, however, is updated before it is used again).

### System Fields

The statement `APPEND` sets `sy-tabix` to the line number of the last appended line in the primary table index.

### Hints

- The administration of a unique secondary table key is updated immediately; the administration of a non-unique key is not updated until the secondary table key is next used explicitly (lazy update). Runtime costs for creating or updating a non-unique secondary table key are not incurred therefore until it is used for the first time.

- The [value operator](../../abap-glossary/abenvalue_operator_glosry.md) [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) can also be used to [construct](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md) the content of internal tables.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

100 random numbers are appended to the internal table `itab` with line type `i`.

``` abap
DATA itab TYPE TABLE OF i WITH EMPTY KEY. 
 
FINAL(rnd) = cl_abap_random_int=>create( 
  seed =  CONV #( cl_demo_date_time=>get_utc_time( ) ) 
  min  = 1 
  max  = 100 ). 
 
DO 100 TIMES. 
  APPEND rnd->get_next( ) TO itab. 
ENDDO.
```

## Addition

`... SORTED BY comp`

### Description

If used correctly, this addition can produce ranking lists in descending order. This only works if a value greater than 0 is specified in the declaration of the internal table in the addition [`INITIAL SIZE`](../abap-declarations/abaptypes_itab.md). If the value 0 is specified for `INITIAL SIZE`, the statement `APPEND` is ignored when used with the addition `SORTED BY`.

The addition `SORTED BY` can be used only when a work area `wa` is specified and for a standard table. `wa` must also be [compatible](../../abap-glossary/abencompatible_glosry.md) with the line type of the table. The component `comp` can be specified as shown in the section [Specifying Components](abenitab_components.md), however, only a single component can be addressed using the object component selector, and no attributes of classes.

Provided that the declaration of the internal table for `INITIAL SIZE` has a value greater than zero, the statement is executed in two steps:

- Starting from the final line, the table is searched for a line in which the value of the component `comp` is greater than or equal to the value of the component `comp` of `wa`. If a line like this exists, the work area `wa` is inserted after this line with respect to the primary index. In no such line is found, the work area `wa` is inserted in front of the first line with respect to the primary index. The line numbers of all lines after the inserted line are increased by 1 in the primary table index.

- If the number of lines before the statement is executed is greater than or equal to the number specified in the declaration of the internal table in the addition `INITIAL SIZE`, the new final line is deleted with respect to the primary table index.

When using only the statement `APPEND` with the addition `SORTED BY` to fill an internal table with a value no greater than 0 for `INITIAL SIZE`, this rule produces an internal table that contains as many lines as specified in its definition after `INITIAL SIZE` and that is sorted in descending order with respect to the primary table index by component `comp` (ranking list).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of a ranking of the three flights of a connection showing the most free seats.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: carrid TYPE sflight-carrid VALUE 'LH', 
      connid TYPE sflight-connid VALUE '0400'. 
cl_demo_input=>new( 
  )->add_field( CHANGING field = carrid 
  )->add_field( CHANGING field = connid )->request( ). 
 
DATA: BEGIN OF seats, 
        fldate    TYPE sflight-fldate, 
        seatsocc  TYPE sflight-seatsocc, 
        seatsmax  TYPE sflight-seatsmax, 
        seatsfree TYPE sflight-seatsocc, 
      END OF seats. 
 
DATA seats_tab LIKE STANDARD TABLE OF seats 
               INITIAL SIZE 3. 
 
SELECT fldate, seatsocc, seatsmax, seatsmax - seatsocc AS seatsfree 
       FROM sflight 
       WHERE carrid = @carrid AND 
             connid = @connid 
       INTO @seats. 
  APPEND seats TO seats_tab SORTED BY seatsfree. 
ENDSELECT. 
 
out->write( seats_tab ). 
 
out->display( ).
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_ITAB_DUPLICATE_KEY`

- *Cause:* Duplicate key values in unique secondary key

  *Runtime error:* `ITAB_DUPLICATE_KEY`
