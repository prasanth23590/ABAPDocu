---
title: "DDIC - Special Character-Like Types"
source_file: abenddic_special_character_types.html
section: "ABAP Dictionary (DDIC) > DDIC - Built-In Data Types > DDIC - Properties of the Built-In Dictionary Types > DDIC - Special Dictionary Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Special Character-Like Types

The following character-like data types in ABAP Dictionary have a special semantic meaning:

- [`NUMC`](abenddic_builtin_types.md) for [numeric texts](../../abap-glossary/abennumeric_text_glosry.md)

  From a technical perspective, the built-in data type `NUMC` describes objects of the type `CHAR` with a maximum length of 255 characters. It is intended for numeric texts. This is not checked however when writing to or reading from database fields of this type.

- [`CLNT`](abenddic_builtin_types.md) for [client columns](../../abap-glossary/abenclient_column_glosry.md)

  From a technical perspective, the data type `CLNT` describes objects of the type `CHAR` with length 3. If the data type `CLNT` is used for the first key field of a DDIC database table, this makes the DDIC database table [client-dependent](../ddic-database-tables/abenddic_database_tables_client.md).

- [`LANG`](abenddic_builtin_types.md) for language keys

  From a technical perspective, the built-in data type `LANG` describes objects of the type `CHAR` with length 1. It is intended specifically for language keys. The [primary key](../../abap-glossary/abenprimary_key_glosry.md) of a [text table](../../abap-glossary/abentext_table_glosry.md) consists of the [foreign key](../../abap-glossary/abenforeign_key_glosry.md) and a field of type `LANG`.
