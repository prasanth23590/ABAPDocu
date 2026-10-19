---
title: "ABAP Programs on the AS ABAP"
source_file: abenorganization_of_modules.html
section: "ABAP Programming Language > ABAP - Overview"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Programs on the AS ABAP

ABAP programs are executed on the [Application Server ABAP (AS ABAP)](../../abap-glossary/abenas_abap_glosry.md) of an [ABAP system](../../abap-glossary/abenabap_system_glosry.md). The figure below shows a highly simplified representation of the AS ABAP as part of an ABAP system.

  
![figure](images_abap_platform.gif)  

The [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) represents the application layer of the ABAP system. The AS ABAP is identified by a [system ID](../../abap-glossary/abensystem_id_glosry.md), which is also the name of the entire ABAP system. Users can log on to the AS ABAP using a [user name](../../abap-glossary/abenuser_name_glosry.md). The most important components of an AS ABAP for ABAP program execution are:

- **AS instance**

  The actual ABAP program execution takes place in [AS instances (application server instances)](../../abap-glossary/abenas_instance_glosry.md). One or more AS instances can be instantiated for an AS ABAP. Multiple AS instances are usually distributed across several [host computers](../../abap-glossary/abenhost_computer_glosry.md). The AS instances communicate with each other using a message server that exists only once for each AS ABAP.

- **Work processes**

  Each AS instance has [work processes](../../abap-glossary/abenwork_process_glosry.md) to execute ABAP programs. There are different types of work processes for different applications: dialog, enqueue, background, spool, and update work processes. For the entire runtime of an AS instance, each work process is logged on to the [standard database](../../abap-glossary/abenstandard_db_glosry.md) of the [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) as a [database user](../../abap-glossary/abendatabase_user_glosry.md) using a [standard connection](../../abap-glossary/abenstandard_db_connection_glosry.md). This user is assigned the [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md) that represents the [database layer](../../abap-glossary/abendatabase_layer_glosry.md) of an [ABAP system](../../abap-glossary/abenabap_system_glosry.md). The ABAP database schema stores both [system programs](../../abap-glossary/abensystem_program_glosry.md) and [system tables](../../abap-glossary/abensystem_table_glosry.md), as well as [application programs](../../abap-glossary/abenapplication_program_glosry.md) and [application tables](../../abap-glossary/abenapplication_table_glosry.md).

- **Communication components**

  The communication components connect the AS instances to the [presentation layer](../../abap-glossary/abenpresentation_layer_glosry.md) of the [ABAP system](../../abap-glossary/abenabap_system_glosry.md), or to other systems that themselves can be another AS ABAP or external systems. Examples of communication components are:

  - The ICM for linking to browser-based user interfaces ([SAPUI5](../../abap-glossary/abensapui5_glosry.md), Web Dynpro) and to the Internet.

  - The RFC interface for linking to other systems.

    There are different protocols for communication, such as HTTP, HTTPS, TCP, or SAP's RFC protocol.

For more information, see [Application Server Infrastructure - ABAP](https://help.sap.com/docs/ABAP_PLATFORM_NEW/7bbf03267f654b5cb06a8bf78f61fca1/797de8aa42e24916953c4bb3d983662d).

ABAP program execution is organized in sessions, which can access different memory areas:

- [Sessions and Memory Areas](abenmemory_organization.md)

In general, the execution of an ABAP program is triggered by a call or by handling an event from outside the application server. Typical calls or events are:

- Dialog requests from an UI

  - Via ICM/ICF for Web UIs

- Remote calls from other systems

  - Via ICF/ICM for internet request

  - Via RFC for remote calls

Furthermore, the execution of an ABAP program can be triggered by the AS ABAP itself, as it the case for scheduled job executions in background processing.
