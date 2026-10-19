---
title: "ABAP - Keyword Documentation"
source_file: abenabap.html
section: "ABAP - Keyword Documentation"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP - Keyword Documentation

The keyword documentation describes the syntax and semantics of the keywords of programming languages provided by SAP on an [Application Server ABAP](abap-glossary/abenas_abap_glosry.md) (AS ABAP) of an [ABAP system](abap-glossary/abenabap_system_glosry.md) for [ABAP Cloud](abap-glossary/abenabap_cloud_glosry.md). It also provides an introduction to the environment of these languages plus language-related frameworks and their associated system classes.

The language version [ABAP for Cloud Development](abap-glossary/abenabap_for_cloud_dev_glosry.md) and the frameworks for [ABAP Cloud](abap-glossary/abenabap_cloud_glosry.md) do not cover all elements of the [ABAP technology](abap-glossary/abenabap_techno_glosry.md) and are restricted to the needs of ABAP Cloud.

- **Modeling**

  - [ABAP - Dictionary](abap-dictionary-ddic/abenabap_dictionary.md)

    ABAP Dictionary is a persistent repository of metadata used to describe data types, database tables, views, and similar objects that can be used in development objects such as [ABAP programs](abap-glossary/abenabap_program_glosry.md) or [CDS entities](abap-glossary/abencds_entity_glosry.md). This section of the ABAP keyword documentation provides a full description of the most important ABAP Dictionary objects that are relevant for the programming languages. It also includes documentation for the [Dictionary DDL](abap-glossary/abendictionary_ddl_glosry.md) used to define certain dictionary objects in the ABAP development tools for Eclipse (ADT).

  - [ABAP - Core Data Services](abap-core-data-services-abap-cds/abencds.md)

    The ABAP Core Data Services (ABAP CDS) are the ABAP-specific implementation of SAP's [CDS](abap-glossary/abencds_glosry.md) concept. They are used to develop data models that go far beyond the capabilities of ABAP Dictionary. CDS entities can access ABAP Dictionary objects and can be used in ABAP programs. This section of the ABAP keyword documentation introduces the concepts of ABAP CDS and provides full descriptions of the programming languages used to define [CDS objects](abap-glossary/abencds_object_glosry.md) in the ABAP development tools for Eclipse (ADT), such as [CDS DDL](abap-glossary/abencds_ddl_glosry.md), [CDS DCL](abap-glossary/abencds_ddl_glosry.md), [CDS SDL](abap-glossary/abencds_sdl_glosry.md), or [RAP BDL](abap-glossary/abencds_bdl_glosry.md).

- **Application Programming**

  - [ABAP - Programming Language](abap-programming-language/abenabap_reference.md)

    The [ABAP language](abap-glossary/abenabala_glosry.md) (ABAP for short) is the main programming language of the [ABAP development environment (ABAP DE)](abap-glossary/abenabap_dev_envir_glosry.md) provided by an [ABAP system](abap-glossary/abenabap_system_glosry.md). It is the namesake for the [Application Server ABAP](abap-glossary/abenas_abap_glosry.md) (or AS ABAP) and many of its components. ABAP is the programming interface of an [AS ABAP](abap-glossary/abenas_abap_glosry.md) and is used for the development of system programs and application programs that are usually based on objects in ABAP Dictionary or in ABAP CDS. This section of the ABAP keyword documentation provides a full description of the ABAP programming language and its object-oriented part, [ABAP Objects](abap-glossary/abenabap_objects_glosry.md). It also provides descriptions of the XML-based language elements for [Simple Transformations](abap-glossary/abensimple_transformation_glosry.md).

  - [ABAP - RAP Business Objects](abap-rap-business-objects/abenabap_rap.md)

    The [ABAP RESTful Application Programming Model (RAP)](abap-glossary/abenarap_glosry.md) is a programming model that is [RESTful](abap-glossary/abenrestful_glosry.md) or that meets the requirements of a [REST](abap-glossary/abenrest_glosry.md) architecture. In ABAP RAP, [AS ABAP](abap-glossary/abenas_abap_glosry.md) plays the role of a stateless Web server. [OData](abap-glossary/abenodata_glosry.md) serves as the RESTful protocol for requests from Web clients and the state of a session can be saved to the [standard database](abap-glossary/abenstandard_db_glosry.md). The modeling is based on [CDS entities](abap-glossary/abencds_entity_glosry.md) and [RAP behavior definitions](abap-glossary/abencds_behavior_definition_glosry.md). This section of the ABAP keyword documentation describes the modeling, implementation, publication, and consumption of [RAP business objects](abap-glossary/abenrap_bo_glosry.md), including [RAP business services](abap-glossary/abenbusiness_service_glosry.md), [RAP behavior definitions](abap-glossary/abencds_behavior_definition_glosry.md), and [ABAP EML](abap-glossary/abeneml_glosry.md) for providing and consuming RAP BOs.

- **Additional Information**

  - [ABAP APIs](abap-apis/abenabap_versions_and_apis.md)

    Rules on how to develop robust ABAP programs using [released APIs](abap-glossary/abenreleased_api_glosry.md).

  - [ABAP - Release News](abap-release-news/abennews.md)

    List of release-specific changes and enhancements to ABAP and the other

    programming languages.

- **Alphabetic Directories**

  - [ABAP - Glossary](abap-glossary/abenabap_glossary.md)

    Terms in ABAP and their explanations.

- **Domain-Specific Glossaries**

  Terms and their definitions for specific subject areas.

  - [ABAP Technology Glossary](abap-programming-language/abap-overview/abentechno_glossary.md)

  - [DDIC Glossary](abap-dictionary-ddic/abenddic_glossary.md)

  - [ABAP CDS Glossary](abap-core-data-services-abap-cds/abencds_glossary.md)

  - [ABAP Language Glossary](abap-programming-language/abenabala_glossary.md)

  - [RAP Glossary](abap-rap-business-objects/abenrap_glossary.md)

  - [ABAP SQL - Glossary](abap-programming-language/abap-database-access/abensql_glossary.md)

  - [AMDP - Glossary](abap-programming-language/abap-database-access/abenamdp_glossary.md)

## Hint

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The database tables of the flight data model used in the example programs can be filled using the class `CL_DEMO_FILL_FLIGHT_MODEL_TABS`.
