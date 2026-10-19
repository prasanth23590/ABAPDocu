---
title: "%pky"
source_file: abapderived_types_pky.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Components Related to Keys and RAP BO Instance Identification"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %pky

## Use

`%pky` is a [component group](../../abap-glossary/abencomponent_group_glosry.md) in [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md).

It serves as an identifier in a transaction in which a [RAP BO instance](../../abap-glossary/abenrap_bo_instance_glosry.md) is created. In non-[`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) scenarios, `%pky` is equal to [`%key`](abapderived_types_key.md) (and, thus, serves also as an identifier for persisted RAP BO instances). In a late numbering scenario, it is equal to the combination of [`%pid`](abapderived_types_pid.md) and `%key`. This identifier does not change between the creation of an instance and the next saving.

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- Wherever `%key` can be specified within ABAP EML statements during the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md) except for RAP create operations, `%pky` can be specified, too.

- `%pky` is basically another option to refer to the keys. In non-late numbering scenarios, `%key` is the same as `%pky` since `%pid` is not available. In scenarios without late numbering and without [draft](../rap-behavior-definitions/abenbdl_with_draft.md), `%pky` is [`%tky`](abapderived_types_tky.md) since [`%is_draft`](abapderived_types_is_draft.md) is not available. As outlined in the topic [Using Keys and Identifying RAP BO Instances in a Nutshell](abapderived_types_keys_identifiers.md), the use of `%tky` is generally preferable to `%pky`. However, there are special cases in which `%tky` is not available and `%pky` can be used instead, for example, implementations with [draft actions](../rap-behavior-definitions/abenbdl_draft_action.md) or save actions.

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

## Executable Example

The example [Using `%pre` / `%tmp` / `%pky`](abenderived_types_pre_tmp_abexa.md) demonstrates the use of `%pky` with an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) in a [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) scenario.
