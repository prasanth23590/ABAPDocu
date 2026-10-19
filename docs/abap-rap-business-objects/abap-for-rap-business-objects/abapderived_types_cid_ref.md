---
title: "%cid_ref"
source_file: abapderived_types_cid_ref.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Components Related to Keys and RAP BO Instance Identification"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %cid_ref

## Use

`%cid_ref` is a component of [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). It is used as a reference to a [RAP BO](../../abap-glossary/abenrap_bo_glosry.md) instance for which [`%cid`](abapderived_types_cid.md) has been specified manually. The value of `%cid_ref` is the same string as `%cid` that is referred to. This `%cid` must exist in the same ABAP EML [`MODIFY`](abapmodify_entity_entities.md) request. Thus, `%cid_ref` cannot be used to refer to a particular `%cid` from another request.

When referencing an instance that has been created in the same request, note the following aspects:

- It is mandatory to provide `%cid` and then `%cid_ref` in the referencing operation. Otherwise, the new instance is not found in a referencing operation.

- [`%key`](abapderived_types_key.md) is ignored in the referencing operation. If `%cid_ref` is provided in a referencing operation, `%key` need not be specified.

## More Information

[Using Keys and Identifying RAP BO Instances in a Nutshell](abapderived_types_keys_identifiers.md)

**Type**

The component has the following type: `ABP_BEHV_CID`.

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- `CREATE` ([create-by-association operations](../../abap-glossary/abenrap_cba_operation_glosry.md) only)

- `UPDATE`

- `DELETE`

- `ACTION IMPORT` ([instance action](../rap-behavior-definitions/abenbdl_action.md))

- `ACTION RESULT` (instance action)

## Hints

- If a [RAP BO operation](../../abap-glossary/abenrap_bo_operation_glosry.md) refers to an instance via `%cid_ref`, the key values of the affected instance are basically ignored if specified in the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md). For example, if a create request is followed by an update request and the reference is made via `%cid_ref`, it does not matter if the update request also specifies the key values for the instance reference (it could actually be a non-existent key).

- According to the [RAP Business Object Contract](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap), for example, a duplicate update on [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) within one and the same ABAP EML request is not allowed. However, the syntax currently allows for a RAP BO operation following a create request in the same RAP transaction to refer to a previously created instance both via `%cid_ref` and only the key values, too.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_DRVD_TYPES_CID` demonstrates the component `%cid_ref` that refers to a previously defined content ID `%cid`.

``` abap
MODIFY ENTITY demo_managed_root_4 
  CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
  WITH VALUE #( 
    ( %cid = 'cid1' 
      key_field = 1 
      field1 = 'aaa' 
      field2 = 'bbb' 
      field3 = 10 
      field4 = 11 ) 
    ( %cid = 'cid2' 
      key_field = 2 
      field1 = 'ccc' 
      field2 = 'ddd' 
      field3 = 20 
      field4 = 21 ) 
    ( %cid = 'cid3' 
      key_field = 3 
      field1 = 'eee' 
      field2 = 'fff' 
      field3 = 30 
      field4 = 31 ) ) 
  CREATE BY \_child 
   FIELDS ( key_field_child field1 field2 field3 field4 ) 
   WITH VALUE #( 
    ( %cid_ref = 'cid1' 
      %target = VALUE #( 
        ( %cid = 'cid_child1' 
          key_field_child = 10 
          field1 = 'ggg' 
          field2 = 'hhh' 
          field3 = 100 
          field4 = 101  ) ) ) ) 
  UPDATE FIELDS ( field2 ) WITH VALUE #( 
    ( %cid_ref = 'cid2' 
      field2 = 'iii' ) ) 
  DELETE FROM VALUE #( 
    ( %cid_ref = 'cid3' ) ) 
   MAPPED FINAL(mapped) 
   FAILED FINAL(failed) 
   REPORTED FINAL(reported).
```

## Executable Example

The example [Using `%cid` / `%cid_ref`](abenderived_types_cid_cidref_abexa.md) demonstrates the use of `%cid` and `%cid_ref` with a managed RAP BO.
