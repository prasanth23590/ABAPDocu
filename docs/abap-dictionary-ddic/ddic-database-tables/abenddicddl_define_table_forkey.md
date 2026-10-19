---
title: "DDIC DDL - DEFINE TABLE, foreign_key"
source_file: abenddicddl_define_table_forkey.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Dictionary DDL for Defining Database Tables > DDIC DDL - DEFINE TABLE > DDIC DDL - DEFINE TABLE, field"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC DDL - DEFINE TABLE, foreign_key

## Syntax

``` abap
...  WITH FOREIGN KEY [[n,m]] check_table 
       WHERE check_field1 = dbtab.field1 
         [AND check_field2 = dbtab.field2 ...] ...  
```

## Description

Assigns a [check table](abenddic_database_tables_checktab.md) to a [table field](abenddicddl_define_table_comps.md) whose data type is defined by a data element in the definition of a DDIC database table using the [Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md) statement [`DEFINE TABLE`](abenddicddl_define_table.md). `check_table` must be an existing DDIC database table. This statement turns `check_table` into a check table and turns the current DDIC database table into a [foreign key table](../../abap-glossary/abenforeign_key_table_glosry.md). The current table field is turned into a [foreign key field](../../abap-glossary/abenforeign_key_field_glosry.md) of the [foreign key](abenddic_database_tables_forkey.md) of the current table.

- Fields of the check table must be assigned to the foreign key fields of the foreign key table after `WHERE`.

- `[n,m]` can be used to define the [cardinality](../../abap-glossary/abencardinality_glosry.md) of the [foreign key](abenddic_database_tables_forkey.md).

  - The possible values for `n` are `1` for [1](abenddic_database_tables_forkey.md) and `[0..1]` for [C](abenddic_database_tables_forkey.md).

  - The possible values for `m` are `1` for [1](abenddic_database_tables_forkey.md), `[0..1]` for [C](abenddic_database_tables_forkey.md), `[1..*]` for [N](abenddic_database_tables_forkey.md), and `[0..*]` for [CN](abenddic_database_tables_forkey.md).

Further properties of the foreign key can be specified using [`foreign_key_annos`](abenddicddl_define_table_fkprps.md).

## Hint

The addition `WITH FOREIGN KEY` can be used, with the same meaning, in the definition of a structure using [`DEFINE STRUCTURE`](../ddic-data-types/abenddicddl_define_structure.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Dictionary DDL for specifying the check table `SCARR` of the foreign key field `CARRID` of the foreign key table `SPFLI`.

``` abap
... 
define table spfli { 
  ... 
  @AbapCatalog.foreignKey.label : 'Check Against Airline' 
  @AbapCatalog.foreignKey.keyType : #KEY 
  @AbapCatalog.foreignKey.screenCheck : true 
  key carrid : s_carr_id not null 
    with foreign key [0..*,1] scarr 
      where mandt = spfli.mandt 
        and carrid = spfli.carrid; 
  ... 
}
```
