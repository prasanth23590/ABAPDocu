---
title: "AbapCatalog.deliveryClass"
source_file: abencds_61840010-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.deliveryClass

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)                                                                    |
|-------------|-----------------------------------------------------------------------------------------------------------------------|
| **Syntax**  | `AbapCatalog.deliveryClass`                                                                                           |
| **Scope**   | `#TABLE_ENTITY`                                                                                                       |
| **Type**    | `String(30)`                                                                                                          |
| **Enums**   | `#APPLICATION_DATA, #CUSTOMIZING_DATA, #LOCAL_DATA, #SYSTEM_ADMINISTRATIVE_DATA, #SYSTEM_DATA, #SYSTEM_EDITABLE_DATA` |
| **Default** | `-`                                                                                                                   |
| **Text**    | `-`                                                                                                                   |
| **MDE**     | `-`                                                                                                                   |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`                                                         |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AbapCatalog

Technical settings of a CDS entity.

## deliveryClass

The delivery class can be defined for CDS table entities and controls the transport of table data in installations, upgrades, or client copies, and in transports between customer systems.

## Enums

## \#APPLICATION_DATA

Application table for master data and transaction data. The data is written by application programs.

This delivery class corresponds to delivery class 'A' in classical DDIC tables.

- An application table is delivered as an empty table or with a template for real data in client 000.

- In client copies, the data in client-dependent tables is copied only if the corresponding flag is set in the client copy profile. Any client-independent data is not copied.

- In installations, updates, and language imports, the data in client-dependent tables is only imported into the system client with the client ID 000, overwriting any existing data that match the content in the key fields. Any client-independent data is not imported.

- In transports between customer systems, all data is transported. In client-dependent tables, only the data in the specified target client is respected.

## \#CUSTOMIZING_DATA

Customizing table for data maintained exclusively by the customer.

This delivery class corresponds to delivery class 'C' in classical DDIC tables.

- Client-dependent customizing tables can be delivered with patterns for real data.

- In client copies, the data of client-dependent tables is copied. Any client-independent data is not copied.

- In installations, updates, and language imports, the data in client-dependent tables is only imported into the system client with the client ID 000, overwriting any existing data that match the content in the key fields. Any client-independent data is not imported.

- In transports between customer systems, all data is transported. In client-dependent tables, only the data in the specified target client is respected.

## \#LOCAL_DATA

Table for local data of each ABAP system. SAP delivers tables in the delivery class L as empty tables.

This delivery class corresponds to delivery class 'L' in classical DDIC tables.

- These tables are delivered as empty tables.

- No data is copied in client copies.

- No data is imported in installations, updates, and language imports.

- No data is transported in transports between customer systems.

## \#SYSTEM_DATA

System table delivered by SAP as part of the system. Contains predefined data. In the Change and Transport Systems (CTS), the data is handled like repository objects, which means that they have an original system and any changes in other systems are modifications or repairs.

This delivery class corresponds to delivery class 'S' in classical DDIC tables.

- These system tables are delivered with prefilled data.

- In client copies, the data of client-dependent tables is copied. Any client-independent data is not copied.

- In installations, updates, and language imports, all data is imported, overwriting any existing data that match the content in the key fields.

- In transports between customer systems, all data is transported. In client-dependent tables, only the data in the specified target client is respected.

## \#SYSTEM_ADMINISTRATIVE_DATA

System table for system administration data. A system table in this delivery class is usually delivered with prefilled data by SAP and can be modified by customer modifications. The content is transported using transport objects assigned to the managed objects.

This delivery class corresponds to delivery class 'W' in classical DDIC tables.

- These system tables are delivered with prefilled entries.

- No data is copied in client copies.

- In installations, updates, and language imports, all data is imported, overwriting any existing data that match the content in the key fields.

- In transports between customer systems, all data is transported. In client-dependent tables, only the data in the specified target client is respected.

## \#SYSTEM_EDITABLE_DATA

System table in which customers can make entries.

This delivery class corresponds to delivery class 'E' in classical DDIC tables.

- These system tables are delivered with prefilled entries.

- In client copies, the data of client-dependent tables is copied. Any client-independent data is not copied.

- In installations, updates, and language imports, all data is imported, overwriting any existing data that match the content in the key fields.

- In transports between customer systems, all data is transported. In client-dependent tables, only the data in the specified target client is respected.
