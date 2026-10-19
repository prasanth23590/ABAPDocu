---
title: "DDIC DDL - DEFINE STRUCTURE, include"
source_file: abenddicddl_define_struct_incl.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Structures > DDIC - Dictionary DDL for Structure Definitions > DDIC DDL - DEFINE STRUCTURE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC DDL - DEFINE STRUCTURE, include

## Syntax

``` abap
[group :] INCLUDE struct [WITH SUFFIX suffix] 
                  [... 
                   extend 
                   ...];  
```

[`extend`](abenddicddl_define_struct_comp_ext.md)

## Description

Includes an [include structure](abenddic_include_structure.md) in the definition of a structure with the statement [`DEFINE STRUCTURE`](abenddicddl_define_structure.md) in [Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md).

- Any existing DDIC structure, DDIC database table, or DDIC view can be specified as `struct`.

- `group` can be used to specify an optional name of a [group](abenddic_include_structure.md).

- `suffix` can be used to specify an optional three-character [suffix](abenddic_include_structure.md).

- A blank-separated list of additions, [`extend`](abenddicddl_define_struct_comp_ext.md), can be used to overwrite the assignment to a search help and the definition of a foreign key dependency for each included component.

## Hint

The addition `INCLUDE` can be used with the same semantics in the statement [`DEFINE TABLE`](../ddic-database-tables/abenddicddl_define_table.md) if the include structure is suitable for DDIC database tables.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Syntax for defining the structure `DEMO_WEEK` in ADT.

``` abap
... 
define structure demo_week { 
  monday    : include demo_day with suffix _mo; 
  tuesday   : include demo_day with suffix _tu; 
  wednesday : include demo_day with suffix _we; 
  thursday  : include demo_day with suffix _th; 
  friday    : include demo_day with suffix _fr; 
}
```
