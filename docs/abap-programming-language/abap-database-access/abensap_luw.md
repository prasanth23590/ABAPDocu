---
title: "SAP LUW"
source_file: abensap_luw.html
section: "ABAP Programming Language > ABAP - Database Access > Data Consistency"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SAP LUW

An application program can be split into multiple program sections, which are processed in sequence using different [work processes](../../abap-glossary/abenwork_process_glosry.md). Each switch of a work process is linked with an implicit [database commit](../../abap-glossary/abendatabase_commit_glosry.md), which means that an application program is not linked with a single [database LUW](../../abap-glossary/abendatabase_luw_glosry.md) automatically. ![figure](images_abdoc_sap_luw.gif)

To ensure the data consistency of application programs that are executed across multiple work processes, the change statements are not executed directly in an [SAP LUW](../../abap-glossary/abensap_luw_glosry.md). Instead, they are first registered and then executed by a single work process, that is, in a single database LUW.

## SAP LUWs and Internal Sessions

Each closing of an [internal session](../../abap-glossary/abeninternal_session_glosry.md) ends the current SAP LUW.
