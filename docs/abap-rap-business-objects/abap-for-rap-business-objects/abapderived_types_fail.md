---
title: "%fail"
source_file: abapderived_types_fail.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Components Related to Information Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %fail

## Use

`%fail` is a component of [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). It is used as a component of the `FAILED` [RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md).

`%fail` is a structure that stores the symptom of a failed [RAP BO](../../abap-glossary/abenrap_bo_glosry.md) instance in the component `cause`. The values of the failure cause (for example, `NOT_FOUND` for untraceable entries) are defined in the interface `IF_ABAP_BEHV`.

**Type**

- `%fail` has the following type: `IF_ABAP_BEHV=>T_FAILINFO`

- `%fail-cause` has the following type: `IF_ABAP_BEHV=>T_FAIL_CAUSE`

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- `FAILED [EARLY|LATE]`

## More Information

See more details on message handling in the Development Guide for the ABAP RESTful Application Programming Model, section [Messages](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/ac74189b5cae49c1b091f04393bac069?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section is taken from here: `BP_DEMO_MANAGED_ROOT_FAILED===CCIMP`. The global class of the [behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is `BP_DEMO_MANAGED_ROOT_FAILED`. It demonstrates the component `%fail` in the context of an implementation for the `get_instance_features` method. See the executable program for this example further down.

``` abap
METHOD get_instance_features. 
 
READ ENTITIES OF demo_managed_root_failed IN LOCAL MODE 
      ENTITY demo_managed_root_failed FIELDS ( field2 ) 
        WITH CORRESPONDING #( keys ) 
      RESULT DATA(lt_inst_features) 
      FAILED failed. 
 
  IF lt_inst_features IS INITIAL. 
    APPEND VALUE #( 
       %msg = new_message_with_text( 
         severity = if_abap_behv_message=>severity-information 
         text = 'get_instance_features: Not relevant!' ) 
             ) TO reported-demo_managed_root_failed. 
  ELSE. 
    LOOP AT lt_inst_features ASSIGNING FIELD-SYMBOL(<fs>). 
      CASE <fs>-field2. 
       WHEN 'ZZZ'. 
        APPEND VALUE #( %tky = <fs>-%tky 
                        %update = if_abap_behv=>fc-o-disabled 
                      ) TO result. 
      WHEN OTHERS. 
        APPEND VALUE #( 
          %msg = new_message_with_text( 
            severity = if_abap_behv_message=>severity-information 
            text = 'get_instance_features: field3 is unrestricted!' ) 
          key_field = <fs>-key_field 
                      ) TO reported-demo_managed_root_failed. 
        ENDCASE. 
    ENDLOOP. 
ENDIF. 
ENDMETHOD.
```

## Executable Example

The example [Using `%fail`](abenderived_types_fail_abexa.md) demonstrates the use of `%fail` with a managed RAP BO.
