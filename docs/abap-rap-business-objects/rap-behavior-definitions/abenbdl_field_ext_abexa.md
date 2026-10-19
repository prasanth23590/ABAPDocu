---
title: "RAP - Field Extension"
source_file: abenbdl_field_ext_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension > RAP - EntityBehaviorExtension > RAP - ExtensionBody > RAP - Adding Elements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Field Extension

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how extension fields are added and behavior-enabled in a RAP BO extension scenario.

## Original RAP BO

**DDIC data model**

The DDIC data model consists of one database table: `DEMO_ROOT_EXT`:

``` abap
@EndUserText.label : 'Database Table for Root Entity of RAP BO'
@AbapCatalog.enhancement.category : #EXTENSIBLE_ANY
@AbapCatalog.tableCategory : #TRANSPARENT
@AbapCatalog.deliveryClass : #A
@AbapCatalog.dataMaintenance : #ALLOWED
define table demo_root_ext {

  key client    : mandt not null;
  key key_field : abap.int4 not null;
  data_field    : abap.string(0);
  char_field    : abap.char(25);
  char_field_2  : abap.char(25);
  dec_field     : abap.dec(15,2);
  include demo_extension;

}
```

This database table includes structure `DEMO_EXTENSION`.

``` abap
@EndUserText.label : 'Used for demo of RAP BO extension'
@AbapCatalog.enhancement.category : #EXTENSIBLE_ANY
define structure demo_extension {

  crea_date_time : timestampl;
  lchg_date_time : timestampl;

}
```

**CDS data model**

The CDS data model consists of one root entity without child entities: `DEMO_RAP_FIELD_EXT`:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, RAP BO ext'
@AbapCatalog.extensibility.extensible: true
@AbapCatalog.extensibility.dataSources: ['A']
define root view entity DEMO_RAP_FIELD_EXT
  as select from demo_root_ext as A

{
  key key_field  as KeyField,
//      data_field as DataField,
      char_field as CharField,
      dec_field  as DecField
}
```

**CDS transactional interface**

The following CDS transactional interface is created as stable public interface for extensions:

``` abap
@EndUserText.label: 'CDS transactional interface, RAP BO ext'
@AccessControl.authorizationCheck: #NOT_REQUIRED
@AbapCatalog.extensibility.dataSources: [ 'A' ]
define root view entity DEMO_RAP_FIELD_EXT_INT 
provider contract transactional_interface
as projection on DEMO_RAP_FIELD_EXT as A
{
  key KeyField,
//  DataField,
  CharField,
  DecField
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_RAP_FIELD_EXT` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as shown below. It defines global authorization control and adds field attributes to multiple fields.

``` abap
managed implementation in class bp_demo_rap_field_ext unique;
strict(2);
extensible;

define behavior for DEMO_RAP_FIELD_EXT alias Root
persistent table demo_root_ext
lock master
authorization master ( global )
extensible
{
  create;
  update;
  delete;

  field ( mandatory : create, readonly : update ) KeyField;
  field ( features : instance ) DecField;
//  field(readonly) CharField;

  mapping for demo_root_ext corresponding extensible
  {
    KeyField = key_field;
//    DataField = data_field;
    CharField = char_field;
    DecField = dec_field;
  }
}
```

**Behavior implementation**

For the RAP behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_RAP_FIELD_EXT`, see `BP_DEMO_RAP_FIELD_EXT=========CCIMP`. This global class implements two methods:

- `get_instance_features`: Implements dynamic feature control for field `DecField`: If field `CharField` has value *A*, then field `DecField` is read-only. If field `CharField` has any other value, then field `DecField` can be accessed without any restrictions.

- `get_global_auth`: Defines global feature control for the complete RAP BO: Update requests are generally authorized and delete requests are generally unauthorized.

**RAP BO Interface**

The following RAP BO interface is used as stable public interface for extensions.

``` abap
interface;
extensible;

define behavior for DEMO_RAP_FIELD_EXT_INT alias Root
{
  use create;
  use update;
  use delete;
}
```

## Extension RAP BO

**DDIC data model extension**

Extension fields are added to the DDIC data model via the structure extension `DEMO_EXTEND_STR`:

``` abap
@EndUserText.label : 'Used for demo of RAP BO extension'
@AbapCatalog.enhancement.category : #NOT_EXTENSIBLE
extend type demo_extension with demo_extend_str {

  data_field_ext : abap.string(0);
  char_field_ext : abap.char(25);
  int_field_ext  : abap.int4;
  num_field_ext  : abap.int2;
  int1_field_ext : abap.int1;

}
```

**CDS data model extension**

The extension fields are added to the CDS data model via the CDS view entity extension `DEMO_EXTENSION_RAP_BO`:

``` abap
extend view entity DEMO_RAP_FIELD_EXT with
{
//  demo_root_ext.data_field_ext,
  A.char_field_ext,
  A.int_field_ext,
  A.num_field_ext,
  A.int1_field_ext
}
```

**CDS transactional interface extension**

The extension fields are added to the CDS transactional interface by means of an entity extension `DEMO_RAP_TI_FIELD_EXT`:

``` abap
extend view entity DEMO_RAP_FIELD_EXT_INT with
{
//  DEMO_RAP_FIELD_EXT.data_field_ext as DataFieldExt,
  A.char_field_ext as CharFieldExt,
  A.int_field_ext  as IntFieldExt,
  A.num_field_ext  as NumFieldExt,
  A.int1_field_ext as Int1FieldExt
}
```

**BDEF extension**

The BDEF extension `DEMO_EXTENSION_RAP_BO` adds field attributes to the extension fields using the BDEF interface.

``` abap
extension using interface DEMO_RAP_FIELD_EXT_INT
 implementation in class bp_demo_extension_rap_bo unique;

extend behavior for Root
{

//  field ( readonly ) DataFieldExt;
  field ( mandatory ) IntFieldExt;
  field ( suppress ) CharFieldExt;
  field ( features : instance ) NumFieldExt;

  field ( readonly : update ) Int1FieldExt;
}
```

**ABP extension**

The ABP extension is implemented in the global class `BP_DEMO_EXTENSION_RAP_BO`, see `BP_DEMO_EXTENSION_RAP_BO======CCIMP`. This global class implements dynamic feature control for the extension field `NumFieldExt`: If the value of field `IntFieldExt` is greater than 1000, then field `NumFieldExt` is read-only. If the value of field `IntFieldExt` is less than or equal to 1000, access to field `NumFieldExt` is unrestricted.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_rap_field_ext DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_field_ext IMPLEMENTATION. 
  METHOD main. 
 
    DELETE FROM demo_root_ext. 
    MODIFY ENTITIES OF demo_rap_field_ext_int 
         ENTITY root 
           CREATE 
             FIELDS ( keyfield charfield intfieldext ) WITH VALUE #( 
              ( %cid = '1' 
                keyfield = 1 
                charfield = 'A' 
                intfieldext = 2000 ) 
              ( %cid = '2' 
                keyfield = 2 
                charfield = 'B' 
                intfieldext = 500 ) ) 
               MAPPED DATA(mapped) 
               FAILED DATA(failed) 
               REPORTED DATA(reported). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred ` && 
      `in the RAP save sequence.` ). 
    ENDIF. 
 
    MODIFY ENTITIES OF demo_rap_field_ext_int 
          ENTITY root 
          UPDATE FIELDS ( charfield numfieldext ) WITH VALUE #( 
          ( keyfield = 1 charfield = 'A' numfieldext = 7 ) 
          ( keyfield = 2 charfield = 'B' numfieldext = 7 ) ) 
             MAPPED mapped 
             FAILED  failed 
             REPORTED reported. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred ` && 
      `in the RAP save sequence.` ). 
    ENDIF. 
 
    DATA itab TYPE TABLE OF string WITH EMPTY KEY. 
    LOOP AT reported-root ASSIGNING FIELD-SYMBOL(<fs>). 
      APPEND `Instance key: ` && 
      <fs>-keyfield && 
      `, ` && 
       reported-root[ sy-tabix ]-%msg->m_severity  && 
       `: ` && 
      reported-root[ sy-tabix ]-%msg->if_message~get_text(  ) 
        TO itab. 
    ENDLOOP. 
    out->write( itab ). 
    SELECT key_field, char_field, data_field, 
           int_field_ext, num_field_ext 
    FROM demo_root_ext 
    INTO TABLE @FINAL(result). 
    out->write( result ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The source code above uses [ABAP EML](../../abap-glossary/abeneml_glosry.md) to access the [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) from an ABAP class:

- It inserts two entity instances using [`MODIFY ENTITIES CREATE`](../abap-for-rap-business-objects/abapmodify_entity_entities_op.md).

- It updates both entity instances using [`MODIFY ENTITIES UPDATE`](../abap-for-rap-business-objects/abapmodify_entity_entities_op.md).

For the entity instance with key value *1*, the field `NumFieldExt` is dynamically set to read-only by the field feature control. This field is not updated, but error messages are returned.

Execution order for `CREATE`:

- Global authorization control specified in the original ABP.

Execution order for `UPDATE`:

- Global authorization control specified in the original ABP.

- Field feature control specified in the original ABP.

- Field feature control specified in the extension ABP.
