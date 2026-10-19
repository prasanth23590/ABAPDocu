---
title: "AMDP - Client Safety"
source_file: abenamdp_client_safety.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Client Handling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Client Safety

The AMDP framework does not introduce implicit client conditions into the AMDP method implementations and there is no implicit client handling when executing an AMDP method. Therefore, [client safety](../../abap-glossary/abenclient_safe_glosry.md) must be delegated to the objects accessed in an AMDP method and declared in its [`USING`](abapmethod_by_db_proc.md) list. An AMDP method is [client-safe](../../abap-glossary/abenclient_safe_glosry.md) if the following prerequisites are met:

- One of the following AMDP options must be used:

  - [`CDS SESSION CLIENT DEPENDENT`](abapmethods_amdp_options_client.md)

  - The method is declared as client dependent, the HANA [session variable](../../abap-glossary/abensession_variable_glosry.md) `CDS_CLIENT` is set to its default value. Client safety is achieved by the fact that the results of all objects of the `USING` list are restricted to the current client via implicit filter conditions for the CDS session [`$session.client`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_session_var_builtin_v2.md) that addresses the HANA session variable `CDS_CLIENT`. For that, the `USING` list is checked for the following client-safe objects only:

    [Client-dependent CDS view entities](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_v2_view_client_handling.md). [Client-dependent CDS table functions](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_handling.md) that are [client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md). Client-dependent [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md) Other client-dependent AMDP methods with the AMDP option `CDS SESSION CLIENT DEPENDENT`. Client-independent CDS objects, DDIC database tables or AMDP methods

  - [`CLIENT INDEPENDENT`](abapmethods_amdp_options_client.md)

    The method is declared as [client independent](../../abap-glossary/abenclient_independent_glosry.md) and client safety is achieved by checking the `USING` list for the following client-safe objects only: [Client-independent CDS view entities](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_v2_view_client_handling.md) [Client-independent CDS table functions](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_handling.md) that are [client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md). Client-independent [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md) Other client-independent AMDP methods with the AMDP option `CLIENT INDEPENDENT`.

- The SQLScript code of client-safe AMDP methods must not contain one of the following:

  - Access to database objects that are not managed by ABAP. In particular, it is not allowed to call SQLScript procedures that are not managed by AMDP and it is not allowed to access database objects outside the [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md) that cannot be controlled by the `USING` list.

  - Cross-client access when accessing built-in HANA functions, that have an actual parameter for the client ID. Such functions are `CONVERT_CURRENCY`, `CONVERT_UNIT`, `ADD_WORKDAYS`, `WORKDAYS_BETWEEN`, `ABAP_USER_TIMEZONE`, or `ABAP_SYSTEM_TIMEZONE`.

For a detailed overview, how the `USING` list depends on the client handling, refer to [Client Handling/`USING` Matrices](abenamdp_call_matrices.md).

## Hints

- AMDP methods that have the [ABAP language version](../../abap-glossary/abenabap_version_glosry.md) [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md) or are a [released API](../../abap-glossary/abenreleased_api_glosry.md) with a [C1 contract](../../abap-glossary/abenc1_contract_glosry.md) or a [C4 contract](../../abap-glossary/abenc4_contract_glosry.md) must be client-safe and must access client-safe objects only.

- When using a client-dependent [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md) in an AMDP method with the option `CDS SESSION CLIENT DEPENDENT`, the database table is not accessed directly. Instead an implicitly created view is accessed that is client-safe by a filter condition for the HANA session variable `CDS_CLIENT`.

- Refer also to SAP Note [3472859](https://launchpad.support.sap.com/#/notes/3472859).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The executable example of an [SQLScript procedure](abenamdp_cs_abexa.md) demonstrates client handling using the HANA session variable `CDS_CLIENT` that is [client-safe](../../abap-glossary/abenclient_safe_glosry.md).
