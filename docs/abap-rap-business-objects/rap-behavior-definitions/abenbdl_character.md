---
title: "RAP - EntityBehaviorCharacteristics"
source_file: abenbdl_character.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - EntityBehaviorCharacteristics

## Syntax

``` abap
...  [persistent table] TableName 
     [draft table DraftTableName] 
     [SavingOptions] 
    {[etag  ] 
     [Locking] 
     [Authorization]} 
    | SyntaxShortForm 
     [extensible  ] 
     [early numbering  ] 
     [late numbering  ] ...  
```

[`persistent table`](abenbdl_persistent_table.md) · [`draft table`](abenbdl_draft_table.md) · [`SavingOptions`](abenbdl_saving.md) · [`etag `](abenbdl_etag.md) · [`Locking`](abenbdl_locking.md) · [`Authorization`](abenbdl_authorization.md) · [`SyntaxShortForm`](abenbdl_short_syntax.md) · [`extensible `](abenbdl_extensible.md) · [`early numbering `](abenbdl_early_numb.md) · [`late numbering `](abenbdl_late_numbering.md)

## Description

This topic provides an overview of all available [entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md). Entity behavior characteristics define additional properties for a [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md). Some are mandatory and some are optional. Different characteristics are available for managed, unmanaged, and draft-enabled scenarios. In some cases, the order of notation is important. For example, the `total etag` must always be specified directly after the `lock master`. These details are described in the respective topics.

- [`persistent table`](abenbdl_persistent_table.md)

  Specifies the [RAP persistent table](../../abap-glossary/abenrap_persistent_table_glosry.md) `TableName` for storing the CDS entity's data changes that result from transactional behavior. Only available for [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md).

- [`draft table`](abenbdl_draft_table.md)

  Specifies the [RAP draft table](../../abap-glossary/abendraft_table_glosry.md) `DraftTableName` for storing data changes of [draft instances](../../abap-glossary/abenrap_draft_instance_glosry.md). This addition is only available for draft-enabled scenarios using the addition [`with draft`](abenbdl_with_draft.md) or [`with collaborative draft`](abenbdl_with_coll_draft.md).

- [`SavingOptions`](abenbdl_saving.md)

  The default [save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) can either be enhanced or switched off and overwritten with a user-defined saving strategy. Can be defined in the [BDEF header](../../abap-glossary/abencds_bdef_header_glosry.md) and then applies to all entities of the business object. It is also possible to define saving options as an entity behavior characteristic. If specified, an implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is required. Only available for [managed implementation scenarios](../../abap-glossary/abenmanaged_rap_bo_glosry.md).

- [`etag`](abenbdl_etag.md)

  [Optimistic concurrency control](../../abap-glossary/abenoptimistic_conc_control_glosry.md).

- [`Locking`](abenbdl_locking.md)

  [Pessimistic concurrency control](../../abap-glossary/abenpessimist_conc_control_glosry.md).

- [`Authorization`](abenbdl_authorization.md)

  Defines which [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md) under which circumstances are allowed to read or change data of a business object.

- [`ShortSyntaxForm`](abenbdl_short_syntax.md): The three statements `lock dependent by _assoc`, `authorization dependent by _assoc`, and `etag dependent by _assoc` can be summarized into one statement: ` (lock, authorization, etag) dependent by _assoc`. For details, see topic [RAP - `SyntaxShortForm`](abenbdl_short_syntax.md).

- [`extensible`](abenbdl_extensible.md)

  [RAP extensibility enablement](../../abap-glossary/abenrap_ext_enablement_glosry.md)

- [`early numbering`](abenbdl_early_numb.md)

  [RAP early numbering](../../abap-glossary/abenrap_early_numbering_glosry.md) means early value assignment for the primary key fields.

- [`late numbering`](abenbdl_late_numbering.md)

  [Late numbering](../../abap-glossary/abenrap_late_numbering_glosry.md) means late value assignment for the primary key fields.

## Hint

Each characteristic can occur only once in a RAP behavior definition.
