---
title: "RAP - Locking"
source_file: abenbdl_locking.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorCharacteristics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Locking

## Syntax

``` abap
... lock master [unmanaged] 
  | lock dependent by _Assoc  
```

## Description

Specifies the [RAP locking](../../abap-glossary/abenrap_locking_glosry.md) mechanism for a [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md).. It prevents simultaneous modification access to data on the database by more than one user. This is also known as [pessimistic concurrency control](../../abap-glossary/abenpessimist_conc_control_glosry.md). Whenever a lock is requested for a specific entity instance, its [lock master](../../abap-glossary/abenrap_lock_ma_ent_glosry.md) and all [lock-dependent](../../abap-glossary/abenrap_lock_dep_ent_glosry.md) entity instance are locked for editing by a different user, in other words, as soon as one node receives a locking request, the whole BO instance is locked. Lock master entities are locked on each locking request of one of their lock-dependent entities.

The following rules apply:

- The root node must be declared as `lock master` entity.

- Each child entity must be declared as lock-dependent entity using the syntax `lock dependent by _Assoc`. Locking requests of lock-dependent entity instances are delegated to the lock master entity.

- Each RAP BO entity must be defined as `lock master` or `lock dependent` entity.

- The association `_Assoc` from the lock-dependent entity to the lock master entity must be explicitly defined in the entity behavior definition using the syntax `association _AssocToLockMaster { }`. The association must also be defined in the underlying CDS data model.

In a managed RAP BO, the locking mechanism is handled by the [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md), so that no implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is required. If the optional addition `unmanaged` is used, the lock mechanism must be implemented manually in the method [`FOR LOCK`](../abap-for-rap-business-objects/abaphandler_meth_lock.md) of the behavior pool, just like in the unmanaged scenario. It is then invoked at runtime.

In an unmanaged RAP BO, the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR LOCK`](../abap-for-rap-business-objects/abaphandler_meth_lock.md) must be implemented for lock master entities.

**Setting Locks**

If a lock is defined for a RAP BO entity, the entity instances in question are implicitly locked during the runtime of the following [modify operations](../../abap-glossary/abenrap_modify_operation_glosry.md):

- [`update`](abenbdl_standard_operations.md)

- [`delete`](abenbdl_standard_operations.md)

- [`create by association`](abenbdl_association.md)

- [`action`](abenbdl_action.md)

  **Note:** The optional addition [`lock:none`](abenbdl_lock_none.md) is available for actions. It can be used to prevent the locking mechanism for the entity instance for which an action is executed.

- **Note:** [`create`](abenbdl_standard_operations.md): In a managed RAP BO, the newly created key values (if available) of instances are written into the global lock table during the create operation. This is part of a uniqueness check, which is automatically and implicitly carried out by the RAP framework. In an unmanaged RAP BO, there is no automatic uniqueness check and no key values are written into the global lock table. For further details, see the development guide for the ABAP RESTful Application Programming Model, section [Uniqueness Check](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/cc4064be45ff46d6a6b8828d3aaa9bb9?version=sap_cross_product_abap).

## Availability

- [Managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- [Draft-enabled RAP business object](../../abap-glossary/abendraft_rap_bo_glosry.md)

  If a BO is [draft-enabled](abenbdl_with_draft.md), locking must also be considered. As soon as a draft instance is created for an existing active instance, the active instance is given an [exclusive lock](../../abap-glossary/abenexclusive_lock_glosry.md) and cannot be modified by another user. This exclusive lock remains for a determined time, even if the [ABAP session](../../abap-glossary/abenabap_session_glosry.md) terminates. The duration time of the exclusive lock can be configured. Once the exclusive lock expires after the duration time, the [optimistic lock phase](abenbdl_etag.md) begins. During the optimistic lock phase, a draft can be resumed as long as the active instance does not change, but there is no longer an exclusive lock.

- [Projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md)

  In a [projection business object](../../abap-glossary/abenrap_projection_bo_glosry.md), the RAP locking mechanism that is defined and implemented for the [base BO](../../abap-glossary/abenrap_projected_bo_glosry.md) is automatically reused and does not need to be explicitly defined. For details, see topic [RAP - `EntityBehaviorCharacteristics`, Projection BDEF](abenbdl_character_projection.md).

## Hints

- The [draft action `Resume`](abenbdl_draft_action.md) recreates a lock for an entity instance on the [persistent database table](../../abap-glossary/abenrap_persistent_table_glosry.md) when a draft instance is resumed after the lock has expired.

- The EML statement [`SET LOCKS`](../abap-for-rap-business-objects/abapset_locks.md) can be used to explicitly lock [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md).

- Locks are managed in a global lock table.

- The following syntax short form is available to summarize lock dependent, ETag dependent, and authorization dependent:

  `([lock][, authorization][, etag]) dependent by _assoc` For details, see topic [RAP - `SyntaxShortForm`](abenbdl_short_syntax.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Pessimistic Concurrency Control (Locking)](https://help.sap.com/docs/ABAP_PLATFORM_NEW/fc4c71aa50014fd1b43721701471913d/99d8162b8d7d4a83ae65320d2a03b8ab).
