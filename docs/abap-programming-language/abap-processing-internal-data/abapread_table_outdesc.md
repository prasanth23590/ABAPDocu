---
title: "READ TABLE, result"
source_file: abapread_table_outdesc.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > READ TABLE itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# READ TABLE, result

## Syntax

``` abap
... { INTO wa [transport_options] }   
  | { ASSIGNING <fs> [CASTING] [ELSE UNASSIGN] }   
  | { REFERENCE INTO dref }   
  | { TRANSPORTING NO FIELDS } ...  
```

[`transport_options`](abapread_table_transport_options.md)

### Alternative

[1. `... INTO wa [transport_options]`](abapread_table_outdesc.md#alternative-1)

[2. `... ASSIGNING <fs> [CASTING] [ELSE UNASSIGN]`](abapread_table_outdesc.md#alternative-2)

[3. `... REFERENCE INTO dref`](abapread_table_outdesc.md#alternative-3)

[4. `... TRANSPORTING NO FIELDS`](abapread_table_outdesc.md#alternative-4)

## Overview

### Description

Defines the output behavior of a [`READ` statement](abapread_table.md) for an internal table. There are four alternatives for the output behavior:

- The addition `INTO` assigns the content of the found line to a work area. This addition can be used regardless of how `itab` is specified.

- The addition `ASSIGNING` assigns the found line to a field symbol `<fs>`. This addition is possibly only if an existing internal table is specified for `itab`.

- The addition `REFERENCE INTO` creates a reference to the found line in a reference table. This addition is possibly only if an existing internal table is specified for `itab`.

- The addition `TRANSPORTING NO FIELDS` specifies that only the relevant system fields are filled. This addition can be used regardless of how `itab` is specified.

## Alternative 1

`... INTO wa [transport_options]`

### Description

The content of the found line is assigned to the work area `wa`. The following can be specified for `wa`:

- An existing work area that matches the line type of the internal table. The line type must be compatible with or convertible to the data type of the work area. If the work area is incompatible with the line type of the internal table, the content of the table line is converted to the data type of the work area in accordance with the [conversion rules](abenconversion_rules.md).

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), where a work area with the line type of the internal table is declared. The line type must be known statically and completely.

If no line is found, `wa` remains unchanged or initial. If a conversion error occurs in the assignment to `wa`, the exception cannot be handled using `CX_SY_CONVERSION_ERROR` and the associated runtime error occurs instead.

If the additions [`transport_options`](abapread_table_transport_options.md) are used, the work area `wa` must be compatible with the line type of the internal table.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of a particular line in the internal table `sflight_tab` and assignment to a work area `sflight_wa` declared inline. After a successful assignment, the content of a component of the line is changed in the internal table.

``` abap
DATA: carrid TYPE sflight-carrid, 
      connid TYPE sflight-connid, 
      fldate TYPE sflight-fldate. 
 
... 
 
DATA sflight_tab TYPE SORTED TABLE OF sflight 
                 WITH UNIQUE KEY carrid connid fldate. 
 
SELECT * 
       FROM sflight 
       WHERE carrid = @carrid AND 
             connid = @connid 
       INTO TABLE @sflight_tab. 
 
IF sy-subrc = 0. 
  READ TABLE sflight_tab 
       WITH TABLE KEY carrid = carrid 
                      connid = connid 
                      fldate = fldate 
       INTO DATA(sflight_wa). 
  IF sy-subrc = 0. 
    sflight_wa-price *= '0.9'. 
    MODIFY sflight_tab FROM sflight_wa INDEX sy-tabix. 
  ENDIF. 
ENDIF.
```

## Alternative 2

`... ASSIGNING <fs> [CASTING] [ELSE UNASSIGN]`

### Addition

[1. `... CASTING`](abapread_table_outdesc.md#addition-1)

[2. `... ELSE UNASSIGN`](abapread_table_outdesc.md#addition-2)

### Description

The found table line is assigned to a field symbol. After the statement `READ TABLE`, the field symbol points to the table line in the memory. The addition cannot be specified if `itab` is specified as the return value or result of a [functional method](../../abap-glossary/abenfunctional_method_glosry.md), a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md), or a [table expression](../../abap-glossary/abentable_expression_glosry.md), since this value no longer exists once the statement has been executed.

The following can be specified for `<fs>`:

- An existing field symbol whose typing matches the line type of the internal table. The optional addition `CASTING` can be used to perform a casting.

- An inline declaration [`FIELD-SYMBOL(<fs>)`](../abap-declarations/abenfield-symbol_inline.md), where a field symbol with the line type of the internal table is declared. If this cannot be known statically, the field symbol is declared with the generic type `any` and is assigned the constant [`space`](../abap-built-in-types-data-objects-functions-and-constructors/abenspace.md) initially. The addition `CASTING` is not possible after an inline declaration.

If no table line is found, the state of `<fs>` depends on the addition `ELSE UNASSIGN`.

As long as the field symbol points to the line, assignments to the field symbol modify the line in the internal table. The following restrictions apply with respect to modifications to key fields of the [primary](../../abap-glossary/abenprimary_table_key_glosry.md) and [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md):

- The key fields of the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) of [sorted tables](../../abap-glossary/abensorted_table_glosry.md) and [hashed tables](../../abap-glossary/abenhashed_table_glosry.md) are read-only and must not be modified, since this would invalidate internal table administration. The processing statements for internal tables check whether writes are performed on individual key fields and a corresponding attempt raises an uncatchable exception. If writes are performed in write positions across the entire table line, for example, as a target field of assignments or as actual parameters for output parameters, an exception is always raised.

- The key fields of a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md), however, are only read-only, while the secondary table is used. This is the case for [`LOOP`](abaploop_at_itab.md) and when using the [`MODIFY`](abapmodify_itab.md) statement where the secondary key is specified after `USING KEY`. Otherwise the key fields are not read-only.

The administration of unique secondary keys is updated after modifications are made to individual lines using field symbols the next time the internal table is accessed ([delayed update](../../abap-glossary/abendelayed_update_glosry.md)). The administration of non-unique secondary keys is updated after the next explicit use of the secondary key ([lazy update](../../abap-glossary/abenlazy_update_glosry.md)). The check on the uniqueness of a secondary key does not take place until the time of the update. An internal table might therefore be in an inconsistent state with respect to the secondary key after individual lines have been modified using field symbols, which does not raise an exception until the table is next used. If the next use is not directly after the modification, the secondary key can be explicitly updated using methods of the class `CL_ABAP_ITAB_UTILITIES` to handle any exceptions on the spot.

### Hints

- The [typing](../../abap-glossary/abentyping_glosry.md) of the field symbol must match the line type of the internal table.

- If the `READ` statement is successful (`sy-subrc` has value 0), it is guaranteed that the field symbol immediately points to a memory area after the execution of the statement. A query using [`IS ASSIGNED`](../abap-program-flow-logic/abenlogexp_assigned.md) is not necessary there.

- If the addition `ELSE UNASSIGN` is not used, it is recommended that the return code `sy-subrc` is evaluated and that [`IS ASSIGNED`](../abap-program-flow-logic/abenlogexp_assigned.md) is not used, since in case of an unsuccessful read, the field symbol keeps its previous state and a memory area can be assigned to field symbol. This applies in particular to inline declarations. If the addition `ELSE UNASSIGN` is used, `sy-subrc` as well as the predicate `IS ASSIGNED` can be used.

- If the line to which the field symbol points is deleted, no more memory area is assigned to the field symbol and it can no longer be used instead of a data object. If the field symbol is not used directly after the `READ` statement, it may be useful to carry out a check using [`IS ASSIGNED`](../abap-program-flow-logic/abenlogexp_assigned.md).

- Another form of the statement `READ TABLE` using the addition `ASSIGNING` is the specification of a [table expression](../../abap-glossary/abentable_expression_glosry.md) [`table_exp`](abapassign_mem_area_writable_exp.md) after the statement [`ASSIGN`](abapassign.md).

## Addition 1

`... CASTING`

### Description

The addition `CASTING` has the same meaning as if it were specified without further additions in the statement [`ASSIGN`](abapassign_casting.md): The field symbol must be either completely typed, or typed with one of the generic built-in ABAP types `c`, `n`, `p`, or `x`. The assigned table line is [cast](../../abap-glossary/abencast_casting_glosry.md) to the type of the field symbol. The same exceptions can be raised here as with `ASSIGN`.

The addition `CASTING` cannot be used if the field symbol is declared inline with `FIELD-SYMBOL`.

## Addition 2

`... ELSE UNASSIGN`

### Description

The addition `ELSE UNASSIGN` sets the state of the field symbol to unassigned if no table line is found and `sy-subrc` is set to 4 or 8. If `ELSE UNASSIGN` is not specified, the field symbol keeps its previous state.

### Hint

See also the addition [`ELSE UNASSIGN`](abapassign_else_unassign.md) of the statement `ASSIGN`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of a particular line in the internal table `sflight_tab` and assignment to a field symbol `<sflight>` declared inline. After a successful assignment, the content of a component of the line is changed in the internal table. See also the example of the assignment of a [table expression](abapassign_mem_area_writable_exp.md) to a field symbol.

``` abap
DATA: carrid TYPE sflight-carrid, 
      connid TYPE sflight-connid, 
      fldate TYPE sflight-fldate. 
 
... 
 
DATA sflight_tab TYPE SORTED TABLE OF sflight 
                 WITH UNIQUE KEY carrid connid fldate. 
 
SELECT * 
       FROM sflight 
       WHERE carrid = @carrid AND 
             connid = @connid 
       INTO TABLE @sflight_tab. 
 
IF sy-subrc = 0. 
  READ TABLE sflight_tab 
       WITH TABLE KEY carrid = carrid 
                      connid = connid 
                      fldate = fldate 
       ASSIGNING FIELD-SYMBOL(<sflight>) ELSE UNASSIGN. 
  IF <sflight> IS ASSIGNED. 
    <sflight>-price *= '0.9'. 
  ENDIF. 
ENDIF.
```

## Alternative 3

`... REFERENCE INTO dref`

### Description

A reference to the found table line is made in the data reference variable `dref`. The addition cannot be specified if `itab` is specified as the return value or result of a [functional method](../../abap-glossary/abenfunctional_method_glosry.md) or of a [table expression](../../abap-glossary/abentable_expression_glosry.md) of a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md), since this value no longer exists once the statement has been executed.

The following can be specified for `dref`:

- An existing data reference variable whose static type is compatible with the line type of the internal table or is the generic type `data`.

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), where a data reference variable is declared whose static type is the line type of the internal table. The line type must be known statically and completely.

If no table line is found, `dref` remains unchanged or initial.

By dereferencing the data reference, the content of the found table line can be evaluated and changed. The same restrictions apply to the modification of key fields of the [primary](../../abap-glossary/abenprimary_table_key_glosry.md) and [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) as to access using field symbols (see `ASSIGNING` addition).

### Hints

- If the `READ` statement is successful (`sy-subrc` has value 0), it is guaranteed that the data reference variable immediately points to a line after the execution of the statement. A query using [`IS BOUND`](../abap-program-flow-logic/abenlogexp_bound.md) is not necessary here.

- Alongside the statement [`GET REFERENCE`](abapget_reference.md) and the reference operator [`REF`](abenconstructor_expression_ref.md), `REFERENCE INTO` is the only way of creating [stack references](../../abap-glossary/abenstack_reference_glosry.md). Stack references can become invalid if the referenced data object is deleted.

- When applied to internal tables in the [heap](../../abap-glossary/abenheap_glosry.md) `REFERENCE INTO` creates memory-retaining [heap references](../../abap-glossary/abenheap_reference_glosry.md).

- All references ([heap references](../../abap-glossary/abenheap_reference_glosry.md) and [stack references](../../abap-glossary/abenstack_reference_glosry.md)) that point to lines from internal tables can become invalid when lines are deleted. If a data reference variable is not used directly after the `READ` statement, it may be useful to carry out a check using [`IS BOUND`](../abap-program-flow-logic/abenlogexp_bound.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of a particular line of the internal table `sflight_tab` and assignment of a reference to the found line to the data reference variable `sflight_ref` (declared inline). After a successful assignment, the content of a component of the line is changed in the internal table.

``` abap
DATA: carrid TYPE sflight-carrid, 
      connid TYPE sflight-connid, 
      fldate TYPE sflight-fldate. 
 
... 
 
DATA sflight_tab TYPE SORTED TABLE OF sflight 
                 WITH UNIQUE KEY carrid connid fldate. 
 
SELECT * 
       FROM sflight 
       WHERE carrid = @carrid AND 
             connid = @connid 
       INTO TABLE @sflight_tab. 
 
IF sy-subrc = 0. 
  READ TABLE sflight_tab 
       WITH TABLE KEY carrid = carrid 
                      connid = connid 
                      fldate = fldate 
            REFERENCE INTO FINAL(sflight_ref). 
 
  IF sy-subrc = 0. 
    sflight_ref->price *= '0.9'. 
  ENDIF. 
ENDIF.
```

## Alternative 4

`... TRANSPORTING NO FIELDS`

### Description

If the addition `TRANSPORTING NO FIELDS` is used, the statement `READ TABLE` only checks whether the line that is being searched for exists and fills the system fields `sy-subrc` and `sy-tabix`. The system cannot access the content of the found line.

### Hints

- The [predicate function](../../abap-glossary/abenpredicate_function_glosry.md) [`line_exists`](../abap-program-flow-logic/abenline_exists_function.md) can also be used to check the existence of a table line.

- The built-in function [`line_index`](abenline_index_function.md) can also be used to identify the line number in the table index.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Check whether a particular line exists in the internal table `sflight_carr` and assignment of the line number in the primary table index of the found line in `sy-tabix` to `idx`.

``` abap
DATA carrid TYPE scarr-carrid. 
 
... 
 
DATA: scarr_tab TYPE SORTED TABLE OF scarr 
                WITH UNIQUE KEY carrid, 
      idx TYPE i. 
 
SELECT * 
       FROM scarr 
       INTO TABLE @scarr_tab. 
 
READ TABLE scarr_tab 
     WITH TABLE KEY carrid = carrid 
     TRANSPORTING NO FIELDS. 
IF sy-subrc = 0. 
  idx = sy-tabix. 
ENDIF.
```
