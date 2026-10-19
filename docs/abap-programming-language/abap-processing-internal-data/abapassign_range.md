---
title: "ASSIGN, range_spec"
source_file: abapassign_range.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Field Symbols > ASSIGN"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ASSIGN, range_spec

## Syntax

``` abap
... { }   
  | {RANGE range}.  
```

### Alternative

[1. `... { }`](abapassign_range.md#alternative-1)

[2. `... RANGE range`](abapassign_range.md#alternative-2)

## Overview

### Description

The specification `range_spec` defines the area limits within which a memory area can be assigned to the field symbol. Either nothing can be specified here or the addition `RANGE`.

At the same time, the statement `ASSIGN` assigns these area limits to the field symbol `<fs>`. If the field symbol `<fs>` is itself used in a subsequent `ASSIGN` statement to specify a memory area [`mem_area`](abapassign_mem_area.md), the assigned memory areas are used to determine the area limits of the field symbol to which the assignment is made.

### Hints

- The area limits assigned to a field symbol using `range_spec` only apply to the following `ASSIGN` statements. In other statements the [general rules](../abap-operands/abenoperands_data_objects.md) apply.

## Alternative 1

`... { }`

### Description

If no value is specified for `range_spec`, the area limits are defined as follows:

- If an elementary data object was specified for `dobj` in [`mem_area`](abapassign_mem_area_static_dobj.md), the memory area of this data object determines the area limits.

- If a field symbol was specified for `dobj` in [`mem_area`](abapassign_mem_area_static_dobj.md), and an elementary data object is assigned to it, the field symbol `<fs>` of the current statement inherits the area limits assigned to this field symbol.

- If a structure or a field symbol that points to a structure was specified for `dobj` in [`mem_area`](abapassign_mem_area_static_dobj.md), the system checks whether the structure has a character-like initial part up to the first [alignment gap](../../abap-glossary/abenalignment_gap_glosry.md). This then determines the area limits.

If these area limits are exceeded, no memory area is assigned for the static variant of `mem_area` after the `ASSIGN` statement and the [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md) [`<fs> IS ASSIGNED`](../abap-program-flow-logic/abenlogexp_assigned.md) is false, while `sy-subrc` is set to 4 in the dynamic variant.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the first `ASSIGN` statement, the area limits of the data object `text` are assigned to `<fs1>`. In the second `ASSIGN` statement, `<fs2>` inherits these limits. From the sixth loop pass, an attempt is made to assign a larger memory area to `<fs2>`, which makes the logical expression after `IF` false.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA text TYPE c LENGTH 8 VALUE '12345678'. 
 
FIELD-SYMBOLS: <fs1> TYPE ANY, 
               <fs2> TYPE ANY. 
 
ASSIGN text+3(3) TO <fs1>. 
 
DO 8 TIMES. 
  ASSIGN <fs1>(sy-index) TO <fs2>. 
  IF <fs2> IS ASSIGNED. 
    out->write_text( |{ <fs2> }| ). 
  ENDIF. 
ENDDO. 
 
out->display( ).
```

## Alternative 2

`... RANGE range`

### Description

If the addition `RANGE` is specified in `range_spec`, the area limits are defined by the [data area](../../abap-glossary/abendata_area_glosry.md) of the data object `range`. `range` expects a data object of any data type that covers the area limits that result when the `RANGE` addition is not specified (see above). If it is established at runtime that `range` does not cover these area limits, a catchable exception is raised.

When the `RANGE` addition is used, only subareas of the `range` data object can be assigned to the field symbol. If these area limits are exceeded, no memory area is assigned for the static variant of [`mem_area`](abapassign_mem_area.md) after the `ASSIGN` statement and the [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md) [`<fs> IS ASSIGNED`](../abap-program-flow-logic/abenlogexp_assigned.md) is false, while `sy-subrc` is set to 4 in the dynamic variants.

The addition `RANGE` cannot be used with the addition [`CASTING TYPE HANDLE`](abapassign_casting.md) or for assigning [table expressions](abapassign_mem_area_writable_exp.md).

### Hints

- A `RANGE` addition does not remove the type-specific rules for [substring accesses](../abap-operands/abenoffset_length.md). To enable substring access beyond the field limits of a specified data object `dobj`, substring access must be possible in principle. In particular, substring access is never possible beyond the limits of a structure, since the character-like initial part would not be accessed.

- If a structure is specified for `range` that contains [dynamic data objects](../../abap-glossary/abendynamic_data_object_glosry.md), they only contribute the internal reference to the data area of the structure. The actual data area of the dynamic data objects is paged out and is ignored by `RANGE`. This also applies to substructures that are declared as [boxed components](../../abap-glossary/abenboxed_component_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The second dynamic assignment fails because the `RANGE` condition is violated.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: 
  BEGIN OF struct, 
    BEGIN OF substruc1, 
      col1 TYPE c LENGTH 1, 
      col2 TYPE c LENGTH 1, 
    END OF substruc1, 
    BEGIN OF substruc2, 
      col1 TYPE i, 
      col2 TYPE i, 
    END OF substruc2, 
  END OF struct. 
 
TRY. 
    ASSIGN ('STRUCT-SUBSTRUC1-COL1') TO FIELD-SYMBOL(<fs1>) 
                                     RANGE struct-substruc1 
                                     ELSE UNASSIGN. 
    IF <fs1> IS ASSIGNED. 
      out->write( '<fs1> assigned' ). 
    ENDIF. 
    ASSIGN ('STRUCT-SUBSTRUC1-COL1') TO FIELD-SYMBOL(<fs2>) 
                                     RANGE struct-substruc2 
                                     ELSE UNASSIGN. 
    IF <fs2> IS ASSIGNED. 
      out->write( '<fs2> assigned' ). 
    ENDIF. 
  CATCH cx_sy_assign_out_of_range INTO FINAL(exc). 
    out->write( exc->get_text( ) ). 
ENDTRY. 
 
out->display( ).
```
