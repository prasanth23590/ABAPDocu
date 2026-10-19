---
title: "ABAP Technology Glossary"
source_file: abentechno_glossary.html
section: "ABAP Programming Language > ABAP - Overview"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Technology Glossary

In the following, terms of the [ABAP Glossary](../../abap-glossary/abenabap_glossary.md) are listed, that are relevant for the [ABAP technology](../../abap-glossary/abenabap_techno_glosry.md).

**ABAP**

Advanced Business Application Programming. ABAP in the actual sense is the name of the [ABAP language](../../abap-glossary/abenabala_glosry.md), but in a broader sense it is also the term for the entire [ABAP technology](../../abap-glossary/abenabap_techno_glosry.md) provided for and by an [ABAP system](../../abap-glossary/abenabap_system_glosry.md).

**ABAP Analytical Engine**

The ABAP Analytical Engine implements the [OLAP](../../abap-glossary/abenolap_glosry.md) concept on [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). It processes multidimensional data models to be consumed by analytical clients such as SAP Analytics Cloud. Clients communicate with the ABAP Analytical Engine using protocols such as the [InA](../../abap-glossary/abenina_glosry.md) protocol. The ABAP Analytical Engine performs calculations either on the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) or in the [ABAP language](../../abap-glossary/abenabala_glosry.md).

**ABAP Channels**

Framework for event-based communication using messages between [AS instances](../../abap-glossary/abenas_instance_glosry.md) and with the Internet. There are ABAP Messaging Channels (AMC) and ABAP Push Channels (APC).

**ABAP Cloud**

ABAP development model for state-of-the-art, cloud-ready and upgrade-stable solutions. Compared to [classic ABAP](../../abap-glossary/abenclassic_abap_glosry.md), ABAP Cloud uses the [ABAP technology](../../abap-glossary/abenabap_techno_glosry.md) with the following restrictions:

- The [ABAP language version](../../abap-glossary/abenabap_version_glosry.md) is restricted to the [restricted ABAP language version](../../abap-glossary/abenrestricted_version_glosry.md) [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md).

- Access to other [repository objects](../../abap-glossary/abenrepository_object_glosry.md) is restricted to APIs that are [released](../../abap-glossary/abenreleased_api_glosry.md) for [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md).

- Only [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md) can be used. There is no access to SAP GUI.

The transactional programming model for ABAP Cloud is [RAP](../../abap-glossary/abenrap_glosry.md).

ABAP Cloud is supported in all SAP products that are based on ABAP technology. It is fully or partly mandatory in

- [SAP BTP ABAP environment](../../abap-glossary/abensap_btp_abap_env_glosry.md)

- [SAP S/4HANA Cloud Public Edition](../../abap-glossary/abensap_s4hana_cpub_glosry.md)

- [SAP S/4HANA Cloud Private Edition](../../abap-glossary/abensap_s4hana_cpriv_glosry.md)

On the [ABAP Platform](../../abap-glossary/abenabap_platform_glosry.md) of [SAP S/4HANA](../../abap-glossary/abensap_s4hana_glosry.md) it is available besides classic ABAP.

**ABAP daemon**

Instance of an ABAP daemon class that is automatically regenerated whenever a [runtime error](../../abap-glossary/abenruntime_error_glosry.md) or a message of type `E`, *A*, or *X* results in program termination. A separate ABAP daemon session is created for each ABAP daemon during its instantiation. ABAP daemons react to ABAP daemon events and have access to a special ABAP daemon memory.

The properties of an ABAP daemon are defined in a [repository object](../../abap-glossary/abenrepository_object_glosry.md) that is also called ABAP daemon.

**ABAP daemon class**

Global subclass of `CL_ABAP_DAEMON_EXT_BASE`. The instances of an ABAP daemon class are ABAP daemons created by the ABAP daemon framework, each of which are executed in a separate ABAP daemon session. An ABAP daemon class implements interface methods inherited from the superclass to react to ABAP daemon events.

**ABAP daemon event**

Event in the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md) to which an ABAP daemon reacts using the [methods](../../abap-glossary/abenmethod_glosry.md) of the [interface](../../abap-glossary/abenoo_intf_glosry.md) `IF_ABAP_DAEMON_EXTENSION`. ABAP daemon events can be raised in ABAP programs or by the ABAP runtime framework.

**ABAP daemon framework**

ADF for short. A framework based on [classes](../../abap-glossary/abenclass_glosry.md) and [interfaces](../../abap-glossary/abenoo_intf_glosry.md) for using ABAP daemons. ADF includes APIs both for communication with ABAP daemons in [ABAP programs](../../abap-glossary/abenabap_program_glosry.md) and for handling events using ABAP daemons in ABAP daemon sessions.

**ABAP daemon handle**

ABAP daemon framework object that implements the [interface](../../abap-glossary/abenoo_intf_glosry.md) `IF_ABAP_DAEMON_HANDLE`. An ABAP daemon handle enables users to send PCP messages to the daemon using the `SEND` method.

**ABAP daemon manager**

The class `CL_ABAP_DAEMON_CLIENT_MANAGER`. The static methods of the ABAP daemon manager are used to create and use ABAP daemons in [ABAP programs](../../abap-glossary/abenabap_program_glosry.md).

**ABAP daemon memory**

Part of the user memory in which an ABAP daemon can store data in PCP format. An ABAP daemon can use approximately 1 megabyte of the ABAP daemon memory.

**ABAP daemon processing**

Processing of an ABAP daemon. ABAP daemon processing takes place in a dedicated ABAP daemon session and in non-blocking mode where blocking statements are not allowed.

**ABAP daemon session**

[User session](../../abap-glossary/abenuser_session_glosry.md) for ABAP daemon processing. An ABAP daemon session is created by the ABAP daemon framework (ADF) when an ABAP daemon is instantiated.

**ABAP database schema**

[Database schema](../../abap-glossary/abendatabase_schema_glosry.md) of the [standard database](../../abap-glossary/abenstandard_db_glosry.md) assigned to the [database user name](../../abap-glossary/abendatabase_user_name_glosry.md) used for database accesses to an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) via the [standard connection](../../abap-glossary/abenstandard_db_connection_glosry.md). If the standard connection is used, a [work process](../../abap-glossary/abenwork_process_glosry.md) acting as a [database user](../../abap-glossary/abendatabase_user_glosry.md) accesses the objects of this database schema implicitly. The objects of a database that are managed by the [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md) and implementations of [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md) are located in the ABAP database schema. The name of the ABAP database schema of an AS ABAP can be determined using the function module `DB_DBSCHEMA_CURRENT`.

**ABAP Debugger**

Tool used to execute [ABAP programs](../../abap-glossary/abenabap_program_glosry.md) line by line or section by section. This makes it possible to edit the content of [data objects](../../abap-glossary/abendata_object_glosry.md) and to check the program logic. See also [breakpoint](../../abap-glossary/abenbreakpoint_glosry.md).

**ABAP development environment**

ABAP DE for short. Development environment provided by the [ABAP technology](../../abap-glossary/abenabap_techno_glosry.md) for [repository objects](../../abap-glossary/abenrepository_object_glosry.md) that form ABAP applications. It mainly consists of:

- Its main programming language [ABAP](../../abap-glossary/abenabala_glosry.md) and other programming languages such as [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) for metadata definitions.

- Development tools such as [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md) or the ABAP Workbench.

- Other [repository objects](../../abap-glossary/abenrepository_object_glosry.md) that can be accessed as APIs.

Depending on the programming paradigm [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md) or [classic ABAP](../../abap-glossary/abenclassic_abap_glosry.md), ABAP development environments are either restricted or unrestricted.

- In [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md):

  - The [ABAP language version](../../abap-glossary/abenabap_version_glosry.md) is restricted to [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md).

  - Access to other [repository objects](../../abap-glossary/abenrepository_object_glosry.md) is restricted to [released APIs](../../abap-glossary/abenreleased_api_glosry.md).

  - Only [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md) can be used. There is no access to SAP GUI.

- In [classic ABAP](../../abap-glossary/abenclassic_abap_glosry.md):

  - The [ABAP language version](../../abap-glossary/abenabap_version_glosry.md) can be chosen freely.

  - [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md) and the ABAP Workbench can both be used.

  - Access to other [repository objects](../../abap-glossary/abenrepository_object_glosry.md) is not restricted.

The deployment of repository objects is managed by an integrated [Change and Transport System (CTS)](../../abap-glossary/abencts_glosry.md).

**ABAP development tools for Eclipse**

ADT for short. Eclipse-based tools for editing [repository objects](../../abap-glossary/abenrepository_object_glosry.md) of the [ABAP Repository](../../abap-glossary/abenabap_repository_glosry.md) and their components. The ADT currently cover a subset of the ABAP Workbench functions. In the case of newer repository objects, sometimes only ADT can be used.

**ABAP Doc**

ABAP Doc is a documentation tool that enables documentation files to be created automatically in HTML format from [ABAP source code](../../abap-glossary/abenabap_source_code_glosry.md). ABAP Doc is based on special [ABAP Doc comments](../../abap-glossary/abenabap_doc_comment_glosry.md).

**ABAP Doc comment**

Special [comment](../../abap-glossary/abencomment_glosry.md) consisting of one or more [comment lines](../../abap-glossary/abencomment_line_glosry.md), each of which is initiated by `"!`. ABAP Doc comments can precede [declarations](../../abap-glossary/abendeclaration_glosry.md) and are used by [ABAP Doc](../../abap-glossary/abenabap_doc_glosry.md) for their documentation.

**ABAP Dump Analysis**

Tool for listing and analyzing [runtime errors](../../abap-glossary/abenruntime_error_glosry.md) that occurred in [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) and that can be used to access the affiliated [short dumps](../../abap-glossary/abenshort_dump_glosry.md). Called using transaction `ST22`.

**ABAP Editor**

ABAP Workbench tool for creating [ABAP programs](../../abap-glossary/abenabap_program_glosry.md). It is either called directly using transaction code `SE38` or it is integrated into other tools, such as Object Navigator, Class Builder, or Function Builder.

**ABAP Enhancement Framework**

Framework for [enhancing](../../abap-glossary/abenenhancement_glosry.md) [repository objects](../../abap-glossary/abenrepository_object_glosry.md). The ABAP Enhancement Framework comprises the Enhancement Builder tool of the ABAP Workbench and specific [ABAP statements](../abap-enhancements/abenenhancement_framework.md) for enhancing [ABAP source code](../../abap-glossary/abenabap_source_code_glosry.md).

**ABAP environment**

ABAP environment may refer to:

- [SAP BTP ABAP environment](../../abap-glossary/abensap_btp_abap_env_glosry.md).

- [ABAP development environment](../../abap-glossary/abenabap_dev_envir_glosry.md).

- [SAP S/4HANA Cloud ABAP environment](../../abap-glossary/abens4_hana_cloud_abap_env_glosry.md)

- AS ABAP system environment

- [ABAP runtime environment](../../abap-glossary/abenabap_runtime_envir_glosry.md)

**ABAP for Cloud Development**

[Restricted ABAP language version](../../abap-glossary/abenrestricted_version_glosry.md) with restricted language scope and restricted access to [released APIs](../../abap-glossary/abenreleased_api_glosry.md). In ABAP for Cloud Development, [client isolation](../../abap-glossary/abenclient_isolation_glosry.md) is enforced. ABAP for Cloud Development is the [ABAP language version](../../abap-glossary/abenabap_version_glosry.md) for [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md).

**ABAP for Key Users**

[Restricted ABAP language version](../../abap-glossary/abenrestricted_version_glosry.md) with restricted language scope and restricted access to [released APIs](../../abap-glossary/abenreleased_api_glosry.md) for [enhancements](../../abap-glossary/abenenhancement_glosry.md) made by key users at dedicated enhancement points. ABAP for Key Users is available in the special enhancement tools for key users.

**ABAP memory**

Memory area within each [ABAP session](../../abap-glossary/abenabap_session_glosry.md) that can be accessed jointly by the programs of a call sequence using the statements [`EXPORT`](../abap-data-cluster/abapexport_data_cluster.md) and [`IMPORT`](../abap-data-cluster/abapimport_data_cluster.md), and whose data is persisted for the duration of the top-level transaction of a call sequence.

**ABAP messaging channel**

[Repository object](../../abap-glossary/abenrepository_object_glosry.md) that defines the properties of AMC communication.

**ABAP Messaging Channels**

AMC for short. Framework for communication between the [ABAP programs](../../abap-glossary/abenabap_program_glosry.md) of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). Communication is enabled by sending and receiving [data objects](../../abap-glossary/abendata_object_glosry.md) as messages across the boundaries of an [AS instance](../../abap-glossary/abenas_instance_glosry.md).

**ABAP Platform**

Name for the [ABAP technology](../../abap-glossary/abenabap_techno_glosry.md) shipped as a basis of [SAP S/4HANA](../../abap-glossary/abensap_s4hana_glosry.md) and [SAP S/4HANA Cloud Private Edition](../../abap-glossary/abensap_s4hana_cpriv_glosry.md). The release numbering of an ABAP Platform is based on the respective SAP S/4HANA release. An ABAP Platform supports the programming paradigm [classic ABAP](../../abap-glossary/abenclassic_abap_glosry.md) but programming according to the rules of [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md) is also possible and encouraged.

**ABAP programming model for SAP Fiori**

Obsolete programming model for SAP HANA-optimized Fiori apps based on the [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). Its successor is the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md).

**ABAP push channel**

[Repository object](../../abap-glossary/abenrepository_object_glosry.md) that defines the APC handler class, a node in the ICF service tree, the protocol (Web socket or TCP), an optional subprotocol (PCP), and other properties for an APC server.

**ABAP Push Channels**

APC for short. Framework for bidirectional communication between an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) and the Internet using the WebSocket protocol or TCP socket protocol. ABAP Push Channels can be linked with ABAP Messaging Channels.

**ABAP Repository**

Part of the [standard database](../../abap-glossary/abenstandard_db_glosry.md) of [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) that contains client-independent [repository objects](../../abap-glossary/abenrepository_object_glosry.md). The repository can be searched using the Repository Information System.

**ABAP runtime framework**

Also called ABAP runtime environment. Hardware- and operating system-independent platform (virtual machine) of an [ABAP program](../../abap-glossary/abenabap_program_glosry.md). Processes of the ABAP runtime framework control the execution of an ABAP program by calling the [processing blocks](../../abap-glossary/abenprocessing_block_glosry.md) of the program. [ABAP statements](../../abap-glossary/abenabap_statement_glosry.md) are implemented in the [ABAP kernel](../../abap-glossary/abenkernel_glosry.md) of the ABAP runtime framework. The ABAP runtime framework is provided by the [Application Server ABAP](../../abap-glossary/abenas_abap_glosry.md) and, therefore, [ABAP programs](../../abap-glossary/abenabap_program_glosry.md) can only be executed in AS ABAP.

**ABAP session**

Instance for a [user session](../../abap-glossary/abenuser_session_glosry.md) of an [AS instance](../../abap-glossary/abenas_instance_glosry.md) with the ABAP Memory as a separate memory area. Each GUI window of a user session is linked with its own ABAP session. A maximum of 16 ABAP sessions can be managed by a single user session. An [ABAP program](../../abap-glossary/abenabap_program_glosry.md) is executed in an [internal session](../../abap-glossary/abeninternal_session_glosry.md) of an ABAP session.

**ABAP system**

[Client-server system](../../abap-glossary/abenclient_server_system_glosry.md) that is based on and provides [ABAP technology](../../abap-glossary/abenabap_techno_glosry.md). It consists of:

- ABAP-specific components of the [presentation layer](../../abap-glossary/abenpresentation_layer_glosry.md), such as SAP GUI or web-based technologies.

- [Application Server ABAP (AS ABAP)](../../abap-glossary/abenas_abap_glosry.md)

- [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md) of the [standard database](../../abap-glossary/abenstandard_db_glosry.md) of the AS ABAP storing both [system programs](../../abap-glossary/abensystem_program_glosry.md) and [system tables](../../abap-glossary/abensystem_table_glosry.md), as well as [application programs](../../abap-glossary/abenapplication_program_glosry.md) and [application tables](../../abap-glossary/abenapplication_table_glosry.md).

The name of an ABAP system matches the [system ID](../../abap-glossary/abensystem_id_glosry.md) of its AS ABAP.

**ABAP technology**

The ABAP technology or [ABAP](../../abap-glossary/abenabap_glosry.md) for short comprises the entire technology provided for and by an [ABAP system](../../abap-glossary/abenabap_system_glosry.md) for developing and executing ABAP-based applications. ABAP technology supports the programming paradigms [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md) and [classic ABAP](../../abap-glossary/abenclassic_abap_glosry.md).

**ABAP Test Cockpit**

ATC for short. Framework for executing and evaluating various tests for [repository objects](../../abap-glossary/abenrepository_object_glosry.md) integrated into ABAP Workbench or [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md) and the [Change and Transport System (CTS)](../../abap-glossary/abencts_glosry.md).

**ABAP timer**

A timer for wait times in non-blocking mode integrated into the ABAP runtime framework. An ABAP Timer is started using a timer manager for a given runtime and at the end a timeout event is raised, which can be responded to with a timer handler.

**ABAP timer handler**

[Class](../../abap-glossary/abenclass_glosry.md) that implements the [interface](../../abap-glossary/abenoo_intf_glosry.md) `IF_ABAP_TIMER_HANDLER`. The interface method `ON_TIMEOUT` of the timer handler, which is specified with a ABAP Timer Manager when an ABAP Timer is started. It handles the timeout event of the timer.

**ABAP timer manager**

Object of the [class](../../abap-glossary/abenclass_glosry.md) `CL_ABAP_TIMER_MANAGER` that is accessed using the [interface](../../abap-glossary/abenoo_intf_glosry.md) `IF_ABAP_TIMER_MANAGER`. A timer manager allows an ABAP Timer to be started and stopped in non-blocking mode. When the timer is started, a runtime and an ABAP Timer handler are defined.

**ABAP Unit**

Test tool integrated into the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md) that is used for checking the functions of code units in a program ([unit tests](../../abap-glossary/abenunit_test_glosry.md)). Individual tests are implemented as [test methods](../../abap-glossary/abentest_method_glosry.md) of local [test classes](../../abap-glossary/abentest_class_glosry.md) in ABAP programs. The tests of one test class use the same [fixture](../../abap-glossary/abenfixture_glosry.md). Global test classes can only be used in local test classes. The properties of a test can be specified in the definition of a local test class. Tests of multiple ABAP programs can be combined into [test tasks](../../abap-glossary/abentest_task_glosry.md).

**ABAP user**

In the context of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) also user for short.

1.  Defined in the AS ABAP by a [user name](../../abap-glossary/abenuser_name_glosry.md) and a [user master record](../../abap-glossary/abenuser_master_record_glosry.md) in transaction code `SU01`.

2.  User (person or other system) that is logged on to the AS ABAP.

Once ABAP users have logged on to the AS ABAP and have been authenticated, they can access the functions and objects of the AS ABAP during their [user session](../../abap-glossary/abenuser_session_glosry.md) in accordance with their [authorizations](../../abap-glossary/abenauthorization_glosry.md).

**ABAP Workbench**

SAP GUI-based part of an [ABAP development environment](../../abap-glossary/abenabap_dev_envir_glosry.md) for [repository objects](../../abap-glossary/abenrepository_object_glosry.md) in [ABAP Repository](../../abap-glossary/abenabap_repository_glosry.md) and their components. Contains tools for processing and managing almost all repository objects. Accessed using either forward navigation, Object Navigator, transaction codes, or SAP Easy Access. Some newer repository objects can only be edited in the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md).

**ABAP-managed database object**

[Database object](../../abap-glossary/abendb_object_glosry.md) in the [standard database](../../abap-glossary/abenstandard_db_glosry.md) of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) that is both managed and used by AS ABAP. Only ABAP should be used to access an ABAP-managed database object.

**ABAP-managed HDI container**

AMHC for short. Special HDI container managed by [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). An AMHC is created and changed using transaction `SCTS_AMHC`. An AMHC and the contained HDI objects are connected to the [Change and Transport System](../../abap-glossary/abencts_glosry.md) using SAP HANA Transport for ABAP (HTA). When an AMHC is created, a logical HDI container is defined and during its activation a physical HDI container is created in the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md). The logical HDI container can be a logical schema in an [AMDP macro](../../abap-glossary/abenamdp_macro_glosry.md) where it represents the [database schema](../../abap-glossary/abendatabase_schema_glosry.md) of the physical HDI container.

**activatable checkpoint**

[Checkpoint](../../abap-glossary/abencheckpoint_glosry.md) that is assigned to a [checkpoint group](../../abap-glossary/abencheckpoint_group_glosry.md) using the addition `ID` of the statements [`ASSERT`](../abap-program-maintenance/abapassert.md), `BREAK-POINT`, or `LOG-POINT`. The behavior of an activatable checkpoint is controlled by either group-specific or program-specific activation settings, where program-specific settings apply to all activatable checkpoints of a program and overwrite the settings of the relevant checkpoint group.

**activation variant**

[Repository object](../../abap-glossary/abenrepository_object_glosry.md) that contains activation settings for [activatable checkpoints](../../abap-glossary/abenactivatable_checkpoint_glosry.md). An activation variant can contain settings for [checkpoint groups](../../abap-glossary/abencheckpoint_group_glosry.md) and [compilation units](../../abap-glossary/abencompilation_unit_glosry.md). Activation variants are created and the activation settings are maintained using transaction `SAAB`.

**additional program group**

[Program group](../../abap-glossary/abenprogram_group_glosry.md) of an [internal session](../../abap-glossary/abeninternal_session_glosry.md). Created when a [function pool](../../abap-glossary/abenfunction_pool_glosry.md) is loaded into the internal session using an external procedure call or a [class pool](../../abap-glossary/abenclass_pool_glosry.md) via its global [class](../../abap-glossary/abenclass_glosry.md). The function pool or class pool is the main program of the additional program group. An additional program group and its data remain for the entire duration of the internal session.

**ADF**

*-\>* ABAP daemon framework

**AMC**

*-\>* ABAP Messaging Channels

**AMDP BAdI**

Special [BAdI](../../abap-glossary/abenbadi_glosry.md) for [AMDP procedure implementations](../../abap-glossary/abenamdp_procedure_method_glosry.md). If the associated [AMDP procedure](../../abap-glossary/abenamdp_procedure_glosry.md) is called from a different [AMDP method](../../abap-glossary/abenamdp_method_glosry.md), this takes place based on the switch-based rules of the ABAP Enhancement Framework.

**APC**

*-\>* ABAP Push Channels

**APC handler class**

[Global class](../../abap-glossary/abenglobal_class_glosry.md) in which the handling of a query sent to an ABAP push channel in [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) is implemented. The request is handled as APC processing in a separate APC session.

**APC processing**

Processing of a WebSocket or TCP request using the APC framework in an APC handler class. APC processing takes place in a dedicated APC session. APC processing can be stateless or stateful. Stateful APC processing must take place in non-blocking mode, where blocking statements are forbidden.

**APC server**

Instance of a system that provides services that can be called using APC. An APC server can be a WebSocket server or a TCP server.

**APC session**

[User session](../../abap-glossary/abenuser_session_glosry.md) for APC processing. An APC session is opened by the APC framework for the handling of a WebSocket or TCP queries in an APC handler class.

**application client**

[Client](../../abap-glossary/abenclient_glosry.md) of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) used for the processing data of [application tables](../../abap-glossary/abenapplication_table_glosry.md) in [application programs](../../abap-glossary/abenapplication_program_glosry.md).

**application layer**

Software layer of a [client-server system](../../abap-glossary/abenclient_server_system_glosry.md) that contains the application logic. [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) represents the application layer of an [ABAP system](../../abap-glossary/abenabap_system_glosry.md) in which [ABAP programs](../../abap-glossary/abenabap_program_glosry.md) are executed.

**Application Server ABAP**

AS ABAP for short. AS ABAP represents the [application layer](../../abap-glossary/abenapplication_layer_glosry.md) of an [ABAP system](../../abap-glossary/abenabap_system_glosry.md) in which [ABAP programs](../../abap-glossary/abenabap_program_glosry.md) are executed. It provides the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md) and contains communication components such as the RFC interface, Internet Communication Manager (ICM), and ABAP Channels. It supports Internet protocols (HTTP/HTTPS/SMTP, WebSocket protocol, and TCP) and [XML](../../abap-glossary/abenxml_glosry.md). AS ABAP is implemented from a single message server and one or more [AS instances](../../abap-glossary/abenas_instance_glosry.md). It has a [system ID](../../abap-glossary/abensystem_id_glosry.md) that [ABAP users](../../abap-glossary/abenabap_user_glosry.md) can use to [log on](../../abap-glossary/abenlogon_glosry.md) and a dedicated user administration based on a [user master record](../../abap-glossary/abenuser_master_record_glosry.md).

**application server instance**

AS instance for short. Component of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). An AS ABAP can be implemented using one or more AS instances, which are usually instantiated on different [host computers](../../abap-glossary/abenhost_computer_glosry.md). However, multiple AS instances of one or more AS ABAP can also be instantiated on the same host computer. Each AS instance has [work processes](../../abap-glossary/abenwork_process_glosry.md) to execute [ABAP programs](../../abap-glossary/abenabap_program_glosry.md). The memory areas of an AS instance that can be accessed in the ABAP programs are the [shared memory](../../abap-glossary/abenshared_memory_glosry.md), the user memory, the ABAP memory, and the [session memory](../../abap-glossary/abenroll_area_glosry.md) in the [internal session](../../abap-glossary/abeninternal_session_glosry.md).

**ArchiveLink**

Service used to link applications of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) with archived documents.

**archiving**

Storing of spool lists using the ArchiveLink tool. Spool lists stored in the SAP spool system can be archived. During archiving, spool lists passed from the spool system are saved in the same format that was used there.

**archiving parameter**

A parameter that must be passed to a spool request if its data is to be archived using ArchiveLink.

**area**

[Repository object](../../abap-glossary/abenrepository_object_glosry.md) used for the managing and storage of shared objects. An area is the template for area instance versions in the [shared memory](../../abap-glossary/abenshared_memory_glosry.md). An identically named area class and any area root class are assigned to each area. Areas are created and managed using transaction `SHMA`.

**area class**

[Final](../../abap-glossary/abenfinal_glosry.md) global [class](../../abap-glossary/abenclass_glosry.md) whose instances are used as area handles for shared objects. The [attributes](../../abap-glossary/abenattribute_glosry.md) of the instances of an area class represent the properties of an area. The [methods](../../abap-glossary/abenmethod_glosry.md) of an area class are used to access the area. All area classes are [subclasses](../../abap-glossary/abensubclass_glosry.md) of `CL_ABAP_MEMORY_AREA`. When creating areas, area classes of the same name are generated as subclasses of `CL_SHM_AREA`. A special predefined area class is `CL_IMODE_AREA`, whose instance represents the area handle for the [internal session](../../abap-glossary/abeninternal_session_glosry.md) of a program.

**area handle**

Instance of an area class. An area handle allows an ABAP program access to an area instance version in the [shared memory](../../abap-glossary/abenshared_memory_glosry.md) and to the shared objects stored there. An area handle is created by the static methods of its area class and is bound to an area instance version. Each bound area handle sets an area lock on the affected area instance version.

**area instance**

Sum of all area instance versions with the same area instance name. An area instance is a unique variant of an area and is divided into versions.

**area instance version**

Variant of an area in the shared objects memory. In an area instance version, shared objects are stored in the form of [anonymous data objects](../../abap-glossary/abenanonymous_data_object_glosry.md) or instances of shared memory-enabled classes, where for every area instance version, there is at least one instance of the root data class of the area. The creation of and access to area instance versions takes place exclusively using area handles. Each area instance version has a name. Area instance versions with the same name form an area instance.

**area lock**

Read lock or change lock (write lock, update lock) on an area instance version in the shared objects memory. Area locks are set by binding area handles to area instance versions.

**area menu**

Tree structure whose nodes can be linked with transaction codes, executable programs, and other area menus. Area menus are maintained using transaction code `SE43` and displayed via SAP Easy Access.

**area root class**

A global shared memory-enabled class that must be assigned to an area when it is defined. A non-empty area instance version contains at least one instance of the area root class as the root object.

**aRFC**

*-\>* asynchronous remote function call

**AS ABAP release**

*-\>* [ABAP release](../../abap-glossary/abenabap_release_glosry.md)

**AS ABAP system environment**

Current system environment of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md), consisting of the operating system of the [host computer](../../abap-glossary/abenhost_computer_glosry.md) of the current [AS instance](../../abap-glossary/abenas_instance_glosry.md), the [database system](../../abap-glossary/abendatabase_system_glosry.md), the [text environment](../../abap-glossary/abentext_environment_glosry.md), and the communication interfaces.

**asJSON**

ABAP Serialization JSON. Abbreviation for the [canonical JSON representation](../../abap-glossary/abencanonical_json_represen_glosry.md) of ABAP data.

**asJSON-XML**

[JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) representation of [asJSON](../../abap-glossary/abenasjson_glosry.md).

**asXML**

ABAP Serialization XML. Short name for the [canonical XML representation](../../abap-glossary/abencanonical_xml_represent_glosry.md) of ABAP data.

**asynchronous Remote Function Call**

aRFC for short. Remote function call that does not wait for the end of processing of the remotely called function.

**asynchronous update**

Update in which update function modules are executed with high priority in the update work process, whereby the calling program does not wait for termination. Asynchronous updates are started by [`COMMIT WORK`](../abap-database-access/abapcommit.md) without the addition `AND WAIT` and are executed in a separate update session.

**ATC**

*-\>* [ABAP Test Cockpit](../../abap-glossary/abenabap_test_cockpit_glosry.md)

**authorization**

Entry in the [user master record](../../abap-glossary/abenuser_master_record_glosry.md) as part of an [authorization profile](../../abap-glossary/abenauthorization_profile_glosry.md). An authorization consists of complete or generic values for the [authorization fields](../../abap-glossary/abenauthorization_field_glosry.md) of an [authorization object](../../abap-glossary/abenauthorization_object_glosry.md). The combination specifies which activities an [ABAP user](../../abap-glossary/abenabap_user_glosry.md) can use to access which data. Authorizations are generated with the profile generator from role management tool (transaction `PFCG`) and can be displayed using transaction code `SU03`.

**authorization assignment**

Creates [authorization profiles](../../abap-glossary/abenauthorization_profile_glosry.md) in the [user master record](../../abap-glossary/abenuser_master_record_glosry.md).

**authorization field**

Smallest unit of an [authorization object](../../abap-glossary/abenauthorization_object_glosry.md). An authorization field represents either data such as a [key field](../../abap-glossary/abenkey_field_glosry.md) of a [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md) or activities such as reading or changing. Activities are specified as abbreviations that are stored in the DDIC database table `TACT` and in `TACTZ` for customers.

**authorization group**

[Program property](../../abap-glossary/abenprogram_property_glosry.md) that allows the combination of different programs into groups for shared [authorization checks](../../abap-glossary/abenauthorization_check_glosry.md). The group name is an [authorization field](../../abap-glossary/abenauthorization_field_glosry.md) of the [authorization object](../../abap-glossary/abenauthorization_object_glosry.md) `S_PROGRAM`, for which an [authorization check](../../abap-glossary/abenauthorization_check_glosry.md) is performed when an executable program is executed using the statement `SUBMIT`. This is done to check whether the current [ABAP user](../../abap-glossary/abenabap_user_glosry.md) is authorized to execute the program. All authorization groups should be stored in the database table `TPGP`.

**authorization object**

A [repository object](../../abap-glossary/abenrepository_object_glosry.md) that is the basis of [authorizations](../../abap-glossary/abenauthorization_glosry.md). An authorization object consists of up to ten [authorization fields](../../abap-glossary/abenauthorization_field_glosry.md). The combination of authorization fields that represent data and activities is used for [authorization assignments](../../abap-glossary/abenauthorization_assign_glosry.md) and [authorization checks](../../abap-glossary/abenauthorization_check_glosry.md). Authorization objects are grouped in authorization object classes. They are maintained using transaction `SU21`.

**authorization profile**

A summary of multiple [authorizations](../../abap-glossary/abenauthorization_glosry.md). An authorization can be assigned to multiple authorization profiles. Entering authorization profiles in the [user master record](../../abap-glossary/abenuser_master_record_glosry.md) assigns [user names](../../abap-glossary/abenuser_name_glosry.md) to authorizations. Authorization profiles can be generated by the profile generator from role maintenance (transaction `PFCG`) or be displayed using transaction code `SU02`.

**background job**

*-\>* background request

**background processing**

Execution of [ABAP programs](../../abap-glossary/abenabap_program_glosry.md) with defined settings in the background, that is, with no on-screen user dialog. In contrast to dialog processing, the execution process is predefined when the program is started. An executable program is scheduled in ABAP Editor or after calling *System -\> Services -\> Reporting* via the menu *Program -\> Execute -\> Background* for automatic execution or is called in the background using `SUBMIT VIA JOB`. Background processing takes place in a separate background session and at least one background [work process](../../abap-glossary/abenwork_process_glosry.md) must be configured.

**background processing framework**

The background processing framework (bgPF) is a framework that asynchronously and reliably executes methods of applications that develop background processes. It is based on the background remote function call and supports the inbound scenario. Background processes are executed transactionally and with a service quality of *Exactly Once (EO)*. The bgPF can ensure transactional consistency within the controlled SAP LUW.

**background Remote Function Call**

bgRFC for short. Asynchronous remote function call for which the called RFMs can be executed transactionally and in a predefined call sequence. bgRFC replaces tRFC and qRFC apart from the no-send scenario of qRFC. The latter is replaced by the local data queue (LDQ).

**background request**

Job used to start one or more [ABAP programs](../../abap-glossary/abenabap_program_glosry.md) in background processing. A background request consists of background tasks.

**background session**

[User session](../../abap-glossary/abenuser_session_glosry.md) for background processing. A background session is opened when a program is executed using `SUBMIT VIA JOB`.

**background task**

Subunit of a background request.

**BAdI**

Business Add-In, template for [BAdI objects](../../abap-glossary/abenbadi_object_glosry.md). A BAdI consists of a [BAdI interface](../../abap-glossary/abenbadi_interface_glosry.md), a set of filters, and various settings. BAdIs are the basis for [enhancements](../../abap-glossary/abenenhancement_glosry.md), for which [BAdI methods](../../abap-glossary/abenbadi_method_glosry.md) in [object plug-ins](../../abap-glossary/abenobject_plugin_glosry.md) can be called in ABAP programs, whereby the caller can control which [BAdI implementations](../../abap-glossary/abenbadi_implementation_glosry.md) are used by specifying the filter values. BAdIs can also be defined as screen or menu enhancements for dynpros or GUI status. BAdIs are edited as [enhancement spot element definitions](../../abap-glossary/abenenhancement_spot_def_glosry.md) in Enhancement Builder and are in the namespace of the global [classes](../../abap-glossary/abenclass_glosry.md). Their implementations can be switched on and off using the [Switch Framework](../../abap-glossary/abenswitch_framework_glosry.md). Furthermore, there are also the classic BAdIs that were processed directly in the BAdI Builder and replaced the function module exits.

**BAdI Builder**

ABAP Workbench tool that can be used to create and maintain [BAdIs](../../abap-glossary/abenbadi_glosry.md). The BAdI Builder is the BAdI-specific variant of access to the Enhancement Builder. Previously, the BAdI Builder was used exclusively for the maintenance of classic BAdIs. Called using transactions `SE18` (definition) and `SE19` (implementation).

**BAdI class**

Specific global class that is created when a [BAdI](../../abap-glossary/abenbadi_glosry.md) is defined in the Enhancement Builder and given the name of the BAdI as a [subclass](../../abap-glossary/abensubclass_glosry.md) of the [abstract](../../abap-glossary/abenabstract_glosry.md) global [class](../../abap-glossary/abenclass_glosry.md) `CL_BADI_BASE`. BAdI classes are a part of the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md) and, apart from being in the namespace of all global [types](../../abap-glossary/abentype_glosry.md), they are not visible externally.

**BAdI context object**

[Instance](../../abap-glossary/abeninstance_glosry.md) of a [class](../../abap-glossary/abenclass_glosry.md) that implements the [tag interface](../../abap-glossary/abentag_interface_glosry.md) `IF_BADI_CONTEXT`. This tag interface can be implemented by any class. [References](../../abap-glossary/abenreference_glosry.md) to BAdI context objects can be used in the statement [`GET BADI`](../abap-enhancements/abapget_badi.md) to specify a context for [object plug-ins](../../abap-glossary/abenobject_plugin_glosry.md).

**BAdI implementation**

Implementation of a [BAdI](../../abap-glossary/abenbadi_glosry.md). Multiple BAdI implementations can be assigned to a single BAdI. A BAdI implementation consists of a [BAdI implementation class](../../abap-glossary/abenbadi_implement_class_glosry.md) and a filter condition that can be used to select the BAdI implementation in the [`GET BADI`](../abap-enhancements/abapget_badi.md) statement in the [BAdI object](../../abap-glossary/abenbadi_method_glosry.md). A BAdI implementation is created as an [enhancement implementation element](../../abap-glossary/abenenhancement_impl_elem_glosry.md) as part of an [enhancement](../../abap-glossary/abenenhancement_glosry.md) in Enhancement Builder, where it can be marked as a standard implementation. A BAdI implementation can be in the state *active* or *inactive*, which overrides both the [Switch Framework](../../abap-glossary/abenswitch_framework_glosry.md) setting and the filter condition.

**BAdI implementation class**

Global [class](../../abap-glossary/abenclass_glosry.md) that implements one or more [BAdI interfaces](../../abap-glossary/abenbadi_interface_glosry.md) and therefore also their [BAdI methods](../../abap-glossary/abenbadi_method_glosry.md). BAdI implementation classes are the main components of [BAdI implementations](../../abap-glossary/abenbadi_implementation_glosry.md), and their instances act as [object plug-ins](../../abap-glossary/abenobject_plugin_glosry.md) for functional [enhancements](../../abap-glossary/abenenhancement_glosry.md) of ABAP programs. A BAdI implementation class that is not part of a BAdI implementation is not linked to an [enhancement implementation](../../abap-glossary/abenenhancement_impl_glosry.md). The latter can be used, for example, as fallback BAdI implementation classes of [BAdIs](../../abap-glossary/abenbadi_glosry.md).

**BAdI interface**

A BAdI interface is a global [interface](../../abap-glossary/abenoo_intf_glosry.md) that includes the [tag interface](../../abap-glossary/abentag_interface_glosry.md) `IF_BADI_INTERFACE`. A BAdI interface can be used as part of the definition of one or more [BAdIs](../../abap-glossary/abenbadi_glosry.md) and may only contain [methods](../../abap-glossary/abenmethod_glosry.md) ([BAdI methods](../../abap-glossary/abenbadi_method_glosry.md)) and [events](../../abap-glossary/abenevent_glosry.md) but not variable [attributes](../../abap-glossary/abenattribute_glosry.md). Furthermore, a BAdI interface cannot contain any [component interfaces](../../abap-glossary/abencomponent_interface_glosry.md) other than other BAdI interfaces. An interface that includes a BAdI interface is also a BAdI interface.

**BAdI method**

[Method](../../abap-glossary/abenmethod_glosry.md) of a [BAdI interface](../../abap-glossary/abenbadi_interface_glosry.md). A BAdI method is implemented in [BAdI implementations](../../abap-glossary/abenbadi_implementation_glosry.md) and then called exclusively via the associated BAdI object using [`CALL BADI`](../abap-enhancements/abapcall_badi.md). If the BAdI interface is part of the definition of a [BAdI](../../abap-glossary/abenbadi_glosry.md) that is defined for multiple use, the [parameter interface](../../abap-glossary/abenparameter_interface_glosry.md) of a BAdI method can only contain [input parameters](../../abap-glossary/abeninput_parameter_glosry.md) and [input/output parameters](../../abap-glossary/abeninput_output_parameter_glosry.md). If all BAdIs are defined for single use, the interface can also have [output parameters](../../abap-glossary/abenoutput_parameter_glosry.md) or a [return value](../../abap-glossary/abenreturn_value_glosry.md). BAdI methods can define or propagate [exceptions](../../abap-glossary/abenexception_glosry.md), and their implementation can be made [optional](../abap-declarations/abapmethods_default.md).

**BAdI object**

Instance of a [BAdI](../../abap-glossary/abenbadi_glosry.md). BAdI objects are addressed exclusively using [BAdI reference variables](../../abap-glossary/abenbadi_reference_variable_glosry.md) in which a [BAdI reference](../../abap-glossary/abenbadi_reference_glosry.md) was set using [`GET BADI`](../abap-enhancements/abapget_badi.md). A BAdI object acts as a handle for the calls of [BAdI methods](../../abap-glossary/abenbadi_method_glosry.md) and contains references to the [object plug-ins](../../abap-glossary/abenobject_plugin_glosry.md) created based on filter specifications. From a technical point of view, BAdI objects are [instances](../../abap-glossary/abeninstance_glosry.md) of [BAdI classes](../../abap-glossary/abenbadi_class_glosry.md).

**BAdI reference**

Reference to a [BAdI object](../../abap-glossary/abenbadi_object_glosry.md). BAdI references occur only as content of [BAdI reference variables](../../abap-glossary/abenbadi_reference_variable_glosry.md). Technically, BAdI references are [object references](../../abap-glossary/abenobject_reference_glosry.md) to [instances](../../abap-glossary/abeninstance_glosry.md) of [BAdI classes](../../abap-glossary/abenbadi_class_glosry.md).

**BAdI reference variable**

Special [object reference variable](../../abap-glossary/abenobject_refer_variable_glosry.md) that is declared with reference to a [BAdI](../../abap-glossary/abenbadi_glosry.md) and is used to access the associated [BAdI object](../../abap-glossary/abenbadi_object_glosry.md). BAdI reference variables are supplied with a [BAdI reference](../../abap-glossary/abenbadi_reference_glosry.md) using [`GET BADI`](../abap-enhancements/abapget_badi.md) and are only used in [`CALL BADI`](../abap-enhancements/abapcall_badi.md) to call [BAdI methods](../../abap-glossary/abenbadi_method_glosry.md). Technically, BAdI reference variables are [class reference variables](../../abap-glossary/abenclass_reference_variabl_glosry.md) of the [static type](../../abap-glossary/abenstatic_type_glosry.md) of a concrete [BAdI](../../abap-glossary/abenbadi_class_glosry.md) class, or of its abstract superclass `CL_BADI_BASE`.

**BAPI**

*-\>* [Business Application Programming Interface](../../abap-glossary/abenbusiness_app_prog_inter_glosry.md)

**basXML**

Binary ABAP Serialization XML. Representation of [asXML](../../abap-glossary/abenasxml_glosry.md) in [Binary XML](../../abap-glossary/abenbinary_xml_glosry.md). basXML is used, among other things, as an RFC protocol with the same name.

**batch input**

Data transfer technique that allows data sets to be transferred automatically to the dynpros of transactions, and thus to [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). Batch input is controlled by batch input sessions. The processing of batch input sessions in batch input is partly implemented directly in the [ABAP kernel](../../abap-glossary/abenkernel_glosry.md). See also batch input tables.

**batch input session**

A summary of a series of transaction calls including input data and user actions. A batch input session can be used to execute dialog transactions in batch input, whereby some or all of the screens are handled by the session. Batch input sessions are stored persistently and are managed by the batch input administration in transaction `SM35`. See also batch input tables.

**bgPF**

*-\>* [Background Processing Framework](../../abap-glossary/abenbackround_processing_fw_glosry.md)

**bgRFC**

*-\>* Background Remote Function Call

**binary file**

File on the [host computer](../../abap-glossary/abenhost_computer_glosry.md) of an [AS instance](../../abap-glossary/abenas_instance_glosry.md) opened using the addition `BINARY` of the statement `OPEN DATASET`. The content of a binary file is read or written without being handled.

**binary XML**

SAP-specific format for the binary storage of [XML](../../abap-glossary/abenxml_glosry.md) data. In Binary XML, redundant information is suppressed, and [UTF-8](../../abap-glossary/abenutf8_glosry.md) encoding is used, which leads to performance benefits when storing and transporting data. In [AS ABAP](../../abap-glossary/abenas_abap_glosry.md), Binary XML occurs as one of the supported [formats](../abap-data-interchange-formats/abenabap_sxml_lib_formats.md) in the [sXML Library](../abap-data-interchange-formats/abenabap_sxml_lib.md).

**binary XML**

SAP-specific format for the binary storage of [XML](../../abap-glossary/abenxml_glosry.md) data. In Binary XML, redundant information is suppressed, and [UTF-8](../../abap-glossary/abenutf8_glosry.md) encoding is used, which leads to performance benefits when storing and transporting data. In [AS ABAP](../../abap-glossary/abenas_abap_glosry.md), Binary XML occurs as one of the supported [formats](../abap-data-interchange-formats/abenabap_sxml_lib_formats.md) in the [sXML Library](../abap-data-interchange-formats/abenabap_sxml_lib.md).

**BOPF**

*-\>* [Business Object Processing Framework](../../abap-glossary/abenbo_processing_fw_glosry.md)

**breakpoint**

Stopping point in an [ABAP program](../../abap-glossary/abenabap_program_glosry.md) that when it is reached in dialog processing, is branched into the [ABAP Debugger](../../abap-glossary/abenabap_debugger_glosry.md). Breakpoints with a limited lifespan and a validity related to the current [ABAP user](../../abap-glossary/abenabap_user_glosry.md) can be set interactively in the ABAP Editor or [ABAP Debugger](../../abap-glossary/abenabap_debugger_glosry.md). The statement `BREAK-POINT` can be used to create a breakpoint as an unconditional [checkpoint](../../abap-glossary/abencheckpoint_glosry.md) with an unlimited lifespan, which is either always active or can be [activated](../../abap-glossary/abenactivatable_checkpoint_glosry.md) by assignment to a [checkpoint group](../../abap-glossary/abencheckpoint_group_glosry.md)..

**BSP**

*-\>* Business Server Pages

**Business Add-In**

*-\>* [BAdI](../../abap-glossary/abenbadi_glosry.md)

**Business Application Programming Interface**

BAPI for short. A predefined interface to data and processes of an SAP application that is stored in the business object repository with the basic functions *Create Objects*, *Query Object Properties*, and *Change Object Properties*. BAPIs are implemented using remotely called [function modules](../../abap-glossary/abenfunction_module_glosry.md) with the naming convention `BAPI_business_object_name_method_name` that are not allowed to lead a user dialog.

The BAPI Explorer that lists the function modules for each application is called using the transaction code BAPI.

**Business Function**

`BF` for short. [Repository object](../../abap-glossary/abenrepository_object_glosry.md) that represents a self-contained (business) function within the scope of the [Switch Framework](../../abap-glossary/abenswitch_framework_glosry.md). Multiple business functions are grouped into a Business Function Set. Technically, a business function is a grouping of [switches](../../abap-glossary/abenswitch_glosry.md) that serve the same function. When a business function is activated, the corresponding switches are activated as well. Business functions are created in transaction `SFW2` and switched in transaction `SFW5`.

**Business Function Set**

BFS for short. [Repository object](../../abap-glossary/abenrepository_object_glosry.md) that groups multiple business functions to form a unit that covers the requirements of an industry solution within the scope of [Switch Framework](../../abap-glossary/abenswitch_framework_glosry.md). For each [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) only one business function set can be activated. Within a business function set, it is ensured that all business functions are compatible with one another. Business function sets are created in transaction `SFW3` and switched in transaction `SFW5`.

**Business Object Processing Framework**

[BOPF](../../abap-glossary/abenbopf_glosry.md) for short. An ABAP-based framework that provides a set of generic services and functionalities to create [business objects](../../abap-glossary/abenbusiness_object_glosry.md) (BOs), such as [CDS-based BOPF BOs](../../abap-glossary/abencds_bopf_bo_glosry.md).

**Business Server Pages**

User interface of an Internet application of the [Application Server ABAP](../../abap-glossary/abenas_abap_glosry.md) encoded in HTML. Business Server Pages can include server-side scripts that are written in ABAP. When a script of this type is compiled, a [class](../../abap-glossary/abenclass_glosry.md) is generated in [ABAP Objects](../../abap-glossary/abenabap_objects_glosry.md) whose [methods](../../abap-glossary/abenmethod_glosry.md) implement the functions of the script. This means that all language tools available in ABAP Objects can also be used in Business Server Pages and particularly that the [database](../../abap-glossary/abendatabase_glosry.md) can be accessed using the [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md). Business Server Pages are created using Web Application Builder.

**business service**

BS for short. A business service makes [repository objects](../../abap-glossary/abenrepository_object_glosry.md) from [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) available for consumption outside of AS ABAP. A business service is based on a [CDS service definition](../../abap-glossary/abencds_service_definition_glosry.md) and a [service binding](../../abap-glossary/abenservice_binding_glosry.md). Different communication protocols are available, such as OData, the [Information Access protocol](../../abap-glossary/abenina_protocol_glosry.md), and [SQL services](../../abap-glossary/abenabap_sql_services_glosry.md). In the context of the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md), a business service is a [RESTful](../../abap-glossary/abenrestful_glosry.md) service which can be called by a consumer. See [RAP business service](../../abap-glossary/abenbusiness_service_glosry.md).

**C0 contract, extend**

[Release contract](../../abap-glossary/abenrelease_contract_glosry.md) that ensures stability at dedicated extension points to allow for a certain extensibility of repository objects by using enhancement tools.

More information:

- [ABAP - Release Contracts](../../abap-apis/release-contracts/abenabap_release_contracts.md)

- [Contract Checks for Released APIs](../../abap-apis/release-contracts/abenrestricted_apis_atc_checks.md)

**C1 contract, use system-internally**

[Release contract](../../abap-glossary/abenrelease_contract_glosry.md) that ensures a stable public interface of [released APIs](../../abap-glossary/abenreleased_api_glosry.md) for system-internal use.

**C2 contract, use as remote API**

[Release contract](../../abap-glossary/abenrelease_contract_glosry.md) that ensures a stable public interface for use as remote API for external consumption.

**C3 contract, manage configuration content**

[Release contract](../../abap-glossary/abenrelease_contract_glosry.md) that ensures a stable persistence of configuration content that can be used by dedicated APIs.

**C4 contract, use in ABAP-Managed Database Procedures**

[Release contract](../../abap-glossary/abenrelease_contract_glosry.md) that ensures a stable public interface of [released APIs](../../abap-glossary/abenreleased_api_glosry.md) for use in [ABAP Managed Database Procedures](../../abap-glossary/abenabap_managed_db_proc_glosry.md) (AMDP).

**canonical JSON representation**

Format of [JSON](../../abap-glossary/abenjson_glosry.md) data that is created during the [serialization](../../abap-glossary/abenserialization_glosry.md) of ABAP data by the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) and that is a prerequisite for a [deserialization](../../abap-glossary/abendeserialization_glosry.md) using identity transformations. The short name is [asJSON](../../abap-glossary/abenasjson_glosry.md).

**canonical XML representation**

Format of [XML](../../abap-glossary/abenxml_glosry.md) data that is created during the [serialization](../../abap-glossary/abenserialization_glosry.md) of ABAP data with the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) and that is a prerequisite for a [deserialization](../../abap-glossary/abendeserialization_glosry.md) using identity transformations and is used as an intermediate format when using [XSLT](../../abap-glossary/abenxslt_glosry.md) to access ABAP data. The short name is [asXML](../../abap-glossary/abenasxml_glosry.md); see also [basXML](../../abap-glossary/abenbasxml_glosry.md)

**CDS-Based Enterprise Search**

The ABAP-CDS-specific version of the [SAP Enterprise Search](../../abap-glossary/abensap_enterprisesearch_glosry.md) technology. It is based on [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) in the backend. These view entities are annotated with [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) from the [`EnterpriseSearch`](../../abap-core-data-services-abap-cds/abap-cds-annotations/abencds_enterprisesearch_f.md) domain. The annotations define search capabilities and they also trigger the generation of a [CDS-based search connector](../../abap-glossary/abencds_search_connector_glosry.md). CDS-based enterprise search provides enhanced search capabilities in SAP Fiori launchpad.

**Change and Transport System**

Abbreviated to CTS. The Change and Transport System includes all [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) tools used to manage and transport [repository objects](../../abap-glossary/abenrepository_object_glosry.md) and other objects between different [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) systems. A repository object is connected to CTS using its [package](../../abap-glossary/abenpackage_glosry.md).

**change lock**

Area lock on an area instance version in the shared objects memory. A change lock is either a write lock or an update lock.

**check indicator**

Indicates whether an [authorization object](../../abap-glossary/abenauthorization_object_glosry.md) is checked by [authorization check](../../abap-glossary/abenauthorization_check_glosry.md) in a certain context, for example a transaction. Check indicators for authorization objects are defined at SAP by the transaction `SU22` and in customer systems by the transaction `SU24`. Check indicators can have the statuses *check* and *do not check*, where *check* is given a proposal status with the values *empty* (not yet set), *yes*, and *no*. The changes made in transaction `SU22` have the role of proposal values in customer systems and can be passed to transaction `SU24` with transaction `SU25`.

**Class Builder**

Tool in ABAP Workbench for used for creating and maintaining global [classes](../../abap-glossary/abenclass_glosry.md). Called using transaction `SE24`.

**class library**

The class library consists of all [global](../../abap-glossary/abenglobal_type_glosry.md) [object types](../../abap-glossary/abenobject_type_glosry.md), namely of all [global classes](../../abap-glossary/abenglobal_class_glosry.md) and [interfaces](../../abap-glossary/abenglobal_interface_glosry.md).

**classic ABAP**

ABAP development model for legacy solutions. Classic ABAP is based on the [ABAP technology](../../abap-glossary/abenabap_techno_glosry.md) without restrictions regarding [ABAP language versions](../../abap-glossary/abenabap_version_glosry.md), usage of tools or access to [repository objects](../../abap-glossary/abenrepository_object_glosry.md). Classic ABAP is still supported by the [ABAP Platform](../../abap-glossary/abenabap_platform_glosry.md) of [SAP S/4HANA](../../abap-glossary/abensap_s4hana_glosry.md). See also [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md).

**classified API**

An API (for example, methods of classes and interfaces, and function modules) with special classifications. These classifications are typically included as type definitions, start with `IF_ABAP_TX_...` and define specific [transactional contracts](../../abap-glossary/abentransactional_contract_glosry.md). In the context of the [controlled SAP LUW](../../abap-glossary/abencontrolled_sap_luw_glosry.md), the classifications are used to specify that the functionality encapsulated by the API is only used in [transactional phases](../../abap-glossary/abentr_phase_glosry.md) where allowed.

**client**

Organizational unit of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). For each [logon](../../abap-glossary/abenlogon_glosry.md) to AS ABAP, a [client ID](../../abap-glossary/abenclient_identifier_glosry.md) must be specified. This ID enables a logon to a specific client. The different clients of an AS ABAP have their own [user master records](../../abap-glossary/abenuser_master_record_glosry.md) with specific [authorizations](../../abap-glossary/abenauthorization_glosry.md). [Client-dependent](../../abap-glossary/abenclient_dependent_glosry.md) data is kept separate using the [client column](../../abap-glossary/abenclient_column_glosry.md) in [application tables](../../abap-glossary/abenapplication_table_glosry.md). [Application programs](../../abap-glossary/abenapplication_program_glosry.md) are generally executed in [application clients](../../abap-glossary/abenapplication_client_glosry.md). There is also a system client for carrying out system-specific or administrative tasks.

**client ID**

Three-digit ID of a [client](../../abap-glossary/abenclient_glosry.md) that specifies the [current client](../../abap-glossary/abencurrent_client_glosry.md) when [logging on](../../abap-glossary/abenlogon_glosry.md) to [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). In [application tables](../../abap-glossary/abenapplication_table_glosry.md), [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md) data is indicated by the client ID stored in the [client column](../../abap-glossary/abenclient_column_glosry.md).

**Code Inspector**

CI for short. Tool for checking [repository objects](../../abap-glossary/abenrepository_object_glosry.md) in terms of performance, security, syntax, and adherence to naming conventions. Called using transaction code `SCI`.

[***-\>* More about**](https://help.sap.com/docs/ABAP_PLATFORM_NEW/ba879a6e2ea04d9bb94c7ccd7cdac446/49205531d0fc14cfe10000000a42189b)

**composite enhancement implementation**

Semantic combination of ([simple](../../abap-glossary/abensimple_enhancement_impl_glosry.md) or other composite) [enhancement implementations](../../abap-glossary/abenenhancement_impl_glosry.md) with the aim of providing structure.

**composite enhancement spot**

Semantic combination of [simple](../../abap-glossary/abensimple_enhancement_spot_glosry.md) and other composite [enhancement spots](../../abap-glossary/abenenhancement_spot_glosry.md) with the aim of providing structure.

**conflict resolution**

Term in [Switch Framework](../../abap-glossary/abenswitch_framework_glosry.md). A conflict occurs if multiple [enhancement implementation elements](../../abap-glossary/abenenhancement_impl_elem_glosry.md) exist for a single [enhancement option](../../abap-glossary/abenenhancement_point_glosry.md) for which only one enhancement can be carried out, and when more than one of these enhancement implementation elements are switched on at the same time. Currently, a conflict can occur with the statements `ENHANCEMENT-SECTION` and [`GET BADI`](../abap-enhancements/abapget_badi.md). To resolve the conflict, the [conflict resolving enhancement implementation](../../abap-glossary/abenconflict_resol_impl_glosry.md) with the highest priority is searched among the [enhancement implementations](../../abap-glossary/abenenhancement_impl_glosry.md) and its enhancement implementation element is then used.

**conflict resolving enhancement implementation**

An [enhancement implementation](../../abap-glossary/abenenhancement_impl_glosry.md) to which a [conflict switch](../../abap-glossary/abenconflict_switch_glosry.md) is assigned instead of a regular [switch](../../abap-glossary/abenswitch_glosry.md). A conflict resolving enhancement implementation is used for [conflict resolution](../../abap-glossary/abenconflict_resolution_glosry.md). It must mirror the common semantics of all regular enhancement implementations that can potentially be switched on at the same time and which then show conflicts. These enhancement implementations can be determined by assigning switches to the conflict switch. During conflict resolution, a conflict resolving enhancement implementation has priority over regular enhancements. In the event of multiple conflict resolving enhancement implementations exist, the one that resolves the most conflicts takes priority.

**conflict switch**

A special [switch](../../abap-glossary/abenswitch_glosry.md) for [conflict resolution](../../abap-glossary/abenconflict_resolution_glosry.md). Multiple regular switches are assigned to a conflict switch. The switch status of a conflict switch is determined by the switch status of the assigned switches: *on* if all assigned switches are *on*, *off* if at least one assigned switch is *off*, and *standby* in all remaining cases. For every combination of [enhancement implementation](../../abap-glossary/abenenhancement_impl_glosry.md) to which the regular switches of the conflict switch are assigned, a [conflict resolving enhancement implementation](../../abap-glossary/abenconflict_resol_impl_glosry.md) must be created to which the conflict switch is assigned.

**Context Builder**

Tool in the ABAP Workbench for editing contexts. Called using transaction `SE33`.

**controlled SAP LUW**

An extension of the [SAP LUW](../../abap-glossary/abensap_luw_glosry.md) concept. The controlled SAP LUW introduces a checking mechanism to detect transactional consistency violations. The controlled SAP LUW is automatically and implicitly supported by newer ABAP concepts such as [RAP](../../abap-glossary/abenrap_glosry.md). In non-RAP transactions, the controlled SAP LUW can be used by explicitly setting transactional phases using the static methods of the [`CL_ABAP_TX`](../abap-database-access/abaprap_cl_abap_tx.md) class. In addition, [released APIs](../../abap-glossary/abenreleased_api_glosry.md) can have special classifications (starting with [`IF_ABAP_TX...`](../abap-database-access/abapapi_classification.md)) that enable specific transactional contracts that are checked in the [transactional phases](../../abap-glossary/abentr_phase_glosry.md).

**Coverage Analyzer**

Tool for recording how often programs or individual [processing blocks](../../abap-glossary/abenprocessing_block_glosry.md) are executed, classified by time period, [ABAP user](../../abap-glossary/abenabap_user_glosry.md), or subject area. It is called using transaction code `SCOV`.

**cross-transaction application buffer**

Application buffer in the [shared memory](../../abap-glossary/abenshared_memory_glosry.md). ABAP programs access cross-transaction application buffers by specifying [`SHARED BUFFER`](../abap-data-cluster/abapexport_data_cluster_medium.md) or [`SHARED MEMORY`](../abap-data-cluster/abapexport_data_cluster_medium.md) as the medium with the statements [`EXPORT`](../abap-data-cluster/abapexport_data_cluster.md) and [`IMPORT`](../abap-data-cluster/abapimport_data_cluster.md) for [data clusters](../../abap-glossary/abendata_cluster_glosry.md). The difference between the two types lies in the system behavior when the memory limit is reached.

**current client**

The current client of a [user session](../../abap-glossary/abenuser_session_glosry.md) is the [client](../../abap-glossary/abenclient_glosry.md) whose [client ID](../../abap-glossary/abenclient_identifier_glosry.md) was specified during [logon](../../abap-glossary/abenlogon_glosry.md).

**customer exit**

Option provided by SAP for the enhancement of delivered standard programs without modification of the original program in a customer system. For potential customer requirements that are not part of the standard, SAP provides blank containers, which customers can fill with their own functions. Customer exits are managed by SAP in transaction `SMOD`. In transaction `CMOD`, the customers select the enhancement that they want to process, groups them together as enhancement projects, processes the components, and activates the relevant projects. Customer exits are obsolete and have been replaced by [BAdIs](../../abap-glossary/abenbadi_glosry.md) and other [enhancement points](../../abap-glossary/abenenhancement_point_glosry.md).

**customer namespace**

Predefined [namespace](../../abap-glossary/abennamespace_glosry.md) for [repository objects](../../abap-glossary/abenrepository_object_glosry.md) created in non-SAP and non-partner development systems. Names have `Y` or `Z` as the first character. These names have to be used in non-SAP and non-partner systems, if no [prefix namespace](../../abap-glossary/abenprefix_name_space_glosry.md) is available.

**data aging**

A [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) concept where current data is distinguished from outdated data by entries in a [temperature column](../../abap-glossary/abentemperature_column_glosry.md). Only current data exists in the memory.

**data area**

Memory area of an [ABAP program](../../abap-glossary/abenabap_program_glosry.md) in which data is stored. The data area covers a static area for [data objects](../../abap-glossary/abendata_object_glosry.md) of fixed length and a dynamic area for data objects of variable length ([data types](../../abap-glossary/abendata_type_glosry.md) [`string`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md), [`xstring`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md), and [internal tables](../../abap-glossary/abeninternal_table_glosry.md)). The internal [references](../../abap-glossary/abenreference_glosry.md) to the dynamic area are in the static area.

**Data Browser**

Tool of the ABAP Workbench for accessing the content of [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md). Called using transaction `SE16`.

**database**

System for storing and managing data between which logical dependencies exist. The data in the database of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) is stored on the [database server](../../abap-glossary/abendatabase_server_glosry.md) and is managed by the [database system](../../abap-glossary/abendatabase_system_glosry.md). See also [relational database](../../abap-glossary/abenrelational_database_glosry.md).

**database commit**

End of a [database LUW](../../abap-glossary/abendatabase_luw_glosry.md), in which changed data records are written to the [database](../../abap-glossary/abendatabase_glosry.md). All changes are temporary until they have been written using a database commit. Changes are always directly visible to the executing program. The [database system](../../abap-glossary/abendatabase_system_glosry.md) that is used determines whether other users can see the database changes immediately or only after the database commit. In [AS ABAP](../../abap-glossary/abenas_abap_glosry.md), database commits are triggered implicitly, as well as by explicit requests.

**database connection**

Connection of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) to a [database system](../../abap-glossary/abendatabase_system_glosry.md). A database connection defines the address of the database system, the [database user](../../abap-glossary/abendatabase_user_glosry.md), and therefore the [database schema](../../abap-glossary/abendatabase_schema_glosry.md) assigned to it. By default, the [database interface](../../abap-glossary/abendatabase_interface_glosry.md) accesses the [standard AS ABAP database](../../abap-glossary/abenstandard_db_glosry.md) using the [standard connection](../../abap-glossary/abenstandard_db_connection_glosry.md) of the current [work process](../../abap-glossary/abenwork_process_glosry.md). Optionally, database accesses can also be performed using [service connections](../../abap-glossary/abenservice_connection_glosry.md) to the standard database. Up to 16 database connections can be opened for a single work process.

**database function**

[SQLScript function](../../abap-glossary/abensql_script_function_glosry.md) in the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md). Database functions must have a return value defined with `RETURN`. There are [table functions](../../abap-glossary/abentable_function_glosry.md) with a tabular return value and [scalar functions](../../abap-glossary/abenscalar_function_glosry.md) with a scalar return value. Unlike [database procedures](../../abap-glossary/abendatabase_procedure_glosry.md), database functions cannot be called using `CALL`, but can be used directly in read positions of statements. Database functions can be managed as [AMDP functions](../../abap-glossary/abenamdp_function_glosry.md) in the [ABAP Managed Database Procedures](../../abap-glossary/abenabap_managed_db_proc_glosry.md) (AMDP).

**database interface**

[Interface](../../abap-glossary/abenintf_gen_glosry.md) of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) to its [database](../../abap-glossary/abendatabase_glosry.md) that is integrated into the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md). Statements in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and Native SQL access the database using the database interface. The database interface is divided into an [ABAP SQL interface](../../abap-glossary/abenabap_sql_interface_glosry.md) and a Native SQL interface. In addition, classic dynpros also access the database using the database interface. The database interface is responsible for data transport between the AS ABAP and the [database system](../../abap-glossary/abendatabase_system_glosry.md), implicit [client handling](../../abap-glossary/abenclient_handling_glosry.md), and [table buffering](../../abap-glossary/abentable_buffering_glosry.md). The database interface can also be involved in maintaining [ABAP-managed database objects](../../abap-glossary/abenabap_managed_db_object_glosry.md).

**database layer**

Software layer of a [client-server system](../../abap-glossary/abenclient_server_system_glosry.md) in which [persistent data](../../abap-glossary/abenrap_persistent_data_glosry.md) is stored and managed. The [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) of an [ABAP system](../../abap-glossary/abenabap_system_glosry.md) is always connected to a database layer in the form of a [database server](../../abap-glossary/abendatabase_server_glosry.md) that contains a [database system](../../abap-glossary/abendatabase_system_glosry.md) with the [standard AS ABAP database](../../abap-glossary/abenstandard_db_glosry.md).

**database lock**

Physical [locks](../../abap-glossary/abenlock_glosry.md) for rows in [database tables](../../abap-glossary/abendatabase_table_glosry.md), imposed by the [database system](../../abap-glossary/abendatabase_system_glosry.md). A database lock persists until the end of the current [database LUW](../../abap-glossary/abendatabase_luw_glosry.md).

**database LUW**

Also referred to as database transaction. Indivisible sequence of database operations concluded by a [database commit](../../abap-glossary/abendatabase_commit_glosry.md). The database LUW is either executed completely or not at all by the [database system](../../abap-glossary/abendatabase_system_glosry.md). If an error is detected within a database LUW, all database changes made since the start of the database LUW can be canceled using a [database rollback](../../abap-glossary/abendatabase_rollback_glosry.md).

**database object**

Object saved in a [database](../../abap-glossary/abendatabase_glosry.md), such as a [database table](../../abap-glossary/abendatabase_table_glosry.md), an [SQL view](../../abap-glossary/abensql_view_glosry.md), or a [stored procedure](../../abap-glossary/abenstored_procedure_glosry.md). [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) mainly uses [ABAP-managed database objects](../../abap-glossary/abenabap_managed_db_object_glosry.md).

**database procedure**

General synonym for [stored procedure](../../abap-glossary/abenstored_procedure_glosry.md). In [SAP HANA databases](../../abap-glossary/abenhana_database_glosry.md) it is a name for an [SQLScript procedure](../../abap-glossary/abensql_script_procedure_glosry.md) programmed in [SQLScript](../../abap-glossary/abensql_script_glosry.md) or an L procedure programmed in L. Database procedures can be managed as [AMDP procedures](../../abap-glossary/abenamdp_procedure_glosry.md) in the [ABAP Managed Database Procedures](../../abap-glossary/abenabap_managed_db_proc_glosry.md) (AMDP). See also [database function](../../abap-glossary/abendatabase_function_glosry.md).

**database procedure interface**

Global non-modifiable [interface](../../abap-glossary/abenintf_gen_glosry.md) of the [class library](../../abap-glossary/abenclass_library_glosry.md) that is generated for each database procedure proxy. For each interface parameter of the represented [SQLScript procedure](../../abap-glossary/abensql_script_procedure_glosry.md), a database procedure interface contains the declaration of an [ABAP data type](../../abap-glossary/abendata_type_glosry.md), as defined in the mapping of the database procedure proxy. Programs that use `CALL DATABASE PROCEDURE` to call the SQLScript procedure can refer to the data types of the database procedure interface when declaring the required actual parameters.

**database rollback**

End of a [database LUW](../../abap-glossary/abendatabase_luw_glosry.md) in which all modifying database operations are undone until the beginning of the LUW. In an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md), database rollbacks are triggered implicitly, as well as by explicit requests.

**database schema**

A database schema groups [database objects](../../abap-glossary/abendb_object_glosry.md) in a [database](../../abap-glossary/abendatabase_glosry.md). Within a database schema, [SQL](../../abap-glossary/abensql_glosry.md) can be used to access the objects of the same schema directly. [Database users](../../abap-glossary/abendatabase_user_glosry.md) implicitly access the database schema assigned to their [database user names](../../abap-glossary/abendatabase_user_name_glosry.md). Objects in a different schema can be accessed only by specifying their schema name. Access to a database schema by a database user is regulated by individual authorizations. The objects managed by the [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md) for a database and the implementations of [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md) are located in the [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md) that is assigned the database user name when the [standard connection](../../abap-glossary/abenstandard_db_connection_glosry.md) in [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) is accessed.

**database transaction**

*-\>* [database LUW](../../abap-glossary/abendatabase_luw_glosry.md)

**DBA Cockpit**

Central tool for managing and monitoring [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) [database connections](../../abap-glossary/abendatabase_connection_glosry.md). Called using the transaction code `DBACOCKPIT`.

**DDL object**

A [database](../../abap-glossary/abendatabase_glosry.md) artifact that is not managed by the [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md). It can be used in the context of [AMDP](../../abap-glossary/abenamdp_glosry.md). Currently, the following DDL objects can be used with AMDP:

- [Views](../../abap-glossary/abenview_glosry.md)

- L libraries

- [Graph workspaces](../../abap-glossary/abengraph_workspace_glosry.md)

DDL objects can be consumed by other [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md).

**deserialization**

Transformation of [XML](../../abap-glossary/abenxml_glosry.md) data or [JSON](../../abap-glossary/abenjson_glosry.md) data to ABAP data objects. Performed either by calling an [XSLT program](../../abap-glossary/abenxsl_transformation_glosry.md) or a [Simple Transformation](../../abap-glossary/abensimple_transformation_glosry.md). If use [XSLT](../../abap-glossary/abenxslt_glosry.md) is used, the result of the transformation (in XML) must be a [canonical XML representation](../../abap-glossary/abencanonical_xml_represent_glosry.md) (([asXML](../../abap-glossary/abenasxml_glosry.md)).

**developer extensibility**

An extensibility approach that allows ABAP developers to create upgrade-stable custom ABAP code in cloud and on-premise environments. It delivers flexibility beyond key user extensibility and can be done directly on the software stack using the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md) (ADT) via local [released APIs](../../abap-glossary/abenreleased_api_glosry.md).

One use case for developer extensibility is [RAP extensibility](../../abap-glossary/abenrap_extensibility_glosry.md). Using [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md), a RAP application can be extended from the database to the service definition directly in ADT with custom ABAP code.

**developer trace**

Trace files on the [host computers](../../abap-glossary/abenhost_computer_glosry.md) of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) that contain technical information for use in the event of an error.

**development object**

[*-\>* Repository object](../../abap-glossary/abenrepository_object_glosry.md)

**DOM**

Short for Document Object Model. Interface for accessing [XML](../../abap-glossary/abenxml_glosry.md) documents that are based on an object-oriented tree-like representation of the documents in the memory, where each node is represented by an object. In ABAP, the [iXML Library](../abap-data-interchange-formats/abenabap_ixml_lib_cloud.md) can be used to process XML documents in DOM representation.

**elementary operand**

An [operand](../../abap-glossary/abenoperand_glosry.md) that is not an [expression](../../abap-glossary/abenexp_glosry.md). The value of a elementary operand can be used directly and must not be evaluated.

**embedded Steampunk**

Internal SAP project name for [SAP S/4HANA Cloud ABAP environment](../../abap-glossary/abens4_hana_cloud_abap_env_glosry.md). See also [Steampunk](../../abap-glossary/abensteampunk_glosry.md).

**enhancement**

Addition to a [repository object](../../abap-glossary/abenrepository_object_glosry.md) that is managed by the ABAP Enhancement Framework and changes its behavior without modification. An enhancement can be made by creating [enhancement implementation elements](../../abap-glossary/abenenhancement_impl_elem_glosry.md) for explicitly defined or implicitly available [enhancement options](../../abap-glossary/abenenhancement_point_glosry.md). Enhancements are switchable using the [Switch Framework](../../abap-glossary/abenswitch_framework_glosry.md).

**Enhancement Builder**

Tool in the ABAP Workbench for creating and administering [enhancements](../../abap-glossary/abenenhancement_glosry.md) within the enhancement framework.

**enhancement concept**

Concept for enhancing [repository objects](../../abap-glossary/abenrepository_object_glosry.md) without modifying them. Implemented by the ABAP Enhancement Framework

**enhancement implementation**

A [repository object](../../abap-glossary/abenrepository_object_glosry.md) used for the administration of [enhancements](../../abap-glossary/abenenhancement_glosry.md) of other repository objects. Enhancement implementations are components of a hierarchical tree structure of which the branches represent [composite](../../abap-glossary/abencomp_enhancement_impl_glosry.md) enhancement implementations, and the leaves are [simple enhancement implementations](../../abap-glossary/abensimple_enhancement_impl_glosry.md).

**enhancement implementation element**

Individual element of an [enhancement implementation](../../abap-glossary/abenenhancement_impl_glosry.md). One enhancement implementation can contain multiple enhancement implementation elements, for example, different source code plug-ins.

**Enhancement Information System**

Tool of the ABAP Workbench for the search for [enhancements](../../abap-glossary/abenenhancement_glosry.md) made with the ABAP Enhancement Framework. Called in the Object Navigator or via transaction code `SPAU_ENH`.

**enhancement option**

Position in a [repository object](../../abap-glossary/abenrepository_object_glosry.md) that can be enhanced with the ABAP Enhancement Framework. Enhancement options can be explicitly defined or available implicitly. Explicitly defined enhancement options are implemented using [enhancement spot element definitions](../../abap-glossary/abenenhancement_spot_def_glosry.md) and [enhancement spot invocations](../../abap-glossary/abenenhancement_spot_invoc_glosry.md) and are administrated using [enhancement spots](../../abap-glossary/abenenhancement_spot_glosry.md).

**enhancement spot**

A [repository object](../../abap-glossary/abenrepository_object_glosry.md) used for the administration of explicitly created [enhancement options](../../abap-glossary/abenenhancement_point_glosry.md). Enhancement spots are components of a tree structure hierarchy, whose branches represent [composite](../../abap-glossary/abencomp_enhancement_spot_glosry.md) enhancement spots and whose leaves are [simple enhancement spots](../../abap-glossary/abensimple_enhancement_spot_glosry.md). Enhancement points that are available implicitly do not have enhancement spots.

**enhancement spot element definition**

Part of the definition of an explicit [enhancement option](../../abap-glossary/abenenhancement_point_glosry.md). An enhancement spot element definition must be assigned to at least one [enhancement spot](../../abap-glossary/abenenhancement_spot_glosry.md).

**enhancement spot element invocation**

Part of the definition of an explicit [enhancement option](../../abap-glossary/abenenhancement_point_glosry.md); the calling position of an [enhancement spot element definition](../../abap-glossary/abenenhancement_spot_def_glosry.md). An enhancement spot element definition can be called at multiple positions besides source code enhancements.

**environment code page**

The active [system code page](../../abap-glossary/abensystem_codepage_glosry.md) of an [internal session](../../abap-glossary/abeninternal_session_glosry.md). The current release only supports [Unicode systems](../../abap-glossary/abenunicode_system_glosry.md) and the environment codepage is always [UTF-16](../../abap-glossary/abenutf16_glosry.md).

**EPP component ID**

Component of an extended passport (EPP). Contains the [system ID](../../abap-glossary/abensystem_id_glosry.md) and the name of the [application server instance](../../abap-glossary/abenas_instance_glosry.md) of the original [ABAP session](../../abap-glossary/abenabap_session_glosry.md).

**EPP connection counter**

Component of an extended passport (EPP). Counts connections between clients and servers with the same EPP connection ID.

**EPP connection ID**

Component of an extended passport (EPP). ID of a connection that is created by calls from [ABAP sessions](../../abap-glossary/abenabap_session_glosry.md) or external connections in ABAP sessions.

**EPP precomponent ID**

Component of an extended passport (EPP). Contains the [system ID](../../abap-glossary/abensystem_id_glosry.md) and the name of the [application server instance](../../abap-glossary/abenas_instance_glosry.md) of the [ABAP session](../../abap-glossary/abenabap_session_glosry.md) on which the current connection is based.

**EPP root context ID**

Component of an extended passport (EPP). ID of the original [ABAP session](../../abap-glossary/abenabap_session_glosry.md).

**EPP transaction ID**

Component of an extended passport (EPP). ID of the current [SAP-LUW](../../abap-glossary/abensap_luw_glosry.md).

**exclusive lock**

[Lock](../../abap-glossary/abenlock_glosry.md) that does not allow other users to set simultaneous locks for the exclusively locked data. The [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statements [`INSERT`](../abap-database-access/abapinsert_dbtab.md), [`DELETE`](../abap-database-access/abapdelete_dbtab.md), [`MODIFY`](../abap-database-access/abapmodify_dbtab.md), and [`UPDATE`](../abap-database-access/abapupdate.md), [`SELECT`](../abap-database-access/abapselect.md) with the addition [`FOR UPDATE`](../abap-database-access/abapselect_single.md), and all corresponding Native SQL statements or statements in [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md) set corresponding [database locks](../../abap-glossary/abendatabase_lock_glosry.md) on the rows they address. An exclusive lock is set as an SAP lock by calling a lock function module with the appropriate parameters.

**exit message**

[Message](../../abap-glossary/abenmessage_glosry.md) of the [message type](../../abap-glossary/abenmessage_type_glosry.md) *X*. Exit messages create a [database rollback](../../abap-glossary/abendatabase_rollback_glosry.md) and terminate the running program with the [runtime error](../../abap-glossary/abenruntime_error_glosry.md) `MESSAGE_TYPE_X`. The short text of the message can be found in the [short dump](../../abap-glossary/abenshort_dump_glosry.md).

**extended passport**

EPP for short. Internal data structure that exists for each [ABAP session](../../abap-glossary/abenabap_session_glosry.md) and contains information about this session and its external connections.

**extended program check**

Complete check of the [ABAP source code](../../abap-glossary/abenabap_source_code_glosry.md) for all statically recognizable errors. Programs with errors in the extended program check can be executed, but usually result in an [exception](../../abap-glossary/abenexception_glosry.md). Called in the ABAP Editor via *Program -\> Check -\> Extended Program Check* or via the transaction code `SLIN` or using the [ABAP Test Cockpit](../../abap-glossary/abenabap_test_cockpit_glosry.md). Settings for the extended program check can be made in the administration transaction `SLIN_ADMIN`.

[***-\>* More about**](https://help.sap.com/docs/ABAP_PLATFORM_NEW/bd833c8355f34e96a6e83096b38bf192/d1801afd454211d189710000e8322d00)

**fast data access**

FDA for short. Protocol that allows the content of [internal tables](../../abap-glossary/abeninternal_table_glosry.md) to be passed between the [Application Server ABAP](../../abap-glossary/abenas_abap_glosry.md) and a [database system](../../abap-glossary/abendatabase_system_glosry.md). FDA is supported by the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) and some other platforms. FDA can be switched on and off with database parameters and [database hints](../../abap-glossary/abendatabase_hint_glosry.md). FDA write access is the prerequisite for [`SELECT, FROM @itab`](../abap-database-access/abapselect_itab.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md). Depending on settings, FDA is also used for [`SELECT, FOR ALL ENTRIES`](../abap-database-access/abenwhere_all_entries.md).

**field exit**

Obsolete customer exit that can be linked with [DDIC data elements](../../abap-glossary/abendata_element_glosry.md) in the [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md) in customer systems. If a dynpro field is defined with reference to such a data element, a function module named `FIELD_EXIT_dtel` is called during the data transport from the dynpro to the ABAP program at the event PAI. Here, `dtel` is the name of the data element. The value of the dynpro field can be modified in the function module. The function module of a field exit cannot be debugged at present.

**file**

Storage of data under a name in a persistent storage medium. Statements of the ABAP file interface can be used to process files on the [host computer](../../abap-glossary/abenhost_computer_glosry.md) of an [AS instance](../../abap-glossary/abenas_instance_glosry.md). For files on the presentation servers, [function modules](../../abap-glossary/abenfunction_module_glosry.md) or [methods](../../abap-glossary/abenmethod_glosry.md) of a global [class](../../abap-glossary/abenclass_glosry.md) are available. The files of the [database server](../../abap-glossary/abendatabase_server_glosry.md) are part of the [database](../../abap-glossary/abendatabase_glosry.md) and are maintained by the [database system](../../abap-glossary/abendatabase_system_glosry.md).

**format setting**

Part of the [language environment](../../abap-glossary/abenlanguage_environment_glosry.md) where the formatting for numbers, dates, and times is defined. Defined either by defaults in the [user master record](../../abap-glossary/abenuser_master_record_glosry.md) or by [country-specific formats](../abap-language-environment/abencountry_formats.md).

**full text index**

Specific [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md) of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) for text searches. Not supported by [SAP HANA Cloud database](../../abap-glossary/abensap_hana_cloud_db_glosry.md).

**Function Builder**

ABAP Workbench tool for creating and maintaining [function modules](../../abap-glossary/abenfunction_module_glosry.md). Called using transaction `SE37`.

**fuzzy search index**

[Index](../../abap-glossary/abenindex_glosry.md) of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) that database that provides fast error-tolerant text search, where a query returns records even when the search term contains additional or missing characters or other types of spelling errors. The [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md) allows fuzzy search indexes to be created for [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md).

**garbage collector**

Deletes [objects](../../abap-glossary/abenobject_glosry.md) that are no longer referenced by [heap references](../../abap-glossary/abenheap_reference_glosry.md) or [field symbols](../../abap-glossary/abenfield_symbol_glosry.md) and for which no method is registered as an [event handler](../../abap-glossary/abenevent_handler_glosry.md). The garbage collector is called periodically by the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md). It tracks the [reference variables](../../abap-glossary/abenreference_variable_glosry.md) of deleted objects.

## The following can be used to call the garbage collector explicitly:

- Static method `COLLECT` of system class `CL_ABAP_GARBAGE_COLLECTOR`

It is generally unnecessary to trigger clearing explicitly. However, it can be beneficial in exceptional cases, such as when very large, unneeded objects consume a significant amount of memory, or when explicitly releasing memory in resource-constrained environments is required. It can also aid in analyzing memory consumption and ensuring proper memory release, or when large objects are created repeatedly in a short period.

**HDI**

SAP HANA Deployment Infrastructure Framework for deploying HDI objects.

**HDI container**

An HDI container is a [database schema](../../abap-glossary/abendatabase_schema_glosry.md) of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) for HDI objects. Special ABAP Managed HDI Containers (AMHC) can be created for HDI objects accessed in ABAP.

**HDI object**

Native HDI-managed database object in an HDI container of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md).

**host computer**

Computer on which the current [AS instance](../../abap-glossary/abenas_instance_glosry.md) is instantiated. The name of the current host computer can be read from the [system field](../../abap-glossary/abensystem_field_glosry.md) `sy-host`.

**ICF**

*-\>* Internet Communication Framework.

**ICF processing**

Processing of an HTTP/HTTPS query or SMTP query using ICF in an appropriate handler class and in a separate ICF session.

**ICF server**

Instance of a system that provides services that can be called using ICF. An ICF server can be an HTTP/HTTPS server or an SMTP server.

**ICF session**

[User session](../../abap-glossary/abenuser_session_glosry.md) for ICF processing. An ICF session is opened by the ICF to process an HTTP/HTTPS query or SMTP query.

**ICM**

*-\>* Internet Communication Manager.

**identity transformation**

[XSL transformation](../../abap-glossary/abenxsl_transformation_glosry.md) called `ID` delivered by SAP for reading or writing the canonical formats [asXML](../../abap-glossary/abenasxml_glosry.md) and [asJSON](../../abap-glossary/abenasjson_glosry.md). Calls of this transformation are handled in special ways internally, depending on the formats involved.

**InA**

[*-\>* Information Access Protocol](../../abap-glossary/abenina_protocol_glosry.md).

**Information Access protocol**

[InA](../../abap-glossary/abenina_glosry.md) for short. InA is a standardized protocol for defining and consuming multidimensional analytical queries. InA can be specified as a type of [service binding](../../abap-glossary/abenservice_binding_glosry.md) and it is interpreted by the [ABAP Analytical Engine](../../abap-glossary/abenabap_ae_glosry.md).

**information message**

[Message](../../abap-glossary/abenmessage_glosry.md) of the [message type](../../abap-glossary/abenmessage_type_glosry.md) *I*. Information messages are usually displayed in a dialog box.

**Interchange Text Format**

ITF for short. A SAP-specific markup language for system texts maintained in databases `DOKIL`, `DOKHL` and `DOKTL`. System texts written in ITF serve as API documentation for [repository objects](../../abap-glossary/abenrepository_object_glosry.md) that can be maintained in the ABAP Workbench. ITF is also used by text management tools such as [SAPscript](https://help.sap.com/docs/ABAP_PLATFORM_NEW/872c7db8e8ad411c8c3364aceed6e2c1/4e16389db8294181e10000000a15822b) or the current [ABAP Keyword Documentation](../../abenabap.md). Refer also to [KTD](../../abap-glossary/abenktd_glosry.md) for system texts used for documenting repository objects that can be maintained in [ADT](../../abap-glossary/abenadt_glosry.md) only.

**Internet Communication Framework**

ICF for short. A software layer in [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) that provides an ABAP interface for HTTP, HTTPS, and SMTP requests. Using the ICF, [ABAP programs](../../abap-glossary/abenabap_program_glosry.md) can communicate with the internet in both the sever and the client role. The ICF receives and sends web-based ABAP calls using the Internet Communication Manager.

**Internet Communication Manager**

ICM for short. A process of [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) that enables AS ABAP to communicate directly with the Internet using HTTP/HTTPS/SMTP. The `ICM` is used to connect an AS ABAP to web-based presentation components such as [SAPUI5](../../abap-glossary/abensapui5_glosry.md), Web Dynpro ABAP, and `BSP`. The ICM also enables an AS ABAP to serve both as a client and as a server for Web services. ABAP programs access ICM via classes and interfaces of the Internet Communication Framework.

**iXML Library Classic**

Global [classes](../../abap-glossary/abenglobal_class_glosry.md) that are accessible via [interfaces](../../abap-glossary/abenoo_intf_glosry.md) for handling [XML](../../abap-glossary/abenxml_glosry.md) documents in [DOM](../../abap-glossary/abendom_glosry.md) representation. The *integrated* iXML Library provides services such as an XML parser, an XML renderer, and reads and writes to the DOM. The interfaces of the iXML Library Classic start with the prefix `IF_IXML`.

**iXML Library Classic**

Global [classes](../../abap-glossary/abenglobal_class_glosry.md) that are accessible via [interfaces](../../abap-glossary/abenoo_intf_glosry.md) for handling [XML](../../abap-glossary/abenxml_glosry.md) documents in [DOM](../../abap-glossary/abendom_glosry.md) representation. The *integrated* iXML Library provides services such as an XML parser, an XML renderer, and reads and writes to the DOM. The interfaces of the iXML Library Classic start with the prefix `IF_IXML`.

**iXML Library for ABAP Cloud**

Global [classes](../../abap-glossary/abenglobal_class_glosry.md) that are accessible via [interfaces](../../abap-glossary/abenoo_intf_glosry.md) for handling [XML](../../abap-glossary/abenxml_glosry.md) documents in [DOM](../../abap-glossary/abendom_glosry.md) representation. The *integrated* iXML Library provides services such as an XML parser, an XML renderer, and reads and writes to the DOM. The interfaces of the iXML Library for ABAP Cloud start with the prefix `IF_IXML_CORE`.

**iXML Library for ABAP Cloud**

Global [classes](../../abap-glossary/abenglobal_class_glosry.md) that are accessible via [interfaces](../../abap-glossary/abenoo_intf_glosry.md) for handling [XML](../../abap-glossary/abenxml_glosry.md) documents in [DOM](../../abap-glossary/abendom_glosry.md) representation. The *integrated* iXML Library provides services such as an XML parser, an XML renderer, and reads and writes to the DOM. The interfaces of the iXML Library for ABAP Cloud start with the prefix `IF_IXML_CORE`.

**job**

Sequences of programs executed chronologically by particular control commands, especially as background requests.

**JSON**

JavaScript Object Notation ([`http://www.json.org/`](http://www.json.org/)). Data format in text form for data exchange between applications. In ABAP, the [sXML Library](../../abap-glossary/abensxml_library_glosry.md) and [transformations](../abap-data-interchange-formats/abenabap_json_trafos.md) can be used to access JSON, for which a special JSON-XML supported by [sXML](../../abap-glossary/abenjson_xml_glosry.md) Library is used. Additionally, a [JSON](../abap-data-interchange-formats/abenabap_json_lib_reader.md) reader and a [JSON writer](../abap-data-interchange-formats/abenabap_json_lib_writer.md) can be used.

**JSON library**

Global [interfaces](../../abap-glossary/abenglobal_interface_glosry.md) and [classes](../../abap-glossary/abenglobal_class_glosry.md) for handling [JSON](../../abap-glossary/abenjson_glosry.md) data. The classes and interfaces in the JSON library start with the prefixes `CL_JSON` or `IF_JSON`.

**JSON reader**

There are two kinds of JSON readers:

- [Instance](../../abap-glossary/abeninstance_glosry.md) of a [class](../../abap-glossary/abenclass_glosry.md) of the [JSON Library](../../abap-glossary/abenjson_library_glosry.md) that implements the [interface](../../abap-glossary/abenoo_intf_glosry.md) `IF_JSON_READER`.

- [XML reader](../../abap-glossary/abenxml_reader_glosry.md) that accesses [JSON](../../abap-glossary/abenjson_glosry.md) data. A JSON reader handles the JSON data internally like [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md).

[JSON reader](../abap-data-interchange-formats/abenabap_json_lib_reader.md)

[XML reader](../abap-data-interchange-formats/abenabap_json_sxml.md)

**JSON writer**

There are two kinds of JSON writers:

- [Instance](../../abap-glossary/abeninstance_glosry.md) of a [class](../../abap-glossary/abenclass_glosry.md) of the [JSON Library](../../abap-glossary/abenjson_library_glosry.md) that implements the [interface](../../abap-glossary/abenoo_intf_glosry.md) `IF_JSON_WRITER`.

- [XML writer](../../abap-glossary/abenxml_writer_glosry.md) that writes [JSON](../../abap-glossary/abenjson_glosry.md) data. A JSON writer expects input for [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) and uses it to create the JSON data.

[JSON writer](../abap-data-interchange-formats/abenabap_json_lib_writer.md)

[XML writer](../abap-data-interchange-formats/abenabap_json_sxml.md)

**JSON-XML**

SAP-specific representation of [JSON](../../abap-glossary/abenjson_glosry.md) data in [XML](../../abap-glossary/abenxml_glosry.md) format. [JSON readers](../../abap-glossary/abenjson_reader_glosry.md) and [JSON writers](../../abap-glossary/abenjson_writer_glosry.md) use JSON-XML to [parse](../abap-data-interchange-formats/abenabap_json_sxml.md) and [render](../abap-data-interchange-formats/abenabap_json_sxml.md) JSON data.

**Knowledge Transfer Document**

KTD for short. A Knowledge Transfer Document contains the documentation of a development object or its elements. It is based on a markdown language with plain text formatting syntax. A KTD can be displayed and maintained for its development object in [ADT](../../abap-glossary/abenadt_glosry.md).

**L**

Low-level programming language of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md). The programming language L can only be used internally and with restrictions at SAP. For general programming with the SAP HANA database, [SQL](../../abap-glossary/abensql_glosry.md) or the script language [SQLScript](../../abap-glossary/abensql_script_glosry.md) must be used. The use of L by customers and partners is not supported.

**L procedure**

[Database procedure](../../abap-glossary/abendatabase_procedure_glosry.md) of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) programmed in the internal SAP language L. SQLScript procedures can be created interactively in the SAP Web IDE for SAP HANA. In addition, [ABAP Managed Database Procedures (AMDP)](../../abap-glossary/abenabap_managed_db_proc_glosry.md) enable L procedures to be implemented in [AMDP procedure implementations](../../abap-glossary/abenamdp_procedure_method_glosry.md) of [AMDP classes](../../abap-glossary/abenamdp_class_glosry.md).

**language setting**

Part of the [language environment](../../abap-glossary/abenlanguage_environment_glosry.md). The language setting of an ABAP program comprises the [logon language](../../abap-glossary/abenlogon_language_glosry.md) and the [text environment language](../../abap-glossary/abentext_env_langu_glosry.md) of the [text environment](../../abap-glossary/abentext_environment_glosry.md).

**LDQ**

*-\>* Local Data Queue

**local data queue**

Persistence layer into which data can be placed and read only in the order in which it was stored. The local data queue triggers the no-send scenario of the qRFC.

**local update**

Update in the current [work process](../../abap-glossary/abenwork_process_glosry.md). It is not executed in a separate update session but in a separate [internal session](../../abap-glossary/abeninternal_session_glosry.md) of the current [ABAP session](../../abap-glossary/abenabap_session_glosry.md). The local update can be activated for an [SAP LUW](../../abap-glossary/abensap_luw_glosry.md) by using the statement `SET UPDATE TASK LOCAL`.

**lock**

Locks control the access to data by multiple users. Regarding access to [database tables](../../abap-glossary/abendatabase_table_glosry.md), there are [shared locks](../../abap-glossary/abenshared_lock_glosry.md) or [exclusive locks](../../abap-glossary/abenexclusive_lock_glosry.md) implemented as [database locks](../../abap-glossary/abendatabase_lock_glosry.md) and SAP locks. Regarding access to shared objects, there are area locks.

**lock function module**

Special [function module](../../abap-glossary/abenfunction_module_glosry.md) for setting and removing SAP locks. When creating a lock object, a function module with the prefix `ENQUEUE_` is created to set the lock, and a function module with the prefix `DEQUEUE_` is created to remove the lock.

**Logical Database Builder**

Tool in ABAP Workbench used to create and maintain logical databases. Called using transaction `SE36`.

**logical database schema**

A logical schema on a database. There are the following types of logical database schemas:

- logical local database schema

- [CDS logical external schema](../../abap-glossary/abencds_logical_schema_glosry.md)

**logical file name**

Platform-independent name that can be assigned to physical file names using the transactions `FILE` and `SF01`. Logical file names are used for platform-independent programming to validate file names.

**logical HDI container**

Part of the definition of an ABAP-managed HDI container (AMHC) to which a physical HDI container in the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) is mapped. A logical HDI container can be used as a logical schema in an [AMDP macro](../../abap-glossary/abenamdp_macro_glosry.md).

**logical local database schema**

A logical database schema in which the assignment of a physical [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md) of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) takes place in a mapping table. A logical local database schema is represented by a transportable [repository object](../../abap-glossary/abenrepository_object_glosry.md) that defines its properties.

**logical schema**

A logical schema is a symbolic name for a [database schema](../../abap-glossary/abendatabase_schema_glosry.md) of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) that can be used in an [AMDP macro](../../abap-glossary/abenamdp_macro_glosry.md). There are logical local database schemas, which are assigned to the database schema in a mapping table, and logical HDI containers, where the mapping is part of the definition of an ABAP-managed HDI container (AMHC).

In ABAP CDS, there are [logical external schemas](../../abap-glossary/abencds_logical_schema_glosry.md) that map [CDS external entities](../../abap-glossary/abencds_external_entity_glosry.md) to database schemas in an external system. They can be used in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) queries and as data sources in other [CDS entities](../../abap-glossary/abencds_entity_glosry.md).

**logon**

Time at which an [ABAP user](../../abap-glossary/abenabap_user_glosry.md) logs on to the [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) by specifying the [client ID](../../abap-glossary/abenclient_identifier_glosry.md), [user name](../../abap-glossary/abenuser_name_glosry.md), [password](../../abap-glossary/abenpassword_glosry.md), and the [logon language](../../abap-glossary/abenlogon_language_glosry.md). Each logon starts a [user session](../../abap-glossary/abenuser_session_glosry.md). Logons are made using the SAP GUI logon window or using frameworks such as `RFC`, ICF, or APC.

**logon language**

Language that an [ABAP user](../../abap-glossary/abenabap_user_glosry.md) specifies when logging on to an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). The logon language is persistent for the entire [user session](../../abap-glossary/abenuser_session_glosry.md). The logon language affects [messages](../../abap-glossary/abenmessage_glosry.md), [text elements](../../abap-glossary/abentext_element_glosry.md), and the [text environment](../../abap-glossary/abentext_environment_glosry.md). It can be determined using the method `GET_LOGON_LANGUAGE` of the class `CL_ABAP_SYST`.

**LUW**

Short for Logical unit of work. Time between two consistent states of the [database](../../abap-glossary/abendatabase_glosry.md). See also [SAP LUW](../../abap-glossary/abensap_luw_glosry.md) and [database LUW](../../abap-glossary/abendatabase_luw_glosry.md).

**MDMP system**

Short for multidisplay, multiprocessing system. An MDMP system contains multiple non-[Unicode](../../abap-glossary/abenunicode_glosry.md) [system code pages](../../abap-glossary/abensystem_codepage_glosry.md). The environment [code page](../../abap-glossary/abencodepage_glosry.md) of an [internal session](../../abap-glossary/abeninternal_session_glosry.md) depends on its current [text environment](../../abap-glossary/abentext_environment_glosry.md). MDMP systems are no longer supported from [ABAP release](../../abap-glossary/abenabap_release_glosry.md) 7.0.

**Memory Inspector**

Tool for displaying and analyzing memory snapshots. Called using transaction code `S_MEMORY_INSPECTOR`.

**memory snapshot**

Contains information about all [data objects](../../abap-glossary/abendata_object_glosry.md) and [instances](../../abap-glossary/abeninstance_glosry.md) of an [internal session](../../abap-glossary/abeninternal_session_glosry.md) along with their memory consumption. A memory snapshot can be created in the [ABAP Debugger](../../abap-glossary/abenabap_debugger_glosry.md) by the static method `WRITE_MEMORY_CONSUMPTION_FILE` of the [system class](../../abap-glossary/abensystem_class_glosry.md) `CL_ABAP_MEMORY_UTILITIES`, or by entering */hmusa* in the command field of the standard toolbar. Another option is selecting *System \> Utilities -\> Memory Analysis -\> Create Memory Snapshot*. The evaluation is performed by Memory Inspector.

**Message Maintenance**

Tool in [ADT](../../abap-glossary/abenadt_glosry.md) or in the ABAP Workbench (transaction `SE91`) for creating and maintaining [messages](../../abap-glossary/abenmessage_glosry.md).

**message server**

Component of the [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) that implements the communication between the [AS instances](../../abap-glossary/abenas_instance_glosry.md), and which determines the AS instance used when an [ABAP user](../../abap-glossary/abenabap_user_glosry.md) logs on to an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md).

**namespace**

A namespace is a set of unique names that identify a set of objects. In ABAP, we can distinguish [namespaces for program-internal objects](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) and a namespace for [repository objects](../../abap-glossary/abenrepository_object_glosry.md). The latter can be divided into a [SAP namespace](../../abap-glossary/abensap_namespace_glosry.md), a [customer namespace](../../abap-glossary/abencustomer_namespace_glosry.md), a [partner namespace](../../abap-glossary/abenpartner_namespace_glosry.md) and [prefix namespaces](../../abap-glossary/abenprefix_name_space_glosry.md).

**namespace prefix**

Prefix with five to ten characters that must contain a forward slash character (`/.../`) in the first and final place. The names of the [repository objects](../../abap-glossary/abenrepository_object_glosry.md) of a [prefix namespace](../../abap-glossary/abenprefix_name_space_glosry.md) are introduced by a namespace prefix.

**Native SQL**

Database-specific [SQL](../../abap-glossary/abensql_glosry.md) statements that are handled by the Native SQL interface of the [database interface](../../abap-glossary/abendatabase_interface_glosry.md). Native SQL is either passed from [ABAP programs](../../abap-glossary/abenabap_program_glosry.md) to the Native SQL interface using [objects](../../abap-glossary/abenobject_glosry.md) from the ADBC [classes](../../abap-glossary/abenclass_glosry.md) or specified statically between the statements `EXEC SQL` and `ENDEXEC`. [ABAP Managed Database Procedures (AMDP)](../../abap-glossary/abenabap_managed_db_proc_glosry.md) use Native SQL to call and manage [database procedures](../../abap-glossary/abendatabase_procedure_glosry.md) and [database functions](../../abap-glossary/abendatabase_function_glosry.md) with platform-dependent implementations.

**Native SQL interface**

Part of the [database interface](../../abap-glossary/abendatabase_interface_glosry.md) responsible for Native SQL statements. The Native SQL interface handles the statements made from the ADBC framework and all Native SQL statements embedded statically between `EXEC` and `ENDEXEC`. Vendor-specific [SQL](../../abap-glossary/abensql_glosry.md) statements are passed unchanged to the [database system](../../abap-glossary/abendatabase_system_glosry.md) of the current [database connection](../../abap-glossary/abendatabase_connection_glosry.md). SAP-specific static Native SQL statements are processed in the Native SQL interface before being passed. To enable this, the Native SQL interface contains platform-dependent parts (referred to as client libraries), which also perform conversion between ABAP types and database types.

**non-blocking mode**

Any statements that block the program flow are not allowed in an [ABAP programs](../../abap-glossary/abenabap_program_glosry.md) that is processed in non-blocking mode. There are values of the non-blocking mode for APC and ADF.

**Non-Unicode ABAP**

Obsolete [language version](../../abap-glossary/abenabap_version_glosry.md) of an [ABAP program](../../abap-glossary/abenabap_program_glosry.md) in which the [Unicode checks](../../abap-glossary/abenunicode_check_glosry.md) are not effective. A program with this language version cannot be executed in [Unicode systems](../../abap-glossary/abenunicode_system_glosry.md). In the current [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) release, only Unicode systems are supported. Therefore, Non-Unicode ABAP can no longer be used.

**Object Navigator**

Tool of the ABAP Workbench for the central maintenance of [repository objects](../../abap-glossary/abenrepository_object_glosry.md). The Object Navigator displays repository objects as nodes of different tree representations (browsers), such as Repository Browser, Repository Information System, or Enhancement Information System, in the navigation area. From here, they can be accessed via forward navigation in the tool area. Called using transaction `SE80`.

**OData**

Short for Open Data Protocol. OData is a standardized protocol for defining and consuming [RESTful](../../abap-glossary/abenrestful_glosry.md) APIs. [SAP Gateway](../../abap-glossary/abensap_gateway_glosry.md) provides such APIs for [AS ABAP](../../abap-glossary/abenas_abap_glosry.md).

[***-\>* More about**](http://www.odata.org)

**OLE automation**

OLE (object linking and embedding) automation allows various software applications to use automation objects to communicate with each other, exchange data, and control each other. A software application can make automation objects available to other applications (clients) by means of an automation interface. A client can use the corresponding object interface to create and control these kinds of objects.

**package**

A package encapsulates [repository objects](../../abap-glossary/abenrepository_object_glosry.md) in self-contained units. Packages are themselves repository objects and connect the repository objects they contain to the [Change and Transport System (CTS)](../../abap-glossary/abencts_glosry.md). The components of a package that can be used outside of the package must be published in a package interface. A package that accesses the repository objects of another package must declare this and have permission from the other package. Packages are created using Package Builder. See also [Package Concept](../../abap-glossary/abenpackage_concept_glosry.md).

**Package Builder**

An ABAP Workbench tool for creating and maintaining [packages](../../abap-glossary/abenpackage_glosry.md). Called using transaction `SE21`.

**package concept**

Rule set that is based on [packages](../../abap-glossary/abenpackage_glosry.md) and specifies the mutual usability of [repository objects](../../abap-glossary/abenrepository_object_glosry.md). Currently, only some of the rules are checked and only by the [ABAP Test Cockpit (ATC)](../../abap-glossary/abenabap_test_cockpit_glosry.md). There are no checks at runtime.

**parallel Remote Function Call**

pRFC for short. Extension of the asynchronous remote function call that enables parallelization to be controlled.

**partner namespace**

Predefined [namespace](../../abap-glossary/abennamespace_glosry.md) for [repository objects](../../abap-glossary/abenrepository_object_glosry.md) created in partner development systems. Names have `J` as the first character. These names can be used in partner systems, if no [prefix namespace](../../abap-glossary/abenprefix_name_space_glosry.md) is available.

**PCP**

*-\>* Push Channel Protocol

**performance trace**

Test tool combining multiple trace functions that allow system behavior to be analyzed in [database access](../abap-database-access/abendb_access.md) (SQL trace), access to the [table buffer](../../abap-glossary/abentable_buffer_glosry.md), access to lock management reads, and for external read access using RFC and ICF. Called using transaction `ST05`.

**pRFC**

*-\>* parallel remote function call

**profile parameter**

Defines default settings for an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). Profile parameters are created and displayed using transaction `RZ11`.

**Push Channel Protocol**

PCP for short. Describes an SAP communications format used to exchange messages between programs and internal or external interfaces. Currently, PCP is used by ABAP Channels and ABAP daemons.

**PXA**

Short for Program Execution Area. Memory for managing the fixed data of a running ABAP program. The PXA notably contains the byte codes of all programs running simultaneously on an [AS instance](../../abap-glossary/abenas_instance_glosry.md). This memory is shared by all [internal sessions](../../abap-glossary/abeninternal_session_glosry.md) of the AS instance, and there is only one such memory on each server. The byte code of a program that is executed once remains buffered in the PXA as a program load for as long as possible to prevent reloads from the database if the program is executed again. Furthermore, the PXA buffers shared resources, such as values of [constants](../../abap-glossary/abenconstant_glosry.md), and is used for the [initial value sharing](../../abap-glossary/abeninitial_value_sharing_glosry.md) of [boxed components](../../abap-glossary/abenboxed_component_glosry.md).

**qRFC**

*-\>* queued remote function call

**queued Remote Function Call**

qRFC for short. Obsolete extension of the transactional remote function call enabling a call sequence to be determined.

**read lock**

Area lock on an area instance version in the shared objects memory. A read lock enables read accesses to the area instance version.

**release contract**

Classification of a [repository object](../../abap-glossary/abenrepository_object_glosry.md) that is a prerequisite for its usability as an [released API](../../abap-glossary/abenreleased_api_glosry.md). A release contract ensures a certain stability regarding consistency and compatibility of released APIs.

There are currently the following release contracts:

- [C0 contract, release](../../abap-glossary/abenc0_contract_glosry.md), which allows enhancement fields to be added at specified extension options.

- [C1 contract, use system-internally](../../abap-glossary/abenc1_contract_glosry.md), which guarantees a stable interface for use within the [AS ABAP](../../abap-glossary/abenas_abap_glosry.md)

- [C2 contract, use as remote API](../../abap-glossary/abenc2_contract_glosry.md), which also guarantees a stable interface for use outside the AS ABAP.

- [C3 contract, manage configuration content](../../abap-glossary/abenc3_contract_glosry.md), which ensures a stable persistence for configuration content.

- [C4 contract, use in ABAP-Managed Database Procedures](../../abap-glossary/abenc4_contract_glosry.md), which guarantees a stable interface of [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md) for use in other AMDP methods.

Objects are classified in [ADT](../../abap-glossary/abenadt_glosry.md) or using special transactions such as `SCFD_REGISTRY`.

**released API**

[Repository object](../../abap-glossary/abenrepository_object_glosry.md) or part of an repository object that is released for access in [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md). A released API is based on two classifications:

- A [release contract](../../abap-glossary/abenrelease_contract_glosry.md) that governs changes to released APIs.

- Visibility for a [restricted ABAP language version](../../abap-glossary/abenrestricted_version_glosry.md).

**Remote Function Call**

RFC for short. Call of a [function module](../../abap-glossary/abenfunction_module_glosry.md) using the RFC interface Calls be made in the same or in different systems. The target system is determined using an RFC destination. Connections are possible between different [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) or between an AS ABAP and an external system. In non-SAP systems, specially programmed functions whose [interface](../../abap-glossary/abenintf_gen_glosry.md) simulates a function module are called in external systems instead of function modules. Function calls can be synchronous, asynchronous, or transactional.

**remote-enabled function module**

RFM for short. [Function module](../../abap-glossary/abenfunction_module_glosry.md) that is marked as *remote-enabled* in its properties and can be called using remote function call.

**repository**

*-\>* [ABAP Repository](../../abap-glossary/abenabap_repository_glosry.md)

**repository browser**

Standard layout of the Object Navigator for the structured display of [repository objects](../../abap-glossary/abenrepository_object_glosry.md) sorted according to their type.

**Repository Info System**

Tool in the ABAP Workbench for searching for [repository objects](../../abap-glossary/abenrepository_object_glosry.md). Called in the Object Navigator or via transaction code `SE15`.

**restricted ABAP language version**

[ABAP language version](../../abap-glossary/abenabap_version_glosry.md) that is restricted as follows:

- The ABAP language scope is limited.

- Access to other repository objects is restricted by [released APIs](../../abap-glossary/abenreleased_api_glosry.md).

Restricted ABAP language versions are:

- [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md)

- [ABAP for Key Users](../../abap-glossary/abenabap_for_key_users_glosry.md)

[Standard ABAP](../../abap-glossary/abenstandard_abap_glosry.md) is an [unrestricted ABAP language version](../../abap-glossary/abenunrestricted_version_glosry.md).

**RFC**

*-\>* remote function call

**RFC client**

Instance of a system that calls services using RFC.

**RFC destination**

An RFC destination contains the connection parameters for remote function calls. It contains the connection type, the target system, and the partner program. Connections that only affect another [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) can be classified as trusted systems. RFC destinations are managed statically using the transaction `SM59` or dynamically using the class `CL_DYNAMIC_DESTINATION`.

**RFC interface**

Interface for remote function calls (RFC). The RFC interface consists of an interface for [ABAP programs](../../abap-glossary/abenabap_program_glosry.md) and interfaces for non-ABAP programs.

**RFC processing**

Processing of a remote function call using the RFC interface in an RFM.

**RFC server**

Instance of a system that provides services that can be called using RFC.

**RFC server group**

Group of multiple [AS instances](../../abap-glossary/abenas_instance_glosry.md) of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) that are provided to process asynchronous remote function calls (RFC) concurrently. RFC server groups are created using transaction code `RZ12`.

**RFC session**

[User session](../../abap-glossary/abenuser_session_glosry.md) for RFC processing. An RFC session is opened using a remote function call.

**RFM**

Remote-enabled function module *-\>*.

**runtime analysis**

Tool for analyzing the execution of program parts or individual statements and for measuring their runtime in SAP GUI. Called using transaction code `SAT`. Replaced by the ABAP Profiler in the [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md).

**runtime monitor**

Tool for recording events raised by [system classes](../../abap-glossary/abensystem_class_glosry.md) when a program is executed. Called using transaction code `SRTM`.

**SAP BTP ABAP environment**

[ABAP system](../../abap-glossary/abenabap_system_glosry.md) (aka [Steampunk](../../abap-glossary/abensteampunk_glosry.md)) in [SAP BTP](../../abap-glossary/abensap_btp_glosry.md) that provides the [ABAP technology](../../abap-glossary/abenabap_techno_glosry.md) as a service to customers and partners. ABAP development is governed by the restricted rules of [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md).

**SAP buffering**

Buffering of frequently used data in the [shared memory](../../abap-glossary/abenshared_memory_glosry.md) buffers of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) [AS instance](../../abap-glossary/abenas_instance_glosry.md). Includes [table buffering](../../abap-glossary/abentable_buffering_glosry.md).

[***-\>* More about**](https://help.sap.com/docs/ABAP_PLATFORM_NEW/3364beced9d145a5ad185c89a1e04658/c43a6dbb505211d189550000e829fbbd)

**SAP Business Technology Platform**

SAP BTP for short. A platform for development and deployment of business technology provided by SAP. The main focus of SAP BTP is on cloud development, but it also supports technologies used in on-premise deployments such as the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md). SAP BTP comprises the [SAP BTP ABAP environment](../../abap-glossary/abensap_btp_abap_env_glosry.md) that makes the [ABAP technology](../../abap-glossary/abenabap_techno_glosry.md) available for cloud development with [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md).

**SAP Code page number**

Internal SAP ID for a [code page](../../abap-glossary/abencodepage_glosry.md) that is stored in the database table `TCP00`. If the [byte order](../../abap-glossary/abenbyte_order_glosry.md) of a code page is relevant, an individual SAP code page number is assigned to it there for each endian. For example, the code page numbers for [UTF-16](../../abap-glossary/abenutf16_glosry.md) are 4102 ([big endian](../../abap-glossary/abenbig_endian_glosry.md)) and 4103 ([little endian](../../abap-glossary/abenlittle_endian_glosry.md)).

**SAP Easy Access**

Initial program that is called after a dialog based logon to an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). SAP Easy Access displays an initial menu for the access to the AS ABAP by a dialog user. By default, this menu is either the SAP menu or a user menu. The SAP menu is an area menu that is centrally defined or overridden by an entry in the [user master record](../../abap-glossary/abenuser_master_record_glosry.md). A user menu contains all the functions required by a dialog user and is created and assigned by the system administrator via the role maintenance (transaction `PFCG`). Each user can also define their favorites menu in SAP Easy Access that is displayed together with or instead of the default menu.

**SAP Enterprise Search**

A technology that enables you to search data in an application in a unified way. It provides a unified, comprehensive, secure, and real-time access to enterprise data and information from inside and outside of a company. The search returns both structured data (business objects) and unstructured data (HTML files, presentations, documents) from SAP systems and other search providers, and provides direct access to the related applications and actions. In ABAP, [CDS-based enterprise search](../../abap-glossary/abencds_enterprisesearch_glosry.md) is available.

**SAP Gateway**

Framework that makes it possible to access [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) using standardized open protocols such as [OData](../../abap-glossary/abenodata_glosry.md). [Business services](../../abap-glossary/abenbusiness_service_glosry.md) and [RAP business objects](../../abap-glossary/abenrap_bo_glosry.md) based on the data and behavior modeled in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) use SAP Gateway internally as part of the [RAP runtime framework](../../abap-glossary/abenrap_runt_framework_glosry.md).

**SAP HANA**

SAP HANA is a platform for SAP In-Memory Computing based on the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md). If an SAP HANA database is used as the [standard database](../../abap-glossary/abenstandard_db_glosry.md) of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md), ABAP programs can use [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) to access SAP HANA directly. In addition, secondary connections can also be used to access SAP HANA from ABAP.

**SAP HANA Cloud database**

Database of [SAP HANA Cloud](../../abap-glossary/abensap_hana_cloud_glosry.md) that offers restricted functionality compared with a general [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md). An SAP HANA Cloud database does not support SAP HANA XSC and there is no full text index.

**SAP HANA Cockpit**

Browser-based administration tool in XSA. Replaces the administration perspective of the SAP-HANA-Studios.

**SAP HANA database**

The SAP HANA database is the in-memory database of [SAP HANA](../../abap-glossary/abensap_hana_glosry.md). It is the only database that is supported as the [standard database](../../abap-glossary/abenstandard_db_glosry.md) of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md).

**SAP HANA remote source**

A named [database object](../../abap-glossary/abendb_object_glosry.md) that contains the connection details for accessing an external system and the credentials to use it. An SAP HANA remote source uses a remote source adapter, such as [ODBC](../../abap-glossary/abenodbc_glosry.md), to connect to a remote [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md), a non-SAP HANA database, or to the [SQL services](../../abap-glossary/abenabap_sql_services_glosry.md) of a remote [AS ABAP](../../abap-glossary/abenas_abap_glosry.md).

**SAP HANA Repository**

Repository of objects in the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md). More specifically, XSC objects are stored in the SAP HANA Repository. XSA objects, on the other hand, are not stored in the SAP HANA Repository but are usually deployed using HDI.

**SAP HANA Smart Data Access**

Software that enables the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) to access and query data from other (remote) enterprise data stores based on a [data federation](../../abap-glossary/abendata_federation_glosry.md) approach. This technology is included in the SAP HANA platform. SAP HANA Smart Data Access uses the [ODBC](../../abap-glossary/abenodbc_glosry.md) protocol for external communication.

[***-\>* More about**](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/a07c7ff25997460bbcb73099fb59007d)

**SAP HANA SQL optimizer**

The query optimizer generates the most efficient query execution plan for a given query and passes it to the executor. In [HANA SQL](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f), there are basically two optimization tasks:

- Rule-based optimization (declarative): Rewriting of the entire tree by, for example, removing joins. More efficient queries are produced at best.

- Cost-based optimization (procedural): Discovering the space of access plans of the queries produced during the rule-based optimization and comparing the access plans by cost and size. The cheapest query is used for further processing.

**SAP HANA Studio**

Eclipse-based tool for database objects of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md), especially for XSC objects stored in the SAP HANA Repository. In XSA, SAP HANA Studio is replaced by the SAP Web IDE for SAP HANA and the SAP HANA Cockpit.

**SAP HANA Transport for ABAP**

HTA for short. Infrastructure that links the transport of database objects of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) (SAP HANA Repository objects and HDI objects) to the [Change and Transport System (CTS)](../../abap-glossary/abencts_glosry.md) of ABAP.

[***-\>* More about**](https://help.sap.com/docs/ABAP_PLATFORM_NEW/6811c09434084fd1bc4f40e66913ce11/ff7652bd542849b18b218efe8d2f2373)

**SAP HANA view**

An SAP HANA view is used to select, analyze, or perform calculations with data from the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md). Attribute views, analytic views and calculation views can be distinguished. SAP HANA views can be defined as objects of SAP HANA XS for which there are special methods for accessing these views in [ABAP programs](../../abap-glossary/abenabap_program_glosry.md).

**SAP HANA virtual table**

A named, SAP HANA-local proxy object that represents a database object, such as a table or a view, in an external system. A virtual table can be accessed and queried as a normal table or view, allowing you to access data from a remote object in the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) as if the data were stored in local tables. The [SAP HANA Smart Data Access](../../abap-glossary/abensap_hana_sda_glosry.md) technology uses virtual tables to communicate with external systems.

For [dynamic external entities](../../abap-glossary/abencds_dynamic_ee_glosry.md), a virtual table is created as a representation of the remote database object to be read. This is done implicitly by the [database interface](../../abap-glossary/abendatabase_interface_glosry.md) of [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) as soon as the external entity is accessed using [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) under the precondition that a configured [logical external schema](../../abap-glossary/abencds_logical_schema_glosry.md) is available.

**SAP HANA XS**

Short for SAP HANA extended application services. XS is a framework for developing and managing native applications in [SAP HANA](../../abap-glossary/abensap_hana_glosry.md). The current version, XSA, replaces the previous version, XSC. XS objects can be accessed in ABAP.

**SAP HANA XSA**

Short for SAP HANA extended application services Advanced Model. Current version of XS and successor to XSC. SAP Web IDE for SAP HANA and SAP HANA Cockpit can be used to develop and manage XSA objects. Objects are usually deployed using HDI.

**SAP HANA XSC**

Short for SAP HANA extended application services Classic Model. Previous version of XS and predecessor to XSA. XSC objects are stored in the SAP HANA repository and are usually developed and managed in SAP HANA Studio. SAP HANA XSC is not supported by a [SAP HANA Cloud database](../../abap-glossary/abensap_hana_cloud_db_glosry.md).

**SAP lock**

Logical [lock](../../abap-glossary/abenlock_glosry.md) based on lock objects.

**SAP LUW**

Interrelated sequence of programming units, the execution of which, for example, in dialog steps or in remote function calls, can be distributed across several [work processes](../../abap-glossary/abenwork_process_glosry.md). However, their database changes are processed within a single [database LUW](../../abap-glossary/abendatabase_luw_glosry.md). SAP LUWs are implemented by bundling techniques, in which programming units such as update function modules or [subroutines](../../abap-glossary/abensubroutine_glosry.md) are registered in different work processes but executed by a single work process. An SAP LUW is usually started by opening a new [internal session](../../abap-glossary/abeninternal_session_glosry.md) and completed by the [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statement [`COMMIT WORK`](../abap-database-access/abapcommit.md). Changes within one SAP LUW can be undone by the ABAP SQL statement [`ROLLBACK WORK`](../abap-database-access/abaprollback.md).

The [controlled SAP LUW](../../abap-glossary/abencontrolled_sap_luw_glosry.md) is an extension to the SAP LUW.

**SAP memory**

Obsolete name for user memory

**SAP namespace**

[Namespace](../../abap-glossary/abennamespace_glosry.md) for [repository objects](../../abap-glossary/abenrepository_object_glosry.md) created in SAP's own development systems. There are no real restrictions for the names. To avoid namespace conflicts [prefix namespace](../../abap-glossary/abenprefix_name_space_glosry.md) can be used. Internally at SAP, all names are checked using a cross-system table to ensure their uniqueness.

**SAP S/4HANA**

SAP's on-premise business suite that is based on a [ABAP Platform](../../abap-glossary/abenabap_platform_glosry.md) and runs on [SAP HANA](../../abap-glossary/abensap_hana_glosry.md). See also [SAP S/4HANA Cloud Public Edition](../../abap-glossary/abensap_s4hana_cpub_glosry.md) and [SAP S/4HANA Cloud Private Edition](../../abap-glossary/abensap_s4hana_cpriv_glosry.md).

**SAP S/4HANA Cloud**

*-\>* [SAP S/4HANA Cloud Public Edition](../../abap-glossary/abensap_s4hana_cpub_glosry.md)

**SAP S/4HANA Cloud ABAP environment**

Restricted [ABAP development environment](../../abap-glossary/abenabap_dev_envir_glosry.md) (aka [embedded Steampunk](../../abap-glossary/abenembedded_steampunk_glosry.md)) for customer developments in [SAP S/4HANA Cloud Public Edition](../../abap-glossary/abensap_s4hana_cpub_glosry.md), [SAP S/4HANA Cloud Private Edition](../../abap-glossary/abensap_s4hana_cpriv_glosry.md) and [SAP S/4HANA](../../abap-glossary/abensap_s4hana_glosry.md). The developments are governed by the restricted rules of [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md). See also [SAP BTP ABAP environment](../../abap-glossary/abensap_btp_abap_env_glosry.md) (aka [Steampunk](../../abap-glossary/abensteampunk_glosry.md)).

**SAP S/4HANA Cloud Private Edition**

Cloud version of [SAP S/4HANA](../../abap-glossary/abensap_s4hana_glosry.md) based on the [ABAP Platform](../../abap-glossary/abenabap_platform_glosry.md) of SAP S/4HANA. Partner and customer developments can either use the [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md) or the [classic ABAP](../../abap-glossary/abenclassic_abap_glosry.md) paradigm. For ABAP Cloud the [SAP S/4HANA Cloud ABAP environment](../../abap-glossary/abens4_hana_cloud_abap_env_glosry.md) (aka [embedded Steampunk](../../abap-glossary/abenembedded_steampunk_glosry.md)) can be used. See also [SAP S/4HANA Cloud Public Edition](../../abap-glossary/abensap_s4hana_cpub_glosry.md).

**SAP S/4HANA Cloud Public Edition**

SAP S/4HANA Cloud for short. Cloud version of [SAP S/4HANA](../../abap-glossary/abensap_s4hana_glosry.md). Partner and customer developments are governed by the [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md) paradigm. For that the [SAP S/4HANA Cloud ABAP environment](../../abap-glossary/abens4_hana_cloud_abap_env_glosry.md) (aka [embedded Steampunk](../../abap-glossary/abenembedded_steampunk_glosry.md)) can be used. See also [SAP S/4HANA Cloud Private Edition](../../abap-glossary/abensap_s4hana_cpriv_glosry.md).

**SAP Web IDE for SAP HANA**

Browser-based development tool in XSA. Replaces the development and modeling perspectives of the SAP-HANA-Studios.

**SAP XSLT processor**

System program integrated into the [ABAP kernel](../../abap-glossary/abenkernel_glosry.md) to execute [XSL transformations](../../abap-glossary/abenxsl_transformation_glosry.md).

**scalar function**

In the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md), a [database function](../../abap-glossary/abendatabase_function_glosry.md) with a scalar or elementary return value. In [SQLScript](../../abap-glossary/abensql_script_glosry.md), scalar functions can be used as operands in the same places as elementary variables or columns of database tables or views. A scalar function can be managed as an [AMDP function](../../abap-glossary/abenamdp_function_glosry.md) in an [AMDP class](../../abap-glossary/abenamdp_class_glosry.md).

**secondary connection**

User-defined [database connection](../../abap-glossary/abendatabase_connection_glosry.md) from an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) to a secondary database. The connection can be to other databases or to other [database schemas](../../abap-glossary/abendatabase_schema_glosry.md) in the [standard database](../../abap-glossary/abenstandard_db_glosry.md). The properties of the secondary connections that can be used by a [work process](../../abap-glossary/abenwork_process_glosry.md) are defined in the database table `DBCON`. These secondary connections are managed using the DBA Cockpit tool. The only secondary connections that should be used are those from an AS ABAP with an [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) as its standard database to another SAP HANA database. [SAP HANA Smart Data Access (SDA)](../../abap-glossary/abensap_hana_sda_glosry.md) should be used for access to other databases. [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) provides [CDS external entities](../../abap-glossary/abencds_external_entity_glosry.md) for remote connections with [SAP HANA Smart Data Access](../../abap-glossary/abensap_hana_sda_glosry.md).

**secondary database**

Target database of a secondary connection defined in the database table `DBCON`. The database system must be a system supported by SAP and the software required for access using ABAP must be installed as a database shared library (DBSL) on the current [AS ABAP](../../abap-glossary/abenstandard_db_glosry.md), if the database is different to its standard database of the AS ABAP. Only [SAP HANA databases](../../abap-glossary/abenhana_database_glosry.md) should be used as secondary databases of systems that have such a database as their [standard database](../../abap-glossary/abenstandard_db_glosry.md).

**secondary language** Language specified in the profile parameter `zcsa/second_language`. The secondary language is used for [messages](../../abap-glossary/abenmessage_glosry.md), [text pools](../../abap-glossary/abentext_pool_glosry.md), and translatable [CDS annotations](../../abap-glossary/abencds_annotation_glosry.md) if the desired language is not found.

**selection include**

[Include program](../../abap-glossary/abeninclude_program_glosry.md) within a logical database in which the standard selection screen of the logical database is defined.

**selection view**

If dynamic selections are required for a node of a logical database, a selection view can be used to determine the node [fields](../../abap-glossary/abenfield_glosry.md) for which the user can define dynamic selections.

**serialization**

Transformation of ABAP data into [XML](../../abap-glossary/abenxml_glosry.md) data or [JSON](../../abap-glossary/abenjson_glosry.md) data. Performed either by calling an [XSLT program](../../abap-glossary/abenxsl_transformation_glosry.md) or a [Simple Transformation](../../abap-glossary/abensimple_transformation_glosry.md). If [XSLT](../../abap-glossary/abenxslt_glosry.md) is used, the system first creates a [canonical XML representation](../../abap-glossary/abencanonical_xml_represent_glosry.md) ([asXML](../../abap-glossary/abenxml_glosry.md)).

**service connection**

Additional [database connection](../../abap-glossary/abendatabase_connection_glosry.md) from an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) to the [standard database](../../abap-glossary/abenstandard_db_glosry.md). In addition to the [standard connection](../../abap-glossary/abenstandard_db_connection_glosry.md), service connections to the standard database called `R/3*name` can be opened for a [work process](../../abap-glossary/abenwork_process_glosry.md) to access the [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md).

**session**

Organizational unit of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) for executing ABAP programs. An ABAP program is executed in an [internal session](../../abap-glossary/abeninternal_session_glosry.md) in an [ABAP session](../../abap-glossary/abenabap_session_glosry.md), which itself is in a [user session](../../abap-glossary/abenuser_session_glosry.md). Within the program, there is access to memory areas assigned to the sessions and to the [shared memory](../../abap-glossary/abenshared_memory_glosry.md) of the current [AS instance](../../abap-glossary/abenas_instance_glosry.md).

**session memory**

Memory for the modifiable parts of a program in an [internal session](../../abap-glossary/abeninternal_session_glosry.md). From the perspective of an ABAP program, the session memory can be divided into a [heap](../../abap-glossary/abenheap_glosry.md) area and a [stack](../../abap-glossary/abenstack_glosry.md) area. The non-modifiable parts of a program are stored in [PXA](../../abap-glossary/abenpxa_glosry.md), which is referred to in the session memory.

**SFW**

*-\>* [Switch Framework](../../abap-glossary/abenswitch_framework_glosry.md)

**shared lock**

[Lock](../../abap-glossary/abenlock_glosry.md) that allows other users to set further shared locks but no simultaneous [exclusive locks](../../abap-glossary/abenexclusive_lock_glosry.md) for the locked data. The [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statement [`SELECT`](../abap-database-access/abapselect.md) without the addition [`FOR UPDATE`](../abap-database-access/abapselect_single.md) as well as the corresponding Native SQL statement or a `SELECT` statement in an [AMDP](../../abap-glossary/abenamdp_method_glosry.md) method do not set such a [database lock](../../abap-glossary/abendatabase_lock_glosry.md) for the addressed lines by default. A shared lock is set as an SAP lock via a correspondingly parameterized call of a lock function module.

**shared memory**

Memory area of an [AS instance](../../abap-glossary/abenas_instance_glosry.md) in which the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md) stores programs, program data, buffers, and so on. In the shared memory of the current AS instance, [ABAP programs](../../abap-glossary/abenabap_program_glosry.md) can either access [data clusters](../../abap-glossary/abendata_cluster_glosry.md) in cross-transactional application buffers or shared objects in the shared objects memory. The amount of shared memory that can be occupied by the different consumers is defined statically using profile parameters. Transaction `ST02` (SAP Memory Management) shows the current occupancy of the shared memory and the corresponding profile parameters.

**shared object**

[Instance](../../abap-glossary/abeninstance_glosry.md) of a shared memory-enabled class or [anonymous data object](../../abap-glossary/abenanonymous_data_object_glosry.md) that is stored in an area instance version of the [shared memory](../../abap-glossary/abenshared_memory_glosry.md). A shared object is created using the addition `AREA HANDLE` of statement [`CREATE OBJECT`](../abap-creating-objects-and-values/abapcreate_object.md) or [`CREATE DATA`](../abap-creating-objects-and-values/abapcreate_data.md). [References](../../abap-glossary/abenreference_glosry.md) to shared objects are possible in other shared objects of the same area instance version and during the connection to the respective area instance version via an area handle.

**simple enhancement implementation**

Semantically interrelated enhancement of a [repository object](../../abap-glossary/abenrepository_object_glosry.md). A simple enhancement implementation manages one or more [enhancement implementation elements](../../abap-glossary/abenenhancement_impl_elem_glosry.md). A simple enhancement implementation can occur independently or as a component of a [composite enhancement implementation](../../abap-glossary/abencomp_enhancement_impl_glosry.md).

**simple enhancement spot**

Reference to a set of [enhancement spot element definitions](../../abap-glossary/abenenhancement_spot_def_glosry.md). A simple enhancement spot can occur independently or as a component of a [composite enhancement spot](../../abap-glossary/abencomp_enhancement_spot_glosry.md).

**Simple Transformation**

ST for short. SAP-specific programming language for transformations between [XML](../../abap-glossary/abenxml_glosry.md) formats and ABAP data and vice versa. [Serializations](../../abap-glossary/abenserialization_glosry.md) and [deserializations](../../abap-glossary/abendeserialization_glosry.md) can be carried out using ST. Simple Transformations are edited using the Transformation Editor and are called using the statement [`CALL TRANSFORMATION`](../abap-data-interchange-formats/abapcall_transformation.md).

**single code page system**

System with only one [system code page](../../abap-glossary/abensystem_codepage_glosry.md). Either a [Unicode system](../../abap-glossary/abenunicode_system_glosry.md) with [UTF 16](../../abap-glossary/abenutf16_glosry.md) or a non-Unicode system with a non-Unicode code page. From [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) [ABAP release](../../abap-glossary/abenabap_release_glosry.md) 7.0, only single code page systems are supported and from ABAP release 7.62 only Unicode systems. The [text environment](../../abap-glossary/abentext_environment_glosry.md) for an [internal session](../../abap-glossary/abeninternal_session_glosry.md) can only be set using this code page in a single code page system. See also MDMP system.

**SQL service**

A standardized protocol of the [Application Server ABAP](../../abap-glossary/abenas_abap_glosry.md) providing SQL-level access to [ABAP-managed database objects](../../abap-glossary/abenabap_managed_db_object_glosry.md), such as [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), for consumers outside the system. The SQL service can be accessed with the ODBC driver for ABAP using the [ODBC](../../abap-glossary/abenodbc_glosry.md) protocol. It can be specified as a type of [service binding](../../abap-glossary/abenservice_binding_glosry.md). With the SQL service, remote access to the database of AS ABAP is performed using the [ABAP SQL engine](../../abap-glossary/abenabap_sql_engine_glosry.md) and (almost) all important ABAP SQL features are supported. The SQL service is also integrated with [SAP HANA Smart Data Access](../../abap-glossary/abensap_hana_sda_glosry.md), which enables the SAP HANA database to query data from remote data stores.

**SQL trace**

Trace function used to analyze the [SQL](../../abap-glossary/abensql_glosry.md) statements passed from the [database interface](../../abap-glossary/abendatabase_interface_glosry.md) to the [database system](../../abap-glossary/abendatabase_interface_glosry.md). It can be called from the tools [ABAP Debugger](../../abap-glossary/abenabap_debugger_glosry.md) or performance trace (transaction `ST05`).

**SQL view**

[ABAP-managed database object](../../abap-glossary/abenabap_managed_db_object_glosry.md) that is generated automatically by the [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md) or by [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) for DDIC table views and [CDS entities](../../abap-glossary/abencds_entity_glosry.md), such as:

- [DDIC database view](../../abap-glossary/abendatabase_view_glosry.md), the name of the SQL View is the same as the name of the DDIC database view

- [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), the name of the SQL view is the same as the name of the CDS view entity

- [CDS transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md), where the name of the SQL view is the same as the name of the CDS transactional query

- [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md), where the name of the SQL view is the same as the name of the CDS transactional interface

- [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md), the name of the SQL view is the same as the name of the CDS hierarchy view

- [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), the name of the SQL view is the same as the name of the respective [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md)

Like all ABAP-managed database objects, an SQL view should mainly be accessed with [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) using the names defined in the ABAP Dictionary or in ABAP CDS. For [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), the name of the CDS entity should be used and not the name of the CDS-managed DDIC view (obsolete). When using [AMDP](../../abap-glossary/abenamdp_glosry.md) or Native SQL, only the technical name of the SQL view can be used.

**SQLScript**

Script language for the programming of [SQLScript procedures](../../abap-glossary/abensql_script_procedure_glosry.md) and [SQLScript functions](../../abap-glossary/abensql_script_function_glosry.md) on the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md).

[***-\>* More about**](https://help.sap.com/docs/SAP_HANA_PLATFORM/de2486ee947e43e684d39702027f8a94/28f2d64d4fab4e789ee0070be418419d)

**SQLScript function**

A [database function](../../abap-glossary/abendatabase_function_glosry.md) of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) programmed in the language [SQLScript](../../abap-glossary/abensql_script_glosry.md). SQLScript functions can be created using tools such as SAP Web IDE for SAP HANA or Native SQL in programs. [ABAP Managed Database Procedures (AMDP)](../../abap-glossary/abenabap_managed_db_proc_glosry.md) enable SQLScript functions to be implemented in [AMDP procedure implementations](../../abap-glossary/abenamdp_function_method_glosry.md) of [AMDP classes](../../abap-glossary/abenamdp_class_glosry.md). See also [SQLScript procedure](../../abap-glossary/abensql_script_procedure_glosry.md). [***-\>* More about**](https://help.sap.com/docs/SAP_HANA_PLATFORM/de2486ee947e43e684d39702027f8a94/28f2d64d4fab4e789ee0070be418419d)

**SQLScript procedure**

A [database procedure](../../abap-glossary/abendatabase_procedure_glosry.md) of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) programmed in the language [SQLScript](../../abap-glossary/abensql_script_glosry.md). SQLScript procedures can be created using tools such as SAP Web IDE for SAP HANA or Native SQL in programs. [ABAP Managed Database Procedures (AMDP)](../../abap-glossary/abenabap_managed_db_proc_glosry.md) enable SQLScript procedures to be implemented in [AMDP procedure implementations](../../abap-glossary/abenamdp_procedure_method_glosry.md) of [AMDP classes](../../abap-glossary/abenamdp_class_glosry.md). Database procedure proxies can be created to call SQLScript procedures in the SAP HANA Repository. See also [SQLScript Function](../../abap-glossary/abensql_script_function_glosry.md).

[***-\>* More about**](https://help.sap.com/docs/SAP_HANA_PLATFORM/de2486ee947e43e684d39702027f8a94/28f2d64d4fab4e789ee0070be418419d)

**sRFC**

*-\>* synchronous remote function call

**SRID**

*-\>* [spatial reference identifier](../../abap-glossary/abenspatial_ref_identifier_glosry.md)

**ST**

*-\>* [Simple transformation](../../abap-glossary/abensimple_transformation_glosry.md).

**Standard ABAP**

[Unrestricted ABAP language version](../../abap-glossary/abenunrestricted_version_glosry.md) with unrestricted language scope and unrestricted access to [repository objects](../../abap-glossary/abenrepository_object_glosry.md). For Standard ABAP, the [Unicode checks](../../abap-glossary/abenunicode_check_glosry.md) are effective that are required in an [Unicode systems](../../abap-glossary/abenunicode_system_glosry.md). Standard ABAP is the [ABAP language version](../../abap-glossary/abenabap_version_glosry.md) for [classic ABAP](../../abap-glossary/abenclassic_abap_glosry.md).

**Standard ABAP with restricted object use**

Obsolete [ABAP language version](../../abap-glossary/abenabap_version_glosry.md) with restricted use of [repository objects](../../abap-glossary/abenrepository_object_glosry.md) in which all language elements of [Standard ABAP](../../abap-glossary/abenstandard_abap_glosry.md) are allowed.

**standard connection**

[Database connection](../../abap-glossary/abendatabase_connection_glosry.md) between an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) and its [standard database](../../abap-glossary/abenstandard_db_glosry.md). A standard connection is always opened for each [work process](../../abap-glossary/abenwork_process_glosry.md) of an AS ABAP. The [ABAP database schema](../../abap-glossary/abendatabase_user_glosry.md) is assigned to the [database user](../../abap-glossary/abenabap_db_schema_glosry.md) of the standard connection. By default, reads in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), Native SQL, and [AMDP](../../abap-glossary/abenamdp_glosry.md) are performed on this [database schema](../../abap-glossary/abendatabase_schema_glosry.md) using this standard connection.

**standard database**

Central database of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). A [standard connection](../../abap-glossary/abenstandard_db_connection_glosry.md) to the standard database always exists for each [work process](../../abap-glossary/abenwork_process_glosry.md) of an AS ABAP. Only a [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) is supported as a standard database.

**Steampunk**

Internal SAP project name for the [SAP BTP ABAP environment](../../abap-glossary/abensap_btp_abap_env_glosry.md). See also [embedded Steampunk](../../abap-glossary/abenembedded_steampunk_glosry.md).

**switch**

[Repository object](../../abap-glossary/abenrepository_object_glosry.md) that in the context of a [Switch Framework](../../abap-glossary/abenswitch_framework_glosry.md) is determines whether another [repository object](../../abap-glossary/abenrepository_object_glosry.md) or a component of a repository object (such as a screen element) is visible and used in a system. This also applies in particular to [enhancements](../../abap-glossary/abenenhancement_glosry.md) of the ABAP Enhancement Framework. In most cases, extensions can be switched on whenever they are defined in a [package](../../abap-glossary/abenpackage_glosry.md) to which a switch is assigned. A switch can have the status *on*, *off*, or *stand-by*. Switches are created in transaction `SFW1` and switched in transaction `SFW5` using business functions. See also [conflict switch](../../abap-glossary/abenconflict_switch_glosry.md).

**Switch Framework**

`SFW` for short. Framework for the externally controlling the visibility of [repository objects](../../abap-glossary/abenrepository_object_glosry.md), their components, or [enhancements](../../abap-glossary/abenenhancement_glosry.md) using [switches](../../abap-glossary/abenswitch_glosry.md).

**sXML library**

Global [interfaces](../../abap-glossary/abenglobal_interface_glosry.md) and [classes](../../abap-glossary/abenglobal_class_glosry.md) for handling [XML](../../abap-glossary/abenxml_glosry.md) data in different [formats](../abap-data-interchange-formats/abenabap_sxml_lib_formats.md). The *serial* XML Library provides XML readers and XML writers for various sources and targets. The classes and interfaces in sXML Library start with the prefixes `CL_SXML` or `IF_SXML`.

**SXPG framework**

A framework for calling operating system statements of the current [AS instance](../../abap-glossary/abenas_instance_glosry.md) [host computer](../../abap-glossary/abenhost_computer_glosry.md) from ABAP programs, based on the transaction `SM69` and [function modules](../../abap-glossary/abenfunction_module_glosry.md) in the [function pool](../../abap-glossary/abenfunction_pool_glosry.md) SXPG

**synchronous Remote Function Call**

sRFC for short. Remote function call in which the calling program waits for the end of processing of the remotely called function.

**synchronous update**

Update in which update function modules of high priority are executed in the update work process whereby the calling program waits for completion. Synchronous updates are started via [`COMMIT WORK`](../abap-database-access/abapcommit.md) with the addition `AND WAIT` and are executed in a separate update session.

**system client**

Special [client](../../abap-glossary/abenclient_glosry.md) in [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) with the [client ID](../../abap-glossary/abenclient_identifier_glosry.md) *000*. The system client is used to execute system-specific [system programs](../../abap-glossary/abensystem_program_glosry.md).

**system code page**

[Code page](../../abap-glossary/abencodepage_glosry.md) released for use on an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). In the current release, each system is a [Unicode system](../../abap-glossary/abenunicode_system_glosry.md), that is, a [single code page system](../../abap-glossary/abensingle_codepage_system_glosry.md) with the system code page [UTF-16](../../abap-glossary/abenutf16_glosry.md) with a platform-dependent [byte order](../../abap-glossary/abenbyte_order_glosry.md). The programming language ABAP supports the subset [UCS-2](../../abap-glossary/abenucs2_glosry.md) without [surrogates](../../abap-glossary/abensurrogates_glosry.md). The system code page of a single code page system is always the code page of the [text environment](../../abap-glossary/abentext_environment_glosry.md) of an [internal session](../../abap-glossary/abeninternal_session_glosry.md).

**system date**

[Local date](../../abap-glossary/abenlocal_date_glosry.md) in the [system time zone](../../abap-glossary/abensystem_time_zone_glosry.md) of the [AS ABAP](../../abap-glossary/abenas_abap_glosry.md).

**system ID**

SID for short. Identification or name of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) and therefore also the ID or name of the [ABAP system](../../abap-glossary/abenabap_system_glosry.md). A system ID consists of three characters and is the content of the [system field](../../abap-glossary/abensystem_field_glosry.md) [`sy-sysid`](../abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md).

**system log**

Central storage location for the recording of system errors on an [AS instance](../../abap-glossary/abenas_instance_glosry.md). It is called via transaction code `SM21`.

**system time zone**

Client-dependent [time zone](../../abap-glossary/abentime_zone_glosry.md) of the [system time](../../abap-glossary/abensystem_time_glosry.md) in [AS ABAP](../../abap-glossary/abenas_abap_glosry.md).

**temperature column**

Column of a [database table](../../abap-glossary/abendatabase_table_glosry.md) called `_DATAAGING`. On an [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md), the values in this column determine whether [data aging](../../abap-glossary/abendata_aging_glosry.md) data is current or obsolete.

**tenant**

Independent organizational unit that rents a hosting system from a provider. A tenant's [application programs](../../abap-glossary/abenapplication_program_glosry.md) are run along with those of other tenants on the hosting system. The applications from different tenants in a system are kept separate by means of tenant isolation and are based on the multitenancy concept. On a multitenancy [AS ABAP](../../abap-glossary/abenas_abap_glosry.md), tenants are mapped to [application clients](../../abap-glossary/abenapplication_client_glosry.md). Multitenancy is not supported in the current release.

**text environment language**

Language of the [text environment](../../abap-glossary/abentext_environment_glosry.md) of the current [internal session](../../abap-glossary/abeninternal_session_glosry.md). The text environment language is the content of the [system field](../../abap-glossary/abensystem_field_glosry.md) [`sy-langu`](../abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md). At the beginning of each internal session, it is the [logon language](../../abap-glossary/abenlogon_language_glosry.md) and can be set explicitly with `SET LOCALE LANGUAGE`.

**text file**

File on the [host computer](../../abap-glossary/abenhost_computer_glosry.md) of an [AS instance](../../abap-glossary/abenas_instance_glosry.md) that has been opened using the addition `TEXT` of the statement `OPEN DATASET`. In a text file, the content is handled as text in the [character representation](../../abap-glossary/abenchar_representation_glosry.md) that was chosen when the file was opened.

**transaction code**

Twenty-character name that is connected with a dynpro, another transaction code, or a [method](../../abap-glossary/abenmethod_glosry.md) of an [ABAP program](../../abap-glossary/abenabap_program_glosry.md) and is used to execute programs. Transaction codes linked with dynpros are possible for executable programs, module pools, and [function pools](../../abap-glossary/abenfunction_pool_glosry.md). Parameter transactions and variant transactions are linked with other transaction codes. Transaction codes linked with methods are allowed for all program types that contain methods. Transaction codes are maintained and administrated using transaction code `SE93`.

**transaction owner**

The transaction owner is the leading application and is responsible for orchestrating the transaction. It is also responsible for triggering commit and rollback commands.

**transactional Remote Function Call**

tRFC for short. Obsolete remote function call in which the function called remotely is registered for execution and started using the statement [`COMMIT WORK`](../abap-database-access/abapcommit.md).

**Transformation Editor**

Tool in the ABAP Workbench for creating [XSLT programs](../../abap-glossary/abenxslt_program_glosry.md) or [Simple Transformations](../../abap-glossary/abensimple_transformation_glosry.md) in [transformation source code](../../abap-glossary/abenxslt_program_glosry.md). Called using the transaction code `STRANS`.

**transformation source code**

[Source code](../../abap-glossary/abensource_code_glosry.md) of [XSLT programs](../../abap-glossary/abenxslt_program_glosry.md) and [Simple Transformations](../../abap-glossary/abensimple_transformation_glosry.md) processed in the Transformation Editor.

**tRFC**

*-\>* transactional remote function call

**trusted system**

[AS ABAP](../../abap-glossary/abenas_abap_glosry.md) that is classified as a trusted caller of remote function calls in a trusting system. The trusted system provides the RFC client. The system is classified in transaction `SMT1`. Trusted systems log on to the trusting system without passing a password. User-specific logon data is checked in the trusting system.

**trusting system**

[AS ABAP](../../abap-glossary/abenas_abap_glosry.md) that trusts a trusted system in calls using Remote Function Call. The trusting system provides the RFC server. The trusting systems can be listed in a trusted system using transaction code `SMT2`.

**Unicode system**

[Single code page system](../../abap-glossary/abensingle_codepage_system_glosry.md) in which characters are encoded in a [Unicode character representation](../../abap-glossary/abenunicode_char_represent_glosry.md). The [system code page](../../abap-glossary/abensystem_codepage_glosry.md) of a Unicode system is [UTF-16](../../abap-glossary/abenutf16_glosry.md) with platform-dependent [byte order](../../abap-glossary/abenbyte_order_glosry.md) of which the ABAP programming language supports the subset covered by [UCS-2](../../abap-glossary/abenucs2_glosry.md). All ABAP programs in a Unicode system must have the [ABAP language version](../../abap-glossary/abenabap_version_glosry.md) [Standard ABAP](../../abap-glossary/abenstandard_abap_glosry.md). In the current [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) release, only Unicode systems are supported.

**unrestricted ABAP language version**

[ABAP language version](../../abap-glossary/abenabap_version_glosry.md) that is not restricted regarding the ABAP language scope and access to other repository objects. [Standard ABAP](../../abap-glossary/abenstandard_abap_glosry.md) is unrestricted. See also [restricted ABAP language versions](../../abap-glossary/abenrestricted_version_glosry.md).

**update lock**

Area lock on an area instance version in the shared objects memory. An update lock enables to change an existing area instance version.

**update session**

[User session](../../abap-glossary/abenuser_session_glosry.md) for synchronous and asynchronous updates. Local updates are not carried out in a separate update session.

**user interface**

All the control elements of an [ABAP program](../../abap-glossary/abenabap_program_glosry.md). The user interface can be implemented by different technologies, such as the browser-based [SAPUI5](../../abap-glossary/abensapui5_glosry.md), Web Dynpro, or the user-installed SAP GUI.

**user master record**

A user master record must exist that a user can [log on](../../abap-glossary/abenlogon_glosry.md) to an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). The record determines which actions an [ABAP user](../../abap-glossary/abenabap_user_glosry.md) with a certain [user name](../../abap-glossary/abenuser_name_glosry.md) is allowed to execute and which [authorizations](../../abap-glossary/abenauthorization_glosry.md) are granted. Default settings, such as [format settings](../../abap-glossary/abenformat_setting_glosry.md) for [character strings](../../abap-glossary/abencharacter_string_glosry.md) are also recorded in the user master record. User master records are maintained in transaction `SU01`.

**user memory**

Memory area of the current [AS instance](../../abap-glossary/abenas_instance_glosry.md) to which all [ABAP sessions](../../abap-glossary/abenabap_session_glosry.md) of a [user session](../../abap-glossary/abenuser_session_glosry.md) have access. [ABAP programs](../../abap-glossary/abenabap_program_glosry.md) have access to SPA/GPA parameters stored in the user memory. ABAP daemons access the subarea ABAP daemon memory of the user memory

**user session**

Status of an [AS instance](../../abap-glossary/abenas_instance_glosry.md) that exists between an [ABAP user](../../abap-glossary/abenabap_user_glosry.md) [logging on](../../abap-glossary/abenlogon_glosry.md) to the [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) and off again. During the user session, the user can work with the AS ABAP. A user session is characterized by the [user name](../../abap-glossary/abenuser_name_glosry.md), [client ID](../../abap-glossary/abenclient_identifier_glosry.md) ([current client](../../abap-glossary/abencurrent_client_glosry.md)), and [logon language](../../abap-glossary/abenlogon_language_glosry.md). There are different types of user sessions for different purposes and they can be opened in different ways- Each user session is linked with at least one and up to 16 [ABAP sessions](../../abap-glossary/abenabap_session_glosry.md). The user memory is assigned to a user session has its own memory area.

**Web Application Builder**

Tool in ABAP Workbench for creating Business Server Pages. It can be called via *Create -\> `BSP` Library -\> `BSP` Application* in Object Navigator.

**Web Dynpro**

Technology used to create platform-independent Web-based interfaces, based on the Model View Controller (MVC) approach. Before the introduction of [SAPUI5](../../abap-glossary/abensapui5_glosry.md), Web Dynpro for ABAP was the standard SAP `UI` technology for developing Web applications on [Application Server ABAP](../../abap-glossary/abenas_abap_glosry.md). Web Dynpros for ABAP are created in the Web Dynpro Explorer.

**Web Dynpro Explorer**

Tool in the ABAP Workbench for creating Web Dynpros. Called via *Create -\> Web Dynpro -\> ...* in Object Navigator.

**WebSocket protocol**

`WSP` for short. A TCP based protocol for the bidirectional communication between a client and a server. Using ABAP Push Channels, an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) can be used as a server and as a client for the WebSocket protocol.

[***-\>* More about**](http://tools.ietf.org/html/rfc6455)

**work process**

Component of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) [AS instance](../../abap-glossary/abenas_instance_glosry.md). Work processes execute applications written in ABAP. There are various types of work processes for different applications: dialog, enqueue, background, spool, and update work processes. Each work process is registered for the complete runtime of an AS instance on to the [standard database](../../abap-glossary/abenstandard_db_glosry.md) of [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) as a [database user](../../abap-glossary/abendatabase_user_glosry.md) using a [standard connection](../../abap-glossary/abenstandard_db_connection_glosry.md). In dialog processing, a work process is assigned to an [ABAP program](../../abap-glossary/abenabap_program_glosry.md) for the duration of a dialog step.

**write lock**

Area lock on an area instance version in the shared objects memory. A write lock enables to create a new area instance version.

**XML reader**

[Instance](../../abap-glossary/abeninstance_glosry.md) of a [class](../../abap-glossary/abenclass_glosry.md) of the [sXML Library](../../abap-glossary/abensxml_library_glosry.md) that implements the [interface](../../abap-glossary/abenoo_intf_glosry.md) `IF_SXML_READER`. An XML reader enables the parsing of [XML](../../abap-glossary/abenxml_glosry.md) data in different [formats](../abap-data-interchange-formats/abenabap_sxml_lib_formats.md).

**XML writer**

[Instance](../../abap-glossary/abeninstance_glosry.md) of a [class](../../abap-glossary/abenclass_glosry.md) of the [sXML Library](../../abap-glossary/abensxml_library_glosry.md) that implements the [interface](../../abap-glossary/abenoo_intf_glosry.md) `IF_SXML_WRITER`. An XML writer enables the rendering of [XML](../../abap-glossary/abenxml_glosry.md) in different [formats](../abap-data-interchange-formats/abenabap_sxml_lib_formats.md).

**XSL transformation**

Program written in [XSLT](../../abap-glossary/abenxslt_glosry.md) to transform [XML](../../abap-glossary/abenxml_glosry.md) data. XSL transformations of the [repository](../../abap-glossary/abenrepository_glosry.md) are edited in Transformation Editor and called using the statement [`CALL TRANSFORMATION`](../abap-data-interchange-formats/abapcall_transformation.md). Implicit [serializations](../../abap-glossary/abenserialization_glosry.md) and [deserializations](../../abap-glossary/abendeserialization_glosry.md) allow the direct transformation of ABAP data into XML formats and vice versa.

**XSLT program**

*-\>* [XSL transformation](../../abap-glossary/abenxsl_transformation_glosry.md)
