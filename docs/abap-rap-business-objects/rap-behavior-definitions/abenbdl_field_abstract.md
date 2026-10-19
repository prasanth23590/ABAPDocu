---
title: "RAP - Field Characteristics, Abstract BDEF"
source_file: abenbdl_field_abstract.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Abstract Behavior Definitions > RAP - Entity Behavior Definition, Abstract BDEF > RAP - Entity Behavior Body, Abstract BDEF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Field Characteristics, Abstract BDEF

## Syntax

``` abap
... field(suppress) Field1, Field2, ...; 
       | (mandatory:execute) Field1, Field2, ...;  
```

### Variant

[1. `... field(suppress) Field1, Field2, ...`](abenbdl_field_abstract.md#variant-1)

[2. `... field(mandatory:execute) Field1, Field2, ...`](abenbdl_field_abstract.md#variant-2)

## Overview

### Description

This topic lists field attributes for the [fields](../../abap-glossary/abenrap_bo_field_glosry.md) of an [abstract BDEF](../../abap-glossary/abencds_abstract_bdef_glosry.md).

Commas can be used to classify multiple fields in the same way. Example: `field(suppress) Field1, Field2, Field3;`.

## Variant 1

`... field(suppress) Field1, Field2, ...`

### Description

- Removes a field from all [derived types](../../abap-glossary/abenrap_derived_type_glosry.md) generated for the BDEF. In particular, the redundancy is avoided in the [`TYPE TABLE FOR HIERARCHY`](../abap-for-rap-business-objects/abaptype_table_for.md) / [`TYPE STRUCTURE FOR HIERARCHY`](../abap-for-rap-business-objects/abaptype_structure_for.md) types.

- This is possible for all fields except for [key fields](../../abap-glossary/abenkey_field_glosry.md) and fields used by the current BDEF.

### Hint

A typical use case for `field(suppress)` was to exclude foreign-key fields used in the `ON` condition of the [to-parent association](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_absent_to_parent_assoc.md) to appear redundantly in the hierarchical type. This was particularly useful when it was still mandatory to define an `ON` condition in to-parent associations of CDS abstract entities. However, since release 7.85, the `ON` condition can be left out.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following abstract BDEF suppresses one field from its derived type.

``` abap
abstract;
strict(2);

define behavior for DEMO_CDS_SCALAR_ROOT_3 alias Root
{
  field ( suppress ) field2;
}
```

## Variant 2

` field(mandatory:execute) Field1, Field2, ...`

### Description

- Declares a field of an abstract BDEF as mandatory. Whenever the hierarchical type is used as [input parameter](abenbdl_action_input_param.md) for a [RAP action](../../abap-glossary/abenrap_action_glosry.md) or a [RAP function](../../abap-glossary/abenrap_function_glosry.md), a value must be supplied. Otherwise, a [runtime error](../../abap-glossary/abenruntime_error_glosry.md) occurs.

- As a prerequisite, the addition [`with hierarchy`](abenbdl_bdef_abstract_header.md) must be used in the [behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md) and [`with control`](abenbdl_define_beh_abstract.md) must be specified for the [entity behavior definition](../../abap-glossary/abencds_entity_bdef_glosry.md) in question. Moreover, [BDEF strict mode](../../abap-glossary/abenrap_strict_mode_glosry.md) must be enabled.

### Hint

When using [`IN LOCAL MODE`](../abap-for-rap-business-objects/abapin_local_mode.md), `mandatory:execute` does not have any effect.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following abstract BDEF defines the field `NUM1` as `mandatory:execute`. It fulfills the mandatory prerequisites and uses both the additions `with hierarchy` and `with control`.

``` abap
abstract;
strict(2);
with hierarchy;

define behavior for DEMO_ABSTRACT_ROOT
with control
{
  association _item1;
  association _item2;
  association _scalar;

  field ( mandatory:execute ) num1;

}

define behavior for DEMO_HIER_ABS_ITEM1
with control
{
  field ( suppress ) root2_id;
  association _root2 with hierarchy;
}

define behavior for DEMO_HIER_ABS_ITEM2
with control
{
}

scalar entity DEMO_HIER_ABS_SCALAR field char1;
```

This abstract BDEF is used as input parameter for the action `ACTION_DEEP_PARAM` in the managed BDEF `DEMO_MANAGED_HIERARCHY`.

``` abap
managed implementation in class bp_demo_managed_hierarchy unique;
strict(2);

define behavior for DEMO_MANAGED_HIERARCHY
persistent table demo_tab_root_6
lock master
authorization master ( none )

{
  create;
  update;
  delete;

  field ( readonly, numbering : managed ) id;

  // flat
  static action action_flat_param parameter
    DEMO_ABSTRACT_ROOT result [1..*] $self;

  // structure as input parameter
  static action action_deep_param deep parameter
    DEMO_ABSTRACT_ROOT result [1..*] $self;

  // table as input parameter
  static action action_deep_table_param deep table
    parameter DEMO_ABSTRACT_ROOT result [1..*] $self;

  static action storeHData deep parameter
    DEMO_ABSTRACT_ROOT result [1..*] $self;

  static action returnHData deep result [1] DEMO_ABSTRACT_ROOT;

}
```

The ABAP class `CL_DEMO_MANDATORY_EXECUTE` executes the action `ACTION_DEEP_PARAM`. It supplies a value for the field `NUM1` and sets the [`%control`](../abap-for-rap-business-objects/abapderived_types_comp.md) structure for this field to `if_abap_behv=>mk-on`.

Code Snippet:

``` abap
MODIFY ENTITY demo_managed_hierarchy 
       EXECUTE action_deep_param 
       FROM VALUE #( ( %cid = 'cid_deep_param' 
                       %param = VALUE #( 
                         char1 = 'a' 
                         char2 = 'b' 
                         "num1 and the corresponding field of the 
                         "control-structure are mandatory. 
                         num1 = 1 
                         %control-num1 = if_abap_behv=>mk-on 
                         num2 = 2 
                         %control-num2 = if_abap_behv=>mk-off ) ) ) 
        RESULT FINAL(lt_result2) 
        MAPPED FINAL(ls_mapped2) 
        REPORTED FINAL(ls_reported2) 
        FAILED FINAL(ls_failed2).
```

The following code results in a runtime error, since the `%control` structure for field `NUM1` is set to `if_abap_behv=>mk-off`.

Code Snippet:

``` abap
MODIFY ENTITY demo_managed_hierarchy 
       EXECUTE action_deep_param 
       FROM VALUE #( ( %cid = 'cid_deep_param' 
                       %param = VALUE #( 
                         char1 = 'a' 
                         char2 = 'b' 
                         num1 = 1 
                         %control-num1 = if_abap_behv=>mk-off 
                         num2 = 2 
                         %control-num2 = if_abap_behv=>mk-off ) ) ) 
        RESULT FINAL(lt_result2) 
        MAPPED FINAL(ls_mapped2) 
        REPORTED FINAL(ls_reported2) 
        FAILED FINAL(ls_failed2).
```

### Executable Example

An executable example is available in topic [Using `TYPE TABLE` /`TYPE STRUCTURE FOR HIERARCHY`](../abap-for-rap-business-objects/abenderived_type_hierarchy_abexa.md).
