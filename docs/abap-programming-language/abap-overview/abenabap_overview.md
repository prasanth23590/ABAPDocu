---
title: "ABAP Programming Language, Overview"
source_file: abenabap_overview.html
section: "ABAP Programming Language > ABAP - Overview"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Programming Language, Overview

ABAP is a programming language developed by SAP for the development of business applications with an [ABAP development environment (ABAP DE)](../../abap-glossary/abenabap_dev_envir_glosry.md).

- [ABAP on the Application Server ABAP](abenabap_overview.md#abap-on-the-application-server-abap)

- [Programming Models](abenabap_overview.md#programming-models)

- [Database Access](abenabap_overview.md#database-access)

- [Special Characteristics](abenabap_overview.md#special-characteristics)

- [Multilingualism](abenabap_overview.md#multilingualism)

## ABAP on the Application Server ABAP

ABAP is the programming interface of the [Application Server ABAP](../../abap-glossary/abenas_abap_glosry.md) (AS ABAP) of an [ABAP system](../../abap-glossary/abenabap_system_glosry.md).

- Before the ABAP programming language can be used, an AS ABAP must be installed as the [application layer](../../abap-glossary/abenapplication_layer_glosry.md) of an [ABAP system](../../abap-glossary/abenabap_system_glosry.md). The AS ABAP provides the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md) in which ABAP programs are executed independently of the actual [host computer](../../abap-glossary/abenhost_computer_glosry.md).

- AS ABAP must be connected to a [database layer](../../abap-glossary/abendatabase_layer_glosry.md) or to a [database system](../../abap-glossary/abendatabase_system_glosry.md) where its central dataset is stored in a [standard database](../../abap-glossary/abenstandard_db_glosry.md).

- UI-based access requires a [presentation layer](../../abap-glossary/abenpresentation_layer_glosry.md) that displays the AS ABAP user interface (in SAP GUI or a Web browser).

## Programming Models

ABAP supports the following:

- An object-oriented programming model that is based on [classes](../../abap-glossary/abenclass_glosry.md) and [interfaces](../../abap-glossary/abenoo_intf_glosry.md) of [ABAP Objects](../../abap-glossary/abenabap_objects_glosry.md).

## Database Access

One of the fundamental properties of ABAP as a programming language for business applications is the access to database tables that is fully integrated into the language.

- Data modeling

  ABAP data modeling makes it possible to create data models for business applications that are defined on the database:

  - The [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md) is a persistent repository for data types and their relationships that are visible and can be used in all other development objects. The ABAP Dictionary manages the database tables, views, and lock objects of the [standard AS ABAP database](../../abap-glossary/abenstandard_db_glosry.md).

  - The [ABAP Core Data Services](../../abap-glossary/abenabap_core_data_services_glosry.md) implement the SAP CDS concept for the AS ABAP. A platform-independent [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) and [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md) make it possible to define [CDS entities](../../abap-glossary/abencds_entity_glosry.md) such as [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) or [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md), and associated [CDS roles](../../abap-glossary/abencds_role_glosry.md) and their semantic enrichment.

- Database access

  Access to data in database tables is fully integrated in ABAP:

  - [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) makes it possible to access the database objects defined in the ABAP Dictionary or in ABAP CDS with implicit [client handling](../../abap-glossary/abenclient_handling_glosry.md). This access is platform-independent and integrated into the language. The performance can be optimized by using the [table buffering](../../abap-glossary/abentable_buffering_glosry.md) integrated into the ABAP runtime framework.

  - [AMDP](../../abap-glossary/abenamdp_glosry.md) can be used to manage and call database procedures and database functions of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md).

## Special Characteristics

ABAP is a 4GL language developed specifically for the mass processing of data in business applications and, in addition to integrated database access, has the following characteristics when compared with the elementary languages in which such functions are usually stored in libraries:

- [Internal tables](../../abap-glossary/abeninternal_table_glosry.md) for the dynamic storage and processing of tabular mass data in the working memory.

- An [LUW concept](../../abap-glossary/abenluw_glosry.md) integrated into the ABAP runtime framework that allows many users to access the [standard database](../../abap-glossary/abenstandard_db_glosry.md) simultaneously.

- An integrated interface of the language to other programming environments using Remote Function Call.

- An integrated interface of the language to [XML](../../abap-glossary/abenxml_glosry.md).

The integration of such functions into the language is particularly beneficial for static checks and performance of programs. In return, this means that ABAP also contains considerably more language elements than an elementary programming language.

## Multilingualism

ABAP programs can be programmed as fully language-independent by removing language-specific program parts from the source code and then reloading them during program execution in accordance with the language environment. A [text environment](../../abap-glossary/abentext_environment_glosry.md) determines the exact program behavior at runtime, for example the order in which text is sorted.
