---
title: "Structures"
source_file: abendata_objects_structure.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Structures

Structures are data objects that consist of components of any data type that are stored consecutively in the memory. The data type of a structure is a [structured type](../../abap-glossary/abenstructured_type_glosry.md):

- In a program, a structured type or structure is created using the additions [`BEGIN OF ... END OF`](../abap-declarations/abaptypes_struc.md) of the statements `TYPES`, `DATA`, and so on. Structured types can also be created dynamically using the [RTTC](../../abap-glossary/abenrun_time_type_creation_glosry.md) methods.

- In ABAP Dictionary, structured types are [DDIC structures](../../abap-dictionary-ddic/ddic-data-types/abenddic_structures.md) or types of [DDIC database tables](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables.md).

- In [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), [CDS entities](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_entities.md) represent structured types.

The following sections give an overview of structures in ABAP.

- [Kinds of Structures](abendata_objects_structure.md#kinds-of-structures)

- [Use of Structures](abendata_objects_structure.md#use-of-structures)

  - [Use of Deep Structures](abendata_objects_structure.md#use-of-deep-structures)

  - [Use of Deep DDIC Structures](abendata_objects_structure.md#use-of-deep-ddic-structures)

- [Boxed Components](abendata_objects_structure.md#boxed-components)

## Kinds of Structures

Depending on the type of component, structures are named as follows:

- **Flat structures** do not contain any [deep](../../abap-glossary/abendeep_glosry.md) components. They only contain components with flat data types, such as elementary types `c`, `n`, `d`, `t`, `decfloat16`, `decfloat34`, `f`, `b`, `s`, `i`, `int8`, `p`, `x`, `utclong`, or structures with these types.

- **Flat character-like structures** are flat structures with exclusively [character-like](../../abap-glossary/abencharlike_data_object_glosry.md) components.

- **Nested structures** contain at least one [substructure](../../abap-glossary/abensubstructure_glosry.md). Whether a nested structure is flat or character-like depends on the properties of all components.

- **Deep structures** contain at least one [deep](../../abap-glossary/abendeep_glosry.md) component in any nesting level. Possible deep components include strings, internal tables, boxed components, data or object references.

A structure that contains static or dynamic components is formally also a [static](../../abap-glossary/abenstatic_data_object_glosry.md) or [dynamic data object](../../abap-glossary/abendynamic_data_object_glosry.md), respectively.

The following figure illustrates a deep structure.

  
![figure](images_abdoc_deep_structure.gif)  

### Hints

- The term *nested structure* must not be confused with the term *deep structure*. A nested structure is flat if it contains exclusively flat components and subcomponents. A nested structure is deep when it has at least one deep component or subcomponent.

- Generally, the components of a structure are not stored directly one after the other in memory and [alignment gaps](../../abap-glossary/abenalignment_gap_glosry.md) may occur.

- The maximum number of bytes a structure can contain including alignment gaps is the maximum length of a field of type `x`, which is stored in the constant `TYPE_X_MAX_LENGTH` of the class `CL_ABAP_ELEMDESCR`. Components that are reference variables, strings or internal tables each use 8 bytes.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Nested structure. The substructure is created using a reference to the DDIC structure `SCARR` for the second component. The components are accessed using the structure component selector (`-`).

``` abap
DATA: 
  BEGIN OF struct, 
    name  TYPE c LENGTH 10 VALUE 'SCARR', 
    scarr TYPE scarr, 
  END OF struct. 
 
SELECT SINGLE * 
       FROM scarr 
       WHERE carrid = 'LH' 
       INTO CORRESPONDING FIELDS OF @struct-scarr. 
 
cl_demo_output=>new( 
)->write_data( struct-name 
)->write_data( struct-scarr-carrid 
)->write_data( struct-scarr-carrname 
)->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Deep structure. The following structure contains exclusively deep components.

``` abap
DATA: 
  BEGIN OF struct, 
    text TYPE string, 
    hex  TYPE xstring, 
    tab  TYPE STANDARD TABLE OF i WITH EMPTY KEY, 
    dref TYPE REF TO i, 
    iref TYPE REF TO if_demo_output, 
  END OF struct.
```

## Use of Structures

Structures are addressed either completely or by component in appropriate operand positions. The [structure component selector](../../abap-glossary/abenstructure_component_sel_glosry.md) (`-`) is used for the latter. In the case of data reference variables that are typed as a structure, the components of the structure to which the data reference variable points can also be addressed using the object component selector (`->`).

Special [conversion](../abap-processing-internal-data/abenconversion_struc.md) and [comparison rules](../abap-program-flow-logic/abenlogexp_rules_operands_struc.md) apply to assignments that involve structures. Flat character-like structures have the special feature that they can be used like [character-like data objects](../../abap-glossary/abencharlike_data_object_glosry.md) in many operand positions and included in the generic ABAP type [`clike`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md). They can be specified in almost all operand positions where elementary character-like data objects are possible. The ABAP runtime framework then interprets the structure as an elementary field of the type `c` in the length of the structure. An exception to this are operand positions of [string expressions](../abap-processing-internal-data/abapcompute_string.md) and [string functions](../abap-processing-internal-data/abenstring_functions.md) with named parameters.

For the assignment of structure components, there is a special statement [`MOVE-CORRESPONDING`](../abap-processing-internal-data/abapmove-corresponding.md), a constructor operator [`CORRESPONDING`](../abap-processing-internal-data/abenconstructor_expr_corresponding.md), and a system class [`CL_ABAP_CORRESPONDING`](../abap-processing-internal-data/abencl_abap_corresponding.md). The [`INTO`](../abap-database-access/abapinto_clause.md) clause of ABAP SQL also has an addition `CORRESPONDING`. The statement [`ASSIGN`](../abap-processing-internal-data/abapassign.md) has a special variant [`COMPONENT OF STRUCTURE`](../abap-processing-internal-data/abapassign_dynamic_components.md) for dynamic access to structure components.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Inline declaration of a structure `wa` in a `SELECT` statement with reference to the DDIC database table `SCARR`. The components of the structure are accessed using the structure component selector (`-`).

``` abap
SELECT carrid, carrname 
       FROM scarr 
       INTO @FINAL(wa). 
  cl_demo_output=>write( |{ wa-carrid WIDTH = 5 
                         }{ wa-carrname }| ). 
ENDSELECT. 
cl_demo_output=>display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of a structure as an [anonymous data object](../../abap-glossary/abenanonymous_data_object_glosry.md) with the type of the DDIC database table `SCARR` in the ABAP Dictionary to which the data reference variable `dref` points. Used as the target area of a `SELECT` statement using the [dereferencing operator](../../abap-glossary/abendereferencing_operat_glosry.md) (`->*`). The components of the structure are accessed using the object component selector (`->`).

``` abap
FINAL(dref) = NEW scarr( ). 
 
SELECT * 
       FROM scarr 
       INTO @dref->*. 
  cl_demo_output=>write( |{ dref->carrid WIDTH = 5 
                         }{ dref->carrname }| ). 
ENDSELECT. 
cl_demo_output=>display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates that a flat structure with exclusively character-like components can behave like a structure and like a character-like data object.

``` abap
DATA: 
  BEGIN OF struct, 
    col1 TYPE c LENGTH 5 VALUE '12345', 
    col2 TYPE c LENGTH 5 VALUE 'abcde', 
  END OF struct. 
 
cl_demo_output=>new( 
  )->write_data( struct 
  )->write_data( struct-col1 
  )->write_data( struct-col2 
  )->write_data( CONV string( struct ) 
  )->display( ).
```

### Use of Deep Structures

Since the data content of deep structures is not stored completely within the memory bounds of the structure itself and the deep components are just references to the actual data instead, there are some general restrictions apply when using deep structures, as opposed to flat structures:

- Deep structures must be [compatible](abencompatibility.md) in [assignments](../abap-processing-internal-data/abenvalue_assignments.md) and [comparisons](../abap-program-flow-logic/abenlogexp_comp.md).

- [Substring access](../abap-operands/abenoffset_length.md) using offset/lengths is not possible for deep structures.

- Deep structures cannot be used as character-like data objects in operand positions and are not included in the generic ABAP type [`clike`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md). This applies in particular to structures that contain [strings](../../abap-glossary/abenstring_glosry.md).

- When data objects are cast with [`ASSIGN`](../abap-processing-internal-data/abapassign_casting.md), the deep components of deep structures must match in type and position in the type of the data object, and in the type of the field symbol.

- The [work area](../abap-database-access/abenabap_sql_wa.md) of ABAP SQL statements cannot contain any deep components other than strings or [LOB handles](../../abap-glossary/abenlob_handle_glosry.md).

- The target or source field of the statements `OPEN DATASET` and `TRANSFER` cannot be a deep structure.

- No internal tables with a deep line type can be passed to a `TABLES` parameter in a remote function call. Deep structures can be passed to the other parameters, as long as they do not contain any reference variables.

### Hint

These restrictions are particularly important if single components in existing flat character-like structures are converted to strings, which makes the entire structure deep.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following two deep structures are not compatible and cannot be converted to each other.

``` abap
DATA: 
  BEGIN OF struct1, 
    col1 TYPE c LENGTH 4, 
    col2 TYPE REF TO data, 
  END OF struct1, 
  BEGIN OF struct2, 
    col1a TYPE c LENGTH 2, 
    col1b TYPE c LENGTH 2, 
    col2 TYPE REF TO data, 
  END OF struct2. 
 
struct1 = struct2. "Syntax error
```

### Use of Deep DDIC Structures

The same restrictions apply to deep DDIC structures defined in the ABAP Dictionary as to deep structures declared in ABAP programs.

## Boxed Components

The substructures of nested structures and structured components of classes or interfaces can be declared as [boxed components](abenboxed_components.md).
