---
title: "Generic ABAP Types"
source_file: abenbuilt_in_types_generic.html
section: "ABAP Programming Language > ABAP - Built-In Types, Data Objects, Functions, and Constructors > Built-In Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Generic ABAP Types

The following table shows the built-in generic ABAP types. A generic data type is an incomplete type specification that comprises several complete type specifications. Apart from `object`, all generic types can be used after [`TYPE`](../abap-declarations/abentyping_generic.md) for the [typing](../../abap-glossary/abentyping_glosry.md) of [field symbols](../../abap-glossary/abenfield_symbol_glosry.md) and [formal parameters](../../abap-glossary/abenformal_parameter_glosry.md). When a data object is assigned to generically typed field symbols using the statement [`ASSIGN`](../abap-processing-internal-data/abapassign.md), or when a data object is used as an [actual parameter](../../abap-glossary/abenactual_parameter_glosry.md) for generically typed formal parameters in [procedure calls](../abap-calling-and-exiting-program-units/abencall_procedures.md), the system checks whether its concrete data type is [compatible](../../abap-glossary/abencompatible_glosry.md) with the object, that is, whether the data type is a subset of the generic type.

The only generic types that can be used after [`TYPE REF TO`](../abap-declarations/abaptypes_references.md) are `data`, for the generic typing of data references and `object`, for the generic typing of object references.

| **Type**                           | **Description**                                                                                                                                       |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `any`                              | Any data type                                                                                                                                         |
| `any structure [ containing ... ]` | [Fully generic structured types](../abap-declarations/abapany_structure.md) and [user-defined partially generic structured types](../abap-declarations/abapany_structure_containing.md)     |
| `any table`                        | Internal table with any table type                                                                                                                    |
| `c`                                | Text field with a generic length                                                                                                                      |
| `clike`                            | Character-like (`c`, `n`, and `string`, as well as the date/time types `d`, `t` and character-like [flat structures](../../abap-glossary/abenflat_structure_glosry.md)) |
| `csequence`                        | Text-like (`c`, `string`)                                                                                                                             |
| `data`                             | Any data type                                                                                                                                         |
| `decfloat`                         | [Decimal floating point number type](../../abap-glossary/abendecfloat_type_glosry.md) (`decfloat16`, `decfloat34`)                                                      |
| `hashed table`                     | [Hashed table](../../abap-glossary/abenhashed_table_glosry.md)                                                                                                          |
| `index table`                      | [Index table](../../abap-glossary/abenindex_table_glosry.md)                                                                                                            |
| `n`                                | [Numeric text](../../abap-glossary/abennumeric_text_glosry.md) with generic length                                                                                      |
| `numeric`                          | Numeric ((`b`, `s`), `i`, `int8`, `p`, `decfloat16`, `decfloat34`, `f`)                                                                               |
| `object`                           | Any object type (root class of the inheritance hierarchy)                                                                                             |
| `p`                                | Packed number with generic length and generic number of [decimal places](../../abap-glossary/abenfract_digit_glosry.md)                                                 |
| `simple`                           | Elementary data type including [enumerated types](../../abap-glossary/abenenum_type_glosry.md) and structured types with exclusively character-like flat components     |
| `sorted table`                     | [Sorted table](../../abap-glossary/abensorted_table_glosry.md)                                                                                                          |
| `standard table`                   | [Standard table](../../abap-glossary/abenstandard_table_glosry.md)                                                                                                      |
| `table`                            | Standard table                                                                                                                                        |
| `x`                                | Byte field with generic length                                                                                                                        |
| `xsequence`                        | Byte-like (`x`, `xstring`)                                                                                                                            |

A typing with the generic type `data` acts like a typing with the generic type `any`, with the following exception: No [numeric functions](../../abap-glossary/abenmathematical_funktion_glosry.md), [description functions](../../abap-glossary/abendescription_function_glosry.md), or [arithmetic functions](../../abap-glossary/abenarithmetic_expression_glosry.md) can be passed to a formal parameter typed with the type `data`. All other expressions, built-in functions, and functional methods are possible.

In addition to the built-in generic types shown in the table above, ABAP currently includes exactly one kind of user-defined generic type. A [table type](../../abap-glossary/abentable_type_glosry.md) defined with [`TYPES - TABLE OF`](../abap-declarations/abaptypes_itab.md) or defined in the ABAP Dictionary is generic if the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) is not specified or specified incompletely or if the [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) of the table type is generic.

## Hints

- As a rule, generic types can be used for the [typing](../../abap-glossary/abentyping_glosry.md) of [field symbols](../../abap-glossary/abenfield_symbol_glosry.md) and [formal parameters](../../abap-glossary/abenformal_parameter_glosry.md) only. They cannot be used in positions, where a complete type is required, e.g. when declaring a data object. `c`, `n`, `p`, `x` and table types with generic keys are an exception to this rule. In declarative statements, the compiler implicitly uses default length, decimal places or key specification then.

- When generic types are used for the [typing](../../abap-glossary/abentyping_glosry.md) of [field symbols](../../abap-glossary/abenfield_symbol_glosry.md) and [formal parameters](../../abap-glossary/abenformal_parameter_glosry.md), it must be ensured that the correct results are obtained regardless of the actual type used. For example, if `csequence` is used, it must be taken into account that the possible concrete types `c` and `string` behave differently with respect to trailing blanks, or that the concrete numeric types that are possible for `numeric` in calculations lead to different [calculation types](../../abap-glossary/abencalculation_type_glosry.md). Especially during generalization of existing types, it may be necessary to adapt the implementation accordingly.

- Like all generic types listed here, except `data` and `object`, the generic type `any` can only be specified directly after `TYPE`. `any` cannot be specified after [`TYPE REF TO`](../abap-declarations/abaptypes_references.md). The only generic types allowed here are `data` for fully generic data reference variables and `object` for fully generic object reference variables. Specifying `REF TO any` would define a fully generic reference variable that includes data references and object references, which is currently not possible.

- The generic type `object` can only be specified after `REF TO` and not directly after `TYPE`.

- The object type `object` plays a special role, since it is not actually a real generic type but the empty abstract root class of all object classes of ABAP Objects. An object reference variable typed using `REF TO object` can point to any object because of the general property of reference variables where reference variables with the static type of a superclass can point to objects in all related subclasses. When compared with a data reference variable typed using the real generic data type `data`, which can point to any data object, it is also possible to classify `object` as a generic type.

- In the case of the generic type `p`, note that when passing functional methods or arithmetic expressions to this type of typed input parameters, the length is always set to 16. With generic types `numeric`, `simple` and `data` or `any`, this is only the case for arithmetic expressions.

- The elementary data type `utclong` is only included in the generic types `simple`, `data`, and `any`.

- Regardless of their [base type](../../abap-glossary/abenbase_type_glosry.md), [enumerated types](../../abap-glossary/abenenumerated_type_glosry.md) are only enclosed by the generic types `any`, `data` and `simple`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of the built-in generic type `numeric` to type the input parameters of a method. Parameters with any numeric data types can be passed to the method (but no other data types).

``` abap
METHODS numeric_operation IMPORTING num1          TYPE numeric 
                                    num2          TYPE numeric 
                          RETURNING VALUE(result) TYPE decfloat34.
```
