---
title: "map_messages, RAP Saver Method"
source_file: abensaver_map_messages.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Saver Class and Methods > RAP Saver Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# map_messages, RAP Saver Method

## Syntax

``` abap
Declaration part:

CLASS lsc_bdef DEFINITION INHERITING FROM base_class ... 
     ... 
     METHODS map_messages REDEFINITION. 
     ... 
ENDCLASS.  

Implementation part:

CLASS lsc_bdef IMPLEMENTATION. 
      ... 
      METHOD map_messages. 
      ... 
      ENDMETHOD 
      ... 
ENDCLASS.  
```

[`CLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`DEFINITION`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`INHERITING FROM`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`REDEFINITION`](../../abap-programming-language/abap-declarations/abapmethods_redefinition.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`CLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`IMPLEMENTATION`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`METHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDMETHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md)

## Description

[RAP saver method](../../abap-glossary/abenabp_saver_method_glosry.md) that is declared as part of a [RAP saver class](../../abap-glossary/abenabp_saver_class_glosry.md) `lsc_bdef` in the [CCIMP include](../../abap-glossary/abenccimp_glosry.md) of an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). The predefined saver method must be redefined.

`base_class` stands for the base class from which the RAP saver class inherits, for example, `CL_ABAP_BEHAVIOR_SAVER`.

The following points are relevant for this RAP saver method:

- Its use is optional.

- It has the following implicit, predefined [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - [`reported`](abaptype_response_for.md): [RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md) that is of type [`TYPE RESPONSE FOR REPORTED LATE`](abaptype_response_for.md).

- It is available in [behavior pools](../../abap-glossary/abenbehavior_pool_glosry.md) for those [RAP BOs](../../abap-glossary/abenrap_bo_glosry.md) whose [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md) includes BOs that are defined as [foreign entities](../../abap-glossary/abenrap_foreign_entity_glosry.md).

- Its purpose is to handle messages of foreign entities, i. e. entities that are not directly exposed, within one [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md). Depending on your business requirements, these messages might be available for the exposed RAP BO and mapped to the business context or just ignored and deleted.

- If a RAP BO is defined as foreign entity in a BDEF, the responses in the [`reported`](abaptype_response_for.md) parameter of the exposed RAP BO also contain this foreign entity as a component allowing the messages returned by the foreign entity to be mapped to the business context of the exposed RAP BO.

- It is called in the [RAP early save phase](../../abap-glossary/abenearly_rap_save_phase_glosry.md) if the RAP BOs that are defined as foreign entities return [RAP transition messages](../../abap-glossary/abenrap_trans_mes_glosry.md) in the `reported` [response parameter](../../abap-glossary/abenrap_response_param_glosry.md) in their respective saver class. Note that [RAP state messages](../../abap-glossary/abenrap_state_mes_glosry.md) cannot be mapped in the save phase.

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Message Mapping](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/741dfc88293d4ac99186815b9fc35e31?version=sap_cross_product_abap).

## Executable Example

The example [Example for RAP Saver Method `map_messages`](abenabp_map_messages_abexa.md) demonstrates this RAP saver method within a RAP saver class using unmanaged RAP BOs.
