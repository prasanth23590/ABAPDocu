---
title: "CL_ABAP_BEHAVIOR_SAVER_FAILED, RAP Saver Class"
source_file: abenabp_cl_abap_beh_saver_failed.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Saver Class and Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_BEHAVIOR_SAVER_FAILED, RAP Saver Class

## Syntax

``` abap
Syntax for unmanaged scenarios. The adjust_numbers   method is only available for late numbering   scenarios. See more methods that can be implemented here.

CLASS lsc_bdef DEFINITION 
  INHERITING FROM CL_ABAP_BEHAVIOR_SAVER_FAILED   [ABSTRACT] [FINAL]. 
  PROTECTED SECTION. 
      ... 
      METHODS adjust_numbers   REDEFINITION. 
      METHODS save   REDEFINITION. 
      ... 
ENDCLASS. 
 
CLASS lsc_bdef IMPLEMENTATION. 
      ... 
      METHOD adjust_numbers. ... ENDMETHOD. 
      METHOD save. ... ENDMETHOD. 
      ... 
ENDCLASS.  

Syntax for managed scenarios with additional or unmanaged save. See more methods that can be implemented here.

CLASS lsc_bdef DEFINITION 
  INHERITING FROM CL_ABAP_BEHAVIOR_SAVER_FAILED   [ABSTRACT] [FINAL]. 
  PROTECTED SECTION. 
      ... 
     METHODS adjust_numbers   REDEFINITION. 
     METHODS save_modified   REDEFINITION. 
      ... 
ENDCLASS. 
 
CLASS lsc_bdef IMPLEMENTATION. 
      ... 
      METHOD adjust_numbers. ... ENDMETHOD. 
      METHOD save_modified. ... ENDMETHOD. 
      ... 
ENDCLASS.  
```

[`unmanaged`](../rap-behavior-definitions/abenbdl_impl_type.md) · [`late numbering `](../rap-behavior-definitions/abenbdl_late_numbering.md) · [`here`](abenabp_cl_abap_beh_handler.md) · [`CLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`DEFINITION`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`INHERITING FROM`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`CL_ABAP_BEHAVIOR_SAVER_FAILED`](abenabp_cl_abap_beh_saver_failed.md) · [`ABSTRACT`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`FINAL`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`PROTECTED SECTION`](../../abap-programming-language/abap-declarations/abapprotected.md) · [`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`adjust_numbers`](abensaver_adjust_numbers.md) · [`REDEFINITION`](../../abap-programming-language/abap-declarations/abapmethods_redefinition.md) · [`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`save `](abensaver_method_save.md) · [`REDEFINITION`](../../abap-programming-language/abap-declarations/abapmethods_redefinition.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`CLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`IMPLEMENTATION.`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`METHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDMETHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`METHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDMETHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`additional or unmanaged save`](../rap-behavior-definitions/abenbdl_saving.md) · [`here`](abenabp_cl_abap_beh_handler.md) · [`CLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`DEFINITION`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`INHERITING FROM`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`CL_ABAP_BEHAVIOR_SAVER_FAILED`](abenabp_cl_abap_beh_saver_failed.md) · [`ABSTRACT`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`FINAL`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`PROTECTED SECTION`](../../abap-programming-language/abap-declarations/abapprotected.md) · [`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`adjust_numbers`](abensaver_adjust_numbers.md) · [`REDEFINITION`](../../abap-programming-language/abap-declarations/abapmethods_redefinition.md) · [`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`save_modified`](abaprap_saver_meth_save_modified.md) · [`REDEFINITION`](../../abap-programming-language/abap-declarations/abapmethods_redefinition.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`CLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`IMPLEMENTATION.`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`METHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDMETHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`METHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDMETHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md)

## Description

Used as base class from which a [RAP saver class](../../abap-glossary/abenabp_saver_class_glosry.md) `lsc_bdef` in an [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) inherits. The RAP saver class must be defined in the [CCIMP include](../../abap-glossary/abenccimp_glosry.md) of an ABP.

Mandatory [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md) must be implemented. Optional RAP saver methods can be implemented. The RAP saver methods are declared by redefining predefined methods of the [superclass](../../abap-glossary/abensuperclass_glosry.md). They implicitly have [RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md).

RAP saver classes are implicitly [`ABSTRACT`](../../abap-programming-language/abap-declarations/abapclass_options.md) and [`FINAL`](../../abap-programming-language/abap-declarations/abapclass_options.md) since instantiating and calling only happens through the [RAP runtime engine](../../abap-glossary/abenrap_runtime_engine_glosry.md). All saver methods are called after at least one successful modification of data in the current [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md) following the triggering of the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md), for example, by an explicit [`COMMIT ENTITIES`](abapcommit_entities.md) statement. In contrast to [RAP handler methods](abapmethods_for_rap_behv.md), saver methods do not have data of [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) as import parameter (except for the [`save_modified`](abaprap_saver_meth_save_modified.md) method). Therefore, instance data must be handled via the [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md) when self-implementing the saver methods.

Normally, the basic rule is that failures must not occur in the [RAP late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md), but must be detected in the [RAP early save phase](../../abap-glossary/abenearly_rap_save_phase_glosry.md) in order for the save to be successful. The base class `CL_ABAP_BEHAVIOR_SAVER_FAILED` can be used in exceptional cases where the basic rule cannot be met.

Unlike when using the default base class `CL_ABAP_BEHAVIOR_SAVER`, when using `CL_ABAP_BEHAVIOR_SAVER_FAILED`,the [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md) [`adjust_numbers`](abensaver_adjust_numbers.md) (for [late numbering](../../abap-glossary/abenrap_late_numbering_glosry.md) scenarios), [`save`](abensaver_method_save.md) (for unmanaged RAP BOs) and [`save_modified`](abaprap_saver_meth_save_modified.md) (for managed RAP BOs that include a RAP saver class in their implementation) include the [RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md) `failed` and `reported`.

If errors occur in the late save phase, runtime errors due to a violation of the above basic rule can be avoided. [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md) can be informed by filling the RAP response parameters in the method implementation so that they can react accordingly.

One way to retrieve the response in the RAP BO consumer is to use the [long form](abapemlcommit_entities_long.md) of the `COMMIT ENTITIES` statement. The current [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md) is inconsistent if an error occurs in the late save phase. All changes must be rolled back to the last consistent state using a [`ROLLBACK ENTITIES`](abaprollback_entities.md) statement if the RAP BO consumer is to continue with ABAP EML requests after the error. Otherwise, exception `CX_SADL_DUMP_APPL_MODEL_ERROR` is raised.

## Hints

- It is recommended that the use of `CL_ABAP_BEHAVIOR_SAVER_FAILED` is reserved for exceptional cases only, as there is a risk of data inconsistency when multiple RAP BOs are involved.

  - An exceptional case may be when [BAPIs](../../abap-glossary/abenbapi_glosry.md) are included in the runtime of the RAP BO and are called to save RAP BO instances in the late save phase. Such BAPIs can be designed to include the validation and saving of data in one go. However, if such a BAPI is called in the late save phase, a validation is usually too late and a RAP BO consumer cannot react to potential errors.

  - Regarding late numbering scenarios in such an exceptional case: The RAP saver method [`adjust_numbers`](abensaver_adjust_numbers.md) is responsible for converting preliminary keys and identifiers (e. g. [`%pid`](abapderived_types_pid.md)) to the final key values of [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md). The final key values must be returned here, hence, the `save` (or `save_modified`) method is too late in such a case. As a solution, the BAPI request that includes the saving part is to be done in the `adjust_numbers` method.

- After a [`COMMIT ENTITIES`](abapcommit_entities.md) statement of a RAP BO consumer that triggers the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) and when a failure occurs in the late save phase, `sy-subrc` is set to 8.

- This base class from which the RAP saver class inherits must be manually implemented. [ADT](../../abap-glossary/abenadt_glosry.md) automatically creates the saver class using `CL_ABAP_BEHAVIOR_SAVER`.

- The use of `CL_ABAP_BEHAVIOR_SAVER_FAILED` is restricted to redefining RAP saver methods in a behavior pool.

- Only one RAP saver class can be implemented for a RAP BO.

- The RAP saver method `adjust_numbers` contains the RAP response parameter `reported` in any case. When this base class is used, the additional parameter `failed` is available.

## Executable Example

The [Example for `CL_ABAP_BEHAVIOR_SAVER_FAILED`](abencl_abap_beh_saver_failed_abexa.md) demonstrates the base class using a managed RAP BO whose BDEF is specified with `with unmanaged save`.
