---
title: "TYPES, BEGIN OF ENUM enum_type"
source_file: abaptypes_enum.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, BEGIN OF ENUM enum_type

## Syntax

``` abap
TYPES: BEGIN OF ENUM enum_type 
              [STRUCTURE struc] 
              [BASE TYPE dtype], 
         val1 [VALUE IS INITIAL], 
         val2 [VALUE val], 
         val3 [VALUE val], 
         ... 
       END OF ENUM enum_type 
              [STRUCTURE struc].  
```

### Addition

[1. `... STRUCTURE struc`](abaptypes_enum.md#addition-1)

[2. `... BASE TYPE dtype`](abaptypes_enum.md#addition-2)

[3. `... VALUE {IS INITIAL}|val`](abaptypes_enum.md#addition-3)

## Overview

### Description

Definition of an [enumerated type](../../abap-glossary/abenenumerated_type_glosry.md) `enum_type`. An enumerated type describes [enumerated variables](../../abap-glossary/abenenumerated_variable_glosry.md), that is, elementary data objects that can only have certain [enumerated values](../../abap-glossary/abenenumerated_value_glosry.md). These values are defined in the form of [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) `val1`, `val2`, ... in the definition of the enumerated type as its value set. Enumerated variables and enumerated constants are both [enumerated objects](../../abap-glossary/abenenumerated_object_glosry.md).

The statements for defining an enumerated type are introduced with a `TYPES BEGIN OF ENUM` statement and end with a `TYPES END OF ENUM` statement. Between these are `TYPES` statements for defining the value set of the enumerated type. At least one enumerated value must be defined. No other statements are allowed.

The definition of an enumerated type includes:

- **Name `enum_type`**.

  The enumerated type, like any data type defined with `TYPES`, can be used with its name `enum_type`, for example, after a `TYPE` addition or in suitable [constructor expressions](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md). It acts as a complete type in [typing](abentyping.md) of field symbols or actual parameters.

- **Base type**

  The [base type](../../abap-glossary/abenbase_type_glosry.md) determines the data type of the enumerated constants in the value set of the enumerated type and the technical type of enumerated variables.

  - If the `BASE TYPE` addition is not specified, the default base type is `i`.

  - The `BASE TYPE` addition can be used to explicitly define the base type; all flat elementary data types, including [CDS simple types](../../abap-glossary/abencds_simple_type_glosry.md), that are no longer than 16 bytes can be specified for `dtype`.

- Enumerated constants

  Each enumerated value `val1`, `val2`, ... is declared by a separate `TYPES` statement. However, it does not define a data type, and an enumerated constant that contains the enumerated value is defined instead. The data type of each constant is the enumerated type `enum`. The technical data type for the enumerated value is the base type. Each name `val1`, `val2`, ... must adhere strictly to the [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md).

  - If the `STRUCTURE` addition is not specified, each enumerated constant is a separate data object with the respective name `val1`, `val2`, .... The enumerated constants are declared in the namespace and validity area of the current context (procedure, class, program), and each name must be unique within the enumerated type as well as in the entire current context.

  - The `STRUCTURE` addition creates a constant structure `struc` with the components `val1`, `val2`, ... as an [enumerated structure](../../abap-glossary/abenenumerated_structure_glosry.md) in the current context. The enumerated values are stored in the components of this structure.

    The individual enumerated constants or the constant enumerated structure can be [used](../abap-processing-internal-data/abenenumerated_types_usage.md) in certain read positions. In classes they belong, like all constants, to the static attributes and can be addressed accordingly using the component selectors `=>` and `->`.

- Enumerated values

  The enumerated values, that is, the content of the enumerated constants, are determined as follows:

  - If the `VALUE` addition is not specified, the base type must be numeric and the enumerated constants `val1`, `val2`, and so on are filled with the enumerated values 0, 1, and so on, from left to right.

  - The `VALUE` addition is used to assign explicit type-compliant enumerated values to the enumerated constants. The addition must be specified either for all or for none of the enumerated constants `val1`, `val2`, .... The `IS INITIAL` addition must be specified for exactly one constant. Each enumerated value must be unique within the enumerated type. The order of the specified values is not important. For non-numeric base types, the `VALUE` addition must be specified for each enumerated constant.

Special [conversion rules](../abap-processing-internal-data/abenconversion_enumerated.md) apply to enumerated types that ensure only the enumerated values defined in the enumerated type can be assigned to an [enumerated variable](../../abap-glossary/abenenumerated_variable_glosry.md).

### Hints

- If `STRUCTURE` is not specified, an elementary type `enum` is declared, and a single data object is declared for each enumerated value of the value set. Each `TYPES` statement for defining an enumerated value `val` has a similar effect to a declaration.

  `CONSTANTS val TYPE enum_type VALUE ...`

- An enumerated type is always an elementary data type and is included in the generic type [`simple`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md). Likewise, the associated type description class `CL_ABAP_ENUMDESCR` is a subclass of `CL_ABAP_ELEMDESCR`.

- The statements for defining an enumerated type are usually summarized in a [chained statement](../../abap-glossary/abenchained_statement_glosry.md).

- In a [type pool](../../abap-glossary/abentype_pool_glosry.md), the names of the enumerated constants, in addition to the type name `enum_type`, must have the name of the type pool as a prefix.

- The definition of enumerated types is supported in the ABAP language and in [ABAP CDS](../../abap-glossary/abencds_glosry.md) but not in ABAP Dictionary.

  - The definition of enumerated types in ABAP CDS is described in the topic [ABAP CDS - Enumerated Types](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_enumeration_types.md).

  - Enumerated types defined in ABAP CDS can be used in ABAP programs in the same way as enumerated types defined in ABAP with an enumerated structure.

  - Enumerated types defined in ABAP CDS are represented in ABAP by an [enumerated structure](../../abap-glossary/abenenumerated_structure_glosry.md) with the name of the type. This structure is implicitly created as an ABAP data object in the global program context, before a CDS enumerated type is addressed for the first time in the program. After that, the CDS enumerated type can be used like an ABAP enumerated type with an enumerated structure of the same name.

- For more information about usage, see [enumerated objects](../abap-processing-internal-data/abenenumerated_types_usage.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of an enumerated type `planet` without using optional additions. The base type is `i` and the enumerated values of the enumerated constants `mercury`, `venus`, ... are 0 to 7. The enumerated variable `planet` is declared with the enumerated type `planet`. It can only be assigned the enumerated values defined in the enumerated type.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF ENUM planet, 
    mercury, 
    venus, 
    earth, 
    mars, 
    jupiter, 
    saturn, 
    uranus, 
    neptune, 
  END OF ENUM planet. 
 
DATA planet type planet. 
 
planet = earth. 
 
out->write( planet ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The enumerated type `number` comprises the same value set as the fixed values of the domain `DEMO_NUMBERS`. This is checked by the assignment of each domain fixed value to an enumerated variable `number` of the enumerated type `number`. The necessary [conversions](../abap-processing-internal-data/abenconv_constructor_enum.md) are performed.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF ENUM number, 
    n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, 
  END OF ENUM number. 
 
DATA doma_values TYPE TABLE OF dd07v. 
CALL FUNCTION 'DD_DOMVALUES_GET' 
  EXPORTING 
    domname   = 'S_NUMBERS' 
  TABLES 
    dd07v_tab = doma_values. 
 
TRY. 
    LOOP AT doma_values INTO FINAL(doma_value). 
      FINAL(number) =  CONV number( CONV i( doma_value-domvalue_l ) ). 
    ENDLOOP. 
  CATCH cx_sy_conversion_no_enum_value. 
    out->write( 
      |{ doma_value-domvalue_l } does not match| ). 
ENDTRY. 
 
out->display( ).
```

## Addition 1

`... STRUCTURE struc`

### Description

If the `STRUCTURE` addition is specified, no separate enumerated constant is created for each enumerated value `val1`, `val2`, .... Instead, a constant [enumerated structure](../../abap-glossary/abenenumerated_structure_glosry.md) `struc` is declared in the namespace and validity area of the current context (procedure, class, program). The `TYPES` statements for the enumerated values `val1`, `val2`, ... define the components of the structure in the order they appear. They have the names `val1`, `val2`, ..., and each has the enumerated type `enum`. The components of the structure are special [enumerated objects](../../abap-glossary/abenenumerated_object_glosry.md).

### Hints

- If `STRUCTURE` is specified, an elementary type `enum` and a structured data object `struc` are declared. With regard to the structure, the `TYPES` statement has the following effect:

  ` CONSTANTS: BEGIN OF struc, val1 TYPE enum_type VALUE ... val2 TYPE enum_type VALUE ... val3 TYPE enum_type VALUE ... ... END OF struc.` The structure `struc` is a data object and not a data type. It cannot be referred to by a `TYPE` addition.

- If `STRUCTURE` is specified, the enumerated values of the enumerated type can be addressed using `struc-val1`, `struc-val2`, .... Additionally, the structure can be addressed as a whole, with the rules for structures whose components have enumerated types.

- The enumerated type `enum` is an elementary type, even if `STRUCTURE` is specified.

- In a [type pool](../../abap-glossary/abentype_pool_glosry.md), the name of the enumerated structure, in addition to the type name `enum_type`, must have the name of the type pool as a prefix. This is not necessary for the components.

- In a class, the enumerated structure cannot have the same name as the enumerated type.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of an enumerated type `planet` using the optional `STRUCTURE` addition. This declares a constant enumerated structure `p` that can be addressed in the program, is declared with the components `mercury`, `venus`, ... with the base type `i` and the enumerated values 0 to 7. The enumerated variable `planet` is declared with the enumerated type `planet`. It can only be assigned the enumerated values declared in the enumerated type.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF ENUM planet STRUCTURE p, 
    mercury, 
    venus, 
    earth, 
    mars, 
    jupiter, 
    saturn, 
    uranus, 
    neptune, 
  END OF ENUM planet STRUCTURE p. 
 
DATA planet type planet. 
 
planet = p-earth. 
 
out->write( planet ). 
 
out->write( p ). 
 
out->display( ).
```

## Addition 2

`... BASE TYPE dtype`

### Description

The `BASE TYPE` addition defines an explicit base type `dtype` for the enumerated values of the value set of the enumerated type `enum`. All built-in and user-defined flat elementary data types that are no longer than 16 bytes can be specified. This includes the following [built-in ABAP types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) and all [dictionary types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types_intro.md) that are mapped to them:

- All [numeric types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md)

- The [character-like types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) `c` and `n` with a maximum length of 8, but no text strings

- the [byte-like type](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) `x` with a maximum length of 16, but no byte strings

- The [date types and time types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md)

If the `BASE TYPE` addition is not specified, the base type `i` is used.

### Hints

- The base type describes how each enumerated value of the value set is stored internally, but it is not the type of the associated enumerated constant that can be used in a program. Its type is the enumerated type `enum` itself.

- If an explicitly specified base type is not numeric, the `VALUE` addition must be used for each enumerated value of the value set.

- The explicit definition of a base type other than `i` is usually unnecessary.

- To access an enumerated value of the value set in accordance with its representation in the base type, the conversion operator `CONV` can be used.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of an enumerated type `bool` in a class `boolean` with explicit specification of the base type `abap_bool` from the type pool `ABAP`. Unlike a variable of type `abap_bool`, an enumerated variable of type `boolean=>bool` can only have the enumerated values `abap_true` and `abap_false`. However, it is also not necessary to specify the base type explicitly in this example and usage of the class shown would also work with the implicit base type `i`.

``` abap
CLASS boolean DEFINITION. 
  PUBLIC SECTION. 
    TYPES: 
      BEGIN OF ENUM bool BASE TYPE abap_boolean, 
        wrong VALUE IS INITIAL, 
        ok  VALUE abap_true, 
      END OF ENUM bool. 
ENDCLASS. 
 
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main 
      IMPORTING p           TYPE any 
      RETURNING VALUE(bool) TYPE boolean=>bool. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD main. 
    bool = COND #( WHEN p IS INITIAL THEN boolean=>wrong 
                                     ELSE boolean=>ok ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    IF demo=>main( 1 ). 
      out->write( |True| ). 
    ENDIF. 
    IF NOT demo=>main( ' ' ). 
      out->write( |False| ). 
    ENDIF. 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Addition 3

`... VALUE {IS INITIAL}|val`

### Description

The `VALUE` addition can be used to assign explicit enumerated values to the enumerated constants `val1`, `val2`, ... of the value set of the enumerated type `enum`. The `VALUE` addition must either be specified for all or for none of them. `IS INITIAL` must be specified for exactly one enumerated constant. An enumerated value `val` that matches the base type must be specified for all other enumerated constants.

- If the base type is numeric, `VALUE` can be specified.

- If the base type is not numeric, `VALUE` must be specified.

The same applies to the `VALUE` addition as to the statements [`CONSTANTS`](abapconstants.md) and [`DATA`](abapdata_options.md):

- `IS INITIAL` generates the initial value of the base type.

- `val` can either be specified as a literal or as an already defined constant.

Each enumerated value can only occur once within the value set of an enumerated type. If the `VALUE` addition is not specified, the enumerated values of the value set are set to 0, 1, 2, and so on, from left to right. If it is specified explicitly, the enumerated values do not have to be sorted by size.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following enumerated type, the planets are in alphabetical order. The explicit assignment of enumerated values, however, corresponds to their order in the solar system. Accordingly, the logical expression after `ASSERT` is true. The order of the components of the structure `p`, on the other hand, corresponds to the order of definition. The enumerated value is determined using the conversion operator [`CONV`](../abap-processing-internal-data/abenconv_constructor_enum.md), to which a special rule applies.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF ENUM planet STRUCTURE p, 
    earth   VALUE 20, 
    jupiter VALUE 40, 
    mars    VALUE 30, 
    mercury VALUE IS INITIAL, 
    neptune VALUE 70, 
    saturn  VALUE 50, 
    uranus  VALUE 60, 
    venus   VALUE 10, 
  END OF ENUM planet STRUCTURE p. 
 
ASSERT p-mercury < p-venus   AND 
       p-venus   < p-earth   AND 
       p-earth   < p-mars    AND 
       p-mars    < p-jupiter AND 
       p-jupiter < p-saturn  AND 
       p-saturn  < p-uranus  AND 
       p-uranus  < p-neptune. 
 
DO. 
  ASSIGN p-(sy-index) TO FIELD-SYMBOL(<fs>). 
  IF sy-subrc <> 0. 
    EXIT. 
  ENDIF. 
  out->write( 
    |Name:  { <fs> && `,` WIDTH = 8 } Value: { CONV i( <fs> ) }| ). 
ENDDO. 
 
out->display( ).
```
