---
title: "%op"
source_file: abapderived_types_op.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Miscellaneous Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %op

## Use

`%op` is a [component group](../../abap-glossary/abencomponent_group_glosry.md) in [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) that summarizes derived type components for [standard operations](../rap-behavior-definitions/abenbdl_standard_operations.md) ([`%create`](abapderived_types_create.md), for example), [nonstandard operations](../rap-behavior-definitions/abenbdl_nonstandard.md) ([`%action`](abapderived_types_action.md)), and associations defined in the BDEF as well as [`%element`](abapderived_types_element.md) in the context of [RAP messages](../../abap-glossary/abenrap_message_glosry.md) and [authorization control](../../abap-glossary/abenrap_auth_control_glosry.md).

For example, if `%op-%create` is marked in a [RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md), it indicates that the message relates to a [RAP create operation](../../abap-glossary/abenrap_create_operation_glosry.md).

**Type**

The components are typed with `ABP_BEHV_FLAG`.

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- `FAILED [EARLY|LATE]`

- `REPORTED [EARLY|LATE]`

- `[INSTANCE] AUTHORIZATION RESULT`

## Hint

The `FILLED_COMPONENTS_X` method of the system class `CL_ABAP_STRUCT_UTILITIES` supports an efficient processing of non-initial components of a structure where all components are typed with `x LENGTH 1`. It is particularly useful for checking filled components of structured derived types. See [here](../../abap-programming-language/abap-processing-internal-data/abencl_abap_struct_utilities.md) for more information.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section is taken from here: `BP_DEMO_MANAGED_ROOT_PERM=====CCIMP`. The global class of the [behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is `BP_DEMO_MANAGED_ROOT_PERM`. The code example demonstrates the component `%op` in the context of a `get_instance_authorizations` method that returns information on whether delete operations and executions of an action are allowed on RAP BO instances or not. See the executable program for this example further down.

``` abap
METHOD get_instance_authorizations. 
  READ ENTITIES OF demo_managed_root_perm IN LOCAL MODE 
     ENTITY demo_managed_root_perm 
       FIELDS ( field2 ) 
       WITH CORRESPONDING #( keys ) 
     RESULT DATA(lt_status) 
     FAILED DATA(fail). 
 
  failed =  CORRESPONDING #( DEEP fail ). 
 
  result = VALUE #( FOR ls_status IN lt_status 
           ( %tky    = ls_status-%tky 
             %op = VALUE #( 
               %delete = COND #( WHEN ls_status-field2 = 'B' 
                                 THEN if_abap_behv=>auth-unauthorized 
                                 ELSE if_abap_behv=>auth-allowed ) 
               %action-action = COND #( 
                                 WHEN ls_status-field2 = 'B' 
                                 THEN if_abap_behv=>auth-unauthorized 
                                 ELSE if_abap_behv=>auth-allowed ) 
                         ) ) ). 
 
ENDMETHOD.
```

## Executable Example

The example [BDEF derived type components in the context of requesting permissions](abenderived_types_misc_abexa.md) demonstrates the use of various BDEF derived type components including `%op` with a managed RAP BO.
