---
title: "DDIC - Naming Rules for Data Types"
source_file: abenddic_types_names.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Naming Rules for Data Types

The name of a DDIC data type must stick to the following rules:

- It can have a maximum of 30 characters.

- It can consist of letters, digits, and underscores.

- It must start with a letter.

- It can be introduced using a [namespace prefix](../../abap-glossary/abenname_space_prefix_glosry.md) (`/.../`) of a [prefix namespace](../../abap-glossary/abenprefix_name_space_glosry.md)

- It is in the same namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

- It must not be the name of a [built-in data type](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types.md) in ABAP.

All DDIC data types, alongside [DDIC database tables](../ddic-database-tables/abenddic_database_tables.md) and DDIC views, are located in the same namespace which includes all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP. [DDIC domains](../../abap-glossary/abendomain_glosry.md), on the other hand, are in a separate namespace, and can therefore have the same name as, for example, a data element.
