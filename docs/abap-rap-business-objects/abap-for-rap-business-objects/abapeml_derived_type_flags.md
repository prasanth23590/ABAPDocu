---
title: "Constants for BDEF Derived Type Components"
source_file: abapeml_derived_type_flags.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Constants for BDEF Derived Type Components

Numerous BDEF derived types incorporate `%` components that represent flags. For example, these flags are used in ABAP EML read requests within the [`%control`](abapderived_types_control.md) structure to specify the fields to be read.

The flags are differentiated by various types available as constants defined in the interface `IF_ABAP_BEHV`. Despite the technical type properties being identical (type `RAW` length 1), ensure you do not confuse the constants and use them in the correct context. The usable values are components of the following structured constants:

| **Type**              | **Structured Constant** | **Description**                                                                                                                     |
|-----------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `ABP_BEHV_FLAG`       | ` IF_ABAP_BEHV=>MK`     | Used to mark and unmark fields in ABAP EML modify and read operations, such as in `%control` and `%element`.                        |
| `ABP_BEHV_FIELD_PERM` | `IF_ABAP_BEHV=>PERM-F`  | Used for field permission results, like a field marked as mandatory or read-only.                                                   |
| `ABP_BEHV_OP_PERM`    | `IF_ABAP_BEHV=>PERM-O`  | Used for operation permission results, such as a delete operation that is marked as enabled.                                        |
| `ABP_BEHV_FIELD_CTRL` | `IF_ABAP_BEHV=>FC-F`    | Used for field feature control results, like a field marked with no restrictions.                                                   |
| `ABP_BEHV_OP_CTRL`    | `IF_ABAP_BEHV=>FC-O`    | Used for operation feature control results, like an update operation that is marked as disabled.                                    |
| `ABP_BEHV_AUTH`       | `IF_ABAP_BEHV=>AUTH`    | Used for authorization results, like an operation marked as unauthorized.                                                           |
| `ABP_BEHV_FEATURE`    | \-                      | This type is obsolete for field permission and feature control results. Use `ABP_BEHV_FIELD_PERM` or `ABP_BEHV_FIELD_CTRL` instead. |

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code snippet shows BDEF derived type components that are typed with `ABP_BEHV_FLAG`. The components are assigned values of the structured constant `IF_ABAP_BEHV=>MK`.

``` abap
MODIFY ENTITY demo_managed_root_4 
  CREATE FROM VALUE #( 
      %control-key_field = if_abap_behv=>mk-on 
      %control-field1 = if_abap_behv=>mk-on 
      %control-field2 = if_abap_behv=>mk-on 
      %control-field3 = if_abap_behv=>mk-on 
      %control-field4 = if_abap_behv=>mk-off 
    ( %cid = 'cid1' 
      key_field = 1 
      field1 = 'aaa' 
      field2 = 'bbb' 
      field3 = 10 
      field4 = 11 ) 
    ( %cid = 'cid2' 
      key_field = 2 
      field1 = 'ccc' 
      field2 = 'ddd' 
      field3 = 20 
      field4 = 21 ) ) 
      MAPPED FINAL(mapped) 
      FAILED FINAL(failed) 
      REPORTED FINAL(reported). 
 
... 
 
DATA request TYPE STRUCTURE FOR 
        PERMISSIONS REQUEST demo_managed_root_perm. 
 
request = VALUE #( 
    %create = if_abap_behv=>mk-on 
    %update = if_abap_behv=>mk-on 
    %delete = if_abap_behv=>mk-off ).
```
