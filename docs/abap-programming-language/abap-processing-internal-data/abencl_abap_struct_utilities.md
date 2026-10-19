---
title: "CL_ABAP_STRUCT_UTILITIES, System Class"
source_file: abencl_abap_struct_utilities.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_STRUCT_UTILITIES, System Class

The system class `CL_ABAP_STRUCT_UTILITIES` allows an efficient processing of non-initial components of a structure. The following static methods are available:

- `FILLED_COMPONENTS`

  Returns an internal table containing the names of the non-initial components of the structure and their index.

- `FILLED_COMPONENTS_C`

  Same as above. All structure components must be typed with `c LENGTH 1`.

- `FILLED_COMPONENTS_X`

  Same as above. All structure components must be typed with `x LENGTH 1`. It is especially useful for checking filled components of [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md), for example, [`%control`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapderived_types_control.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates `FILLED_COMPONENTS` as follows: A structure is created with components of different types. Values are assigned to all components. All components are retrieved using RTTI. Using `FILLED_COMPONENTS`, an internal table is retrieved that contains the names and indexes of the non-initial components. In a `DO` loop, structure components are initialized one by one, and `FILLED_COMPONENTS` is called again to show that components with their type-specific initial values are not included in the result.

Similarly, `FILLED_COMPONENTS_C` and `FILLED_COMPONENTS_X` are demonstrated. `FILLED_COMPONENTS_X` is demonstrated using a BDEF derived type to check the flags in the `%control` structure.

``` abap
DATA(o) = cl_demo_output=>new( ). 
o->write( `*********** filled_components ***********` ). 
DATA: BEGIN OF struct, 
        a TYPE c LENGTH 1, 
        b TYPE i, 
        c TYPE spfli, 
        d TYPE REF TO string, 
      END OF struct. 
 
struct = VALUE #( a = 'X' 
                  b = 123 
                  c = VALUE #( carrid = 'LH' ) 
                  d = NEW #( `ABAP` ) ). 
 
DATA(all_comps) = CAST cl_abap_structdescr( 
  cl_abap_typedescr=>describe_by_data( struct ) )->components. 
o->write( |Number of components: { lines( all_comps ) }| ). 
o->write( all_comps ). 
 
DATA(filled_comps) = 
  cl_abap_struct_utilities=>filled_components( struct ). 
o->write( filled_comps ). 
DATA(comp_num) = lines( all_comps ). 
DO lines( all_comps ) TIMES. 
  CLEAR struct-(comp_num). 
  filled_comps = cl_abap_struct_utilities=>filled_components( struct ). 
  o->write( filled_comps ). 
  comp_num -= 1. 
ENDDO. 
 
o->write( `*********** filled_components_c ***********` ). 
DATA: BEGIN OF struct_c1, 
        a TYPE c LENGTH 1 VALUE 'X', 
        b TYPE c LENGTH 1, 
        c TYPE c LENGTH 1 VALUE 'X', 
      END OF struct_c1. 
 
DATA(all_comps_c1) = CAST cl_abap_structdescr( 
  cl_abap_typedescr=>describe_by_data( struct_c1 ) )->components. 
o->write( |Number of components: { lines( all_comps_c1 ) }| ). 
o->write( all_comps_c1 ). 
 
filled_comps = 
  cl_abap_struct_utilities=>filled_components_c( struct_c1 ). 
o->write( filled_comps ). 
 
o->write( `*********** filled_components_x ***********` ). 
DATA struc_der_type TYPE STRUCTURE FOR READ IMPORT demo_managed_root_4. 
struc_der_type = VALUE #( 
  %control = VALUE #( key_field = if_abap_behv=>mk-on 
                      field1    = if_abap_behv=>mk-on 
                      field4 = if_abap_behv=>mk-on ) ). 
 
DATA(all_comps_ctrl) = CAST cl_abap_structdescr( 
  cl_abap_typedescr=>describe_by_data( 
    struc_der_type-%control ) )->components. 
o->write( |Number of components: { lines( all_comps_ctrl ) }| ). 
o->write( all_comps_ctrl ). 
 
filled_comps = cl_abap_struct_utilities=>filled_components_x( 
  struc_der_type-%control ). 
o->write( filled_comps ). 
o->display( ).
```
