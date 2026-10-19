---
title: "%path"
source_file: abapderived_types_path.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Components Related to Information Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %path

## Use

`%path` is a component of [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). It is used as a component of the `REPORTED` [RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md).

`%path` can only be used for [child entities](../../abap-glossary/abenchild_entity_glosry.md). The component maps a child entity to its parent. If there is a business object with multiple child entities, `%path` is extended to map the child entity to its [parent](../../abap-glossary/abenparent_entity_glosry.md) and the [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md). The component must be filled for all child entities of a root entity to explicitly map child entities to the parents.

**Type**

Structure whose components are nested structures named according to the child entities. The components of these structures are [`%key`](abapderived_types_key.md) and, if relevant and depending on the context, other `%` components like [`%pid`](abapderived_types_pid.md).

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- `REPORTED [EARLY|LATE]`

## More Information

See more details on message handling in the Development Guide for the ABAP RESTful Application Programming Model, section [Messages](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/ac74189b5cae49c1b091f04393bac069?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section is taken from here: `BP_DEMO_MANAGED_ROOT_REPORTED=CCIMP`. The global class of the [behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is `BP_DEMO_MANAGED_ROOT_REPORTED`. The code example demonstrates the component `%path` in the context of a method implementation for a [validation](../rap-behavior-definitions/abenbdl_validations.md) that checks field values of RAP BO instances before saving. See the executable program for this example further down.

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

The example [Example for Message-Related BDEF Derived Type Components](abenderived_types_reported_abexa.md) demonstrates the use of various BDEF derived type components including `%path` with a managed RAP BO.
