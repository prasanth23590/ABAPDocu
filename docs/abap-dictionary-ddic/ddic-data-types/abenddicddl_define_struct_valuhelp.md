---
title: "DDIC DDL - DEFINE STRUCTURE, value_help"
source_file: abenddicddl_define_struct_valuhelp.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Structures > DDIC - Dictionary DDL for Structure Definitions > DDIC DDL - DEFINE STRUCTURE > DDIC DDL - DEFINE STRUCTURE, component"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC DDL - DEFINE STRUCTURE, value_help

## Syntax

``` abap
...  WITH VALUE HELP value_help 
       WHERE parameter1 = structure.component1 
         [AND parameter2 = structure.component2 ...] ...  
```

## Description

Assigns a [search help](../../abap-glossary/abensearch_help_glosry.md) to a [structure component](abenddicddl_define_struct_comps.md) whose data type is defined by a data element with an elementary data type in the definition of a structure using the statement [`DEFINE STRUCTURE`](abenddicddl_define_structure.md) in [Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md). Here, `value_help` is an existing search help in the ABAP Dictionary. All parameters of the search help must be linked with structure components after `WHERE`.

## Hint

The addition `WITH VALUE HELP` can be used, with the same meaning, in the definition of a database using [`DEFINE TABLE`](../ddic-database-tables/abenddicddl_define_table.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of elementary components with reference to data elements and binds a search help to the second component.

``` abap
... 
define structure struct { 
  comp1 : s_carr_id; 
  comp2 : s_conn_id 
    with value help demo_f4_field 
      where carrid = struct.comp1 
        and connid = struct.comp2; 
  ... 
  }
```
