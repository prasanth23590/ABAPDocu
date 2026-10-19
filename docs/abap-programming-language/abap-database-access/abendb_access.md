---
title: "ABAP - Database Access"
source_file: abendb_access.html
section: "ABAP Programming Language"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP - Database Access

All the data relevant for all applications of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md), including metadata and technical data, is stored and managed centrally in its [standard database](../../abap-glossary/abenstandard_db_glosry.md). AS ABAP supports database systems from different vendors. The [database objects](../../abap-glossary/abendb_object_glosry.md) for storing and accessing data, such as database tables, views, or stored procedures, are created as platform-dependent objects by the ABAP-specific frameworks [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md), [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), and [AMDP](../../abap-glossary/abenamdp_glosry.md) in the [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md).

- In the ABAP Dictionary, [DDIC database tables](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables.md) and DDIC views, and in ABAP CDS [CDS persistent entities](../../abap-glossary/abencds_sql_entity_glosry.md) are defined as ABAP-specific objects. Instances of these objects are created in the [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md) when they are activated. Such database tables, views, and entities can also be used as globally visible structured types in ABAP programs.

- The [AMDP](../../abap-glossary/abenamdp_glosry.md) framework makes it possible to create ABAP-based definitions of [AMDP procedures](../../abap-glossary/abenamdp_procedure_glosry.md) and [AMDP functions](../../abap-glossary/abenamdp_function_glosry.md) in the [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md). In ABAP, they can be called as follows:

  - Using [method calls](../abap-calling-and-exiting-program-units/abenmethod_calls.md)

  - Using [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) for accessing a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md).

  - With [CDS scalar functions](../../abap-glossary/abencds_scalar_function_glosry.md).

To enable access to database objects, every database system uses the largely standardized language [SQL](../../abap-glossary/abensql_glosry.md), which can be implemented in different ways to suit specific platforms. The following options are available in ABAP for accessing ABAP-managed database objects: [ABAP-managed database objects](../../abap-glossary/abenabap_managed_db_object_glosry.md):

- [ABAP SQL](abenabap_sql.md)

  For mostly platform-independent access to database tables, and [CDS persistent entities](../../abap-glossary/abencds_sql_entity_glosry.md), the [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statements embedded in ABAP are used, which themselves are transformed to platform-dependent SQL using the [ABAP SQL interface](../../abap-glossary/abenabap_sql_interface_glosry.md) in AS ABAP. This method also covers ABAP-specific evaluations, such as implicit [client handling](../../abap-glossary/abenclient_handling_glosry.md) or [CDS access control](../../abap-glossary/abencds_access_control_glosry.md).

- [AMDP](abenamdp.md)

  Framework used to manage and call [database procedures](../../abap-glossary/abendatabase_procedure_glosry.md) and [database functions](../../abap-glossary/abendatabase_function_glosry.md) in ABAP.

The following topics also deal with important aspects of database access:

- [Data consistency](abendata_consistency.md)

  [LUW](../../abap-glossary/abenluw_glosry.md) concepts must be employed to ensure data consistency when handling persistent data in databases.

## Hints

- If a [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) is used as the standard AS ABAP database, it is handled in ABAP programs like any relational database.

- [SQL services](../../abap-glossary/abenabap_sql_services_glosry.md) provide SQL-level access to [ABAP-managed database objects](../../abap-glossary/abenabap_managed_db_object_glosry.md) for consumers outside the system.
