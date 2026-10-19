---
title: "RAP - Extensibility Enabling for Abstract BDEF Extensions"
source_file: abenbdl_ext_enabl_ext_abs.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - BDEF Extension, Extensibility Enabling > RAP - Extensibility Enabling for BDEF Extensions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Extensibility Enabling for Abstract BDEF Extensions

## Syntax

``` abap
extension for abstract 
extensible; 
[...] 
extend behavior for EntityName 
  [...] 
{ 
  [...] 
  [[deep] mapping for PartnerType corresponding extensible] 
   ... 
} 
 
define behavior for ExtNode 
  extensible 
  [...] 
{ 
  [...] 
  [[deep] mapping for PartnerType corresponding extensible] 
  ... 
} 
[...] 
...  
```

[`extension for abstract`](abenbdl_extension_for_abstract.md) · [`extensible`](abenbdl_extensible.md) · [`extend behavior for EntityName`](abenbdl_extension_for_abstract.md) · [`[deep] mapping for PartnerType corresponding extensible`](abenbdl_type_mapping_abstract.md) · [`define behavior for ExtNode`](abenbdl_extension_for_abstract.md) · [`extensible`](abenbdl_extensible.md) · [`[deep] mapping for PartnerType corresponding extensible`](abenbdl_type_mapping_abstract.md)

## Description

To extend an [abstract BDEF extension](../../abap-glossary/abenrap_abs_bdef_ext_glosry.md), the keyword `extensible` can be specified in the following places:

- `extensible` in the abstract BDEF extension header:

  Prerequisite for extensibility. If it is not specified, extensions are not allowed. If specified, at least one component of the abstract BDEF extension must be declared as extensible. Allows the following components to be added to an abstract BDEF extension via another abstract BDEF extension:

  - Adding new nodes to the hierarchical type of the abstract BDEF using the statement [`define behavior for AbstractEntity`](abenbdl_extension_for_abstract.md).

  - Adding new scalar entities to the hierarchical type using the statement [`scalar entity`](abenbdl_extension_for_abstract.md).

- `extensible` in the body of an [entity behavior extension](../../abap-glossary/abenrap_behavior_extension_glosry.md):

  - [`[deep] mapping for PartnerType corresponding extensible`](abenbdl_type_mapping_abstract.md): a [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) can be extended with extension fields. `extensible` can only be used in combination with `corresponding`, so that components with the same name are automatically mapped to each other.

- `extensible` specified for an individual node after the statement [`define behavior for AbstractEntity`](abenbdl_extension_for_abstract.md)

  Mandatory for each individual node that allows extensions. Allows the following extensions to be added via an abstract BDEF extension:

  - [RAP field characteristics](../../abap-glossary/abenrap_field_char_glosry.md) can be added to extension fields.

  - Associations

  - [Type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md)

- `extensible` in the [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md):

  [`[deep] mapping for PartnerType corresponding extensible`](abenbdl_type_mapping_abstract.md): a [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) defined in the original abstract BDEF can be extended with extension fields. `extensible` can only be used in combination with `corresponding`, so that components with the same name are automatically mapped to each other.

**Note:** It is not required that the underlying [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) is declared as `extensible`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The abstract BDEF extension `DEMO_RAP_ABSTRACT_X` allows for BDEF extensions:

``` abap
extension for abstract;
extensible;

extend behavior for DEMO_RAP_ABSTRACT_ROOT
{
  association _item3;
  extend deep mapping for demo_rap_struc_x
    {
      sub _Item3 = sub_3;
    }
}

scalar entity DEMO_RAP_ABSTRACT_5 field comp3;

extend behavior for DEMO_RAP_ABSTRACT_1
{
  association _x1;
}

define behavior for DEMO_RAP_ABSTRACT_4
with control
extensible
{
  field ( suppress ) comp1, comp2;
}
```

The abstract BDEF extension `DEMO_RAP_ABSTRACT_X1` extends the BDEF extension `DEMO_RAP_ABSTRACT_X`:

``` abap
extension for abstract;

extend behavior for DEMO_RAP_ABSTRACT_ROOT
{
}

extend behavior for DEMO_RAP_ABSTRACT_1
{
}
```
