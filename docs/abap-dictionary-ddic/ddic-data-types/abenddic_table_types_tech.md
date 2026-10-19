---
title: "DDIC - Technical Properties of Table Types"
source_file: abenddic_table_types_tech.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Table Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Technical Properties of Table Types

A table type describes an [internal table](../../abap-glossary/abeninternal_table_glosry.md) with the following technical properties:

- **Line type**

  The line type can be defined as follows:

  - The line type can be defined by referencing any [data type](abenddic_data_types.md), including [DDIC database tables](../ddic-database-tables/abenddic_database_tables.md) and DDIC views.

  - Elementary or reference-like line types can also be specified by using their technical properties directly. This is done in the same way as with [data elements](abenddic_data_elements.md) or [structure components](abenddic_structures_tech.md).

- **Table category**

  The table category can be specified as follows:

  - [Standard table](../../abap-glossary/abenstandard_table_glosry.md)

  - [Sorted table](../../abap-glossary/abensorted_table_glosry.md)

  - [Hashed table](../../abap-glossary/abenhashed_table_glosry.md)

  - [Index table](../../abap-glossary/abenindex_table_glosry.md) as a generic table category for standard tables and sorted tables

  - Any table as a generic table category for all table categories

    These specifications are the same as defining the table category using the statement [`TYPES`](../../abap-programming-language/abap-declarations/abaptypes_tabcat.md).

- **Table key**

  The following can be defined as a [table key](../../abap-programming-language/abap-data-types-and-data-objects/abenitab_key.md):

  - A primary key as a [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md). The primary key is either

    \- the [standard key](../../abap-glossary/abenstandard_key_glosry.md), or - the entire table line, given it is not a table type and does not contain a table type as a component, or - is determined using individual components of a structured line type in the relevant order, or - an [empty primary table key](../../abap-programming-language/abap-data-types-and-data-objects/abenitab_empty_key.md) for [standard tables](../../abap-glossary/abenstandard_table_glosry.md). A non-empty primary key of sorted tables and hashed tables can be given a unique [alias name](../../abap-glossary/abenalias_glosry.md) from the namespace of the secondary keys. The uniqueness of the primary key is unique or non-unique, depending on the table category, and cannot be specified at all for generic tables. If no primary key is specified or its uniqueness is not defined, the table type is generic regarding this property.

  - Up to 15 secondary keys as [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md). Each secondary key has a unique name, which cannot be `PRIMARY_KEY` or `LOOP_KEY`, and is either a sorted key or a hash key. Sorted keys can be either unique or non-unique and a hash key is always unique. A secondary key is defined either by the entire table line, if it is not a table type or does not contain a table type as component, or by using individual components of a structured line type in the relevant order. Using the additions [`WITH`](../../abap-programming-language/abap-declarations/abaptypes_keydef.md) or [`WITHOUT FURTHER SECONDARY KEYS`](../../abap-programming-language/abap-declarations/abaptypes_keydef.md) of the statement `TYPES`, it is possible to define explicitly whether the table type is generic with respect to the secondary keys. It is currently not possible to specify an [alias name](../../abap-glossary/abenalias_glosry.md) for a secondary key in the ABAP Dictionary.

- **Initial row count**

  This specification is a hint for the internal memory management of internal tables and corresponds to the addition [`INITIAL SIZE`](../../abap-programming-language/abap-declarations/abaptypes_itab.md) in the declaration of an internal table in an ABAP program.

## Hints

- Generic table types, that is, table types for which one or more properties are generic, can only be used in ABAP for [generic typings](../../abap-glossary/abengeneric_typing_glosry.md) of formal parameters or field symbols.

- A line type cannot be defined using a reference to a [CDS entity](../../abap-glossary/abencds_entity_glosry.md), nor using a reference to a [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md) of a corresponding [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). The latter has been possible before, but since ABAP release 7.85, access to CDS-managed DDIC views (obsolete) is [obsolete](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_access_obsolete.md).
