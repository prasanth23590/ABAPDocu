---
title: "%tky"
source_file: abapderived_types_tky.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Components Related to Keys and RAP BO Instance Identification"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %tky

## Use

`%tky` is a [component group](../../abap-glossary/abencomponent_group_glosry.md) in [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) and specifies the transactional key. A [RAP BO instance](../../abap-glossary/abenrap_bo_instance_glosry.md) must always be uniquely identifiable by its transactional key for internal processing during the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md).

`%tky` contains [`%key`](abapderived_types_key.md) and the draft indicator [`%is_draft`](abapderived_types_is_draft.md) as components which makes it particularly suitable for [draft](../rap-behavior-definitions/abenbdl_with_draft.md) scenarios. Since `%tky` includes `%key`, `%tky` can also be used in non-draft scenarios for referring to the primary keys. Its use in non-draft scenarios is even recommended as a preparation for a possible later switch to a draft scenario. In doing so, lots of adaptations to the code regarding the keys and the inclusion of [`%is_draft`](abapderived_types_is_draft.md) can be avoided.

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

## More Information

[Using Keys and Identifying RAP BO Instances in a Nutshell](abapderived_types_keys_identifiers.md)

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- Wherever `%key` can be specified within ABAP EML statements during the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md) except for RAP create operations, `%tky` can be specified, too.

## Hint

As outlined in the topic [Using Keys and Identifying RAP BO Instances in a Nutshell](abapderived_types_keys_identifiers.md), the use of `%tky` is generally preferable in whatever context. However, there are special cases in which `%tky` is not available and [`%pky`](abapderived_types_pky.md) can be used instead, for example, implementations with [draft actions](../rap-behavior-definitions/abenbdl_draft_action.md) or save actions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_DRVD_TYPES_TKY` demonstrates the component `%tky`.

``` abap
MODIFY ENTITY demo_managed_draft_root 
 UPDATE FIELDS ( field2 ) WITH VALUE #( 
    ( %tky = VALUE #( %is_draft = if_abap_behv=>mk-on 
                      %key-key_field = 4 ) 
      field2 = 'up_draft1' ) 
    ( %tky = VALUE #( %is_draft = if_abap_behv=>mk-on 
                      %key-key_field = 5 ) 
      field2 = 'up_draft2' ) 
    ( %tky = VALUE #( %is_draft = if_abap_behv=>mk-on 
                      %key-key_field = 6 ) 
      field2 = 'up_draft3' ) ) 
    MAPPED FINAL(mapped) 
    FAILED FINAL(failed) 
    REPORTED FINAL(reported).
```

## Executable Example

The example [Using `%tky`](abenderived_types_tky_abexa.md) demonstrates the use of `%tky` with a managed RAP BO in a draft and non-draft scenario.
