---
title: "RAP - Extensibility Enabling for Abstract BDEFs"
source_file: abenbdl_ext_enabling_abstract.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - BDEF Extension, Extensibility Enabling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Extensibility Enabling for Abstract BDEFs

## Syntax

``` abap
abstract 
strict[(version)]; 
extensible; 
define behavior for AbstractEntity 
  extensible 
  [...] 
{ 
  [...] 
  [[deep] mapping for PartnerType corresponding extensible] 
  [...] 
} 
 ...  
```

[`abstract`](abenbdl_impl_type.md) · [`strict[(version)]`](abenbdl_strict.md) · [`extensible`](abenbdl_extensible.md) · [`define behavior for AbstractEntity`](abenbdl_define_beh_abstract.md) · [`extensible`](abenbdl_extensible.md) · [`[deep] mapping for PartnerType corresponding extensible`](abenbdl_type_mapping_abstract.md)

## Prerequisite

To allow [abstract BDEF extensions](../../abap-glossary/abenrap_abs_bdef_ext_glosry.md) to an [abstract behavior definition](../../abap-glossary/abencds_abstract_bdef_glosry.md), [BDEF strict mode](../../abap-glossary/abenrap_strict_mode_glosry.md) must be switched on using the keyword [`strict [(version)]`](abenbdl_strict.md).

## Description

The keyword `extensible` can be specified at different places to allow for extensions:

- `extensible` in the [abstract BDEF header](abenbdl_bdef_abstract_header.md)

  Prerequisite for extensibility. If it is not specified, then extensions are not allowed. If specified, at least one entity must be declared as extensible after the statement [`define behavior for AbstractEntity ...`](abenbdl_define_beh_abstract.md) Allows the following components to be added to an abstract behavior definition via an abstract BDEF extension:

  - Adding new nodes to the hierarchical type of the abstract BDEF using the statement `define behavior for AbstractEntity`.

  - Adding new scalar entities to the hierarchical type.

- `extensible` specified for an individual node after the statement `define behavior for AbstractEntity`

  Mandatory for each individual node that allows extensions. Allows the following extensions to be added via an abstract BDEF extension:

  - [RAP field characteristics](../../abap-glossary/abenrap_field_char_glosry.md) can be added to extension fields.

  - Associations

  - [Type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md)

- `extensible` in the [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md):

  [`[deep] mapping for PartnerType corresponding extensible`](abenbdl_type_mapping.md): a [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) defined in the original abstract BDEF can be extended with extension fields. `extensible` can only be used in combination with `corresponding`, so that components with the same name are automatically mapped to each other.

**Note:** It is not required that the underlying [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) is declared as `extensible`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The abstract behavior definition `DEMO_RAP_ABSTRACT_ROOT` enables BDEF extensions:

``` abap
abstract;
strict ( 2 );
extensible;
with hierarchy;

define behavior for DEMO_RAP_ABSTRACT_ROOT
extensible
with control
{
// key field, unwanted in derived types
  field ( suppress ) comp1key;

  association _item;
  association _sib;

  deep mapping for demo_rap_struc_x corresponding extensible
    {
          comp2 = comp2;
    }
}

define behavior for DEMO_RAP_ABSTRACT_1
extensible
with control
{
// foreign key field for parent, unwanted in derived types
  field ( suppress ) comp1, comp2;

}
```
