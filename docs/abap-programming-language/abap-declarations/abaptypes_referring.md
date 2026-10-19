---
title: "TYPES, TYPE, LIKE"
source_file: abaptypes_referring.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, TYPE, LIKE

## Syntax

``` abap
TYPES dtype { {TYPE [LINE OF] type}   
            | {LIKE [LINE OF] dobj}  }.  
```

### Addition

[`... LINE OF ...`](abaptypes_referring.md#addition)

## Overview

### Description

By specifying a data type `type` or a data object `dobj`, `dtype` inherits all properties of the specified data type or data object.

- The following can be specified for `type`:

  - A non-generic data type from the ABAP Dictionary or ABAP CDS allowed by the package check, particularly including the structure of a DDIC database table, or a [CDS type](../../abap-glossary/abencds_type_glosry.md).

  - A non-generic public type of a global class allowed by the package check

  - A non-generic data type of the same program defined previously using `TYPES`

- A data object that is [visible](../abap-data-types-and-data-objects/abenlifetime_and_visibility.md) at this point can be [specified](../abap-operands/abendata_objects_usage_reading.md) for `dobj`. If a field symbol or formal parameter is specified for `dobj`, this must be [completely typed](abentyping_complete.md). The declared type is inherited. No data object must be bound when the statement is evaluated.

If a reference is made to a data type in the ABAP Dictionary, its elementary components are transformed to built-in ABAP types in accordance with the [tables](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) of built-in types in the ABAP Dictionary.

### Hints

- A data type that is defined by a `TYPE` reference to another data type is a copy of this data type (possibly in a different context and with a different name). If the original type is defined in the [ABAP Dictionary](../../abap-dictionary-ddic/ddic-data-types/abenddic_data_types.md) or is a CDS simple type, its semantic properties are preserved.

- The data objects that can be referred to with `LIKE` also include the public attributes of global classes.

- A data type that is declared by a direct `TYPE` or `LIKE` reference to a [boxed component](../../abap-glossary/abenboxed_component_glosry.md) inherits its data type but is not a boxed component.

- A data type that is declared by a `TYPE` or `LIKE` reference to an [enumerated type](abaptypes_enum.md) has exactly the same meaning as the enumerated type itself. The value set defined for the enumerated type is not duplicated.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a local type `also_my_struct_type` based on the type `my_struct_type` using `LIKE`.

``` abap
TYPES: BEGIN OF struct_type, 
         s1 TYPE i, 
         s2 TYPE i, 
       END OF struct_type. 
DATA my_struct TYPE struct_type. 
 
TYPES also_my_struct_type LIKE my_struct.
```

## Addition

`... LINE OF ...`

### Description

The optional addition `LINE OF` can be used if `type` is a table type or if `dobj` is an internal table. This means that `dtype` inherits the properties of the line type of the internal table.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

These `TYPES` statements define two data types local to the program. The first inherits a table type from a [type pool](../../abap-glossary/abentype_pool_glosry.md) of the ABAP Dictionary, and the second corresponds to the line type of this table type.

``` abap
DATA: event_table TYPE cntl_simple_events, 
      event       LIKE LINE OF event_table.
```
