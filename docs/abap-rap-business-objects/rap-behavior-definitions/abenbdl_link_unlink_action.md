---
title: "RAP - Link / Unlink Action"
source_file: abenbdl_link_unlink_action.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Operations for Associations > RAP - NonstandardOperationsForAssoc"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Link / Unlink Action

## Syntax

``` abap
...{   [internal] 
       {[link action mylinkaction] 
       [unlink action myunlinkaction]} 
       [( 
       [features: {instance |global}] 
       [precheck] 
       [authorization:none] 
       [authorization:update] 
        )]; 
    }  
```

[`internal`](abenbdl_internal.md) · [`features: {instance |global}`](abenbdl_actions_fc.md) · [`precheck`](abenbdl_precheck.md) · [`authorization:none`](abenbdl_actions_auth.md) · [`authorization:update`](abenbdl_actions_auth_update.md)

## Description

- Link Action

  - The link action is an instance-based action which can be defined for a [foreign key association](../../abap-glossary/abenforeign_key_assoc_glosry.md). The link action takes a combination of [association source](../../abap-glossary/abenassociation_source_glosry.md) and [target entity](../../abap-glossary/abenassociation_target_glosry.md) instance as input, and establishes a connection via the [association](../../abap-glossary/abenassociation_glosry.md) between the two entity instances. This operation is realized by updating the [foreign key](../../abap-glossary/abenforeign_key_glosry.md) on the source entity to the value of the supplied target instance.

  - The link action is required when the [foreign key](../../abap-glossary/abenforeign_key_glosry.md) relationship between instances cannot be established by setting the respective [foreign key](../../abap-glossary/abenforeign_key_glosry.md) through create or update operations.

  - The link action can be used in [hierarchy](../../abap-glossary/abenhierarchy_glosry.md) scenarios to change the tree order by updating the [foreign keys](../../abap-glossary/abenforeign_key_glosry.md) of entity instances.

- Unlink Action

  - Use the unlink action to break connections in data models where [foreign-key](../../abap-glossary/abenforeign_key_glosry.md) relationships were previously established.

  - The unlink action dissolves the [foreign-key](../../abap-glossary/abenforeign_key_glosry.md) relationship between source and target instances by initializing the [foreign key field(s)](../../abap-glossary/abenforeign_key_field_glosry.md) on the particular entity. It is defined for the [association](../../abap-glossary/abenassociation_glosry.md) of the entity that stores the [foreign key](../../abap-glossary/abenforeign_key_glosry.md).

  - The unlink action can be used in the same scenarios as described for the link action.

**RAP BDL Operation Additions**

The following [RAP BDL operation additions](abenbdl_operations_additions.md) are possible:

- [`internal`](abenbdl_internal.md): The create-by-association operation can only be accessed internally.

- [`features:instance`](abenbdl_actions_fc.md): Enables dynamic feature control for the association in question.

- [`features:global`](abenbdl_actions_fc.md): Enables global feature control for the association in question.

- [`precheck`](abenbdl_precheck.md): Prevents illegal changes from reaching the application buffer by prechecking [modify operations](../../abap-glossary/abenrap_modify_operation_glosry.md).

- [`authorization:none`](abenbdl_actions_auth.md): Excludes the association in question from [authorization checks](abenbdl_authorization.md).

- [`authorization:update`](abenbdl_actions_auth_update.md): Delegates the [authorization control](abenbdl_authorization.md) to the authorization check that is implemented for the update operation.

## Availability

- Managed RAP BO: In a [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md), the inverse function does not require an [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md), since it is completely handled by the managed RAP BO provider, unless the association is unmanaged.

- Unmanaged RAP BO: In an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), the inverse function must be implemented in the ABAP behavior pool in the [RAP handler method](../abap-for-rap-business-objects/abapmethods_for_rap_behv.md) [`FOR MODIFY`](../abap-for-rap-business-objects/abaphandler_meth_modify.md), unless the association is managed.

- Projection BO and RAP BO Interface: In a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md) and in a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), the inverse function can be reused from the [baseBDEF](../../abap-glossary/abenrap_base_bdef_glosry.md). This can be done using the keyword `use` for the association, listing the respective operations again. For further details, see topic [RAP BDL - use, projection BDEF](abenbdl_use_projection.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Link Action](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/579f8c1b7e9043999383e88aa6e9302b?version=sap_cross_product_abap) and [Unlink Action](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/b53c24b9372d4c2a8f5a17659c33fc69?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example is based on two separate BOs, one serving as the source and the other as the target entity.

The association `_CROSS_ASSOC` is defined as a target resolved association, where the field `TargetKey` is used as the foreign key. See the CDS view `DEMO_RAP_LINKACTION_SRC` of the source BO:

``` abap
@AbapCatalog.viewEnhancementCategory: [#NONE]
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS View Link Action Source'
@Metadata.ignorePropagatedAnnotations: true
@ObjectModel.usageType:{
  serviceQuality: #X,
  sizeCategory: #S,
  dataClass: #MIXED
}
define root view entity DEMO_RAP_LINKACTION_SRC
  as select from demo_dbtab_src

  association [0..1] to DEMO_RAP_LINKACTION_TGT as _CROSS_ASSOC 
  on $projection.TargetKey = _CROSS_ASSOC.TargetKey

{
  key source_key as SourceKey,
      target_key as TargetKey,
      char_field as CharField,

      _CROSS_ASSOC
}
```

In the BDEF of the source BO, the association `_CROSS_ASSOC` is used, with the additions `create`, `link action` and `unlink action`.

``` abap
managed implementation in class bp_demo_rap_linkaction_src unique;
strict ( 2 );
with cross associations;

define behavior for DEMO_RAP_LINKACTION_SRC
persistent table demo_dbtab_src
lock master
authorization master ( instance )

{
  create ( authorization : global );
  update;
  delete;
  field ( readonly ) SourceKey;
  field ( readonly : update ) TargetKey;

  association _CROSS_ASSOC
  {
    create;
    link action link_action;
    unlink action unlink_action;
  }

  mapping for demo_dbtab_src
    {
      SourceKey = source_key;
      TargetKey = target_key;
      CharField = char_field;
    }

}
```abap
The database table of the source BO is initially filled with one 
instance, where `TargetKey = 100`\.
```

\|SOURCE_KEY\|TARGET_KEY\|CHAR_FIELD \|

\|1\|100\|source\|

The database table of the target BO is filled with two instances, where `TargetKey = 100` and `101` respectively.

\|TARGET_KEY\|CHAR_FIELD \|

\|100\|target \| \|101\|target2\|

When the `link action` is executed with `SourceKey = '1'` and `%param-TargetKey = '101'`, as shown below, the `TargetKey` field in the source entity is overwritten with the new value 101, thus linking the source instance with the target instance 101.

\|SOURCE_KEY\|TARGET_KEY\|CHAR_FIELD \|

\|1\|101\|source\|

See class `CL_DEMO_RAP_LINKACTION` for the following code snippet:

``` abap
MODIFY ENTITIES OF DEMO_RAP_LINKACTION_SRC 
     ENTITY DEMO_RAP_LINKACTION_SRC 
      EXECUTE link_action FROM VALUE #( ( 
                                           SourceKey = '1' 
                                        %param-TargetKey = '101' 
                                          ) ). 
 
    COMMIT ENTITIES.
```

When the `unlink action` is executed with the parameter `SourceKey = '1'`, the `TargetKey` field in the source entity is emptied, thus breaking the link between the source and target instance.

``` abap
    MODIFY ENTITIES OF DEMO_RAP_LINKACTION_SRC 
     ENTITY DEMO_RAP_LINKACTION_SRC 
      EXECUTE unlink_action FROM VALUE #( ( 
                                           SourceKey = '1' 
                                          ) ). 
 
    COMMIT ENTITIES.
```

\|SOURCE_KEY\|TARGET_KEY\|CHAR_FIELD \|

\|1\| \|source\|
