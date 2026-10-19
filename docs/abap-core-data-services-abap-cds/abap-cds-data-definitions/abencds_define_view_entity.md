---
title: "CDS DDL - DEFINE VIEW ENTITY"
source_file: abencds_define_view_entity.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE VIEW ENTITY

## Syntax

``` abap
[@entity_annot1] 
[@entity_annot2] 
... 
[@view_entity_annot1] 
[@view_entity_annot2] 
... 
[DEFINE] [WRITABLE] [ROOT] VIEW ENTITY view_entity 
        [parameter_list] 
         AS select_statement [;]...  
```

[`@entity_annot1`](abencds_f1_entity_annotations.md) · [`@entity_annot2`](abencds_f1_entity_annotations.md) · [`@view_entity_annot1`](abencds_view_entity_anno.md) · [`@view_entity_annot2`](abencds_view_entity_anno.md) · [`WRITABLE`](abencds_define_wrtbl_view_v2.md) · [`ROOT`](abencds_define_root_view_v2.md) · [`parameter_list`](abencds_parameter_list_v2.md) · [`select_statement`](abencds_select_statement_v2.md)

### Addition

[1. `... WRITABLE ...`](abencds_define_view_entity.md#addition-1)

[2. `... ROOT ...`](abencds_define_view_entity.md#addition-2)

## Overview

### Description

Defines a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). A CDS view entity is implemented using a [`select_statement`](abencds_select_statement_v2.md).

The name of the CDS view entity is defined after the `DEFINE VIEW ENTITY` statement. The usual rules for ABAP Dictionary views apply to this name and it is not case-sensitive (it is transformed internally into uppercase letters). It can have a maximum of 30 characters and is in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP. The name of the DDL source and of the CDS entity must be identical.

The CDS view entity can be enriched with [entity annotations](abencds_f1_entity_annotations.md) (these are annotations that can be used in all CDS entities) or with [view entity annotations](abencds_view_entity_anno.md) (these are annotations that are only available for CDS view entities). All annotations are optional and a view entity can also be created without any annotation.

[`parameter_list`](abencds_parameter_list_v2.md) can be used to assign input parameters to the view. These input parameters can be specified in operand positions of the view and can be assigned actual parameters when the view is used.

### Hints

- [ABAP annotations](abencds_view_entity_anno.md) can be used to assign further technical and semantic properties to a view for evaluation by the ABAP runtime framework. [Framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be used to assign further semantic properties to a view that are evaluated by other SAP frameworks.

- If a [CDS role](../../abap-glossary/abencds_role_glosry.md) is defined for a CDS entity using the CDS-DCL statement [`DEFINE ROLE`](../abap-cds-access-control/abencds_f1_define_role.md), implicit [access control](../../abap-glossary/abencds_access_control_glosry.md) applies by default when the CDS entity is accessed using ABAP SQL. CDS access control can be switched off using the value `#NOT_ALLOWED` for the annotation [`@AccessControl.authorizationCheck`](abencds_view_entity_anno.md) and using the addition [`WITH PRIVILEGED ACCESS`](../../abap-programming-language/abap-database-access/abapselect_data_source.md) in the [`FROM`](../../abap-programming-language/abap-database-access/abapfrom_clause.md) clause of an ABAP SQL query.

- After a CDS view entity has been transported, its name can no longer be changed.

- The programming of CDS views using the DDL of the Core Data Services is one of the tasks included in the implementation of data models and is not usually the responsibility of regular ABAP application programmers. Once created, CDS views are used in ABAP programs using ABAP SQL read statements and must be stable enough to allow this.

- Every CDS view entity has its own [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md). The DDL source code of a CDS view entity is edited in a different editor than the [DDLA source code](../../abap-glossary/abenddla_source_code_glosry.md) of an [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md), the [DDLX source code](../../abap-glossary/abenddlx_source_code_glosry.md) of a [CDS metadata extension](../../abap-glossary/abencds_metadata_extension_glosry.md), and the [DCL source code](../../abap-glossary/abendcl_source_code_glosry.md) of a [CDS role](../../abap-glossary/abencds_role_glosry.md). The [ADT](../../abap-glossary/abenadt_glosry.md) documentation describes how the different types of source code are created.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS view entity `DEMO_SALES_CDS_BUPA_VE` contains information about a business partner. It selects data from the database table `DEMO_SALES_BUPA`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'SDDL: Interface (BO) View for BuPa'
define root view entity DEMO_SALES_CDS_BUPA_VE
  as select from
    demo_sales_bupa as bupa
    {
      key id,
          given_name,
          middle_name,
          family_name
    }
```

## Addition 1

`... WRITABLE ...`

### Description

The addition [`WRITABLE`](abencds_define_wrtbl_view_v2.md) is optional. It defines the CDS view entity as [writable](../../abap-glossary/abenwritable_v2_glosry.md) For further details, see the topic [CDS DDL - CDS View Entity, `WRITABLE`](abencds_define_wrtbl_view_v2.md).

## Addition 2

`... ROOT ...`

### Description

The addition [`ROOT`](abencds_define_root_view_v2.md) is optional. It defines the CDS view entity as root entity of a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) in the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md). For further details, see topic [CDS DDL - CDS View Entity, `ROOT`](abencds_define_root_view_v2.md).
