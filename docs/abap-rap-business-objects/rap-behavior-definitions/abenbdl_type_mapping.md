---
title: "RAP - TypeMapping"
source_file: abenbdl_type_mapping.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - TypeMapping

## Syntax

``` abap
... mapping for PartnerType           [control ControlType] 
                                      {[corresponding [extensible][except EntityComp1,EntityComp2, ...]]} 
    [{ 
      EntityComp1       = PartnerComp1 [control ControlComp1]; 
     [EntityComp2       = PartnerComp2 [control ControlComp2];] 
     [parameter Param   = PartnerComp3;] 
     [constant Literal  = PartnerComp4;] 
     [... ;] 
    }] 
...  
```

[`extensible`](abenbdl_extensibility_enabling_m_u.md)

### Addition

[1. `... control`](abenbdl_type_mapping.md#addition-1)

[2. `... corresponding [except]`](abenbdl_type_mapping.md#addition-2)

[3. `... corresponding extensible`](abenbdl_type_mapping.md#addition-3)

## Overview

### Description

[RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) maps data types of the data model that is defined in CDS for a RAP BO to other data types that do not the match BDEF derived type component pattern. Type mapping is useful for applications whose [business object](../../abap-glossary/abenbusiness_object_glosry.md) implements existing types or existing functions. The mapping connects a [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) to an existing [DDIC type](../../abap-glossary/abenddic_type_glosry.md) in the behavior definition of a business object.

`PartnerType` is the name of a [DDIC structure](../../abap-glossary/abenddic_structure_glosry.md). Within curly brackets, components that correspond to each other but do not have the same name are mapped to each other using the equal operator (`=`). On the left-hand side, the following options are possible:

- The name of a field of the current RAP BO entity `EntityComp1`, `EntityComp2`, ... can be specified.

- [Input parameters](abenbdl_action_input_param.md) of actions and functions `Param` can be specified, introduced by the keyword `parameter`.

- Fixed values `Literal` can be specified, introduced by the keyword `constant`. `Literal` can be specified as an [untyped](../../abap-glossary/abenuntyped_literal_glosry.md) character literal or an untyped numeric literal. This syntax can be used to map a field of the underlying RAP persistent table to a fixed value in the BDEF type mapping. This can be useful in scenarios where different entities are mapped to the same underlying table.

On the right-hand side of the equal operator, the name of a component of the partner type `PartnerComp1`, `PartnerComp2`, ... is specified.

One or more type mappings are possible in a behavior definition. If multiple type mappings are defined, each type mapping must define a mapping for a different partner type `PartnerType`. For each partner type, exactly one mapping can be defined.

If the names of the fields of the DDIC structure and in the current data model are exactly the same, no mapping is required. Otherwise, it is mandatory (syntax check warning). In particular, in case of a managed RAP BO, the field names of the [RAP persistent table](../../abap-glossary/abenrap_persistent_table_glosry.md) must match the field names of the corresponding [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md). If the names do not match, a type mapping is required. Otherwise, a syntax check warning occurs.

No implementation in an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is required.

The [assignment and conversion rules](../../abap-programming-language/abap-processing-internal-data/abenconversion_rules.md) for elementary data objects apply to the mapping of components.

When using the addition `corresponding`, it is also possible to leave out the mapping of individual components specified in curly brackets.

## Availability

- [Managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BOs](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- [Projection BOs](../../abap-glossary/abenrap_projection_bo_glosry.md)

- [Abstract BDEFs](../../abap-glossary/abencds_abstract_bdef_glosry.md)

## More Information

- Development guide for the ABAP RESTful Application Programming Model, topic [Using Type and Control Mapping](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/0b143178489a4397a0eb5013d4c8b03d?version=sap_cross_product_abap).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF based on the CDS root view entity `DEMO_RAP_MANAGED_ASSOC_ROOT`. A type mapping from the fields of the database table to the fields of the BO entities is defined. This is required since the fields of the CDS view entities have alias names and therefore differ from the field names of the database table.

**Note:** This example does not fully meet the requirements of the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). It is intentionally kept short and simple and serves demonstration purposes only. See more information on the RAP BO contract in the [Development guide for the ABAP RESTful Application Programming Model](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

``` abap
managed
implementation in class BP_DEMO_RAP_MANAGED_ASSOC_ROOT unique;
strict ( 2 );
with cross associations;

define behavior for DEMO_RAP_MANAGED_ASSOC_ROOT alias _Root
persistent table demo_dbtab_root
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  association _child { create; }
  association _ext { create; }
  field ( readonly : update ) KeyFieldRoot;

  mapping for demo_dbtab_root
    {
      KeyFieldRoot  = key_field;
      DataFieldRoot = data_field;
      CharFieldRoot = char_field;
      CharFieldRoot2 = char_field_2;
      DecFieldRoot  = dec_field;
      constant 'Demo' = char_field_3;
    }
}

define behavior for DEMO_RAP_MANAGED_ASSOC_CHILD alias _Child
persistent table demo_dbtab_child
lock dependent by _parent
authorization dependent by _parent
{
  update;
  delete;

  association _parent { }

  field ( readonly : update ) KeyField, KeyFieldChild;
  mapping for demo_dbtab_child
    {
      KeyField      = key_field;
      KeyFieldChild = key_field_child;
      DataField     = data_field;
      CharField     = char_field;
    }
}
```

## Addition 1

`... control`

### Description

`control` maps a type of the RAP business object to a [control structure](../../abap-glossary/abencontrol_structure_glosry.md). A control structure has the same components as `PartnerType` with the difference that all components have the [built-in ABAP type](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) `c(1)` or `x(1)`. Its function is to indicate which of the fields are accessed by an operation. The control structure works analogous to the [`%control`](../abap-for-rap-business-objects/abapderived_types_comp.md) structure in derived types. A mapping can be done simultaneously for a main type `PartnerType` and for a control type `ControlType`.

In a standard use case, the field names of the main and the control types should be identical. If this is not the case, fields can be mapped to each other using the addition `control`.

If a component of the main structure is missing in the control structure, this is tolerated and leads to two independently executable mappings.

## Addition 2

`... corresponding [except]`

### Description

The optional addition `corresponding` defines that components with the same name are automatically mapped to each other. The addition `except` can be specified together with `corresponding` to exclude components with identical names from the automatic mapping.

Example: `mapping for PartnerType corresponding;`.

## Addition 3

`... corresponding extensible`

### Description

The optional addition `extensible` enables [BDEF extensions](../../abap-glossary/abenrap_extension_glosry.md) for the type mapping in question. That means that [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md) are allowed to add extension fields to that particular type mapping. `extensible` can only be used in combination with `corresponding`, so that components with the same name are automatically mapped to each other.

Example: `mapping for PartnerType corresponding extensible;`.

For details on extensibility enabling, see topic [RAP - Extensibility Enabling for Base BOs](abenbdl_extensibility_enabling_m_u.md).
