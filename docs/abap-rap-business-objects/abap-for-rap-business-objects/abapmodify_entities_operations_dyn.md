---
title: "MODIFY ENTITIES OPERATIONS, Dynamic Form"
source_file: abapmodify_entities_operations_dyn.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > MODIFY ENTITY, ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MODIFY ENTITIES OPERATIONS, Dynamic Form

## Syntax

``` abap
MODIFY ENTITIES [IN LOCAL MODE|[FORWARDING  ] PRIVILEGED  ] OPERATIONS op_tab [response_param  ].  
```

[`IN LOCAL MODE`](abapin_local_mode.md) · [`FORWARDING `](abapeml_privileged.md) · [`PRIVILEGED `](abapeml_privileged.md) · [`response_param `](abapeml_response.md)

### Addition

[1. `... IN LOCAL MODE ...`](abapmodify_entities_operations_dyn.md#addition-1)

[2. `... [FORWARDING] PRIVILEGED ...`](abapmodify_entities_operations_dyn.md#addition-2)

[3. `... response_param.`](abapmodify_entities_operations_dyn.md#addition-3)

## Overview

### Description

The dynamic version of the `MODIFY ENTITIES` statement executes multiple modify operations for multiple RAP BOs in one `MODIFY` statement.

`op_tab` must be a table of type `ABP_BEHV_CHANGES_TAB`. This table has specific components:

| **Component** | **Details**                                                                                                                                                                                                                                                                                                                                                  |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `op`          | It is a mandatory component specifying the operation to be executed. It can be set with the defined constants, for example, `op-m-create`, of interface `IF_ABAP_BEHV` or just the predefined value for the operation in the interface, for example `'C'` for a create operation (`op = 'C'`).                                                               |
| `entity_name` | It is a mandatory component and specifies the name of the BO entity for which the operation is executed. The name must be provided using capital letters.                                                                                                                                                                                                    |
| `sub_name`    | Optional component. It is only relevant for specifying association names in case of create-by-association operations or for actions. The name must be provided using capital letters. In case of create-by-association operations, when using the constant `if_abap_behv=>op-m-create_ba`, the alias name for the association must be provided in uppercase. |
| `instances`   | It is a mandatory component specifying the instances in an internal table. The table is a reference variable with [static type](../../abap-glossary/abenstatic_type_glosry.md) `DATA`.                                                                                                                                                                                         |
| `request`     | It is an optional component specifying an internal table for requests. The table is a reference variable with [static type](../../abap-glossary/abenstatic_type_glosry.md) `DATA`.                                                                                                                                                                                             |
| `results`     | It is an optional component storing results of an action. The table is a reference variable with [static type](../../abap-glossary/abenstatic_type_glosry.md) `DATA`.                                                                                                                                                                                                          |

### Hint

A [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) must not use ABAP EML `MODIFY` statements in the [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md) [`check_before_save`](abensaver_check_before_save.md), [`adjust_numbers`](abensaver_adjust_numbers.md), [`save`](abensaver_method_save.md), [`save_modified`](abaprap_saver_meth_save_modified.md) and [`cleanup`](abensaver_method_cleanup.md). The statements can only be used in the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md) and in the [`finalize`](abensaver_finalize.md) saver method in the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md). Furthermore, ABAP EML `MODIFY` statements are not allowed in read-only [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md).

## Addition 1

`... IN LOCAL MODE ...`

### Description

The addition [`IN LOCAL MODE`](abapin_local_mode.md) is used to exclude [feature controls](../rap-behavior-definitions/abenbdl_actions_fc.md) and [authorization checks](../rap-behavior-definitions/abenbdl_authorization.md). It can only be used within the RAP BO runtime implementation.

## Addition 2

`... [FORWARDING] PRIVILEGED ...`

### Description

The addition [`PRIVILEGED`](abapeml_privileged.md) is used for a privileged access to a RAP BO, i. e. the RAP BO runtime does not perform certain authorization checks. As a prerequisite, `privileged` must be specified in the BDEF.

## Addition 3

`... response_param.`

### Description

The addition [`response_param`](abapeml_response.md) represents the response parameters that can be specified. Used in the context of the dynamic form of the ABAP EML statement, the parameters must be internal tables typed with `ABP_BEHV_RESPONSE_TAB`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_MODIFY` demonstrates an EML `MODIFY ENTITIES OPERATIONS` statement that includes `CREATE`, `UPDATE` and `DELETE` operations.

``` abap
DATA: failed_dyn       TYPE abp_behv_response_tab, 
      reported_dyn     TYPE abp_behv_response_tab, 
      mapped_dyn       TYPE abp_behv_response_tab, 
      op_tab           TYPE abp_behv_changes_tab, 
      create_root_tab  TYPE TABLE FOR CREATE demo_managed_root, 
      update_root_tab  TYPE TABLE FOR UPDATE demo_managed_root, 
      delete_root_tab  TYPE TABLE FOR UPDATE demo_managed_root, 
      cba              TYPE TABLE FOR CREATE demo_managed_root\_child, 
      update_child_tab TYPE TABLE FOR UPDATE demo_managed_child, 
      delete_child_tab TYPE TABLE FOR DELETE demo_managed_child. 
 
create_root_tab = VALUE #( 
            ( %cid = 'cid1' 
              key_field = 5 
              %control-key_field = if_abap_behv=>mk-on 
              data_field1_root = 'aaa' 
              %control-data_field1_root = if_abap_behv=>mk-on 
              data_field2_root = 'bbb' 
              %control-data_field2_root = if_abap_behv=>mk-on ) 
            ( %cid = 'cid2' 
              key_field = 6 
              %control-key_field = if_abap_behv=>mk-on 
              data_field1_root = 'ccc' 
              %control-data_field1_root = if_abap_behv=>mk-on 
              data_field2_root = 'ddd' 
              %control-data_field2_root = if_abap_behv=>mk-on ) 
            ( %cid = 'cid3' 
              key_field = 7 
              %control-key_field = if_abap_behv=>mk-on 
              data_field1_root = 'eee' 
              %control-data_field1_root = if_abap_behv=>mk-on 
              data_field2_root = 'fff' 
              %control-data_field2_root = if_abap_behv=>mk-on ) ). 
 
update_root_tab = VALUE #( 
          ( %cid_ref = 'cid2' 
            %control-key_field = if_abap_behv=>mk-on 
            data_field1_root = 'GGG' 
            %control-data_field1_root = if_abap_behv=>mk-on 
            data_field2_root = 'HHH' 
            %control-data_field2_root = if_abap_behv=>mk-on ) ). 
 
cba = VALUE #( 
            ( %cid_ref = 'cid1' 
              %target = VALUE #( ( 
                %cid = 'cid_cba1' 
                %control-key_field = if_abap_behv=>mk-off 
                data_field1_child = 'iii' 
                %control-data_field1_child = if_abap_behv=>mk-on 
                data_field2_child = 'jjj' 
                %control-data_field2_child = if_abap_behv=>mk-on 
            ) ) ) 
            ( %cid_ref = 'cid2' 
              %target = VALUE #( ( 
                %cid = 'cid_cba2' 
                %control-key_field = if_abap_behv=>mk-off 
                data_field1_child = 'kkk' 
                %control-data_field1_child = if_abap_behv=>mk-on 
                data_field2_child = 'lll' 
                %control-data_field2_child = if_abap_behv=>mk-on 
            ) ) ) 
            ( %cid_ref = 'cid3' 
              %target = VALUE #( ( 
                %cid = 'cid_cba3' 
                %control-key_field = if_abap_behv=>mk-off 
                data_field1_child = 'mmm' 
                %control-data_field1_child = if_abap_behv=>mk-on 
                data_field2_child = 'nnn' 
                %control-data_field2_child = if_abap_behv=>mk-on 
            ) ) ) ). 
 
update_child_tab = VALUE #( 
           ( key_field = 6 
             %control-key_field = if_abap_behv=>mk-off 
             data_field1_child = 'OOO' 
             %control-data_field1_child = if_abap_behv=>mk-on 
             data_field2_child = 'PPP' 
             %control-data_field2_child = if_abap_behv=>mk-on ) ). 
 
delete_root_tab = VALUE #( ( key_field = 7 ) ). 
 
delete_child_tab = VALUE #( ( key_field = 7 ) ). 
 
op_tab = VALUE #( 
       ( op = if_abap_behv=>op-m-create 
         entity_name = 'DEMO_MANAGED_ROOT' 
         instances   = REF #( create_root_tab ) ) 
       ( op = if_abap_behv=>op-m-update 
         entity_name = 'DEMO_MANAGED_ROOT' 
         instances   = REF #( update_root_tab ) ) 
       ( op = if_abap_behv=>op-m-delete 
         entity_name = 'DEMO_MANAGED_ROOT' 
         instances   = REF #( delete_root_tab ) ) 
       ( op = if_abap_behv=>op-m-create_ba 
         entity_name = 'DEMO_MANAGED_ROOT' 
         sub_name    = '_CHILD' 
         instances   = REF #( cba ) ) 
       ( op = if_abap_behv=>op-m-update 
         entity_name = 'DEMO_MANAGED_CHILD' 
         instances   = REF #( update_child_tab ) ) 
       ( op = if_abap_behv=>op-m-delete 
         entity_name = 'DEMO_MANAGED_CHILD' 
         instances   = REF #( delete_child_tab ) ) 
       ). 
 
MODIFY ENTITIES OPERATIONS op_tab 
  FAILED   failed_dyn 
  REPORTED reported_dyn 
  MAPPED   mapped_dyn.
```

### Executable Example

- The example [ABAP EML - `MODIFY`, Variants](abeneml_modify_alternatives_abexa.md) demonstrates this `MODIFY` variant with a simple managed RAP BO.

- For more examples of `MODIFY` operations in general, refer to [Examples for ABAP EML `MODIFY`](abapeml_modify_examples_abexas.md).
