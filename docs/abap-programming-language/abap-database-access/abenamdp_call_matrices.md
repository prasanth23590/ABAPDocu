---
title: "[CLASS-]METHODS, Client Handling/USING Matrices"
source_file: abenamdp_call_matrices.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Methods > [CLASS-]METHODS, AMDP OPTIONS > [CLASS-]METHODS, AMDP OPTIONS client_handling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# \[CLASS-\]METHODS, Client Handling/USING Matrices

The following table show how the client handling affects the [`USING`](abapmethod_by_db_proc.md) list of an AMDP method. For standalone AMDP methods, client handling is defined by AMDP options. For AMDP methods implementing CDS table functions, client handling is governed by the table function.

- [Standalone AMDP Methods](abenamdp_call_matrices.md#standalone-amdp-methods)

- [AMDP Methods for CDS Table Functions](abenamdp_call_matrices.md#amdp-methods-for-cds-table-functions)

*CS* means usage of [client-safe](../../abap-glossary/abenclient_safe_glosry.md) object by a client-safe object. *-* means usage not possible.

## Standalone AMDP Methods

The following table shows the allowed combinations of the AMDP options [`client_handling`](abapmethods_amdp_options_client.md) (columns) with objects of the [`USING`](abapmethod_by_db_proc.md) list (rows).

\|**`client_handling`/`USING`**\|[`CDS SESSION CLIENT DEPENDENT`](abapmethods_amdp_options_client.md) ([client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md))\|[`CDS SESSION CLIENT INDEPENDENT`](abapmethods_amdp_options_client.md) ([client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md)) \| \|:---\| \|**AMDP Methods** \| \|[`CDS SESSION CLIENT DEPENDENT`](abapmethods_amdp_options_client.md) ([client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md))\|*CS*\|- \| \|[`CDS SESSION CLIENT INDEPENDENT`](abapmethods_amdp_options_client.md) ([client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md))\|*CS*\|*CS* \| \|**CDS Table Functions** \| \|[Client-dependent using session variable without client parameter](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_hdl_def.md) ([client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md))\|*CS*\|- \| \|[Client-independent](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_hdl_def.md) ([client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md))\|*CS*\|*CS* \| \|**Other CDS entities** \| \|Client-dependent, filtered by session variable (e.g. [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md)), except [CDS DDIC-based view](../../abap-glossary/abencds_v1_view_glosry.md) ([client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md))\|*CS*\|*-* \| \|Client-independent ([client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md)) \|*CS*\|*CS* \| \|**DDIC objects** \| \|[DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md)\|*CS*\|*CS*\|

## AMDP Methods for CDS Table Functions

The following table shows the allowed combinations of [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md) implemented by [`FOR TABLE FUNCTION`](abapclass-methods_for_tabfunc.md) (columns) with objects of the [`USING`](abapmethod_by_db_proc.md) list (rows).

\|**Table Function**/

`USING`\|[Client-dependent using session variable without client parameter](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_hdl_def.md) ([client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md))\|[Client-independent](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_hdl_def.md) ([client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md)) \| \|:---\| \|**AMDP Methods** \| \|[`CDS SESSION CLIENT DEPENDENT`](abapmethods_amdp_options_client.md) ([client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md))\|*CS*\|- \| \|[`CDS SESSION CLIENT INDEPENDENT`](abapmethods_amdp_options_client.md) ([client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md))\|*CS*\|*CS* \| \|**CDS Table Functions** \| \|[Client-dependent using session variable without client parameter](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_hdl_def.md) ([client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md))\|*CS*\|- \| \|[Client-independent](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_hdl_def.md) ([client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md))\|*CS*\|*CS* \| \|**Other CDS entities** \| \|Client-dependent, filtered by session variable (e.g. [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md)), except [CDS DDIC-based view](../../abap-glossary/abencds_v1_view_glosry.md) ([client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md))\|*CS*\|*-* \| \|Client-independent ([client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md)) \|*CS*\|*CS* \| \|**DDIC objects** \| \|[DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md)\|*CS*\|*CS*\|
