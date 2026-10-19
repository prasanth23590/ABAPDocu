---
title: "RAP - Adding Elements"
source_file: abenbdl_new_elem_ext.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension > RAP - EntityBehaviorExtension > RAP - ExtensionBody"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Adding Elements

## Syntax

``` abap
... 
  [determination] 
  [validation] 
  [event] 
  [managed event] 
  [field characteristics] 
  [action] 
  [function] 
  [determine action] 
  [association] 
  [define pure key] 
  [mapping for] 
  ...  
```

[`determination`](abenbdl_determinations.md) · [`validation`](abenbdl_validations.md) · [`event`](abenbdl_event.md) · [`managed event`](abenbdl_managed_event.md) · [`field characteristics`](abenbdl_field_char.md) · [`action`](abenbdl_action.md) · [`function`](abenbdl_function.md) · [`determine action`](abenbdl_determine_action.md) · [`association`](abenbdl_association.md) · [`define pure key`](abenbdl_define_key.md) · [`mapping for`](abenbdl_type_mapping.md)

### Variant

[1. `... determination ...`](abenbdl_new_elem_ext.md#variant-1)

[2. `... validation ...`](abenbdl_new_elem_ext.md#variant-2)

[3. `... event ...`](abenbdl_new_elem_ext.md#variant-3)

[4. `... managed event ...`](abenbdl_new_elem_ext.md#variant-4)

[5. `... field characteristics ...`](abenbdl_new_elem_ext.md#variant-5)

[6. `... action ...`](abenbdl_new_elem_ext.md#variant-6)

[7. `... function ...`](abenbdl_new_elem_ext.md#variant-7)

[8. `... determine action ...`](abenbdl_new_elem_ext.md#variant-8)

[9. `... association ...`](abenbdl_new_elem_ext.md#variant-9)

[10. `... define pure key ...`](abenbdl_new_elem_ext.md#variant-10)

[11. `... mapping for...`](abenbdl_new_elem_ext.md#variant-11)

## Overview

### Description

The elements listed in this topic can be added to the [body](../../abap-glossary/abencds_entity_body_glosry.md) of an existing RAP BO entity. All of them are optional, and multiple elements or all elements can be specified together.

The elements can be added in a [base BDEF extension](../../abap-glossary/abenrap_base_bdef_ext_glosry.md) with or without the addition [`using interface`](abenbdl_using_interface.md). In other words, these elements are possible in direct base extensions and also in extensions that make use of an interface layer.

### Executable Example

Executable examples:

- [Node extension](abenbdl_assoc_ext_abexa.md):

  - A RAP BO with four nodes is extended via a RAP BO interface with one further node on the level of the great-grandchild.

  - Ancestor associations are defined, while lock master and authorization master entities are not explicitly defined.

  - An ABAP EML call creates instances of all five nodes.

- [Field extension](abenbdl_field_ext_abexa.md)

  - The original BO consists of one root node.

  - The root node is extended via a RAP BO interface with extension fields. These extension fields are created on database level and added to the CDS data model via a CDS data model extension.

  - Field attributes are added to the extension fields.

  - Dynamic feature control for the extension fields is implemented in the extension ABP.

- [Behavior extension](abenbdl__behavior_ext_abexa.md):

  - The original BO consists of one root node.

  - One extension node is added to the original BO via a RAP BO interface.

  - The extended RAP BO implements authorization control, feature control, a validation, a determination and two actions. These implementations are distributed between original ABP and extension ABP.

  - An ABAP EML call performs multiple operations and logs the execution order of the handler methods.

## Variant 1

`... determination ...`

### Description

- Adds a [RAP determination](../../abap-glossary/abenrap_determination_glosry.md) to the entity behavior body of an existing RAP BO entity via a BDEF extension.

- As a prerequisite, the extended BDEF must explicitly allow the particular kind of determination (see the topic [RAP - Extensibility Enabling for Base BOs](abenbdl_extensibility_enabling_m_u.md)).

- Syntax: exactly the same as for RAP BOs, see the topic [RAP - `determination`](abenbdl_determinations.md).

- All fields (extension fields and original fields) can be used as trigger.

- Implementation in the extension ABAP behavior pool must obey the rules for [extension ABPs](abenbdl_in_class_unique_ext.md).

- **Limitation:** Currently not supported for BDEF extensions to unmanaged RAP BOs.

### Hint

The execution order of determinations and validations is arbitrary, also between original and extension components.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The BDEF extension `DEMO_RAP_EXT_DET_VAL` extends the RAP behavior definition `DEMO_RAP_BASE_DET_VAL`. It adds a determination on save `setStatus`, which is triggered whenever a new entity instance is created.

Original BDEF: explicitly allows determinations on save in the BDEF extension header:

``` abap
managed implementation in class bp_demo_rap_base_det_val unique;
strict ( 2 );
extensible
{ with determinations on modify;
  with determinations on save;
  with validations on save; }

define behavior for DEMO_RAP_BASE_DET_VAL
persistent table demo_dbtab_root
lock master
authorization master ( none )
extensible
{
  create;
  update;
  delete;
  field ( readonly : update ) key_field;
}
```

Extension BDEF: Defines a determination on save.

``` abap
extension using interface DEMO_RAP_INT_DET_VAL
 implementation in class bp_demo_rap_ext_det_val unique;

extend behavior for RootInterface
{
  determination setStatus on save { create; }
}
```

This determination is implemented in the extension ABP. It sets the field `char_field` automatically to status *A* whenever a new entity instance is created.

``` abap
METHOD setStatus. 
  MODIFY ENTITIES OF DEMO_RAP_INT_DET_VAL IN LOCAL MODE 
     ENTITY RootInterface 
       UPDATE 
       FIELDS ( char_field ) WITH 
       VALUE #( FOR key IN keys ( %tky   = key-%tky 
                                  char_field = status-status_a ) ) 
       REPORTED DATA(lt_reported). 
  reported = CORRESPONDING #( DEEP lt_reported ). 
ENDMETHOD.
```

### Executable Example

An executable example for a BDEF extension adding a new determination is provided in topic [RAP BDL - extend determine action](abenbdl_det_action_ext_abexa.md).

## Variant 2

`... validation ...`

### Description

- Adds a [RAP validation](../../abap-glossary/abenrap_validation_glosry.md) to the entity behavior body of an existing RAP BO entity via a BDEF extension.

- As a prerequisite, the extended BDEF must explicitly allow the particular kind of validation (see the topic about [RAP - Extensibility Enabling for Base BOs](abenbdl_extensibility_enabling_m_u.md)).

- Syntax: exactly the same as for RAP BOs, see topic about [validations](abenbdl_validations.md).

- All fields (extension fields and original fields) can be used as trigger.

- Implementation in the extension ABAP behavior pool must obey the rules for [extension ABPs](abenbdl_in_class_unique_ext.md).

- **Limitation:** Currently not supported for BDEF extensions to unmanaged RAP BOs.

### Hint

The execution order of determinations and validations is arbitrary, also between original and extension components.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The BDEF extension `DEMO_RAP_EXT_VALIDATION` extends the RAP behavior definition `DEMO_RAP_BASE_DET_VAL`. It adds a validation on save `Limit`, which is triggered when field `dec_field` is updated.

Original BDEF: explicitly allows validation on save in the BDEF extension header:

``` abap
managed implementation in class bp_demo_rap_base_det_val unique;
strict ( 2 );
extensible
{ with determinations on modify;
  with determinations on save;
  with validations on save; }

define behavior for DEMO_RAP_BASE_DET_VAL
persistent table demo_dbtab_root
lock master
authorization master ( none )
extensible
{
  create;
  update;
  delete;
  field ( readonly : update ) key_field;
}
```

Extension BDEF: Defines a validation on save.

``` abap
extension using interface DEMO_RAP_INT_DET_VAL
implementation in class bp_demo_rap_ext_validation unique;

extend behavior for RootInterface
{
  validation Limit on save { field dec_field; }
}
```

This validation is implemented in the extension ABP. It checks that the value inserted into field `dec_field` does not exceed 500. If it does, the validation fails and an error message is returned.

``` abap
METHOD Limit. 
*  The value of field dec_field must not be > 500. 
  READ ENTITIES OF DEMO_RAP_INT_DET_VAL IN LOCAL MODE 
    ENTITY RootInterface 
    FIELDS ( dec_field ) 
    WITH CORRESPONDING #( keys ) 
    RESULT DATA(result) 
    FAILED DATA(failed1). 
 
  LOOP AT result INTO DATA(lv_limit). 
    APPEND VALUE #(  %tky        = lv_limit-%tky 
                       %state_area = 'VALIDATE_LIMIT' ) 
                       TO reported-rootinterface. 
    IF lv_limit-dec_field > 500. 
 
      APPEND VALUE #( %tky = lv_limit-%tky ) TO failed-rootinterface. 
      APPEND VALUE #( %tky                 = lv_limit-%tky 
                      %state_area          = 'VALIDATE_LIMIT' 
                      %msg                 = new_message_with_text( 
                      severity = if_abap_behv_message=>severity-error 
                      text = 'validation failed' ) 
                      %element-dec_field     = if_abap_behv=>mk-on ) 
                      TO reported-rootinterface. 
    ENDIF. 
  ENDLOOP. 
ENDMETHOD.
```

## Variant 3

`... event ...`

### Description

- Adds a [RAP business event](../../abap-glossary/abenrap_entity_event_glosry.md) to the entity behavior body of an existing RAP BO entity via a BDEF extension.

- RAP business events can only be defined in the root node of a RAP business object. As a consequence, they can only be defined in a BDEF extension to the root node.

- Syntax: exactly the same as for RAP BOs, see the topic about [RAP - `event`](abenbdl_event.md).

- An extension RAP business event must be raised in the extension ABAP behavior pool of the RAP BO in question with the [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md) statement [`RAISE ENTITY EVENT`](../abap-for-rap-business-objects/abapraise_entity_event.md). The rules for [extension ABPs](abenbdl_in_class_unique_ext.md) must be obeyed.

## More Information

The development guide for the ABAP RESTful Application Programming Model provides an example for a RAP business event that is added by means of a BDEF extension. See *Creating RAP Business Events*.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The BDEF extension `DEMO_RAP_EVENT_EXT` extends the RAP behavior definition `DEMO_RAP_EXTENSIBLE`. It adds the RAP business event `MyEvent` to the [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md). It adds a [RAP additional save](../../abap-glossary/abenrap_add_save_glosry.md), so the event can be raised in the extension ABP in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`save_modified`](../abap-for-rap-business-objects/abaprap_saver_meth_save_modified.md).

``` abap
extension
implementation in class bp_demo_rap_event_ext unique;

extend behavior for DEMO_RAP_EXTENSIBLE
with additional save
{
  event MyEvent;
}
```

## Variant 4

`... managed event ...`

### Description

- Adds a [RAP derived event](../../abap-glossary/abenrap_derived_event_glosry.md) to the entity behavior body of an existing RAP BO entity via a BDEF extension.

- RAP derived events can only be defined in the root node of a RAP business object. As a consequence, they can only be defined in a BDEF extension to the root node.

- Syntax: exactly the same as for RAP BOs, see the topic [RAP - `managed event`](abenbdl_managed_event.md).

- An implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is not required. Derived events are raised automatically when the referenced event is raised.

## More Information

The development guide for the ABAP RESTful Application Programming Model provides an example for a RAP derived event that is added by means of a BDEF extension. See *Derived Business Events*.

## Variant 5

`... field characteristics ...`

### Description

- Adds [field attributes](../../abap-glossary/abenrap_field_char_glosry.md) to extension fields.

- Field attributes can be added only for extension fields. Extension fields are fields which are not part of the original BO, but are added via [RAP data model extension](../../abap-glossary/abenrap_data_model_ext_glosry.md).

- The following field attributes are available in BDEF extensions for extension fields:

  - `readonly`

  - `mandatory`

  - `suppress`

  - `readonly:update`

  - `features:instance`

    **Note:** When implementing [instance feature control](../../abap-glossary/abenrap_ins_feature_control_glosry.md) for fields, the rules for [extension ABPs](abenbdl_in_class_unique_ext.md) apply.

- These field attributes work as described in the topic [RAP - `FieldCharacteristics`](abenbdl_field_char.md).

  **Note:** [Internal field numbering](abenbdl_field_numbering.md) is not available in BDEF extensions. **Note:** The field characteristic `mandatory:create` is not available in BDEF extensions.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The BDEF extension `DEMO_EXTENSION_RAP_BO` extends the RAP behavior definition `DEMO_RAP_FIELD_EXT`. It behavior-enables multiple extension fields.

``` abap
extension using interface DEMO_RAP_FIELD_EXT_INT
 implementation in class bp_demo_extension_rap_bo unique;

extend behavior for Root
{

//  field ( readonly ) DataFieldExt;
  field ( mandatory ) IntFieldExt;
  field ( suppress ) CharFieldExt;
  field ( features : instance ) NumFieldExt;

  field ( readonly : update ) Int1FieldExt;
}
```

### Executable Example

The example above is described in detail in the topic [RAP - Field Extension](abenbdl_field_ext_abexa.md).

## Variant 6

`... action ...`

### Description

- Adds a [RAP action](../../abap-glossary/abenrap_action_glosry.md) to the entity behavior body of an existing RAP BO entity.

- Syntax: exactly the same as for RAP BOs, see the topic [RAP - `action`](abenbdl_action.md).

  **Note:** The following additional rule applies: Each extension action must define an authorization control at action level that replaces the authorization control specified in the [authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md) of the original RAP BO. That means that one of the following additions must be specified for each extension action: [`authorization:none`](abenbdl_actions_auth.md) [`authorization:update`](abenbdl_actions_auth_update.md) [`authorization:global`](abenbdl_actions_auth_global.md) [`authorization:instance`](abenbdl_actions_auth_instance.md) [`authorization:instance, authorization:global`](abenbdl_actions_auth_instance.md) [`authorization:global, authorization:instance`](abenbdl_actions_auth_instance.md) For details, see the topic [RAP - Authorization](abenbdl_authorization.md). **Note:** The optional addition [`default`](abenbdl_action_default_factory.md) to define a factory action as default factory action is not available in BDEF extensions.

- Implementation in the extension ABAP behavior pool must obey the rules for [extension ABPs](abenbdl_in_class_unique_ext.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The BDEF extension `DEMO_RAP_BEH_EXT_CH` extends the RAP behavior definition `DEMO_RAP_BEH_EXT`. It adds action `setValue` to the behavior definition body.

``` abap
extension using interface DEMO_RAP_BEH_EXT_INT
implementation in class bp_demo_rap_beh_ext_ch unique;

extend behavior for RootInterface
{

  association _child { create; }

  action ( features : global, authorization : global ) setValue
    result [1] $self;
}

define behavior for DEMO_RAP_BEH_EXT_CHILD alias ChildInterface
using DEMO_RAP_BEH_EXT_INT_CH
persistent table demo_dbtab_fi_ch
( lock, authorization ) dependent
{
  update;
  delete;
  field ( readonly ) key_field;
  field ( readonly ) key_field_child;
  association _parent;
  determination myDet on modify { field int_field3; }
  action ( authorization : global ) ActionExt;
}
```

### Executable Example

The example above is described in detail in the topic [RAP - Behavior Extension](abenbdl__behavior_ext_abexa.md).

## Variant 7

`... function ...`

### Description

- Adds a [RAP function](../../abap-glossary/abenrap_function_glosry.md) to the entity behavior body of an existing RAP BO entity.

- Syntax: exactly the same as for RAP BOs, see the topic [RAP - `function`](abenbdl_function.md).

- Implementation in the extension ABAP behavior pool must obey the rules for [extension ABPs](abenbdl_in_class_unique_ext.md).

## Variant 8

`... determine action ...`

### Description

- Adds a [RAP BO determine action](../../abap-glossary/abenrap_bo_det_action_glosry.md) to the entity behavior body of an existing RAP BO entity.

- Syntax exactly the same as for RAP BOs, see the topic [RAP - `determine action`](abenbdl_determine_action.md).

- Only [determinations](../../abap-glossary/abenrap_determination_glosry.md) and [validations](../../abap-glossary/abenrap_validation_glosry.md) from the same BDEF extension can be assigned. Determinations and validations from the original BDEF must not be assigned.

- **Limitation:** Currently not supported for BDEF extensions to unmanaged RAP BOs.

## Variant 9

`... association ...`

### Description

- Behavior-enables an association.

- The syntax is exactly the same as for RAP BOs, see the topic [RAP - Operations for Associations](abenbdl_association.md).

- **Limitation:** Currently, only intra-BO associations are fully supported in extensions. Defining cross-BO associations in extension BDEFs is not generally supported, except for the following scenarios:

  - Custom extensions between two released SAP BOs: source-resolved.

  - Custom BO to released SAP BO: source-resolved or target-resolved via reverse association.

  - Released SAP BO to custom BO: source-resolved.

- It is not possible to define a draft-enabled target-resolved association in an extension of a released SAP BO (including the required reverse association in the target BO). This modeling results in an error on the service layer.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The BDEF extension `DEMO_RAP_EXTENSION_1` extends the RAP behavior definition `DEMO_RAP_EXTENSIBLE_ROOT`. The first section of this extension extends an existing node by behavior-enabling the association `_Children4Ext`. The association target is an extension node.

``` abap
extension using interface demo_rap_ext_using_interface;
foreign entity demo_rap_factory_ACTION;
extend behavior for GrandChildInterface
{
  association _Children4Ext { create; with draft; }
}

define behavior for DEMO_RAP_EXTENSIBLE_EXT alias ExtNode
  using DEMO_RAP_EXT_USING_INT_EXT
persistent table demo_ggchl_ex_ba
draft table demo_ggrch_ext
etag master Timestamp
( lock, authorization ) dependent

{
  update;
  delete;
  field ( readonly )
  KeyField, KeyFieldchild, Keyfieldgrchld;

  field ( readonly : update ) Keyfieldggchld;
  field ( readonly ) Timestamp;

  association _parent { with draft; }
  association _Sibling4 { with draft; }
  ancestor association _GrandParent2 { with draft; }
  ancestor association _GreatGrandParent1 { with draft; }

  mapping for demo_ggchl_ex_ba
  {
    Keyfield = key_field;
    Keyfieldchild = key_field_child;
    Keyfieldgrchld = key_field_grchld;
    Keyfieldggchld = key_field_ggchld;
    Datafield = data_field;
    Charfield = char_field;
    Timestamp = timestamp;
  }
}
```

### Executable Example

The example above is described in detail in the topic [RAP - Node Extension](abenbdl_assoc_ext_abexa.md).

## Variant 10

`... define pure key ...`

### Description

- Adds a [BDEF pure key](../../abap-glossary/abenrap_pure_key_glosry.md) to the entity behavior body of an existing RAP BO entity. This is allowed only in BDEF extensions declared as [BDEF friend](../../abap-glossary/abenrap_bdef_friend_glosry.md).

- The syntax is exactly the same as for RAP BOs, see the topic [RAP - BDEF Alternative Key](abenbdl_define_key.md).

### Hint

[BDEF secondary keys](../../abap-glossary/abenrap_secondary_key_glosry.md) are not allowed in BDEF extensions.

## Variant 11

`... mapping for ...`

### Description

- Adds a [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) to the entity behavior body of an existing RAP BO entity. This type mapping can only contain extension fields. It must not contain any fields from the extended BDEF.

- The syntax is exactly the same as for RAP BOs, see the topic [RAP - `TypeMapping`](abenbdl_type_mapping.md).

### Hint

In a BDEF extension, it is possible to add a new RAP type mapping or to extend an existing type mapping from the original behavior definition using the syntax [`extend type mapping`](abenbdl_type_mapping_ext.md). If the partner type is identical, both variants are equivalent. There is no difference between `mapping for PartnerType ...` and `extend mapping for PartnerType ...`
