---
title: "RAP - foreign entity"
source_file: abenbdl_foreign.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - BehaviorDefinitionHeader"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - foreign entity

## Syntax

``` abap
... 
foreign entity ForeignEntityName [alias AliasName]; 
 ...  
```

## Description

Defines a [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md) which is not part of the [CDS composition tree](../../abap-glossary/abencds_composition_tree_glosry.md) of the current RAP BO as part of the [response structures](../abap-for-rap-business-objects/abapeml_response.md), thus enabling message mapping for other BOs. An alias name `AliasName` can be specified. The length of this alias name can have a maximum of 30 characters.

A [foreign entity](../../abap-glossary/abenrap_foreign_entity_glosry.md) is defined in the [RAP behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md) and is therefore included in the response structures of all RAP BO nodes of the current RAP BO. A foreign entity includes the specified entity `ForeignEntityName` in the response structures, but not a complete foreign RAP BO. It is possible to specify multiple foreign entities, if required.

## Use

Here is an example for a use case: A [RAP determination](../../abap-glossary/abenrap_determination_glosry.md) may trigger an operation of another business object that then returns messages. To receive and adapt the messages from a foreign business object, the foreign business object can be registered in the current BO as a foreign entity. The messages are mapped during the [save sequence](../../abap-glossary/abenrap_save_seq_glosry.md).

A reimplementation of the [RAP saver method](../../abap-glossary/abenabp_saver_method_glosry.md) [`map_messages`](../abap-for-rap-business-objects/abensaver_map_messages.md) in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is optional.

## Availability

RAP foreign entities can be defined in the following types of behavior definitions:

- [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- [projection BDEF](../../abap-glossary/abenrap_projection_bo_glosry.md)

- [interface BDEF](../../abap-glossary/abenrap_bo_interface_glosry.md)

## Hint

The [association target](../../abap-glossary/abenassociation_target_glosry.md) of a [cross-BO association](../../abap-glossary/abencds_cross_bo_assoc_glosry.md) in a BDEF is automatically included in the response types as a foreign entity. This default behavior can be disabled using the syntax addition [`without response`](abenbdl_association.md).

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section [*Mapping Messages Between Business Objects*](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/6a0e78d79b0a4f7e8d3298dbd99c8d09?version=sap_cross_product_abap).

- [`map_messages`, RAP Saver Method](../abap-for-rap-business-objects/abensaver_map_messages.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF based on the CDS root view entity `DEMO_RAP_FOREIGN_ENTITY`. It establishes a connection to the foreign entity `DEMO_SALES_CDS_SO_1`.

**Note:** This example is intentionally kept short and simple and serves demonstration purposes only. The [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) are not implemented here.

``` abap
managed implementation in class bp_demo_rap_foreign_entity unique;
strict ( 2 );
//enables MAP_MESSAGES:
foreign entity DEMO_SALES_CDS_SO_1;

define behavior for DEMO_RAP_FOREIGN_ENTITY alias RootEntity
persistent table demo_dbtab_root
lock master
authorization master ( none )
{
  create;
  update;
  delete;

  field ( readonly : update ) key_field;
}
```

The class `CL_DEMO_RAP_FOREIGN_ENTITY` accesses the BDEF and creates three new entity instances.

Code snippet:

``` abap
DELETE FROM demo_dbtab_root. 
    MODIFY ENTITIES OF DEMO_RAP_FOREIGN_ENTITY 
         ENTITY RootEntity 
         CREATE FIELDS ( key_field ) WITH VALUE #( 
              ( %cid = '1' key_field = 1  ) 
              ( %cid = '2' key_field = 2  ) 
              ( %cid = '3' key_field = 3  ) ) 
                MAPPED FINAL(mapped) 
               FAILED FINAL(failed) 
               REPORTED FINAL(reported). 
    COMMIT ENTITIES.
```

Result: The entities of the referenced foreign business object are added to the `reported` structure. ![figure](images_abdoc_foreign_entity.png)

## Executable Example

[Example for RAP Saver Method `map_messages`](../abap-for-rap-business-objects/abenabp_map_messages_abexa.md)
