---
title: "%state_area"
source_file: abapderived_types_state_area.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Components Related to Information Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %state_area

## Use

`%state_area` is a component of [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). It is a [character string](../../abap-glossary/abencharacter_string_glosry.md) of type [`string`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) and used as a component of the `REPORTED` [RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md), which is filled by the [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md).

If this component is filled, the framework interprets a message as [state message](../../abap-glossary/abenrap_state_mes_glosry.md). Otherwise, a message is interpreted as a [transition message](../../abap-glossary/abenrap_trans_mes_glosry.md).

In ABAP EML, state messages can only be accessed via an ABAP EML [`READ`](abapread_entity_short.md) statement. In this case, the `%state_area` component is filled with the value `%STATE`. In all other ABAP EML statements, the [`reported`](abaptype_response_for.md) response parameter only contains transition messages.

The `%state_area` component is mainly relevant in the following contexts:

- [draft](../rap-behavior-definitions/abenbdl_with_draft.md) scenarios because state messages are persisted until the state of the RAP BO is changed. The string provided is not relevant for the [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md). The RAP BO consumer is only interested in transition messages.

- [`finalize`](abensaver_finalize.md) and [`check_before_save`](abensaver_check_before_save.md) RAP saver methods in [unmanaged RAP business objects](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- [RAP determinations](../../abap-glossary/abenrap_determination_glosry.md) and [validations](../../abap-glossary/abenrap_validation_glosry.md) in [managed RAP business objects](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

**Note:** You must manually invalidate state messages, i. e. remove the assignment of persisted messages, in the RAP BO provider implementation. To identify the messages, use the respective key ([`%tky`](abapderived_types_tky.md)) and `%state_area` string.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows the manual invalidation of a state message.

``` abap
APPEND VALUE #( %tky        = instance-%tky 
                %state_area = `STATE_AREA_NAME` ) 
TO reported-rap_bo_entity.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

You can also use a constant to invalidate all state messages for an instance:

``` abap
APPEND VALUE #( %tky        = instance-%tky 
                %state_area = if_abap_behv=>state_area_all ) 
TO reported-rap_bo_entity.
```

**Type**

The component has the following type: `STRING`

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- `REPORTED [EARLY|LATE]`

## More Information

See more details on message handling in the Development Guide for the ABAP RESTful Application Programming Model, section [Messages](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/ac74189b5cae49c1b091f04393bac069?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section is taken from here: `BP_DEMO_MANAGED_ROOT_REPORTED=CCIMP`. The global class of the [behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is `BP_DEMO_MANAGED_ROOT_REPORTED`. The code example demonstrates the component `%state_area` in the context of a method implementation for a [validation](../rap-behavior-definitions/abenbdl_validations.md) that checks field values of RAP BO instances before saving. See the executable program for this example further down.

``` abap
METHOD ValidateNum. 
 
  READ ENTITIES OF demo_managed_root_reported IN LOCAL MODE 
   ENTITY demo_managed_child_reported 
      FIELDS ( key_field key_field_child ch_field3 ) 
      WITH CORRESPONDING #( keys ) 
   RESULT DATA(lt_child_result) 
   FAILED DATA(lt_child_failed). 
 
  failed =  CORRESPONDING #( DEEP lt_child_failed ). 
 
  READ ENTITIES OF demo_managed_root_reported IN LOCAL MODE 
   ENTITY demo_managed_child_reported BY \_parent 
      FIELDS ( key_field field3 field4  ) 
      WITH CORRESPONDING #( lt_child_result ) 
   RESULT DATA(lt_root_result) 
   FAILED DATA(lt_root_failed). 
 
  failed =  CORRESPONDING #( DEEP BASE ( failed ) lt_root_failed  ). 
 
  LOOP AT lt_child_result ASSIGNING FIELD-SYMBOL(<fs_child>). 
    ASSIGN lt_root_result[ KEY entity COMPONENTS 
     key_field = <fs_child>-key_field ] TO FIELD-SYMBOL(<fs_root>). 
 
    "Invalidate state area. 
    APPEND VALUE #( %tky        = <fs_child>-%tky 
                    %state_area = 'VALIDATE_NUMBERS' ) 
                    TO reported-%own-demo_managed_child_reported. 
 
    IF <fs_child>-ch_field3 NOT BETWEEN <fs_root>-field3 
                                    AND <fs_root>-field4. 
 
      "Fill FAILED 
      APPEND VALUE #( %tky = <fs_child>-%tky ) 
      TO failed-demo_managed_child_reported. 
      "Fill REPORTED 
      APPEND VALUE #( 
        %tky = <fs_child>-%tky 
        %state_area = 'VALIDATE_NUMBERS' 
        %path = VALUE #( demo_managed_root_reported-key_field = 
                         <fs_child>-key_field ) 
        %msg =  new_message_with_text( 
                 severity = if_abap_behv_message=>severity-error 
                 text   = 'Validation failed' ) 
        %element-ch_field3 = if_abap_behv=>mk-on ) 
        TO reported-%own-demo_managed_child_reported. 
 
    ENDIF. 
 
  ENDLOOP. 
 
  "Get time stamp 
  DATA: ts1 TYPE timestampl. 
  GET TIME STAMP FIELD ts1. 
 
  "Fill %OTHER 
  reported-%other = VALUE #( 
    ( new_message_with_text( 
       severity = if_abap_behv_message=>severity-information 
       text   = |b) Unbound message set at { ts1 TIMESTAMP = ISO }.| 
    ) ) ). 
 
ENDMETHOD.
```

## Executable Example

- The example [Example for message-related BDEF derived type components](abenderived_types_reported_abexa.md) demonstrates the use of various BDEF derived type components including `%state_area` with a managed RAP BO.

- [RAP Messages: Transition and State Messages](abenrap_messages_abexa.md)
