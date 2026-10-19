---
title: "RAP - OutputParameter"
source_file: abenbdl_action_output_para.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - RAP BO Operation, Additions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - OutputParameter

## Syntax

``` abap
... [deep] result [selective] [cardinality] 
           { $self 
           | entity OutputParameterEntity 
           | ResultParameterStructure [external 'ExternalName'] }  
```

[`external`](abenbdl_external.md)

### Addition

[1. `... deep`](abenbdl_action_output_para.md#addition-1)

[2. `... selective`](abenbdl_action_output_para.md#addition-2)

[3. `... [cardinality]`](abenbdl_action_output_para.md#addition-3)

## Overview

### Description

The output parameter for an [action](abenbdl_action.md) or [function](abenbdl_function.md) is defined with the keyword `result`. It can be used to store the result of an action or function in an internal table. For details on the components of the result structure, see the topic [ABAP EML - `RESULT result_tab`](../abap-for-rap-business-objects/abapeml_result.md).

If a result parameter is declared in the action or function definition, it must be filled in the implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md).

The return type of the result parameter can be an entity or a structure:

- `$self` specifies that the result type is the same type as the entity for which the action or function is defined.

- `entity OutputParameterEntity` specifies that the result is a different CDS view entity of the same or another [BO](../../abap-glossary/abenrap_bo_glosry.md).

- `ResultParameterStructure`: A [RAP abstract BDEF](../../abap-glossary/abencds_abstract_bdef_glosry.md) can be specified as a return type. A resulting structure for actions or functions is defined without the keyword `entity`.

  For result structures, it is possible to define an alias to clearly identify the result in the OData metadata. The keyword [`external`](abenbdl_external.md) after the result type defines this OData representation of the action or function result.

### Hint

If the result is a [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md), the result must be defined without the keyword `entity` as abstract entities are generally considered to be structures in ABAP.

## More Information

Development guide for the ABAP RESTful Application Programming Model, topic [Action Definition](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/14ddc6b2442b4b97842af9158a1c9c44?version=sap_cross_product_abap).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF with two actions, `Approve_Order` and `Reject_Order`. The result is `$self` with cardinality 1, so the output parameter has the same type as the entity for which the action is executed.

``` abap
managed implementation in class bp_demo_cds_purch_doc_m unique;
strict(2);

define behavior for DEMO_CDS_PURCH_DOC_M alias PurchaseDocument
persistent table demo_purch_doc
lock master
etag master crea_date_time
authorization master (none)
{
  create;
  update;
  delete;
  association _PurchaseDocumentItem { create; }

  action Approve_Order result [1] $self;
  action Reject_Order  result [1] $self;

  field(readonly:update) PurchaseDocument;

  field ( readonly )  crea_uname , crea_date_time;

  mapping for demo_purch_doc corresponding;
}

define behavior for DEMO_CDS_PURCH_DOC_I_M alias PurchaseDocumentItem
persistent table DEMO_PURCH_DOC_I
lock dependent by _PurchaseDocument
authorization dependent by _PurchaseDocument
{
  update;
  delete;
  field ( readonly )  PurchaseDocumentItem , PurchaseDocument;
  field ( mandatory ) Price , Quantity , QuantityUnit;

  association _PurchaseDocument;

  mapping for DEMO_PURCH_DOC_I corresponding;
}
```

In the behavior pool `BP_DEMO_CDS_PURCH_DOC_M`, the result parameter is declared as follows:

``` abap
result = VALUE #( FOR purchase IN lt_purchase 
                    ( %tky   = purchase-%tky 
                      %param = purchase ) ).
```abap
The class `CL_DEMO_CDS_PURCHASE` accesses the business object and executes the action `Approve_Order` for one entity instance\. 
Code snippet:
```abap
 MODIFY ENTITIES OF demo_cds_purch_doc_m 
    ENTITY PurchaseDocument 
    EXECUTE approve_order 
    FROM VALUE #( ( PurchaseDocument = 'a' ) ) 
    RESULT FINAL(result).
```

Result: the changed entity instance is stored in the `result` structure. ![figure](images_abdoc_result.jpg)

### Executable Example

The example from above is explained in detail in topic [RAP BDL - action](abenbdl_action1_abexa.md).

## Addition 1

`... deep`

### Description

When using the optional addition `deep`, the syntax for the output parameter is as follows:

`... deep result [selective] [cardinality] AbstractBDEF;`

The output parameter `AbstractBDEF` must be a [RAP abstract BDEF](../../abap-glossary/abencds_abstract_bdef_glosry.md) [`with hierarchy`](abenbdl_bdef_abstract_header.md). The BDEF derived type for an abstract BDEF is a hierarchy that contains all entity fields plus a component for every [CDS composition](../../abap-glossary/abencds_composition_glosry.md).

The optional addition `selective` can be specified to return only parts of the result structure.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF. The action `a2_deep_result` uses the abstract BDEF `DEMO_CDS_ABSTRACT_ROOT` as deep output parameter.

**Note:** This example is intentionally kept short and simple and serves demonstration purposes only. The [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) are not implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) here.

``` abap
managed implementation in class bp_demo_cds_deep_parameter unique;
strict(2);

define behavior for DEMO_CDS_DEEP_PARAMETER
persistent table DEMO_BO_DEEP
lock master
authorization master ( none )
{
  create;
  update;
  delete;

    mapping for demo_bo_deep
    {
    RootBO = root;
    }

  field (readonly:update) RootBO;

// mapping: none
  action a2_from_flat              parameter DEMO_CDS_ABSTRACT_ROOT;

// mapping: structure
  action a2_from_deep       deep  parameter DEMO_CDS_ABSTRACT_ROOT;

 // mapping: table
  action a2_from_deep_table deep table
                                  parameter DEMO_CDS_ABSTRACT_ROOT;

//deep selective output parameter
  action a2_deep_result deep result selective [1]
    DEMO_CDS_ABSTRACT_ROOT;
}
```

## Addition 2

`... selective`

### Description

With the optional addition `selective`, it is possible to return only parts of the result structure, for example the keys only. This can help to improve performance.

An implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is required. If `selective` is specified in the BDEF, the action or function signature has the additional input parameter `REQUEST requested fields`, which marks all requested fields with `01`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF based on the CDS view entity `DEMO_RAP_MANAGED_SELECTIVE_1`. It defines the function `myfunction` with a selective result.

``` abap
managed implementation in class bp_demo_rap_managed_selectiv_1 unique;
strict(2);

define behavior for DEMO_RAP_MANAGED_SELECTIVE_1
persistent table demo_dbtab_root
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field(readonly:update) KeyFieldRoot;

  function (authorization:none) myfunction result selective [1] $self;

  mapping for demo_dbtab_root
  {
    KeyFieldRoot = key_field;
    DataFieldRoot = data_field;
    CharFieldRoot = char_field;
    LastChangedAt = lchg_date_time;
    Timestamp = crea_date_time;
  }
}
```

In the ABAP behavior pool, the instance function `myfunction` is implemented so that it reads the values of all fields and returns them in the result structure. The result structure interprets the importing parameter `requested_fields` and fills only those fields that are requested by the EML consumer.

Code snippet:

``` abap
METHOD myfunction. 
  DATA(lt_keys) = keys. 
  CHECK lt_keys IS NOT INITIAL. 
 
  READ ENTITIES OF demo_rap_managed_selective_1 IN LOCAL MODE 
    ENTITY demo_rap_managed_selective_1 
      FIELDS ( KeyFieldRoot 
               CharFieldRoot 
               DataFieldRoot 
               Timestamp 
               LastChangedAt ) 
      WITH CORRESPONDING #( lt_keys ) 
    RESULT DATA(lt_item) 
    FAILED DATA(read_failed). 
 
  LOOP AT lt_item ASSIGNING FIELD-SYMBOL(<fs_item>). 
    APPEND VALUE #( %tky   = <fs_item>-%tky 
                    %param-keyfieldroot = COND #( 
                    WHEN requested_fields-KeyFieldRoot 
                    EQ if_abap_behv=>mk-on 
                    THEN  <fs_item>-KeyFieldRoot ) 
                     %param-charfieldroot = COND #( 
                     WHEN requested_fields-charfieldRoot 
                     EQ if_abap_behv=>mk-on 
                    THEN  <fs_item>-charFieldRoot ) 
                    %param-datafieldroot = COND #( 
                    WHEN requested_fields-datafieldRoot 
                    EQ if_abap_behv=>mk-on 
                    THEN  <fs_item>-dataFieldRoot ) 
                     %param-timestamp = COND #( 
                     WHEN requested_fields-timestamp 
                     EQ if_abap_behv=>mk-on 
                    THEN  <fs_item>-timestamp ) 
                     %param-lastchangedat = COND #( 
                     WHEN requested_fields-lastchangedat 
                     EQ if_abap_behv=>mk-on 
                    THEN  <fs_item>-lastchangedat ) 
                      ) TO result. 
  ENDLOOP. 
ENDMETHOD.
```

For the complete implementation in the ABAP behavior pool, see `BP_DEMO_RAP_MANAGED_SELECTIV_1CCIMP`.

The class `CL_DEMO_RAP_MANAGED_SELECTIVE` accesses the business object and executes the action `myfunction`. It requests only the fields `KeyFieldRoot` and `Timestamp` and therefore, the result structure displays only the values of these two fields.

Code Snippet:

``` abap
READ ENTITIES OF demo_rap_managed_selective_1 
 ENTITY demo_rap_managed_selective_1 
  EXECUTE myfunction 
  FROM VALUE #( (  %tky-KeyFieldRoot =  1 ) ) 
  REQUEST VALUE #( 
    KeyFieldRoot = if_abap_behv=>mk-on 
    Timestamp = if_abap_behv=>mk-on ) 
 RESULT FINAL(result) 
 FAILED FINAL(entity_failed) 
 REPORTED FINAL(entity_reported).
```

The following image shows that the importing parameter `requested_fields` marks the field requested by the EML consumer with `01`. ![figure](images_abdoc_requested_fields.jpg)

Result: the result structure contains only the values of the requested fields. ![figure](images_abdoc_result_1.jpg)

## Addition 3

`... [cardinality]`

### Description

Defines the [cardinality](../../abap-glossary/abencardinality_glosry.md) of the output parameter. This is a mandatory addition. The square brackets are part of the syntax. The following values can be specified for cardinality:

- `[0..1]`

- `[1]`

- `[0..*]`

- `[1..*]`
