---
title: "DDIC DDL - DEFINE TABLE, foreign_key_annos"
source_file: abenddicddl_define_table_fkprps.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Dictionary DDL for Defining Database Tables > DDIC DDL - DEFINE TABLE > DDIC DDL - DEFINE TABLE, field"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC DDL - DEFINE TABLE, foreign_key_annos

## Syntax

``` abap
[@AbapCatalog.foreignKey.label : '...'] 
[@AbapCatalog.foreignKey.keyType : key_type] 
[@AbapCatalog.foreignKey.screenCheck : true|false] 
[@AbapCatalog.foreignKey.messageClass : msg_cls] 
[@AbapCatalog.foreignKey.messageNumber : msg_no]  
```

## Description

Annotations used to specify properties for a [foreign key dependency](../../abap-glossary/abenforeign_key_dependency_glosry.md) of a [table field](abenddicddl_define_table_comps.md) defined using [`foreign_key`](abenddicddl_define_table_forkey.md) in the definition of a DDIC database table using the [Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md) statement [`DEFINE TABLE`](abenddicddl_define_table.md).

- In quotation marks, `@AbapCatalog.foreignKey.label` defines the short text of the foreign key in the original language of the database table.

- `@AbapCatalog.foreignKey.keyType` defines the [type of the foreign key fields](abenddic_database_tables_forkey.md). `key_type` can be specified as:

  - `#NON_KEY` - [No key fields/candidates](abenddic_database_tables_forkey.md)

  - `#KEY` - [Key fields/candidates](abenddic_database_tables_forkey.md)

  - `#TEXT_KEY` - [Key fields of a text table](abenddic_database_tables_forkey.md)

- `@AbapCatalog.foreignKey.screenCheck` enables or disables the foreign key dependency for the [input check](abenddic_database_tables_forkey.md).

- `@AbapCatalog.foreignKey.messageClass` and `@AbapCatalog.foreignKey.messageNumber` specify the message class `msg_class` and message number `msg_no` for the [message](../../abap-glossary/abenmessage_glosry.md) of the [input check](abenddic_database_tables_forkey.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

See [`foreign_key`](abenddicddl_define_table_forkey.md).
