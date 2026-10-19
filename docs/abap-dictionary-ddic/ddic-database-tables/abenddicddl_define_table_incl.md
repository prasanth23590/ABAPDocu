---
title: "DDIC DDL - DEFINE TABLE, include"
source_file: abenddicddl_define_table_incl.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Dictionary DDL for Defining Database Tables > DDIC DDL - DEFINE TABLE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC DDL - DEFINE TABLE, include

## Syntax

``` abap
[KEY] [group :] INCLUDE struct [WITH SUFFIX suffix] [NOT NULL] 
                  [... 
                   extend 
                   ...];  
```

[`extend`](../ddic-data-types/abenddicddl_define_struct_comp_ext.md)

## Description

Includes an [include structure](../ddic-data-types/abenddic_include_structure.md) in the definition of a DDIC database table with the statement [`DEFINE TABLE`](abenddicddl_define_table.md) in [Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md). The same applies as to [including](../ddic-data-types/abenddicddl_define_struct_incl.md) include structures into structures with the statement [`DEFINE STRUCTURE`](../ddic-data-types/abenddicddl_define_structure.md), except that the include structures must be suitable for DDIC database tables.

Additionally, the additions `KEY` and `NOT NULL` can be used:

- By using `KEY` all fields of the included structure are flagged as [key fields](abenddic_database_tables_key.md). The include structure must then be inserted between the existing key fields or directly after them. The key attribute of the individual fields of an included structure does not have an effect. Either all fields are included as key fields or none.

- By using `NOT NULL` the [flag for initial values](abenddic_database_tables_init.md) is set for the included structure. When used, those fields in the include structure for which this attribute is set also keep their attribute, but it is not switched on for fields where the attribute is not set. If the flag for initial values is not set for the included include structure, this attribute is removed for all fields.
