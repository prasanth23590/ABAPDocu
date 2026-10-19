---
title: "RAP - event"
source_file: abenbdl_event.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - Events"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - event

## Syntax

``` abap
event EventName [[deep] parameter ParamName];  
```

## Description

Defines a [RAP business event](../../abap-glossary/abenrap_entity_event_glosry.md) in a [managed](../../abap-glossary/abenmanaged_rap_bo_glosry.md) or [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md). A RAP business event is a data record that expresses a significant change in the state of a [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md). An interested party that has subscribed to this event can consume and process it.

An [input parameter](../../abap-glossary/abeninput_parameter_glosry.md) `ParamName` can optionally be defined to specify the information that is passed to the event consumers. This information is called the [payload](../../abap-glossary/abenpayload_glosry.md) of the event.

- If `parameter ParamName` is specified, `ParamName` must be a [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md). The parameter is flat in this case. This means that the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) for the parameter contains a component for each field of the CDS abstract entity.

- If `deep parameter ParamName` is specified, `ParamName` must be an [abstract BDEF](../../abap-glossary/abencds_abstract_bdef_glosry.md) [`with hierarchy`](abenbdl_bdef_abstract_header.md). The parameter is deep in this case. This means that the BDEF derived type for the parameter is a hierarchy that contains all entity fields plus the components for every [CDS composition](../../abap-glossary/abencds_composition_glosry.md).

A RAP business event must be raised in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) of the RAP BO in question with the [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md) statement [`RAISE ENTITY EVENT`](../abap-for-rap-business-objects/abapraise_entity_event.md) in the [RAP late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md). In managed RAP BOs, it is recommended that a [RAP additional save](../../abap-glossary/abenrap_add_save_glosry.md) is specified using the syntax addition [`with additional save`](abenbdl_saving.md) and raise the RAP business event in this additional save implementation.

## Availability

- RAP business events can be defined in [managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md) and in [unmanaged RAP BOs](../../abap-glossary/abenunmanaged_rap_bo_glosry.md).

- RAP business events can be reused in [RAP interface behavior definitions](../../abap-glossary/abencds_interface_bdef_glosry.md) using the keyword `use event`. This is described in the topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

  Reusing RAP business events in [RAP projection behavior definitions](../../abap-glossary/abencds_proj_bdef_glosry.md) is not possible.

## Hint

Once a RAP business event has been created and raised, an event binding must be defined to map the event to an event type.

## More Information

Development guide for the ABAP RESTful Application Programming Model, section about [RAP Business Events](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/0b925bc556d4491aad395b21ec2566ff?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF based on the CDS root view entity `DEMO_RAP_EVENT`. It defines two events:

- `myEvent` defines a flat input parameter

- `myEvent1` defines a deep input parameter

``` abap
managed with additional save
implementation in class bp_demo_rap_event unique;
strict ( 2 );

define behavior for DEMO_RAP_EVENT alias Root
persistent table demo_dbtab_root
lock master
authorization master ( none )
{
  create;
  update;
  delete;

  field ( readonly : update ) key_field;

  event myEvent parameter demo_abstract_root_1;
  event myEvent1 deep parameter demo_abstract_root;
}
```

The following CDS abstract entity is used as flat parameter:

``` abap
@EndUserText.label: 'CDS root abstract entity, RAP event demo'
define abstract entity DEMO_ABSTRACT_ROOT_1
{
     col1: abap.int4;
     col2: abap.char(25);    
}
```

The following abstract BDEF is used as deep parameter:

``` abap
abstract;
strict(2);
with hierarchy;

define behavior for DEMO_ABSTRACT_ROOT
with control
{
  association _item1;
  association _item2;
  association _scalar;

  field ( mandatory:execute ) num1;

}

define behavior for DEMO_HIER_ABS_ITEM1
with control
{
  field ( suppress ) root2_id;
  association _root2 with hierarchy;
}

define behavior for DEMO_HIER_ABS_ITEM2
with control
{
}

scalar entity DEMO_HIER_ABS_SCALAR field char1;
```

The RAP business event is raised in the RAP saver method `save_modified` as follows:

``` abap
METHOD save_modified. 
  IF create-root IS NOT INITIAL. 
 
    RAISE ENTITY EVENT demo_rap_event~MyEvent 
      FROM VALUE #( 
        FOR var IN create-root ( 
            %param = VALUE #( col1 = var-data_field 
                              col2 = var-char_field ) ) ). 
  ENDIF. 
 
  IF update-root IS NOT INITIAL. 
 
    RAISE ENTITY EVENT demo_rap_event~MyEvent1 
      FROM VALUE #( 
        FOR var2 IN create-root ( 
            %param = VALUE #( char1 = var2-char_field 
                              num1 
= var2-data_field ) ) ). 
  ENDIF. 
ENDMETHOD.
```

The BDEF derived type of the flat parameter looks as follows: ![figure](images_flat_para.jpg)

The BDEF derived type of the deep parameter looks as follows: ![figure](images_deep_para2.jpg)
