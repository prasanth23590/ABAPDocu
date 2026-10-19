---
title: "RAP - SavingOptions"
source_file: abenbdl_saving.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorCharacteristics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - SavingOptions

## Syntax

``` abap
... {with additional save [and cleanup][with full data]} 
  | {with unmanaged save [and cleanup][with full data]} ...  
```

### Variant

[1. `... with additional save [and cleanup][with full data]`](abenbdl_saving.md#variant-1)

[2. `... with unmanaged save [and cleanup][with full data]`](abenbdl_saving.md#variant-2)

### Addition

[1. `... and cleanup`](abenbdl_saving.md#addition-1)

[2. `... with full data`](abenbdl_saving.md#addition-2)

## Overview

### Description

Defines a [RAP unmanaged save](../../abap-glossary/abenrap_unman_save_glosry.md) or a [RAP additional save](../../abap-glossary/abenrap_add_save_glosry.md):

- A RAP unmanaged save is defined using the addition `with unmanaged save`. It allows developers to implement a save logic that replaces the default save sequence in a managed RAP BO.

- A RAP additional save is defined using the addition `with additional save`. It allows developers to implement additional steps for the save logic of a managed RAP BO, thereby enhancing the standard save sequence.

By default, the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md) performs a managed save. With an [additional save](../../abap-glossary/abenrap_add_save_glosry.md), steps can be added to the managed save. An [unmanaged save](../../abap-glossary/abenrap_unman_save_glosry.md) prevents the default and allows the implementation of a dedicated saving strategy. Both additions require a reimplementation of the [`save_modified`](../abap-for-rap-business-objects/abaprap_saver_meth_save_modified.md) method of the [RAP saver class](../abap-for-rap-business-objects/abenabp_saver_class.md) in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md).

There are two options for notation:

- In the [BDEF header](../../abap-glossary/abencds_bdef_header_glosry.md), directly after the keyword `managed`. In this case, the additional save or unmanaged save is enabled for all entities of the business object.

  Example: `managed with additional save implementation in class ...;`

- As an [entity behavior property](../../abap-glossary/abencds_entity_properties_glosry.md). In this case, it can be specified for each entity individually.

  Example: `define behavior for EntityName with unmanaged save`

## Availability

- Available in [managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md) only. In unmanaged business objects, the saving strategy is user-defined by default.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF that defines an additional save in the BDEF header.

``` abap
managed with additional save with full data
implementation in class bp_demo_managed_additional_sav unique;
strict(2);

define behavior for DEMO_MANAGED_ADDITIONAL_SAVE
persistent table DEMO_TAB_ROOT_3
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field(readonly:update) key_field;
}
```

In the ABAP behavior pool, the method `save_modified` tracks data changes in a log table. The complete implementation can be seen in the `BP_DEMO_MANAGED_ADDITIONAL_SAVCCIMP`.

The ABAP class `CL_DEMO_RAP_MANAGED_ADD_SAVE` uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object. It performs a create, update, and delete operations. The changes are saved and tracked in internal log tables.

### Executable Example

- The example shown above is displayed and explained in detail in the topic [ABAP EML - `TYPE REQUEST FOR` in a Managed RAP BO with Additional Save](../abap-for-rap-business-objects/abenrap_additional_save_abexa.md).

- An example for a managed RAP BO with unmanaged save is shown in the topic [ABAP EML - `TYPE REQUEST FOR` in a Managed RAP BO with Unmanaged Save](../abap-for-rap-business-objects/abenrap_managed_unm_save_abexa.md).

## Variant 1

`... with additional save`

### Description

Allows additional functionality to be called during the standard save sequence, for example, change documents and an application log.

An implementation in the local saver class is required.

## More Information

Development guide for the ABAP RESTful Application Programming Model, section about [Additional Save](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/ca7097c8ea404b11b1f1334fd54cdd15?version=sap_cross_product_abap).

## Variant 2

`... with unmanaged save`

### Description

Prevents the BO's managed runtime from saving changes and allows the implementation of a dedicated saving strategy instead. In case of an unmanaged save, a [persistent table](abenbdl_persistent_table.md) must not be specified.

An implementation in the local saver class is required.

### Executable Example

An example for a managed RAP BO with unmanaged save is shown in the topic [ABAP EML - `TYPE REQUEST FOR` in a Managed RAP BO with Unmanaged Save](../abap-for-rap-business-objects/abenrap_managed_unm_save_abexa.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, section about [Unmanaged Save](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/2c2bec28fff6475f922f9f876491826d?version=sap_cross_product_abap).

## Addition 1

`... and cleanup`

### Description

If specified, the RAP saver method [`cleanup`](../abap-for-rap-business-objects/abensaver_method_cleanup.md) must be redefined.

## Addition 2

`... with full data`

### Description

When one of the additions `with additional save` or `with unmanaged save` is specified, by default, only the values of the key fields and changed fields are handed over to the [`save_modified`](../abap-for-rap-business-objects/abaprap_saver_meth_save_modified.md) method of the [RAP saver class](../abap-for-rap-business-objects/abenabp_saver_class.md). The addition `with full data` can be used to hand over the full instance data to the `save_modified` method. In other words, the values of all fields that are part of the [component group](../../abap-glossary/abencomponent_group_glosry.md) [`%data`](../abap-for-rap-business-objects/abapderived_types_data.md) are filled with values when the `save_modified` method is called.

### Hints

- The fields of the [component group](../../abap-glossary/abencomponent_group_glosry.md) [`%control`](../abap-for-rap-business-objects/abapderived_types_control.md) are not affected by this. Still, only the changed fields of `%control` are flagged.

- In scenarios where all fields, not only changed fields, are required for further processing, the addition `with full data` can be used. This spares the RAP BO consumer an additional `READ` operation.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF that defines an additional save `with full data` in the BDEF header.

``` abap
managed with additional save with full data
implementation in class bp_demo_managed_additional_sav unique;
strict(2);

define behavior for DEMO_MANAGED_ADDITIONAL_SAVE
persistent table DEMO_TAB_ROOT_3
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field(readonly:update) key_field;
}
```

In the ABAP behavior pool, the method `save_modified` tracks data changes in a log table. The complete implementation can be seen in the `BP_DEMO_MANAGED_ADDITIONAL_SAVCCIMP`.

The ABAP class `CL_DEMO_RAP_MANAGED_FULL_DATA` uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object. First, it creates two entity instances, filling values into all entity fields. Then, it updates both entity instances, changing the values of two fields, namely `field1` and `field2`. Without the addition `with full data`, only the values of the changed fields are respected in the `save_modified` method. The fields that are not changed have their initial value. But since this example uses `with full data`, even the values of fields `field3` and `field4` are respected.

Code Snippet: Note that `field3` and `field4` are not updated.

``` abap
MODIFY ENTITY demo_managed_additional_save 
     UPDATE FROM VALUE #( 
        ( key_field = 1 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'update_1' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'update_2' 
          %control-field2 = if_abap_behv=>mk-on 
 ) 
        ( key_field = 2 
          %control-key_field = if_abap_behv=>mk-on 
          field1 = 'update_3' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'update_4' 
          %control-field2 = if_abap_behv=>mk-on 
 ) 
        ). 
 
    COMMIT ENTITIES.
```

Variable `lt_update` in the ABAP behavior pool when the addition `with full data` is specified: all fields are listed with their values, even the fields which are not included in the update operation. ![figure](images_with_full_data.png)

Variable `lt_update` in the ABAP behavior pool when the addition `with full data` is **not** specified: fields that are not updated are filled with initial values. ![figure](images_without_full_data.png)

**Note:** In this example, fields that are not updated are filled with initial values. Note that this is not always the case. Fields which are not updated do not contain consistent values and the values must therefore not be evaluated.
