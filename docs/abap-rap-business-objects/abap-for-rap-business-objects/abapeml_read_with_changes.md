---
title: "READ ENTITY, ENTITIES, WITH CHANGES"
source_file: abapeml_read_with_changes.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > READ ENTITY, ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# READ ENTITY, ENTITIES, WITH CHANGES

## Syntax Forms

**Short Form**

``` abap
READ ENTITY IN LOCAL MODE bdef WITH CHANGES ...
```

**Long Form**

``` abap
READ ENTITIES OF bdef IN LOCAL MODE ENTITY entity ... WITH CHANGES ...
```

## Description

The `WITH CHANGES` addition enables access to accumulated change operation information for [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) within a [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md).

When specified, the ABAP EML `READ` statement expects a data object of type `TYPE TABLE FOR READ CHANGES` following [`RESULT`](abapeml_result.md). In addition to RAP BO instance data, the result's type includes the component [`%chg`](abapderived_types_chg.md), which indicates the accumulated operation. For example, it helps determine whether a RAP BO instance is unchanged or has been newly created, updated, or deleted within the current [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md). The [`%control`](abapderived_types_control.md) structure components in the read result show which fields have changed, but only for those components whose `%chg` value is either `if_abap_behv=>cop-create`, `if_abap_behv=>cop-update`, or `if_abap_behv=>cop-recreate`. In other cases, the `%control` component value remains initial.

The `WITH CHANGES` functionality is implicitly available with managed RAP BOs; no separate BDEF specification is required. However, this functionality is not supported in unmanaged scenarios. Therefore, the `WITH CHANGES` addition and the creation of BDEF derived types, such as `TYPE TABLE FOR READ CHANGES`, is not possible in implementation classes of unmanaged RAP BOs.

## Restriction

- Can only be used in [implementation classes](../../abap-glossary/abenbehavior_pool_glosry.md) of managed RAP BOs and managed [draft-enabled RAP BOs](../../abap-glossary/abendraft_rap_bo_glosry.md), including their [extensions](../../abap-glossary/abenrap_extension_glosry.md). Cannot be used with unmanaged RAP BOs.

- Must be specified in conjunction with [`IN LOCAL MODE`](abapin_local_mode.md).

- Cannot be specified for [RAP read-by-association operations](../../abap-glossary/abenrap_rba_operation_glosry.md) or executing [RAP functions](../../abap-glossary/abenrap_function_glosry.md).

## Hints

- Regarding dynamic ABAP EML `READ` statements:

  - The `WITH CHANGES` addition is not available, and the `IN LOCAL MODE` addition must be used.

    `READ ENTITIES IN LOCAL MODE OPERATIONS ...`

  - In such dynamic statements, the `WITH CHANGES` functionality is achieved by setting the `full` component of the statement's operand, which is of type `ABP_BEHV_RETRIEVALS_TAB` (line type: `ABP_BEHV_RETRIEVALS`), to `if_abap_behv=>typekind-result_chg`. Then, `WITH CHANGES` applies, and the result type includes the `%chg` component. **Note:** The referenced type of the `result` component must be typed with `TYPE TABLE FOR READ CHANGES`. Otherwise, the runtime error `BEHAVIOR_ILLEGAL_TYPE` is raised.

- In contrast to an ABAP EML `READ` statement without the `WITH CHANGES` addition, deleted and re-deleted instances appear in the read result (`RESULT result_tab`) rather than the `failed` response parameter, and only with [`%tky`](abapderived_types_tky.md) and [`%chg`](abapderived_types_chg.md) filled. However, instances removed through the [draft action](../../abap-glossary/abenrap_bo_draft_action_glosry.md) `discard` are returned in `failed`.

- Use cases include:

  - Adapting authorization checks and feature controls, especially for new instances to be saved.

  - Invoking legacy APIs that support control flags, such as when calling the [`finalize`](abensaver_finalize.md) [RAP saver method](../../abap-glossary/abenabp_saver_method_glosry.md).

  - Enabling RAP BO consumers to respond to specific changes.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code example, taken from an action implementation of the executable example, shows the short form of an ABAP EML `READ` statement using the `WITH CHANGES` addition.

``` abap
DATA read_changes TYPE TABLE FOR READ CHANGES demo_rap_entity_m. 
 
READ ENTITY IN LOCAL MODE demo_rap_entity_m 
  WITH CHANGES 
  ALL FIELDS WITH CORRESPONDING #( keys ) 
  RESULT read_changes 
  FAILED failed.
```

The following code example, taken from an action implementation of the executable example, shows a dynamic ABAP EML `READ` statement that includes the `WITH CHANGES` functionality.

``` abap
DATA: op_tab          TYPE abp_behv_retrievals_tab, 
      read_dyn        TYPE TABLE FOR READ IMPORT demo_rap_entity_m, 
      read_dyn_result TYPE TABLE FOR READ CHANGES demo_rap_entity_m, 
      entity          TYPE abp_entity_name VALUE 'DEMO_RAP_ENTITY_M'. 
 
read_dyn = VALUE #( FOR wa IN keys ( 
  %key-key_field = wa-key_field 
  %control-field1 = if_abap_behv=>mk-on 
  %control-field2 = if_abap_behv=>mk-on 
  %control-field3 = if_abap_behv=>mk-on 
  %control-field4 = if_abap_behv=>mk-on ) ). 
 
op_tab = VALUE #( ( 
  op = if_abap_behv=>op-r-read 
  entity_name = entity 
  full        = if_abap_behv=>typekind-result_chg 
  instances   = REF #( read_dyn ) 
  results     = REF #( read_dyn_result ) ) ). 
 
READ ENTITIES IN LOCAL MODE OPERATIONS op_tab FAILED DATA(f).
```

## Executable Example

The example [ABAP EML - Read Operations Using `WITH CHANGES`](abeneml_read_with_changes_abexa.md) demonstrates the `WITH CHANGES` addition to both short and long form of the ABAP EML `READ` statement. It also shows a dynamic ABAP EML `READ` statement that includes the `WITH CHANGES` functionality.
