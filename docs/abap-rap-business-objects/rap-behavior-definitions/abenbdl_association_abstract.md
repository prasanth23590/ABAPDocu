---
title: "RAP - Associations, Abstract BDEF"
source_file: abenbdl_association_abstract.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Abstract Behavior Definitions > RAP - Entity Behavior Definition, Abstract BDEF > RAP - Entity Behavior Body, Abstract BDEF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Associations, Abstract BDEF

## Syntax

``` abap
... association [(mandatory:execute)] _Assoc [with hierarchy];  
```

## Description

Includes a [CDS association](../../abap-glossary/abencds_association_glosry.md) in the hierarchical [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md). The keyword `association` is used for associations and for [CDS compositions](../../abap-glossary/abencds_composition_glosry.md). An entity whose child entity is included in the same [abstract BDEF](../../abap-glossary/abencds_abstract_bdef_glosry.md) **must** specify the respective composition using the keyword `association`. If no behavior is defined for a subnode, then the respective composition **must not** be specified.

The optional addition `mandatory:execute` declares an association of an abstract BDEF as mandatory. It can be used for [CDS compositions](../../abap-glossary/abencds_composition_glosry.md) and for [cross-BO associations](../../abap-glossary/abencds_cross_bo_assoc_glosry.md), but not for to-parent associations. Whenever the abstract BDEF is used as an [input parameter](abenbdl_action_input_param.md) for a [RAP action](../../abap-glossary/abenrap_action_glosry.md) or a [RAP function](../../abap-glossary/abenrap_function_glosry.md), a value must be supplied, that is, the [`%control`](../abap-for-rap-business-objects/abapderived_types_control.md) flag must be set. Otherwise, a [runtime error](../../abap-glossary/abenruntime_error_glosry.md) occurs. As a prerequisite, the addition [`with hierarchy`](abenbdl_bdef_abstract_header.md) must be used in the [behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md) and [`with control`](abenbdl_define_beh_abstract.md) must be specified for the [entity behavior definition](../../abap-glossary/abencds_entity_bdef_glosry.md) in question. In addition, the [BDEF strict mode](../../abap-glossary/abenrap_strict_mode_glosry.md) must be enabled. When using [`IN LOCAL MODE`](../abap-for-rap-business-objects/abapin_local_mode.md), `mandatory:execute` has no effect.

The optional addition `with hierarchy` can be used for [cross-BO associations](../../abap-glossary/abencds_cross_bo_assoc_glosry.md) that specify [`with hierarchy`](abenbdl_bdef_abstract_header.md) in the BDEF header. An association with this addition is handled like a composition: the target type is integrated (as structure or table, depending on the cardinality) into the source type. As a result, the association in question is included several times in the type structure. The definable structure thus generalizes from type tree to DAG (directed acyclic graph). Note that the addition `with hierarchy` must not be used for to-child associations or to-parent associations to avoid cyclical graphs.

The [association target](../../abap-glossary/abenassociation_target_glosry.md) of an association with the addition `with hierarchy` must be covered by an abstract BDEF `with hierarchy`. Typically, to-parent associations `with hierarchy` are used for local sub-structures, while cross-BO associations serve reuse.

[Type mappings](abenbdl_type_mapping_abstract.md) to other DDIC types continue to be defined in the BDEF containing the respective entity. Thus, if a hierarchical type is defined with cross-BO associations, its mapping to a hierarchical DDIC type spreads out across multiple abstract BDEFs.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following abstract BDEF defines behavior for four nodes, including intra- and cross-BO associations.

``` abap
abstract;
strict(2);
with hierarchy;

define behavior for DEMO_CDS_SCALAR_ROOT alias Root
with control
{
  association _sibling;

  association _item1;

  // key field, unwanted in dTypes
  field ( suppress ) key_field;

  deep mapping for demo_cds_scalar_1 corresponding
  {
    field1 = r_fd1;
    field2 = r_fd2;
    field3 = r_sib;

    sub _Item1 = sub_1;
  }
}

define behavior for DEMO_CDS_SCALAR_CHILD alias Child
with control
{
  // foreign key field for parent, unwanted in dTypes
  field ( suppress ) key_field, i1pfk;

  // hierarchy-enabled [*]-assoc to foreign entity
  association _i1_r2 with hierarchy;

  association _sub1;
  association _sub3;
  deep mapping for DEMO_CDS_SCALAR_3 corresponding
  {
    i1fd1 = i1_fd1;
    i1fd2 = i1_fd2;
    sub _sub1 = sub_1;
    sub _sub3 = sub_3;  // scalar (table)
    sub _i1_r2 = root2;  // cross-BO assoc [*] "with hierarchy"

  }
}

define behavior for DEMO_CDS_SCALAR_GRANDCHILD_1 alias Grandchild1
with control
{
  field ( suppress ) s1key, s1pfk, s1rfk;

  mapping for DEMO_CDS_SCALAR_5 corresponding
  {
    s1fd1 = s1_fd1;
    s1fd2 = s1_fd2;
  }
}

scalar entity DEMO_CDS_SCALAR_GRANDCHILD_2 field s3val;
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates the effect of the attribute `mandatory:execute`.

The abstract BDEF `DEMO_CDS_ABSTRACT_ROOT_ME` defines the association `_child` as `mandatory:execute`.

``` abap
abstract;
strict ( 2 );
with hierarchy;

define behavior for DEMO_CDS_ABSTRACT_ROOT_ME alias Root
with control
{
  field ( mandatory : execute ) id, comp1;
  association ( mandatory : execute ) _child;
}

define behavior for DEMO_CDS_ABSTRACT_CHILD_ME alias Child
with control
{
  field ( mandatory : execute ) iid, comp2;
  association _root;
}
```

The managed BDEF `DEMO_RAP_MANDATORY_EXEC_ASSOC` defines an action `Action1`. This action specifies the abstract BDEF`DEMO_CDS_ABSTRACT_ROOT_ME` as deep output parameter.

``` abap
managed implementation in class bp_demo_rap_mandatory_exec_ass unique;
strict ( 2 );

define behavior for DEMO_RAP_MANDATORY_EXEC_ASSOC
persistent table demo_ddic_types
lock master
authorization master ( none )
{
  create;
  update;
  delete;

  field ( readonly : update ) id;

  action ( authorization : none ) Action1 deep parameter
      DEMO_CDS_ABSTRACT_ROOT_ME;
}
```

The ABAP class `CL_DEMO_MANDATORY_EXECUTE_ASSO` executes the action `ACTION1`. It sets the [`%control`](../abap-for-rap-business-objects/abapderived_types_comp.md) structure for the association `_child` to `if_abap_behv=>mk-on`. This is mandatory, since this association is marked as `mandatory:execute` in the abstract BDEF that is used as input parameter. If the `%control` structure were set to `if_abap_behv=>mk-off` or not provided at all, a runtime error would occur.

Code Snippet:

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: 
      "Derived type for abstract entity; 
      par1 TYPE TABLE FOR ACTION IMPORT 
        demo_rap_mandatory_exec_assoc~action1. 
 
par1 = VALUE #( ( 
  id     = 'A' 
  %param = VALUE #( 
     %control = VALUE #( 
        id     = if_abap_behv=>mk-on 
        comp1  = if_abap_behv=>mk-on 
        _child = if_abap_behv=>mk-on 
        ) 
        _child   = VALUE #( 
          %control = VALUE #( 
            iid   = if_abap_behv=>mk-on 
            comp2 = if_abap_behv=>mk-on ) ) ) 
                ) ). 
 
"Executing Action1 
MODIFY ENTITY demo_rap_mandatory_exec_assoc 
   EXECUTE action1 
   FROM par1 
    MAPPED FINAL(ls_mapped2) 
    REPORTED FINAL(ls_reported2) 
    FAILED FINAL(ls_failed2). 
 
out->write( `Action1 successfully called` ). 
 
out->display( ).
```
