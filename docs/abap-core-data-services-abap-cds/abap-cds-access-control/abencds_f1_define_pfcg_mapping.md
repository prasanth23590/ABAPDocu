---
title: "CDS DCL - DEFINE PFCG_MAPPING"
source_file: abencds_f1_define_pfcg_mapping.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ACCESSPOLICY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE PFCG_MAPPING

## Syntax

``` abap
[pfcg_mapping_annot] 
[DEFINE] PFCG_MAPPING pfcg_mapping(output1[, output2 ...]) 
  BETWEEN mapping_entity AND auth_object [IN SCENARIO scenario_name] 
  { input1 = auth_field1 [CONSTRAINT ID][, 
    input2 = auth_field2 [CONSTRAINT ID] ... ] }  
```

[`pfcg_mapping_annot`](abencds_f1_dcl_pm_annotations.md)

### Addition

[`... IN SCENARIO`](abencds_f1_define_pfcg_mapping.md#addition)

## Description

Defines a [PFCG mapping](../../abap-glossary/abencds_pfcg_mapping_glosry.md) `pfcg_mapping` as part of a [CDS access policy](../../abap-glossary/abencds_access_policy_glosry.md) defined using [`DEFINE ACCESSPOLICY`](abencds_f1_define_accesspolicy.md). The name of the PFCG mapping must match the name of the CDS access policy.

The definition of a PCFG mapping contains the following:

- A comma-separated list after the name `pfcg_mapping` in which the output fields of the PFCG mapping are defined. These fields must be elements of the CDS entity `mapping_entity` specified after `BETWEEN`. The specified order is relevant.

- A CDS entity `mapping_entity` specified after the keyword `BETWEEN` to define the fields used in the mapping. This definition specifies the input and output fields of the mapping.

- An [authorization object](../../abap-glossary/abenauthorization_object_glosry.md) `auth_object` specified after the keyword `AND`. The PFCG mapping can be [used](abencds_f1_cond_pfcg_mapping.md) in exactly those [PFCG conditions](abencds_f1_cond_pfcg.md) in which this authorization object is specified after `ASPECT pfcg_auth`.

- A comma-separated unordered list in curly brackets that associates the input fields `input1`, `input2`, ... of the mapping with [authorization fields](../../abap-glossary/abenauthorization_field_glosry.md) `auth_field` of the authorization object `auth_object`.

  - The input fields on the left sides must be elements of the CDS entity `mapping_entity` specified after `BETWEEN`.

  - Authorization fields of the authorization object `auth_object` must be specified on the right sides.

  - Any number of optional assignments can be flagged using the addition `CONSTRAINT ID`.

A PFCG mapping can be [used](abencds_f1_cond_pfcg_mapping.md) in a [PFCG](abencds_f1_cond_pfcg.md) condition of the same authorization object. It is transformed to specific access conditions as follows when the condition is evaluated:

- The values of the current user for the authorization fields assigned to the input fields fill the input fields of the mapping.

- The output fields of the mapping are assigned to the elements within the [curly brackets](abencds_f1_cond_pfcg_mapping.md) of the PFCG condition in the specified order.

- The following applies to the input fields flagged with `CONSTRAINT ID`:

  - Only those authorization fields of the authorization object can be assigned that contain a single value in a specific authorization. Multiple values or patterns are not allowed (with the exception of full authorization using the value *\**). Otherwise the PFCG mapping in the PFCG condition returns the value *false* for the authorization in question.

  - Full authorization can be assigned only when applied to all input fields of the PFCG mapping.

- If full authorization exists for all input fields of the PFCG mapping (value *\**), the PFCG mapping in the PFCG condition returns the value *true* when evaluated. This makes it possible to read entries of the protected entity for which there are no output fields in the mapping.

## Hint

In ABAP SQL access to a CDS entity assigned a role of this type, PFCG mappings are defined internally using a subquery after `EXISTS`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows the definition of a PFCG mapping `demo_cds_auth_pfcg_mapping` based on the CDS entity `demo_cds_mapping_entity` below. The output fields of the PFCG mapping are the authorization fields `OBJECT`, `OBJ_NAME`, and `DEVCLASS` of the authorization object `S_DEVELOP`. The input fields of the PFCG mapping are the elements of the CDS entity to which the output fields are assigned. The [example](abencds_f1_cond_pfcg_mapping.md) that demonstrates how a PFCG mapping is specified in a role shows how the mapping is used.

- **PFCG Mapping**

``` abap
CDS or DDIC source code was not found
```

- **CDS Entity**

``` abap
define view entity demo_cds_mapping_entity
  as select from
    tadir
    {
      devclass as map_devclass,
      object   as map_object,
      obj_name as map_obj_name
    }
    where
          devclass =    'SABAPDEMOS'
      and object   =    'PROG'
      and obj_name like 'DEMO%'
```
