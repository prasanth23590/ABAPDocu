---
title: "INSERT itab"
source_file: abapinsert_itab.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INSERT itab

## Syntax

``` abap
INSERT line_spec INTO itab_position [result].  
```

[`line_spec`](abapinsert_itab_linespec.md) · [`itab_position`](abapinsert_itab_position.md) · [`result`](abapinsert_itab_result.md)

## Description

This statement adds one or more lines [`line_spec`](abapinsert_itab_linespec.md) at a position [`itab_position`](abapinsert_itab_position.md) in an internal table. The position can be specified using the primary table key or a table index. [`result`](abapinsert_itab_result.md) can be used when appending a single line to set a reference to the appended line in the form of a field symbol or a data reference.

When the line is inserted, all existing unique table keys are checked. These can be a unique [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) and multiple unique [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md). The system handles any duplicates of the different keys according to the following hierarchy:

1.  If attempting to insert a single line using a primary key would produce duplicates with respect to the unique primary key, no line is inserted and `sy-subrc` is set to 4.

2.  If attempting to insert a single line using the key or the index would result in duplicates with respect to a unique secondary key, a catchable exception of the class `CX_SY_ITAB_DUPLICATE_KEY` is raised.

3.  If attempting to insert a single line using an index or multiple lines as a block would result in duplicates with respect to a unique primary or secondary key, a runtime error occurs.

## System Fields

| **`sy-subrc`** | **Meaning**                                                                                                                                                                                                                                                      |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0              | One or more lines were inserted.                                                                                                                                                                                                                                 |
| 4              | No line was inserted because either a line with the same unique key already existed when inserting single lines using the primary key or the specified index was greater than the current number of lines plus 1 when inserting the lines using the table index. |

The system field `sy-tabix` is not set.

## Hints

- The [value operator](../../abap-glossary/abenvalue_operator_glosry.md) [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) can also be used to [construct](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md) the content of internal tables.

- A special variant [`INSERT mesh_path`](abenmesh_insert.md) can be used to insert lines into the last node of a [mesh path](../../abap-glossary/abenmesh_path_glosry.md).

- The administration of an unique secondary table key is updated immediately ([direct update](../../abap-glossary/abendirect_update_glosry.md)) and the administration of a non-unique secondary table key is updated at the next explicit use of the secondary table key ([lazy update](../../abap-glossary/abenlazy_update_glosry.md)). Runtime costs for creating or updating a non-unique secondary table key are not incurred therefore until it is used for the first time.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Insertion of single lines into a [standard table](../../abap-glossary/abenstandard_table_glosry.md) `int_tab` using the table index and insertion of references to these lines in a [hashed table](../../abap-glossary/abenhashed_table_glosry.md) `ref_tab` using the table key. The output in the [`LOOP`](abaploop_at_itab.md) loops produces the numbers 10 to 1 for `int_tab` and the numbers 1 to 10 for `ref_tab`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES intref type REF TO i. 
 
DATA: int_tab TYPE STANDARD TABLE OF i, 
      ref_tab TYPE HASHED TABLE OF intref 
              WITH UNIQUE KEY table_line. 
 
DO 10 TIMES. 
  INSERT sy-index 
         INTO int_tab INDEX 1 
         REFERENCE INTO DATA(dref). 
  INSERT dref 
         INTO TABLE ref_tab. 
ENDDO. 
 
out->begin_section( `Integer Table` ). 
LOOP AT int_tab INTO FINAL(int). 
  out->write( |{ int }| ). 
ENDLOOP. 
out->next_section( `Reference Table` ). 
LOOP AT ref_tab INTO dref. 
  out->write( |{ dref->* }| ). 
ENDLOOP. 
 
out->display( ).
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_ITAB_DUPLICATE_KEY`

- *Cause:* Duplicate key values in unique secondary key

  *Runtime error:* `ITAB_DUPLICATE_KEY`
