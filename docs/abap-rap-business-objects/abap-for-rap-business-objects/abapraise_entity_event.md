---
title: "RAISE ENTITY EVENT"
source_file: abapraise_entity_event.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for RAP Business Events"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAISE ENTITY EVENT

## Syntax

``` abap
RAISE ENTITY EVENT ent~evt FROM tab.  
```

## Description

Raises a [RAP business event](../../abap-glossary/abenrap_entity_event_glosry.md). The statement can only be used in [ABAP behavior pools](../../abap-glossary/abenbehavior_pool_glosry.md) by [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md) in the [RAP late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md). Otherwise, the runtime error `BEHAVIOR_ILLEGAL_STATEMENT` occurs.

RAP business events can be raised on the [root node](../../abap-glossary/abenroot_node_glosry.md) and [child node](../../abap-glossary/abenchild_node_glosry.md) level (`ent` is the name of the [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md)). In the case of an extension using an interface, it must be the source name of the BDEF interface. The event `evt` that is raised must be defined in a [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md) or [BDEF extension](../../abap-glossary/abenrap_extension_glosry.md). `tab` is an internal table typed with the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) [`TYPE TABLE FOR EVENT`](abaptype_table_for.md).

The statement triggers the calling of [RAP event handler methods](../../abap-glossary/abenrap_event_handler_meth_glosry.md). The data that is passed in `tab` always includes a [RAP BO instance](../../abap-glossary/abenrap_bo_instance_glosry.md) key of the root entity (component group [`%key`](abapderived_types_key.md)). If the event is defined with parameters, `tab` includes the component groups `%key` and [`%param`](abapderived_types_param.md).

## Hints

- It is recommended that RAP business events are raised by [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md). In managed RAP BOs, it is recommended that a [RAP additional save](../../abap-glossary/abenrap_add_save_glosry.md) is specified using the syntax addition [`with additional save`](../rap-behavior-definitions/abenbdl_saving.md) and raise the RAP business event in the implementation of the [`save_modified`](abaprap_saver_meth_save_modified.md) method.

- If you need to raise a RAP business event outside of the behavior pool, you can create a separate [local class](../../abap-glossary/abenlocal_class_glosry.md) in the behavior pool's [global class](../../abap-glossary/abenglobal_class_glosry.md). In this local class, you can create a [static method](../../abap-glossary/abenstatic_method_glosry.md) where the event raising is wrapped in the implementation part. You can also implement the raising of RAP business event from the associated RAP BO in ABP [ABP auxiliary classes](../../abap-glossary/abenabp_aux_class_glosry.md).

## More Information

- [RAP BDL - event](../rap-behavior-definitions/abenbdl_event.md)

- Development guide for the ABAP RESTful Application Programming Model, section about [RAP Business Events](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/0b925bc556d4491aad395b21ec2566ff?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code snippet demonstrates the implementation of a [`save_modified`](abaprap_saver_meth_save_modified.md) method in which RAP business events are raised for RAP BO instances that are created and deleted. The event for created RAP BO instances is defined without parameters in the BDEF. The event for deleted instances is defined with parameters. Therefore, the [`%param`](abapderived_types_param.md) component group is contained in the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md). In both cases, the internal tables (which have the name of the BDEF) contained in the [deep structures](../../abap-glossary/abendeep_structure_glosry.md) `create` (which is of type [`TYPE REQUEST FOR CHANGE`](abaptype_request_for.md)) and `delete` (which is of type [`TYPE REQUEST FOR DELETE`](abaptype_request_for.md)) as components are looped across using [iteration expressions](../../abap-programming-language/abap-program-flow-logic/abenfor.md) with `FOR` to make sure that events are raised for all relevant instances.

``` abap
... 
CLASS lsc_some_bdef IMPLEMENTATION. 
 
  METHOD save_modified. 
 
   IF create-some_bdef IS NOT INITIAL. 
     "Event defined in BDEF: event created; 
     RAISE ENTITY EVENT some_bdef~created 
       FROM VALUE #( FOR <cr> IN create-some_bdef ( 
         %key = VALUE #( key_field = <cr>-key_field )  ) ). 
   ENDIF. 
 
   IF delete-some_bdef IS NOT INITIAL. 
   "Event defined in BDEF: event deleted parameter some_abstract_entity; 
     RAISE ENTITY EVENT some_bdef~deleted 
       FROM VALUE #( FOR <del> IN delete-some_bdef ( 
         %key   = VALUE #( key_field = <del>-key_field ) 
         %param = VALUE #( par_a = '01' 
                           par_b = 'Item deleted' ) ) ). 
   ENDIF. 
 
  ENDMETHOD. 
 
ENDCLASS.
```

## Executable Example

- [Local Consumption of RAP Business Events (Database Table Modification)](abenrap_events_local_con_abexa.md)
