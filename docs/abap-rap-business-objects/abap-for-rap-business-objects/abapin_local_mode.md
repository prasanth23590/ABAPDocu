---
title: "ABAP EML - IN LOCAL MODE"
source_file: abapin_local_mode.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP EML - Providing RAP BOs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - IN LOCAL MODE

## Syntax

``` abap
... IN LOCAL MODE ...  
```

## Description

The addition is used to suppress feature controls, authorization checks, and prechecks. It can be added to the following EML statements:

- [`READ ENTITY, ENTITIES`](abapread_entity_entities.md)

- [`MODIFY ENTITY, ENTITIES`](abapmodify_entity_entities.md)

It is only applicable in [RAP business object (RAP BO)](../../abap-glossary/abenrap_bo_glosry.md) implementations for the accessed RAP BO itself. This means `IN LOCAL MODE` can only be used in implementation classes of this RAP BO and in code called from those implementation classes (for example, legacy code or other reused logic). In the latter case, a compiler warning results. At runtime, there will not be an issue if this logic is called via the implementation classes of this RAP BO. Otherwise, a short dump is the consequence.

**Example use case**

A field to display the booking status of a trip on an SAP Fiori UI is specified as `readonly` in a [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md). Hence, it cannot be modified by a user on the UI directly. For example, the status of a trip is set to and displayed as *not booked*. A button on the UI triggers an action to book the trip. With clicking the button, the status gets changed and *booked* is displayed. To enable this, the underlying modify operation with the action to be executed in the ABP has the addition `IN LOCAL MODE` that ignores the feature control.

**Considerations for suppressing checks when using `IN LOCAL MODE`**

- The implementation of a RAP BO is usually partitioned into several [RAP BO providers](../../abap-glossary/abenrap_bo_provider_glosry.md) (i. e. [ABAP behavior pools (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md)), in particular, different ABPs for [RAP base BO](../../abap-glossary/abenrap_projected_bo_glosry.md) and [BDEF extensions](../../abap-glossary/abenrap_extension_glosry.md). A provider *owns* certain elements, like [actions](../../abap-glossary/abenrap_action_glosry.md), or an entire [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md), based on their specification in its [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md), and it provides the implementation for these elements.

- To understand the effect of adding `IN LOCAL MODE` to ABAP EML statements, *using* and *owning* providers must be distinguished:

  - *Using* provider: The provider that includes or indirectly calls the ABAP EML statement.

  - *Owning* provider: The providers/provider that own/owns the elements used in the ABAP EML statement.

- The addition only suppresses checks on elements where *using* = *owning* provider. It cannot suppress checks for operations or elements that are not *owned*.

- Examples:

  - In the ABAP behavior pool of the RAP base BO, a [RAP factory action](../../abap-glossary/abenrap_factory_action_glosry.md) implements an ABAP EML `MODIFY` statement with `IN LOCAL MODE` to create new instances for that BO. If the create operation specifies a precheck, the precheck handler method is not called.

  - In an [extension](../../abap-glossary/abenrap_extension_glosry.md) ABAP behavior pool's handler implementation, a combined update operation affects both the extension entity and the base BO's root entity. Using `IN LOCAL MODE` suppresses checks on the extension entity, but not on the base BO's root entity.

## Hints

- A [BAdI](../../abap-glossary/abenbadi_glosry.md) call occurring during a BO implementation is not considered to be part of the BO implementation, so `IN LOCAL MODE` inside the BAdI will result in a runtime error.

- Special behavior when using the `IN LOCAL MODE` addition in the context of [BDEF extensions](../../abap-glossary/abenrap_extension_glosry.md):

  - `IN LOCAL MODE` has its check-suppressing effect only on operations owned by the extension. It is not applied to operations owned by the original BO or another extension.

  - When the `IN LOCAL MODE` addition is used in ABAP EML requests in the context of BDEF extensions, the privileged mode is implicitly used as if the `PRIVILEGED` addition had been added. The [BDEF privileged mode](../../abap-glossary/abenrap_privileged_mode_glosry.md) is applied to the entire ABAP EML request and, if supported by the RAP BO, authorization checks are turned off.

- Specifying the `IN LOCAL MODE` addition (in the original BO implementation) acts as if [`FORWARDING PRIVILEGED`](abapeml_privileged.md) was specified.

- In [cross-BO](../../abap-glossary/abencds_cross_bo_assoc_glosry.md) scenarios, when association-related ABAP EML requests on the [association source](../../abap-glossary/abenassociation_source_glosry.md)&#x00A0;are performed and specify `IN LOCAL MODE` (such as [read-by-association](../../abap-glossary/abenrap_rba_operation_glosry.md) or [create-by-association](../../abap-glossary/abenrap_cba_operation_glosry.md) operations), the [association target](../../abap-glossary/abenassociation_target_glosry.md)'s implementation of the operation is accessed in privileged mode (not in local mode), bypassing the association target's authorization checks. This applies only if the association target is specified with a [privileged](../../abap-glossary/abenrap_privileged_mode_glosry.md) context.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section is taken from here: `BP_DEMO_MANAGED_ROOT_3========CCIMP`. The global class of the behavior pool is `BP_DEMO_MANAGED_ROOT_3`. The code example is used in the context of the `get_instance_features` method of the executable example `CL_DEMO_RAP_EML_GET_PERMISSION`.

``` abap
READ ENTITIES OF demo_managed_root_3 IN LOCAL MODE 
  ENTITY demo_managed_root_3 
  FIELDS ( data_field3_root data_field4_root ) 
  WITH CORRESPONDING #( keys ) 
  RESULT DATA(lt_numbers) 
  FAILED DATA(failed).
```
