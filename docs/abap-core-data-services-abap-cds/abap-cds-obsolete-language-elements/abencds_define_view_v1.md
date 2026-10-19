---
title: "CDS DDL - DEFINE VIEW ddic_based"
source_file: abencds_define_view_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE VIEW ddic_based

## Syntax

``` abap
[@entity_annot1] 
[@entity_annot2] 
... 
@AbapCatalog.sqlViewName: 'CDS_DB_VIEW' 
[@view_annot1] 
[@view_annot2] 
... 
[DEFINE] [ROOT] VIEW ddic_based_view 
        [name_list] 
        [parameter_list] 
         AS select_statement [;]  
```

[`@entity_annot1`](../abap-cds-data-definitions/abencds_f1_entity_annotations.md) · [`@entity_annot2`](../abap-cds-data-definitions/abencds_f1_entity_annotations.md) · [`@AbapCatalog.sqlViewName: 'CDS_DB_VIEW'`](abencds_view_anno_v1.md) · [`@view_annot1`](abencds_view_anno_v1.md) · [`@view_annot2`](abencds_view_anno_v1.md) · [`ROOT`](abencds_define_root_view_v1.md) · [`name_list`](abencds_name_list_v1.md) · [`parameter_list`](abencds_parameter_list_v1.md) · [`select_statement`](abencds_select_statement_v1.md)

## Description

Defines a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). A CDS view is implemented using a query [`select_statement`](abencds_select_statement_v1.md). The [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`AbapCatalog.sqlViewName`](abencds_view_anno_v1.md) must be specified before the view itself is defined using `DEFINE VIEW`. Further optional annotations [`entity_annot1`](../abap-cds-data-definitions/abencds_f1_entity_annotations.md), ..., [`view_annot1`](abencds_view_anno_v1.md), ... can also be specified.

Two repository objects are created for a CDS view (of the [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md)) that is defined using `DEFINE VIEW`. A name must be specified for each of the two objects:

- The name `CDS_DB_VIEW` of an [CDS-managed DDIC view](../../abap-glossary/abencds_mngdddic_view_glosry.md) must be specified in quotation marks after the [annotation](abencds_view_anno_v1.md) `@AbapCatalog.sqlViewName`. This view is the technical foundation of the CDS view in ABAP Dictionary. The usual rules for ABAP Dictionary views apply to this name and it is not case-sensitive (it is transformed internally into uppercase letters). The associated SQL view is created under this name on the database. The name given to the DDIC database view can no longer be changed after the CDS view is transported into a follow-on system.

- The name `ddic_based_view` of the [CDS entity](../../abap-glossary/abencds_entity_glosry.md) is defined after the keywords `DEFINE VIEW` (`DEFINE` is optional). No quotation marks need to be specified. This name follows the rules of the CDS-managed DDIC view (obsolete), but can have 30 characters. The CDS entity represents all properties of the CDS view.

Both names are in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP. and must each be unique. The name `ddic_based_view` of the CDS entity can be used in other CDS DDL statements or in ABAP programs to access the CDS view.

The information specified in [`name_list`](abencds_name_list_v1.md) can be used to define the names of the elements of the view in a name list. [`parameter_list`](abencds_parameter_list_v1.md) can be used to assign input parameters to the view. These input parameters can be specified in operand positions of the view and can be assigned actual parameters when the view is used.

## Hints

- The [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md) `CDS_DB_VIEW` must not be used directly in CDS DDL and ABAP. Usage has been declared [obsolete](abencds_access_obsolete.md). Instead, it is strongly recommended that only the [CDS entity](../../abap-glossary/abencds_entity_glosry.md) is used, since only this entity covers all properties of the CDS view.

- [ABAP annotations](abencds_view_anno_v1.md) can be used to assign further technical and semantic properties to a view for evaluation by the ABAP runtime framework. [Framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be used to give the element specific semantic properties for other SAP frameworks.

- If a [CDS role](../../abap-glossary/abencds_role_glosry.md) is defined for a CDS entity using the CDS-DCL statement [`DEFINE ROLE`](../abap-cds-access-control/abencds_f1_define_role.md), implicit [access control](../../abap-glossary/abencds_access_control_glosry.md) applies by default when the CDS entity is accessed using ABAP SQL. CDS access control can be switched off using the value `#NOT_ALLOWED` for the annotation [`@AccessControl.authorizationCheck`](abencds_view_anno_v1.md) and using the addition [`WITH PRIVILEGED ACCESS`](../../abap-programming-language/abap-database-access/abapselect_data_source.md) in the [`FROM`](../../abap-programming-language/abap-database-access/abapfrom_clause.md) clause of an ABAP SQL query.

- The DDL source code of a CDS view does not need to have the same name as the CDS entity, but it is advisable to use this name.

- After a piece of DDL source code is transported, the combination of its name and the name of the CDS view defined in it and its CDS-managed DDIC view is defined and can no longer be modified by being renamed.

- The programming of CDS views using the DDL of the Core Data Services is one of the tasks included in the implementation of data models and is not usually the responsibility of regular ABAP application programmers. Once created, CDS views are used in ABAP programs using ABAP SQL read statements and must be stable enough to allow this.

- Every CDS view has its own [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md). The DDL source code of a CDS view is edited in a different editor than the [DDLA source code](../../abap-glossary/abenddla_source_code_glosry.md) of an [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md), the [DDLX source code](../../abap-glossary/abenddlx_source_code_glosry.md) of a [CDS metadata extension](../../abap-glossary/abencds_metadata_extension_glosry.md), and the [DCL source code](../../abap-glossary/abendcl_source_code_glosry.md) of a [CDS role](../../abap-glossary/abencds_role_glosry.md). The [ADT](../../abap-glossary/abenadt_glosry.md) documentation describes how the different types of source code are created.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view works in exactly the same way as the DDIC projection view `DEMO_SPFLI` in ABAP Dictionary. The class `CL_DEMO_CDS_PROJECTION` uses `SELECT` to access the view. Unlike when the DDIC view `DEMO_SPFLI` is accessed, no client column is returned when the CDS entity `DEMO_CDS_SPFLI` is accessed. The CDS-managed DDIC view (obsolete) `DEMO_CDS_PRJCTN` returns the client column too.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_PRJCTN'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_spfli
  as select from
    spfli
    {
      key spfli.carrid,
      key spfli.connid,
          spfli.cityfrom,
          spfli.cityto
    }
```
