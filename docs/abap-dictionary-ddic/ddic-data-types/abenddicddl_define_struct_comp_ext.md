---
title: "DDIC DDL - DEFINE STRUCTURE, extend"
source_file: abenddicddl_define_struct_comp_ext.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Structures > DDIC - Dictionary DDL for Structure Definitions > DDIC DDL - DEFINE STRUCTURE > DDIC DDL - DEFINE STRUCTURE, include"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC DDL - DEFINE STRUCTURE, extend

## Syntax

``` abap
... [foreign_key_annos] 
    EXTEND component : [value_help] [foreign_key] ...  
```

[`foreign_key_annos`](../ddic-database-tables/abenddicddl_define_table_fkprps.md) · [`value_help`](abenddicddl_define_struct_valuhelp.md) · [`foreign_key`](../ddic-database-tables/abenddicddl_define_table_forkey.md)

## Description

Defines component properties when [including](abenddicddl_define_struct_incl.md) include structures using the statement [`DEFINE STRUCTURE`](abenddicddl_define_structure.md) in [Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md). The addition `EXTEND` can be specified for the every component `component` in the included [include structure](abenddic_include_structure.md) and defines the following properties for this structure. If any of the properties of the included component already exist, they are overwritten.

- [`foreign_key_annos`](../ddic-database-tables/abenddicddl_define_table_fkprps.md) - Properties of a foreign key relationship

- [`value_help`](abenddicddl_define_struct_valuhelp.md) - Assignment to a search help.

- [`foreign_key`](../ddic-database-tables/abenddicddl_define_table_forkey.md) - Definition of a foreign key dependency.

At least one of the additions `value_help` and `foreign_key` must be specified.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Inclusion of a structure `include_struct` in a structure `struct`, where `EXTEND` is used to assign a search help to the components `comp1` and `comp2`.

``` abap
... 
define structure struct { 
  ... 
  include include_struct 
    extend comp1 : 
      with value help demo_f4_field 
        where carrid = struct.comp1 
          and connid = struct.comp2 
    extend comp2 : 
      with value help demo_f4_field 
        where carrid = struct.comp1 
          and connid = struct.comp2; 
  ... 
  }
```
