---
title: "RAP - save after"
source_file: abenbdl_save_after.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - BehaviorDefinitionHeader"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - save after

## Syntax

``` abap
... 
save after BdefName1[, BdefName2, ...]; 
 ...  
```

## Description

`save_after` explicitly sets the order in which RAP BOs are saved when instances of multiple RAP BOs are involved after triggering the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md). It is used in the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md) of [RAP BO root entities](../../abap-glossary/abenrap_bo_root_entity_glosry.md) defining other RAP BOs (`BdefName1`, `BdefName2`, etc.) in the `save after` list that are processed first.

`BdefName1`, `BdefName2`, etc., can be other root entities and [RAP BO interface entities](../../abap-glossary/abenrap_bo_interface_entity_glosry.md).

Contradictory specifications must be avoided. For example, if RAP BO *A* specifies `save after B;`, then RAP BO *B* cannot specify `save after A;`.

## Availability

`save after` can be defined in the following types of behavior definitions:

- [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

## Hint

Using `save_after` is typically relevant for scenarios involving [late numbering](../../abap-glossary/abenrap_late_numbering_glosry.md). When RAP BO *A* specifies `save after` and declares RAP BO *B* as a predecessor, *B* is processed first. The final keys of *B* can be retrieved using [`CONVERT KEY`](../abap-for-rap-business-objects/abapconvert_key.md) in the [`adjust_numbers`](../abap-for-rap-business-objects/abensaver_adjust_numbers.md) [RAP saver method](../../abap-glossary/abenabp_saver_method_glosry.md) of *A*.

## Executable Example

[RAP - RAP Explicit Save Order](abenbdl_save_after_abexa.md)
