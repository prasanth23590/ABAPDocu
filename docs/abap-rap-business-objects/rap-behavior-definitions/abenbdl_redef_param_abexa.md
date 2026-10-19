---
title: "RAP - Reuse with Redefined Parameter"
source_file: abenbdl_redef_param_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Projection Behavior Definitions > RAP - EntityBehaviorDefinition, Projection BDEF > RAP - EntityBehaviorBody, Projection BDEF > RAP - use, Projection and Interface BDEF > RAP - RedefinedParameter"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Reuse with Redefined Parameter

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how input and output parameters of [RAP actions](../../abap-glossary/abenrap_action_glosry.md), [RAP functions](../../abap-glossary/abenrap_function_glosry.md), and [RAP business events](../../abap-glossary/abenrap_entity_event_glosry.md) can be redefined in a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md) or in an [interface BDEF](../../abap-glossary/abencds_interface_bdef_glosry.md).

**Note:** This example does not fully meet the requirements of the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). It is intentionally kept short and simple and focuses on specific RAP aspects. For example, some [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) implementations might be empty. See more information on the RAP BO contract in the [Development guide for the ABAP RESTful Application Programming Model](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

**Definition of abstract BDEFs as parameters**

The following CDS abstract entity defines a data type with three components. The `ROOT` keyword is required to use the abstract entity as the basis of an abstract BDEF.

``` abap
@EndUserText.label: 'Demo for parameter redefinition'
define root abstract entity Demo_Rap_Abstract_All_Fields
  
{
    comp1: abap.int4;
    comp2: abap.char(20);
    comp3: abap.char(20);
    
}
```

The following CDS abstract entity defines a data type with two components. It is a subset of the data type with three components displayed above. The `ROOT` keyword is required to use the abstract entity as the basis of an abstract BDEF.

``` abap
@EndUserText.label: 'Demo for parameter redefinition'
define root abstract entity DEMO_RAP_ABSTRACT_SUB_FIELDS

{
  comp2 : abap.char(20);
  comp3 : abap.char(20);
}
```

The redefinition of parameters is possible only for deep parameters. Deep parameters are always defined as abstract BDEFs. The following abstract BDEF is used as a deep parameter for base operations and events.

``` abap
abstract;
strict ( 2 );
with hierarchy;

define behavior for Demo_Rap_Abstract_All_Fields
with control
{
}
```

The following abstract BDEF is used as a redefined deep parameter in an interface BDEF. It contains a type mapping that maps the fields of the base data type to the fields of the redefined data type.

``` abap
abstract;
strict ( 2 );
with hierarchy;

define behavior for DEMO_RAP_ABSTRACT_SUB_FIELDS
with control


{
  deep mapping for demo_rap_abstract_all_fields
    {
      comp2 = comp2;
      comp3 = comp3;
    }
}
```

**Managed RAP BO**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_RAP_REDEFINE_PARAM` defines an action, two functions, and an event with deep input and output parameters.

``` abap
managed implementation in class bp_demo_rap_redefine_param unique;
strict ( 2 );
extensible;

define behavior for DEMO_RAP_REDEFINE_PARAM
persistent table demo_dbtab_root
lock master
authorization master ( none )
extensible

{
  create;
  update;
  delete;

  field(readonly:update) key_field;

  action Action1 deep parameter Demo_Rap_Abstract_All_Fields;

  function (authorization:none) Function1
    deep result[1] Demo_Rap_Abstract_All_Fields;
  function (authorization:none) Function2
    deep parameter Demo_Rap_Abstract_All_Fields
    result[1] $self;

  event Event1 deep parameter Demo_Rap_Abstract_All_Fields;
}
```

The function `Function1` is implemented in the ABAP behavior pool as displayed below. It reads fields and returns a result parameter.

``` abap
METHOD Function1. 
  DATA(lt_keys) = keys. 
  CHECK lt_keys IS NOT INITIAL. 
 
  READ ENTITIES OF demo_rap_redefine_param IN LOCAL MODE 
    ENTITY demo_rap_redefine_param 
      FIELDS ( key_field char_field ) 
      WITH CORRESPONDING #( lt_keys ) 
    RESULT DATA(lt_item) 
    FAILED DATA(read_failed). 
 
  failed = CORRESPONDING #( DEEP read_failed ). 
 
  result = VALUE #( FOR ls_agency IN lt_item ( 
                    %param-comp1 = '4' 
                    %param-comp2 = 'baseComp2' 
                    %param-comp3 = 'baseComp3' ) ). 
ENDMETHOD.
```

The action `Action1` is implemented in the ABAP behavior pool as displayed below. It writes a value provided by the input parameter into the field `CHAR_FIELD`.

``` abap
METHOD Action1. 
  MODIFY ENTITIES OF demo_rap_redefine_param IN LOCAL MODE 
  ENTITY demo_rap_redefine_param 
  UPDATE FIELDS ( char_field ) 
  WITH VALUE #( FOR ls_key IN keys ( 
                %tky                = ls_key-%tky 
                %data-char_field    = ls_key-%param-comp1 
                %control-char_field = if_abap_behv=>mk-on ) ). 
ENDMETHOD.
```

**RAP BO interface with redefined parameters**

The following BDEF of type `interface` reuses the action, functions, and event from the base BDEF. It replaces the input and output parameters of the base operations with the projection-specific parameter `DEMO_RAP_ABSTRACT_SUB_FIELDS`.

``` abap
interface;
extensible;

define behavior for DEMO_RAP_REDEFINE_PARAM_I alias Interface
{
  use create;
  use update;
  use delete;

  use action Action1 deep parameter DEMO_RAP_ABSTRACT_SUB_FIELDS ;
  use function Function1 deep result DEMO_RAP_ABSTRACT_SUB_FIELDS;
  use function Function2 deep parameter DEMO_RAP_ABSTRACT_SUB_FIELDS;

  use event Event1 deep parameter DEMO_RAP_ABSTRACT_SUB_FIELDS;
}
```

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
CLASS cl_demo_rap_redefine_param DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_redefine_param IMPLEMENTATION. 
  METHOD main. 
 
    DELETE FROM demo_dbtab_root. 
    INSERT demo_dbtab_root FROM TABLE @( VALUE #( 
           ( key_field = 1 char_field = 'A' ) 
           ( key_field = 2 char_field = 'B' ) 
           ( key_field = 3 char_field = 'C' ) 
           ( key_field = 4 char_field = 'D' ) ) ). 
 
    "execute base function. result structure contains 3 components. 
    READ ENTITIES OF demo_rap_redefine_param 
    ENTITY demo_rap_redefine_param 
    EXECUTE Function1 
    FROM VALUE #( ( %tky-key_field = '1' ) 
                  ( %tky-key_field = '2' ) ) 
    RESULT FINAL(result) 
    FAILED FINAL(failed) 
    REPORTED FINAL(reported). 
 
    "execute interface function. result structure has only 2 components 
    READ ENTITIES OF demo_rap_redefine_param_i 
    ENTITY Interface 
    EXECUTE Function1 
    FROM VALUE #( ( %tky-key_field = '1' ) 
                  ( %tky-key_field = '2' ) ) 
    RESULT FINAL(result1) 
    FAILED FINAL(failed1) 
    REPORTED FINAL(reported1). 
 
    "execute base action 
    MODIFY ENTITIES OF demo_rap_redefine_param 
        ENTITY demo_rap_redefine_param 
        EXECUTE Action1 
        FROM VALUE #( ( key_field    = 1 
                        %param-comp1 = 999 
                        %param-comp2 = 999 
                        %param-comp3 = 999 ) ) 
        FAILED FINAL(failed2) 
        REPORTED FINAL(reported2). 
 
    COMMIT ENTITIES. 
 
    SELECT key_field, char_field 
    FROM demo_dbtab_root 
    INTO TABLE @FINAL(result3). 
 
    "execute interface action 
    MODIFY ENTITIES OF demo_rap_redefine_param_i 
    ENTITY Interface 
    EXECUTE Action1 
    FROM VALUE #( ( key_field    = 1 
*                   %param-comp1 = 999 -> syntax check error because 
                    "comp1 is not part of the redefined input parameter 
                    %param-comp2 = 999 %param-comp3 = 999 ) 
                ) 
    FAILED FINAL(failed3) 
    REPORTED FINAL(reported3). 
 
    COMMIT ENTITIES. 
    SELECT key_field, char_field 
       FROM demo_dbtab_root 
       INTO TABLE @FINAL(result4). 
 
    out->next_section( 'Base function result' 
        )->write( result 
        )->next_section( 'Interface function result' 
        )->write( result1 
        )->next_section( 'Base action result' 
        )->write( result3 
        )->next_section( 'Interface action result' 
        )->write( result4 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- First, it inserts data into the database table using ABAP SQL `INSERT`.

- It executes the function `Function1` from the base BDEF and from the interface BDEF. The result parameter differs between the two executions. In the first execution, the result parameter has three components. In the second execution, the result parameter has only two components. The component `comp1` is not a part of the result structure, since `comp1` is not part of the redefined output parameter.

- It executes the action `Action1` from the base BDEF and from the interface BDEF. The second execution from the interface BDEF does not accept an input for `comp1`, since `comp1` is not part of the redefined input parameter.
