---
title: "AMDP - Client Handling Definition"
source_file: abenamdp_client_hdl_def.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Client Handling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Client Handling Definition

The client handling of an AMDP method that does not implement a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md) is defined by the usage of the respective AMDP options [`client_handling`](abapmethods_amdp_options_client.md) that can be used behind the statements `METHODS` or `CLASS-METHODS`. The client handling of an AMDP method that implements a CDS table function by [`FOR TABLE FUNCTION`](abapclass-methods_for_tabfunc.md) is governed by the [client handling](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_handling.md) of the table function.

The following options are possible:

- [`CDS SESSION CLIENT DEPENDENT`](abapmethods_amdp_options_client.md)

  This option sets the HANA [session variable](../../abap-glossary/abensession_variable_glosry.md) `CDS_CLIENT` to the ID of the [client](../../abap-glossary/abenclient_glosry.md) of the current [logon](../../abap-glossary/abenlogon_glosry.md) to the [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) when the method is called from ABAP. Furthermore, it restricts the [`USING`](abapmethod_by_db_proc.md) list to client-independent objects or to client-dependent objects that can access data of that client only. Such an AMDP method is [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md) and [client-safe](../../abap-glossary/abenclient_safe_glosry.md).

- [`CLIENT INDEPENDENT`](abapmethods_amdp_options_client.md)

  This option restricts the [`USING`](abapmethod_by_db_proc.md) list to [client-independent](../../abap-glossary/abenclient_independent_glosry.md) objects. The AMDP method is itself client-independent and [client-safe](../../abap-glossary/abenclient_safe_glosry.md).

- [`CDS SESSION CLIENT CURRENT`](abapmethods_amdp_options_client.md)

  This option sets the HANA [session variable](../../abap-glossary/abensession_variable_glosry.md) `CDS_CLIENT` in the same way as the option `CDS SESSION CLIENT DEPENDENT` but does not restrict the [`USING`](abapmethod_by_db_proc.md) list. It depends on the objects used and the implementation of the method which data of which clients are accessed. Such an AMDP method is not [client-safe](../../abap-glossary/abenclient_safe_glosry.md).

- [`CDS SESSION CLIENT clnt`](abapmethods_amdp_options_client.md)

  This option sets the HANA [session variable](../../abap-glossary/abensession_variable_glosry.md) `CDS_CLIENT` to the value that is passed to the parameter `clnt` of the method. It does not restrict the [`USING`](abapmethod_by_db_proc.md) list. It depends on the objects used and the implementation of the method which data of which clients are accessed. Such an AMDP method is not [client-safe](../../abap-glossary/abenclient_safe_glosry.md).

- If none of the above options are used:

  The HANA [session variable](../../abap-glossary/abensession_variable_glosry.md) `CDS_CLIENT` is not set when the method is called. The [`USING`](abapmethod_by_db_proc.md) list can contain all kinds of objects that are not restricted to data of the client represented by the HANA session variable `CDS_CLIENT`. It depends on the objects used and the implementation of the method which data of which clients are accessed. Such an AMDP method is not [client-safe](../../abap-glossary/abenclient_safe_glosry.md).

For all of the above client-dependent options, the client selection is not done by the AMDP framework but depends on the method implementation, that is on the data sources and the `WHERE` conditions used for the client ID.

- If CDS entities are accessed that are filtered implicitly for the HANA session variable `CDS_CLIENT`, one of the options [`CDS SESSION CLIENT`](abapmethods_amdp_options_client.md) must be used. The data sources return data of that client only. If a `WHERE` condition of the implementation filters data of another client, the result is empty.

- If [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md) are accessed in AMDP methods with the addition `CDS SESSION CLIENT DEPENDENT`, not the database table itself is accessed, but an implicitly generated database view that is filtered for the HANA session variable `CDS_CLIENT` and returns data of the client contained in that variable only.

- If data sources that are not filtered implicitly for the HANA session variable `CDS_CLIENT` are accessed and none of the options [`CDS SESSION CLIENT`](abapmethods_amdp_options_client.md) are used, the required client ID must be selected explicitly in the implementation. In such cases, the parameter interface of an AMDP method must usually contain an input parameter for the client ID that is used in a `WHERE` condition for he client ID.

In [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md), an AMDP method must be [client-safe](../../abap-glossary/abenclient_safe_glosry.md). For client-dependent data sources this can only achieved by using the AMDP option [`CDS SESSION CLIENT DEPENDENT`](abapmethods_amdp_options_client.md). Then it is guaranteed, that all data sources are filtered implicitly by the current client.

For a detailed overview, how the `USING` list depends on the client handling, refer to [Client Handling/`USING` Matrices](abenamdp_call_matrices.md).

## Hints

- For AMDP methods that use one of the options [`CDS SESSION CLIENT`](abapmethods_amdp_options_client.md) and that access only data sources that are filtered implicitly for the HANA session variable `CDS_CLIENT`, usually do not need an input parameter for a client ID. This is especially the case for the option [`CDS SESSION CLIENT DEPENDENT`](abapmethods_amdp_options_client.md).
