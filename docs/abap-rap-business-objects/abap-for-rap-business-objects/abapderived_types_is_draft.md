---
title: "%is_draft"
source_file: abapderived_types_is_draft.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Components Related to Keys and RAP BO Instance Identification"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %is_draft

## Use

The draft indicator `%is_draft` is a component of [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). It is used to indicate if a [RAP BO](../../abap-glossary/abenrap_bo_glosry.md) instance is a [drafts](../rap-behavior-definitions/abenbdl_with_draft.md) instance or an active instance. To create a draft instance, `%is_draft` must be explicitly set in ABAP EML [`MODIFY`](abapmodify_entity_entities.md) requests.

## More Information

[Using Keys and Identifying RAP BO Instances in a Nutshell](abapderived_types_keys_identifiers.md)

**Type**

The component has the following type: `ABP_BEHV_FLAG`

**Where used**

In ABAP EML [`MODIFY`](abapmodify_entity_entities.md) requests, the component can be referred to directly or via the [component group](../../abap-glossary/abencomponent_group_glosry.md) [`%tky`](abapderived_types_tky.md) since `%is_draft` is a component of `%tky`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_DRVD_TYPES_ISDRAFT` demonstrates the component `%is_draft`.

``` abap
MODIFY ENTITY demo_unmanaged_root_draft 
    CREATE FIELDS ( field1 field2 field3 field4 ) 
    WITH VALUE #( 
       ( %cid = 'cid4' 
         %is_draft = if_abap_behv=>mk-on 
         key_field = 4 
         field1 = 'ggg' 
         field2 = 'hhh' 
         field3 = 40 
         field4 = 41 ) 
       ( %cid = 'cid5' 
         %is_draft = if_abap_behv=>mk-on 
         key_field = 5 
         field1 = 'iii' 
         field2 = 'jjj' 
         field3 = 50 
         field4 = 51 ) 
       ( %cid = 'cid6' 
         %is_draft = if_abap_behv=>mk-on 
         key_field = 6 
         field1 = 'kkk' 
         field2 = 'lll' 
         field3 = 60 
         field4 = 61 ) ) 
       MAPPED FINAL(mapped) 
       FAILED FINAL(failed) 
       REPORTED FINAL(reported).
```

## Executable Example

The example [Using `%is_draft`](abenderived_types_isdraft_abexa.md) demonstrates the use of `%is_draft` with an unmanaged RAP BO in a draft scenario.
