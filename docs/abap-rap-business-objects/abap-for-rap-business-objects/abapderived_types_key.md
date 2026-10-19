---
title: "%key"
source_file: abapderived_types_key.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Components Related to Keys and RAP BO Instance Identification"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %key

## Use

`%key` is a [component group](../../abap-glossary/abencomponent_group_glosry.md) in [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). The component group contains the primary key fields of a [RAP BO instance](../../abap-glossary/abenrap_bo_instance_glosry.md). Thus, it serves as an identifier for persisted instances.

Wherever `%key` can be specified within ABAP EML statements during the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md), [`%tky`](abapderived_types_tky.md) can be specified, too. Since the component group `%tky` includes `%key`, it is recommended that `%tky` is specified instead of `%key` also in non-[draft](../rap-behavior-definitions/abenbdl_with_draft.md) scenarios. `%tky` also contains the draft indicator [`%is_draft`](abapderived_types_is_draft.md). When using `%tky` in non-draft scenarios, you are prepared for a later switch to a draft scenario and you can avoid lots of adaptations in the code.

**Type**

The key fields in `%key` have their original line type. In case of the use within [`%control`](abapderived_types_control.md), the type of the key fields is `ABP_BEHV_FLAG`.

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- `CREATE`

- `UPDATE`

- `DELETE`

- `READ IMPORT`

- `READ RESULT`

- `READ LINK` (here, as part of the structures `SOURCE` and `TARGET`)

- `ACTION IMPORT` ([instance actions](../rap-behavior-definitions/abenbdl_action.md))

- `ACTION RESULT` (instance actions)

- `ACTION REQUEST` (instance actions)

- `FUNCTION IMPORT` ([instance functions](../rap-behavior-definitions/abenbdl_function.md) )

- `FUNCTION RESULT` (instance functions)

- `FUNCTION REQUEST` (instance functions)

- `PERMISSIONS KEY`

- `DETERMINATION`

- `VALIDATION`

- `FAILED [EARLY|LATE]`

- `MAPPED [EARLY|LATE]`

- `REPORTED [EARLY|LATE]`

- `CHANGE`

- `[INSTANCE] FEATURES KEY`

- `[INSTANCE] FEATURES RESULT`

- `[INSTANCE] AUTHORIZATION KEY`

- `[INSTANCE] AUTHORIZATION RESULT`

The component also occurs within the following component groups:

- `%control`

- [`%param`](abapderived_types_param.md)

- [`%tmp`](abapderived_types_tmp.md)

- [`%pky`](abapderived_types_pky.md)

**Assignment of Key Component Groups**

As a general best practice, you should use a [RAP BO instance key component group](../../abap-glossary/abenkey_comp_group_glosry.md) when referring to the entire key, rather than listing the individual key fields. It is recommended that you use %tky whenever possible.

In the following cases, type compatibility cannot be guaranteed in component group assignments, resulting in syntax warnings:

- Mixing key component groups when they refer to the same RAP BO entity, e.g. `wa-%tky = wa-%key`. Such an assignment should also be avoided when both component groups have an identical scope in terms of components (e.g. `%tky` and `%key` in non-late-numbering and non-draft scenarios).

- Mixing the same key component groups when referring to two different RAP BO entities, for example, `wa_root-%tky = wa_child-%tky`. In this case, adding more components later may cause syntax errors for an assignment that worked previously.

- Defining structured types that have the same components as key component groups, and then assigning data objects of that type to those of the respective, original key component group.

In the above cases, the CORRESPONDING operator can be used to ensure type compatibility in assignments to key component groups:

``` abap
... %tky = CORRESPONDING #( wa-%tky ) ... 
... %key = CORRESPONDING #( wa-%key ) ... 
... %pky = CORRESPONDING #( wa-%pky ) ...
```

In cases where different data objects of key component groups of a BDEF derived type are to be assigned to the same key component group of the same entity, a direct assignment works without a syntax warning because the content is identical. A direct assignment is recommended (...wa1_root-%tky = wa2_root-%tky ...). The use of the CORRESPONDING operator is unnecessary and has poorer performance. This is true, for example, for key component group assignments in the context of RAP response parameters failed and reported.

``` abap
APPEND VALUE #( %tky = wa-%tky 
                  ... 
               ) TO failed-root_entity.
```

## Hints

- In late numbering scenarios, not only [`%pid`](abapderived_types_pid.md) but also `%key` can contain preliminary keys during the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md). The preliminary keys are transformed into final key values with the [`adjust_numbers`](abensaver_adjust_numbers.md) method.

- The components of an internal table typed with `TYPE TABLE FOR KEY OF` or a structure with the type `TYPE STRUCTURE FOR KEY OF` comprise the key fields directly and not as `%key` component groups.

## More Information

[Using Keys and Identifying RAP BO Instances in a Nutshell](abapderived_types_keys_identifiers.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_DRVD_TYPES_KEY` demonstrates the component `%key`. It includes various options on how to refer to the key, also visualizing the occurrence of the key in various component groups.

``` abap
MODIFY ENTITY demo_managed_root_4 
    CREATE FROM VALUE #( 
       %control = VALUE #( key_field = if_abap_behv=>mk-on 
                           field1 = if_abap_behv=>mk-on 
                           field2 = if_abap_behv=>mk-on 
                           field3 = if_abap_behv=>mk-on 
                           field4 = if_abap_behv=>mk-on ) 
      ( %cid = 'cid1' 
        %key-key_field = 1 
        field1 = 'aaa' field2 = 'bbb' field3 = 10 field4 = 11 ) 
      ( %cid = 'cid2' 
        %key = VALUE #( key_field = 2 ) 
        field1 = 'ccc' field2 = 'ddd' field3 = 20 field4 = 21 ) 
      ( %cid = 'cid3' 
        key_field = 3 
        field1 = 'eee' field2 = 'fff' field3 = 30 field4 = 31 ) 
      ( %cid = 'cid4' 
        %data-%key-key_field = 4 
        field1 = 'ggg' field2 = 'hhh' field3 = 40 field4 = 41 ) 
      ( %cid = 'cid5' 
        %data-key_field = 5 
        field1 = 'iii' field2 = 'jjj' field3 = 50 field4 = 51 ) ) 
    "Other options for referring to the key besides using %key 
    "are demonstrated. 
    UPDATE FIELDS ( field2 ) WITH VALUE #( 
      ( %key-key_field = 1 
        field2 = 'up1' ) 
      ( key_field = 2 
        field2 = 'up2' ) 
      ( %tky-%key-key_field = 3 
        field2 = 'up3' ) 
      ( %tky-key_field = 4 
        field2 = 'up4' ) 
      ( %tky-%pky-%key-key_field = 5 
        field2 = 'up5' ) 
      ( %tky-%pky-key_field = 6 
        field2 = 'up6' ) 
      ( %pky-key_field = 7 
        field2 = 'up7' ) 
      ( %pky-%key-key_field = 8 
        field2 = 'up8' ) 
      ( %data-%key-key_field = 9 
        field2 = 'up9' ) 
      ( %data-key_field = 10 
        field2 = 'up10' ) ) 
     MAPPED FINAL(mapped) 
     FAILED FINAL(failed) 
     REPORTED FINAL(reported).
```

## Executable Example

The example [Using `%key`](abenderived_types_key_abexa.md) demonstrates the use of `%key` with a managed RAP BO.
