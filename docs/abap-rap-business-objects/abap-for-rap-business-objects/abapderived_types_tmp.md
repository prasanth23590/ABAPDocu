---
title: "%tmp"
source_file: abapderived_types_tmp.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Components Related to Keys and RAP BO Instance Identification"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %tmp

## Use

`%tmp` is a [component group](../../abap-glossary/abencomponent_group_glosry.md) in [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md), holding preliminary key values. It is used in the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) within the [`adjust_numbers`](abensaver_adjust_numbers.md) method, making it available only in [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) scenarios. This component is crucial for the [`mapped`](abaptype_response_for.md) parameter to map preliminary to final key values in [`%key`](abapderived_types_key.md), especially in case [`%key`](abapderived_types_key.md) is used to contain preliminary keys instead of [`%pid`](abapderived_types_pid.md) during the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md).

## More Information

[Using Keys and Identifying RAP BO Instances in a Nutshell](abapderived_types_keys_identifiers.md)

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- `MAPPED LATE`

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code snippet from the `BP_DEMO_UMANAGED_ROOT_LATE_NU3CCIMP` of the global class of the [behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) `BP_DEMO_UMANAGED_ROOT_LATE_NU3` demonstrates the component `%tmp` in the context of an [`adjust_numbers`](abensaver_adjust_numbers.md) method that assigns the final keys. See the executable program for this example further down.

``` abap
... 
APPEND VALUE #( %pre = VALUE #( %pid = <fs>-pid 
                                %tmp-key_field = <fs>-tmp_key ) 
                %key-key_field = final_key 
              ) TO mapped-demo_umanaged_root_late_num3. 
...
```

## Executable Example

The example [Using `%pre` / `%tmp` / `%pky`](abenderived_types_pre_tmp_abexa.md) demonstrates the use of `%tmp` with an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) in a [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) scenario.
