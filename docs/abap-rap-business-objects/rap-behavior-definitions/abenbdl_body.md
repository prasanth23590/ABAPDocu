---
title: "RAP - EntityBehaviorBody"
source_file: abenbdl_body.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - EntityBehaviorBody

## Syntax

``` abap
 
... {[FieldCharacteristics] 
     [FieldNumbering] 
     [RAP BO Operations] 
     [validation] 
     [determination] 
     [Events] 
     [side effects] 
     [changedocuments, Options] 
     [instance hierarchy] 
     [BDEF alternative key] 
     [TypeMapping]} 
     [group] 
...  
```

[`FieldCharacteristics`](abenbdl_field_char.md) · [`FieldNumbering`](abenbdl_field_numbering.md) · [`RAP BO Operations`](abenbdl_operations.md) · [`validation`](abenbdl_validations.md) · [`determination`](abenbdl_determinations.md) · [`Events`](abenbdl_event_overview.md) · [`side effects`](abenbdl_side_effects.md) · [`changedocuments, Options`](abenbdl_changedocs_options.md) · [`instance hierarchy`](abenbdl_instance_hierarchy.md) · [`BDEF alternative key`](abenbdl_define_key.md) · [`TypeMapping`](abenbdl_type_mapping.md) · [`group`](abenbdl_grouping.md)

## Description

The [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md) can consist of the following elements:

- [`FieldCharacteristics`](abenbdl_field_char.md): [RAP field characteristics](../../abap-glossary/abenrap_field_char_glosry.md) define properties for RAP BO fields that restrict access to the fields in question. For example, a field can be defined as mandatory read-only.

- [`FieldNumbering`](abenbdl_field_numbering.md): Defines managed [internal numbering](../../abap-glossary/abenrap_int_numbering_glosry.md) for key fields.

- [RAP BO operations](abenbdl_operations.md): [RAP BO operations](../../abap-glossary/abenrap_bo_operation_glosry.md) implement the [RAP BO behavior](../../abap-glossary/abenrap_bo_behavior_glosry.md).

- [`validation`](abenbdl_validations.md): [Validations](../../abap-glossary/abenrap_validation_glosry.md) check the consistency of a RAP business object instance.

- [`determination`](abenbdl_determinations.md): [Determinations](../../abap-glossary/abenrap_determination_glosry.md) calculate or determine field values at runtime.

- [`Events`](abenbdl_event_overview.md): [RAP business events](../../abap-glossary/abenrap_entity_event_glosry.md) are events that can be used for asynchronous communication.

- [`side effects`](abenbdl_side_effects.md): [RAP side effects](../../abap-glossary/abenrap_side_effects_glosry.md) define interdependencies among BO properties that trigger a reload of the affected properties on the user interface.

- [`changedocuments, Options`](abenbdl_changedocs_options.md): If the RAP BO entity in question is enabled for [change documents](../../abap-glossary/abenrap_change_documents_glosry.md), logging options can be defined in the entity behavior body.

- [`instance hierarchy`](abenbdl_instance_hierarchy.md): Enables the editable [treeview](../../abap-glossary/abenrap_treeview_glosry.md) scenario.

- [BDEF alternative key](abenbdl_define_key.md): A [BDEF alternative key](../../abap-glossary/abenrap_alternative_key_glosry.md) defines a user-defined BDEF key. There are [pure keys](../../abap-glossary/abenrap_pure_key_glosry.md) and [secondary keys](../../abap-glossary/abenrap_secondary_key_glosry.md) and they are used, for example, in [RAP key functions](abenbdl_keyfunction.md).

- [`TypeMapping`](abenbdl_type_mapping.md): A [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) is required if the field names from database tables differ from field names of the CDS data model.

- [`group`](abenbdl_in_class_unique.md): Implementation grouping makes it possible to divide the implementation-relevant parts of a business object's business logic into multiple groups for behavior implementation, each with its own [implementation class](abenbdl_in_class_unique.md).
