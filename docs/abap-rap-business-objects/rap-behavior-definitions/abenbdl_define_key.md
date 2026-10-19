---
title: "RAP - BDEF Alternative Key"
source_file: abenbdl_define_key.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - BDEF Alternative Key

## Syntax

``` abap
define {pure|secondary} key AlternativeKey { altKeyField1; altKeyField2; }  
```

## Description

In general, behavior definitions have the following types of keys:

- The [primary key](../../abap-glossary/abenprimary_key_glosry.md) of a RAP BO is derived from the key definition of the underlying CDS data model.

- There are several predefined [secondary table keys for BDEF derived types](../abap-for-rap-business-objects/abapderived_types_secondary_keys.md).

In addition, the following types of user-defined keys exist:

- [BDEF Pure Key](../../abap-glossary/abenrap_pure_key_glosry.md)

  A BDEF pure key `AlternativeKey` defines a set of fields of the underlying CDS entity that can be used as an alternative key. For example, a BDEF pure key is used to define the signature of a [key function](abenbdl_keyfunction.md).

- [BDEF Secondary Key](../../abap-glossary/abenrap_secondary_key_glosry.md)

  A BDEF secondary key `AlternativeKey` has the same effect as a BDEF pure key. In addition, it defines a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) for all [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) that contain the component [`%data`](../abap-for-rap-business-objects/abapderived_types_data.md), such as [`TABLE FOR CREATE`](../abap-for-rap-business-objects/abaptype_table_for.md), [`TABLE FOR UPDATE`](../abap-for-rap-business-objects/abaptype_table_for.md), [`TABLE FOR READ RESULT`](../abap-for-rap-business-objects/abaptype_table_for.md), and [`TABLE FOR CHANGE`](../abap-for-rap-business-objects/abaptype_table_for.md).

Syntax rules:

- The name `AlternativeKey` can be used to address the alternative key. It must follow the [naming conventions](../../abap-programming-language/abap-syntax-elements-of-an-abap-program/abennaming_conventions.md). For more details, see the topic [`TYPES`, `secondary_key`](../../abap-programming-language/abap-declarations/abaptypes_secondary_key.md).

- The [alternative key](../../abap-glossary/abenrap_alternative_key_glosry.md) `AlternativeKey` consists of one or more fields `altKeyField1`, `altKeyField2`, ..., from the underlying CDS entity. Each field can only be used once.

- There can be a maximum of ten secondary keys for each RAP BO entity in a [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md). The number of pure keys is not limited.

- BDEF secondary keys have the same restrictions as secondary table keys in internal tables. In particular, the fields of a secondary table key cannot be a subset of the fields of another secondary table key. For details, see [`TYPES`, `secondary_key`](../../abap-programming-language/abap-declarations/abaptypes_secondary_key.md).

## Restriction

The fields `altKeyField1`, `altKeyField2`, ... should not have one of the following data types: `STRING`, `RAWSTRING`, `GEOM_EWKB`, `LCHR`, and `LRAW`.

## Use

BDEF alternative keys are used, for example, to define the signature of a RAP key function to enable [read-by-association](../../abap-glossary/abenrap_rba_operation_glosry.md) operations in RAP BOs with [cross-BO associations](../../abap-glossary/abencds_cross_bo_assoc_glosry.md) involving RAP reuse objects.

- BDEF pure keys are recommended for defining a [RAP key function](../../abap-glossary/abenrap_key_function_glosry.md). For details, see the topic [RAP - `key function`](abenbdl_keyfunction.md).

- BDEF secondary keys are recommended if you want to support efficient looping over tables that use these fields as a secondary index.

## Availability

- [Managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BOs](../../abap-glossary/abenunmanaged_rap_bo_glosry.md).

- In a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md) and in a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), alternative keys from the [base BO](../../abap-glossary/abenrap_projected_bo_glosry.md) can be reused. For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

## Hint

The syntax `define key` is obsolete and should not be used. `define secondary key` or `define pure key` should be used instead.
