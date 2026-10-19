---
title: "DDIC DDL - DEFINE STRUCTURE, component"
source_file: abenddicddl_define_struct_comps.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Structures > DDIC - Dictionary DDL for Structure Definitions > DDIC DDL - DEFINE STRUCTURE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC DDL - DEFINE STRUCTURE, component

## Syntax

``` abap
[component_annos] 
[foreign_key_annos] 
[geo_annos] 
[KEY] comp : { {data_element [value_help] 
                             [foreign_key]} 
               |abap.type[(n)|(n,m)] } 
           | { REFERENCE TO any_type } 
           | { struct [BOXED] } 
           | { table_type } 
           [NOT NULL];  
```

[`component_annos`](abenddicddl_define_struct_cmpprps.md) · [`foreign_key_annos`](../ddic-database-tables/abenddicddl_define_table_fkprps.md) · [`geo_annos`](../ddic-database-tables/abenddicddl_define_table_srprps.md) · [`value_help`](abenddicddl_define_struct_valuhelp.md) · [`foreign_key`](../ddic-database-tables/abenddicddl_define_table_forkey.md) · [`type`](../ddic-built-in-data-types/abenddic_builtin_types.md)

## Description

Defines a single [component](abenddic_structures_tech.md) in the definition of a DDIC structure using the statement [`DEFINE STRUCTURE`](abenddicddl_define_structure.md) in [Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md).

- Optional component properties can be specified using annotations [`component_annos`](abenddicddl_define_struct_cmpprps.md).

- [`foreign_key_annos`](../ddic-database-tables/abenddicddl_define_table_fkprps.md) can be used to specify the properties of a foreign key dependency defined with [`foreign_key`](../ddic-database-tables/abenddicddl_define_table_forkey.md).

- [`geo_annos`](../ddic-database-tables/abenddicddl_define_table_srprps.md) specify properties of a component with the [geodata type](../../abap-glossary/abengeo_data_type_glosry.md) `GEOM_EWKB`.

- `comp` indicates the name of the component.

- `data_element` or `abap.type` is used to define an elementary component or a component with a reference type:

  - `data_element` can be used to specify an existing [DDIC data element](../../abap-glossary/abendata_element_glosry.md). If the data element has an elementary data type, an elementary component is defined. If the data element has a reference type, the component is defined with this reference type.

  - `abap.type[(n)|(n,m)]` can be used to specify a built-in data type from the ABAP Dictionary and an elementary component of this type is defined. The prefix `abap` is mandatory and [`type`](../ddic-built-in-data-types/abenddic_builtin_types.md) indicates the type. `n` and `m` specify the length and number of decimal places, if required.

- `REFERENCE TO any_type` is used to define a reference type. For `any_type`, the syntax `abap.type[(n)|(n,m)]` can be used to specify any existing data types from the ABAP Dictionary, classes or interfaces from the class library, the generic types `DATA` or `OBJECT`, or built-in types.

- `struct [BOXED]` is used to define a substructure. DDIC structures, DDIC database tables, or DDIC views can all be specified for `struct`. `BOXED` can be used to define the substructure as a [static box](../../abap-glossary/abenstatic_box_glosry.md).

- `table_type` is used to define a tabular component. [Table types](../../abap-glossary/abentable_type_glosry.md) from the ABAP Dictionary can be specified for `table_type`.

- The additions `KEY` and `NOT NULL` can be used to define the component as a [key field](abenddic_structures_sema.md) and to set a [flag for initial values](abenddic_structures_sema.md). The addition `KEY` has no effect when the structure is included in DDIC database tables. The addition `NOT NULL` can be respected for structures that are included in DDIC database tables.

- The addition [`value_help`](abenddicddl_define_struct_valuhelp.md) can be used to assign a search help to a structure component whose data type is defined using a data element with elementary data type.

- The addition [`foreign_key`](../ddic-database-tables/abenddicddl_define_table_forkey.md) can be used to define a [foreign key dependency](../../abap-glossary/abenforeign_key_dependency_glosry.md) for a structure component whose data type is defined using a data element with elementary data type. This addition only makes sense for structures that are included in DDIC database tables.

## Hint

The [activation type](abenddic_structures_tech.md) (relevant only for DDIC database tables) cannot be modified using `DEFINE STRUCTURE`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of elementary components of the structure `DEMO_DAY` with reference to built-in dictionary types. In the example for [include structures](abenddicddl_define_struct_incl.md), the structure is included more than once in another structure.

``` abap
@EndUserText.label : 'Demo for include structure' 
@AbapCatalog.enhancement.category : #NOT_EXTENSIBLE 
define structure demo_day { 
  work : abap.char(8); 
  free : abap.char(16); }
```
