---
title: "RAP - ancestor association"
source_file: abenbdl_ancestor_ext.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension > RAP - Extension Entity Behavior Definition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - ancestor association

## Syntax

``` abap
...  ancestor association _Assoc[;] 
             [abbreviation _newName] 
             [without response] 
             [{[with draft;]}]  
```

## Description

Declares an [association](../../abap-glossary/abencds_association_glosry.md) as an [ancestor association](../../abap-glossary/abencds_ancestor_assoc_glosry.md). An ancestor association is an [intra-BO association](../../abap-glossary/abencds_intra_bo_assoc_glosry.md) that has as its [association target](../../abap-glossary/abenassociation_target_glosry.md) a [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md) between the current node and the [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md). The association target must be higher in the hierarchical structure of the RAP composition tree, so it must not be a sibling node. Moreover, it must not be the [CDS parent entity](../../abap-glossary/abenparent_entity_glosry.md) of the current node. The purpose of ancestor associations is to make it possible to implicitly derive the path to a RAP BO's [authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md), [lock master entity](../../abap-glossary/abenrap_lock_ma_ent_glosry.md), [ETag master entity](../../abap-glossary/abenrap_etag_ma_ent_glosry.md), and [RAP change documents master entity](../../abap-glossary/abenrap_change_doc_master_glosry.md) so the respective entities need not be defined explicitly.

The following rules apply to ancestor associations:

- Each association that points to an entity between the current node and the root node should be marked as `ancestor`, except for the direct parent entity. That means that an entity can have multiple ancestor associations.

  The following associations must not be declared as `ancestor`:

  - Sibling entities on the same hierarchy level must not be marked as `ancestor`.

  - The direct parent entity must not be marked as `ancestor`, since it can be clearly identified as ancestor by its CDS definition.

  - If there are multiple associations with the same association target, at most one of them can be declared as `ancestor`.

    All other associations should be marked as `ancestor`.

- An ancestor association must have a [cardinality](../../abap-glossary/abencardinality_glosry.md) of 1.

- The key fields of all ancestor associations must be marked as `readonly`.

The purpose of ancestor associations is to guarantee the stability of extensions even if the extended RAP BO is modified. Via ancestor associations, the path to the [RAP authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md), [RAP lock master entity](../../abap-glossary/abenrap_lock_ma_ent_glosry.md), [RAP ETag master entity](../../abap-glossary/abenrap_etag_ma_ent_glosry.md), and [RAP change documents master entity](../../abap-glossary/abenrap_change_doc_master_glosry.md) can be derived and need not be specified explicitly. Therefore, the syntax `ancestor association` makes the direct pointing to a authorization master, lock master, ETag master, and change documents master obsolete:

- Syntax to specify a [RAP lock dependent entity](../../abap-glossary/abenrap_lock_dep_ent_glosry.md): `lock dependent` instead of `lock dependent by _Assoc`

- Syntax to specify a [RAP authorization dependent entity](../../abap-glossary/abenrap_auth_dep_ent_glosry.md): `authorization dependent` instead of `authorization dependent by _Assoc`

- Syntax to specify a [RAP ETag dependent entity](../../abap-glossary/abenrap_etag_dep_ent_glosry.md): `etag dependent` instead of `etag dependent by _Assoc`

- Syntax to specify a RAP change documents master entity: `changedocuments dependent` instead of `changedocuments dependent by _Assoc`

A short syntax form is available: `( lock, authorization, etag, changedocuments ) dependent`. Each of the components `lock`, `authorization`, `etag`, and `changedocuments` is optional but at least one of them must be specified within the brackets.

When creating new entity instances, the corresponding foreign keys of the association targets of the ancestor associations are derived implicitly, so that these foreign keys do not need to be provided, calculated, or read from the database.

**Additions:**

- `abbreviation _newName`: Defines an alternative name for an association. The abbreviation `_newName` can have a maximum of 16 characters. Associations are in the namespace of their root entity and can have up to 30 characters. This is under certain circumstances too long to be processed in [ABAP RAP](../../abap-glossary/abenabap_rap_glosry.md). Whenever a shorter name is required, you are prompted to assign an abbreviation for the association with no more than 16 characters.

- `without response` The optional addition `without response` is for cross-BO associations that have an association target from another BO. With such a cross-BO association, the association target entity is automatically included in the response types as [foreign entity](abenbdl_foreign.md). In this way, problems with the target entity can become part of the response types during read-by-association or create-by-association operations. `without response` prevents the default behavior of the [foreign entity](../../abap-glossary/abenrap_foreign_entity_glosry.md) being included in the response types.

- `with draft`: [Draft-enables](../../abap-glossary/abenrap_draft_handling_glosry.md) an association. A draft-enabled association retrieves active data if it is followed from an [active instance](../../abap-glossary/abenrap_active_instance_glosry.md) and draft data if it is followed from a [draft instance](../../abap-glossary/abenrap_draft_instance_glosry.md) (for details about RAP draft handling, see [RAP - `with draft`](abenbdl_with_draft.md)).

  If a [BO](../../abap-glossary/abenbusiness_object_glosry.md) is draft-enabled, then all associations should be draft-enabled, so that the associations always lead to the target instance with the same state (draft or active). As soon as you draft-enable a BO by adding `with draft`, all BO-internal associations are automatically draft-enabled. To make this behavior explicit, the behavior prompts you to specify the compositions within a draft BO with `with draft`.

## More Information

Development guide for the ABAP RESTful Application Programming Model, section about [*Node Extensions*](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/05aef486ac5e4b74b87f3bf39be1718a?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The BDEF extension `DEMO_RAP_EXTENSION_1` extends the RAP behavior definition `DEMO_RAP_EXTENSIBLE_ROOT`. It behavior-enables an extension node and defines the associations to its sibling, grandparent, and great-grandparent as ancestor associations. Lock, authorization, and ETag master are not specified explicitly, but derived implicitly via ancestor associations.

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

## Executable Example

The executable example [Node Extension](abenbdl_assoc_ext_abexa.md) explains the example above in detail.
