---
title: "%foreign"
source_file: abapderived_types_foreign.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Components Related to Information Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %foreign

`%foreign` is a [component group](../../abap-glossary/abencomponent_group_glosry.md) in [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). The component group is contained in the `REPORTED` [RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md) in the context of the [`map_messages`](abensaver_map_messages.md) saver method and summarizes all available [foreign entities](../../abap-glossary/abenrap_foreign_entity_glosry.md) defined in the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md).

**Type**

The subcomponents of `%foreign` are internal tables of type [`TYPE TABLE FOR REPORTED LATE`](abaptype_table_for.md).

**Where used**

- [`TYPE RESPONSE FOR REPORTED LATE`](abaptype_response_for.md)

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Message Mapping](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/741dfc88293d4ac99186815b9fc35e31?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section is taken from here: `BP_DEMO_UNMANAGED_MAP_MESSAGESCCIMP`. The global class of the [behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is `BP_DEMO_UNMANAGED_MAP_MESSAGES`. It demonstrates the component group `%foreign` in the context of a `map_messages` method implementation that is responsible for processing the responses of a foreign entity. See the executable program for this example further down.

``` abap
METHOD map_messages. 
 
  LOOP AT reported-%foreign-demo_unmanaged_foreign_entity 
    ASSIGNING FIELD-SYMBOL(<src>). 
    "Adapt message from foreign entity. 
    <src>-%msg = new_message_with_text( 
             severity  = if_abap_behv_message=>severity-information 
             text      = |Foreign entity: Instance with | && 
                         |key { <src>-key_field } was saved.| ). 
 
    "Insert changed messages into REPORTED table of the exposed BO. 
    INSERT VALUE #( key_field = <src>-%key-key_field 
                    %msg = <src>-%msg 
                  ) INTO TABLE reported-demo_unmanaged_map_messages. 
  ENDLOOP. 
 
  "You can delete the original messages to remove them from the external result. 
  CLEAR reported-%foreign-demo_unmanaged_foreign_entity. 
 
ENDMETHOD.
```

## Executable Example

The example [Example for RAP Saver Method `map_messages`](abenabp_map_messages_abexa.md) demonstrates the use of `%foreign` in the context of the implementation of a `map_messages` saver method within a RAP saver class using unmanaged RAP BOs.
