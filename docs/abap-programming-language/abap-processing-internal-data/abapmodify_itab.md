---
title: "MODIFY itab"
source_file: abapmodify_itab.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MODIFY itab

## Syntax

``` abap
MODIFY { itab_line | itab_lines }.  
```

[`itab_line`](abapmodify_itab_single.md) · [`itab_lines`](abapmodify_itab_multiple.md)

## Description

This statement changes the content either of a single line [`itab_line`](abapmodify_itab_single.md) or multiple lines [`itab_lines`](abapmodify_itab_multiple.md), which can be specified using a table key or a table index.

The following restrictions apply with respect to modifications to key fields of the [primary](../../abap-glossary/abenprimary_table_key_glosry.md) and [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md):

- The key fields of the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) of [sorted tables](../../abap-glossary/abensorted_table_glosry.md) and [hashed tables](../../abap-glossary/abenhashed_table_glosry.md) are read-only and must not be modified, since this would invalidate internal table administration. The processing statements for internal tables check whether writes are performed on individual key fields and a corresponding attempt raises an uncatchable exception. If writes are performed in write positions across the entire table line, for example, as a target field of assignments or as actual parameters for output parameters, an exception is always raised.

- The key fields of a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md), however, are only read-only, while the secondary table is used. This is the case for [`LOOP`](abaploop_at_itab.md) and when using the [`MODIFY`](abapmodify_itab.md) statement where the secondary key is specified after `USING KEY`. Otherwise the key fields are not read-only.

The administration of unique secondary keys is updated directly after a modification using `MODIFY`, and raises a uncatchable exception if duplicate entries would otherwise be produced. The non-unique secondary keys are updated when the secondary table key is next used explicitly ([lazy update](../../abap-glossary/abenlazy_update_glosry.md)).

## System Fields

| **`sy-subrc`** | **Meaning**                                                                                                                                                                                                                   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0              | At least one line was changed.                                                                                                                                                                                                |
| 4              | No lines were changed, since no suitable line was found in the search using a table key or in the logical expression, or the specified index was greater than the current number of lines for the search using a table index. |

The system field `sy-tabix` is not set.

## Hints

- Apart from using the `MODIFY` statement, the content of an individual table line can be changed using assignments to field symbols and dereferenced data references that point to the table line.

- There is no implicit selection of a suitable key or index. The used table key or table index is always specified uniquely. A syntax check warning occurs if there is a suitable [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) available but not used. This warning should be removed by using the key. However, in exceptional cases, it can also be bypassed using a [pragma](../../abap-glossary/abenpragma_glosry.md).

- Using a special variant [`MODIFY mesh_path`](abenmesh_modify.md), lines from the last path node of a [mesh path](../../abap-glossary/abenmesh_path_glosry.md) can be changed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Modification of a line in an internal table using a [key access](abapmodify_itab_table_key.md). A line with a specific key value is read to a work area `wa` and a structure with a different value is then constructed in a non-key component after the addition [`FROM`](abapmodify_itab_single.md) of the statement `MODIFY`. The table line with the appropriate key value is then modified.

**Note:** The key access is expressed by the addition `TABLE`. Without `TABLE`, the statement would be syntactically correct within [`LOOP AT`](abaploop_at_itab_variants.md) and express an [index access](abapmodify_itab_index.md) that accesses the current line of the loop implicitly.

``` abap
DATA itab TYPE HASHED TABLE OF scarr WITH UNIQUE KEY carrid. 
 
SELECT * 
       FROM scarr 
       INTO TABLE @itab. 
 
FINAL(wa) = VALUE #( itab[ carrid = 'LH' ] OPTIONAL ). 
 
IF wa IS NOT INITIAL. 
  MODIFY TABLE itab 
         FROM VALUE #( BASE wa carrname = '...' ). 
ENDIF.
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_ITAB_DYN_LOOP`

- *Cause:* Error in a dynamic `WHERE` condition

  *Runtime error:* `DYN_WHERE_PARSE_ERROR`
