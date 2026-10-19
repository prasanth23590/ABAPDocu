---
title: "%param"
source_file: abapderived_types_param.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Miscellaneous Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %param

## Use

`%param` is a structured component in [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md).

It is used for the [`result`](abapeml_result.md) parameter in the context of [action](../rap-behavior-definitions/abenbdl_action.md) and [function](../rap-behavior-definitions/abenbdl_function.md) implementations. `%param` must be filled by the action or function implementation if a result is defined. For actions or functions with a selective result, only those fields that are requested with the `REQUEST` addition must be filled.

In the context of the draft action [`edit`](../rap-behavior-definitions/abenbdl_draft_action.md), `%param` contains the component `preserve_changes`. It is a Boolean value and if it is set to true, the draft action request is rejected if a draft already exists. If it is set to false, which is the default setting, the edit is executed, i. e. the active instance is copied to the draft database table and the existing draft is overwritten with the values of the active data. In that case, current changes on the existing draft instance are lost.

**Type**

- Depending on the specification of the parameter in the BDEF, `%param` can be a structure whose components are comprised of `%data` and `%key`/`%tky`/`%pky` plus, if relevant, other `%` components like `%pid`. `%param` can also be of the DDIC type that is specified in the BDEF for static actions or functions.

- In the context of the draft action `edit`, `%param` is of type `ABP_BEHV_PAR_EDIT`.

- In the context of [RAP key functions](../../abap-glossary/abenrap_key_function_glosry.md) when using BDEF derived types of type `FUNCTION IMPORT`, `%param` contains [`%skey`](abapderived_types_skey.md).

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- `ACTION IMPORT`

- `ACTION RESULT`

- `FUNCTION IMPORT`

- `FUNCTION RESULT`

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_DRVD_TYPES_TKY` demonstrates the component `%param` in the context of the draft action `edit`.

``` abap
MODIFY ENTITY demo_managed_draft_root 
    EXECUTE Edit FROM 
    VALUE #( ( %key-key_field = 4 
               %param-preserve_changes = abap_false ) 
             ( %key-key_field = 5 
               %param-preserve_changes = abap_false ) 
             ( %key-key_field = 6 
               %param-preserve_changes = abap_false ) ) 
    MAPPED FINAL(mapped) 
    FAILED FINAL(failed) 
    REPORTED FINAL(reported).
```

## Executable Example

The example [Using `%tky`](abenderived_types_tky_abexa.md) focuses on the use of [`%tky`](abapderived_types_tky.md) with a managed RAP BO in a draft and non-draft scenario. In the code snippet, the [draft action](../rap-behavior-definitions/abenbdl_draft_action.md) `edit` includes the specification of `%param-preserve_changes`.
