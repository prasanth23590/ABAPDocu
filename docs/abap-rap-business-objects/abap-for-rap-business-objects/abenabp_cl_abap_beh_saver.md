---
title: "CL_ABAP_BEHAVIOR_SAVER, RAP Saver Class"
source_file: abenabp_cl_abap_beh_saver.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Saver Class and Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_BEHAVIOR_SAVER, RAP Saver Class

## Syntax

Syntax for [unmanaged scenarios](../rap-behavior-definitions/abenbdl_impl_type.md). The `adjust_numbers` method is only available for [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) scenarios.

``` abap
CLASS lsc_bdef DEFINITION 
  INHERITING FROM CL_ABAP_BEHAVIOR_SAVER   [ABSTRACT] [FINAL]. 
  PROTECTED SECTION. 
     [METHODS finalize   REDEFINITION.] 
     [METHODS check_before_save   REDEFINITION.] 
      METHODS adjust_numbers   REDEFINITION. 
      METHODS save   REDEFINITION. 
     [METHODS map_messages   REDEFINITION.] 
     [METHODS cleanup   REDEFINITION.] 
     [METHODS cleanup_finalize   REDEFINITION.] 
ENDCLASS. 
 
CLASS lsc_bdef IMPLEMENTATION. 
     [METHOD finalize. ... ENDMETHOD.] 
     [METHOD check_before_save. ... ENDMETHOD.] 
      METHOD adjust_numbers. ... ENDMETHOD. 
      METHOD save. ... ENDMETHOD. 
     [METHOD map_messages. ... ENDCLASS.] 
     [METHOD cleanup. ... ENDMETHOD.] 
     [METHOD cleanup_finalize. ... ENDMETHOD.] 
ENDCLASS.  
```

Syntax for managed scenarios with [additional or unmanaged save](../rap-behavior-definitions/abenbdl_saving.md). The `adjust_numbers` method is only available for [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) scenarios.

``` abap
CLASS lsc_bdef DEFINITION 
  INHERITING FROM CL_ABAP_BEHAVIOR_SAVER   [ABSTRACT] [FINAL]. 
  PROTECTED SECTION. 
     METHODS adjust_numbers   REDEFINITION. 
     METHODS save_modified   REDEFINITION. 
    [METHODS cleanup REDEFINITION.] 
ENDCLASS. 
 
CLASS lsc_bdef IMPLEMENTATION. 
      METHOD adjust_numbers. ... ENDMETHOD. 
      METHOD save_modified. ... ENDMETHOD. 
     [METHOD cleanup. ... ENDMETHOD.] 
ENDCLASS.  
```

[`unmanaged`](../rap-behavior-definitions/abenbdl_impl_type.md) · [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) · [`CLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`DEFINITION`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`INHERITING FROM`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`CL_ABAP_BEHAVIOR_SAVER`](abenabp_cl_abap_beh_saver.md) · [`ABSTRACT`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`FINAL`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`PROTECTED SECTION`](../../abap-programming-language/abap-declarations/abapprotected.md) · [`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`finalize`](abensaver_finalize.md) · [`REDEFINITION`](../../abap-programming-language/abap-declarations/abapmethods_redefinition.md) · [`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`check_before_save`](abensaver_check_before_save.md) · [`REDEFINITION`](../../abap-programming-language/abap-declarations/abapmethods_redefinition.md) · [`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`adjust_numbers`](abensaver_adjust_numbers.md) · [`REDEFINITION`](../../abap-programming-language/abap-declarations/abapmethods_redefinition.md) · [`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`save`](abensaver_method_save.md) · [`REDEFINITION`](../../abap-programming-language/abap-declarations/abapmethods_redefinition.md) · [`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`map_messages`](abensaver_map_messages.md) · [`REDEFINITION`](../../abap-programming-language/abap-declarations/abapmethods_redefinition.md) · [`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`cleanup `](abensaver_method_cleanup.md) · [`REDEFINITION`](../../abap-programming-language/abap-declarations/abapmethods_redefinition.md) · [`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`cleanup_finalize`](abapsaver_class_cleanup_finalize.md) · [`REDEFINITION`](../../abap-programming-language/abap-declarations/abapmethods_redefinition.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`CLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`IMPLEMENTATION.`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`METHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDMETHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`METHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDMETHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`METHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDMETHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`METHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDMETHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`METHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`METHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDMETHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`METHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDMETHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`additional or unmanaged save`](../rap-behavior-definitions/abenbdl_saving.md) · [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) · [`CLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`DEFINITION`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`INHERITING FROM`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`CL_ABAP_BEHAVIOR_SAVER`](abenabp_cl_abap_beh_saver.md) · [`ABSTRACT`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`FINAL`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`PROTECTED SECTION`](../../abap-programming-language/abap-declarations/abapprotected.md) · [`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`adjust_numbers`](abensaver_adjust_numbers.md) · [`REDEFINITION`](../../abap-programming-language/abap-declarations/abapmethods_redefinition.md) · [`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`save_modified`](abaprap_saver_meth_save_modified.md) · [`REDEFINITION`](../../abap-programming-language/abap-declarations/abapmethods_redefinition.md) · [`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`REDEFINITION`](../../abap-programming-language/abap-declarations/abapmethods_redefinition.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`CLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`IMPLEMENTATION.`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`METHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDMETHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`METHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDMETHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`METHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDMETHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md)

## Description

Used as base class from which a [RAP saver class](../../abap-glossary/abenabp_saver_class_glosry.md) `lsc_bdef` in an [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) inherits. The RAP saver class must be defined in the [CCIMP include](../../abap-glossary/abenccimp_glosry.md) of an ABP.

Mandatory [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md) must be implemented. Optional RAP saver methods can be implemented. The RAP saver methods are declared by redefining predefined methods of the [superclass](../../abap-glossary/abensuperclass_glosry.md). They implicitly have [RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md).

RAP saver classes are implicitly [`ABSTRACT`](../../abap-programming-language/abap-declarations/abapclass_options.md) and [`FINAL`](../../abap-programming-language/abap-declarations/abapclass_options.md) since instantiating and calling only happens through the [RAP runtime engine](../../abap-glossary/abenrap_runtime_engine_glosry.md). All saver methods are called after at least one successful modification of data in the current [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md) following the triggering of the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md), for example, by an explicit [`COMMIT ENTITIES`](abapcommit_entities.md) statement. In contrast to [RAP handler methods](abapmethods_for_rap_behv.md), saver methods do not have data of [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) as import parameter (except for the [`save_modified`](abaprap_saver_meth_save_modified.md) method). Therefore, instance data must be handled via the [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md) when self-implementing the saver methods.

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Save Sequence Runtime](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/ab7459048c7e4ecda98d0b6f51b01e7b?version=sap_cross_product_abap).

## Hints

- The use of `CL_ABAP_BEHAVIOR_SAVER` is restricted to redefining RAP saver methods in a behavior pool.

- Only one RAP saver class can be implemented for a RAP BO.

## Executable Examples

- The example [Example for a RAP Saver Class](abenabp_saver_class_abexa.md) demonstrates RAP saver methods within a RAP saver class using a simple unmanaged RAP BO.

- The example [Example for a RAP Saver Class (Late Numbering)](abenabp_saver_ln_abexa.md) demonstrates RAP saver methods within a RAP saver class using a simple unmanaged RAP BO in late numbering scenario to also include the `adjust_numbers` saver method.

- The example [Example for `save_modified` in a managed RAP BO with additional save](abensave_modified_add_save_abexa.md) demonstrates the `save_modified` method in the context of a simple managed RAP BO whose BDEF is specified with `with additional save`.

- The example [Example for `save_modified` in a managed RAP BO with unmanaged save](abenrap_managed_unm_save_abexa.md) demonstrates the `save_modified` method in the context of a simple managed RAP BO whose BDEF is specified with `with unmanaged save`.
