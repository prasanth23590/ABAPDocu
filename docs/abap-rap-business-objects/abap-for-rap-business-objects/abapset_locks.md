---
title: "SET LOCKS"
source_file: abapset_locks.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SET LOCKS

## Syntax Forms

**[`SET LOCKS ENTITY`, Short Form](abapset_locks_entity.md)**

``` abap
1. SET LOCKS ENTITY entity FROM inst [response_param].
```

**[`SET LOCKS OF`, Long Form](abapset_locks_of.md)**

``` abap
2. SET LOCKS OF bdef 
   ENTITY entity1 FROM inst1 
  [ENTITY entity2 FROM inst2] 
  [...] 
  [response_param].
```

**[`SET LOCKS lock_tab`, Dynamic Form](abapset_locks_dyn.md)**

``` abap
3. SET LOCKS lock_tab [response_param].
```

[`response_param`](abapeml_response.md) · [`response_param`](abapeml_response.md) · [`response_param`](abapeml_response.md)

## Description

Used to set enqueue locks for [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) to prevent the concurrent modification of instances. The [RAP framework](../../abap-glossary/abenrap_framework_glosry.md) automatically locks instances for subsequent modifications. However, if the [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) requires an exclusive lock so that no other user can modify the same instance in parallel, the statements can be used. The lock remains active until the end of a [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md).

In the BDEF, the [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md) must always be specified with `lock master`. All child entities are always `lock dependent`. Consequently, when child entities are requested to be locked, their corresponding instance of the root entity is locked. See more details on the BDEF prerequisites in the RAP BDL documentation for [locking](../rap-behavior-definitions/abenbdl_locking.md).

The addition [`response_param`](abapeml_response.md) is optional. If an instance is already locked in parallel, information with the failure cause `IF_ABAP_BHEV-LOCKED` (see types contained in the interface `IF_ABAP_BEHV`) is returned in the `FAILED` response parameter.

The following variants of the statement `SET LOCKS` enable the exclusive locking of instances:

- [`SET LOCKS ENTITY`, Short Form](abapset_locks_entity.md)

  The short form of the `SET LOCKS` statement allows instances of a single entity to be locked.

- [`SET LOCKS OF`, Long Form](abapset_locks_of.md)

  The long form of the `SET LOCKS` statement allows instances of multiple entities to be locked.

- [`SET LOCKS lock_tab`, Dynamic Form](abapset_locks_dyn.md)

  The dynamic form of the `SET LOCKS` statement allows multiple instances to be collected and locked in multiple entities in one `SET LOCKS` statement.

## Hints

- `SET LOCKS` statements are only allowed in the [`FOR LOCK`](abaphandler_meth_lock.md) and [`FOR MODIFY`](abaphandler_meth_modify.md) handler methods.

- ABAP EML statements should not be used in loops. Using them can have a performance impact because it can result in multiple single database accesses. There should be only one ABAP EML statement to read the necessary data, and then the data should be modified with an ABAP EML modify request.

## More Information

When implementing RAP operations, ensure that you comply with [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). Follow the implementation guidelines in the development guide for the ABAP RESTful Application Programming Model, section [RAP Business Object Contract](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

You can find a selected set of guidelines in [here](abaprap_impl_rules.md).
