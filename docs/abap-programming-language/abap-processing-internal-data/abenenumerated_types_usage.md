---
title: "Enumerated Objects (enum)"
source_file: abenenumerated_types_usage.html
section: "ABAP Programming Language > ABAP - Processing Internal Data"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Enumerated Objects (enum)

This section summarizes the use of [enumerated objects](../../abap-glossary/abenenumerated_object_glosry.md), that is, data objects with [enumerated types](../../abap-glossary/abenenum_type_glosry.md).

- [Declaration](abenenumerated_types_usage.md#declaration)

- [Processing of Enumerated Objects](abenenumerated_types_usage.md#processing-of-enumerated-objects)

  - [Operand Positions for Enumerated Objects](abenenumerated_types_usage.md#operand-positions-for-enumerated-objects)

  - [Value Assignments](abenenumerated_types_usage.md#value-assignments)

  - [Comparisons](abenenumerated_types_usage.md#comparisons)

  - [Typing of Formal Parameters and Field Symbols](abenenumerated_types_usage.md#typing-of-formal-parameters-and-field-symbols)

  - [Access to the Enumerated Value](abenenumerated_types_usage.md#access-to-the-enumerated-value)

  - [Type Descriptions](abenenumerated_types_usage.md#type-descriptions)

  - [Data Interfaces](abenenumerated_types_usage.md#data-interfaces)

  - [ABAP SQL](abenenumerated_types_usage.md#abap-sql)

  - [Forbidden Uses](abenenumerated_types_usage.md#forbidden-uses)

  - [Example for General Use](abenenumerated_types_usage.md#example-for-general-use)

## Declaration

An enumerated object is a data object with an [enumerated type](../../abap-glossary/abenenum_type_glosry.md).

Enumerated types can be defined as follows:

- In the ABAP language, an enumerated type is defined using the following `TYPES` statements:

  [`TYPES BEGIN OF ENUM enum_type ...`](../abap-declarations/abaptypes_enum.md)

  [`TYPES val1 [VALUE IS INITIAL].`](../abap-declarations/abaptypes_enum.md)

  [`TYPES val2 [VALUE val].`](../abap-declarations/abaptypes_enum.md)

  ` ...`

  [`TYPES END OF ENUM enum_type ...`](../abap-declarations/abaptypes_enum.md) An enumerated type defined in ABAP can be used within the same program. Enumerated types defined as components of [interfaces (ABAP Objects)](../../abap-glossary/abenoo_intf_glosry.md) or [classes](../../abap-glossary/abenclass_glosry.md) can be used in all ABAP programs that are allowed to access them. The definition of an enumerated type in ABAP also declares its [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) and optionally an [enumerated structure](../../abap-glossary/abenenumerated_structure_glosry.md) in the context of the declaration. [Enumerated variables](../../abap-glossary/abenenumerated_variable_glosry.md) can be declared by referring to the enumerated type.

- In ABAP CDS, an enumerated type is defined using the following statement:

  [`DEFINE TYPE ... ENUM`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_enum_type.md) Enumerated types defined in ABAP CDS can be used in all ABAP CDS objects and ABAP programs that are allowed to access them. In an ABAP program, an CDS enumerated type is handled like an ABAP enumerated type with an [enumerated structure](../../abap-glossary/abenenumerated_structure_glosry.md) that has the same name as the enumerated type:

  - The CDS enumerated type can be used directly for the declaration of [enumerated variables](../../abap-glossary/abenenumerated_variable_glosry.md).

  - The enumerated structure and its components can be used in read positions.

    The enumerated structure is implicitly created in the global context of the current ABAP program before the first read access. After its creation, it can be used like an enumerated structure defined in ABAP. Especially, it can be referred to by `LIKE` which is not possible before the access to the CDS enumerated type. In contrast to an ABAP enumeration type, the components of the enumerated structure derived from an CDS enumerated structure are ordered alphabetically instead of following the order of the definition.

The technical data type of the content of an enumerated object is the [base type](../../abap-glossary/abenbase_type_glosry.md) of the enumerated type. The possible content is defined by the [enumerated values](../../abap-glossary/abenenumerated_value_glosry.md) defined using [`TYPES ... [VALUE]`](../abap-declarations/abaptypes_enum.md) in ABAP or by [`EnumConstant = EnumValue`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_enum_type.md) in ABAP CDS. Exactly one value must have the type-specific initial value. In ABAP, the base type is `i` by default, but it can also be a different elementary data type. In ABAP CDS, the base type must be specified and there is no default.

The following enumerated objects can be used in ABAP programs:

- **Enumerated variables**

  An [enumerated variable](../../abap-glossary/abenenumerated_variable_glosry.md) is a variable defined using [`DATA enum_var TYPE enum_type ...`](../abap-declarations/abapdata_enum.md) that can contain only [enumerated values](../../abap-glossary/abenenumerated_value_glosry.md) of the enumerated type. This is ensured by the ABAP runtime framework and the rules for using enumerated types described below.

- **Enumerated constants**

  An [enumerated constant](../../abap-glossary/abenenumerated_constant_glosry.md) is used to define a value in the value set of an enumerated type.

  - In ABAP, an enumerated constant is defined in the definition of an enumerated type with

    [`TYPES val ...`](../abap-declarations/abaptypes_enum.md) under the name `val`. It exists as `val` in the context where the enumerated type is defined.

  - In ABAP CDS, an enumerated constant is defined by the syntax

    [`EnumConstant = EnumValue`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_enum_type.md) An enumerated constant defined in ABAP CDS is handled in an ABAP program as a component of an [enumerated structure](../../abap-glossary/abenenumerated_structure_glosry.md) that has the name of the CDS enumerated type `EnumName`. This enumerated structure is created implicitly as an ABAP data object before a first read access. An enumerated constant contains the [enumerated value](../../abap-glossary/abenenumerated_value_glosry.md) assigned in the definition. It can be specified in all read positions in which enumerated objects are possible. Its enumerated value is either determined automatically as an integer or is specified explicitly in the definition.

- **Components of enumerated structures**

  A component of an [enumerated structure](../../abap-glossary/abenenumerated_structure_glosry.md) is a special form of an enumerated constant that exists as a component of a constant structure and not as a single data object.

  - For an ABAP enumerated type, an enumerated structure `struc` can be declared optionally using

    [`TYPES BEGIN OF ENUM enum_type STRUCTURE struc ...`](../abap-declarations/abaptypes_enum.md) Enumerated constants that are not components of an enumerated structure are elementary constants in their context.

  - For an CDS enumerated type, there is always an enumerated structure created in the ABAP program with the same name as the enumerated type `EnumName` before the first read access.

    Enumerated constants that are components of an enumerated structure must be addressed like any structure component with a component selector ([structure component selector](../../abap-glossary/abenstructure_component_sel_glosry.md) (`-` or [object component selector](../../abap-glossary/abenobject_component_select_glosry.md) `->`). The enumerated constants of a CDS enumerated type can only be accessed in ABAP as structure components. Otherwise, the same rules apply as to enumerated constants that are not components of enumerated structures.

### Hints

- Enumerated objects are mainly used to check allowed values. This usually restricts the actual parameters passed to methods to the enumerated values defined in the class.

- The base type and the actual enumerated value are almost always ignored when enumerated objects are used. Assignments and comparisons are usually only made between enumerated objects with the same enumerated type.

- As a rule, the base type and the actual enumerated values do not matter when enumerated objects are used. Base types other than `i` and the actual enumerated values may be significant in transformations between enumerated type or in migrations of previous concepts.

- Enumerated structures can be used to avoid naming conflicts if there are multiple enumerated types in a namespace. In the case of enumerated structures, it is possible to use the same enumerated constant name in multiple enumerated types.

- An enumerated type is always an elementary type independent from an enumerated structure. This is true for ABAP and especially for CDS enumerated types that are always connected to an enumerated structure.

- Normally, an enumerated structure should not be accessed as a whole and the order of its components is not important. Otherwise, the different order in ABAP enumerated types and CDS enumerated types must be respected.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of an enumerated type `size` in a class. The method parameter `size` has the enumerated type and only enumerated objects of this type can be passed to this parameter. This example show how the enumerated constant `demo=>l` is passed. This guarantees that only enumerated values of the enumerated type can be passed to the parameter. These can be evaluated in comparisons with the enumerated constants. In the `CASE` control structure shown here, the statement block after `WHEN OTHERS` can be reached only when `demo=>xl` and `demo=>xxl` are passed.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    TYPES: 
      BEGIN OF ENUM size, 
        s, m, l, xl, xxl, 
      END OF ENUM size. 
    CLASS-METHODS main 
      IMPORTING size TYPE size. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD main. 
    CASE size. 
      WHEN s. 
        ... 
      WHEN m. 
        ... 
      WHEN l. 
        ... 
      WHEN OTHERS. 
        ... 
    ENDCASE. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS user DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS user IMPLEMENTATION. 
  METHOD main. 
    demo=>main( demo=>l ). 
  ENDMETHOD. 
ENDCLASS.
```

### Executable Example

[enum, Declaration](abenenum_declaration_abexa.md)

## Processing of Enumerated Objects

The processing of enumerated objects is usually independent of the base type of the enumerated type. Only the enumerated type itself is relevant for all rules specified here. Assignments of enumerated objects with a numeric base type, for example, cannot be assigned to numeric target fields and cannot be compared with numeric fields. The enumerated value in the base type can be accessed using the constructor operators [`CONV`](abenconv_constructor_enum.md) and [`EXACT`](abenexact_constructor_enum.md) only.

### Operand Positions for Enumerated Objects

- Read positions

  Enumerated objects can be used in all [read positions](../abap-operands/abendata_objects_usage_reading.md) in which the operand type is their enumerated type or in which the operand is converted to one of the character-like types `c` or `string`. [Substring access](../abap-operands/abenoffset_length.md) is not possible.

- Write positions

  Enumerated variables can only be used in [write positions](../abap-operands/abendata_objects_usage_writing.md) in which the operand type is the enumerated type and only the associated enumerated values can be written. If known statically, an attempt to assign a value other than a valid enumerated value to an enumerated variable produces a syntax error. If not known statically, an exception is raised.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the first assignment, the enumerated constant `xl` in a read position is assigned to the enumerated variable `size` in a write position. The string expression in the second half exploits the fact that the enumerated constants are converted implicitly to the type `string` before the concatenation. The result is `SMLXLXXL`.

``` abap
TYPES: 
  BEGIN OF ENUM size, 
    s, m, l, xl, xxl, 
  END OF ENUM size. 
DATA size TYPE size. 
 
size = xl. 
 
FINAL(str) = s && m && l && xl && xxl.
```

### Value Assignments

Only enumerated objects with the same enumerated type can be assigned to an enumerated variable. In the assignment, the target field is given the enumerated value of the source field.

The initial value of the base type is always a valid enumerated value of an enumerated type. Accordingly, an enumerated variable can be set to the initial value of its base type using [`CLEAR`](abapclear.md). Assignments of [`VALUE enum_type( )`](../abap-creating-objects-and-values/abenvalue_constructor_params_init.md) are also possible.

Conversely, enumerated objects can only be assigned to compatible enumerated variables, with the following exception: There is a [conversion rule](abenconversion_enumerated.md) for assignments of enumerated objects to character-like variables of the types `c` and `string`. In this case, the target field is assigned the name of the enumerated constant or the component of the enumerated structure under which the enumerated value of the source field is defined in the enumerated type. Since this rule can produce unexpected results, conversions of this type lead to a message from the extended program check that can be hidden using the pragma `##types`.

In structures, each component with an enumerated type forms a separate fragment of the [structure fragment view](abenunicode_fragment_view.md). In assignments between structures of this type, the fragment views must match so that only components with the same enumerated type can be assigned to each other.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the first assignment, the enumerated constant `sz-xl` is assigned to the enumerated variable `size` of its enumerated type. This variable then contains the associated enumerated value 3. In the second assignment, the enumerated constant is assigned to the text string `size_string`. This string is given the value *XL* in accordance with the conversion rule.

``` abap
TYPES: 
  BEGIN OF ENUM size STRUCTURE sz, 
    s, m, l, xl, xxl, 
  END OF ENUM size STRUCTURE sz. 
 
DATA size TYPE size. 
size = sz-xl. 
 
DATA size_string TYPE string. 
size_string = sz-xl.
```

### Comparisons

For comparisons between enumerated objects, the [comparison rule](../abap-program-flow-logic/abenlogexp_rules_operands_enum.md) applies that an enumerated object can only be compared with an enumerated object with the same enumerated type. Here, the values of the operands are compared in accordance with their base type.

Each enumerated type has an initial enumerated value, which makes checks with the predicate expression [`IS INITIAL`](../abap-program-flow-logic/abenlogexp_initial.md) possible.

### Hint

Comparisons do not perform an implicit conversion of an enumerated object to the character-like types `c` and `string`. Conversions of this type must be performed explicitly, for example with the conversion operator [`CONV`](abenconstructor_expression_conv.md). This difference between assignments and comparisons is particularly significant when reading from internal tables using the statement [`READ TABLE`](abapread_table.md) or [table expressions](../../abap-glossary/abentable_expression_glosry.md) and the statement [`LOOP AT`](abaploop_at_itab_variants.md) or a [`FOR`](abenfor_itab.md) statement. When individual lines are read, the comparison fields of conditions are converted implicitly; this is not the case when multiple lines are read. Implicit conversions produce the message from the extended program check mentioned above.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first comparison shows a typical case where an enumerated variable is compared with an enumerated constant. The syntax of the second comparison that is in a comment is not possible. In the third comparison, the enumerated variable is converted explicitly to the type `string` before the comparison with a text string.

``` abap
TYPES: 
  BEGIN OF ENUM size, 
    s, m, l, xl, xxl, 
  END OF ENUM size. 
DATA size TYPE size. 
 
... 
 
IF size = xl. 
ENDIF. 
 
"IF size = `XL`. "<--- Syntax error 
"ENDIF. 
 
IF CONV string( size ) = `XL`. 
ENDIF.
```

### Typing of Formal Parameters and Field Symbols

If [formal parameters](../../abap-glossary/abenformal_parameter_glosry.md) of procedures or [field symbols](../../abap-glossary/abenfield_symbol_glosry.md) are [typed](../abap-declarations/abentyping.md) with an enumerated type, only enumerated objects with the same enumerated type can be assigned to them. As usual, an exception to this are return values of functional methods that can also be converted to character-like objects of the types `c` and `string`.

Enumerated types are covered by the generic types [`any`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md), [`data`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md), and [`simple`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md). When an enumerated object is passed to generically typed formal parameters or in assignments to generically typed field symbols, they inherit the enumerated type. In assignments to field symbols, no castings with the [`CASTING`](abapassign_casting.md) addition can be performed and an enumerated type cannot be specified after this addition.

When using generically typed formal parameters or field symbols for enumerated objects, the restriction applies that at [read positions](../../abap-glossary/abenread_position_glosry.md) where a statically known [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) is expected, only statically known operands of the same [enumerated type](../../abap-glossary/abenenumerated_type_glosry.md) are allowed. This affects, for example, the source field of an assignment to an [enumerated variable](../../abap-glossary/abenenumerated_variable_glosry.md) or an operand that is compared with an enumerated object. In [write positions](../../abap-glossary/abenwrite_position_glosry.md) for enumerated objects, however, generic formal parameters or field symbols are allowed for enumerated types. If the operand type is not known statically, the check is only made at runtime in read positions as well.

### Executable Example

[enum, Parameter Passing](abenenum_formal_para_abexa.md)

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The field symbol `fs1` typed generically with `simple` cannot be assigned to an enumerated variable `size` known statically or compared with it. An assignment of `size` to the field symbol and fully generic handling is, however, possible.

``` abap
TYPES: 
  BEGIN OF ENUM size, 
    s, m, l, xl, xxl, 
  END OF ENUM size. 
 
FIELD-SYMBOLS <fs1> TYPE simple. 
FIELD-SYMBOLS <fs2> TYPE simple. 
 
FINAL(size) = xl. 
 
ASSIGN size TO <fs1>. 
ASSIGN size TO <fs2>. 
 
<fs1> = size. 
"size = <fs1>.        "<--- Syntax error 
"ASSERT size = <fs1>. "<--- Syntax error 
 
<fs2> = <fs1>. 
ASSERT <fs1> = <fs2>.
```

### Access to the Enumerated Value

A special [rule](abenconv_constructor_enum.md) for the conversion operator [`CONV`](abenconstructor_expression_conv.md) applies when accessing the enumerated value of an enumerated object:

[`... CONV base_type( enum_dobj ) ...`](abenconv_constructor_enum.md)

If the base type `base_type` of an enumerated object `enum_dobj` specified as an operand is specified directly or indirectly, `CONV` returns its enumerated value.

Conversely, a valid enumerated value can be converted to an enumerated object:

[`... CONV enum_type( dobj ) ...`](abenconv_constructor_enum.md)

The operand `dobj` is converted to the base type of the enumerated type `enum_type` and `CONV` returns an enumerated object with this value. Any invalid values raise an exception.

In combinations of these two variants where `CONV base_type( enum_dobj )` is used as an operand `dobj` of `CONV enum_type( dobj )`, there is a short form:

[`... CONV enum_type( enum_dobj ) ...`](abenconv_constructor_enum.md)

Provided that different enumerated types can have the same base type, an enumerated object of an enumerated type can be converted to the corresponding enumerated object of a different enumerated type.

### Hint

The corresponding [rules](abenexact_constructor_enum.md) applies to the lossless operator [`EXACT`](abenconstructor_expression_exact.md), whereby additional losslessness checks are made.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The inner conversion operator `CONV` accesses the current enumerated value of the enumerated object `size` and returns it in the type `i`. The outer conversion operator `CONV` converts the result of the addition back to an enumerated type and assigns this enumerated value to the enumerated variable `size`. The enumerated value in `size` is raised by one for each iteration. The final result is the value of the enumerated constant `xxl`.

``` abap
TYPES: 
  BEGIN OF ENUM size, 
    s, m, l, xl, xxl, 
  END OF ENUM size. 
 
DATA size TYPE size. 
 
DO 4 TIMES. 
  size = CONV #( CONV i( size ) + 1 ). 
ENDDO.
```

### Type Descriptions

The type returned by the statement `DESCRIBE FIELD` for an enumerated object is `k`. The length is the length of the enumerated values in the basis type in bytes.

In [RTTS](../../abap-glossary/abenrun_time_type_services_glosry.md), enumerated objects are described by objects of the class `CL_ABAP_ENUMDESCR`. This class can be used for [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md) and [RTTC](../../abap-glossary/abenrun_time_type_creation_glosry.md) purposes. Like any enumerated type, an enumerated type created using RTTC is only compatible with itself.

The following attributes exist in a type description of the class `CL_ABAP_ENUMDESCR`:

- `KIND` always has the value *E* for the elementary base type

- `TYPE_KIND` always has the value *k* as in the statement `DESCRIBE FIELD`

- `BASE_TYPE_KIND` describes the base type

- `MEMBERS` is a table of the enumerated constants and the associated enumerated values

### Hint

A [CDS enumerated type](../../abap-glossary/abencds_enum_type_glosry.md) can be described directly with the RTTI method `DESCRIBE_BY_NAME`.

### Executable Example

[Enumerated Objects, Type Description](abenenum_description_abexa.md)

### Data Interfaces

The following data interfaces support enumerated types:

The character-like representation of enumerated objects, that is, the result of a `c` or `string`, is used for their output and serialization. The output consists of the name with a maximum of thirty characters of the enumerated constant of the current enumerated value in uppercase. Deserializations are performed in the reverse direction. The following are supported:

- [Data clusters](../../abap-glossary/abendata_cluster_glosry.md) with the statements [`EXPORT`](../abap-data-cluster/abapexport_data_cluster.md) and [`IMPORT`](../abap-data-cluster/abapimport_data_cluster.md). When an enumerated object is exported, the enumerated value is stored in the base type and flagged as an enumerated value. Enumerated objects and exported data objects of the base type can be imported to a suitable enumerated object (the value is checked here). No exported enumerated objects, however, can be imported to data objects of the base type.

- ABAP file interface with the statements `TRANSFER` and `READ DATASET`. In writes and reads to and from a file, enumerated objects are handled like data objects of their base type. In reads from a file to an enumerated object, the system checks whether it is a valid enumerated value.

- Serializations and deserializations from and to [XML](../../abap-glossary/abenxml_glosry.md) and [JSON](../../abap-glossary/abenjson_glosry.md). The formats [asXML](../abap-data-interchange-formats/abenabap_xslt_asxml_enum.md) and [asJSON](../abap-data-interchange-formats/abenabap_asjson_abap_types_enum.md) represent the content of enumerated objects in their character-like representation, that is, the name of the enumerated constant of the current enumerated value. Only valid names are allowed in deserializations to an enumerated object.

### Hint

A deserialization of a name of an enumerated constant is one of the few ways of creating an enumerated value from the name fully dynamically.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Enumerated objects in data clusters. The exported enumerated object `one` as well as the normal numeric literal `2` can be imported into an enumerated variable `enum_var`. But the exported enumerated object `one` cannot be imported into a normal numeric variable using the `IMPORT` statement.

``` abap
TYPES: 
  BEGIN OF ENUM enum, 
    zero, 
    one, 
    two, 
  END OF ENUM enum. 
 
FINAL(out) = cl_demo_output=>new( ). 
 
DATA data_buffer TYPE xstring. 
EXPORT p_enum = one p_num = 2 TO DATA BUFFER data_buffer. 
 
DATA enum_var TYPE enum. 
TRY. 
    IMPORT p_enum = enum_var FROM DATA BUFFER data_buffer. 
    DATA(subrc) = sy-subrc. 
  CATCH  cx_sy_import_mismatch_error. 
    subrc = 8. 
ENDTRY. 
IF subrc = 0. 
  out->write( enum_var ). 
ENDIF. 
TRY. 
    IMPORT p_num = enum_var FROM DATA BUFFER data_buffer. 
    subrc = sy-subrc. 
  CATCH  cx_sy_import_mismatch_error. 
    subrc = 8. 
ENDTRY. 
IF subrc = 0. 
  out->write( enum_var ). 
ENDIF. 
 
DATA num TYPE i. 
TRY. 
    IMPORT p_enum = num FROM DATA BUFFER data_buffer. 
  CATCH  cx_sy_import_mismatch_error INTO DATA(exc1). 
    out->write( exc1->get_text(  ) ). 
ENDTRY. 
 
 
out->display( ).
```

### Executable Example

[Enumerated Objects, Deserialization](abenenum_deserialization_abexa.md)

### ABAP SQL

[CDS enumerated elements](../../abap-glossary/abencds_enum_element_glosry.md), [CDS enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md), and [host variables](../../abap-glossary/abenhost_variable_glosry.md) typed with a [CDS enumerated type](../../abap-glossary/abencds_enum_type_glosry.md) can be used in ABAP SQL as elementary operands (column specifications, host variables and operands of host expressions). They can also be used in cast expressions.

## Restriction

Host variables and operands of host expressions can have a [CDS enumerated type](../../abap-glossary/abencds_enum_type_glosry.md) but not an [ABAP enumerated type](../../abap-glossary/abenenumerated_type_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following `SELECT` statement uses CDS enumerated elements, CDS enumerated constants, and a host variable typed with a CDS enumerated type in different operand positions.

``` abap
DATA fri TYPE demo_cds_enum_weekday. 
SELECT Id, friday, EnumConstantField, @fri as HostEnum 
       FROM demo_cds_enum_type_usage_2( 
         p1 = @demo_cds_enum_char-first_value ) 
       WHERE friday = @demo_cds_enum_weekday-fri 
       ORDER BY @demo_cds_enum_char-initial_value 
       INTO TABLE @FINAL(itab).
```

The following example defines an enumerated variable with reference to an ABAP enumerated type. This enumerated variable cannot be used as host variable in a `SELECT` statement.

``` abap
TYPES: 
  BEGIN OF ENUM abap_wd STRUCTURE abap_wd BASE TYPE int1, 
    mon, 
    tue, 
    wed, 
    thu, 
    fri, 
    sat, 
    sun, 
  END OF ENUM abap_wd STRUCTURE abap_wd. 
 
DATA fri TYPE abap_wd. 
*syntax error because host variables with an ABAP enumerated type 
*are not possible. 
*SELECT @fri AS MyEnum FROM scarr INTO TABLE @FINAL(itab).
```

### Forbidden Uses

The following uses are forbidden to ensure that an enumerated object always contains only a single valid enumerated value:

- Within ABAP, enumerated objects are never interpreted in accordance with their base type. This means that they cannot be used in operand positions that expect numeric, character-like, or byte-like data types. The only exception to this are the operand positions in which an implicit conversion to a character-like type takes place.

- Enumerated types are not currently supported by the [ABAP Dictionary](../../abap-dictionary-ddic/abenabap_dictionary.md). Accordingly, no database tables whose columns have an enumerated type can be defined in the ABAP Dictionary.

- In Native SQL (`EXEC SQL`, ADBC), no [host variables](../../abap-glossary/abenhost_variable_glosry.md) or references to ABAP variables with enumerated type can be used. The actual parameters of [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md) cannot be typed using enumerated types.

- No enumerated types are supported for the input fields of selection screens.

- It is not possible to inherit enumerated values from lists in the list buffer, since there are no conversion rules between character-like types and enumerated types.

If an enumerated object is provided with an invalid value due to a gap in the rules, this results in the following behavior:

- The result of a conversion to `c` or `string` is the string `<illegal enum value>`, which is displayed accordingly in the ABAP Debugger.

- An enumerated object with an invalid value can be assigned to other enumerated objects with the same enumerated type without being checked.

- The expressions [`CONV base_type( enum_dobj )`](abenconv_constructor_enum.md) and [`EXACT base_type( enum_dobj )`](abenexact_constructor_enum.md) return the invalid value.

An invalid value is to be regarded as an error and should never occur.

### Example for General Use

### Executable Example

enum, General Use
