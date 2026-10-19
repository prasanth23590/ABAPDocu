---
title: "DATA, data_options"
source_file: abapdata_options.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects > DATA"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DATA, data_options

## Syntax

``` abap
... [ VALUE val|{IS INITIAL} ] 
    [ READ-ONLY ].  
```

### Addition

[1. `... VALUE val|{IS INITIAL}`](abapdata_options.md#addition-1)

[2. `... READ-ONLY`](abapdata_options.md#addition-2)

## Overview

### Description

The additions `VALUE` and `READ-ONLY` are specifically for data objects and distinguish the `DATA` syntax from the `TYPES` syntax.

## Addition 1

`... VALUE val|{IS INITIAL}`

### Description

The addition `VALUE` can be used to define a [start value](../../abap-glossary/abenstart_value_glosry.md) `val` for the content of a variable for all forms of the variable declaration. This value is used to initialize the variable when it is created before [`LOAD-OF-PROGRAM`](../abap-program-structure/abapload-of-program.md). The addition `VALUE` is not allowed in the declaration part of an interface for the statement `DATA`.

The start value `val` can either be specified as a literal or as a constant. Constants, rather than using the actual value, work like the literal that is specified after `VALUE` when it is declared. If the data type of the literal does not match the data type of the declaration, it is usually converted in accordance with the [conversion rules](../abap-processing-internal-data/abenconversion_elementary.md) for elementary data types during program generation when the program is activated. If the literal cannot be converted to the data type, an exception is raised when the program is generated instead.

Without the addition `VALUE`, or if `IS INITIAL` is specified, the content is initial. The [initial values](../../abap-glossary/abeninitial_value_glosry.md) depend on the data type.

The initial values of elementary types are dependent on the [built-in ABAP types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md). In the case of initial structures, the components are initial, initial reference variables contain the [null reference](../../abap-glossary/abennull_reference_glosry.md), which does not point to an object, and initial internal tables do not contain any lines.

The addition `VALUE` is possible for all data types, particularly for the [deep](../../abap-glossary/abendeep_glosry.md) types (strings, reference types, table types, or structured types with deep components, including [boxed components](../../abap-glossary/abenboxed_component_glosry.md)). A start value `val`, however, can only be specified for the ABAP types `string` and `xstring`. Otherwise, only `IS INITIAL` is possible. `IS INITIAL` is also the only possible start value for structures with non-character-like and flat components.

### Hints

- A start value should be specified according to type. In particular, no values that are longer can be specified and, in the case of certain data types such as `d` and `t`, the length must match exactly.

- If numbers with [decimal places](../../abap-glossary/abendecimal_place_glosry.md) are specified or specified as a start value for data objects of the data types `p` or `f` in scientific notation with mantissa and exponents, it should be ensured that there are no literals for these numbers. Instead, the character literals must be specified with the appropriate content. These are then converted into the numeric data type in accordance with the conversion rules for elementary data types. The same applies to byte-like data objects.

- If the data object is character-like, the [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) `val1`, `val2`, ... of the value set of an [enumerated type](abaptypes_enum.md) `enum` can also be specified for `val`. The constant then is given the name of the enumerated constant as its value.

- The [value operator](../../abap-glossary/abenvalue_operator_glosry.md) [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) can also be used to construct the content of complex data objects (structures, internal tables).

- In the [declaration part](../../abap-glossary/abendeclaration_part_glosry.md) of [global classes](../../abap-glossary/abenglobal_class_glosry.md) the character representation of default values is limited to 132 characters. When you work in [ADT](../../abap-glossary/abenabap_dev_envir_glosry.md), exceeding characters will not be truncated. However, a syntax warning appears.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of data by specifying the initial value, where one value is specified by a constant.

``` abap
CONSTANTS underscores TYPE string VALUE `__________`. 
 
DATA: 
  num TYPE i       VALUE 123, 
  txt TYPE string  VALUE underscores, 
  hex TYPE xstring VALUE `0123456789ABCDEF`.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates that if a constant is used after `VALUE`, the literal that is specified after the `VALUE` addition of the constant declaration is evaluated. The variable `text1` is given the full content of the literal while the variable `text2` is assigned the value of the constant that contains only the digits of the literal and any leading zeros in accordance with the [conversion rule](../abap-processing-internal-data/abencharacter_source_fields.md) from `c` to `n`.

``` abap
 
CONSTANTS 
  const TYPE n LENGTH 10 VALUE 'x1x1x1x'. 
 
TYPES 
  text TYPE c LENGTH 10. 
 
DATA: 
  text1 type text VALUE const, 
  text2 TYPE text. 
 
text2 = const. 
 
cl_demo_output=>display( 
  |text1: { text1 }\ntext2: { text2 }| ).
```

## Addition 2

`... READ-ONLY`

### Description

This addition is always possible in the [public](../../abap-glossary/abenpublic_glosry.md) visibility section class or in an interface. This addition ensures that an attribute declared using `DATA` can be read from outside of the class but can only be changed using methods of the class or its subclasses. This addition has no effect on the [friends](../../abap-glossary/abenfriend_glosry.md) of the class.

A class attribute defined using `READ-ONLY` can be used outside of the class, its friends, and subclasses only in [read positions](../../abap-glossary/abenread_position_glosry.md) in ABAP statements.

### Hints

- If a read-only attribute is a [reference variable](../../abap-glossary/abenreference_variable_glosry.md), the read-only property concerns the [reference](../../abap-glossary/abenreference_glosry.md) but not the content of the object referred by the reference. A read-only reference variable followed by the [object component selector](../../abap-glossary/abenobject_component_select_glosry.md) (`->`) can be used in [write positions](../../abap-glossary/abenwrite_position_glosry.md).

- The declaration of attributes using the addition `READ-ONLY` does not prevent methods of the class from passing [references](../../abap-glossary/abenreference_glosry.md) to these attributes externally as [reference variables](../../abap-glossary/abenreference_variable_glosry.md) or [field symbols](../../abap-glossary/abenfield_symbol_glosry.md) and therefore making the attributes modifiable outside of the class.

- The addition `READ-ONLY` is always recommended if attributes need to be invisible, but a `GET` method is not executed for every read for performance reasons.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of the static constructor as the factory method of a class with instances created privately. The reference to the created singleton objects is available in the `READ-ONLY` attribute `clsref`.

``` abap
CLASS cls DEFINITION CREATE PRIVATE. 
  PUBLIC SECTION. 
    CLASS-DATA clsref TYPE REF TO cls READ-ONLY. 
    CLASS-METHODS 
      class_constructor. 
    ... 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD class_constructor. 
    IF clsref IS INITIAL. 
      clsref = NEW #( ). 
    ENDIF. 
  ENDMETHOD. 
  ... 
ENDCLASS.
```
