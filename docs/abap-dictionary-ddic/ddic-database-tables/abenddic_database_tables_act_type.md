---
title: "DDIC - Activation Type of Database Tables"
source_file: abenddic_database_tables_act_type.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Technical Properties of Database Tables > DDIC - Table-Specific Technical Properties of Database Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Activation Type of Database Tables

The activation type defines whether a DDIC database table can be activated in an ABAP Dictionary tool or whether it must be controlled using the ABAP runtime framework environment. This setting is not relevant for DDIC database tables in application programming. In these tables, the default value *00* should be preserved. The following settings are possible:

- **Activation type 00**

  The default setting in which a DDIC database table can be activated in an ABAP Dictionary tool. DDIC database tables in application programming should always have this activation type.

- The following values for the activation type only apply to those DDIC database tables required by the ABAP runtime framework itself and hence only to internal SAP developments:

  - **Activation type 01**

    The [DDIC runtime object](../../abap-glossary/abenddic_runtime_object_glosry.md) of the database table must be created using an [ABAP kernel](../../abap-glossary/abenkernel_glosry.md) program before the table is activated in an ABAP Dictionary tool. This makes it impossible to modify and activate important system tables directly.

  - **Activation type 02**

    The DDIC database table is used in the [ABAP kernel](../../abap-glossary/abenkernel_glosry.md), but the [DDIC runtime object](../../abap-glossary/abenddic_runtime_object_glosry.md) can be activated (and hence created) in an ABAP Dictionary tool. It may be necessary to adjust the consumer programs of the kernel. This is indicated by a note in the activation log.

  - **Activation type 10**

    The DDIC database table is required before other objects are modified as part of a transport.
