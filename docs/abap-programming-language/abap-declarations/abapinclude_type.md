---
title: "INCLUDE, TYPE, STRUCTURE"
source_file: abapinclude_type.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES > TYPES, BEGIN OF struct_type"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INCLUDE, TYPE, STRUCTURE

## Syntax

``` abap
INCLUDE { {TYPE struc_type} 
        | {STRUCTURE struc} } 
        [AS name [RENAMING WITH SUFFIX suffix]].  
```

### Addition

[1. `... AS name`](abapinclude_type.md#addition-1)

[2. `... RENAMING WITH SUFFIX suffix`](abapinclude_type.md#addition-2)

## Overview

### Description

This statement can only be executed within a structure definition with the additions `BEGIN OF` and `END OF` of the statements [`TYPES`](abaptypes.md), [`DATA`](abapdata.md), [`CLASS-DATA`](abapclass-data.md), and [`STATICS`](abapstatics.md). It includes all components of a structured type at this position in the current structure definition. The structured type can be specified as follows:

- As a structured data type `struc_type` after `TYPE`, both visible and usable at this position. `struc_type` can be a local structured type, a visible structured type of a global class or global interface, or a structure from ABAP Dictionary.

- As a structured data object `struc` after `STRUCTURE`, visible at this position. Its structured data type is used. `struc` must be a structure of the same program or a visible attribute of a global class or global interface.

The `INCLUDE` statement does not create a [substructure](../../abap-glossary/abensubstructure_glosry.md), which means the components are inserted as if they were listed individually instead of the statement `INCLUDE`.

### Hints

- Note the following when using the `INCLUDE` statement:

  - If the statement `INCLUDE` is used to add more structure components to existing components, or if multiple `INCLUDE` statements are used in a structure, this can produce syntax errors due to naming conflicts. This is particularly problematic if structures are included that are not defined in the same program and that are subsequently changed.

  - The included structures cannot be addressed as such without restrictions.

  - The necessary metadata is stored again for each component of an included structure, whereas the metadata for the components of a [substructure](../../abap-glossary/abensubstructure_glosry.md) is only stored once when the substructure is defined.

  - In contrast to real substructures, structures included using `INCLUDE` cannot be declared as [static boxes](../../abap-glossary/abenstatic_box_glosry.md) when embedded.

    Where possible, real [substructures](../../abap-glossary/abensubstructure_glosry.md) should be created instead of the statement `INCLUDE`. However, the addition `RENAMING WITH SUFFIX` should be used to avoid naming conflicts. This recommendation also applies to [includes of structures](../../abap-dictionary-ddic/ddic-data-types/abenddic_include_structure.md) in ABAP Dictionary, where the structures of database tables particularly cannot contain any real substructures.

- As usual, the addition `TYPE` is used to specify a data type. Like the addition [`LIKE`](abaptypes_referring.md), the addition `STRUCTURE` is used to specify a data object. Outside of ABAP objects, [flat structures](../../abap-glossary/abenflat_structure_glosry.md), database tables, or [views](../../abap-glossary/abenview_glosry.md) of the ABAP Dictionary can also be specified for `struc` with the addition `STRUCTURE`.

- In constant structures defined with [`CONSTANTS`](abapconstants.md), no components can be included using `INCLUDE` because it is not possible to assign a [start value](../../abap-glossary/abenstart_value_glosry.md) to them.

- In regard to their [alignments](../../abap-glossary/abenalignment_glosry.md), structures included using `INCLUDE` behave like substructures, which means [alignment gaps](../../abap-glossary/abenalignment_gap_glosry.md) can occur before the first or after the last component. These do not occur when the components are declared directly.

- A structure that is included using `INCLUDE` is handled by the method `GET_COMPONENTS` of the class `CL_ABAP_STRUCTDESCR` of [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md) like a substructure. The returned component table only contains one line for an included structure. The component type is represented by an object from `CL_ABAP_STRUCTDESCR`, but the `AS_INCLUDE` column contains the value *X*. The method `GET_INCLUDED_VIEW` can be used to resolve components of included structures.

- When a [static box](../../abap-glossary/abenstatic_box_glosry.md) is inherited by one structure from another, its boxed component property is also inherited.

## Addition 1

`... AS name`

### Description

By specifying the name `name` after the addition `AS`, the components of the included structure `struc_type` or `struc` become a [component group](../../abap-glossary/abencomponent_group_glosry.md) also known as [named include](../../abap-glossary/abennamed_include_glosry.md). Besides regular addressing using the name of the including structure, they either can be addressed together using the name `name` or as individual components using the structure component selector (`name-`). The name `name` must be unique within the structure into which the components are included. This means that there must not be any other component with this name and it must not be specified in a different `INCLUDE` statement after `AS`.

### Hints

- Included components for which a name is specified after `AS`, can be addressed in the same way as if they were components of a substructure `name`.

- A name `name` specified with `AS name` is used only for an additional explicit addressing option and is ignored by an implicit addressing in statements such as [`MOVE-CORRESPONDING`](../abap-processing-internal-data/abapmove-corresponding.md) or [`SELECT INTO CORRESPONDING`](../abap-database-access/abapinto_clause.md). A component renamed using `RENAMING WITH SUFFIX` actually has this name and is therefore never ignored.

## Addition 2

`... RENAMING WITH SUFFIX suffix`

### Description

The addition `RENAMING WITH SUFFIX` is used to rename each individual component by appending the extension `suffix`, which prevents naming conflicts between components with the same name. `suffix` must be specified directly.

### Hints

- The use of the `RENAMING WITH SUFFIX` addition makes it possible to include an individual structure multiple times.

- Renaming the components of included structures can prevent errors during an upgrade of these structures.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, the structure `week` is defined by repeated transfer of the components of the structured type `t_day`. The components of `week` are all at the same level and can be addressed as follows: `week-work_mon`, `week-free_mon`, `week-work_tue`, and so on. Alternatively, they can also be addressed as follows: `week-monday-work`, `week-monday-free`, `week-tuesday-work`, and so on.

``` abap
TYPES: BEGIN OF t_day, 
         work TYPE c LENGTH 8, 
         free TYPE c LENGTH 16, 
       END OF t_day. 
 
DATA BEGIN OF week. 
  INCLUDE TYPE t_day AS monday    RENAMING WITH SUFFIX _mon. 
  INCLUDE TYPE t_day AS tuesday   RENAMING WITH SUFFIX _tue. 
  INCLUDE TYPE t_day AS wednesday RENAMING WITH SUFFIX _wed. 
  ... 
DATA END OF week.
```
