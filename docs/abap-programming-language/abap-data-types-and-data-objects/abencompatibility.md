---
title: "Technical Type Properties of Compatible Data Types"
source_file: abencompatibility.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Technical Type Properties of Compatible Data Types

The [compatibility](../../abap-glossary/abencompatible_glosry.md) of two data types apart from reference types is based on the [technical type properties](../../abap-glossary/abentechnical_type_prpt_glosry.md) of the data types. The technical type properties affect the following:

- Whether data objects can be assigned directly or a [type conversion](../../abap-glossary/abentype_conversion_glosry.md) has to take place.

- The [checking of the typing](../abap-declarations/abentyping_check.md) in assignments to [field symbols](../../abap-glossary/abenfield_symbol_glosry.md) or when assigning [actual parameters](../../abap-glossary/abenactual_parameter_glosry.md) to [formal parameters](../../abap-glossary/abenformal_parameter_glosry.md).

In addition, the compatibility of [value assignments](../abap-processing-internal-data/abenvalue_assignments.md) and [comparisons](../abap-program-flow-logic/abenlogexp_comp.md) between data objects apart from reference variables usually determines whether a [conversion](../abap-processing-internal-data/abenconversion_rules.md) has to be performed or not.

In the case of reference types with data objects (reference variables) that have a [dynamic type](../../abap-glossary/abendynamic_type_glosry.md) apart from the [static type](../../abap-glossary/abenstatic_type_glosry.md), the term compatibility that is based entirely on technical type properties is not sufficient.

- [Non-Generic Data Types Except Reference Types](abencompatibility.md#non-generic-data-types-except-reference-types)

- [Generic Data Types](abencompatibility.md#generic-data-types)

- [Reference Types](abencompatibility.md#reference-types)

## Hint

In order to check whether two data types are compatible at runtime, the method `APPLIES_TO_DATA` of RTTI class `CL_ABAP_DATADESCR` can be used. This can be helpful to prevent uncatchable exceptions when assigning generically typed data objects that are neither compatible nor convertible. For an example, see [Assignment and Conversion Rules](../abap-processing-internal-data/abenconversion_rules.md).

## Non-Generic Data Types Except Reference Types

Two non-generic data types apart from [reference types](../../abap-glossary/abenreference_type_glosry.md) and those that contain reference types as components are compatible if all their technical type properties match.

- In the case of **[elementary data types](../../abap-glossary/abenelementary_data_type_glosry.md)**, the technical type properties are as follows:

  - The [built-in ABAP type](../../abap-glossary/abenbuiltin_abap_type_glosry.md)

  - The length (for types `c`, `n`, `p`, and `x`)

  - The number of [decimal places](../../abap-glossary/abendecimal_place_glosry.md) (for type `p`)

    With compatible elementary data types, all these properties match.

- In the case of **[structured types](../../abap-glossary/abenstructured_type_glosry.md)**, the technical type property is as follows:

  - The structure of components

    The structure of structured types not only refers to the sequence of elementary components in the memory, but also to the combination of components with substructures and whether a substructure is a [boxed component](../../abap-glossary/abenboxed_component_glosry.md). The names of the components and of the semantic properties defined in the ABAP Dictionary however, are not important. With compatible structures, all components are compatible in pairs. This applies recursively down to the level of elementary data types. If two structures are constructed identically, but different substructures are declared as boxed components, the structures are not compatible.

- In the case of **[table types](../../abap-glossary/abentable_type_glosry.md)**, the technical type properties are as follows:

  - The [line type](../../abap-glossary/abenrow_type_glosry.md)

  - The [table category](../../abap-glossary/abentable_category_glosry.md)

  - The [table key](../../abap-glossary/abentable_key_glosry.md) including alias names

    With compatible internal tables, the line types are compatible and table category and table key match. Other properties, such as the [initial memory requirement](../../abap-glossary/abeninitial_mem_req_glosry.md), are not important. Note that table types with secondary table key specifications are only compatible if they match in detail, meaning:

  - Secondary table key names must be identical.

  - Alias names, if present, must be identical.

  - Key types (sorted or hashed) must be identical.

  - Key uniqueness (unique or non-unique) must be identical.

- In the case of **[mesh types](../../abap-glossary/abenmesh_type_glosry.md)**, the technical type properties are as follows:

  - The structure of nodes including the node names

  - The mesh associations of each component defined by `ON` conditions, including their names and the table key used

- In the case of **[enumerated types](../../abap-glossary/abenenum_type_glosry.md)**, the technical type properties are as follows:

  - All properties of the enumerated type

    Each enumerated type is unique and only compatible with itself.

### Hints

- The types listed here are not compatible with one another, for example, an elementary data type is never compatible with a structure, even if it has only one component.

- The statement [`TYPES`](../abap-declarations/abaptypes_enum.md) cannot be used to define different enumerated types with the same technical type properties. Even data types that are constructed with [RTTC](../../abap-glossary/abenrun_time_type_creation_glosry.md) methods exactly like an existing enumerated type are not compatible with it. An enumerated type defined by direct or indirect reference (including [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md)) to an existing enumerated type, on the other hand, is compatible.

## Generic Data Types

A non-generic data type apart from a reference type is compatible with a [generic data type](../../abap-glossary/abengeneric_data_type_glosry.md) if its technical properties are included in the generic data type.

## Reference Types

A reference type is the static type of reference variables that determines to which objects they can point. At runtime, reference variables also have a dynamic type determined by the type of the object to which a reference variable points. The dynamic type can be more specific than the static type. For this reason, the rules for typing checks, assignments and comparisons cannot be covered by the idea of a compatibility that is based entirely on the technical properties of the static type. Instead, the following three points show how reference types can be used together:

- When checking typing

  - A reference variable can be passed to a formal parameter typed as a reference variable if the type of the formal parameter is more general or equal to the type of the reference variable (known as an [upcast](../../abap-glossary/abenup_cast_glosry.md)) and the formal parameter cannot be changed within the procedure.

  - A reference variable can be assigned to a field symbol typed as a reference variable if the reference types are identical.

- Assignments between reference variables are possible using an [upcast](../../abap-glossary/abenup_cast_glosry.md) or a [downcast](../../abap-glossary/abendown_cast_glosry.md).

- Data reference variables can be compared with all data reference variables and object reference variables can be compared to all object reference variables.

As a rule, data reference variables can only be used with data reference variables and object reference variables only with object reference variables. No conversions take place between [reference variables](../../abap-glossary/abenreference_variable_glosry.md). Reference variables are either passed without conversion, assigned to each other, compared to each other, or not at all.

### Hints

- These rules for the usability of reference variables in assignments introduced here are one-way. The type of a target reference variable, to which a source reference variable can be assigned, does not itself have to be assignable to the source reference variable. The usability of reference variables in comparisons on the other hand, is not directed.

- If a reference variable is a component of a structure, the usability of the structure is determined accordingly. In particular, the usability of such a structure regarding assignments is also directed.
