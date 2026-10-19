---
title: "DDIC - Character-Like Types and Byte-Like Types"
source_file: abenddic_character_byte_types.html
section: "ABAP Dictionary (DDIC) > DDIC - Built-In Data Types > DDIC - Properties of the Built-In Dictionary Types > DDIC - General Dictionary Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Character-Like Types and Byte-Like Types

- [Character Strings](abenddic_character_byte_types.md#character-strings)

- [Byte Chains](abenddic_character_byte_types.md#byte-chains)

- [Notes on Strings](abenddic_character_byte_types.md#notes-on-strings)

- [Use in ABAP CDS](abenddic_character_byte_types.md#use-in-abap-cds)

- [Use in ABAP SQL](abenddic_character_byte_types.md#use-in-abap-sql)

## Character Strings

The following built-in dictionary data types are available for general character strings:

- [`CHAR`](abenddic_builtin_types.md) for text fields

  The built-in type `CHAR`, mapped to the ABAP type `c`, is used to describe general text fields with a maximum length of 30000 characters. For table fields, view fields, and fields of CDS entities, the maximum length is 1333 characters.

- [`LCHR`](abenddic_builtin_types.md) for long text fields

  The built-in type `LCHR`, also mapped to the ABAP type `c`, is used to describe general text fields with lengths between 256 and 32000 characters. In DDIC database tables, the maximum length must be specified as the value of a preceding `INT2` or `INT4` field. There can only be one table field of type `LCHR` or `LRAW`. It must not be a key field and it must be the last table field. It cannot be used in all positions of ABAP SQL statements.

- [`SSTRING`](abenddic_builtin_types.md) for short text strings

  The built-in type `SSTRING` is mapped to the ABAP type `string`. It is handled like the type `CHAR` or `VARCHAR` in ABAP Dictionary and by DDIC database tables. The length is restricted to a maximum of 1333. Table fields of this type can be used as [key fields](../ddic-database-tables/abenddic_database_tables_key.md) by DDIC database tables and used by ABAP SQL statements in almost all positions where text fields are possible.

- [`STRING`](abenddic_builtin_types.md) for text strings

  The built-in dictionary type `STRING` is mapped to the ABAP type `string`. It is handled like a text string ([CLOB](../../abap-glossary/abenclob_glosry.md)) in ABAP Dictionary and by DDIC database tables. Table fields of this type cannot be used as [key fields](../ddic-database-tables/abenddic_database_tables_key.md) or [index fields](../ddic-database-tables/abenddic_database_tables_index.md) in DDIC database tables. They cannot be used in all positions in ABAP SQL statements. The possible length of a text string is unrestricted, but a maximum length of at least 256 can be specified to restrict its length when used for a table field of a DDIC database table, which is relevant for ABAP SQL access (see below).

### Hints

- In general [DDIC structures](../ddic-data-types/abenddic_structures.md), the length of a component of type `CHAR` is not restricted to 1333.

- In DDIC database tables, there can be only one table field of the type `LCHR` and it must be the last table field. This means that the type `LRAW` cannot be used simultaneously in the same database table. If the statement [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) is used to read an `LCHR` field, the preceding length field must also be read. In [writes](../../abap-programming-language/abap-database-access/abenabap_sql_writing.md) using ABAP SQL, the length field must be given the correct value or data may be lost.

- `LCHR` is no longer recommended for new developments. The type `STRING` is recommended instead, however it is also not suitable for [key fields](../ddic-database-tables/abenddic_database_tables_key.md) of DDIC database tables or for unrestricted use in ABAP SQL. Where possible, `SSTRING` can be used here instead.

- Switching existing dictionary objects from `LCHR` to `STRING` or `SSTRING` can be critical, since all ABAP types and ABAP objects that reference dictionary objects like this are then given a [deep](../../abap-glossary/abendeep_glosry.md) data type. A switch from a [flat](../../abap-glossary/abenflat_glosry.md) data type to a [deep](../../abap-glossary/abendeep_glosry.md) data type usually constitutes an incompatible change and can produce syntax errors in ABAP programs.

## Byte Chains

The following built-in data types in ABAP Dictionary are available for general byte chains:

- [`RAW`](abenddic_builtin_types.md) for byte fields

  The built-in type `RAW`, mapped to the ABAP type `x`, is used to describe byte fields with a maximum length of 32000 characters. For table fields, the maximum length is 255 characters.

- [`LRAW`](abenddic_builtin_types.md) for long byte fields

  The built-in type `LRAW`, also mapped to the ABAP type `x`, is used to describe byte fields with lengths between 256 and 32000 characters. In DDIC database tables, the maximum length must be specified as the value of a preceding `INT2` or `INT4` field. There can only be one table field of type `LRAW` or `LCHR`. It must not be a key field and it must be the last table field. It cannot be used in all positions of ABAP SQL statements.

- [`RAWSTRING`](abenddic_builtin_types.md) for byte strings

  The built-in type `RAWSTRING` is mapped to the ABAP type `xstring` and it is handled like a byte string ([BLOB](../../abap-glossary/abenblob_glosry.md)) in ABAP Dictionary and by DDIC database tables. Table fields of this type cannot be used as [key fields](../ddic-database-tables/abenddic_database_tables_key.md) or [index fields](../ddic-database-tables/abenddic_database_tables_index.md) in DDIC database tables. They cannot be used in all positions in ABAP SQL statements. The possible length of a byte string is unrestricted, but a maximum length of at least 256 can be specified to restrict its length when used for a table field of a DDIC database table. This is relevant for ABAP SQL access (see below).

### Hints

- In general [DDIC structures](../ddic-data-types/abenddic_structures.md), the length of a component of type `RAW` is not restricted to 255.

- In DDIC database tables, there can be only one table field of the type `LRAW` and it must be the last table field. This means that the type `LCHR` cannot be used simultaneously in the same database table. If the statement [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) is used to read an `LRAW` field, the preceding length field must also be read. In [writes](../../abap-programming-language/abap-database-access/abenabap_sql_writing.md) using ABAP SQL, the length field must be given the correct value or data may be lost.

- `LRAW` is no longer recommended for new developments. The type `RAWSTRING` is recommended instead. However, `RAWSTRING` is also not suitable for [key fields](../ddic-database-tables/abenddic_database_tables_key.md) of DDIC database tables or for unrestricted use in ABAP SQL.

- Switching existing dictionary objects from `LRAW` to `RAWSTRING` can be critical, since all ABAP types and ABAP objects that reference dictionary objects like this are then given a [deep](../../abap-glossary/abendeep_glosry.md) data type. A switch from a [flat](../../abap-glossary/abenflat_glosry.md) data type to a [deep](../../abap-glossary/abendeep_glosry.md) data type usually constitutes an incompatible change and can produce syntax errors in ABAP programs.

## Notes on Strings

The following points must be remembered when using built-in dictionary data types for text strings or byte strings:

- The types `STRING` and `RAWSTRING` for [LOBs](../../abap-glossary/abenlob_glosry.md) have a variable length. A maximum length can be specified, but there is no upper limit. If a maximum length is specified, this represents the actual restriction if used for a table field of a DDIC database table.

- The type `SSTRING` also has a variable length, but this is restricted upwards by the maximum length that can be specified. The greatest maximum length is 1333. The benefit of using `SSTRING`, and not `CHAR`, is that it is assigned to the ABAP type `string`. Its advantage over `STRING` is that it can also be used for key fields in databases and in any places in ABAP SQL in which the type `CHAR` is also possible.

- The maximum possible length for the types `STRING` and `RAWSTRING` and the mandatory maximum length for `SSTRING` must not be exceeded in [writes](../../abap-programming-language/abap-database-access/abenabap_sql_writing.md) performed on database fields of these types using ABAP SQL. If it is exceeded, an exception of the class `CX_SY_OPEN_SQL_DB` is raised. If a string is truncated when read to a target field, no exception is raised.

- In ABAP programs, maximum lengths defined in ABAP Dictionary for the types `STRING`, `RAWSTRING`, and `SSTRING` are ignored by the assigned ABAP types `string` and `xstring`. As a result, writing a string that is too long to a database can raise an exception. If required, the ABAP program itself must handle the length restrictions on strings.

- The maximum length of data types based on `STRING`, `RAWSTRING`, and `SSTRING` can be identified in an ABAP program using the built-in function [`dbmaxlen`](../../abap-programming-language/abap-processing-internal-data/abenlength_functions.md).

- Trailing blanks are saved in table fields of the type `STRING` but not in table fields of the type `SSTRING`. This is particularly significant when short strings are used as key fields of database fields, since trailing blanks cannot be used as distinguishing characteristics here.

- [LOBs](../../abap-glossary/abenlob_glosry.md) of the types `STRING` and `RAWSTRING` are usually handled as [deep](../../abap-glossary/abendeep_glosry.md) data objects in which only one LOB locator is saved within the data record. This locator references the actual string data. Database fields of the type `SSTRING` are usually saved as [flat](../../abap-glossary/abenflat_glosry.md) fields. An empty long string can also be saved using the [null value](../../abap-glossary/abennull_value_glosry.md). The actual handling, however, depends on the individual database system and is not important for ABAP programs.

- If a [work area](../../abap-programming-language/abap-database-access/abenabap_sql_wa.md) or an internal table is used to access table fields of the types `SSTRING`, `STRING`, or `RAWSTRING` in ABAP SQL, the work area or the line type of the internal table must be compatible with the database structure.

- If DDIC structures, DDIC database tables, or DDIC views that have strings as components are used for typings in ABAP, it must be remembered that these objects are [deep structures](../../abap-glossary/abendeep_structure_glosry.md). This means, for example, that they cannot be used in the `TABLES` statement (obsolete for database accesses) or for typing the obsolete [table parameters](../../abap-glossary/abentable_parameter_glosry.md) of procedures.

- Access may be slower for long strings (LOBs) in DDIC database tables than for other data types. If not all data is needed at once, and to bypass any memory limits on the AS instance, [streaming](../../abap-programming-language/abap-database-access/abenabap_sql_streaming.md) and [locators](../../abap-programming-language/abap-database-access/abenlocators.md) can be used to access long strings.

## Use in ABAP CDS

The following restrictions apply in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) with respect to character-like types and byte-like types:

- The data types `STRING` and `RAWSTRING` plus `LCHR` and `LRAW` cannot be used in the following cases:

  - In the `SELECT` list if the addition `DISTINCT` is specified ([CDS view entity](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_select_statement_v2.md), [CDS DDIC-based view (obsolete)](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_select_statement_v1.md))

  - In `CAST` expressions ([CDS view entity](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_cast_expression_v2.md), [CDS DDIC-based view (obsolete)](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_cast_expression_v1.md))

  - In comparison expressions `cds_cond` ([CDS view entity](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_conditional_expression_v2.md), [CDS DDIC-based view (obsolete)](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_conditional_expression_v1.md))

  - In string functions ([CDS view entity](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_sql_functions_character_v2.md), [CDS DDIC-based view (obsolete)](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_sql_functions_character_v1.md))

  - In `CASE` expressions ([CDS view entity](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_case_expression_v2.md), [CDS DDIC-based view (obsolete)](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_case_expression_v1.md))

  - In aggregate expressions ([CDS view entity](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_aggregate_functions_v2.md), [CDS DDIC-based view (obsolete)](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_aggregate_functions_v1.md))

  - For columns merged using `UNION`:

    In [CDS DDIC-based views (obsolete)](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_union_v1.md), these data types are generally not supported. In [CDS view entities](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_union_v2.md), these data types are not supported if `UNION` is specified without the addition ` ALL`. `UNION ALL`, by contrast, supports all data types without any restriction.

  - After `GROUP BY` ([CDS view entity](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_group_by_v2.md), [CDS DDIC-based view (obsolete)](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_group_by_v1.md))

  - After `SIBLINGS ORDER BY` in the statement [`DEFINE HIERARCHY`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_define_hierarchy.md)

- The data types `LCHR` and `LRAW` cannot be used in the following case:

  - For [typings](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_typing.md)

- The data type `RAW` can only be used in a small number of operand positions, where this is documented.

### Hint

The obsolete data type `VARC` cannot be used in ABAP CDS.

## Use in ABAP SQL

The following restrictions apply when accessing database fields with character-like and byte-like types in ABAP SQL:

- There are no access restrictions to database fields with the data types `CHAR` and `RAW` in ABAP SQL.

- Database fields with the data types `STRING` and `RAWSTRING` plus `LCHR` and `LRAW` cannot be used in the following operand positions:

  - As arguments of [aggregate functions](../../abap-programming-language/abap-database-access/abapselect_aggregate.md) and [SQL expressions](../../abap-programming-language/abap-database-access/abapsql_expr.md).

  - In the [`SELECT` list](../../abap-programming-language/abap-database-access/abapselect_list.md) when the addition [`DISTINCT`](../../abap-programming-language/abap-database-access/abapselect_clause.md) is used.

  - In the [`SELECT` list](../../abap-programming-language/abap-database-access/abapselect_list.md) when the addition [`FOR ALL ENTRIES`](../../abap-programming-language/abap-database-access/abenwhere_all_entries.md) is used.

  - In [SQL conditions](../../abap-programming-language/abap-database-access/abenasql_cond.md) except [`IS [NOT] NULL`](../../abap-programming-language/abap-database-access/abenwhere_logexp_null.md).

  - In the [`GROUP BY` clause](../../abap-programming-language/abap-database-access/abapgroupby_clause.md).

  - In the [`ORDER BY` clause](../../abap-programming-language/abap-database-access/abaporderby_clause.md).

  - After [`SIBLINGS ORDER BY`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_generator.md) in the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md).

- The data type `SSTRING` can be used without restrictions, except in the [`coalesce`](../../abap-programming-language/abap-database-access/abensql_coalesce.md) function and in [`CASE`](../../abap-programming-language/abap-database-access/abensql_case.md) expressions.
