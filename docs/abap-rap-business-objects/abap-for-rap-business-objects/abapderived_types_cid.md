---
title: "%cid"
source_file: abapderived_types_cid.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Components Related to Keys and RAP BO Instance Identification"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %cid

## Use

`%cid` is a component of [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). It is a string to define a content ID that should be filled for ABAP EML requests. In [`strict(2)`](../rap-behavior-definitions/abenbdl_strict_2.md) mode, the use of `%cid` is mandatory.

Content IDs are used as a unique, preliminary identifier for [RAP BO](../../abap-glossary/abenrap_bo_glosry.md) instances, especially as long as no primary key exists for the particular instance. `%cid` is used in RAP create operations to create RAP BO instances and for performing further, referencing modifications on those instances using [`%cid_ref`](abapderived_types_cid_ref.md). `%cid_ref` - which has the same value as `%cid` - is then used, for example, in RAP operations using [`CREATE BY`](abapmodify_entity_entities_op.md), [`UPDATE`](abapmodify_entity_entities_op.md) and [`DELETE`](abapmodify_entity_entities_op.md), as well as [actions](../rap-behavior-definitions/abenbdl_action.md) with [`EXECUTE`](abapmodify_entity_entities_op.md) in a single ABAP EML [`MODIFY`](abapmodify_entity_entities.md) request.

`%cid` must be unique within one ABAP EML request and can be specified manually or automatically. The specified content ID is only valid within one ABAP EML request. The specification of `%cid` should be done even if there are no further operations referring to it. Especially in the context of [`early numbering`](../rap-behavior-definitions/abenbdl_early_numb.md) and [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) scenarios, `%cid` must be specified to avoid issues.

In ABAP EML `MODIFY` statements, the [`AUTO FILL CID`](abapmodify_entity_entities_fields.md) addition can be used to create `%cid` automatically to ensure that `%cid` is filled. However, if `%cid_ref` is to be used, `%cid` must be manually specified, as `%cid_ref` cannot refer to an automatically created value.

**Type**

The component has the following type: `ABP_BEHV_CID`.

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- `CREATE`

- `ACTION IMPORT` ([static action](../rap-behavior-definitions/abenbdl_action.md))

- `ACTION RESULT` (static action)

- `FUNCTION IMPORT` ([static function](../rap-behavior-definitions/abenbdl_function.md))

- `FUNCTION RESULT` (static function)

- `FAILED [EARLY]`

- `MAPPED [EARLY]`

- `REPORTED [EARLY]`

The component also occurs in the [`%target`](abapderived_types_target.md) component.

## Hints

- A missing `%cid` specification can cause a runtime error. See [RAP Implementation Rules](abaprap_impl_rules.md).

- Note the difference of using `%cid` with static actions and [factory actions](../../abap-glossary/abenrap_factory_action_glosry.md). In factory actions (this also includes static factory actions), the use of `%cid` is as outlined above. In case of static actions, `%cid` assumes a different role. Here, `%cid` must be considered as an operation ID which can be referred to in RAP [responses](abaptype_response_for.md).

## More Information

[Using Keys and Identifying RAP BO Instances in a Nutshell](abapderived_types_keys_identifiers.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_DRVD_TYPES_CID` demonstrates the component `%cid`.

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
   MAPPED FINAL(mapped) 
   FAILED FINAL(failed) 
   REPORTED FINAL(reported).
```

## Executable Example

The example [Using `%cid` / `%cid_ref`](abenderived_types_cid_cidref_abexa.md) demonstrates the use of `%cid` and `%cid_ref` with a managed RAP BO.
