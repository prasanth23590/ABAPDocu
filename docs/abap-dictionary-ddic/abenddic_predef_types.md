---
title: "DDIC - Predefined Types"
source_file: abenddic_predef_types.html
section: "ABAP Dictionary (DDIC)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Predefined Types

The following predefined DDIC data types are delivered with an AS ABAP. They can be used in ABAP Dictionary, ABAP CDS, and ABAP programs.

- [Data Elements for Built-in Dictionary Types](abenddic_predef_types.md#data-elements-for-built-in-dictionary-types)

- [Data Type for Truth Values](abenddic_predef_types.md#data-type-for-truth-values)

- [Data Types for Operand Positions and Parameter Passing](abenddic_predef_types.md#data-types-for-operand-positions-and-parameter-passing)

  - [Types for Operand Positions](abenddic_predef_types.md#types-for-operand-positions)

  - [Types for Parameter Passing](abenddic_predef_types.md#types-for-parameter-passing)

## Data Elements for Built-in Dictionary Types

The following data elements are available for [built-in DDIC types](ddic-built-in-data-types/abenddic_builtin_types.md) of the same name with fixed length.

- `INT1`

- `INT2`

- `INT4`

- `D16N`

- `D34N`

- `DATN`

- `TIMN`

- `UTCL` (for built-in type `UTCLONG`)

- `GEOM_EWKB` and `GGM1` (for built-in type `GEOM_EWKB`)

These data elements allow the built-in DDIC types to be referred by their name.

### Hints

- Note that the respective built-in types cannot be specified directly in an ABAP program. In ABAP CDS however, there is a syntax `ABAP.type` to refer to built-in DDIC types.

- There is no data element `INT8`, since the respective built-in ABAP type has the same name `int8` already.

## Data Type for Truth Values

There is no built-in ABAP type for the truth values `true` or `false`. Instead, it is common to use a character field of length 1 with the meaning that a non-initial value means `true` and an initial value means `false`. The following predefined data element can be used to define these fields:

- `ABAP_BOOLEAN` of type `CHAR` with length 1.

The [type pool](../abap-glossary/abentype_pool_glosry.md) `ABAP` contains the following constants to be used as truth values.

- `abap_true` with value *X*

- `abap_false` with initial value

### Hints

- The type pool `ABAP` also contains a type `abap_bool` of type `c` and length 1. But in new programs, the data element `ABAP_BOOLEAN` should be used instead.

- The disadvantage of using type `abap_bool` and the associated constants `abap_true` and `abap_false` of type pool `ABAP` is that the entire type pool must be loaded, even if only a few types and constants are needed.

- Type pool `ABAP` also contains a third constant `abap_undefined` with value *-*. However, this constant should not be used or in exceptional cases only.

## Data Types for Operand Positions and Parameter Passing

The following types are used for typing specific operand positions of ABAP statements or for special parameter passing.

### Types for Operand Positions

- Structures `MATCH_RESULT`, `SUBMATCH_RESULT`, `REPL_RESULT` and table types `MATCH_RESULT_TAB`, `SUBMATCH_RESULT_TAB`, `REPL_RESULT_TAB` for addition [`RESULT`](../abap-programming-language/abap-processing-internal-data/abapfind_options.md) of statements [`FIND`](../abap-programming-language/abap-processing-internal-data/abapfind.md) and [`REPLACE`](../abap-programming-language/abap-processing-internal-data/abapreplace.md).

- Table type `ABAP_SORTORDER_TAB` for dynamic specification of the sort order in statement [`SORT itab`](../abap-programming-language/abap-processing-internal-data/abapsort_itab.md).

### Types for Parameter Passing

- `abap_parmbind_tab` and `abap_excbind_tab` of type pool `ABAP` for dynamic [parameter tables](../abap-programming-language/abap-calling-and-exiting-program-units/abapcall_method_parameter_tables.md) in the [`CALL METHOD`](../abap-programming-language/abap-calling-and-exiting-program-units/abapcall_method_dynamic.md) statement.

- `abap_func_parmbind_tab` and `abap_func_excbind_tab` of type pool `ABAP` for dynamic [parameter tables](../abap-programming-language/abap-calling-and-exiting-program-units/abapcall_function_dynamic.md) in the [`CALL FUNCTION`](../abap-programming-language/abap-calling-and-exiting-program-units/abapcall_function_general.md) statement.
