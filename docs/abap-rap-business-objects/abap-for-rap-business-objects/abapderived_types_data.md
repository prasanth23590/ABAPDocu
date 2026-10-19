---
title: "%data"
source_file: abapderived_types_data.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Miscellaneous Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %data

## Use

`%data` is a [component group](../../abap-glossary/abencomponent_group_glosry.md) in [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md).

`%data` contains all primary key fields (i. e. it also includes `%key`) and data fields of a [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md).

When specifying a data field, the use of `%data-...` is optional, i. e., the name of the data field can be used directly without `%data-...`.

**Type**

The components of `%data` retain their original line type. In case of the use within `%control`, the type for the individual components is `ABP_BEHV_FLAG`)

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- `CREATE`

- `UPDATE`

- `READ RESULT`

- `CHANGE`

The component also occurs within the following components:

- [`%control`](abapderived_types_control.md)

- [`%param`](abapderived_types_param.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_DRVD_TYPES_DATA` demonstrates the component `%data`.

``` abap
MODIFY ENTITY demo_managed_root_4 
      CREATE FROM VALUE #( 
        ( %cid = 'cid1' 
          %data-key_field = 1 
          %data-field1 = 'aaa' 
          %data-field2 = 'bbb' 
          %data-field3 = 10 
          %data-field4 = 11 
          %control-key_field = if_abap_behv=>mk-on 
          %control-field1 = if_abap_behv=>mk-on 
          %control-field2 = if_abap_behv=>mk-on 
          %control-field3 = if_abap_behv=>mk-on 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid2' 
          %data = VALUE #( key_field = 2 
                           field1 = 'ccc' 
                           field2 = 'ddd' 
                           field3 = 20 
                           field4 = 21 ) 
          %control = VALUE #(  key_field = if_abap_behv=>mk-on 
                               field1 = if_abap_behv=>mk-on 
                               field2 = if_abap_behv=>mk-on 
                               field3 = if_abap_behv=>mk-on 
                               field4 = if_abap_behv=>mk-on ) ) ) 
      CREATE BY \_child 
      FIELDS ( key_field_child field1 field2 field3 field4 ) 
      WITH VALUE #( 
        ( %cid_ref = 'cid1' 
          %target = VALUE #( 
            ( %cid = 'cid_child1' 
              %data = VALUE #( key_field_child = 1 
                               field1 = 'eee' 
                               field2 = 'fff' 
                               field3 = 10 
                               field4 = 11 ) ) ) ) 
        ( %cid_ref = 'cid2' 
          %target = VALUE #( 
            ( %cid = 'cid_child2' 
              %data = VALUE #( key_field_child = 2 
                               field1 = 'ggg' 
                               field2 = 'hhh' 
                               field3 = 20 
                               field4 = 21 ) ) ) ) ) 
    UPDATE FROM VALUE #( 
        ( %data-key_field = 1 
          %data-field1 = 'UPDATED_1' 
          field2 = 'UPDATED_2' 
          %control = VALUE #( field1 = if_abap_behv=>mk-on 
                              field2 = if_abap_behv=>mk-off ) ) 
        ( key_field = 2 
          field1 = 'UPDATED_3' 
          %data-field2 = 'UPDATED_4' 
          %control = VALUE #( field1 = if_abap_behv=>mk-off 
                              field2 = if_abap_behv=>mk-on ) ) ) 
       MAPPED FINAL(mapped) 
       FAILED FINAL(failed) 
       REPORTED FINAL(reported).
```

## Executable Example

The example [Using `%data` / `%target`](abenderived_types_data_abexa.md) demonstrates the use of `%data` with a managed RAP BO.
