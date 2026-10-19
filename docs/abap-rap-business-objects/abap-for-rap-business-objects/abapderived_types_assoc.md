---
title: "%assoc"
source_file: abapderived_types_assoc.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Miscellaneous Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %assoc

## Use

`%assoc` is a structured component in [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md).

It is a structure containing the associations defined in the BDEF as components and is used, for example, in the context of [feature control](../rap-behavior-definitions/abenbdl_actions_fc.md) to get or provide control information for associated entities or to get information in responses if an association was affected in case of failures.

**Type**

The components of the `%assoc` structure are typed with `ABP_BEHV_FLAG`.

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- `PERMISSIONS REQUEST`

- `PERMISSIONS RESULT`

- `FAILED [EARLY|LATE]`

- `[INSTANCE|GLOBAL] AUTHORIZATION REQUEST`

- `[INSTANCE|GLOBAL] AUTHORIZATION RESULT`

- `[INSTANCE|GLOBAL] FEATURES REQUEST`

- `[INSTANCE|GLOBAL] FEATURES RESULT`

## Hint

The `FILLED_COMPONENTS_X` method of the system class `CL_ABAP_STRUCT_UTILITIES` supports an efficient processing of non-initial components of a structure where all components are typed with `x LENGTH 1`. It is particularly useful for checking filled components of structured derived types. See [here](../../abap-programming-language/abap-processing-internal-data/abencl_abap_struct_utilities.md) for more information.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_DRVD_TYPES_PERM` demonstrates the component `%assoc`. In this case, the request parameter, which is of type [`TYPE STRUCTURE FOR PERMISSIONS REQUEST`](abaptype_structure_for.md), is specified for a [`GET PERMISSIONS`](abapget_permissions.md) statement.

``` abap
DATA: request TYPE STRUCTURE FOR 
        PERMISSIONS REQUEST demo_managed_root_perm. 
 
request = VALUE #( 
    %create          = if_abap_behv=>mk-on 
    %update          = if_abap_behv=>mk-on 
    %delete          = if_abap_behv=>mk-on 
    %assoc-_child    = if_abap_behv=>mk-on 
    %action-action   = if_abap_behv=>mk-on 
    %field-key_field = if_abap_behv=>mk-on 
    %field-field1    = if_abap_behv=>mk-on 
    %field-field2    = if_abap_behv=>mk-on 
    %field-field3    = if_abap_behv=>mk-on 
    %field-field4    = if_abap_behv=>mk-on ).
```

## Executable Example

The example [BDEF derived type components in the context of requesting permissions](abenderived_types_misc_abexa.md) demonstrates the use of various BDEF derived type components including `%assoc` with a managed RAP BO.
