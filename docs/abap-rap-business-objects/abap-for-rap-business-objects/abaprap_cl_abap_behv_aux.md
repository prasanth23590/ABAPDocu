---
title: "CL_ABAP_BEHV_AUX"
source_file: abaprap_cl_abap_behv_aux.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > Other RAP-Related ABAP Language Elements and Topics > RAP-Related System Classes and Functionality"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_BEHV_AUX

The `CL_ABAP_BEHV_AUX` class includes methods for retrieving various pieces of information.

| **Method**                      | **Details**                                                                                                                                                                                                                                                                                    |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GET_CURRENT_PHASE`             | Information about the current [RAP transactional phase](../../abap-glossary/abentransactional_phase_glosry.md), such as the [RAP early save phase](../../abap-glossary/abenearly_rap_save_phase_glosry.md), [RAP late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md), or [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md). |
| `GET_CURRENT_CONTEXT`           | Information about the context of the current [RAP handler](../../abap-glossary/abenabp_handler_method_glosry.md) and [saver method](../../abap-glossary/abenabp_saver_method_glosry.md)                                                                                                                                            |
| `GET_CURRENT_HANDLER_KIND`      | Information about the kind of method. For information on the values, see the domain `ABP_BEHV_KIND`.                                                                                                                                                                                           |
| `GET_CURRENT_CONTRACT`          | Information about the current RAP contract.                                                                                                                                                                                                                                                    |
| `GET_PRIVILEGED_ACCESS_PROFILE` | Information about the privileged context. It can be used for the save phase only.                                                                                                                                                                                                              |

## Hint

Regarding `GET_CURRENT_CONTEXT`:

- In the [RAP early save phase](../../abap-glossary/abenearly_rap_save_phase_glosry.md) and [RAP late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md) it makes no sense to evaluate the components other than `from_projection`.

- The `for_permissions` parameter can be used to avoid a double checking of authorization or feature control if an ABAP EML modify request is handled.

- The `from_behavior` parameter returns the name of the RAP BO currently active beneath the current RAP BO in the stack. If no such BO exists, as in a UI scenario, the returned value is initial. This parameter is typically relevant in the context of dependent RAP BOs and in cases where the called RAP BO has a different behavior based on the calling RAP BO.

- Example use cases for the context information:

  - When a behavior is accessed via a [RAP interface behavior definition](../../abap-glossary/abencds_interface_bdef_glosry.md), this access is directly mapped to a request on the [base RAP business object](../../abap-glossary/abenrap_projected_bo_glosry.md). A use case might be that the base BO implementation would like to have the information available that it has been called via a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md). For example, a RAP BO interface implements specific logic (for example, some fields are dynamically set to read-only) in the base BO's behavior pool. The implementation in the base BO then requires the name of the RAP BO interface which can be retrieved using the methods of this class.

  - Similarly, the base BO implementation might be interested in knowing whether it was invoked by a [RAP projection extension entity](../../abap-glossary/abenrap_proj_ext_entity_glosry.md).

Regarding `GET_PRIVILEGED_ACCESS_PROFILE`:

Note the following implementation situations to ensure RAP contract compliance:

- If all ABAP EML modify accesses were privileged during the modify phase, the privileged authorization context is automatically active in the early save phase. An early save disabling context may be added, following the appropriate specification in the BDEF.

- If at least one ABAP EML modify access was non-privileged, implementing an authorization check in the early save phase is allowed and does not violate the RAP contract. The `GET_PRIVILEGED_ACCESS_PROFILE` method of the `CL_ABAP_BEHV_AUX` class can be used in the early save phase to evaluate whether previous modify accesses are privileged or non-privileged. Implementations can then respond accordingly to maintain RAP contract compliance. For example, if the `GET_PRIVILEGED_ACCESS_PROFILE` method returns `only_privileged` (see `CL_ABAP_BEHV_AUX=>T_PRIVILEGED_ACCESS`), and the application would otherwise perform an `AUTHORITY-CHECK` with an object that is not disabled by the privileged context, the authorization check using `AUTHORITY-CHECK` can be skipped at this stage.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code snippet shows how information on the current context might be retrieved using the `GET_CURRENT_CONTEXT` method by storing the information in a variable [declared inline](../../abap-glossary/abeninline_declaration_glosry.md).

``` abap
cl_abap_behv_aux=>get_current_context( IMPORTING 
      from_behavior   = FINAL(fr_behv) 
      from_projection = FINAL(fr_proj) 
      from_interface  = FINAL(fr_int) 
      in_local_mode   = FINAL(loc_mode) 
      draft_activate  = FINAL(dr_act) 
      for_permissions = FINAL(for_perm) 
      privileged      = FINAL(priv) 
      call_kind       = FINAL(call) ).
```

## Executable Examples

- The example [Getting RAP Context Information Using `CL_ABAP_BEHV_AUX`](abenrap_cl_abap_behv_aux_abexa.md) demonstrates the use of methods of the class `CL_ABAP_BEHV_AUX`, focusing on filling specific parameters in multiple contexts.

- The example [Using the Addition `PRIVILEGED` with an ABAP EML Statement](abeneml_privileged_abexa.md) demonstrates the addition `PRIVILEGED` using an [action](../../abap-glossary/abenrap_action_glosry.md) and a managed RAP BO. In this example, the method `get_current_context` is used to retrieve the information whether the running handler is running in privileged mode.

- The example [Checking RAP Transactional Phases](abenrap_cl_abap_behv_aux_ph_abexa.md) demonstrates the methods `GET_CURRENT_PHASE` and `GET_CURRENT_HANDLER_KIND`.

- The executable example class `CL_DEMO_RAP_FROM_BEHAVIOR_PAR` illustrates the `from_behavior` parameter of the `get_current_handler_kind` method in the `CL_ABAP_BEHV_AUX` class. The [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) `DEMO_EXT_M` specifies the function `demo_from_behv_a`, and the RAP BO `DEMO_MANAGED_ROOT_CUSTOM` specifies `demo_from_behv_b`. Both functions use `READ ENTITIES` statements to fetch data from the same RAP BO and another RAP BO by executing the function. In the implementations, the `get_current_handler_kind` method of the `CL_ABAP_BEHV_AUX` class is called, and the value of `from_behavior` is stored and added to the read result. The example demonstrates when the value is initial and when it is filled with the currently active RAP BO beneath the current RAP BO in the stack.
