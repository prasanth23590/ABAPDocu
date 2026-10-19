---
title: "ASSIGN"
source_file: abapassign.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Field Symbols"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ASSIGN

## Syntax

``` abap
ASSIGN mem_area TO <fs> casting_spec   
                        range_spec   
                        [ELSE UNASSIGN].
```

[`mem_area`](abapassign_mem_area.md) · [`casting_spec`](abapassign_casting.md) · [`range_spec`](abapassign_range.md) · [`ELSE UNASSIGN`](abapassign_else_unassign.md)

## Description

This statement assigns the memory area specified using [`mem_area`](abapassign_mem_area.md) to the field symbol `<fs>`. A data object or a memory area calculated from the address of a data object can be assigned. After a successful assignment, the field symbol refers to the assigned memory area and can be used in operand positions. When used in a statement, it works like a dereferenced data reference, meaning that the statement works with the content of the memory area.

The following can be specified for `<fs>`:

- An existing field symbol with appropriate typing.

- An inline declaration [`FIELD-SYMBOL(<fs>)`](../abap-declarations/abenfield-symbol_inline.md). The typing depends on the [`mem_area`](abapassign_mem_area.md) specified.

The data type used to handle the assigned memory area depends on the specification in [`casting_spec`](abapassign_casting.md). Either an explicit [casting](../../abap-glossary/abencast_casting_glosry.md) can be performed, or the field symbol inherits the data type of the data object specified in the assignment. In both cases, the data type used must [match](../abap-declarations/abentyping_check_general.md) the [typing](../../abap-glossary/abentyping_glosry.md) of the field symbol. A field symbol to which a memory area is assigned, has this data type after the assignment and behaves like a data object of this type.

The assigned memory area `mem_area` must be at least as long as the data type specified in `casting_spec` and must have at least the same [alignment](../../abap-glossary/abenalignment_glosry.md). If the data type determined in `casting_spec` is [deep](../../abap-glossary/abendeep_glosry.md), the deep components must correspond exactly in their type and position.

The specification in [`range_spec`](abapassign_range.md) is used to define the memory area that can be assigned to the field symbol.

If the assignment is not successful. the behavior depends on the assigned [`mem_area`](abapassign_mem_area.md) and on the addition [`ELSE UNASSIGN`](abapassign_else_unassign.md):

- If a [static assignment](abapassign_mem_area_static_dobj.md) is not successful, `sy-subrc` is not set. No memory area is assigned to the field symbol. The field symbol has the state unassigned after the `ASSIGN` statement. The addition `ELSE UNASSIGN` is used implicitly and must not be specified.

- If a [dynamic assignment](abapassign_mem_area_dynamic_dobj.md), an [assignment of dynamic components](abapassign_dynamic_components.md), a [dynamic access](abapassign_mem_area_dynamic_access.md) or an [assignment of a table expression](abapassign_mem_area_writable_exp.md) is not successful, `sy-subrc` is set to 4 or 8 and:

  - If `ELSE UNASSIGN` is not specified, the field symbol keeps its previous state.

  - If `ELSE UNASSIGN` is specified, no memory area is assigned to the field symbol. The field symbol has the state unassigned after the `ASSIGN` statement.

    Some invalid dynamic specifications in the [assignment of dynamic components](abapassign_dynamic_components.md) do not set `sy-subrc` but raise an exception.

- An assignment of the constructor operators [`NEW`](abapassign_mem_area_writable_exp.md) or [`CASE`](abapassign_mem_area_writable_exp.md) is either successful or leads to an exception and the addition `ELSE UNASSIGN` must not be used.

If an assignment would lead to illegal memory accesses, an exception is raised for both static and dynamic `ASSIGN` statements.

## System Fields

The `ASSIGN` statement sets the return code for a [dynamic assignment](abapassign_mem_area_dynamic_dobj.md), an [assignment of dynamic components](abapassign_dynamic_components.md), a [dynamic access](abapassign_mem_area_dynamic_access.md) or an [assignment of a table expression](abapassign_mem_area_writable_exp.md). For an [assignment of the constructor operator `NEW`](abapassign_mem_area_writable_exp.md), the return code is set by the constructor operator. The return code is not set for a [static assignment](abapassign_mem_area_static_dobj.md) and an [assignment of the constructor operator `CAST`](abapassign_mem_area_writable_exp.md).

| **`sy-subrc`** | **Meaning**                                                                                 |
|----------------|---------------------------------------------------------------------------------------------|
| 0              | Assignment was successful.                                                                  |
| 4              | Assignment was not successful.                                                              |
| 8              | Assignment of [table expression](abapassign_mem_area_writable_exp.md) was not successful. |

## Hints

- The state of the field symbol can be checked with the [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md) [`<fs> IS ASSIGNED`](../abap-program-flow-logic/abenlogexp_assigned.md).

- When setting field symbols using `ASSIGN`, permission to access the assigned data object is only checked at the position of the statement. The field symbol can then be passed on and used to access the assigned data object in any position. To prevent access to private and read-only attributes using field symbols outside classes, field symbols for these attributes should not be published externally. A constant a read-only input parameter or an [immutable variable](../../abap-glossary/abenimmutable_variable_glosry.md), however, can never be made modifiable by passing a field symbol.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Three field symbols are assigned the substrings for year, month, and day of the system field `sy-datlo`. The substrings can then be addressed using field symbols.

``` abap
FIELD-SYMBOLS <year>  TYPE n. 
FIELD-SYMBOLS <month> TYPE n. 
FIELD-SYMBOLS <day>   TYPE n. 
 
FINAL(date) = cl_demo_date_time=>get_user_date( ). 
 
ASSIGN date+0(4) TO <year>. 
ASSIGN date+4(2) TO <month>. 
ASSIGN date+6(2) TO <day>. 
 
cl_demo_output=>new( 
  )->write(   <year> 
  )->write(   <month> 
  )->display( <day> ).
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_ASSIGN_CAST_ILLEGAL_CAST`

- *Cause:* The type of the source field and the target type do not match exactly in offset and type in those components that are strings, tables, or references.

  *Runtime error:* `ASSIGN_CASTING_ILLEGAL_CAST`

`CX_SY_ASSIGN_CAST_UNKNOWN_TYPE`

- *Cause:* A type specified dynamically after `CASTING` is unknown.

  *Runtime error:* `ASSIGN_CASTING_UNKNOWN_TYPE`

`CX_SY_ASSIGN_OUT_OF_RANGE`

- *Cause:* The data object in addition `RANGE` does not contain the assigned data object.

  *Runtime error:* `ASSIGN_FIELD_NOT_IN_RANGE`

`CX_SY_ASSIGN_ILLEGAL_COMPONENT`

- *Cause:* A dynamically specified component does not exist.

  *Runtime error:* `ASSIGN_ILLEGAL_COMPONENT`
