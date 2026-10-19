---
title: "%control"
source_file: abapderived_types_control.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Miscellaneous Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %control

## Use

`%control` is a [structured](../../abap-glossary/abenstructured_type_glosry.md) component in [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md).

It is a structure that contains all key and data fields of a [RAP BO instance](../../abap-glossary/abenrap_bo_instance_glosry.md) as components indicating flags. It is used to get information on which fields are provided (e. g. in the context of [`CREATE`](abapmodify_entity_entities_op.md) or [`UPDATE`](abapmodify_entity_entities_op.md) operations) or set a flag for which fields are requested (e. g. in the context of [`READ`](abapread_entity_entities.md) operations) by [RAP BO providers](../../abap-glossary/abenrap_bo_provider_glosry.md) or [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md) respectively during the current transaction.

In many cases, the control structure is filled implicitly and automatically, for example, in the context of RAP `MODIFY` operations using the ABAP word [`SET FIELDS WITH`](abapmodify_entity_entities_fields.md). However, depending on the context, the explicit specification of `%control` is mandatory. For example, in the context of a RAP `MODIFY` operation using the ABAP word `FROM` (e. g. `... CREATE FROM ...` or `... UPDATE FROM ...`), `%control` must be specified.

For specifying the values of the fields, the structured constant `mk` of interface `IF_ABAP_BEHV` can be used: `if_abap_behv=>mk-on` and `if_abap_behv=>mk-off`. For example, if fields are set with the value `if_abap_behv=>mk-on` in a `CREATE` operation, they are respected by the operation. If they are set with `if_abap_behv=>mk-off`, the fields are not respected. Note that the technical type is `x length 1`, hence, a simple flag like `'X'` does not work.

In `READ` operations, the keys must always be used and returned. Hence, unmarking the keys in `%control` in the context of managed scenarios are ignored.

**Type**

The components of the `%control` structure have the following type: `ABP_BEHV_FLAG`

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- `CREATE`

- `UPDATE`

- `READ IMPORT`

- `CHANGE`

The component also occurs within the [`%target`](abapderived_types_target.md) component in the context of create- or read-by-association operations.

## Hints

- The `FILLED_COMPONENTS_X` method of the system class `CL_ABAP_STRUCT_UTILITIES` supports an efficient processing of non-initial components of a structure where all components are typed with `x LENGTH 1`. It is particularly useful for checking filled components of structured derived types. See [here](../../abap-programming-language/abap-processing-internal-data/abencl_abap_struct_utilities.md) for more information.

- In [managed](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md) scenarios, setting the[`%control`](abapderived_types_control.md) flags for key fields, such as in the context of the `FROM` addition in ABAP EML `READ` statements, is optional. The returned instances include the key values.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_DRVD_TYPES_CNTRL` demonstrates the component `%control`.

``` abap
MODIFY ENTITY demo_managed_root_4 
      CREATE FROM VALUE #( 
        ( %cid = 'cid3' 
          key_field = 3  %control-key_field = if_abap_behv=>mk-on 
          field1 = 'iii' %control-field1 = if_abap_behv=>mk-on 
          field2 = 'jjj' %control-field2 = if_abap_behv=>mk-off 
          field3 = 30    %control-field3 = if_abap_behv=>mk-on 
          field4 = 31    %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid4' 
          key_field = 4  %control-key_field = if_abap_behv=>mk-on 
          field1 = 'kkk' %control-field1 = if_abap_behv=>mk-off 
          field2 = 'lll' %control-field2 = if_abap_behv=>mk-on 
          field3 = 40    %control-field3 = if_abap_behv=>mk-on 
          field4 = 41    %control-field4 = if_abap_behv=>mk-on ) ) 
      UPDATE FROM VALUE #( 
        ( key_field = 1 
          field1 = 'UPDATED_1' 
          field2 = 'UPDATED_2' 
          %control = VALUE #( field1 = if_abap_behv=>mk-on 
                              field2 = if_abap_behv=>mk-off ) ) 
        ( key_field = 2 
          field1 = 'UPDATED_3' 
          field2 = 'UPDATED_4' 
          %control = VALUE #( field1 = if_abap_behv=>mk-off 
                              field2 = if_abap_behv=>mk-on ) ) ) 
       MAPPED FINAL(mapped) 
       FAILED FINAL(failed) 
       REPORTED FINAL(reported).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_DRVD_TYPES_CNTRL` demonstrates how `%control` might be specified and enabled for all fields for all RAP BO instances in the [superstructure](../../abap-glossary/abensuperstructure_glosry.md) of an ABAP EML request.

``` abap
MODIFY ENTITY demo_managed_root_4 
  CREATE FROM VALUE #( 
      %control-key_field = if_abap_behv=>mk-on 
      %control-field1 = if_abap_behv=>mk-on 
      %control-field2 = if_abap_behv=>mk-on 
      %control-field3 = if_abap_behv=>mk-on 
      %control-field4 = if_abap_behv=>mk-on 
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
```

## Executable Example

The example [Using `%control`](abenderived_types_control_abexa.md) demonstrates the use of `%control` with a managed RAP BO.
