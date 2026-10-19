---
title: "DDIC - Delivery Class of Database Tables"
source_file: abenddic_database_tables_delivery.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Semantic Properties of Database Tables > DDIC - Table-Specific Semantic Properties of Database Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Delivery Class of Database Tables

The delivery class of a DDIC database table controls the [transport](https://help.sap.com/docs/ABAP_PLATFORM_NEW/4a368c163b08418890a406d413933ba7/48c4300fca5d581ce10000000a42189c) of table data in installations, upgrades, or [client copies](https://help.sap.com/docs/ABAP_PLATFORM_NEW/4a368c163b08418890a406d413933ba7/4d8062ec095114afe10000000a42189c), and in [transports](https://help.sap.com/docs/ABAP_PLATFORM_NEW/4a368c163b08418890a406d413933ba7/48c4300fca5d581ce10000000a42189c) between customer systems.

- **Delivery class A**

  Application table for master data and transaction data. The data is written by application programs.

  - An application table is delivered as an empty table or with a template for real data in client 000.

  - In [client copies](https://help.sap.com/docs/ABAP_PLATFORM_NEW/4a368c163b08418890a406d413933ba7/4d8062ec095114afe10000000a42189c), the data in client-dependent tables is copied only if the corresponding flag is set in the [client copy profile](https://help.sap.com/docs/ABAP_PLATFORM_NEW/4a368c163b08418890a406d413933ba7/4d8062ec095114afe10000000a42189c). Any client-independent data is not copied.

  - In installations, updates, and language imports, the data in client-dependent tables is only imported into the system client with the client ID *000*, overwriting any existing data that match the content in the key fields. Any client-independent data is not imported.

  - In transports between customer systems, all data is transported. In client-dependent tables, only the data in the specified target client is respected.

- **Delivery classes C and G**

  Customizing table for data maintained exclusively by the customer.

  - Client-dependent customizing tables can be delivered with patterns for real data.

  - In [client copies](https://help.sap.com/docs/ABAP_PLATFORM_NEW/4a368c163b08418890a406d413933ba7/4d8062ec095114afe10000000a42189c), the data of client-dependent tables is copied. Any client-independent data is not copied.

  - In installations, updates, and language imports, the data in client-dependent tables is only imported into the system client with the client ID *000*, overwriting any existing data that match the content in the key fields. Any client-independent data is not imported.

  - In transports between customer systems, all data is transported. In client-dependent tables, only the data in the specified target client is respected.

    The delivery class G is obsolete and occurs only for existing tables. It can no longer be specified. Tables with delivery class G are handled like delivery class C implicitly.

- **Delivery class L**

  Table for local data of each [ABAP system](../../abap-glossary/abenabap_system_glosry.md). SAP delivers tables in the delivery class L as empty tables.

  - These tables are delivered as empty tables.

  - No data is copied in [client copies](https://help.sap.com/docs/ABAP_PLATFORM_NEW/4a368c163b08418890a406d413933ba7/4d8062ec095114afe10000000a42189c).

  - No data is imported in installations, updates, and language imports.

  - No data is transported in transports between customer systems.

    [Global temporary tables](../../abap-glossary/abenglobal_temporary_table_glosry.md) always have the delivery class L.

- **Delivery class E**

  System table in which customers can make entries. A system table in the delivery class *E* must be assigned a customer namespace in the database table `TRESC` using the program `RDDKOR54`.

  - These system tables are delivered with prefilled entries.

  - In [client copies](https://help.sap.com/docs/ABAP_PLATFORM_NEW/4a368c163b08418890a406d413933ba7/4d8062ec095114afe10000000a42189c), the data of client-dependent tables is copied. Any client-independent data is not copied.

  - In installations, updates, and language imports, all data is imported, overwriting any existing data that match the content in the key fields.

  - In transports between customer systems, all data is transported. In client-dependent tables, only the data in the specified target client is respected.

- **Delivery class S**

  System table delivered by SAP as part of the system. Contains predefined data. In the [Change and Transport Systems (CTS)](../../abap-glossary/abencts_glosry.md), the data is handled like repository objects, which means that they have an original system and any changes in other systems are modifications or repairs.

  - These system tables are delivered with prefilled data.

  - In [client copies](https://help.sap.com/docs/ABAP_PLATFORM_NEW/4a368c163b08418890a406d413933ba7/4d8062ec095114afe10000000a42189c), the data of client-dependent tables is copied. Any client-independent data is not copied.

  - In installations, updates, and language imports, all data is imported, overwriting any existing data that match the content in the key fields.

  - In transports between customer systems, all data is transported. In client-dependent tables, only the data in the specified target client is respected.

- **Delivery class W**

  System table for system administration data, such as `TFDIR` as a directory of all function modules. A system table in the delivery class *W* is usually delivered with prefilled data by SAP and can be modified by customer modifications. The content is transported using transport objects assigned to the managed objects, such as `R3TR FUNC` for function modules.

  - These system tables are delivered with prefilled entries.

  - No data is copied in [client copies](https://help.sap.com/docs/ABAP_PLATFORM_NEW/4a368c163b08418890a406d413933ba7/4d8062ec095114afe10000000a42189c).

  - In installations, updates, and language imports, all data is imported, overwriting any existing data that match the content in the key fields.

  - In transports between customer systems, all data is transported. In client-dependent tables, only the data in the specified target client is respected.

## Hints

- For more information about transports and client copies, see the documentation [Change and Transport System](https://help.sap.com/docs/ABAP_PLATFORM_NEW/4a368c163b08418890a406d413933ba7/48c4300fca5d581ce10000000a42189c) on SAP Help Portal.
