---
title: "General Properties of Data Objects"
source_file: abendobj_general.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# General Properties of Data Objects

- [Creating and Addressing Data Objects](abendobj_general.md#creating-and-addressing-data-objects)

- [Data Types of Data Objects](abendobj_general.md#data-types-of-data-objects)

- [Variable and Constant Data Objects](abendobj_general.md#variable-and-constant-data-objects)

- [Static and Dynamic Data Objects](abendobj_general.md#static-and-dynamic-data-objects)

- [Flat and Deep Data Objects](abendobj_general.md#flat-and-deep-data-objects)

## Creating and Addressing Data Objects

There is a distinction between:

- [Named data objects](../../abap-glossary/abennamed_data_object_glosry.md) that are declared statically using a data-defining statement and are addressed using a name. The typical data-defining statement is [`DATA`](../abap-declarations/abapdata.md). Named objects are created at the start of the lifetime of a context (a program, class, object, or procedure) by the ABAP runtime framework and live for as long as their context exists.

- [Anonymous data objects](../../abap-glossary/abenanonymous_data_object_glosry.md) that are created in the [heap](../../abap-glossary/abenheap_glosry.md) by the statement [`CREATE DATA`](../abap-creating-objects-and-values/abapcreate_data.md) or the instance operator [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) and are addressed using [data reference variables](../../abap-glossary/abendata_reference_variable_glosry.md). Anonymous data objects exist in the [internal session](../../abap-glossary/abeninternal_session_glosry.md) of the program in which they were created and are subject to [garbage collection](../../abap-glossary/abengarbage_collector_glosry.md).

- [Literals](../../abap-glossary/abenabap_literal_glosry.md) that are defined in the source code of a program and are fully defined by their value.

In addition to data objects declared in programs, there is a set of [built-in data objects](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_objects.md) that can always be accessed in ABAP programs. Furthermore, some statements create data objects implicitly that are then available for special purposes.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following example, `dref` is a named data object whose content points to an anonymous data object after the instance operator [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) is used. `555` is a numeric literal.

``` abap
DATA dref TYPE REF TO i. 
dref = NEW #( 555 ).
```

## Data Types of Data Objects

Every data object has a specific data type, and every data object occupies memory for the data. The data type of a data object is defined either with reference to a [standalone data type](../../abap-glossary/abenstand-alone_data_type_glosry.md) or as a [bound data type](../../abap-glossary/abenbound_data_type_glosry.md) when the data object is created.

The data type of a data object is always defined uniquely and cannot be changed at runtime of a program. In the case of anonymous data objects, this data type determines the [dynamic type](../../abap-glossary/abendynamic_type_glosry.md) of the associated reference variables.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following example, `c_20` is a standalone data type used to declare the data object `text1`. The data object `text2`, on the other hand, has a bound data type.

``` abap
TYPES c_20 TYPE c LENGTH 20. 
DATA: text1 TYPE c_20, 
      text2 TYPE c LENGTH 20.
```

## Variable and Constant Data Objects

Variable data objects are distinguished from constant data objects in how they can change. [Variables](../../abap-glossary/abenvariable_glosry.md) can change their value at runtime. [Constants](../../abap-glossary/abenconstant_glosry.md) always keep their initial value.

[Literals](../../abap-glossary/abenabap_literal_glosry.md) and [text symbols](../../abap-glossary/abentext_symbol_glosry.md) are also constant. [Input parameters](../../abap-glossary/abeninput_parameter_glosry.md) in [procedures](../../abap-glossary/abenprocedure_glosry.md) usually cannot be changed if this would cause the assigned [actual parameter](../../abap-glossary/abenactual_parameter_glosry.md) to be changed.

[Immutable variables](../../abap-glossary/abenimmutable_variable_glosry.md) are a special kind of variables. A value can be assigned to an immutable variable at exactly one [write position](../../abap-glossary/abenwrite_position_glosry.md) of a context. Immutable variables are declared inline with the declaration operator [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). Although one and the same declaration can appear only one time in a context, it can be processed multiple times - for example in a loop - and different values can be assigned then.

### Hint

Immutable variables can improve the robustness of programs whenever a variable is filled at a write position only once and after that only read accesses occur.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following example, `true` and `false` are constants that can be assigned to the variable `flag`.

``` abap
TYPES bool TYPE c LENGTH 1. 
 
CONSTANTS: true  TYPE bool VALUE 'X', 
           false TYPE bool VALUE ' '. 
 
DATA flag TYPE bool. 
 
IF ... 
  flag = true. 
ELSE. 
  flag = false. 
ENDIF.
```

## Static and Dynamic Data Objects

Static data objects, for which all technical properties must be defined when declared, are distinguished from dynamic data objects, whose memory requirement or size is not defined until runtime. [Strings](../../abap-glossary/abenstring_glosry.md) and [internal tables](../../abap-glossary/abeninternal_table_glosry.md) are dynamic data objects.

The length of a string is 0 after declaration and changes at runtime depending on the content assigned to it. Internal tables do not contain any lines after their declaration. There can be any number of lines and the number is defined dynamically at runtime when the internal table is filled.

Structures that contain dynamic components are also dynamic data objects.

### Hint

See also [Maximum Size of Dynamic Data Objects](abenmemory_consumption_2.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following example, `text_field` is a static data object and `text_string` is a dynamic data object. When `abcde` is assigned to `text_field`, it is truncated from the tenth character. `text_string` is given all characters and has the same length as `sy-abcde` after the assignment.

``` abap
DATA: text_field  TYPE c LENGTH 10, 
      text_string TYPE string. 
 
FINAL(abcde) = 'abcdefghijklmnopqrstuvwxyz'. 
text_field  = abcde. 
text_string = abcde.
```

## Flat and Deep Data Objects

All static data objects except reference variables are flat. Their content corresponds to the actual work data. Dynamic data objects and reference variables are deep, and they contain references that refer to the actual content. The handling of references is implicit for dynamic data objects (strings and internal tables), and explicit for reference variables.

Structures that do not contain any deep components are flat structures. Structures that contain at least one deep component are deep structures.

### Hint

See also [Memory Management of Deep Objects](abenmemory_consumption.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following example, `struct1` is a flat structure and `struct2` is a deep structure. In the flat structure, character-like components are stored consecutively in the memory and [substring access](../abap-operands/abenoffset_length.md) is possible. In the deep structure, the components contain pointers to the actual data and substring access is not possible.

``` abap
DATA: 
  BEGIN OF struct1, 
    col1 TYPE c LENGTH 5 VALUE '12345', 
    col2 TYPE c LENGTH 5 VALUE 'abcde', 
  END OF struct1, 
  BEGIN OF struct2, 
    col1 TYPE string VALUE `12345`, 
    col2 TYPE string VALUE `abcde`, 
  END OF struct2. 
 
FINAL(section1) = struct1+3(4).
```

DATA(section2) = struct2+3(4). "Syntax error
