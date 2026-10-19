---
title: "%features"
source_file: abapderived_types_features.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Miscellaneous Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %features

## Use

`%features` is a [component group](../../abap-glossary/abencomponent_group_glosry.md) in [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md).

It is used to return [feature control](../rap-behavior-definitions/abenbdl_actions_fc.md) information by marking the components. The components of `%features` are those elements for which feature control is specified in the BDEF. For accessing the components with `%features`, the syntax can, for example, be as follows: `%features-%update`, `%features-%delete`, `%features-%action-action_name`, or `%features-%field-field_name`.

**Type**

The components of the `%features` structure are typed with `ABP_BEHV_FLAG`.

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- `[INSTANCE|GLOBAL] FEATURES RESULT`

## Hint

The `FILLED_COMPONENTS_X` method of the system class `CL_ABAP_STRUCT_UTILITIES` supports an efficient processing of non-initial components of a structure where all components are typed with `x LENGTH 1`. It is particularly useful for checking filled components of structured derived types. See [here](../../abap-programming-language/abap-processing-internal-data/abencl_abap_struct_utilities.md) for more information.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section is taken from here: `BP_DEMO_MANAGED_ROOT_PERM=====CCIMP`. The global class is the [behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) `BP_DEMO_MANAGED_ROOT_PERM`. It demonstrates the component `%features` in the context of a ` get_instance_features` method that returns information on whether certain fields are read-only or can be modified based on certain conditions. Furthermore, information is returned if the creation of instances for an associated entity is enabled or disabled. See the executable program for this example further down.

``` abap
METHOD get_instance_features. 
 
  READ ENTITIES OF demo_managed_root_perm IN LOCAL MODE 
      ENTITY demo_managed_root_perm 
        FIELDS ( field3 field4 ) 
        WITH CORRESPONDING #( keys ) 
      RESULT DATA(lt_numbers) 
      FAILED DATA(fail). 
 
  failed =  CORRESPONDING #( DEEP fail ). 
 
  result = VALUE #( FOR ls_numbers IN lt_numbers 
           ( %tky = ls_numbers-%tky 
             %features = VALUE #( 
             %field-field3 = COND #( 
                               WHEN ls_numbers-field4 > 5 
                               THEN if_abap_behv=>fc-f-read_only 
                               ELSE if_abap_behv=>fc-f-unrestricted ) 
             %field-field4 = COND #( 
                               WHEN ls_numbers-field3 > 10 
                               THEN if_abap_behv=>fc-f-read_only 
                               ELSE if_abap_behv=>fc-f-unrestricted ) 
             %assoc-_child = COND #( 
                               WHEN ls_numbers-field3 > 10 
                               THEN if_abap_behv=>fc-o-disabled 
                               ELSE if_abap_behv=>fc-o-enabled ) 
                ) ) ). 
 
ENDMETHOD.
```

## Executable Example

The example [BDEF derived type components in the context of requesting permissions](abenderived_types_misc_abexa.md) demonstrates the use of various BDEF derived type components including `%features` with a managed RAP BO.
