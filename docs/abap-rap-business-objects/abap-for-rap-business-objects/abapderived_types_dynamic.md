---
title: "Using BDEF Derived Types Dynamically"
source_file: abapderived_types_dynamic.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Using BDEF Derived Types Dynamically

You can use [Runtime Type Services](../../abap-glossary/abenrun_time_type_services_glosry.md) to create BDEF derived types dynamically and type-safe. Since BDEF derived types can be either table or structured types, the classes `CL_ABAP_TABLEDESCR` and `CL_ABAP_STRUCTDESCR` provide the `GET_BDEF_DERIVED_TYPE` method for dynamic type creation.

The method returns a reference to a type description object of a BDEF derived type that can be used to create anonymous data objects.

The following importing parameters are available:

- `p_entity`: Name of the entity

- `p_kind`: It is of type `ABP_BDEF_DERIVED_TYPE`, which is an enumerated type. Thus, only certain values can be specified, for example, `ABP_BDEF_DERIVED_TYPE-CREATE` for types for create operations. Note that a selection of BDEF derived types represented by the enumerated values is available, mainly those relevant for [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md).

- `p_sub_name`: Name of entity elements such as associations, actions or functions.

## Hints

- Some BDEF derived types are only available as structured types. Therefore, they cannot be used with `CL_ABAP_TABLEDESCR`.

- [Absolute type names](../../abap-glossary/abenabsolute_typename_glosry.md) of BDEF derived types have a specific pattern. Example patterns of absolute names of BDEF derived types:

  - `... TYPE TABLE FOR CREATE ...`: `\BDEF=BDEF_NAME\ENTITY=ENTITY_NAME\TYPE=CREATE`

  - `... TYPE STRUCTURE FOR UPDATE ...`: `\BDEF=BDEF_NAME\ENTITY=ENTITY_NAME\TYPE=UPDATE\LINE`

  - `... TYPE TABLE FOR ACTION IMPORT bdef_name~act` `\BDEF=BDEF_NAME\ENTITY=ENTITY_NAME\ACTION=ACT\TYPE=IMPORTING`

- [`%data`](abapderived_types_data.md) and [`%control`](abapderived_types_control.md) are subtypes of BDEF derived types. These types do not have a dedicated BDEF derived type name and have a technical name as absolute type name.

- When calling the method, make sure that you catch potential exceptions such as the following:

  - `CX_SY_RTTI_SYNTAX_ERROR`: Raised in case of syntax errors

  - `CX_SY_BDEF_DERIVED_TYPE_ERROR`: Raised in case of querying errors, for example, if a mandatory element name for a type is not specified, or if such a name is specified but not existent

  - `CX_SY_RTTI_TYPE_NOT_RELEASED`: Raised in case of non-released types

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example explores using BDEF derives dynamically.

``` abap
CONSTANTS entity TYPE string VALUE `DEMO_MANAGED_ROOT_TEST`. 
CONSTANTS assoc_name TYPE string VALUE `_child`. 
CONSTANTS action_name TYPE string VALUE `action1`. 
 
"Dynamically creating tabular BDEF derived type 
"(... TABLE FOR CREATE ...) 
FINAL(tdo_tab_der_type_create) = 
  cl_abap_tabledescr=>get_bdef_derived_type( 
    p_entity = entity 
    p_kind = abp_bdef_derived_type-create ). 
 
"Getting information and the line type, including assertions 
FINAL(absolute_name_tab_der_type) = 
  tdo_tab_der_type_create->absolute_name. 
ASSERT absolute_name_tab_der_type = 
  `\BDEF=DEMO_MANAGED_ROOT_TEST\ENTITY=DEMO_MANAGED_ROOT_TEST\` && 
  `TYPE=CREATE`. 
FINAL(type_kind_tab_der_type) = tdo_tab_der_type_create->type_kind. 
ASSERT type_kind_tab_der_type = 'h'. 
FINAL(line_type_tab_der_type) = 
  tdo_tab_der_type_create->get_table_line_type( ). 
FINAL(absolute_name_line_type) = 
  tdo_tab_der_type_create->get_table_line_type( )->absolute_name. 
ASSERT absolute_name_line_type = 
  `\BDEF=DEMO_MANAGED_ROOT_TEST\ENTITY=DEMO_MANAGED_ROOT_TEST\` && 
  `TYPE=CREATE\LINE`. 
 
"Creating an anonymous data object based on the type 
"description object 
DATA dref_tdo TYPE REF TO data. 
CREATE DATA dref_tdo TYPE HANDLE tdo_tab_der_type_create. 
 
"Creating an anonymous data object based on the absolute name 
DATA dref_abs TYPE REF TO data. 
CREATE DATA dref_abs TYPE (absolute_name_tab_der_type). 
 
"Creating the target type directly for comparison 
DATA tab_der_type_create TYPE TABLE FOR CREATE demo_managed_root_test. 
 
"Checking if the types apply 
FINAL(tdo_itab_der_type) = CAST cl_abap_tabledescr( 
  cl_abap_typedescr=>describe_by_data( tab_der_type_create ) ). 
FINAL(applies_to_itab_1) = 
  tdo_itab_der_type->applies_to_data( dref_tdo->* ). 
ASSERT applies_to_itab_1 = 'X'. 
FINAL(applies_to_itab_2) = 
  tdo_itab_der_type->applies_to_data( dref_abs->* ). 
ASSERT applies_to_itab_2 = 'X'. 
 
"Dynamically creating structured BDEF derived type 
"(... STRUCTURE FOR UPDATE ...) 
FINAL(tdo_struc_der_type_update) = 
  cl_abap_structdescr=>get_bdef_derived_type( 
    p_entity = entity 
    p_kind = abp_bdef_derived_type-update ). 
 
"Getting information, including assertions 
FINAL(absolute_name_struc_der_type) = 
  tdo_struc_der_type_update->absolute_name. 
ASSERT absolute_name_struc_der_type = 
  `\BDEF=DEMO_MANAGED_ROOT_TEST\ENTITY=DEMO_MANAGED_ROOT_TEST\` && 
  `TYPE=UPDATE\LINE`. 
FINAL(type_kind_struc_der_type) = 
  tdo_struc_der_type_update->type_kind. 
ASSERT type_kind_struc_der_type = 'v'. 
 
"Creating an anonymous data object based on the type 
"description object 
CREATE DATA dref_tdo TYPE HANDLE tdo_struc_der_type_update. 
 
"Creating an anonymous data object based on the absolute name 
CREATE DATA dref_abs TYPE (absolute_name_struc_der_type). 
 
"Creating the target type directly for comparison 
DATA struc_der_type_update TYPE STRUCTURE 
      FOR UPDATE demo_managed_root_test. 
 
"Checking if the types apply 
FINAL(tdo_struc_der_type) = CAST cl_abap_structdescr( 
  cl_abap_typedescr=>describe_by_data( struc_der_type_update ) ). 
FINAL(applies_to_struc_1) = 
  tdo_struc_der_type->applies_to_data( dref_tdo->* ). 
ASSERT applies_to_struc_1 = 'X'. 
FINAL(applies_to_struc_2) = 
  tdo_struc_der_type->applies_to_data( dref_abs->* ). 
ASSERT applies_to_struc_2 = 'X'. 
 
"Creating a derived type dynamically involving an action 
FINAL(tdo_der_type_action_import) = 
  cl_abap_tabledescr=>get_bdef_derived_type( 
      p_entity = entity 
      p_kind = abp_bdef_derived_type-action_function_import 
      p_sub_name = action_name ). 
FINAL(abs_name_der_type_act_import) = 
  tdo_der_type_action_import->absolute_name. 
ASSERT abs_name_der_type_act_import = 
  `\BDEF=DEMO_MANAGED_ROOT_TEST\ENTITY=DEMO_MANAGED_ROOT_TEST\` && 
  `ACTION=ACTION1\TYPE=IMPORTING`. 
 
"Specifications raising exceptions 
"Create-by-association without specifying the p_sub_name parameter 
TRY. 
    FINAL(tdo_error_1) = cl_abap_tabledescr=>get_bdef_derived_type( 
      p_entity = entity p_kind = abp_bdef_derived_type-cba ). 
  CATCH cx_sy_rtti_syntax_error 
        cx_sy_bdef_derived_type_error 
        cx_sy_rtti_type_not_released. 
    FINAL(tdo_no_error_1) = cl_abap_tabledescr=>get_bdef_derived_type( 
      p_entity = entity 
      p_kind = abp_bdef_derived_type-cba 
      p_sub_name = assoc_name ). 
    ASSERT tdo_no_error_1->absolute_name = 
    `\BDEF=DEMO_MANAGED_ROOT_TEST\ENTITY=DEMO_MANAGED_ROOT_TEST\` && 
    `ASSOC=_CHILD\TYPE=CREATE`. 
ENDTRY. 
 
"Specifying a wrong value for p_sub_name 
TRY. 
    FINAL(tdo_error_2) = cl_abap_tabledescr=>get_bdef_derived_type( 
      p_entity = entity 
      p_kind = abp_bdef_derived_type-cba 
      p_sub_name = 'SOME_ASSOC' ). 
  CATCH cx_sy_rtti_syntax_error 
        cx_sy_bdef_derived_type_error 
        cx_sy_rtti_type_not_released INTO DATA(error_2). 
ENDTRY. 
ASSERT error_2 IS NOT INITIAL. 
 
"Creating a table type for a derived type that is only possible for 
"structured types 
TRY. 
    FINAL(tdo_error_3) = cl_abap_tabledescr=>get_bdef_derived_type( 
      p_entity = entity 
      p_kind = abp_bdef_derived_type-permissions_request ). 
  CATCH cx_sy_rtti_syntax_error 
        cx_sy_bdef_derived_type_error 
        cx_sy_rtti_type_not_released INTO DATA(error_3). 
ENDTRY. 
ASSERT error_3 IS NOT INITIAL.
```
