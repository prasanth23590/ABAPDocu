---
title: "DDIC - Use of the Built-In Dictionary Types"
source_file: abenddic_builtin_type_usage.html
section: "ABAP Dictionary (DDIC) > DDIC - Built-In Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Use of the Built-In Dictionary Types

The [built-in types](abenddic_builtin_types.md) in ABAP Dictionary are used for the definition of the elementary parts of all data types, including reference types in ABAP Dictionary, and for specifying some types in ABAP SQL and ABAP CDS. The built-in types in ABAP Dictionary can be specified in the places specified below. No other places are possible.

- [Data elements](../ddic-data-types/abenddic_data_elements.md)

  A data element for an elementary data type has either a directly specified built-in type or a type specified using a [domain](../ddic-data-types/abenddic_domains.md). If a data element is used for typing in an ABAP program, the data element's dictionary type is mapped to a [built-in ABAP type](abenddic_builtin_types.md) in accordance with the last column of the [tables of built-in types](abenddic_builtin_types.md).

- [DDIC structures](../ddic-data-types/abenddic_structures.md), [DDIC database tables](../ddic-database-tables/abenddic_database_tables.md),

  The elementary components of a DDIC structure have either a directly specified built-in type or a type specified using a [data element](../ddic-data-types/abenddic_data_elements.md). In references to structures in an ABAP program, the structures are mapped to a [structured type](../../abap-glossary/abenstructured_type_glosry.md), where the elementary components are mapped to [built-in ABAP types](../../abap-glossary/abenbuiltin_abap_type_glosry.md) in accordance with the last column of the [tables of built-in types](abenddic_builtin_types.md). The same applies to the table fields of DDIC database tables.

- [DDIC table types](../ddic-data-types/abenddic_table_types.md)

  The line types of a table type are defined using existing data types from ABAP Dictionary, whose elementary components have a built-in type as explained above. When a reference is made to a table type in an ABAP program, the type is mapped to a matching ABAP type. Here, the elementary components are mapped to [built-in ABAP types](../../abap-glossary/abenbuiltin_abap_type_glosry.md) in accordance with the [tables of built-in types](abenddic_builtin_types.md).

- Reference types

  Data elements, components of structures, or line types of table types can all be reference types. Reference types for data reference variables with an elementary static data type are defined by specifying a built-in type directly or by using a data element.

- Types specified in SQL

  - [Typing](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_typing.md) of elements and input parameters of [CDS entities](../../abap-glossary/abencds_entity_glosry.md) in ABAP CDS.

  - Cast expression [`cast`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_cast_expression_v2.md) in the CDS DDL in ABAP CDS.

  - [Typed literals](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_typed_literal_v2.md) in ABAP CDS.

  - SQL expression [`CAST`](../../abap-programming-language/abap-database-access/abensql_cast.md) in ABAP SQL.

  - [Typed literals](../../abap-programming-language/abap-database-access/abenabap_sql_typed_literals.md) in ABAP SQL.

The data type of all elementary components in a [CDS entity](../../abap-glossary/abencds_entity_glosry.md), such as view fields, literals, parameters, and other operands is based indirectly on the built-in data types in ABAP Dictionary.

In ABAP programs, `TYPE` references to the built-in data types in ABAP Dictionary are possible only by using the DDIC data types above. No other `TYPE` reference to a built-in DDIC type is supported from an ABAP program. Alongside their role in defining data types, these built-in types in ABAP Dictionary must also be considered in [ABAP SQL statements](../../abap-glossary/abenabap_sql_glosry.md):

- ABAP SQL statements work with DDIC database tables whose columns have DDIC data types to which the actual platform-dependent types of the databases are mapped.

## Hints

- In ABAP CDS, a built-in dictionary type `type` is specified by `ABAP.type`, which is in fact a bit misleading.

- In ABAP development, only mappings from the built-in dictionary types to the built-in ABAP types are relevant. In database accesses using ABAP SQL, the actual database type, such as `NVARCHAR`, is hidden by the dictionary type (in this case `CHAR`).

- When referring to built-in dictionary types in ABAP programs, the [initial value](../../abap-glossary/abeninitial_value_glosry.md) of elementary data types is not the initial value assigned to the [built-in dictionary types](abenddic_builtin_types.md) but the initial value of the mapped [built-in ABAP types](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md).

- For some built-in dictionary types, there are [predefined data elements](../abenddic_predef_types.md) of the same name for common usage.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following type reference in an ABAP program does not use the built-in type `INT2` directly. Instead, it used the identically named data element `INT2` whose type is itself defined using the identically named domain `INT2`. The domain finally uses the built-in type `INT2`:

``` abap
DATA num TYPE int2.
```
