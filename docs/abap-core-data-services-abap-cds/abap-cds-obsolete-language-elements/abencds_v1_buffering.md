---
title: "ABAP CDS - Table Buffering of CDS DDIC-Based Views"
source_file: abencds_v1_buffering.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Table Buffering of CDS DDIC-Based Views

The following [CDS annotations](../../abap-glossary/abencds_annotation_glosry.md) can define [table buffering](../../abap-glossary/abentable_buffering_glosry.md) for a CDS view linked with a [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md):

- [`@AbapCatalog.buffering.status`](abencds_view_anno_v1.md) defines whether and how [table buffering](../../abap-programming-language/abap-database-access/abensap_puffering.md) is allowed.

- [`@AbapCatalog.buffering.type`](abencds_view_anno_v1.md) determines the [buffering type](../../abap-programming-language/abap-database-access/abenbuffer_type.md).

- [`@AbapCatalog.buffering.numberOfKeyFields`](abencds_view_anno_v1.md) determines the number of key fields covered if [generic buffering](../../abap-programming-language/abap-database-access/abenbuffer_generic_buffering.md) is used.

Table buffering of CDS views is done for the associated [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md) and the same prerequisites apply as for DDIC database views in ABAP Dictionary. To meet these prerequisites, a CDS view can only be buffered if the following applies:

- It cannot contain any views and no [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md) as [data sources](abencds_data_source_v1.md).

- It cannot have any [input parameters](abencds_parameter_list_v1.md).

- A [client-dependent view](abencds_view_client_handling_v1.md) can use `$session.client` as the only [session variable](abencds_session_variable_v1.md) and must use it directly. This also allows the annotation `@ClientHandling.algorithm:#SESSION_VARIABLE` to be specified to [determine client handling](abencds_view_client_handling_v1.md). A client-independent view must not use any session variables.

- Key fields cannot contain [null values](../../abap-glossary/abennull_value_glosry.md).

- The required key fields must be listed directly in the [`SELECT` list](abencds_select_list_v1.md). Key fields that only occur as operands of expressions cannot be evaluated.

- No database tables can be accessed where [data aging](../../abap-glossary/abendata_aging_glosry.md) is enabled.

Only the key fields of the CDS-managed DDIC view (obsolete) are respected in SAP buffering of [CDS-managed DDIC views (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md). Since ABAP release 7.90, the key fields of the CDS entity and the CDS-managed DDIC views (obsolete) are identical by default.

## Hints

- In [client-dependent views](abencds_view_client_handling_v1.md), the client column must be explicitly included or added to the number in the specification for the annotation `@AbapCatalog.buffering.numberOfKeyFields`.

- For [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), table buffering is [defined](../abap-cds-data-definitions/abencds_v2_view_buffering.md) directly for the CDS entity. A client column is not counted as a key field here.

- In contrast to [table buffering of CDS view entities](../abap-cds-data-definitions/abencds_v2_view_buffering.md), where the prerequisites are real restrictions for the view, for DDIC-based views that do not meet the prerequisites buffering is bypassed implicitly by ABAP SQL.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Enables full buffering for a CDS view.

``` abap
@AbapCatalog.sqlViewName: '...' 
@AbapCatalog.Buffering.status: #ACTIVE 
@AbapCatalog.Buffering.type: #FULL 
  define view ... 
   as select from ... 
   { ... }
```
