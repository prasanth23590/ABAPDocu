---
title: "Absolute Type Names"
source_file: abentype_names.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Absolute Type Names

## Syntax Forms

**Global Context**

``` abap
  \TYPE=type_ name[\LINE][-comp] 
| \CLASS=class_name 
| \INTERFACE=intf_name
```

**Global Class/Interface Context**

``` abap
  \clif\TYPE=type_ name[\LINE][-comp]
```

**Program Context**

``` abap
  \prog\TYPE=type_ name[\LINE][-comp] 
| \prog\CLASS=class_name 
| \prog\INTERFACE=intf_name
```

**Local Class/Interface Context**

``` abap
  \prog\clif\TYPE=type_ name[\LINE][-comp]
```

**Procedure Context**

``` abap
  \clif\meth\TYPE=type_ name[\LINE][-comp] 
| \prog\clif\meth\TYPE=type_ name[\LINE][-comp] 
| \prog\proc\TYPE=type_ name[\LINE][-comp]
```

### Alternative

[1. `Global Context`](abentype_names.md#alternative-1)

[2. `Global Class/Interface Context`](abentype_names.md#alternative-2)

[3. `Program Context`](abentype_names.md#alternative-3)

[4. `Local Class/Interface Context`](abentype_names.md#alternative-4)

[5. `Procedure Context`](abentype_names.md#alternative-5)

### Addition

[`... [\LINE][-comp]`](abentype_names.md#addition)

## Overview

### Description

Absolute type names are [character strings](../../abap-glossary/abencharacter_string_glosry.md) that uniquely specify a user-defined [data type](../../abap-glossary/abendata_type_glosry.md) in its [context](../../abap-glossary/abenobj_context_glosry.md). Absolute type names can be composed from scratch or obtained from [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md) and used in dynamic type specifications.

An absolute type name is composed of the following components that must form a path specification leading to a data type named `type_name`, a class named `class_name` or an interface named `intf_name`:

- `\TYPE=type_name[\LINE][-comp]`

  Specifies a [data type](../../abap-glossary/abendata_type_glosry.md) `type_name` optionally followed by

  - `\LINE` to specify the [line type](../../abap-glossary/abenrow_type_glosry.md) of an [internal table](../../abap-glossary/abeninternal_table_glosry.md) type

  - `-comp` to specify the data type of a [component](../../abap-glossary/abenstructure_component_glosry.md) of a [structured type](../../abap-glossary/abenstructured_type_glosry.md)

- `\CLASS=class_name`

  Specifies a [class](../../abap-glossary/abenclass_glosry.md) `class_name`.

- `\INTERFACE=intf_name`

  Specifies an [interface](../../abap-glossary/abenoo_intf_glosry.md) `intf_name`.

- `\PROGRAM=prog_name`

  Specifies an [ABAP program](../../abap-glossary/abenabap_program_glosry.md) `prog_name`.

- `\CLASS-POOL=class_name`

  Specifies the [class pool](../../abap-glossary/abenclass_pool_glosry.md) of a class `class_name`.

- `\FUNCTION-POOL=fp_name`

  Specifies a [function pool](../../abap-glossary/abenfunction_pool_glosry.md) `fp_name`.

- `\METHOD=meth_name`

  Specifies a [method](../../abap-glossary/abenmethod_glosry.md) `meth_name`.

- `\FUNCTION=func_name`

  Specifies a [function module](../../abap-glossary/abenfunction_module_glosry.md) `func_name`.

The last component of a path must always be one of the following:

- `\TYPE=type_name[\LINE][-comp]`

- `\CLASS=class_name`

- `\INTERFACE=intf_name`

The following sections explain the usage of these components for composing path expressions for different contexts.

Absolute type names can be used in all statements in which dynamic specification of a data type, a class, or an interface is possible. The case sensitivity depends on the statement.

### Hints

- Absolute type names provide an alternative to the regular type names that can be used statically in ABAP statements for user-defined (i.e. not built-in) types. Those type names are [relative type names](../../abap-glossary/abenrelative_type_name_glosry.md) that are only valid in relation to their context. For example, a type name `my_type` defined with `TYPES` in a context can be only be used within this context to address the respective type. The same applies to classes and interfaces. Refer also to [Validity and Visibility](abenlifetime_and_visibility.md).

- Usage types for absolute type names are:

  - Access to global types that are hidden by local types

  - Access to data types, classes, and interfaces of other programs. When a different program is accessed, it is loaded into the current [internal session](../../abap-glossary/abeninternal_session_glosry.md) if required.

- A data type is uniquely identified by its absolute type name. However, there are different ways of forming a unique path for a type.

- A data type that only exists as a [bound data type](../../abap-glossary/abenbound_data_type_glosry.md) of a data object and, therefore, does not have a relative type name, has an internal [technical type name](../../abap-glossary/abentechnical_type_name_glosry.md). Such a technical type name can also be part of an absolute type and can be retrieved by [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md). In the ABAP language version [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md) it cannot be used in dynamic type specifications.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Composing an absolute type name for a data type defined in a method of a local class. The type name is used for creating an anonymous data object. The absolute type name of the anonymous data object retrieved by [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md) is *\PROGRAM=...\CLASS=CLS\METHOD=METH\TYPE=C100* and matches the composed one.

``` abap
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    METHODS meth. 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD meth. 
    TYPES c100 TYPE c LENGTH 100. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
 
CLASS demo IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    DATA dref TYPE REF TO data. 
 
    DATA(type_name) = 
      `\PROGRAM=` && sy-repid && 
      `\CLASS=cls` && 
      `\METHOD=meth` && 
      `\TYPE=c100`. 
 
    TRY. 
        CREATE DATA dref TYPE (type_name). 
        dref->* = 'Success'. 
        out->write( dref ). 
      CATCH cx_sy_create_data_error INTO DATA(exc). 
        out->write( exc->get_text( ) ). 
    ENDTRY. 
 
    out->write( 
      cl_abap_typedescr=>describe_by_data( dref->* )->absolute_name ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

When the methods `m1` and `m2` of the class `c1` are called in the following example, the RTTS return the absolute type names `\TYPE=SPFLI` or `\PROGRAM=...\CLASS=CLS\METHOD=M2\TYPE=SPFLI` for the generically typed parameter `p`. The use of the name `spfli` has a different meaning in the methods `m1` and `m2`. This is also indicated by a syntax check warning.

``` abap
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    METHODS: m1, 
      m2, 
      m3 IMPORTING p TYPE any. 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD m1. 
    DATA struc TYPE spfli. 
    m3( struc ). 
  ENDMETHOD. 
  METHOD m2. 
    TYPES spfli TYPE spfli ##SHADOW[SPFLI]. 
    DATA struc TYPE spfli. 
    m3( struc ). 
  ENDMETHOD. 
  METHOD m3. 
    DATA type_descr TYPE REF TO cl_abap_typedescr. 
    type_descr = cl_abap_typedescr=>describe_by_data( p ). 
    cl_demo_output=>write( type_descr->absolute_name ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD main. 
    DATA(ref) = NEW cls( ). 
    ref->m1( ). 
    ref->m2( ). 
    cl_demo_output=>display( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Alternative 1

` \TYPE=type_name[\LINE][-comp]`

`| \CLASS=class_name`

`| \INTERFACE=intf_name`

### Description

Absolute type names for a

- data type `type_name` from the ABAP Dictionary or ABAP CDS

- global class `class_name` from the class library

- global interface `intf_name` from the class library

The path consists of one component only.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The absolute type names of global types are retrieved with [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md). The output is

``` abap
\TYPE=SCARR 
\TYPE=DEMO_CDS_NULL 
\CLASS=CL_ABAP_DOCU 
\INTERFACE=IF_ABAP_DOCU
```abap
FINAL(out)  = cl_demo_output=>new( ). 
 
out->write( cl_abap_typedescr=>describe_by_name( 'SCARR' 
             )->absolute_name 
  )->write( cl_abap_typedescr=>describe_by_name( 'DEMO_CDS_NULL' 
             )->absolute_name 
  )->write( cl_abap_typedescr=>describe_by_name( 'CL_ABAP_DOCU' 
             )->absolute_name 
  )->write( cl_abap_typedescr=>describe_by_name( 'IF_ABAP_DOCU' 
             )->absolute_name ). 
 
out->display( ).
```

## Alternative 2

`\clif\TYPE=type_ name[\LINE][-comp]`

### Description

Absolute type name for a data type `type_name` defined in a global class or a global interface. `\clif` must be one of the following:

- `\CLASS=class_name`, name of the global class

- `\INTERFACE=intf_name`, name of the global interface

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The absolute type names of types defined in an interface and a class are retrieved with [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md). The output is

``` abap
\INTERFACE=IF_DEMO_INTERFACE_POOL\TYPE=CHAR20 
\CLASS=CL_DEMO_CLASS_POOL\TYPE=CHAR20
```abap
FINAL(out)  = cl_demo_output=>new( ). 
 
DATA: 
  text1 TYPE if_demo_interface_pool=>char20, 
  text2 TYPE cl_demo_class_pool=>char20. 
 
out->write( 
  cl_abap_typedescr=>describe_by_data( text1 
    )->absolute_name 
  )->write( 
  cl_abap_typedescr=>describe_by_data( text2 
      )->absolute_name ). 
 
out->display( ).
```

## Alternative 3

` \prog\TYPE=type_ name[\LINE][-comp]`

`| \prog\CLASS=class_name`

`| \prog\INTERFACE=intf_name`

### Description

Absolute type name for a class `class_name`, an interface `intf_name` or data type `type_name` defined in the [global declaration part](../../abap-glossary/abenglobal_declaration_sect_glosry.md) of a program. `\prog` must be one of the following:

- `\PROGRAM=prog_name`

  For `prog_name`, any technical program name that denotes a [compilation unit](../../abap-glossary/abencompilation_unit_glosry.md) can be used. The names of [include programs](../../abap-glossary/abeninclude_program_glosry.md) cannot be used.

- `\CLASS-POOL=class_name`

  For `class_name`, any global class can be used. The specified program is the [class pool](../../abap-glossary/abenclass_pool_glosry.md) of that class. The local classes, interfaces and data types as well as the global class of the class pool can be specified.

- `\FUNCTION-POOL=fp_name`

  For `fp_name`, any [function pool](../../abap-glossary/abenfunction_pool_glosry.md) (without the prefix `SAPL`) can be used.

### Hints

- Besides `class_name` or `\fp_name`, the technical name `prog_name` of the ABAP program can also be specified behind `\PROGRAM` for classes, interfaces, and data types in a [class pool](../../abap-glossary/abenclass_pool_glosry.md) or [function pool](../../abap-glossary/abenfunction_pool_glosry.md). Since the latter is usually not known, it is recommended that `\CLASS-POOL` or `\FUNCTION-POOL` are used.

- Since an [interface pool](../../abap-glossary/abeninterface_pool_glosry.md) cannot contain definitions outside its global interface, it cannot be specified by `\INTERFACE-POOL`. In order to address the global interface and its components, `\INTERFACE` can be used. The technical name of the interface pool can be used behind `\PROGRAM`, but this is not recommended.

- Access to [test classes](../../abap-glossary/abentest_class_glosry.md) using absolute type names is not allowed.

- Absolute names of [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) have a [specific pattern](../../abap-rap-business-objects/abap-for-rap-business-objects/abapderived_types_dynamic.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Both absolute type names denote the type `char10` defined in the [CCDEF include](../../abap-glossary/abenccdef_glosry.md) of the global class `CL_DEMO_CLASS_POOL`.

- The first one uses `\CLASS_POOL` with the name of the global class.

- The second one uses `\PROGRAM` with the technical name of the class pool.

The [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md) method returns a path with `\CLASS_POOL` in both cases.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA dref TYPE REF TO data. 
 
DATA(type_name) = `\CLASS-POOL=cl_demo_class_pool\TYPE=char10`. 
CREATE DATA dref TYPE (type_name). 
out->write( 
cl_abap_typedescr=>describe_by_data( 
  dref->* )->absolute_name ). 
 
type_name = `\PROGRAM=cl_demo_class_pool============cp\TYPE=char10`. 
CREATE DATA dref TYPE (type_name). 
out->write( 
cl_abap_typedescr=>describe_by_data( 
  dref->* )->absolute_name ). 
 
out->display( ).
```

## Alternative 4

`\prog\clif\TYPE=type_ name[\LINE][-comp]`

### Description

Absolute type name for a data type `type_name` defined in a local class or interface of a program. The same applies to `\prog` as in the previous alternative. `\clif` must be one of the following:

- `\CLASS=class_name`, name of the local class

- `\INTERFACE=intf_name`, name of the local interface

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Absolute type names are used

- to create an anonymous data object with a type defined in a local class `demo` of the [CCIMP include](../../abap-glossary/abenccimp_glosry.md) of the global class

- to create an object of this local class.

The method `meth` of this class is called dynamically, where the anonymous data object serves as an actual parameter with the correct type. Note the different case sensitivity when creating data objects and instances of classes.

The absolute type name for the [test class](../../abap-glossary/abentest_class_glosry.md) `TEST_DEMO` of the class pool cannot be used for creating an object. Instead, an exception is raised.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA dref TYPE REF TO data. 
DATA oref TYPE REF TO object. 
 
FINAL(type_name) = 
  `\CLASS-POOL=cl_demo_class_pool\CLASS=DEMO\TYPE=char30`. 
CREATE DATA dref TYPE (type_name). 
 
DATA(class_name) = 
  `\CLASS-POOL=CL_DEMO_CLASS_POOL\CLASS=DEMO`. 
CREATE OBJECT oref TYPE (class_name). 
 
CALL METHOD oref->('METH') 
  RECEIVING 
    text = dref->*. 
out->write( dref->* ). 
 
TRY. 
    class_name = 
      `\CLASS-POOL=CL_DEMO_CLASS_POOL\CLASS=TEST_DEMO`. 
    CREATE OBJECT oref TYPE (class_name). 
  CATCH cx_sy_create_object_error INTO FINAL(exc). 
    out->write( exc->get_text( ) ). 
ENDTRY. 
 
 
out->display( ).
```

## Alternative 5

` \clif\meth\TYPE=type_ name[\LINE][-comp]`

`| \prog\clif\meth\TYPE=type_ name[\LINE][-comp]`

`| \prog\proc\TYPE=type_ name[\LINE][-comp]`

### Description

Absolute type name for a data type `type_name` defined in a [procedure](../../abap-glossary/abenprocedure_glosry.md).

- `\clif\meth` specifies a method in a global class or interface. The same applies to `\clif` as for the respective alternative. `\meth` must be:

  - `\METHOD=meth_name`

- `\prog\clif\meth` specifies a method in a local class or interface. The same applies to `prog\clif` as for the respective alternative. `\meth` must be:

  - `\METHOD=meth_name`

- `\prog\proc` specifies a function module defined in a program.

  `\prog` can be one of the following:

  - `\PROGRAM=prog_name`

  - `\FUNCTION-POOL=fp_name`

    `\proc` can be one of the following:

  - `\FUNCTION=func_name`

The specification of a function pool for a type in a function module can be omitted because each function module is unique.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Absolute type names for types defined in methods. The first method is a component of the global class `CL_DEMO_CLASS_POOL`. The second method is a component of a local class defined in the [CCIMP include](../../abap-glossary/abenccimp_glosry.md) of its class pool.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA dref TYPE REF TO data. 
 
DATA(type_name) = `\CLASS=cl_demo_class_pool\METHOD=meth\TYPE=char10`. 
CREATE DATA dref TYPE (type_name). 
out->write( 
cl_abap_typedescr=>describe_by_data( 
  dref->* )->absolute_name ). 
 
type_name = 
  `\CLASS-POOL=cl_demo_class_pool\CLASS=demo\METHOD=meth\TYPE=char16`. 
CREATE DATA dref TYPE (type_name). 
out->write( 
cl_abap_typedescr=>describe_by_data( 
  dref->* )->absolute_name ). 
 
out->display( ).
```

## Addition

`... [\LINE][-comp]`

### Description

If a path is terminated with `\TYPE=type_name`, the [line type](../../abap-glossary/abenrow_type_glosry.md) of an internal table type or the data type of a component of a structured type can be specified as follows:

- `\LINE`

  If the data type denoted by `type_name` is an [internal table](../../abap-glossary/abeninternal_table_glosry.md) type, its [line type](../../abap-glossary/abenrow_type_glosry.md) can be specified by `\LINE`.

- `-comp`

  If the data type denoted by `type_name` or the line type denoted by `\LINE` is structured, the type of one of its components can be specified by `-comp` where `comp` is the component name.

`\LINE` and `-comp` cannot be used behind [technical type names](../../abap-glossary/abentechnical_type_name_glosry.md) of data types that only exist as a [bound data type](../../abap-glossary/abenbound_data_type_glosry.md) of a data object.

### Hint

The specification `\LINE` is more like a component selector than a component of the path. It does not precede `=type_name` but follows it in the same way as the structure component selector `-comp`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Using the type names of structured and tabular data objects to compose absolute type names for a structure component and a table line. While the absolute names retrieved from data objects `struc` and `itab1` contain the complete types `struc` and `itab1` of the program, the absolute name retrieved from `itab2` contains the [technical type name](../../abap-glossary/abentechnical_type_name_glosry.md) of this internal table. Since the data type `itab2` is generic (no key definition), a complete type with the standard key is constructed with the `DATA` statement as a [bound data type](../../abap-glossary/abenbound_data_type_glosry.md). Its technical type name cannot be used with `\LINE` and an exception is raised.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES struc TYPE scarr. 
TYPES itab1 TYPE TABLE OF scarr WITH EMPTY KEY. 
TYPES itab2 TYPE TABLE OF scarr. 
 
DATA struc TYPE struc. 
DATA itab1 TYPE itab1. 
DATA itab2 TYPE itab2. 
 
DATA dref TYPE REF TO data. 
 
FINAL(comp_type) = 
  cl_abap_typedescr=>describe_by_data( struc 
    )->absolute_name && '-carrid'. 
TRY. 
    CREATE DATA dref TYPE (comp_type). 
    out->write( 'Data object with type of component created' ). 
  CATCH cx_sy_create_data_error INTO DATA(exc). 
    out->write( exc->get_text( ) ). 
ENDTRY. 
 
FINAL(line_type1) = 
  cl_abap_typedescr=>describe_by_data( itab1 
    )->absolute_name && '\LINE'. 
TRY. 
    CREATE DATA dref TYPE (line_type1). 
    out->write( 'Data object with type of table line created' ). 
  CATCH cx_sy_create_data_error INTO exc. 
    out->write( exc->get_text( ) ). 
ENDTRY. 
 
FINAL(line_type2) = 
  cl_abap_typedescr=>describe_by_data( itab2 
    )->absolute_name && '\LINE'. 
TRY. 
    CREATE DATA dref TYPE (line_type2). 
    out->write( 'Data object with type of table line created' ). 
  CATCH cx_sy_create_data_error INTO exc. 
    out->write( exc->get_text( ) ). 
ENDTRY. 
 
 
out->display( ).
```

### Executable Example

[Absolute Type Names](abenabs_type_names_abexa.md)
