---
title: "Data Types"
source_file: abendata_types.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Data Types

Data types are a subtree of the [ABAP type hierarchy](abentype_hierarchy.md). Data types are type-only descriptions. No memory for storing working data is attached, but they may require space for administrative information. A data type characterizes the technical properties of all [data objects](../../abap-glossary/abendata_object_glosry.md) that have this type. In ABAP, data types occur as properties of data objects, but they can also be defined independently.

The definition of [standalone data types](../../abap-glossary/abenstand-alone_data_type_glosry.md) is based on a set of [built-in data types](../../abap-glossary/abenbuiltin_data_type_glosry.md). The definition can be made within a program using the statement [`TYPES`](../abap-declarations/abaptypes.md) in the global declaration part of a program, in the declaration part of a class or an interface, locally in procedures, or in the [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md).

Built-in and user-defined data types can be used to create data objects and for [typing](../../abap-glossary/abentyping_glosry.md). Particularly in the latter case, [built-in generic data types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) are available. A [generic data type](../../abap-glossary/abengeneric_data_type_glosry.md) is a data type that does not determine all properties of a [data object](../../abap-glossary/abendata_object_glosry.md). Generic data types can only be used for typing [formal parameters](../../abap-glossary/abenformal_parameter_glosry.md) and [field symbols](../../abap-glossary/abenfield_symbol_glosry.md).

Data types can be divided into elementary, reference, and complex data types.

- [Elementary types](../../abap-glossary/abenelementary_data_type_glosry.md) are 'atomic' in the sense that they are not composed of other types. They are further divided into elementary types of fixed and variable length.

  - There are 14 [built-in elementary data types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) of fixed length in ABAP.

    Eight [numeric](../../abap-glossary/abennumeric_data_type_glosry.md) types: Integers (`b`, `s`, `i`, `int8`), decimal floating point numbers (`decfloat16`, `decfloat34`), binary floating point numbers (`f`), and packed numbers (`p`). Two [character-like](../../abap-glossary/abencharlike_data_type_glosry.md) types: text fields (`c`) and numeric text fields (`n`). One [byte-like](../../abap-glossary/abenbyte_like_data_typ_glosry.md) type: byte fields (`x`). Two character-like [date](../../abap-glossary/abendate_type_glosry.md) and [time types](../../abap-glossary/abentime_type_glosry.md): date fields (`d`) and time fields (`t`). A [time stamp type](../../abap-glossary/abentimestamp_type_glosry.md): Time stamp fields (`utclong`). The data types `c`, `n`, `x`, and `p` are generic in terms of their length. `p` is also generic in terms of the number of decimal places. The numeric data types `b` and `s` cannot be specified directly in programs for short integers.

  - There are two [built-in elementary data types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) of variable length in ABAP. A [character-like](../../abap-glossary/abencharlike_data_type_glosry.md) type, namely text string (`string`), and a [byte-like](../../abap-glossary/abenbyte_like_data_typ_glosry.md) type, namely byte string (`xstring`).

  - An [enumerated type](../../abap-glossary/abenenum_type_glosry.md) describes a value set in addition to the elementary data type. An [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) can have only [enumerated values](../../abap-glossary/abenenumerated_value_glosry.md) from this set.

- [Reference types](../../abap-glossary/abenreference_type_glosry.md) describe data objects that contain references to other objects (data objects and instances of classes), which are known as [reference variables](../../abap-glossary/abenreference_variable_glosry.md). There are no built-in reference types in ABAP. A reference type must either be defined in the ABAP program or in ABAP Dictionary. Reference types form a hierarchy that represents the hierarchy of the objects to which the references can point.

- [Complex data types](../../abap-glossary/abencomplex_data_type_glosry.md) are composed of other types. They allow the administration and processing of semantically related datasets under one name. A data object of a complex type can be accessed overall or by component. Apart from the structure [`sy`](../abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md), there are no built-in complex data types in ABAP. A complex type must either be defined in the ABAP program or in ABAP Dictionary. There are two kinds of complex data types:

  - A [structured type](../../abap-glossary/abenstructured_type_glosry.md) is a sequence of any elementary, reference, or complex data types. Structures are used to summarize work areas that logically belong together.

  - [Table types](../../abap-glossary/abentable_type_glosry.md) consist of a sequence of any number of lines of the same data type. Table types are characterized by a [line type](../../abap-glossary/abenrow_type_glosry.md) that can be any elementary type, reference type, or complex data type, by the [table category](../../abap-glossary/abentable_category_glosry.md), which defines how tables can be accessed, and by a [table key](../../abap-glossary/abentable_key_glosry.md) that is used to identify the table lines.

  - A [mesh type](../../abap-glossary/abenmesh_type_glosry.md) is a special structured type with tabular components between which there are [mesh associations](../../abap-glossary/abenmesh_association_glosry.md).
