---
title: "METHODS, FOR ENTITY EVENT"
source_file: abenmethod_for_entity_event.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for RAP Business Events"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# METHODS, FOR ENTITY EVENT

## Syntax

``` abap
**RAP event handler method definitions:**

METHODS meth [FINAL] 
   FOR ENTITY EVENT [IMPORTING  ] { REFERENCE  (der_type) | der_type } FOR ent~evt.  

**RAP event handler method implementations:**

METHOD meth. 
   ... 
ENDMETHOD.  
```

[`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`FINAL`](../../abap-programming-language/abap-declarations/abapmethods_abstract_final.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`METHOD`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`ENDMETHOD`](../../abap-programming-language/abap-declarations/abapmethods.md)

## Description

[RAP event handler methods](../../abap-glossary/abenrap_event_handler_meth_glosry.md) must be defined and implemented in the private [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) of a [local class](../../abap-glossary/abenlocal_class_glosry.md), which is implemented in the [CCIMP include](../../abap-glossary/abenccimp_glosry.md) of a [RAP event handler class](../../abap-glossary/abenrap_event_handler_class_glosry.md). The local class must inherit from `CL_ABAP_BEHAVIOR_EVENT_HANDLER`.

When a RAP business event is raised using a [`RAISE ENTITY EVENT`](abapraise_entity_event.md) ABAP EML statement, the RAP event handler methods are called locally in the system and processed asynchronously.

The following points are relevant concerning the syntax:

- RAP event handler methods must be defined as [instance methods](../../abap-glossary/abeninstance_method_glosry.md) using the `METHODS` keyword.

- The method name `meth` can be freely chosen.

- `der_type` specifies the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md). It is an internal table of type [`TYPE TABLE FOR EVENT`](abaptype_table_for.md). If the event is specified with parameters, the BDEF derived type `der_type` contains the keys of [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) ([`%key`](abapderived_types_key.md)) for which an event has been raised, along with the parameters ([`%param`](abapderived_types_param.md)). If the event is specified without parameters, `der_type` contains only the keys. If the RAP event handler class is related to a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), then the keys and parameters are those used in the [interface BDEF](../../abap-glossary/abencds_interface_bdef_glosry.md).

  - The name of `der_type` can be chosen freely.

  - The BDEF derived type is [passed by reference](../../abap-glossary/abenpass_by_reference_glosry.md). Therefore, instead of just specifying the name of the [formal parameter](../../abap-glossary/abenformal_parameter_glosry.md) `der_type`, the syntax can also be `... REFERENCE(der_type) ...`.

- The methods are implicitly final, and only importing parameters are possible. The specification of the additions [`FINAL`](../../abap-programming-language/abap-declarations/abapclass_options.md) and [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) is optional.

- `ent` specifies the name of a [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md). The events handled by the class must be defined in the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md). `ent` can also be the name of an [interface BDEF](../../abap-glossary/abencds_interface_bdef_glosry.md) that exposes events.

- The name of the RAP BO entity (or interface BDEF) `ent` is followed by a tilde and the (alias) name of the event `evt`.

For modularization purposes, a single RAP event handler method can handle multiple events. The following code snippet demonstrates the definition of a method that handles three events defined in the BDEF.

``` abap
METHODS on_evt FOR ENTITY EVENT 
  evt1_type FOR ent~evt1 
  evt2_type FOR ent~evt2 
  evt3_type FOR ent~evt3.
```

## Hints

- In a RAP event handler class, a RAP business event can be handled only once, i.e. specifying the parameter for an event in event handler methods more than once is not allowed.

- Unlike [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) and [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md), RAP event handler methods do not contain [RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md) as implicit changing parameters.

- The syntax `... FOR EVENT ... FOR` for event handler method declarations is obsolete. Using this syntax generates a syntax warning.

- Method declarations using this syntax are not to be confused with method declarations in the context of non-RAP [events](../../abap-glossary/abenevent_glosry.md): [`METHODS, FOR EVENT`](../../abap-programming-language/abap-declarations/abapmethods_event_handler.md).

- When event handler methods are called, they run through their own RAP transaction, i.e. when they are called, the current phase is the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md). In general, implementations in event handler methods must fulfill the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md) to guarantee transactional consistency. Therefore, implementations can be included in the event handler method that are allowed in the RAP interaction phase right away. However, if your use case requires implementations in such a method that are reserved for the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) and must not occur in the RAP interaction phase, for example, database modifications using ABAP SQL, you must explicitly switch in the event handler method implementation to the RAP save sequence by calling [`cl_abap_tx=>save( ).`](../../abap-programming-language/abap-database-access/abaprap_cl_abap_tx.md). Otherwise, a runtime error occurs. For more information, refer to [Restrictions in Transactional Phases](../../abap-programming-language/abap-database-access/abapinvalid_stmts_in_tx.md). When performing RAP modify operations in RAP event handler implementations, it is recommended that you catch the `CX_ABAP_BEHV_SAVE_FAILED` exception, allowing you to react on errors caused in the [RAP early save phase](../../abap-glossary/abenearly_rap_save_phase_glosry.md) or [RAP late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md).

- Since calling `cl_abap_tx=>save( ).` starts the *save* transactional phase, note the following aspects:

  - In a RAP transaction, if the transaction owner, such as an ABAP program, starts the *save* phase without a `COMMIT ENTITIES` statement to initiate the RAP save sequence, it is recommended that you include the `cl_abap_tx=>save( ).` call within a `TRY` block to catch `CX_ABAP_BEHV_SAVE_FAILED`.

  - This exception occurs if saving fails during the early or late save phases. Catching `CX_ABAP_BEHV_SAVE_FAILED` gives access to attributes like `FAILED_ENTITIES` and `REPORTED_ENTITIES`, which list entries added to the RAP response parameters. Errors causing entries in the failed response can result from failed RAP BO instance validations in the early save phase.

  - Generally, exceptions must not leave RAP handler methods, except for RAP event handler methods.

- Calling `cl_abap_tx=>save( ).` in RAP event handler implementations

  - When RAP event handlers are called, they start in the *modify* transactional phase. Database changes in transactional scenarios require starting the *save* transactional phase. If you need to modify and save RAP BO instances in RAP event handlers, calling `cl_abap_tx=>save( ).` is necessary. Explicit `COMMIT ENTITIES` statements are typically not allowed in handler methods.

  - By catching `CX_ABAP_BEHV_SAVE_FAILED`, you can prevent short dumps and take actions in RAP handler method implementations such as:

  - It is not recommended that you perform cleanup tasks on the transactional buffer - such as correcting failed RAP BO instances and restarting the save - especially when raising custom exceptions.

  - Instead, consider logging the errors to an application log.

  - You can raise custom exceptions inheriting from `CX_ABAP_BEHV_EVENT_HDLR_ERROR` in the `CATCH` block. You can also optionally wrap the raised `CX_ABAP_BEHV_SAVE_FAILED` exception in the `previous` attribute. The raised exceptions are reported to the event framework. **Note:** If corrective tasks are performed for another save, no persistence occurs due to an implicit rollback when raising the custom exception.

  - Only exceptions inheriting from `CX_ABAP_BEHV_EVENT_HDLR_ERROR` may leave RAP event handler method implementations.

- Local events may not execute due to temporary issues like locks, such as those for draft instances. An automatic retry feature can handle these situations, with the framework attempting a restart up to three times. Notes on the automatic retry feature:

  - In your RAP event handler method, you may identify potential error situations that could prevent successful event execution. The issue, such as temporary locks on instances, might resolve over time.

  - You can design your implementation to let the framework automatically retry the event execution after a specified time. To achieve this, you can create custom exceptions that inherit from `CX_RAP_EVENT_HDLR_ERROR_RETRY`, and raise these exceptions, for example, in the `CATCH` block when handling certain exceptions in your code. If a retry is not needed, you can create custom exceptions that inherit from `CX_RAP_EVENT_HDLR_ERROR`. AIF logging is possible in both cases if it is enabled.

  - The instance constructor of the `CX_RAP_EVENT_HDLR_ERROR_RETRY` exception class includes the importing parameter `delay_time`, which allows you to specify the delay for the next automatic execution. This formal parameter expects an integer value and represents the delay in seconds. The framework then makes up to three execution attempts, respecting the specified delay each time.

- In addition to consuming RAP business events locally using RAP handler methods, RAP business events can also be consumed outside of the system using the RAP event binding.

## More Information

Development guide for the ABAP RESTful Application Programming Model, section about [RAP Business Events](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/0b925bc556d4491aad395b21ec2566ff?version=sap_cross_product_abap).
