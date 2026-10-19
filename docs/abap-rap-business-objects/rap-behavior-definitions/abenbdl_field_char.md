---
title: "RAP - FieldCharacteristics"
source_file: abenbdl_field_char.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - FieldCharacteristics

## Syntax

``` abap
... field(readonly) Field1, Field2, ...; 
       | (mandatory) Field1, Field2, ...; 
       | (suppress) Field1, Field2, ...; 
       | (features:instance) Field1, Field2, ...; 
       | (mandatory:create) Field1, Field2, ...; 
       | (mandatory:update) Field1, Field2, ...; 
       | (readonly:create) Field1, Field2, ...; 
       | (readonly:update) Field1, Field2, ...; 
       | (recommendations) Field1, Field2, ...; 
         
```

### Variant

[1. `... field(readonly) Field1, Field2, ...`](abenbdl_field_char.md#variant-1)

[2. `... field(mandatory) Field1, Field2, ...`](abenbdl_field_char.md#variant-2)

[3. `... field(suppress) Field1, Field2, ...`](abenbdl_field_char.md#variant-3)

[4. `... field(features:instance) Field1, Field2, ...`](abenbdl_field_char.md#variant-4)

[5. `... field(mandatory:create) Field1, Field2, ...`](abenbdl_field_char.md#variant-5)

[6. `... field(mandatory:update) Field1, Field2, ...`](abenbdl_field_char.md#variant-6)

[7. `... field(readonly:create) Field1, Field2, ...`](abenbdl_field_char.md#variant-7)

[8. `... field(readonly:update) Field1, Field2, ...`](abenbdl_field_char.md#variant-8)

[9. `... field(recommendations) Field1, Field2, ...`](abenbdl_field_char.md#variant-9)

## Overview

### Description

This topic lists [RAP field characteristics](../../abap-glossary/abenrap_field_char_glosry.md) for the [fields](../../abap-glossary/abenrap_bo_field_glosry.md) of a [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md).

Commas can be used to classify multiple fields in the same way. Example: `field(readonly) Field1, Field2, Field3;`

A field can have multiple characteristics, divided by commas within the brackets. Example: `field(mandatory:create, readonly:update) Field1, Field2, Field3;`. Certain restrictions apply on the combination of field characteristics. They are indicated by a syntax check warning.

## Availability

- [Managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BOs](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- In case of [projection BOs](../../abap-glossary/abenrap_projection_bo_glosry.md), automatic inheritance takes place. To newly define field characteristics in a projection BO, special rules apply. See topic [RAP - `FieldCharacteristics`, Projection BDEF](abenbdl_field_projection.md).

- For [abstract BDEFs](../../abap-glossary/abencds_abstract_bdef_glosry.md), special rules apply. See topic [RAP - Field Characteristics, Abstract BDEF](abenbdl_field_abstract.md).

- For [interface BDEFs](../../abap-glossary/abencds_interface_bdef_glosry.md), automatic inheritance takes place. The interface can add further field characteristics, as long as they do not contradict the field characteristics from the base layer. This is described in topic [Field Characteristics, Interface BDEF](abenbdl_field_interface.md).

### Hints

- In UI scenarios, field characteristics based on field control are displayed as [RAP consumer hints](../../abap-glossary/abenrap_consumer_hint_glosry.md).

- For fields with `field(recommendations)`, [RAP recommendations](../../abap-glossary/abenrecommendation_glosry.md) are shown on the UI.

- All primary key fields must be defined as `readonly` or as `readonly:update`. Otherwise, a syntax check warning occurs.

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section [Feature Control Definition: Fields](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/eb060664a98c4275a3a4346d9c5b6707?version=sap_cross_product_abap)

## Variant 1

`... field(readonly) Field1, Field2, ...`

### Description

- Defines that the values of the specified fields must not be created or updated by the [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md).

- [Static field attribute](../../abap-glossary/abenrap_static_field_char_glosry.md).

- No implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) required.

- If a [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) tries to modify a field specified as `readonly` in the BDEF using [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md) [`CREATE`](../abap-for-rap-business-objects/abapmodify_entity_entities_op.md) or [`UPDATE`](../abap-for-rap-business-objects/abapmodify_entity_entities_op.md), a syntax check error occurs.

## Variant 2

`... field(mandatory) Field1, Field2, ...`

### Description

- Defines that it is mandatory to enter values into the specified fields before persisting them on the database. These fields are marked as mandatory on the user interface in an OData scenario. However, there is no runtime check for mandatory fields and no runtime error occurs if a mandatory field is not filled. If a runtime check is required, the application developer should implement it using a [validation on save](abenbdl_validations.md).

- [Static field attribute](../../abap-glossary/abenrap_static_field_char_glosry.md).

- No implementation in the ABAP behavior pool required.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF that defines the field `char_field1` as mandatory.

**Note:** This example is intentionally kept short and simple and serves demonstration purposes only. It does not fully meet the requirements of the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). See more information on the RAP BO contract in the [Development guide for the ABAP RESTful Application Programming Model](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

``` abap
managed
implementation in class BP_DEMO_RAP_FIELD_MANDATORY unique;
strict ( 2 );

define behavior for DEMO_RAP_FIELD_MANDATORY
persistent table demo_dbtab_field
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field ( readonly : update ) key_field;
  field ( mandatory ) char_field1;
}
```

The ABAP class `CL_DEMO_RAP_MANAGED_MANDATORY` uses [EML](../../abap-glossary/abeneml_glosry.md) to access to RAP business object. It creates three entity instances by specifying a value for the primary key field `key_field`. No value is entered for the mandatory field `char_field1`. It commits the three new entity instances to the database. Using the ABAP SQL `SELECT` statement, it displays the content of the underlying database table.

Code Snippet:

``` abap
DELETE FROM demo_dbtab_field. 
 
MODIFY ENTITIES OF demo_rap_field_mandatory 
    ENTITY demo_rap_field_mandatory 
    CREATE FIELDS ( key_field char_field1 ) WITH VALUE #( 
      ( %cid = '1' 
        key_field = '0894EF1643A01EDB989329BF29E8FD27' ) 
      ( %cid = '2' 
        key_field = '0894EF1643A01EDB989329BF29E81D27' ) 
      ( %cid = '3' 
        key_field = '0894EF1643A01EDB989329BF29E83D27' ) ) 
    MAPPED FINAL(mapped) 
    FAILED FINAL(failed) 
    REPORTED FINAL(reported). 
 
COMMIT ENTITIES.
```

Result: The mandatory field `char_field1` contains the [initial value](../../abap-glossary/abeninitial_value_glosry.md), no syntax check warning or syntax check error occurs. ![figure](images_abdoc_mandatory.png)

## Variant 3

`... field(suppress) Field1, Field2, ...`

### Description

- `Field(suppress)` can be used to remove a field from the [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) and all RAP APIs. This is possible for all fields except for [key fields](../../abap-glossary/abenkey_field_glosry.md), [foreign key fields](../../abap-glossary/abenforeign_key_field_glosry.md), and fields used by the current BDEF, such as [ETag](../../abap-glossary/abenrap_etag_glosry.md) fields. To remove a suppressed field from the OData exposure, the CDS annotation [`@Consumption.hidden:true`](../../abap-core-data-services-abap-cds/abap-cds-annotations/abencds_207868793_anno.md) must be set.

- [Currency key fields](../../abap-glossary/abencurrency_key_glosry.md) of data type `CUKY` can be suppressed only if all [CDS amount fields](../../abap-glossary/abencds_amount_field_glosry.md) that make a reference to this particular `CUKY` field are also suppressed.

- [Static field attribute](../../abap-glossary/abenrap_static_field_char_glosry.md).

- No implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) required.

- If a [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) tries to modify a suppressed field, an error message occurs that tells the consumer that no field of this name exists.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows an interface BDEF that suppresses the field `DataFieldRoot`.

``` abap
interface;
use draft;
foreign entity demo_cds_validation;
define behavior for DEMO_RAP_INTERFACE_DRAFT alias Root
use etag
{
  use create;
  use update;
  use delete;

  use action Activate;
  use action Discard;
  use action Edit;
  use action Resume;
  use action Prepare;

  field(suppress) DataFieldRoot;

}
```

The ABAP class `CL_DEMO_RAP_INTERFACE_DRAFT` creates a variable typed with the BDEF derived type of the RAP BO `DEMO_RAP_INTERFACE_DRAFT` and displays the structure of this variable.

Code Snippet:

``` abap
DATA structure TYPE TABLE FOR CREATE demo_rap_interface_draft. 
APPEND INITIAL LINE TO structure.
```

Result: The suppressed field `DataFieldRoot` is not part of `structure`. ![figure](images_field_suppress.png)

## Variant 4

`... field(features:instance) Field1, Field2,...`

### Description

- [Dynamic field attribute](../../abap-glossary/abenrap_dyn_field_char_glosry.md) that defines access restrictions for fields depending on the state of the BO entity instance.

- Must be implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR INSTANCE FEATURES`](../abap-for-rap-business-objects/abaphandler_meth_features.md). In the ABAP behavior pool, it can be specified that a field is dynamically mandatory, read-only, has no restrictions, or that it is mandatory and read-only.

- If a RAP BO consumer tries to breach the dynamic access restrictions, it is ignored. There is no error or warning message. In a managed RAP BO, there is also no entry in the response structures. In an unmanaged RAP BO, the `reported` structure can be filled, depending on the BO implementation.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF that defines dynamic feature control for field `int_field2`.

**Note:** This example is intentionally kept short and simple and serves demonstration purposes only. It does not fully meet the requirements of the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). See more information on the RAP BO contract in the [Development guide for the ABAP RESTful Application Programming Model](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

``` abap
managed implementation in class bp_demo_rap_instance_features unique;
strict ( 2 );

define behavior for DEMO_RAP_INSTANCE_FEATURES
persistent table demo_dbtab_field
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field ( readonly : update ) key_field;
  field ( features : instance ) int_field2;
}
```

In the ABAP behavior pool, it specifies the following condition: if field `int_field1` contains the value '1', then `int_field2` is read-only.

Code snippet:

``` abap
... %field-int_field2 = COND #( 
                        WHEN ls_variable-int_field1 = '1' 
                        THEN if_abap_behv=>fc-f-read_only 
                        ELSE if_abap_behv=>fc-f-unrestricted 
                        ) ) ).
```

The ABAP class `CL_DEMO_RAP_INSTANCE_FEATURES` uses [EML](../../abap-glossary/abeneml_glosry.md) to access to RAP business object.

- First, it inserts an entity instance directly onto the database using ABAP SQL `INSERT`. This entity instance has the value '1' for field `int_field1`. Therefore, it fulfills the condition that triggers feature control: if this instance is updated, field `int_field2` should be read-only.

- An EML [`UPDATE`](../abap-for-rap-business-objects/abapmodify_entity_entities_op.md) operation is executed on the same instance. This update operation tries to enter a value into field `int_field2`.

- The updated entity instance is committed to the database. Using the ABAP SQL `SELECT` statement, the content of the underlying database table is displayed.

Result: The update operation is prevented by the dynamic feature control. Field `int_field2` contains the initial value. No syntax check warning or syntax check error occurs. ![figure](images_abdoc_instance_features.png)

### Executable Example

[ABAP EML - RAP Calculator](../abap-for-rap-business-objects/abeneml_calculator_abexa.md)

## Variant 5

`... field(mandatory:create) Field1, Field2, ...`

### Description

- [Static field attribute](../../abap-glossary/abenrap_static_field_char_glosry.md) that defines that it is mandatory to enter a value when an instance is created.

- No implementation in the ABAP behavior pool required.

- If a RAP BO consumer tries to create a new entity instance without entering a value into the field defined as `mandatory:create`, a runtime error occurs.

### Hint

A typical use case is to combine `mandatory:create` with `readonly:update` for key fields in an [external numbering](../../abap-glossary/abenrap_ext_numbering_glosry.md) scenario.

## Variant 6

`... field(mandatory:update) Field1, Field2, ...`

### Description

- Defines that it is mandatory to enter values into the specified field by the [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) during update operations and after the `create` operation.

- [Static field attribute](../../abap-glossary/abenrap_static_field_char_glosry.md).

- No implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) required.

- Not supported in a SAP Fiori UI application.

## Variant 7

`... field(readonly:create) Field1, Field2, ...`

### Description

- Defines that the value of the field in question cannot be changed by the [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) during the `create` operation.

- [Static field attribute](../../abap-glossary/abenrap_static_field_char_glosry.md).

- No implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) required.

## Variant 8

`... field(readonly:update) Field1, Field2, ...`

### Description

- [Static field attribute](../../abap-glossary/abenrap_static_field_char_glosry.md) that defines a field as read-only during update operations, that means, the field in question cannot be changed anymore after the `create` operation.

- No implementation in the ABAP behavior pool required.

- If a RAP BO consumer tries to update a field defined as `readonly:update`, a syntax check error occurs.

- In the case of a [draft-enabled RAP business object](../../abap-glossary/abendraft_rap_bo_glosry.md), errors might occur if there is a saved draft instance that has not yet been activated. If a new instance is created with the same primary key values as an already existing draft instance, this is considered an update operation. If the field in question is specified as `readonly:update`, an error message occurs. For further details, see [External Early Numbering (RAP Development Guide)](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/eb060664a98c4275a3a4346d9c5b6707?version=sap_cross_product_abap).

## Variant 9

`...field(recommendations) Field1, Field2,...`

### Description

- `field(recommendations)` is a field attribute that provides [RAP recommendation](../../abap-glossary/abenrecommendation_glosry.md) for the specified fields.

- You can implement RAP recommendations for an [input field](../../abap-glossary/abeninput_field_glosry.md) only if there is a [value help](../../abap-glossary/abeninput_help_glosry.md) available for this field.

- You must also specify a corresponding [recommendation function](abenbdl_recommendations.md) in the behavior definition and implement it in the behavior pool.

- You must define [RAP side effects](../../abap-glossary/abenrap_side_effects_glosry.md) for the recommendation function.

For more information, see [*Adding RAP Recommendations*](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/9d9cc97cab9d48fdaa35d5c333526ba0) in the development guide for the ABAP RESTful Application Programming Model.
