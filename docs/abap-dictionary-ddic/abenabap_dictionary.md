---
title: "ABAP Dictionary (DDIC)"
source_file: abenabap_dictionary.html
section: "ABAP Dictionary (DDIC)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Dictionary (DDIC)

ABAP Dictionary is a persistent repository of type definitions (meta data) in the form of [dictionary objects](../abap-glossary/abendictionary_object_glosry.md). These dictionary objects are visible in and can be accessed from other [repository objects](../abap-glossary/abenrepository_object_glosry.md), particularly [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) objects and ABAP programs, as long as this is in line with the package concept. As in the [ABAP language](../abap-glossary/abenabala_glosry.md), the data types that can be defined in ABAP Dictionary can be elementary, structured, or tabular. Reference types are also possible. The main task of ABAP Dictionary structures is to describe DDIC database tables and DDIC views on the database, while at the same time being visible in all other repository objects and allowing for the definition of type-friendly interface parameters and data objects for handling DDIC database tables and DDIC views. Additionally, ABAP Dictionary manages lock objects and search helps. All ABAP Dictionary objects (definitions) are transportable repository objects.

The following ABAP Dictionary objects are available:

- [Data types](ddic-data-types/abenddic_data_types.md)

  ABAP Dictionary supports the following standalone data types:

  - [Data elements](ddic-data-types/abenddic_data_elements.md) for elementary data types and reference types.

  - [DDIC structures](ddic-data-types/abenddic_structures.md) that consist of other data types.

  - [DDIC table types](ddic-data-types/abenddic_table_types.md) which can have any other DDIC data type except for built-in data types as a line type.

    **Note:** DDIC tables types are not to be confused with DDIC database tables that describe tables on the database. The data types in the ABAP Dictionary serve as reference objects for interface parameters and data objects within AS ABAP. Other repository objects can refer directly to the data types in the ABAP Dictionary.

- [DDIC database tables](ddic-database-tables/abenddic_database_tables.md)

  A DDIC database table (not to be confused with a table type) is an object in the ABAP Dictionary that describes a database table. Regarding the data type, a DDIC database table is a non-nested structure in which further technical properties of the DDIC database table can be defined alongside the type properties. The physical database table on the database is created when a DDIC database table is activated. In an ABAP program, a DDIC database table is handled both as a DDIC structure and as a database table. This means that a DDIC database table can be used for typing structured data objects and it can also be accessed using [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md).

- [DDIC tuning objects](ddic-tuning-objects/abenddic_tuning_objects.md)

  [HANA tuning objects](../abap-glossary/abenhana_tuning_object_glosry.md) can be created for DDIC objects to define technical settings and tunings that can be transported separately.

ABAP Dictionary has the following built-in data types and functions:

- A set of [built-in ABAP Dictionary data types](ddic-built-in-data-types/abenddic_builtin_types_intro.md), which are the basis for the elementary components of all ABAP Dictionary objects. [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) is also based on these elementary data types.

- ABAP Dictionary provides a set of [built-in database functions](ddic-built-in-functions/abenddic_builtin_functions.md) that can be used in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) and/or in [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md).

For common usage in ABAP Dictionary objects, ABAP CDS, and ABAP programs, there is a set of

- [predefined types](abenddic_predef_types.md)

The DDIC types, DDIC database tables, can be used as global data types in ABAP programs. Dictionary objects must be activated before they can be used, just like ABAP programs. Once activated, new or modified definitions are available directly for all other repository objects. If an existing dictionary object is changed, the repository objects that use it continue to work with the previous active version until the modified dictionary object is activated successfully. A dictionary object can only be deleted once all objects that use it have been removed.

- [Activating ABAP Dictionary Types](abenddic_activation.md)
