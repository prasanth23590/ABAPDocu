---
title: "ABAP Language Glossary"
source_file: abenabala_glossary.html
section: "ABAP Programming Language"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Language Glossary

In the following, terms of the [ABAP Glossary](../abap-glossary/abenabap_glossary.md) are listed, that are relevant for the [ABAP Language](abenabap_reference.md).

**ABAP**

Advanced Business Application Programming. ABAP in the actual sense is the name of the [ABAP language](../abap-glossary/abenabala_glosry.md), but in a broader sense it is also the term for the entire [ABAP technology](../abap-glossary/abenabap_techno_glosry.md) provided for and by an [ABAP system](../abap-glossary/abenabap_system_glosry.md).

**ABAP Cloud**

ABAP development model for state-of-the-art, cloud-ready and upgrade-stable solutions. Compared to [classic ABAP](../abap-glossary/abenclassic_abap_glosry.md), ABAP Cloud uses the [ABAP technology](../abap-glossary/abenabap_techno_glosry.md) with the following restrictions:

- The [ABAP language version](../abap-glossary/abenabap_version_glosry.md) is restricted to the [restricted ABAP language version](../abap-glossary/abenrestricted_version_glosry.md) [ABAP for Cloud Development](../abap-glossary/abenabap_for_cloud_dev_glosry.md).

- Access to other [repository objects](../abap-glossary/abenrepository_object_glosry.md) is restricted to APIs that are [released](../abap-glossary/abenreleased_api_glosry.md) for [ABAP for Cloud Development](../abap-glossary/abenabap_for_cloud_dev_glosry.md).

- Only [ABAP development tools for Eclipse (ADT)](../abap-glossary/abenadt_glosry.md) can be used. There is no access to SAP GUI.

The transactional programming model for ABAP Cloud is [RAP](../abap-glossary/abenrap_glosry.md).

ABAP Cloud is supported in all SAP products that are based on ABAP technology. It is fully or partly mandatory in

- [SAP BTP ABAP environment](../abap-glossary/abensap_btp_abap_env_glosry.md)

- [SAP S/4HANA Cloud Public Edition](../abap-glossary/abensap_s4hana_cpub_glosry.md)

- [SAP S/4HANA Cloud Private Edition](../abap-glossary/abensap_s4hana_cpriv_glosry.md)

On the [ABAP Platform](../abap-glossary/abenabap_platform_glosry.md) of [SAP S/4HANA](../abap-glossary/abensap_s4hana_glosry.md) it is available besides classic ABAP.

**ABAP command injection**

Injection of malicious ABAP statements by an attacker. An ABAP statement injection is possible if statements or parts of statements that are transferred from the outside and then are passed to the [runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) go unchecked.

**ABAP Compiler**

ABAP Compiler creates byte code as intermediate code when generating a program from [ABAP source code](../abap-glossary/abenabap_source_code_glosry.md) that is stored in the database as a program load and is loaded into the [PXA](../abap-glossary/abenpxa_glosry.md) if required.

**ABAP connection**

Secondary or [service connection](../abap-glossary/abenservice_connection_glosry.md) that is shared by [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md), Native SQL and [AMDP](../abap-glossary/abenabap_managed_db_proc_glosry.md).

[***-\>* More about**](abap-database-access/abendb_connections_using.md)

**ABAP contract checks**

ABAP contract checks summarize the following checks:

- [RAP BO contract](../abap-glossary/abenrap_bo_contract_glosry.md) checks: Check for violations of [RAP BO consumer](../abap-glossary/abenrap_bo_consumer_glosry.md) and [RAP BO provider](../abap-glossary/abenrap_bo_provider_glosry.md) implementations.

- [Transactional contract](../abap-glossary/abentransactional_contract_glosry.md) checks: Are implemented in the [controlled SAP LUW](../abap-glossary/abencontrolled_sap_luw_glosry.md) concept. Check for transactional consistency violations in a [transactional phase](../abap-glossary/abentr_phase_glosry.md).

**ABAP daemon class**

Global subclass of `CL_ABAP_DAEMON_EXT_BASE`. The instances of an ABAP daemon class are ABAP daemons created by the ABAP daemon framework, each of which are executed in a separate ABAP daemon session. An ABAP daemon class implements interface methods inherited from the superclass to react to ABAP daemon events.

**ABAP daemon framework**

ADF for short. A framework based on [classes](../abap-glossary/abenclass_glosry.md) and [interfaces](../abap-glossary/abenoo_intf_glosry.md) for using ABAP daemons. ADF includes APIs both for communication with ABAP daemons in [ABAP programs](../abap-glossary/abenabap_program_glosry.md) and for handling events using ABAP daemons in ABAP daemon sessions.

**ABAP daemon handle**

ABAP daemon framework object that implements the [interface](../abap-glossary/abenoo_intf_glosry.md) `IF_ABAP_DAEMON_HANDLE`. An ABAP daemon handle enables users to send PCP messages to the daemon using the `SEND` method.

**ABAP daemon manager**

The class `CL_ABAP_DAEMON_CLIENT_MANAGER`. The static methods of the ABAP daemon manager are used to create and use ABAP daemons in [ABAP programs](../abap-glossary/abenabap_program_glosry.md).

**ABAP data type**

*-\>* [data type](../abap-glossary/abendata_type_glosry.md)

**ABAP Database Connectivity**

ADBC for short. Class-based API for the Native SQL interface. ADBC enables object-oriented execution of dynamically specified Native SQL.

**ABAP enumerated type**

[Enumerated type](../abap-glossary/abenenum_type_glosry.md) in ABAP. An [enumerated variable](../abap-glossary/abenenumerated_variable_glosry.md) of an enumerated type can only accept the [enumerated values](../abap-glossary/abenenumerated_value_glosry.md) defined there that exist as the content of [enumerated constants](../abap-glossary/abenenumerated_constant_glosry.md) or components of an [enumerated structure](../abap-glossary/abenenumerated_structure_glosry.md). An enumerated type is defined with [`TYPES BEGIN OF ENUM`](abap-declarations/abaptypes_enum.md).

**ABAP expression**

An [expression](../abap-glossary/abenexp_glosry.md) in an [ABAP statement](../abap-glossary/abenabap_statement_glosry.md). Expressions can be, for example, calls of [built-in functions](../abap-glossary/abenbuiltin_function_glosry.md) or [functional method calls](../abap-glossary/abenfunctional_method_call_glosry.md), [declaration expressions](../abap-glossary/abendeclaration_position_glosry.md), [logical expressions](../abap-glossary/abenlogical_expression_glosry.md) constructed from [relational expressions](../abap-glossary/abenrelational_expression_glosry.md), [constructor expressions](../abap-glossary/abenconstructor_expression_glosry.md), [table expressions](../abap-glossary/abentable_expression_glosry.md), and [calculation expressions](../abap-glossary/abencalculation_expression_glosry.md). See also [SQL Expression](../abap-glossary/abensql_expression_glosry.md).

**ABAP file interface**

The ABAP file interface makes it possible to process files on the [host computers](../abap-glossary/abenhost_computer_glosry.md) of [AS instances](../abap-glossary/abenas_instance_glosry.md) using ABAP statements.

**ABAP for Cloud Development**

[Restricted ABAP language version](../abap-glossary/abenrestricted_version_glosry.md) with restricted language scope and restricted access to [released APIs](../abap-glossary/abenreleased_api_glosry.md). In ABAP for Cloud Development, [client isolation](../abap-glossary/abenclient_isolation_glosry.md) is enforced. ABAP for Cloud Development is the [ABAP language version](../abap-glossary/abenabap_version_glosry.md) for [ABAP Cloud](../abap-glossary/abenabap_cloud_glosry.md).

**ABAP for Key Users**

[Restricted ABAP language version](../abap-glossary/abenrestricted_version_glosry.md) with restricted language scope and restricted access to [released APIs](../abap-glossary/abenreleased_api_glosry.md) for [enhancements](../abap-glossary/abenenhancement_glosry.md) made by key users at dedicated enhancement points. ABAP for Key Users is available in the special enhancement tools for key users.

**ABAP function**

A [function](../abap-glossary/abenfunction_glosry.md) in ABAP can either be predefined as a [built-in function](../abap-glossary/abenbuiltin_function_glosry.md) or can be defined as a [functional method](../abap-glossary/abenfunctional_method_glosry.md). In an [ABAP program](../abap-glossary/abenabap_program_glosry.md), an ABAP function can be called by an [expression](../abap-glossary/abenexpression_glosry.md) by using its name at an [operand position](../abap-glossary/abenoperand_position_glosry.md). During the evaluation of the expression, the function is called and its result is used as an [operand](../abap-glossary/abenoperand_glosry.md).

**ABAP kernel**

Part of the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) which is primarily programmed in C/C++. In particular, [ABAP statements](../abap-glossary/abenabap_statement_glosry.md) are implemented by C functions in the ABAP kernel. When an ABAP statement is executed, the corresponding C functions or the ABAP kernel are called.

**ABAP keyword**

[ABAP word](../abap-glossary/abenabap_word_glosry.md) that introduces an [ABAP statement](../abap-glossary/abenabap_statement_glosry.md). In combination with other ABAP words or [ABAP operands](../abap-glossary/abenabap_operand_glosry.md), it defines an [ABAP language element](../abap-glossary/abenabap_language_element_glosry.md).

**ABAP language**

The ABAP language or [ABAP programming language](../abap-glossary/abenabap_programming_langu_glosry.md) or [ABAP](../abap-glossary/abenabap_glosry.md) for short is the main programming language of the [ABAP development environment (ABAP DE)](../abap-glossary/abenabap_dev_envir_glosry.md). It is used as the programming interface of an [Application Server ABAP](../abap-glossary/abenas_abap_glosry.md) (AS ABAP) of an [ABAP system](../abap-glossary/abenabap_system_glosry.md). Depending on the program paradigm [ABAP Cloud](../abap-glossary/abenabap_cloud_glosry.md) or [classic ABAP](../abap-glossary/abenclassic_abap_glosry.md), different [ABAP language versions](../abap-glossary/abenabap_version_glosry.md) can be used.

**ABAP language element**

[ABAP keyword](../abap-glossary/abenabap_keyword_glosry.md) or combination of an ABAP keyword with one or more following [ABAP words](../abap-glossary/abenabap_word_glosry.md) or [ABAP operands](../abap-glossary/abenabap_operand_glosry.md). An ABAP language element uniquely describes the semantics of an [ABAP statement](../abap-glossary/abenabap_statement_glosry.md). Examples of different ABAP language elements are `GET BIT`, `GET TIME`, `DELETE itab`, or `DELETE dbtab`. ABAP language elements can be enhanced using [ABAP language element additions](../abap-glossary/abenabap_language_elmnt_add_glosry.md).

**ABAP language element addition**

[ABAP word](../abap-glossary/abenabap_word_glosry.md) or combination of multiple ABAP words. A language element addition can be used in [ABAP statements](../abap-glossary/abenabap_statement_glosry.md) as an addition to a suitable [ABAP language element](../abap-glossary/abenabap_language_element_glosry.md). Examples of different ABAP language element additions are `WITH KEY` and `WITH TABLE KEY`.

**ABAP language version**

[Program property](../abap-glossary/abenprogram_property_glosry.md) that determines the language scope and the syntax rules of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) and other [repository objects](../abap-glossary/abenrepository_object_glosry.md). See also [unrestricted](../abap-glossary/abenunrestricted_version_glosry.md) and [restricted ABAP language versions](../abap-glossary/abenrestricted_version_glosry.md).

**ABAP literal**

An [unnamed data object](../abap-glossary/abenunnamed_data_object_glosry.md) defined by textual specification of a value in the [ABAP source code](../abap-glossary/abenabap_source_code_glosry.md) of an [ABAP program](../abap-glossary/abenabap_program_glosry.md). In the general ABAP language, untyped [numeric literals](../abap-glossary/abennumeric_literal_glosry.md) and untyped [character literals](../abap-glossary/abencharacter_literal_glosry.md) are available. A [literal operator](../abap-glossary/abenliteral_operator_glosry.md) enables the linking of multiple literals. See also:

- [anonymous data object](../abap-glossary/abenanonymous_data_object_glosry.md)

- [named data object](../abap-glossary/abennamed_data_object_glosry.md)

- [literal](../abap-glossary/abenliteral_glosry.md)

- [ABAP SQL literal](../abap-glossary/abenabap_sql_literal_glosry.md)

**ABAP Managed Database Procedures**

AMDP for short. Class-based framework for managing and calling [stored procedures](../abap-glossary/abenstored_procedure_glosry.md) or [database procedures](../abap-glossary/abendatabase_procedure_glosry.md) as [AMDP procedures](../abap-glossary/abenamdp_procedure_glosry.md) in [AS ABAP](../abap-glossary/abenas_abap_glosry.md).

**ABAP Objects**

Constituent of the ABAP programming language that allows object-oriented programming based on [classes](../abap-glossary/abenclass_glosry.md) and [interfaces](../abap-glossary/abenoo_intf_glosry.md).

**ABAP operand**

A syntax element of an [ABAP statement](../abap-glossary/abenabap_statement_glosry.md) at an [operand position](../abap-glossary/abenoperand_position_glosry.md). At [read](../abap-glossary/abenread_position_glosry.md) and [write positions](../abap-glossary/abenwrite_position_glosry.md), [data objects](../abap-glossary/abendata_object_glosry.md) or [expressions](../abap-glossary/abenexpression_glosry.md) can be specified. Besides that there are other operand positions, where types, callable units or other external resources such as [CDS entities](../abap-glossary/abencds_entity_glosry.md) or [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) can be specified as operands.

**ABAP program**

[Repository object](../abap-glossary/abenrepository_object_glosry.md) that contains [ABAP source code](../abap-glossary/abenabap_source_code_glosry.md) and has a program type. Additional components such as dynpros or the GUI status are assigned to an ABAP program.

**ABAP programming language**

*-\>* [ABAP language](../abap-glossary/abenabala_glosry.md)

**ABAP release**

Release of [ABAP](../abap-glossary/abenabap_glosry.md) ([ABAP technology](../abap-glossary/abenabap_techno_glosry.md) including the [ABAP language](../abap-glossary/abenabala_glosry.md) and its other programming languages). The counting of the releases is done by release numbers such as 7.57, 7.58, 8.16, ... 7.95, 7.96, 9.12, ... These release numbers are based on the technical release names of the associated software component `SAP_BASIS` as it can be found in system field `sy-saprl`. ABAP is not released standalone but is shipped together with SAP products such as [SAP BTP ABAP environment](../abap-glossary/abensap_btp_abap_env_glosry.md), [SAP S/4HANA Cloud Public Edition](../abap-glossary/abensap_s4hana_cpub_glosry.md) and [SAP S/4HANA](../abap-glossary/abensap_s4hana_glosry.md), [SAP S/4HANA Cloud Private Edition](../abap-glossary/abensap_s4hana_cpriv_glosry.md). These products have other release numbers that can be mapped to the ABAP releases. The releases of the underlying [ABAP kernel](../abap-glossary/abenkernel_glosry.md) are also counted differently and can also be mapped to the ABAP releases.

**ABAP runtime environment**

*-\>* [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md)

**ABAP runtime framework**

Also called ABAP runtime environment. Hardware- and operating system-independent platform (virtual machine) of an [ABAP program](../abap-glossary/abenabap_program_glosry.md). Processes of the ABAP runtime framework control the execution of an ABAP program by calling the [processing blocks](../abap-glossary/abenprocessing_block_glosry.md) of the program. [ABAP statements](../abap-glossary/abenabap_statement_glosry.md) are implemented in the [ABAP kernel](../abap-glossary/abenkernel_glosry.md) of the ABAP runtime framework. The ABAP runtime framework is provided by the [Application Server ABAP](../abap-glossary/abenas_abap_glosry.md) and, therefore, [ABAP programs](../abap-glossary/abenabap_program_glosry.md) can only be executed in AS ABAP.

**ABAP source code**

[Source code](../abap-glossary/abensource_code_glosry.md) for [ABAP programs](../abap-glossary/abenabap_program_glosry.md) consisting of [ABAP statements](../abap-glossary/abenabap_statement_glosry.md) and [comments](../abap-glossary/abencomment_glosry.md). Created and maintained in the ABAP Editor or with the [ABAP development tools for Eclipse (ADT)](../abap-glossary/abenadt_glosry.md). ABAP source code is compiled by the ABAP Compiler when the program is activated. It can be broken down into individual [repository objects](../abap-glossary/abenrepository_object_glosry.md) by using [include programs](../abap-glossary/abeninclude_program_glosry.md).

**ABAP statement**

A complete sentence of the ABAP programming language. Consists of [tokens](../abap-glossary/abentoken_glosry.md) and is closed with a period.

**ABAP type**

[Data type](../abap-glossary/abendata_type_glosry.md) or [object type](../abap-glossary/abendata_type_glosry.md) organized in the [ABAP type hierarchy](../abap-glossary/abenabap_type_hierarchy_glosry.md).

**ABAP type hierarchy**

Also ABAP type system. Hierarchy of all possible [ABAP types](../abap-glossary/abenabap_type_glosry.md).

**ABAP type system**

*-\>* [ABAP type hierarchy](abap-data-types-and-data-objects/abentype_hierarchy.md).

**ABAP word**

Word of the ABAP programming language. ABAP words are the [tokens](../abap-glossary/abentoken_glosry.md) of an [ABAP statement](../abap-glossary/abenabap_statement_glosry.md) and express its semantics. In ABAP statements, ABAP words are either used as [ABAP keywords](../abap-glossary/abenabap_keyword_glosry.md) or as additions. A single ABAP word can be both a keyword and an addition. Combinations of ABAP words form [ABAP language elements](../abap-glossary/abenabap_language_element_glosry.md) or [ABAP language element additions](../abap-glossary/abenabap_language_elmnt_add_glosry.md).

**absolute type name**

[Type name](../abap-glossary/abentype_name_glosry.md), constructed as a path in a [character string](../abap-glossary/abencharacter_string_glosry.md), that uniquely specifies the [context](../abap-glossary/abenobj_context_glosry.md) of a [data type](../abap-glossary/abendata_type_glosry.md), a [class](../abap-glossary/abenclass_glosry.md), or an [interface](../abap-glossary/abenoo_intf_glosry.md), and which can be used in dynamic type specifications. The [RTTS](../abap-glossary/abenrun_time_type_services_glosry.md) can determine the absolute type name of any [object](../abap-glossary/abenobject_glosry.md). See also [relative type name](../abap-glossary/abenrelative_type_name_glosry.md).

**abstract**

Term in [ABAP Objects](../abap-glossary/abenabap_objects_glosry.md). An abstract [class](../abap-glossary/abenclass_glosry.md) cannot be instantiated. An abstract [method](../abap-glossary/abenmethod_glosry.md) can only be implemented in [subclasses](../abap-glossary/abensubclass_glosry.md) of its class. A non-abstract class or method is [concrete](../abap-glossary/abenconcrete_glosry.md).

**ADBC**

*-\>* ABAP Database Connectivity

**addition assignment operator**

[Calculation assignment operator](../abap-glossary/abencalc_assignment_op_glosry.md) `+=` that adds values in an assignment.

**administration client**

Special [client](../abap-glossary/abenclient_glosry.md) in [AS ABAP](../abap-glossary/abenas_abap_glosry.md) whose [client ID](../abap-glossary/abenclient_identifier_glosry.md) is stored in a profile parameter in multitenancy systems. The administration client is where administrative [system programs](../abap-glossary/abensystem_program_glosry.md) can run. When you [log on](../abap-glossary/abenlogon_glosry.md) to an administration client of a multitenancy AS ABAP, you are not subject to the restrictions caused by tenant isolation.

**alias name**

A name that is assigned as a substitute name to an element, an object, etc. The following alias names can be defined in ABAP:

- The statement [`ALIASES`](abap-declarations/abapaliases.md) can be used to declare an alias name for an [interface component](../abap-glossary/abeninterface_component_glosry.md) in a [class](../abap-glossary/abenclass_glosry.md) or in a [compound interface](../abap-glossary/abencompound_interface_glosry.md).

- The addition [`ALIAS`](abap-declarations/abaptypes_primary_key.md) can be used to specify an alias for the [primary table key](../abap-glossary/abenprimary_key_glosry.md) and [secondary table key](../abap-glossary/abensecondary_key_glosry.md) when declaring an [internal table](../abap-glossary/abeninternal_table_glosry.md).

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md), the addition `AS` can be used to define aliases for columns of the result set in a [`SELECT`](abap-database-access/abapselect_list.md) list or for data sources in the [`FROM`](abap-database-access/abapfrom_clause.md) clause.

- In [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), the addition `AS` can be used to define aliases for elements in the `SELECT` list or for [CDS associations](../abap-glossary/abencds_association_glosry.md).

**alignment gap**

Bytes within a [structure](../abap-glossary/abenstructure_glosry.md) that are inserted either before [structure components](../abap-glossary/abenstructure_component_glosry.md) with alignment requirements or before the end of the structure to provide the necessary [alignment](../abap-glossary/abenalignment_glosry.md). Alignment gaps contribute to the length of a structure. The binary content of alignment gaps is not defined and must not be evaluated.

**AMDP**

*-\>* [ABAP Managed Database Procedures](../abap-glossary/abenabap_managed_db_proc_glosry.md)

**AMDP class**

[Global class](../abap-glossary/abenglobal_class_glosry.md) with one or more [tag interfaces](../abap-glossary/abentag_interface_glosry.md) `IF_AMDP_MARKER_ ...` for [ABAP Managed Database Procedures](../abap-glossary/abenabap_managed_db_proc_glosry.md). An AMDP class can contain [AMDP methods](../abap-glossary/abenamdp_method_glosry.md) for different [database systems](../abap-glossary/abendatabase_system_glosry.md).

**AMDP function**

[Database function](../abap-glossary/abendatabase_function_glosry.md) of the [SAP HANA database](../abap-glossary/abenhana_database_glosry.md) that is implemented in an [AMDP function implementation](../abap-glossary/abenamdp_function_method_glosry.md) of an [AMDP class](../abap-glossary/abenamdp_class_glosry.md) and is replicated from there to the [database system](../abap-glossary/abendatabase_system_glosry.md). There are [AMDP table functions](../abap-glossary/abenamdp_table_function_glosry.md) or [AMDP scalar functions](../abap-glossary/abenamdp_scalar_function_glosry.md). See also [AMDP procedure](../abap-glossary/abenamdp_procedure_glosry.md).

**AMDP function implementation**

[AMDP method](../abap-glossary/abenamdp_method_glosry.md) with [return value](../abap-glossary/abenreturn_value_glosry.md) that is indicated by [`BY DATABASE FUNCTION`](abap-database-access/abapmethod_by_db_proc.md) in the [implementation part](../abap-glossary/abenimplementation_part_glosry.md) of the [class](../abap-glossary/abenclass_glosry.md). AMDP functions are implemented in an [AMDP function](../abap-glossary/abenamdp_function_glosry.md) implementation. An AMDP function implementation for an [AMDP scalar function](../abap-glossary/abenamdp_scalar_function_glosry.md) can be called in ABAP programs like a regular [functional method](../abap-glossary/abenfunctional_method_glosry.md). An AMDP function implementation for an [AMDP table function](../abap-glossary/abenamdp_table_function_glosry.md), on the other hand, is generally used to implement a [CDS table function](../abap-glossary/abencds_table_function_glosry.md). It can be used as a data source of [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) read statements using the [CDS entity](../abap-glossary/abencds_entity_glosry.md), but cannot be called in ABAP programs. See also [AMDP procedure implementation](../abap-glossary/abenamdp_procedure_method_glosry.md).

**AMDP macro**

Syntax specified in the implementation of an [AMDP method](../abap-glossary/abenamdp_method_glosry.md) in [SQLScript](../abap-glossary/abensql_script_glosry.md), which is replaced by the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) when the [database procedure](../abap-glossary/abendatabase_procedure_glosry.md) is generated on the [database](../abap-glossary/abendatabase_glosry.md) in compliance with the assigned rules.

**AMDP method**

[Method](../abap-glossary/abenmethod_glosry.md) of an [AMDP class](../abap-glossary/abenamdp_class_glosry.md) that is flagged as an [AMDP procedure implementation](../abap-glossary/abenamdp_procedure_method_glosry.md) using [`BY DATABASE PROCEDURE`](abap-database-access/abapmethod_by_db_proc.md) or as an [AMDP function implementation](../abap-glossary/abenamdp_function_method_glosry.md) using [`BY DATABASE FUNCTION`](abap-database-access/abapmethod_by_db_proc.md) in the [implementation part](../abap-glossary/abenimplementation_part_glosry.md) of the class.

**AMDP procedure**

[Database procedure](../abap-glossary/abendatabase_procedure_glosry.md) implemented in an [AMDP procedure implementation](../abap-glossary/abenamdp_procedure_method_glosry.md) of an [AMDP class](../abap-glossary/abenamdp_class_glosry.md) and replicated from there to the [database system](../abap-glossary/abendatabase_system_glosry.md). See [AMDP function](../abap-glossary/abenamdp_function_glosry.md).

**AMDP procedure implementation**

[AMDP method](../abap-glossary/abenamdp_method_glosry.md) without [return value](../abap-glossary/abenreturn_value_glosry.md) that is indicated by [`BY DATABASE PROCEDURE`](abap-database-access/abapmethod_by_db_proc.md) in the [implementation part](../abap-glossary/abenimplementation_part_glosry.md) of the class. In an AMDP procedure implementation, [AMDP procedures](../abap-glossary/abenamdp_procedure_glosry.md) are implemented in a database-specific language as [ABAP Managed Database Procedures](../abap-glossary/abenabap_managed_db_proc_glosry.md). AMDP procedure implementations are called in ABAP just like regular methods and passed to the database system using the Native SQL interface and executed here. See also [AMDP function implementation](../abap-glossary/abenamdp_procedure_glosry.md).

**AMDP scalar function**

[Scalar function](../abap-glossary/abenscalar_function_glosry.md) of the [SAP HANA database](../abap-glossary/abenhana_database_glosry.md) implemented in an [AMDP function implementation](../abap-glossary/abenamdp_function_method_glosry.md) of an [AMDP class](../abap-glossary/abenamdp_class_glosry.md) and replicated from here to the [database system](../abap-glossary/abendatabase_system_glosry.md).

**AMDP table function**

[Table function](../abap-glossary/abentable_function_glosry.md) of the [SAP HANA database](../abap-glossary/abenhana_database_glosry.md) implemented in an [AMDP function implementation](../abap-glossary/abenamdp_function_method_glosry.md) of an [AMDP class](../abap-glossary/abenamdp_class_glosry.md) and replicated from here to the [database system](../abap-glossary/abendatabase_system_glosry.md).

**anonymous data object**

[Unnamed data object](../abap-glossary/abenunnamed_data_object_glosry.md) that is created using the statement [`CREATE DATA`](abap-creating-objects-and-values/abapcreate_data.md), the [instance operator](../abap-glossary/abeninstance_operator_glosry.md) [`NEW`](abap-creating-objects-and-values/abenconstructor_expression_new.md), or the addition [`NEW`](abap-database-access/abapselect_into_target.md) of the [`INTO`](abap-database-access/abapinto_clause.md) clause of a [query](../abap-glossary/abenasql_query_glosry.md) and can be addressed using [reference variables](../abap-glossary/abenreference_variable_glosry.md) or [field symbols](../abap-glossary/abenfield_symbol_glosry.md). Anonymous data objects are stored in the [heap](../abap-glossary/abenheap_glosry.md). An anonymous data object is kept alive by [heap references](../abap-glossary/abenheap_reference_glosry.md) or by field symbols that address it or part of it. See also [named data object](../abap-glossary/abennamed_data_object_glosry.md) and [literal](../abap-glossary/abenabap_literal_glosry.md).

**application program**

[ABAP program](../abap-glossary/abenabap_program_glosry.md) that is part of the business applications executed on [AS ABAP](../abap-glossary/abenas_abap_glosry.md). Application programs generally only work with the data of the current [application client](../abap-glossary/abenapplication_client_glosry.md) that is stored in [application tables](../abap-glossary/abenapplication_table_glosry.md).

**aRFC**

*-\>* asynchronous remote function call

**arithmetic expression**

Formulation of an arithmetic calculation.

- In general ABAP, an [arithmetic expression](abap-processing-internal-data/abapcompute_arith.md) is a [calculation expression](../abap-glossary/abencalculation_expression_glosry.md). It is assigned a [calculation type](../abap-glossary/abencalculation_type_glosry.md) that is used to execute the calculation. The result of an arithmetic expression is a numeric value that exists in the calculation type. Arithmetic expressions occur in the [read positions of specific statements](abap-operands/abenoperands_expressions.md).

- In ABAP SQL, [arithmetic expressions](abap-database-access/abensql_arith.md) are [SQL expressions](../abap-glossary/abensql_expression_glosry.md).

- In ABAP CDS, [arithmetic expressions](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_arithmetic_expression_v2.md) can be used in the `SELECT` list of CDS view entities.

**arithmetic operator**

Combines two numeric [operands](../abap-glossary/abenoperand_glosry.md) in an [arithmetic expression](../abap-glossary/abenarithmetic_expression_glosry.md).

- In ABAP, arithmetic operators are [`+`](abap-processing-internal-data/abenarith_operators.md), [`-`](abap-processing-internal-data/abenarith_operators.md), [`*`](abap-processing-internal-data/abenarith_operators.md), [`/`](abap-processing-internal-data/abenarith_operators.md), [`DIV`](abap-processing-internal-data/abenarith_operators.md), [`MOD`](abap-processing-internal-data/abenarith_operators.md), and [`**`](abap-processing-internal-data/abenarith_operators.md). See the topic [`arith_exp` - Arithmetic Operators](abap-processing-internal-data/abenarith_operators.md) for further details.

- In ABAP SQL, arithmetic operators are [`+`](abap-database-access/abensql_arith.md), [`-`](abap-database-access/abensql_arith.md), [`*`](abap-database-access/abensql_arith.md), [`/`](abap-database-access/abensql_arith.md).

- In ABAP CDS, arithmetic operators are [`+`](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_arithmetic_expression_v2.md), [`-`](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_arithmetic_expression_v2.md), [`*`](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_arithmetic_expression_v2.md), [`/`](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_arithmetic_expression_v2.md).

**assertion**

Assertion in an [ABAP program](../abap-glossary/abenabap_program_glosry.md). An assertion is defined as a conditional [checkpoint](../abap-glossary/abencheckpoint_glosry.md) using the [`ASSERT`](abap-program-maintenance/abapassert.md) statement. Assertions are either always active or can be [activated](../abap-glossary/abenactivatable_checkpoint_glosry.md) by assigning them to a [checkpoint group](../abap-glossary/abencheckpoint_group_glosry.md). When an active assertion is reached, the corresponding condition is evaluated. If the condition is violated, the program terminates with a runtime error, accesses the [ABAP Debugger](../abap-glossary/abenabap_debugger_glosry.md), or creates a log entry. If a [checkpoint group](../abap-glossary/abencheckpoint_group_glosry.md) is assigned, the program behavior is controlled by the corresponding activation settings. Otherwise, the program is terminated.

**assignment**

Transfer of the value of a [data object](../abap-glossary/abendata_object_glosry.md), a [return value](../abap-glossary/abenreturn_value_glosry.md) or result of a [functional method](../abap-glossary/abenfunctional_method_glosry.md), a [built-in function](../abap-glossary/abenbuiltin_function_glosry.md), a [constructor expression](../abap-glossary/abenconstructor_expression_glosry.md), a [table expression](../abap-glossary/abentable_expression_glosry.md), or the result of a [calculation expression](../abap-glossary/abencalculation_expression_glosry.md) to a target data object. If the [data types](../abap-glossary/abendata_type_glosry.md) are [compatible](../abap-glossary/abencompatible_glosry.md), the content is copied unchanged. If they are incompatible and a suitable [conversion rule](../abap-glossary/abenconversion_rule_glosry.md) exists, the content is converted.

**assignment operator**

[Operator](../abap-glossary/abenoperator_glosry.md) for assigning the content of a [data object](../abap-glossary/abendata_object_glosry.md) to a [variable](../abap-glossary/abenvariable_glosry.md). The general assignment operator in ABAP is the equal sign ([`=`](abap-processing-internal-data/abenequals_operator.md)). The [casting operator](../abap-glossary/abencasting_operator_glosry.md) ([`?=`](abap-processing-internal-data/abapmove_cast.md)) is a special assignment operator. Furthermore, there is the [addition assignment operator](../abap-glossary/abenadd_assignment_op_glosry.md) ([`+=`](abap-processing-internal-data/abencalculation_assignments.md)), the [subtraction assignment operator](../abap-glossary/abensub_assignment_op_glosry.md) ([`-=`](abap-processing-internal-data/abencalculation_assignments.md)), the [multiplication assignment operator](../abap-glossary/abenmult_assignment_op_glosry.md) ([`*=`](abap-processing-internal-data/abencalculation_assignments.md)), the [division assignment operator](../abap-glossary/abendiv_assignment_op_glosry.md) ([`/=`](abap-processing-internal-data/abencalculation_assignments.md)), and the [concatenation assignment operator](../abap-glossary/abenconcat_assignment_op_glosry.md) ([`**=`](abap-processing-internal-data/abencalculation_assignment_string.md)) for [calculation assignments](../abap-glossary/abencalculation_assignment_glosry.md).

**asynchronous Remote Function Call**

aRFC for short. Remote function call that does not wait for the end of processing of the remotely called function.

**attribute**

[Data object](../abap-glossary/abendata_object_glosry.md) declared within a [class](../abap-glossary/abenclass_glosry.md) or an [interface](../abap-glossary/abenoo_intf_glosry.md). Attributes can be [instance attributes](../abap-glossary/abeninstance_attribute_glosry.md) or [static attributes](../abap-glossary/abenstatic_attribute_glosry.md).

**authorization check**

Checks whether the current [ABAP user](../abap-glossary/abenabap_user_glosry.md) has a specific [authorization](../abap-glossary/abenauthorization_glosry.md). For each [authorization field](../abap-glossary/abenauthorization_field_glosry.md) of an [authorization object](../abap-glossary/abenauthorization_object_glosry.md), the system checks a value against the corresponding entries in the [user master record](../abap-glossary/abenuser_master_record_glosry.md). [Check indicators](../abap-glossary/abencheck_indicator_glosry.md) control whether an authorization check takes place. Authorization checks are either implicit when programs are called, or explicit when the [ABAP statement](../abap-glossary/abenabap_statement_glosry.md) [`AUTHORITY-CHECK`](abap-authorizations/abapauthority-check.md) is used.

**background Remote Function Call**

bgRFC for short. Asynchronous remote function call for which the called RFMs can be executed transactionally and in a predefined call sequence. bgRFC replaces tRFC and qRFC apart from the no-send scenario of qRFC. The latter is replaced by the local data queue (LDQ).

**base type**

Technical storage type of [enumerated constants](../abap-glossary/abenenumerated_constant_glosry.md), [enumerated variables](../abap-glossary/abenenumerated_variable_glosry.md), and [CDS enumerated elements](../abap-glossary/abencds_enum_element_glosry.md). In ABAP CDS, the base type of an [enumerated type](../abap-glossary/abenenum_type_glosry.md) is also used for compatibility checks in cast expressions and in comparisons. In ABAP, the base type of an enumerated type can be used in special conversions using [`CONV`](abap-processing-internal-data/abenconv_constructor_enum.md). A base type is [flat](../abap-glossary/abenflat_glosry.md), [elementary](../abap-glossary/abenelementary_data_type_glosry.md), and has a maximum length of 16 bytes.

**batch input table**

[Internal table](../abap-glossary/abeninternal_table_glosry.md) of [line type](../abap-glossary/abenrow_type_glosry.md) `BDCDATA`, which contains the data for a dialog transaction in the same format as in a batch input session. Batch input tables can be specified after the addition `USING` of the statement `CALL TRANSACTION` when calling transactions.

**bgRFC**

*-\>* Background Remote Function Call

**binary floating point arithmetic**

Calculation with [binary floating point numbers](../abap-glossary/abenbinfloat_glosry.md). Can produce rounding errors because floating point numbers are not represented internally using the decimal system.

**binary floating point number**

[Numeric data object](../abap-glossary/abennumeric_data_object_glosry.md) of ABAP or elementary object of the database with a [binary floating point number type](../abap-glossary/abenbinfloat_type_glosry.md). Due to the internal representation as binary fractions, not every decimal number within the type's value range can be represented exactly by a binary floating point number.

**binary floating point number type**

[Numeric data type](../abap-glossary/abennumeric_data_type_glosry.md) used for the binary representation of numbers with mantissa and exponents. The associated [built-in ABAP type](../abap-glossary/abenbuiltin_abap_type_glosry.md) is [`f`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md). The [built-in DDIC type](../abap-glossary/abenbuiltin_ddic_type_glosry.md) is [`FLTP`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The internal representation is in accordance with the norm IEEE-754 (double precision) by one bit for the plus/minus sign, 11 bits for the binary exponent, and 52 bits for the mantissa, whereby [decimal numbers](../abap-glossary/abendecimal_number_glosry.md) can be represented by 17 [places](../abap-glossary/abenplace_glosry.md). A [data object](../abap-glossary/abendata_object_glosry.md) of a binary floating point number type is a [binary floating point number](../abap-glossary/abenbinfloat_glosry.md).

**binary stream**

[Stream](../abap-glossary/abenstream_glosry.md) for [byte-like](../abap-glossary/abenbyte_like_data_typ_glosry.md) data.

**bit expression**

Formulation of a binary operation in a [calculation expression](../abap-glossary/abencalculation_expression_glosry.md). The result of a bit expression is a byte-like value. Bit expressions occur in [read positions of specific statements](abap-operands/abenoperands_expressions.md).

**bit function**

[Built-in function](../abap-glossary/abenbuiltin_function_glosry.md) that processes individual bits of [byte chains](../abap-glossary/abenbyte_chain_glosry.md).

**bit operator**

Is applied to an [operand](../abap-glossary/abenoperand_glosry.md) or combines two operands of a [bit expression](../abap-glossary/abenbit_expression_glosry.md). The possible bit operators are [`BIT-NOT`](abap-processing-internal-data/abenbit_operators.md), [`BIT-AND`](abap-processing-internal-data/abenbit_operators.md), [`BIT-OR`](abap-processing-internal-data/abenbit_operators.md), and [`BIT-XOR`](abap-processing-internal-data/abenbit_operators.md).

**Boolean data object**

[Data object](../abap-glossary/abendata_object_glosry.md) used to register [truth values](../abap-glossary/abentruth_value_glosry.md). Boolean data objects are not supported in ABAP. Instead, a truth value can be evaluated as the return value of a [Boolean function](../abap-glossary/abenboole_function_glosry.md).

**Boolean function**

[Logical function](../abap-glossary/abenlogic_function_glosry.md) that analyzes a [logical expression](../abap-glossary/abenlogical_expression_glosry.md) and returns the [truth value](../abap-glossary/abentruth_value_glosry.md) in character-like or byte-like form.

**Boolean operator**

Negates or combines [logical expressions](../abap-glossary/abenlogical_expression_glosry.md). Boolean operators belong to the [logical operators](../abap-glossary/abenlogical_operator_glosry.md) that are used in [logical expressions](../abap-glossary/abenlogical_expression_glosry.md).

- In ABAP, the possible Boolean operators are [`NOT`](abap-program-flow-logic/abenlogexp_not.md), [`AND`](abap-program-flow-logic/abenlogexp_and.md), [`OR`](abap-program-flow-logic/abenlogexp_or.md), and [`EQUIV`](abap-program-flow-logic/abenlogexp_equiv.md).

- In ABAP SQL, the possible Boolean operators are `NOT`, `AND`, `OR`. For further details, see the topic [`sql_cond` - `AND`, `OR`, `NOT`, `( )`](abap-database-access/abenwhere_logexp_andornot.md).

- In ABAP CDS, the possible Boolean operators are `NOT`, `AND`, `OR`. For further details, see the topic [CDS DDL - CDS View Entity, `cds_cond`](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_conditional_expression_v2.md).

**Boolean value expression**

A Boolean value expression is a [logical expression](../abap-glossary/abenlogical_expression_glosry.md) that produces a [truth value](../abap-glossary/abentruth_value_glosry.md). It can be used in various [general expression positions](../abap-glossary/abengeneral_expr_position_glosry.md), such as on the right side of [assignments](../abap-glossary/abenassignment_glosry.md). Its use is limited to specific data types that can represent true and false values: `c`, `x`, and `n` of length 1, and numeric types.

**bound data type**

[Data type](../abap-glossary/abendata_type_glosry.md) that only exists as a property of a [data object](../abap-glossary/abendata_object_glosry.md). A bound data type has a [technical type name](../abap-glossary/abentechnical_type_name_glosry.md) that can be retrieved as part of an [absolute type name](../abap-glossary/abenabsolute_typename_glosry.md) by [RTTI](../abap-glossary/abenrun_time_type_identific_glosry.md). See also [standalone data type](../abap-glossary/abenstand-alone_data_type_glosry.md).

**boxed component**

Structured [component](../abap-glossary/abencomponent_glosry.md) of a [structure](../abap-glossary/abenstructure_glosry.md) or a [class](../abap-glossary/abenclass_glosry.md) or [interface](../abap-glossary/abenoo_intf_glosry.md) that is not stored at the location of the definition but is [deep](../abap-glossary/abendeep_glosry.md), meaning it is managed by an internal reference. Boxed components are a mixture of [static](../abap-glossary/abenstatic_data_object_glosry.md) and [dynamic data objects](../abap-glossary/abendynamic_data_object_glosry.md). Currently, [static boxes](../abap-glossary/abenstatic_box_glosry.md) are supported as boxed components.

**branch**

Also referred to as selection. [Control structure](../abap-glossary/abencontrol_structure_glosry.md) that can consist of multiple [statement blocks](../abap-glossary/abenstatement_block_glosry.md) that are defined using the keywords [`IF` - `ELSEIF` - `ELSE` - `ENDIF`](abap-program-flow-logic/abapif.md), [`CASE` - `WHEN` - `ENDCASE`](abap-program-flow-logic/abapcase.md), [`TRY` - `CATCH` - `CLEANUP` - `ENDTRY`](abap-program-flow-logic/abaptry.md) and are executed depending on conditions. Branches can be implemented in [operand positions](../abap-glossary/abenoperand_position_glosry.md) using [conditional expressions](../abap-glossary/abenconditional_expression_glosry.md).

**built-in ABAP type**

[Built-in](../abap-glossary/abenbuiltin_data_type_glosry.md) [elementary data type](../abap-glossary/abenelementary_data_type_glosry.md). The built-in ABAP types are: [`b`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`c`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md), [`d`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md), [`decfloat16`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`decfloat34`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`f`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`i`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`int8`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`n`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md), [`p`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`s`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`string`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md), [`t`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md), [`utclong`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md), [`x`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md), and [`xstring`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md).

**built-in data object**

[Data object](../abap-glossary/abendata_object_glosry.md) in an [ABAP program](../abap-glossary/abenabap_program_glosry.md) by the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) that is either permanently active or only in specific [contexts](../abap-glossary/abenobj_context_glosry.md). The built-in data objects are [system fields](../abap-glossary/abensystem_field_glosry.md), the [constant](../abap-glossary/abenconstant_glosry.md) [`space`](abap-built-in-types-data-objects-functions-and-constructors/abenspace.md), and the [self-reference](../abap-glossary/abenself_reference_glosry.md) [`me`](abap-built-in-types-data-objects-functions-and-constructors/abenme.md). The [structure](../abap-glossary/abenstructure_glosry.md) `screen` is obsolete.

**built-in data type**

[Data type](../abap-glossary/abendata_type_glosry.md) that is provided in an [ABAP program](../abap-glossary/abenabap_program_glosry.md) by the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md). The built-in data types are [built-in ABAP types](../abap-glossary/abenbuiltin_abap_type_glosry.md), [generic ABAP types](../abap-glossary/abengeneric_abap_type_glosry.md), [built-in data types](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) from [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md), and [CDS built-in types](../abap-glossary/abencds_built_in_type_glosry.md). The names of the elementary and generic built-in ABAP types are a subset of the [reserved names](../abap-glossary/abenabap_word_glosry.md) (except for internal types `b` and `s`, which cannot be used directly in a program).

**built-in function**

A predefined function in ABAP, ABAP SQL, and ABAP CDS.

- In ABAP, built-in functions can be used as [expressions](../abap-glossary/abenexpression_glosry.md) in [certain operand positions](abap-operands/abenoperands_expressions.md). [Numeric functions](../abap-glossary/abenmathematical_funktion_glosry.md), [string functions](../abap-glossary/abenstring_function_glosry.md), [table functions](../abap-glossary/abentable_function_glosry.md), and [byte chain functions](../abap-glossary/abenbyte_chain_function_glosry.md) that have a return value of the corresponding data type can be distinguished. [Description functions](../abap-glossary/abendescription_function_glosry.md) that provide information on data objects, are also available. The names of the built-in functions are a subset of the [reserved names](../abap-glossary/abenabap_word_glosry.md). For further details, see the topic [Built-In Functions](abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md).

- For ABAP SQL, [built-in functions](abap-database-access/abensql_builtin_func.md) are part of the [SQL expressions](../abap-glossary/abensql_expression_glosry.md).

- For built-in functions in ABAP CDS, see the topic [CDS built-in function](../abap-glossary/abencds_builtin_func_glosry.md).

[Actual parameters](../abap-glossary/abenactual_parameter_glosry.md) passed to the [formal parameters](../abap-glossary/abenformal_parameter_glosry.md) of built-in functions are called also called [arguments](../abap-glossary/abenargument_glosry.md) of the function.

**byte chain**

String or sequence of bytes. Content of any data object. However, direct access to the bytes of a byte chain is possible only in [byte-like data objects](../abap-glossary/abenbyte_like_data_object_glosry.md), or by using appropriately typed [field symbols](../abap-glossary/abenfield_symbol_glosry.md).

**byte chain function**

[Built in function](../abap-glossary/abenbuiltin_function_glosry.md) for processing [byte chains](../abap-glossary/abenbyte_chain_glosry.md).

**byte code**

Result of the generation of an ABAP program using the ABAP Compiler. The statements in the byte code are linked with C functions. When the [ABAP program](../abap-glossary/abenabap_program_glosry.md) is executed, the byte code is loaded into the [PXA](../abap-glossary/abenpxa_glosry.md) as program Load and is interpreted by the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) (virtual machine), whereby the associated C functions are called.

**byte field**

[Byte-like data object](../abap-glossary/abenbyte_like_data_object_glosry.md) of ABAP or elementary object of the database with a [byte field type](../abap-glossary/abenbyte_field_type_glosry.md).

**byte field type**

[Byte-like data type](../abap-glossary/abenbyte_like_data_typ_glosry.md) for storing [byte strings](../abap-glossary/abenbyte_string_glosry.md) of fixed length. The associated [built-in ABAP type](../abap-glossary/abenbuiltin_abap_type_glosry.md) is [`x`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md). The [built-in DDIC types](../abap-glossary/abenbuiltin_ddic_type_glosry.md) are [`RAW`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`LRAW`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). A [data object](../abap-glossary/abendata_object_glosry.md) of a byte field type is a [byte field](../abap-glossary/abenbyte_field_glosry.md).

**byte order**

Determines the order in which the binary representation of a number of the [data types](../abap-glossary/abendata_type_glosry.md) [`i`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`int8`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`decfloat16`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`decfloat34`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`f`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`s`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), or a character is stored in the memory. A distinction is made between [big](../abap-glossary/abenbig_endian_glosry.md) and [little endian](../abap-glossary/abenlittle_endian_glosry.md). In the former case, the system writes the byte with the highest level to the first position in the memory and in the latter case it writes the byte with the lowest level.

**byte sequence**

*-\>* [byte chain](../abap-glossary/abenbyte_chain_glosry.md)

**byte string**

[Byte-like data object](../abap-glossary/abenbyte_like_data_object_glosry.md) of ABAP or elementary object of the database with a [byte string type](../abap-glossary/abenbyte_string_type_glosry.md).

**byte string type**

[Byte-like data type](../abap-glossary/abenbyte_like_data_typ_glosry.md) for storing [byte chains](../abap-glossary/abenbyte_chain_glosry.md) of variable length. The associated [built-in ABAP type](../abap-glossary/abenbuiltin_abap_type_glosry.md) is [`xstring`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md). The [built-in DDIC type](../abap-glossary/abenbuiltin_ddic_type_glosry.md) is [`RAWSTRING`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). Internal administration takes place using an internal [reference](../abap-glossary/abenreference_glosry.md) and the data type is [deep](../abap-glossary/abendeep_glosry.md). A [data object](../abap-glossary/abendata_object_glosry.md) of a byte field type is a [byte string](../abap-glossary/abenbyte_string_glosry.md).

**byte-like data object**

[Data object](../abap-glossary/abendata_object_glosry.md) with a [byte-like data type](../abap-glossary/abenbyte_like_data_typ_glosry.md) whose content is interpreted as non-encoded.

**byte-like data type**

[Data type](../abap-glossary/abendata_type_glosry.md) that allows access to the unencoded bytes of [byte chains](../abap-glossary/abenbyte_chain_glosry.md). These data types are [byte field types](../abap-glossary/abenbyte_field_type_glosry.md) and [byte string types](../abap-glossary/abenbyte_string_type_glosry.md). The associated [generic data type](../abap-glossary/abengeneric_data_type_glosry.md) is [`xsequence`](abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md).

**byte-like expression**

Represents a [byte string](../abap-glossary/abenbyte_string_glosry.md). A byte-like expression is a [bit expression](../abap-glossary/abenbit_expression_glosry.md) or a [function](../abap-glossary/abenfunction_glosry.md), whose return value has a [byte-like data type](../abap-glossary/abenbyte_like_data_typ_glosry.md).

**calculation assignment**

[Assignment](../abap-glossary/abenassignment_glosry.md) using a [calculation assignment operator](../abap-glossary/abencalc_assignment_op_glosry.md) where a calculation is performed.

**calculation assignment operator**

Operator for a [calculation assignment](../abap-glossary/abencalculation_assignment_glosry.md). The following calculation assignment operators are available: [addition assignment operator](../abap-glossary/abenadd_assignment_op_glosry.md) ([`+=`](abap-processing-internal-data/abencalculation_assignments.md)), a [subtraction assignment operator](../abap-glossary/abensub_assignment_op_glosry.md) ([`-=`](abap-processing-internal-data/abencalculation_assignments.md)), a [multiplication assignment operator](../abap-glossary/abenmult_assignment_op_glosry.md) ([`*=`](abap-processing-internal-data/abencalculation_assignments.md)), a [division assignment operator](../abap-glossary/abendiv_assignment_op_glosry.md) ([`/=`](abap-processing-internal-data/abencalculation_assignments.md)), or a [concatenation assignment operator](../abap-glossary/abenconcat_assignment_op_glosry.md) ([`&&=`](abap-processing-internal-data/abencalculation_assignment_string.md)).

**calculation expression**

Calculates a value. Either an [arithmetic expression](../abap-glossary/abenarithmetic_expression_glosry.md), a [bit expression](../abap-glossary/abenbit_expression_glosry.md), or a [string expression](../abap-glossary/abenstring_expression_glosry.md). The three calculation expression types can be used simultaneously as operands of [relational expressions](../abap-glossary/abenrelational_expression_glosry.md), but they cannot be combined within a calculation expression.

**calculation length**

Property of a [bit expression](../abap-glossary/abenbit_expression_glosry.md) depending on the [byte-like data types](../abap-glossary/abenbyte_like_data_object_glosry.md) involved. The calculation length is the length in which the operands of the expression are processed.

**calculation type**

Property of an [arithmetic expression](../abap-glossary/abenarithmetic_expression_glosry.md) depending on the [numeric data types](../abap-glossary/abennumeric_data_type_glosry.md) involved. The calculation type determines the calculation rule used to evaluate an arithmetic expression. There are different rules for the possible calculation types `i`, `int8`, `p`, `decfloat34`, and `f`.

**calendar date**

Date for short. An exact day, week, or month of the Gregorian calendar. Valid content of a [date field](../abap-glossary/abendate_field_glosry.md).

**call sequence**

A call sequence is the set of programs whose [internal sessions](../abap-glossary/abeninternal_session_glosry.md) are loaded jointly into an [ABAP session](../abap-glossary/abenabap_session_glosry.md) by a sequence of calls using `SUBMIT ... AND RETURN` or `CALL TRANSACTION`. It is possible to return to the preceding program in the call sequence from every program. The first program in a call sequence is the top level transaction. The programs of a call sequence have collective access to the ABAP memory. A call sequence can be exited completely using the statement `LEAVE TO TRANSACTION`.

**case distinction**

[Control structure](../abap-glossary/abencontrol_structure_glosry.md) with the [control statement](../abap-glossary/abencontrol_statement_glosry.md) [`CASE`](abap-program-flow-logic/abapcase.md) or [`CASE TYPE OF`](abap-program-flow-logic/abapcase_type.md), [condition expression](../abap-glossary/abenconditional_expression_glosry.md) with the [conditional operator](../abap-glossary/abenconditional_operator_glosry.md) [`SWITCH`](abap-program-flow-logic/abenconditional_expression_switch.md), [`CASE`](abap-database-access/abensql_case.md) expression in [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md), or [`CASE`](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_case_expression_v2.md) expression in [CDS DDL](../abap-glossary/abencds_ddl_glosry.md). In a case distinction, the value of an [operand](../abap-glossary/abenoperand_glosry.md) determines which of multiple source code sections is executed. In the ABAP language, there are only [simple case distinctions](../abap-glossary/abensimple_case_glosry.md). In ABAP CDS and ABAP SQL, there are [simple case distinctions](../abap-glossary/abensimple_case_glosry.md) and [complex case distinctions](../abap-glossary/abencomplex_case_glosry.md).

**case function**

[Processing function](../abap-glossary/abenprocess_function_glosry.md) that makes a character string case-sensitive.

**cast**

In ABAP, see [casting](../abap-glossary/abencast_casting_glosry.md). In [SQL](../abap-glossary/abensql_glosry.md), a cast is a type conversion.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md), the operator [`CAST`](abap-database-access/abensql_cast.md) is used.

- In the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) of [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), the operator `CAST` is used (see [cast in CDS view entities](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_cast_expression_v2.md) or [cast in CDS DDIC-based views (obsolete)](../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_cast_expression_v1.md)).

**casting**

Handling of a [data object](../abap-glossary/abendata_object_glosry.md) by assuming a specific [data type](../abap-glossary/abendata_type_glosry.md). Explicit casting is possible in the statement [`ASSIGN`](abap-processing-internal-data/abapassign.md) with the addition [`ASSIGNING`](abap-processing-internal-data/abapread_table_outdesc.md) when processing internal tables, for some assignments of [actual parameters](../abap-glossary/abenactual_parameter_glosry.md) to [formal parameters](../abap-glossary/abenformal_parameter_glosry.md), and as a [downcast](../abap-glossary/abendown_cast_glosry.md) or [upcast](../abap-glossary/abenup_cast_glosry.md) in the [assignments](../abap-glossary/abenassignment_glosry.md) between [reference variables](../abap-glossary/abenreference_variable_glosry.md). An implicit casting sometimes takes place when handling [operands](../abap-glossary/abenoperand_glosry.md) in certain [operand positions](../abap-glossary/abenoperand_position_glosry.md).

**casting operator**

[Operator](../abap-glossary/abenoperator_glosry.md) for executing a [downcast](../abap-glossary/abendown_cast_glosry.md) for [reference variables](../abap-glossary/abenreference_variable_glosry.md). Casting operators are the special [assignment operator](../abap-glossary/abenassignment_operator_glosry.md) [`?=`](abap-processing-internal-data/abapmove_cast.md) and the [constructor operator](../abap-glossary/abenconstructor_operator_glosry.md) [`CAST`](abap-processing-internal-data/abenconstructor_expression_cast.md).

**catchable exception**

[Exception](../abap-glossary/abenexception_glosry.md) that can be handled in the program using the statements [`TRY - CATCH - ENDTRY`](abap-program-flow-logic/abaptry.md) without causing a [runtime error](../abap-glossary/abenruntime_error_glosry.md). Catchable exceptions are based on [exception classes](../abap-glossary/abenexception_class_glosry.md) and are implemented by [exception objects](../abap-glossary/abenexception_object_glosry.md). A catchable exception is raised either by the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) or by the statement [`RAISE EXCEPTION`](abap-program-flow-logic/abapraise_exception.md) in a program, or by the addition [`THROW`](abap-program-flow-logic/abenconditional_expression_result.md) in a [conditional expression](../abap-glossary/abenconditional_expression_glosry.md). Before the introduction of [class-based exceptions](../abap-glossary/abenclass_based_exception_glosry.md), catchable exceptions could be user-defined only in the interfaces of [function modules](../abap-glossary/abenfunction_module_glosry.md) and [methods](../abap-glossary/abenmethod_glosry.md) and raised using [`RAISE`](abap-program-flow-logic/abapraise_exception.md). Predefined catchable exceptions occurred as catchable runtime errors, now they are obsolete.

**catchable runtime error**

Exception situation in the runtime framework that can still be handled by the obsolete statement `CATCH SYSTEM-EXCEPTIONS`. Replaced by [class-based exceptions](../abap-glossary/abenclass_based_exception_glosry.md).

**CCDEF include**

[Include program](../abap-glossary/abeninclude_program_glosry.md) of a [class pool](../abap-glossary/abenclass_pool_glosry.md) that is included in front of the [declaration part](../abap-glossary/abendeclaration_part_glosry.md) of the [global class](../abap-glossary/abenglobal_class_glosry.md). It can be edited in the Class Builder by navigating to *Class-Relevant Local Definitions* and in [ADT](../abap-glossary/abenadt_glosry.md) by navigating to *Class-Relevant Local Types*. The internal name of the include program ends with `CCDEF`. See also [CCIMP include](../abap-glossary/abenccimp_glosry.md).

**chained attribute access**

[Chaining](../abap-glossary/abenchaining_glosry.md) in which multiple [functional methods](../abap-glossary/abenfunctional_method_glosry.md) or [constructor expressions](../abap-glossary/abenconstructor_expression_glosry.md) are linked via [component selectors](../abap-glossary/abencomponent_selector_glosry.md). The [return values](../abap-glossary/abenreturn_value_glosry.md) or results of the individual methods or expressions are each references to the next methods, respectively, and the return value of the last method references an [attribute](../abap-glossary/abenattribute_glosry.md) that is used as an [ABAP operand](../abap-glossary/abenabap_operand_glosry.md). See also [chained identifiers](../abap-glossary/abenchained_name_glosry.md).

**chained identifier**

[Chaining](../abap-glossary/abenchaining_glosry.md) in which a name for an [ABAP operand](../abap-glossary/abenabap_operand_glosry.md) is composed using [component selectors](../abap-glossary/abencomponent_selector_glosry.md). See also [chained attribute access](../abap-glossary/abenchained_attribute_acc_glosry.md).

**chained method call**

A [chaining](../abap-glossary/abenchaining_glosry.md) in which multiple [functional methods](../abap-glossary/abenfunctional_method_glosry.md) or [constructor expressions](../abap-glossary/abenconstructor_expression_glosry.md) are linked via [component selectors](../abap-glossary/abencomponent_selector_glosry.md). The [return values](../abap-glossary/abenreturn_value_glosry.md) of the individual methods are references to the next methods. A chained method call can either be executed as a [functional method call](abap-calling-and-exiting-program-units/abapcall_method_functional.md) or as a [standalone statement](abap-calling-and-exiting-program-units/abapcall_method_static_short.md).

**chained statement**

Abbreviated way of writing multiple [ABAP statements](../abap-glossary/abenabap_statement_glosry.md) with the same initial part. The identical initial part is specified once and closed using a colon (`:`). This is followed by the remaining parts separated by commas.

**chaining**

Composite specification of an [ABAP operand](../abap-glossary/abenabap_operand_glosry.md) in an [operand position](../abap-glossary/abenoperand_position_glosry.md) in which the individual components are chained using [component selectors](../abap-glossary/abencomponent_selector_glosry.md). Examples of possible chainings are [chained identifiers](../abap-glossary/abenchained_name_glosry.md), [chained method calls](../abap-glossary/abenchained_method_call_glosry.md), [chained attribute accesses](../abap-glossary/abenchained_attribute_acc_glosry.md), chainings of [table expressions](../abap-glossary/abentable_expression_glosry.md), and various combinations of all four.

**changing parameter**

*-\>* [input/output parameter](../abap-glossary/abeninput_output_parameter_glosry.md)

**character literal**

Also referred to as text literal. A [literal](../abap-glossary/abenabap_literal_glosry.md) with a [character-like data type](../abap-glossary/abencharlike_data_type_glosry.md) whose value is a [character string](../abap-glossary/abencharacter_string_glosry.md).

- In general ABAP, character literals are [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), character literals can be [typed literals](../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Character Literals in ABAP](abap-declarations/abenuntyped_character_literals.md)

- [Literals in ABAP SQL](abap-database-access/abenabap_sql_literals.md)

- [Literals in CDS](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_literal_v2.md)

**character stream**

[Stream](../abap-glossary/abenstream_glosry.md) for [character-like](../abap-glossary/abencharlike_data_type_glosry.md) data.

**character string**

String or sequence of characters. Content of a [character-like data object](../abap-glossary/abencharlike_data_object_glosry.md). Also referred to as a character sequence.

**character string expression**

String expression for short. Formulation of an operation with character-like operands in a [calculation expression](../abap-glossary/abencalculation_expression_glosry.md), the result of which is a [character string](../abap-glossary/abencharacter_string_glosry.md).

**character string function**

[Built-in function](../abap-glossary/abenbuiltin_function_glosry.md) that processes [character strings](../abap-glossary/abencharacter_string_glosry.md).

**character string template**

String template for short. A character string template creates a [character string](../abap-glossary/abencharacter_string_glosry.md) from literal text, embedded expressions, and [control characters](../abap-glossary/abencontrol_character_glosry.md) in a [string expression](../abap-glossary/abenstring_expression_glosry.md).

**character-like data object**

[Data object](../abap-glossary/abendata_object_glosry.md) that can be interpreted as character-like if its content is appropriate. Besides data objects with [character-like data types](../abap-glossary/abencharlike_data_type_glosry.md) or [date types](../abap-glossary/abendate_type_glosry.md) and [time types](../abap-glossary/abendate_type_glosry.md), [structures](../abap-glossary/abenstructure_glosry.md) with purely [flat](../abap-glossary/abenflat_glosry.md) character-like [structure components](../abap-glossary/abenstructure_component_glosry.md) can also be character-like in many [operand positions](../abap-glossary/abenoperand_position_glosry.md).

**character-like data type**

[Data type](../abap-glossary/abendata_type_glosry.md) whose [data objects](../abap-glossary/abendata_object_glosry.md) contain [characters](../abap-glossary/abencharacter_glosry.md) encoded according to the current [code page](../abap-glossary/abencodepage_glosry.md). The actual character-like data types are [text field type](../abap-glossary/abentext_field_type_glosry.md), [numeric text field type](../abap-glossary/abennumeric_text_field_type_glosry.md), and [text string type](../abap-glossary/abentext_string_type_glosry.md). [Date type](../abap-glossary/abendate_type_glosry.md) and [time type](../abap-glossary/abentime_type_glosry.md) are special character-like data types. The associated [generic data type](../abap-glossary/abengeneric_data_type_glosry.md) is [`clike`](abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md).

**character-like expression**

Represents a [string](../abap-glossary/abencharacter_string_glosry.md). A character-like expression is a [constructor expression](../abap-glossary/abenconstructor_glosry.md), a [string expression](../abap-glossary/abenstring_expression_glosry.md), a [table expression](../abap-glossary/abentable_expression_glosry.md), or a [function](../abap-glossary/abenfunction_glosry.md), the return value of which has a [character-like data type](../abap-glossary/abencharlike_data_type_glosry.md).

**character-like expression position**

[Character-like](../abap-glossary/abencharlike_position_glosry.md) [read position](../abap-glossary/abenread_position_glosry.md) in which, in addition to a [character-like data object](../abap-glossary/abencharlike_data_object_glosry.md), a [character-like expression](../abap-glossary/abencharlike_expression_glosry.md) can also be specified.

**character-like operand position**

[Read position](../abap-glossary/abenread_position_glosry.md) with character-like [operand type](../abap-glossary/abenoperand_type_glosry.md) in which a [character-like data object](../abap-glossary/abencharlike_data_object_glosry.md) that can be converted into the operand type can be specified. See also [character-like expression position](../abap-glossary/abencharlike_expr_position_glosry.md).

**checkpoint**

Superordinate term for [assertions](../abap-glossary/abenassertion_glosry.md), [breakpoints](../abap-glossary/abenbreakpoint_glosry.md), or [logpoints](../abap-glossary/abenlogpoint_glosry.md). The statements [`ASSERT`](abap-program-maintenance/abapassert.md), `BREAK-POINT`, and `LOG-POINT` for defining checkpoints are not operative but equip the program for test purposes. Inactive checkpoints are ignored during program execution.

**checkpoint group**

[Repository object](../abap-glossary/abenrepository_object_glosry.md) that can be used to group and activate [activatable checkpoints](../abap-glossary/abenactivatable_checkpoint_glosry.md). To create checkpoint groups and maintain the activation settings, use transaction `SAAB`. The activation settings of a checkpoint group are valid for all checkpoints assigned to the group. Settings for a set of checkpoint groups can be created using activation variants.

**class**

Template for [objects](../abap-glossary/abenobject_glosry.md) in [ABAP Objects](../abap-glossary/abenabap_objects_glosry.md). Defined with [`CLASS - ENDCLASS`](abap-declarations/abapclass.md), either as a [global class](../abap-glossary/abenglobal_class_glosry.md) in a [class pool](../abap-glossary/abenclass_pool_glosry.md) or as a [local class](../abap-glossary/abenlocal_class_glosry.md) in almost any [ABAP program](../abap-glossary/abenabap_program_glosry.md). The definition of a class comprises a [declaration part](../abap-glossary/abendeclaration_part_glosry.md) for the declaration of the [class components](../abap-glossary/abenclass_component_glosry.md) and an [implementation part](../abap-glossary/abenimplementation_part_glosry.md) for the implementation of the [methods](../abap-glossary/abenmethod_glosry.md).

**class component**

[Component](../abap-glossary/abencomponent_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md). Declared in the [declaration part](../abap-glossary/abendeclaration_part_glosry.md) of the class. Possible class components are: [Attributes](../abap-glossary/abenattribute_glosry.md), [methods](../abap-glossary/abenmethod_glosry.md), and [events](../abap-glossary/abenevent_glosry.md).

**class component selector**

Characters `=>`. Each visible [static component](../abap-glossary/abenstatic_component_glosry.md) `comp` of a [class](../abap-glossary/abenclass_glosry.md) `class` can be addressed with `class=>comp`.

**class library**

The class library consists of all [global](../abap-glossary/abenglobal_type_glosry.md) [object types](../abap-glossary/abenobject_type_glosry.md), namely of all [global classes](../abap-glossary/abenglobal_class_glosry.md) and [interfaces](../abap-glossary/abenglobal_interface_glosry.md).

**class pool**

[ABAP program](../abap-glossary/abenabap_program_glosry.md) that contains the definition of one [global class](../abap-glossary/abenglobal_class_glosry.md) and is loaded when the class is used. Does not support its own dynpros and the only possible [processing blocks](../abap-glossary/abenprocessing_block_glosry.md) are [methods](../abap-glossary/abenmethod_glosry.md). In addition to the global class, a class pool can contain further [local classes](../abap-glossary/abenlocal_class_glosry.md), that are defined in a [CCDEF include](../abap-glossary/abenccdef_glosry.md), [CCIMP include](../abap-glossary/abenccimp_glosry.md), or a [test include](../abap-glossary/abentest_include_glosry.md).

**class reference variable**

[Object reference variable](../abap-glossary/abenobject_refer_variable_glosry.md) whose [static type](../abap-glossary/abenstatic_type_glosry.md) is a [class](../abap-glossary/abenclass_glosry.md). A class reference variable can be used to access all visible components of an object.

**class-based exception**

[Catchable exception](../abap-glossary/abencatchable_exception_glosry.md), which is represented by an [exception object](../abap-glossary/abenexception_object_glosry.md) of an [exception class](../abap-glossary/abenexception_class_glosry.md). Class-based exceptions replace the obsolete catchable runtime errors and non-class-based exceptions. A class-based exception can either terminate the current context or be a [resumable exception](../abap-glossary/abenresumable_exception_glosry.md).

**classic ABAP**

ABAP development model for legacy solutions. Classic ABAP is based on the [ABAP technology](../abap-glossary/abenabap_techno_glosry.md) without restrictions regarding [ABAP language versions](../abap-glossary/abenabap_version_glosry.md), usage of tools or access to [repository objects](../abap-glossary/abenrepository_object_glosry.md). Classic ABAP is still supported by the [ABAP Platform](../abap-glossary/abenabap_platform_glosry.md) of [SAP S/4HANA](../abap-glossary/abensap_s4hana_glosry.md). See also [ABAP Cloud](../abap-glossary/abenabap_cloud_glosry.md).

**client-safe**

A [repository object](../abap-glossary/abenrepository_object_glosry.md) that accesses [client-dependent](../abap-glossary/abenclient_dependent_glosry.md) [SQL data sources](../abap-glossary/abensql_data_source_glosry.md) is client-safe, if it can access data of one [client](../abap-glossary/abenclient_glosry.md) only. Such repository objects support the concept of [client isolation](../abap-glossary/abenclient_isolation_glosry.md) for [AMDP methods](../abap-glossary/abenamdp_method_glosry.md):

- AMDP methods that have the [ABAP language version](../abap-glossary/abenabap_version_glosry.md) [ABAP for Cloud Development](../abap-glossary/abenabap_for_cloud_dev_glosry.md) or are a [released API](../abap-glossary/abenreleased_api_glosry.md) with a [C1 contract](../abap-glossary/abenc1_contract_glosry.md) or a [C4 contract](../abap-glossary/abenc4_contract_glosry.md) must be [client-safe](abap-database-access/abenamdp_client_safety.md) and must access client-safe objects only.

- For a [CDS entity](../abap-glossary/abencds_entity_glosry.md), an [annotation](../abap-glossary/abencds_annotation_glosry.md) [`ClientHandling.clientSafe`](../abap-core-data-services-abap-cds/abap-cds-annotations/abencds_1549616294_anno.md) can be specified that enforces checks that guarantee its client safety. For CDS entities that do not have this annotations but are [released APIs](../abap-glossary/abenreleased_api_glosry.md), the checks are done implicitly.

A repository object that accesses only [client-independent](../abap-glossary/abenclient_independent_glosry.md) SQL data sources is implicitly client-safe.

**cluster**

Grouping of different data in shared storage. Currently only used as [data clusters](../abap-glossary/abendata_cluster_glosry.md) in different storage media for [data objects](../abap-glossary/abendata_object_glosry.md). Before [ABAP release](../abap-glossary/abenabap_release_glosry.md) 7.73, also used as a table cluster for special [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) (cluster tables).

**comment**

Explanation inserted into the [ABAP source code](../abap-glossary/abenabap_source_code_glosry.md) that is ignored by the ABAP Compiler when the program is generated. Either a [comment line](../abap-glossary/abencomment_line_glosry.md) or an [line end comment](../abap-glossary/abenendline_comment_glosry.md). See also [pseudo comment](../abap-glossary/abenpseudo_comment_glosry.md).

**comment line**

Line in a program that contains nothing but a [comment](../abap-glossary/abencomment_glosry.md). A comment line is either completely identified as a comment by an asterisk `*` in the first position or is a line that contains nothing except a comment introduced by `"` in any position.

**common area**

Interface work area created by the obsolete addition `COMMON PART` of the statement [`DATA`](abap-declarations/abapdata.md).

**comparison**

[Relational expression](../abap-glossary/abenrelational_expression_glosry.md) that compares one or more [operands](../abap-glossary/abenoperand_glosry.md). Implemented in ABAP using [comparison expressions](../abap-glossary/abencomparison_expression_glosry.md).

**comparison expression**

[Relational expression](../abap-glossary/abenrelational_expression_glosry.md) that combines two or more [operands](../abap-glossary/abenoperand_glosry.md) using a [comparison operator](../abap-glossary/abencomp_operator_glosry.md) in accordance with certain [comparison rules](../abap-glossary/abencomparison_rule_glosry.md).

**comparison operator**

[Relational operator](../abap-glossary/abenrel_operator_glosry.md) that combines two or more [operands](../abap-glossary/abenoperand_glosry.md) of a [comparison expression](../abap-glossary/abencomparison_expression_glosry.md) or of an [SQL condition](../abap-glossary/abensql_cond_glosry.md).

**comparison rule**

Rule for performing [comparisons](../abap-glossary/abencomparison_glosry.md) between [data objects](../abap-glossary/abendata_object_glosry.md) or [expressions](../abap-glossary/abenexpression_glosry.md).

**comparison type**

Property of [comparison expressions](../abap-glossary/abencomparison_expression_glosry.md) whose [operands](../abap-glossary/abenoperand_glosry.md) have [elementary data types](../abap-glossary/abenelementary_data_type_glosry.md), including [calculation expressions](../abap-glossary/abencalculation_expression_glosry.md). The comparison type is determined from the operands and defines how the comparison is executed. The comparison type can be of any [built-in ABAP type](../abap-glossary/abenbuiltin_abap_type_glosry.md). Operands of another type are converted to the comparison type before the comparison.

**compatible**

Except for [reference variables](../abap-glossary/abenreference_variable_glosry.md), two non-[generic data types](../abap-glossary/abengeneric_data_type_glosry.md) are compatible if all their [technical properties](../abap-glossary/abentechnical_type_prpt_glosry.md) are the same. Any [data type](../abap-glossary/abendata_type_glosry.md) is compatible with a generic data type if the generic data type includes its technical properties. [Data objects](../abap-glossary/abendata_object_glosry.md) are compatible if their data types are compatible. Compatibility is the basis for checking the [typing](../abap-glossary/abentyping_glosry.md). In an [assignment](../abap-glossary/abenassignment_glosry.md) or [comparison](../abap-glossary/abencomparison_glosry.md) of compatible data objects, no conversion takes place.

**compilation unit**

ABAP program that can be compiled as a standalone program. Executable programs, module pools, [function pools](../abap-glossary/abenfunction_pool_glosry.md), [class pools](../abap-glossary/abenclass_pool_glosry.md), [interface pools](../abap-glossary/abeninterface_pool_glosry.md), subroutine pools, and [type pools](../abap-glossary/abentype_pool_glosry.md) are compilation units. In contrast, [include programs](../abap-glossary/abeninclude_program_glosry.md) are not compilation units but must be included in a compilation unit in order to be compiled. Compilation units that are implicitly modularized in multiple include programs by the development tools are called [master programs](../abap-glossary/abenmaster_program_glosry.md).

**complete data type**

[Data type](../abap-glossary/abendata_type_glosry.md) that is not [generic](../abap-glossary/abengeneric_data_type_glosry.md).

**complete typing**

[Typing](../abap-glossary/abentyping_glosry.md) in which the [data type](../abap-glossary/abendata_type_glosry.md) of a [formal parameter](../abap-glossary/abenformal_parameter_glosry.md) or a [field symbol](../abap-glossary/abenfield_symbol_glosry.md) is completely defined, and which is valid for dynamic access as well as static access.

**complex data type**

A [data type](../abap-glossary/abendata_type_glosry.md) that is made up of other data types. A complex data type is either a [structured data type](../abap-glossary/abenstructured_type_glosry.md), a [table type](../abap-glossary/abentable_type_glosry.md), or a [mesh type](../abap-glossary/abenmesh_type_glosry.md).

**component**

A component is a subunit of a [data type](../abap-glossary/abendata_type_glosry.md) or an [object type](../abap-glossary/abenobject_type_glosry.md):

- [structure component](../abap-glossary/abenstructure_component_glosry.md)

- [class component](../abap-glossary/abenclass_component_glosry.md)

- [interface component](../abap-glossary/abeninterface_component_glosry.md)

**component group**

Also [named include](../abap-glossary/abennamed_include_glosry.md). Group of [structure components](../abap-glossary/abenstructure_component_glosry.md) that are included from another [structure](../abap-glossary/abenstructure_glosry.md) under one name. The components can be addressed by this name.

**component interface**

[Interface](../abap-glossary/abenoo_intf_glosry.md) included in a [compound interface](../abap-glossary/abencompound_interface_glosry.md) by an [`INTERFACES`](abap-declarations/abapinterfaces.md) statement. A component interface can itself be a compound interface.

**component operator**

[Constructor operator](../abap-glossary/abenconstructor_operator_glosry.md) [`CORRESPONDING`](abap-processing-internal-data/abenconstructor_expr_corresponding.md) for component by component assignments between [structures](../abap-glossary/abenstructure_glosry.md) or between [internal tables](../abap-glossary/abeninternal_table_glosry.md) in [operand positions](../abap-glossary/abenoperand_position_glosry.md). By default, the mapping between the [structure components](../abap-glossary/abenstructure_component_glosry.md) is based on identical names and can also be defined using mapping rules.

**component selector**

Syntax that can be used to address [components](../abap-glossary/abencomponent_glosry.md) of higher units. There is the [structure component selector](../abap-glossary/abenstructure_component_sel_glosry.md) (`-`), the [class component selector](../abap-glossary/abenclass_component_select_glosry.md) (`=>`), the [interface component selector](../abap-glossary/abeninterface_comp_selector_glosry.md) (`~`), and the [object component selector](../abap-glossary/abenobject_component_select_glosry.md) (`->`). [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) provides the additional [column selector](../abap-glossary/abentable_comp_selector_glosry.md) `~`.

**compound interface**

Interface in which at least one [component interface](../abap-glossary/abencomponent_interface_glosry.md) is included in its declaration with [`INTERFACES`](abap-declarations/abapinterfaces_ifac.md). Also referred to as a nested interface.

**concatenation**

A concatenation merges the character-like or byte-like content of different operands into one result. Concatenations can be made using the [concatenation operator](../abap-glossary/abenconcatenation_operator_glosry.md), the [concatenation assignment operator](../abap-glossary/abenconcat_assignment_op_glosry.md), [concatenation functions](../abap-glossary/abenconcatenation_function_glosry.md), or the [`CONCATENATE`](abap-processing-internal-data/abapconcatenate.md) statement.

**concatenation assignment operator**

[Calculation assignment operator](../abap-glossary/abencalc_assignment_op_glosry.md) `&&=` that concatenates [strings](../abap-glossary/abencharacter_string_glosry.md) in an assignment.

**concatenation function**

[Processing function](../abap-glossary/abenprocess_function_glosry.md) used to concatenate the character-like lines of an [internal table](../abap-glossary/abeninternal_table_glosry.md).

**concatenation operator**

[String operator](../abap-glossary/abenstring_operator_glosry.md) [`&&`](abap-processing-internal-data/abenstring_operators.md) used to concatenate two character-like operands.

**concrete**

Term in [ABAP Objects](../abap-glossary/abenabap_objects_glosry.md). Concrete classes and methods are not [abstract](../abap-glossary/abenabstract_glosry.md).

**condense function**

[Processing function](../abap-glossary/abenprocess_function_glosry.md) that condenses a string.

**condensed indicator structure**

Special [indicator structure](../abap-glossary/abenindicator_structure_glosry.md) that is not a [substructure](../abap-glossary/abensubstructure_glosry.md) but the last component of a structure with a [byte field type](../abap-glossary/abenbyte_field_type_glosry.md). Here, the individual bits of the [byte field](../abap-glossary/abenbyte_field_glosry.md) serve as indicators for the preceding components.

**conditional expression**

[Constructor expression](../abap-glossary/abenconstructor_expression_glosry.md) with a [conditional operator](../abap-glossary/abenconditional_operator_glosry.md) that creates a value or raises a [class-based exception](../abap-glossary/abenclass_based_exception_glosry.md) depending on a [logical expression](../abap-glossary/abenlogical_expression_glosry.md) or a [case distinction](../abap-glossary/abencase_distinction_glosry.md).

**conditional operator**

[Constructor operator](../abap-glossary/abenconstructor_operator_glosry.md) [`COND`](abap-program-flow-logic/abenconditional_expression_cond.md) or [`SWITCH`](abap-program-flow-logic/abenconditional_expression_switch.md) for [conditional expressions](../abap-glossary/abenconditional_expression_glosry.md).

**constant**

In ABAP, a [named data object](../abap-glossary/abennamed_data_object_glosry.md) whose value cannot be changed during the runtime of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) or a [procedure](../abap-glossary/abenprocedure_glosry.md). In [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), constants appear as components of [CDS enumerated types](../abap-glossary/abencds_enum_type_glosry.md).

**constructor**

A special [method](../abap-glossary/abenmethod_glosry.md) in a [class](../abap-glossary/abenclass_glosry.md) that sets a defined initial value for the status ([attributes](../abap-glossary/abenattribute_glosry.md)) of the class or its [objects](../abap-glossary/abenobject_glosry.md). There is an [instance constructor](../abap-glossary/abeninstance_constructor_glosry.md) for [instance attributes](../abap-glossary/abeninstance_attribute_glosry.md) and a [static constructor](../abap-glossary/abenstatic_constructor_glosry.md) for [static attributes](../abap-glossary/abenstatic_attribute_glosry.md). The constructors always exist implicitly but nevertheless must be declared explicitly for separate implementations. Special [constructor expressions](../abap-glossary/abenconstructor_expression_glosry.md) also exist.

**constructor expression**

A constructor expression uses a [constructor operator](../abap-glossary/abenconstructor_operator_glosry.md) to create a result for a specified [type](../abap-glossary/abentype_glosry.md) and constructs its content.

**constructor operator**

[Operator](../abap-glossary/abenoperator_glosry.md) of a [constructor expression](../abap-glossary/abenconstructor_expression_glosry.md). Possible constructor operators are the [instance operator](../abap-glossary/abeninstance_operator_glosry.md) [`NEW`](abap-creating-objects-and-values/abenconstructor_expression_new.md), the [value operator](../abap-glossary/abenvalue_operator_glosry.md) [`VALUE`](abap-creating-objects-and-values/abenconstructor_expression_value.md), the [reference operator](../abap-glossary/abenreference_operator_glosry.md) [`REF`](abap-processing-internal-data/abenconstructor_expression_ref.md), the [lossless operator](../abap-glossary/abenlossless_operator_glosry.md) [`EXACT`](abap-processing-internal-data/abenconstructor_expression_exact.md), the [conversion operator](../abap-glossary/abenconversion_operator_glosry.md) [`CONV`](abap-processing-internal-data/abenconstructor_expression_conv.md), the [component operator](../abap-glossary/abencorresponding_operator_glosry.md) [`CORRESPONDING`](abap-processing-internal-data/abenconstructor_expr_corresponding.md), the [casting operator](../abap-glossary/abencasting_operator_glosry.md) [`CAST`](abap-processing-internal-data/abenconstructor_expression_cast.md), the [reduction operator](../abap-glossary/abenreduce_operator_glosry.md) [`REDUCE`](abap-program-flow-logic/abenconstructor_expression_reduce.md), the [filter operator](../abap-glossary/abenfilter_operator_glosry.md) [`FILTER`](abap-processing-internal-data/abenconstructor_expression_filter.md), and the [conditional operators](../abap-glossary/abenconditional_operator_glosry.md) [`COND`](abap-program-flow-logic/abenconditional_expression_cond.md) and [`SWITCH`](abap-program-flow-logic/abenconditional_expression_switch.md).

**context**

Contexts are obsolete [repository objects](../abap-glossary/abenrepository_object_glosry.md) that are composed of [key fields](../abap-glossary/abenkey_field_glosry.md) to be entered, relationships between these fields, and further fields that can be derived from them. They are defined [abstractly](../abap-glossary/abenabstract_glosry.md) in the Context Builder in the ABAP Workbench and used during runtime as temporary objects. Contexts can be processed with the statements `CONTEXTS`, `DEMAND`, and `SUPPLY`.

**control statement**

Statement used to define a [control structure](../abap-glossary/abencontrol_structure_glosry.md).

**control structure**

Means of structuring a [processing block](../abap-glossary/abenprocessing_block_glosry.md) in [statement blocks](../abap-glossary/abenstatement_block_glosry.md). Possible control structures are [sequence](../abap-glossary/abensequence_glosry.md), [branch](../abap-glossary/abenbranch_glosry.md), and [loop](../abap-glossary/abenloop_glosry.md) as well as special control structures for exception handling. Control structures can be nested, so that statement blocks can contain other control structures.

**conversion**

*-\>* [type conversion](../abap-glossary/abentype_conversion_glosry.md)

**conversion operator**

[Constructor operator](../abap-glossary/abenconstructor_operator_glosry.md) [`CONV`](abap-processing-internal-data/abenconstructor_expression_conv.md) used to convert a value to a [data type](../abap-glossary/abendata_type_glosry.md).

**conversion rule**

Rule for converting content during [assignments](../abap-glossary/abenassignment_glosry.md) between [incompatible](../abap-glossary/abencompatible_glosry.md) (but [convertible](../abap-glossary/abenconvertible_glosry.md)) [data objects](../abap-glossary/abendata_object_glosry.md).

**convertible**

Two different [data types](../abap-glossary/abendata_type_glosry.md) are convertible if a [conversion rule](../abap-glossary/abenconversion_rule_glosry.md) applies to them. Two [data objects](../abap-glossary/abendata_object_glosry.md) are convertible if their data types are convertible and their content allows the corresponding conversion. Data objects of [compatible](../abap-glossary/abencompatible_glosry.md) data types are assigned to each other without a conversion.

**data cluster**

Grouping of [data objects](../abap-glossary/abendata_object_glosry.md) for transient and persistent storage in a storage medium. A data cluster can be processed using the statements [`IMPORT`](abap-data-cluster/abapimport_data_cluster.md), [`EXPORT`](abap-data-cluster/abapexport_data_cluster.md), and `DELETE FROM`.

**data object**

[Instance](../abap-glossary/abeninstance_glosry.md) of a [data type](../abap-glossary/abendata_type_glosry.md). Exists in the [internal session](../abap-glossary/abeninternal_session_glosry.md) of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) or as a shared object in the [shared memory](../abap-glossary/abenshared_memory_glosry.md). Is either created as a [named](../abap-glossary/abennamed_data_object_glosry.md), statically declared data object (statement [`DATA`](abap-declarations/abapdata.md) and similar) when a program or [procedure](../abap-glossary/abenprocedure_glosry.md) is loaded, or dynamically as an [anonymous data object](../abap-glossary/abenanonymous_data_object_glosry.md) at runtime ( statement [`CREATE DATA`](abap-creating-objects-and-values/abapcreate_data.md) or [instance operator](../abap-glossary/abeninstance_operator_glosry.md) [`NEW`](abap-creating-objects-and-values/abenconstructor_expression_new.md)). In addition, the [literals](../abap-glossary/abenabap_literal_glosry.md) defined as part of the source code are also handled as data objects. The data type of a data object is always complete (not [generic](../abap-glossary/abengeneric_data_type_glosry.md)) and can be [bound](../abap-glossary/abenbound_data_type_glosry.md) or [standalone](../abap-glossary/abenstand-alone_data_type_glosry.md). See also [static data object](../abap-glossary/abenstatic_data_object_glosry.md) and [dynamic data object](../abap-glossary/abendynamic_data_object_glosry.md).

**data reference**

[Reference](../abap-glossary/abenreference_glosry.md) that points to a [data object](../abap-glossary/abendata_object_glosry.md) or a part of a data object. A non-initial data reference can be a [heap reference](../abap-glossary/abenheap_reference_glosry.md) or a [stack reference](../abap-glossary/abenstack_reference_glosry.md).

**data reference variable**

[Reference variable](../abap-glossary/abenreference_variable_glosry.md) for [data references](../abap-glossary/abendata_reference_glosry.md). The [static type](../abap-glossary/abenstatic_type_glosry.md) of a data reference variable is a [data type](../abap-glossary/abendata_type_glosry.md).

**data sink**

*-\>* [streaming data sink](../abap-glossary/abenstreaming_data_sink_glosry.md)

**data stream**

[Stream](../abap-glossary/abenstream_glosry.md) that is either directly connected to a [streaming data source](../abap-glossary/abenstreaming_data_source_glosry.md) as a [reader stream](../abap-glossary/abenreader_stream_glosry.md) or as a [writer stream](../abap-glossary/abenwriter_stream_glosry.md) directly with a [streaming data sink](../abap-glossary/abenstreaming_data_sink_glosry.md).

**data type**

Property of a [data object](../abap-glossary/abendata_object_glosry.md). ABAP interprets the content of a data object in accordance with its data type. Data types exist either as [bound](../abap-glossary/abenbound_data_type_glosry.md) data types as a property of data objects or as [standalone](../abap-glossary/abenstand-alone_data_type_glosry.md) data types. Standalone data types can be defined globally in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) or in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). Data types defined with [`TYPES`](abap-declarations/abaptypes.md) in an [ABAP program](../abap-glossary/abenabap_program_glosry.md) can be either local or global. The latter is true for non-private data types of [classes](../abap-glossary/abenclass_glosry.md) and [interfaces](../abap-glossary/abenoo_intf_glosry.md). The [generic data type](../abap-glossary/abengeneric_data_type_glosry.md) of all data types is [`data`](abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md).

**database program**

[ABAP program](../abap-glossary/abenabap_program_glosry.md) of a logical database, which provides other programs with data in a table work area and, in doing so, raises the reporting event `GET` with the statement `PUT`. The functionality of a database program is implemented in [subroutines](../abap-glossary/abensubroutine_glosry.md), which are called by the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) during the execution of an executable program or the [function module](../abap-glossary/abenfunction_module_glosry.md) `LDB_PROCESS`. The execution time of the individual subroutines is related to certain reporting and selection screen events.

**date type**

[Data type](../abap-glossary/abendata_type_glosry.md) [`d`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md) for saving a [calendar date](../abap-glossary/abencalendar_date_glosry.md) in a [date field](../abap-glossary/abendate_field_glosry.md).

**decimal floating point number**

[Numeric data object](../abap-glossary/abennumeric_data_object_glosry.md) of ABAP or elementary object of the database with a [decimal floating point number type](../abap-glossary/abendecfloat_type_glosry.md).

**decimal floating point number type**

[Numeric data type](../abap-glossary/abennumeric_data_type_glosry.md) for the decimal storage of numbers with mantissa and exponents. The associated [built-in ABAP types](../abap-glossary/abenbuiltin_abap_type_glosry.md) are [`decfloat16`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) and [`decfloat34`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md). The [built-in DDIC types](../abap-glossary/abenbuiltin_ddic_type_glosry.md) are [`DECFLOAT16`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DF16_DEC`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DF16_RAW`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DECFLOAT34`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DF34_DEC`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`DF34_RAW`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The internal representation follows the standard IEEE-754-2008, where [decimal numbers](../abap-glossary/abendecimal_number_glosry.md) with 16 or 34 [places](../abap-glossary/abenplace_glosry.md) are accurately represented in the mantissa. A decimal floating point number has an additional [scaling](../abap-glossary/abenscale_glosry.md) property. A [data object](../abap-glossary/abendata_object_glosry.md) of a decimal floating point number type is a [decimal floating point number](../abap-glossary/abendecfloat_glosry.md).

**decimal separator**

Separator between the integer part and fractional part of a [decimal number](../abap-glossary/abendecimal_number_glosry.md). Within an [ABAP program](../abap-glossary/abenabap_program_glosry.md), the [decimal point](../abap-glossary/abendecimal_point_glosry.md) is always used. The representation of the decimal separator in the output depends on according to the current [formatting setting](abap-language-environment/abencountry.md) of the [language environment](../abap-glossary/abenlanguage_environment_glosry.md) that can be set using `SET COUNTRY`. See also decimal comma and [decimal point](../abap-glossary/abendecimal_point_glosry.md).

**declaration**

Defines the properties of local program entities. [Data types](../abap-glossary/abendata_type_glosry.md), [data objects](../abap-glossary/abendata_object_glosry.md), [classes](../abap-glossary/abenclass_glosry.md), [interfaces](../abap-glossary/abenoo_intf_glosry.md), and [field symbols](../abap-glossary/abenfield_symbol_glosry.md) can be declared. Declarations are made either with [declaration statements](../abap-glossary/abendeclaration_statement_glosry.md) or as [inline declarations](../abap-glossary/abeninline_declaration_glosry.md) using [declaration expressions](../abap-glossary/abendeclaration_expression_glosry.md). The declared unit is visible statically as soon as it is declared and is valid throughout the entire [context](../abap-glossary/abenobj_context_glosry.md).

**declaration expression**

[Expression](../abap-glossary/abenexpression_glosry.md) in which a [declaration operator](../abap-glossary/abendeclaration_operator_glosry.md) is used to make an [inline declaration](../abap-glossary/abeninline_declaration_glosry.md) in a [declaration position](../abap-glossary/abendeclaration_position_glosry.md).

**declaration operator**

[Operator](../abap-glossary/abenoperator_glosry.md) used in a [declaration expression](../abap-glossary/abendeclaration_expression_glosry.md) to make an [inline declaration](../abap-glossary/abeninline_declaration_glosry.md).

**declaration part**

Part of the definition of a [class](../abap-glossary/abenclass_glosry.md) in which the [class components](../abap-glossary/abenclass_component_glosry.md) are declared.

**declaration position**

[Write-only position](../abap-glossary/abenwrite_only_position_glosry.md) in which a [declaration expression](../abap-glossary/abendeclaration_expression_glosry.md) can be specified for an [inline declaration](../abap-glossary/abeninline_declaration_glosry.md).

**declaration statement**

[ABAP statement](../abap-glossary/abenabap_statement_glosry.md) that performs a [declaration](../abap-glossary/abendeclaration_glosry.md).

**declarative statement**

*-\>* [declaration statement](../abap-glossary/abendeclaration_statement_glosry.md)

**deep**

Property of a [data type](../abap-glossary/abendata_type_glosry.md) in which the content of its [data object](../abap-glossary/abendata_object_glosry.md) is either a [reference](../abap-glossary/abenreference_glosry.md) that points to the actual content ([reference variables](../abap-glossary/abenreference_variable_glosry.md)), or is addressed internally using references ([internal tables](../abap-glossary/abeninternal_table_glosry.md), [strings](../abap-glossary/abenstring_glosry.md), and [boxed components](../abap-glossary/abenboxed_component_glosry.md)). See also [flat](../abap-glossary/abenflat_glosry.md).

**deep structure**

[Structure](../abap-glossary/abenstructure_glosry.md) that contains at least one [deep](../abap-glossary/abendeep_glosry.md) [structure component](../abap-glossary/abenstructure_component_glosry.md).

**deep table**

[Internal table](../abap-glossary/abeninternal_table_glosry.md) with a [deep](../abap-glossary/abendeep_glosry.md) [line type](../abap-glossary/abenrow_type_glosry.md).

**delayed update**

Procedure to create or update unique [secondary table keys](../abap-glossary/abensecondary_table_key_glosry.md) of [internal tables](../abap-glossary/abeninternal_table_glosry.md). After a modifying operation using [field symbols](../abap-glossary/abenfield_symbol_glosry.md) or [data references](../abap-glossary/abendata_reference_glosry.md), unique secondary table keys are not updated immediately; instead they are updated the next time the internal table is accessed. See also [direct update](../abap-glossary/abendirect_update_glosry.md) and [lazy update](../abap-glossary/abenlazy_update_glosry.md).

**dereferencing operator**

The special [operator](../abap-glossary/abenoperator_glosry.md) `->*` is used for dereferencing [data reference variables](../abap-glossary/abendata_reference_variable_glosry.md) at [operand positions](../abap-glossary/abenoperand_position_glosry.md).

**description function**

[Built-in function](../abap-glossary/abenbuiltin_function_glosry.md) that returns properties of [data objects](../abap-glossary/abendata_object_glosry.md). There are [description functions for character-like](abap-processing-internal-data/abendescriptive_functions.md), [table-like](abap-processing-internal-data/abenitab_functions.md), and [byte-like](abap-processing-internal-data/abendescriptive_functions_binary.md) arguments.

**development class**

*-\>* [package](../abap-glossary/abenpackage_glosry.md)

**direct update**

Procedure to create or update unique [secondary table keys](../abap-glossary/abensecondary_table_key_glosry.md) of [internal tables](../abap-glossary/abeninternal_table_glosry.md). After an insertion operation using [`INSERT`](abap-processing-internal-data/abapinsert_itab.md) or [`APPEND`](abap-processing-internal-data/abapappend.md), a modifying operating using [`MODIFY`](abap-processing-internal-data/abapmodify_itab.md), or a block operation in which the whole table body is filled in one go, unique secondary table keys are updated immediately. See also [delayed update](../abap-glossary/abendelayed_update_glosry.md) and [lazy update](../abap-glossary/abenlazy_update_glosry.md).

**division assignment operator**

[Calculation assignment operator](../abap-glossary/abencalc_assignment_op_glosry.md)`/=` that divides values in an assignment.

**downcast**

Also called narrowing cast. [Assignment](../abap-glossary/abenassignment_glosry.md) between [reference variables](../abap-glossary/abenreference_variable_glosry.md) in which the [static type](../abap-glossary/abenstatic_type_glosry.md) of the target variable is more specific than the static type of the source variable and the assignability is not checked until runtime. A downcast must always be performed explicitly. This is done using assignments with the [casting operator](../abap-glossary/abencasting_operator_glosry.md) ([`?=`](abap-processing-internal-data/abapmove_cast.md)) and [constructor expressions](../abap-glossary/abenconstructor_expression_glosry.md) with the casting operator [`CAST`](abap-processing-internal-data/abenconstructor_expression_cast.md). Downcasts are also still possible using the `INTO` addition of the statement [`WHEN TYPE`](abap-program-flow-logic/abapwhen_type.md) of a case distinction using [`CASE TYPE OF`](abap-program-flow-logic/abapcase_type.md). See also [upcast](../abap-glossary/abenup_cast_glosry.md).

**dynamic data object**

[Data object](../abap-glossary/abendata_object_glosry.md) for which all properties apart from the memory consumption are statically determined by the [data type](../abap-glossary/abendata_type_glosry.md). Dynamic data objects are [strings](../abap-glossary/abenstring_glosry.md) and [internal tables](../abap-glossary/abeninternal_table_glosry.md). They belong to the [deep data objects](../abap-glossary/abendeep_glosry.md). Structures that contain dynamic components are also dynamic data objects. All other data objects, except for [boxed components](../abap-glossary/abenboxed_component_glosry.md), are [static data objects](../abap-glossary/abenstatic_data_object_glosry.md). When dynamic data objects are accessed, [value semantics](../abap-glossary/abenvalue_semantics_glosry.md) apply.

**elementary data object**

[Data object](../abap-glossary/abendata_object_glosry.md) with an [elementary data type](../abap-glossary/abenelementary_data_type_glosry.md).

**embedded expression**

[General expression position](../abap-glossary/abengeneral_expr_position_glosry.md) enclosed in curly brackets `{}` within a [string template](../abap-glossary/abenstring_template_glosry.md).

**entry node**

A [mesh node](../abap-glossary/abenmesh_node_glosry.md) from which the evaluation of a [mesh association](../abap-glossary/abenmesh_association_glosry.md) starts. The entry node is not always the [start node](../abap-glossary/abenstart_node_glosry.md) of the association.

**enumerated constant**

A [constant](../abap-glossary/abenconstant_glosry.md) declared in the definition of an [enumerated type](../abap-glossary/abenenum_type_glosry.md) that contains an [enumerated value](../abap-glossary/abenenumerated_value_glosry.md) of the enumerated type.

In ABAP, an enumerated constant is a special [enumerated object](../abap-glossary/abenenumerated_object_glosry.md). See also [enumerated structure](../abap-glossary/abenenumerated_structure_glosry.md).

In ABAP CDS, an enumerated constant is a special [enumerated element](../abap-glossary/abencds_enum_element_glosry.md).

- [Enumerated types in ABAP](abap-processing-internal-data/abenenumerated_types_usage.md)

- [Enumerated Types in ABAP CDS](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_enumeration_types.md)

**enumerated object**

[Data object](../abap-glossary/abendata_object_glosry.md) with an [enumerated type](../abap-glossary/abenenum_type_glosry.md). An enumerated object can only contain the [enumerated values](../abap-glossary/abenenumerated_value_glosry.md) of the enumerated type. The data type of an enumerated object is the enumerated type. The technical data type of the content is the [base type](../abap-glossary/abenbase_type_glosry.md) of the enumerated type. [Enumerated variables](../abap-glossary/abenenumerated_variable_glosry.md) are variable enumerated objects that can only contain the associated enumerated values. [Enumerated constants](../abap-glossary/abenenumerated_constant_glosry.md) and components of [enumerated structures](../abap-glossary/abenenumerated_structure_glosry.md) are special enumerated objects that define the value set of an enumerated type.

**enumerated structure**

A constant [structure](../abap-glossary/abenconstant_glosry.md) declared in the definition of an [enumerated type](../abap-glossary/abenenumerated_type_glosry.md), whose components contain all [enumerated values](../abap-glossary/abenenumerated_value_glosry.md) of the enumerated type. The components are special [enumerated objects](../abap-glossary/abenenumerated_object_glosry.md). For an [ABAP enumerated type](../abap-glossary/abenenumerated_type_glosry.md), the declaration of an enumerated structure is optional. A [CDS enumerated type](../abap-glossary/abencds_enum_type_glosry.md) is always connected to an enumerated structure. See also [enumerated constant](../abap-glossary/abenenumerated_constant_glosry.md).

**enumerated type**

Enum for short. An enumerated type is a [data type](../abap-glossary/abendata_type_glosry.md) that specifies a value set in addition to the actual type properties. Enumerated types can be defined in ABAP with [`TYPES BEGIN OF ENUM`](abap-declarations/abaptypes_enum.md) or in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) with [`DEFINE TYPE ENUM`](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_enum_type.md).

See also:

- [ABAP enumerated type](../abap-glossary/abenenumerated_type_glosry.md)

- [CDS enumerated type](../abap-glossary/abencds_enum_type_glosry.md)

**enumerated value**

An enumerated value is an allowed value of an [enumerated variable](../abap-glossary/abenenumerated_variable_glosry.md) or a [CDS enumerated element](../abap-glossary/abencds_enum_element_glosry.md). The possible enumerated values are defined in the definition of the respective [enumerated type](../abap-glossary/abenenum_type_glosry.md) as the values of [enumerated constants](../abap-glossary/abenenumerated_constant_glosry.md) or of components of an [enumerated structure](../abap-glossary/abenenumerated_structure_glosry.md). The technical data type of an enumerated value is the [base type](../abap-glossary/abenbase_type_glosry.md) of the enumerated type.

- [Enumerated types in ABAP](abap-processing-internal-data/abenenumerated_types_usage.md)

- [Enumerated types in ABAP CDS](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_enumeration_types.md)

**enumerated variable**

[Variable](../abap-glossary/abenvariable_glosry.md) with an [enumerated type](../abap-glossary/abenenum_type_glosry.md). An enumerated variable is a variable [enumerated object](../abap-glossary/abenenumerated_object_glosry.md) and can only contain the corresponding [enumerated values](../abap-glossary/abenenumerated_value_glosry.md).

**enumeration**

*-\>* [enumerated type](../abap-glossary/abenenum_type_glosry.md)

**EPP component ID**

Component of an extended passport (EPP). Contains the [system ID](../abap-glossary/abensystem_id_glosry.md) and the name of the [application server instance](../abap-glossary/abenas_instance_glosry.md) of the original [ABAP session](../abap-glossary/abenabap_session_glosry.md).

**EPP connection counter**

Component of an extended passport (EPP). Counts connections between clients and servers with the same EPP connection ID.

**EPP connection ID**

Component of an extended passport (EPP). ID of a connection that is created by calls from [ABAP sessions](../abap-glossary/abenabap_session_glosry.md) or external connections in ABAP sessions.

**EPP precomponent ID**

Component of an extended passport (EPP). Contains the [system ID](../abap-glossary/abensystem_id_glosry.md) and the name of the [application server instance](../abap-glossary/abenas_instance_glosry.md) of the [ABAP session](../abap-glossary/abenabap_session_glosry.md) on which the current connection is based.

**EPP root context ID**

Component of an extended passport (EPP). ID of the original [ABAP session](../abap-glossary/abenabap_session_glosry.md).

**EPP transaction ID**

Component of an extended passport (EPP). ID of the current [SAP-LUW](../abap-glossary/abensap_luw_glosry.md).

**error message**

[Message](../abap-glossary/abenmessage_glosry.md) of the [message type](../abap-glossary/abenmessage_type_glosry.md) *E*. Error messages during the PAI processing of dynpros make input fields on screens ready for input again.

**escape function**

[Processing function](../abap-glossary/abenprocess_function_glosry.md) that replaces special characters in a string in accordance with a set of rules.

**event**

An event can trigger the processing of a [processing block](../abap-glossary/abenprocessing_block_glosry.md), without actually knowing the processing block.

Either a component of a [class](../abap-glossary/abenclass_glosry.md) or an [interface](../abap-glossary/abenoo_intf_glosry.md) declared using [`[CLASS-]`](abap-declarations/abapclass-events.md)[`EVENTS`](abap-declarations/abapevents.md), or an event of the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md). Events in classes trigger [event handlers](../abap-glossary/abenevent_handler_glosry.md).

Events of the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) trigger the processing of [event blocks](../abap-glossary/abenevent_block_glosry.md).

**event block**

[Processing block](../abap-glossary/abenprocessing_block_glosry.md) without local [data area](../abap-glossary/abendata_area_glosry.md), which can be defined in every [ABAP program](../abap-glossary/abenabap_program_glosry.md) except for [type pools](../abap-glossary/abentype_pool_glosry.md), [class pools](../abap-glossary/abenclass_pool_glosry.md), and [interface pools](../abap-glossary/abeninterface_pool_glosry.md). An event block is processed when the corresponding [event](../abap-glossary/abenevent_glosry.md) of the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) is raised. It starts with an [event keyword](../abap-glossary/abenevent_keyword_glosry.md) and ends at the start of the next processing block.

**event handler**

[Method](../abap-glossary/abenmethod_glosry.md) that can handle an [event](../abap-glossary/abenevent_glosry.md) that was raised by [`RAISE EVENT`](abap-calling-and-exiting-program-units/abapraise_event.md) in another method or in the same method. To ensure that an event handler handles a raised event, it must be registered with the statement [`SET HANDLER`](abap-calling-and-exiting-program-units/abapset_handler.md).

**event keyword**

[ABAP keyword](../abap-glossary/abenabap_keyword_glosry.md) that introduces an [event block](../abap-glossary/abenevent_block_glosry.md).

**exception**

Error situation during execution of an [ABAP program](../abap-glossary/abenabap_program_glosry.md). Exceptions are [catchable](../abap-glossary/abencatchable_exception_glosry.md) (statements [`TRY`](abap-program-flow-logic/abaptry.md), [`CATCH`](abap-program-flow-logic/abapcatch_try.md)) or [uncatchable](../abap-glossary/abenuncatchable_exception_glosry.md). Uncaught exceptions result in a [runtime error](../abap-glossary/abenruntime_error_glosry.md).

**exception category**

Classification of [class-based exceptions](../abap-glossary/abenclass_based_exception_glosry.md) corresponding to the [superclasses](../abap-glossary/abensuperclass_glosry.md) of their [exception classes](../abap-glossary/abenexception_class_glosry.md). The exception category determines how the exceptions must be declared in [procedures](../abap-glossary/abenprocedure_glosry.md).

**exception class**

Special [class](../abap-glossary/abenclass_glosry.md) that is the basis for [catchable](../abap-glossary/abencatchable_exception_glosry.md) exceptions. If an [exception](../abap-glossary/abenexception_glosry.md) is raised, an [object](../abap-glossary/abenobject_glosry.md) of an exception class is created. There are predefined exception classes for exceptions of the runtime framework, and user-defined exception classes for custom applications. The superclasses for all exception classes are `CX_STATIC_CHECK`, `CX_DYNAMIC_CHECK`, or `CX_NO_CHECK`, through which exceptions are divided into [exception categories](../abap-glossary/abenexception_category_glosry.md).

**exception group**

Grouping of multiple catchable runtime errors in an organizational unit. The catchable runtime errors of an exception group, together with the obsolete statement `CATCH - ENDCATCH`, can be handled by specifying the group name.

**exception object**

[Instance](../abap-glossary/abeninstance_glosry.md) of an [exception class](../abap-glossary/abenexception_class_glosry.md). Is created when a [catchable exception](../abap-glossary/abencatchable_exception_glosry.md) is raised and contains information on the exception situation. Can be propagated across call levels.

**exception text**

Text that describes an exception and is specified in an [exception class](../abap-glossary/abenexception_class_glosry.md). An exception text can be given parameters using the attributes of the exception class. Exception texts are usually defined with reference to [messages](../abap-glossary/abenmessage_glosry.md) and in [system classes](../abap-glossary/abensystem_class_glosry.md) with reference to the Online Text Repository (OTR).

**executable program**

[ABAP program](../abap-glossary/abenabap_program_glosry.md) that can be executed using the `SUBMIT` statement. An executable program can be started via *System -\> Services -\> Reporting*, or from other services such as report transactions. A `SUBMIT` is always executed internally. An executable program can have its own dynpros, be linked to a logical database, and be executed in background processing.

**exporting parameter**

*-\>* [output parameter](../abap-glossary/abenoutput_parameter_glosry.md)

**expression**

Also [expression syntax](../abap-glossary/abenexpression_syntax_glosry.md). An expression is a syntax that can be used at [operand positions](../abap-glossary/abenoperand_position_glosry.md) of statements. When a statement is processed, its expressions are evaluated and the results are used as [operands](../abap-glossary/abenoperand_glosry.md). See also:

- [ABAP expression](../abap-glossary/abenexpression_glosry.md)

- [SQL expression](../abap-glossary/abensql_expression_glosry.md)

- [CDS DDL expression](../abap-glossary/abencds_expression_glosry.md)

**expression position**

An [operand position](../abap-glossary/abenoperand_position_glosry.md) of an [ABAP statement](../abap-glossary/abenabap_statement_glosry.md) where an [expression](../abap-glossary/abenexpression_glosry.md) can be specified.

**expression syntax**

*-\>* [expression](../abap-glossary/abenexp_glosry.md)

**external procedure call**

[Procedure](../abap-glossary/abenprocedure_glosry.md) call from a different ABAP program of the same [AS ABAP](../abap-glossary/abenas_abap_glosry.md). The first time one of its procedures is called, the required program is loaded into the [internal session](../abap-glossary/abeninternal_session_glosry.md) of the calling program, if not already there, and, apart from [class pools](../abap-glossary/abenclass_pool_glosry.md), the [event](../abap-glossary/abenevent_glosry.md) [`LOAD-OF-PROGRAM`](abap-program-structure/abapload-of-program.md) is raised. See also [program group](../abap-glossary/abenprogram_group_glosry.md).

**external session**

Obsolete name for [ABAP session](../abap-glossary/abenabap_session_glosry.md)

**extract**

Short for extract dataset.

**extract dataset**

Structured unnamed dataset of an [ABAP program](../abap-glossary/abenabap_program_glosry.md). Consists of lines that are organized as field groups. Not part of the ABAP type concept for [data types](../abap-glossary/abendata_type_glosry.md) and [data objects](../abap-glossary/abendata_object_glosry.md).

**extreme value function**

[Function](abap-program-structure/abenfunction.md) that returns the maximum or minimum value from a set of numeric arguments ([`nmax`, `nmin`](abap-processing-internal-data/abennmax_nmin_functions.md)) or character-like arguments ([`cmax`, `cmin`](abap-processing-internal-data/abencmax_cmin_functions.md)).

**fast data access**

FDA for short. Protocol that allows the content of [internal tables](../abap-glossary/abeninternal_table_glosry.md) to be passed between the [Application Server ABAP](../abap-glossary/abenas_abap_glosry.md) and a [database system](../abap-glossary/abendatabase_system_glosry.md). FDA is supported by the [SAP HANA database](../abap-glossary/abenhana_database_glosry.md) and some other platforms. FDA can be switched on and off with database parameters and [database hints](../abap-glossary/abendatabase_hint_glosry.md). FDA write access is the prerequisite for [`SELECT, FROM @itab`](abap-database-access/abapselect_itab.md) in [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md). Depending on settings, FDA is also used for [`SELECT, FOR ALL ENTRIES`](abap-database-access/abenwhere_all_entries.md).

**field**

Another name for [elementary data object](../abap-glossary/abenelementary_data_object_glosry.md).

**field group**

Line structure of an extract dataset. Consists of program-global [fields](../abap-glossary/abenfield_glosry.md) of a program. Defined using the statement `FIELD-GROUPS`.

**field symbol**

Symbolic name for a [data object](../abap-glossary/abendata_object_glosry.md) to which actual memory areas can be assigned at program runtime. A field symbol can be used as a placeholder for a data object at an operand position. A field symbol is [typed](../abap-glossary/abentyping_glosry.md) either generically or completely. Field symbols are declared using the statement [`FIELD-SYMBOLS`](abap-declarations/abapfield-symbols.md) or the [declaration operator](../abap-glossary/abendeclaration_operator_glosry.md) [`FIELD-SYMBOL`](abap-declarations/abenfield-symbol_inline.md); memory areas are assigned to them using [`ASSIGN`](abap-processing-internal-data/abapassign.md).

**file pointer**

Current position for writing to or reading from a file.

**filter operator**

[Constructor operator](../abap-glossary/abenconstructor_operator_glosry.md) [`FILTER`](abap-processing-internal-data/abenconstructor_expression_filter.md) for filtering lines of [internal tables](../abap-glossary/abeninternal_table_glosry.md) using conditions.

**filter stream**

[Stream](../abap-glossary/abenstream_glosry.md) that is not connected directly to a [streaming data source](../abap-glossary/abenstreaming_data_source_glosry.md) or a [streaming data sink](../abap-glossary/abenstreaming_data_sink_glosry.md) but to another stream instead. A filter stream is either a [reader stream](../abap-glossary/abenreader_stream_glosry.md) that reads and filters the data of another reader stream, or a [writer stream](../abap-glossary/abenwriter_stream_glosry.md) that writes filtered data to another writer stream.

**final**

Term in [ABAP Objects](../abap-glossary/abenabap_objects_glosry.md). A final [class](../abap-glossary/abenclass_glosry.md) cannot have any [subclasses](../abap-glossary/abensubclass_glosry.md). A final [method](../abap-glossary/abenmethod_glosry.md) cannot be [redefined](../abap-glossary/abenredefinition_glosry.md).

**fixed point arithmetic**

Calculation with [packed numbers](../abap-glossary/abenpacked_number_glosry.md) ([data type](../abap-glossary/abendata_type_glosry.md) [`p`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md)). Is calculated with an internal accuracy of 31 or (if not sufficient) 63 [places](../abap-glossary/abenplace_glosry.md). [Decimal places](../abap-glossary/abendecimal_place_glosry.md) are rounded arithmetically, if necessary. Places before the [decimal point](../abap-glossary/abendecimal_point_separat_glosry.md) are never lost if a calculation is completed successfully. As a [program property](../abap-glossary/abenprogram_property_glosry.md), the *fixed point arithmetic* determines whether for numbers of type [`p`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) the decimal point is respected in operations or not. The disabling of this program property is obsolete.

**fixed point number**

Number with a fixed number of [decimal places](../abap-glossary/abendecimal_place_glosry.md). In ABAP, fixed point numbers are implemented using [packed numbers](../abap-glossary/abenpacked_number_glosry.md) where a sequence of digits contains a decimal separator at a position defined by a [packed number type](../abap-glossary/abenpacked_number_type_glosry.md).

**flat**

Property of a [data type](../abap-glossary/abendata_type_glosry.md), where the content of its [data objects](../abap-glossary/abendata_object_glosry.md) represents the actual work data. All [elementary data types](../abap-glossary/abenelementary_data_type_glosry.md) except [`string`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) and [`xstring`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md) are flat. See also [deep](../abap-glossary/abendeep_glosry.md).

**flat structure**

[Structure](../abap-glossary/abenstructure_glosry.md) that exclusively contains [flat](../abap-glossary/abenflat_glosry.md) [structure components](../abap-glossary/abenstructure_component_glosry.md).

**flat table**

[Internal table](../abap-glossary/abeninternal_table_glosry.md) with a [flat](../abap-glossary/abenflat_glosry.md) [line type](../abap-glossary/abenrow_type_glosry.md).

**floating point arithmetic**

Calculation with [floating point numbers](../abap-glossary/abenfloating_point_number_glosry.md). It is executed directly on the [host computer](../abap-glossary/abenhost_computer_glosry.md) of the current [AS instance](../abap-glossary/abenas_instance_glosry.md). Either [binary floating point arithmetic](../abap-glossary/abenbinfloat_arith_glosry.md) or [decimal floating point arithmetic](../abap-glossary/abendecfloat_arith_glosry.md).

**floating point function**

[Numeric function](../abap-glossary/abenmathematical_funktion_glosry.md) that expects a [floating point number](../abap-glossary/abenfloating_point_number_glosry.md) as an argument and returns a floating point number as a [return value](../abap-glossary/abenreturn_value_glosry.md).

**floating point number**

Either a [decimal floating point number](../abap-glossary/abendecfloat_glosry.md) or a [binary floating point number](../abap-glossary/abenbinfloat_glosry.md). In floating point numbers, the number of [decimal places](../abap-glossary/abendecimal_place_glosry.md) is part of the value and not part of the data type, as is the case in [packed numbers](../abap-glossary/abenpacked_number_glosry.md). [Floating point arithmetic](../abap-glossary/abenfloating_point_arith_glosry.md) is used for calculations with floating point numbers.

**friend**

Term in [ABAP Objects](../abap-glossary/abenabap_objects_glosry.md). The additions [`FRIENDS`](abap-declarations/abapclass_options.md) and [`LOCAL FRIENDS`](abap-declarations/abapclass_local_friends.md) of the statement [`CLASS`](abap-declarations/abapclass_definition.md) define other [classes](../abap-glossary/abenclass_glosry.md) or [interfaces](../abap-glossary/abenoo_intf_glosry.md) as friends of the class and thus grant them access to all of their components, regardless of the [visibility section](../abap-glossary/abenvisibility_section_glosry.md) or the addition [`READ-ONLY`](abap-declarations/abapdata_options.md). In addition, friends of a class can create [instances](../abap-glossary/abeninstance_glosry.md) of the class without restrictions.

**function group**

*-\>* [function pool](../abap-glossary/abenfunction_pool_glosry.md)

**function module**

[Procedure](../abap-glossary/abenprocedure_glosry.md) that can only be implemented in [function pools](../abap-glossary/abenfunction_pool_glosry.md) and outside [classes](../abap-glossary/abenclass_glosry.md) between the statements [`FUNCTION`](abap-program-structure/abapfunction.md) and [`ENDFUNCTION`](abap-program-structure/abapendfunction.md). An [ABAP program](../abap-glossary/abenabap_program_glosry.md) can use the statement [`CALL FUNCTION`](abap-calling-and-exiting-program-units/abapcall_function.md) to call each function module allowed by the [package concept](../abap-glossary/abenpackage_concept_glosry.md) externally.

**function module exit**

Customer exit for [ABAP programs](../abap-glossary/abenabap_program_glosry.md) in the form of empty or partially implemented [function modules](../abap-glossary/abenfunction_module_glosry.md) delivered with the standard SAP system. Integrated into ABAP programs using the statement `CALL CUSTOMER-FUNCTION`. The function module [interfaces](../abap-glossary/abenintf_gen_glosry.md) are predefined by SAP. The implementation can be empty or partially predefined. The customer must fully implement and activate them using transaction `CMOD`. Function module exits should be replaced by [BAdIs](../abap-glossary/abenbadi_glosry.md).

**function pool**

The only kind of [ABAP program](../abap-glossary/abenabap_program_glosry.md) that can contain [function modules](../abap-glossary/abenfunction_module_glosry.md); usually loaded by calling one of its function modules. A function pool can currently contain a maximum of 99 function modules. It supports its own dynpros.

**functional method**

[Method](../abap-glossary/abenmethod_glosry.md) with exactly one [return value](../abap-glossary/abenreturn_value_glosry.md) declared using [`RETURNING`](abap-declarations/abapmethods_functional.md) and any number of other [formal parameters](../abap-glossary/abenformal_parameter_glosry.md). Can be used in [functional method calls](../abap-glossary/abenfunctional_method_call_glosry.md).

**functional method call**

An [expression](../abap-glossary/abenexpression_glosry.md) that calls a [functional method](../abap-glossary/abenfunctional_method_glosry.md) in a suitable [read position](../abap-glossary/abenread_position_glosry.md), where the [return value](../abap-glossary/abenreturn_value_glosry.md) of the method is used as an [ABAP operand](../abap-glossary/abenabap_operand_glosry.md).

**functional operand position**

[Read position](../abap-glossary/abenread_position_glosry.md) with any [operand type](../abap-glossary/abenoperand_type_glosry.md), in which not only a suitable [data object](../abap-glossary/abendata_object_glosry.md) but also a [functional method call](../abap-glossary/abenfunctional_method_call_glosry.md) or [method chainings](../abap-glossary/abenmethod_chaining_glosry.md), a [constructor expression](../abap-glossary/abenconstructor_expression_glosry.md), or a [table expression](../abap-glossary/abentable_expression_glosry.md) can be specified, the [return value](../abap-glossary/abenreturn_value_glosry.md) or result of which has the suitable [data type](../abap-glossary/abendata_type_glosry.md).

**general expression position**

[Operand position](../abap-glossary/abenread_position_glosry.md) in which not only a suitable [data object](../abap-glossary/abendata_object_glosry.md) can be specified, but also a [constructor expression](../abap-glossary/abenconstructor_expression_glosry.md), a [table expression](../abap-glossary/abentable_expression_glosry.md), a [calculation expression](../abap-glossary/abencalculation_expression_glosry.md), a [built-in function](../abap-glossary/abenbuiltin_function_glosry.md), a [functional method](../abap-glossary/abenfunctional_method_glosry.md), or a [method chaining](../abap-glossary/abenmethod_chaining_glosry.md).

**general numeric function**

[Numeric function](../abap-glossary/abenmathematical_funktion_glosry.md) that expects a [numeric data object](../abap-glossary/abennumeric_data_object_glosry.md) as an argument. The [data type](../abap-glossary/abendata_type_glosry.md) of the argument determines the data type of the [return value](../abap-glossary/abenreturn_value_glosry.md) of the function.

**generic ABAP type**

[Built-in](../abap-glossary/abenbuiltin_data_type_glosry.md) [generic data type](../abap-glossary/abengeneric_data_type_glosry.md). The generic ABAP types are: `any`, `any table`, `c`, `clike`, `csequence`, `data`, `decfloat`, `hashed table`, `index table`, `n`, `numeric`, `p`, `simple`, `sorted table`, `standard table`, `table`, `x`, `xsequence`, and `any structure [ containing ... ]`.

**generic typing**

[Typing](../abap-glossary/abentyping_glosry.md) in which the [data type](../abap-glossary/abendata_type_glosry.md) of a [formal parameter](../abap-glossary/abenformal_parameter_glosry.md) or [field symbol](../abap-glossary/abenfield_symbol_glosry.md) is not fully specified. The actual data type is copied at runtime from the assigned [actual parameter](../abap-glossary/abenactual_parameter_glosry.md) or memory area. During a dynamic access to a generically typed formal parameter or field symbol, the properties of the actual parameter apply. During static access, the properties of the actual parameter determined by the typing apply.

**geodata type**

Data type for geometric data. The [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) currently supports the built-in data type [`GEOM_EWKB`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

**geospatial data**

*-\>* [spatial data](../abap-glossary/abenspatial_data_glosry.md)

**global class**

[Class](../abap-glossary/abenclass_glosry.md) that is defined as a [global type](../abap-glossary/abenglobal_type_glosry.md). Global classes are declared in [class pools](../abap-glossary/abenclass_pool_glosry.md) and are marked as such there using the addition [`PUBLIC`](abap-declarations/abapclass_options.md) of the statement [`CLASS`](abap-declarations/abapclass.md). A class pool can only contain one global class.

**global declaration part**

Area following the opening statement of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) in which [interfaces](../abap-glossary/abenoo_intf_glosry.md), [data types](../abap-glossary/abendata_type_glosry.md), [classes](../abap-glossary/abenclass_glosry.md) and [data objects](../abap-glossary/abendata_object_glosry.md) that are visible in the whole program can be declared.

**global interface**

[Interface](../abap-glossary/abenoo_intf_glosry.md) that is defined as a [global type](../abap-glossary/abenglobal_type_glosry.md). Global interfaces are declared in the [interface pools](../abap-glossary/abeninterface_pool_glosry.md) and are marked as such there using the addition `PUBLIC` of the statement [`INTERFACE`](abap-declarations/abapinterface.md). An interface pool cannot contain anything except for a global interface.

**global type**

[Data type](../abap-glossary/abendata_type_glosry.md) or [object type](../abap-glossary/abenobject_type_glosry.md) that is visible as a [repository object](../abap-glossary/abenrepository_object_glosry.md) in the entire [AS ABAP](../abap-glossary/abenas_abap_glosry.md). Global data types are defined as [DDIC types](../abap-glossary/abenddic_type_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) or as [CDS types](../abap-glossary/abencds_type_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). Global object types are defined as [global classes](../abap-glossary/abenglobal_class_glosry.md) or as [global interfaces](../abap-glossary/abenglobal_interface_glosry.md) in the [class library](../abap-glossary/abenclass_library_glosry.md). All these global types share the same namespace. Besides these global types, data types defined in the public [visibility section](../abap-glossary/abenvisibility_section_glosry.md) of global classes or in global interfaces can also be used globally.

**graph procedure**

A graph procedure is an [ABAP Managed Database Procedure](../abap-glossary/abenabap_managed_db_proc_glosry.md). It refers to [graph workspace](../abap-glossary/abengraph_workspace_glosry.md) and operates on [graph](../abap-glossary/abengraph_glosry.md) models. It is a read-only procedure that is written in [GraphScript](../abap-glossary/abengraphscript_glosry.md).

**graph workspace**

A graph workspace is an object of the [SAP HANA database](../abap-glossary/abenhana_database_glosry.md) that defines a [graph](../abap-glossary/abengraph_glosry.md) in terms of tables and columns, i. e. it consists of two tables (for [vertices](../abap-glossary/abenvertex_glosry.md) and [edges](../abap-glossary/abenedge_glosry.md)) as sources for a graph model. It declares the key column of a [vertex table](../abap-glossary/abenvertex_table_glosry.md) and an [edge table](../abap-glossary/abenedge_table_glosry.md), and also the source and target column of an edge table. It is currently restricted to one key column and one source and target column. Graph workspaces are supported in ABAP by [AMDP](../abap-glossary/abenamdp_glosry.md).

**group break**

Change from one [group level](../abap-glossary/abengroup_level_glosry.md) to another in [group level processing](../abap-glossary/abengroup_level_processing_glosry.md).

**group key**

Value of any [data type](../abap-glossary/abendata_type_glosry.md) that is constructed for each read line in a group key expression when grouping [internal tables](../abap-glossary/abeninternal_table_glosry.md) using [`LOOP AT itab ... GROUP BY`](abap-processing-internal-data/abaploop_at_itab_group_by.md) or [`FOR GROUPS ... OF`](abap-processing-internal-data/abenfor_groups_of.md). All table lines for which the same value is produced are assigned to each group key. In [group level processing](../abap-glossary/abengroup_level_processing_glosry.md) for internal tables, the group key is the content of all columns to the left of a column specified after [`AT`](abap-processing-internal-data/abapat_itab.md).

**group key expression**

Expression for determining the group key of lines in the grouping of [internal tables](../abap-glossary/abeninternal_table_glosry.md) with [`LOOP AT itab ... GROUP BY`](abap-processing-internal-data/abaploop_at_itab_group_by.md) or [`FOR GROUPS ... OF`](abap-processing-internal-data/abenfor_groups_of.md).

**group level**

Set of lines in tabular data e.g. in an [internal table](../abap-glossary/abeninternal_table_glosry.md) that have the same content in an initial part of the lines. Group levels are created by sorting the lines of the table by the initial part. The transition from one group level to the next is called a [group break](../abap-glossary/abengroup_break_glosry.md). Group levels in internal tables can be evaluated with [group level processing](../abap-glossary/abengroup_level_processing_glosry.md). Group levels in [SQL data sources](../abap-glossary/abensql_data_source_glosry.md) can be transformed to [level-based hierarchies](../abap-glossary/abenlevel_based_hiera_glosry.md) by the [hierarchy generator](../abap-glossary/abenhierarchy_generator_glosry.md) of [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md).

**group level processing**

The evaluation of [group levels](../abap-glossary/abengroup_level_glosry.md) in [internal tables](../abap-glossary/abeninternal_table_glosry.md) or the obsolete extracts. Group level processing takes place in [`LOOP`](abap-processing-internal-data/abaploop_at_itab.md)-[loops](../abap-glossary/abenloop_glosry.md) using [control structures](../abap-glossary/abencontrol_structure_glosry.md) defined using the keyword [`AT`](abap-processing-internal-data/abapat_itab.md).

**group loop**

Loop across the groups of an [internal table](../abap-glossary/abeninternal_table_glosry.md) formed by the addition [`GROUP BY`](abap-processing-internal-data/abaploop_at_itab_group_by.md) of the statement [`LOOP AT`](abap-processing-internal-data/abaploop_at_itab_variants.md). A group loop can contain [member loops](../abap-glossary/abenmember_loop_glosry.md) for the evaluation of the groups.

**grouping function**

[Aggregate function](../abap-glossary/abenaggregate_function_glosry.md) for [`GROUPING SETS`](abap-database-access/abapgrouping_sets_clause.md) in a [query](../abap-glossary/abenasql_query_glosry.md). The result of the grouping function `GROUPING` indicates whether a specific column was part of the aggregation. The return value of the grouping function is 0 for the column that was not involved in the aggregation or 1 for the column that was involved in the aggregation.

**hash key**

Unique [table key](../abap-glossary/abentable_key_glosry.md) of an [internal table](../abap-glossary/abeninternal_table_glosry.md), in which the assignment to the table lines is managed using a [hash algorithm](../abap-glossary/abenhash_algorithm_glosry.md). A hash key is the [primary table key](../abap-glossary/abenprimary_table_key_glosry.md) of a [hashed table](../abap-glossary/abenhashed_table_glosry.md) and can be assigned to every type of internal table as a [secondary table key](../abap-glossary/abenprimary_table_key_glosry.md). During access to an internal table using a hash key, the response time is constant, regardless of the number of table entries.

**hashed table**

[Table category](../abap-glossary/abentable_category_glosry.md) of an [internal table](../abap-glossary/abeninternal_table_glosry.md) whose lines are stored internally using a [hash algorithm](../abap-glossary/abenhash_algorithm_glosry.md) and can be accessed using a unique [hash key](../abap-glossary/abenhash_key_glosry.md). A hashed table does not have a [primary table index](../abap-glossary/abenprimary_table_index_glosry.md), but it can be assigned a [secondary table index](../abap-glossary/abensecondary_table_index_glosry.md) using a [secondary table key](../abap-glossary/abensecondary_table_key_glosry.md). The corresponding [generic data type](../abap-glossary/abengeneric_data_type_glosry.md) is [`hashed table`](abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md).

**header line**

Obsolete [work area](../abap-glossary/abenwork_area_glosry.md) of an [internal table](../abap-glossary/abeninternal_table_glosry.md) whose type is the [line type](../abap-glossary/abenrow_type_glosry.md) and has the same name as the internal table. When an internal table with a header line is used in an [operand position](../abap-glossary/abenoperand_position_glosry.md), the header line is usually addressed. To force access to the [table body](../abap-glossary/abentable_body_glosry.md), square brackets `[]` can be specified after the table name.

**heap**

Also referred to as free or dynamic memory. Part of the [program memory](../abap-glossary/abenroll_area_glosry.md), where [anonymous data objects](../abap-glossary/abenanonymous_data_object_glosry.md) created dynamically using [`CREATE DATA`](abap-creating-objects-and-values/abapcreate_data.md), [`CREATE OBJECT`](abap-creating-objects-and-values/abapcreate_object.md), or [`NEW`](abap-creating-objects-and-values/abenconstructor_expression_new.md) or [instances](../abap-glossary/abeninstance_glosry.md) of [classes](../abap-glossary/abenclass_glosry.md) are stored. The occupied memory can be released again by the [garbage collector](../abap-glossary/abengarbage_collector_glosry.md). See also [stack](../abap-glossary/abenstack_glosry.md).

**heap reference**

[Reference](../abap-glossary/abenreference_glosry.md) to an [object](../abap-glossary/abenobject_glosry.md) or part of an object in the [heap](../abap-glossary/abenheap_glosry.md). A heap reference keeps an object alive. See also [stack reference](../abap-glossary/abenstack_reference_glosry.md).

**host constant**

[Host variable](../abap-glossary/abenhost_variable_glosry.md) for which the ABAP [data object](../abap-glossary/abendata_object_glosry.md) is a [constant](../abap-glossary/abenconstant_glosry.md).

**host expression**

ABAP-[expression](../abap-glossary/abenexpression_glosry.md) specified in an operand position of an [ABAP SQL](abap-database-access/abenabap_sql_host_expressions.md) statement. Host expressions are always specified in parentheses preceded by the [escape character](../abap-glossary/abenescape_character_glosry.md) `@`: `@( ... )`.

**host variable**

ABAP [data object](../abap-glossary/abendata_object_glosry.md) specified in an operand position of an [ABAP SQL](abap-database-access/abenabap_sql_host_variables.md) statement or of a statically embedded Native SQL statement. The ABAP data object can be a [variable](../abap-glossary/abenvariable_glosry.md) or a [constant](../abap-glossary/abenconstant_glosry.md) (see [host constant](../abap-glossary/abenhost_constant_glosry.md)). In ABAP SQL, a host variable must be prefixed with the [escape character](../abap-glossary/abenescape_character_glosry.md) `@` ; in Native SQL with the escape character `:`. In ADBC, the placeholder `?` to which ABAP data objects are bound, is used instead of host variables.

**immutable variable**

[Variable](../abap-glossary/abenvariable_glosry.md) that is declared with the [declaration operator](../abap-glossary/abendeclaration_operator_glosry.md) [`FINAL`](abap-declarations/abenfinal_inline.md). This [inline declaration](../abap-glossary/abeninline_declaration_glosry.md) is the only [write position](../abap-glossary/abenwrite_position_glosry.md) within a context where a value can be assigned to an immutable variable.

**implementation part**

Part of the definition of a [class](../abap-glossary/abenclass_glosry.md) in which the [methods](../abap-glossary/abenmethod_glosry.md) of the class are implemented.

**importing parameter**

*-\>* [input parameter](../abap-glossary/abeninput_parameter_glosry.md)

**include program**

[ABAP program](../abap-glossary/abenabap_program_glosry.md) that cannot be compiled independently but must be included in another ABAP program using the statement `INCLUDE`. To be able to be compiled, an include program must be part of a [compilation unit](../abap-glossary/abencompilation_unit_glosry.md). An include program should only be assigned to a single compilation unit.

**index table**

General term for [internal tables](../abap-glossary/abeninternal_table_glosry.md) that are managed using a [primary table index](../abap-glossary/abenprimary_table_index_glosry.md) ([standard tables](../abap-glossary/abenstandard_table_glosry.md) and [sorted tables](../abap-glossary/abensorted_table_glosry.md)). A [secondary table key](../abap-glossary/abensecondary_table_key_glosry.md) can be assigned to enable access using a [hash algorithm](../abap-glossary/abenhash_algorithm_glosry.md). The corresponding [generic data type](../abap-glossary/abengeneric_data_type_glosry.md) is [`index table`](abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md).

**indicator structure**

[Substructure](../abap-glossary/abensubstructure_glosry.md) of a [structured type](../abap-glossary/abenstructured_type_glosry.md). The indicator structure is the last component of the structured type and mirrors the preceding components. The components of the substructure serve as indicators for features of the preceding components. Besides actual indicator structures, there are also [condensed indicator structures](../abap-glossary/abencondensed_ind_structure_glosry.md) that are realized by [byte fields](../abap-glossary/abenbyte_field_glosry.md) where the individual bits serve as indicators. Indicator structures can be defined with the addition [`WITH INDICATORS`](abap-declarations/abaptypes_indicators.md) of the statement [`TYPES`](abap-declarations/abaptypes_indicators.md) and can be used as [ABAP SQL indicators](../abap-glossary/abenabap_sql_indicator_glosry.md). In the latter case, also [inline declarations](../abap-glossary/abeninline_declaration_glosry.md) are possible.

**inheritance**

Generalization-specialization relationship between [classes](../abap-glossary/abenclass_glosry.md). Inheritance means that new [subclasses](../abap-glossary/abensubclass_glosry.md) are derived by adopting all [class components](../abap-glossary/abenclass_component_glosry.md) from [superclasses](../abap-glossary/abensuperclass_glosry.md). A subclass can also be made more specific by declaring new components and [redefining](../abap-glossary/abenredefinition_glosry.md) [methods](../abap-glossary/abenmethod_glosry.md).

**inheritance hierarchy**

Hierarchical relationship between [superclasses](../abap-glossary/abensuperclass_glosry.md) and [subclasses](../abap-glossary/abensubclass_glosry.md) in [inheritance](../abap-glossary/abeninheritance_glosry.md) functions. When [single inheritance](../abap-glossary/abensingle_inheritance_glosry.md) is used, the inheritance hierarchy forms an [inheritance tree](../abap-glossary/abeninheritance_tree_glosry.md).

**inheritance tree**

[Inheritance hierarchy](../abap-glossary/abeninheritance_hierarchy_glosry.md) of the [single inheritance](../abap-glossary/abensingle_inheritance_glosry.md) in which a unique path leads from each [subclass](../abap-glossary/abensubclass_glosry.md) to a [root class](../abap-glossary/abenroot_class_glosry.md).

**initial memory requirement**

Property of a [table type](../abap-glossary/abentable_type_glosry.md) that affects the memory area allocated by the ABAP runtime framework for an [internal table](../abap-glossary/abeninternal_table_glosry.md) before the table is filled with lines. The initial memory requirement is not a [technical type property](../abap-glossary/abentechnical_type_prpt_glosry.md) and does not affect the [compatibility](../abap-glossary/abencompatible_glosry.md) of the table type.

**initial value**

The ABAP runtime framework defines an initial value for each [data type](../abap-glossary/abendata_type_glosry.md). The initial values of the [elementary data types](../abap-glossary/abenelementary_data_type_glosry.md) depend on the corresponding [built-in ABAP type](abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md). The initial value of [reference types](../abap-glossary/abenreference_type_glosry.md) is the [null reference](../abap-glossary/abennull_reference_glosry.md). The initial value of an [internal table](../abap-glossary/abeninternal_table_glosry.md) is an empty table without lines. The initial value of [structured types](../abap-glossary/abenstructured_type_glosry.md) is produced from the initial values of the individual [structure components](../abap-glossary/abenstructure_component_glosry.md). The statement [`CLEAR`](abap-processing-internal-data/abapclear.md) with no additions sets a [data object](../abap-glossary/abendata_object_glosry.md) to the appropriate initial value for its type. Initial values are also assigned to most [built-in data types](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) in [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md), but those are not evaluated in ABAP programs.

**initial value sharing**

The status of a [boxed component](../abap-glossary/abenboxed_component_glosry.md) as long as it is processed by read access only. The [initial value](../abap-glossary/abeninitial_value_glosry.md) of all type-compliant boxed components of the same type is only stored once in each [AS instance](../abap-glossary/abenas_instance_glosry.md) in the [PXA](../abap-glossary/abenpxa_glosry.md).

**injection**

Test-friendly code located between the statements [`TEST-INJECTION`](abap-program-maintenance/abaptest-injection.md) and [`END-TEST-INJECTION`](abap-program-maintenance/abapend-test-injection.md) in a [method](../abap-glossary/abenmethod_glosry.md) of a [test class](../abap-glossary/abentest_class_glosry.md). Injections replace the associated [test seams](../abap-glossary/abentest_seam_glosry.md) when a [unit test](../abap-glossary/abenunit_test_glosry.md) is executed.

**inline declaration**

[Declaration](../abap-glossary/abendeclaration_glosry.md) of a [variable](../abap-glossary/abenvariable_glosry.md), an [immutable variable](../abap-glossary/abenimmutable_variable_glosry.md) or a [field symbol](../abap-glossary/abenfield_symbol_glosry.md) using a [declaration expression](../abap-glossary/abendeclaration_expression_glosry.md) in a [declaration position](../abap-glossary/abendeclaration_position_glosry.md).

**input parameter**

[Formal parameter](../abap-glossary/abenformal_parameter_glosry.md) to which the value of an [actual parameter](../abap-glossary/abenactual_parameter_glosry.md) is passed at the time of a call.

**input stream**

*-\>* [Reader stream](../abap-glossary/abenreader_stream_glosry.md)

**input/output parameter**

[Formal parameter](../abap-glossary/abenformal_parameter_glosry.md) to which the value of an [actual parameter](../abap-glossary/abenactual_parameter_glosry.md) is passed at the time of the call. It can be changed during the call and is available in the actual parameter at the end of the call.

**insertion function**

[Processing function](../abap-glossary/abenprocess_function_glosry.md) that inserts a string into another string.

**instance**

Concrete occurrence of an abstract [type](../abap-glossary/abentype_glosry.md). The instance of a [data type](../abap-glossary/abendata_type_glosry.md) is a [data object](../abap-glossary/abendata_object_glosry.md). The instance of a [class](../abap-glossary/abenclass_glosry.md) is often simply described as an object. See also [instantiation](../abap-glossary/abeninstantiation_glosry.md).

**instance attribute**

[Attribute](../abap-glossary/abenattribute_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md) that is declared using [`DATA`](abap-declarations/abapdata.md). Instance attributes are only valid in the [context](../abap-glossary/abenobj_context_glosry.md) of an [instance](../abap-glossary/abeninstance_glosry.md) of the class. The content of the instance attributes determines the state of the [objects](../abap-glossary/abenobject_glosry.md) of a class.

**instance component**

Superordinate term for [instance attributes](../abap-glossary/abeninstance_attribute_glosry.md), [instance events](../abap-glossary/abeninstance_event_glosry.md), and [instance methods](../abap-glossary/abeninstance_method_glosry.md). The instance components of a [class](../abap-glossary/abenclass_glosry.md) can only be addressed in [instances](../abap-glossary/abeninstance_glosry.md) of the class.

**instance component selector**

*-\>* [object component selector](../abap-glossary/abenobject_component_select_glosry.md)

**instance constructor**

[Constructor](../abap-glossary/abenconstructor_glosry.md) declared under the name [`constructor`](abap-abap-objects/abenconstructor.md) as an [instance method](../abap-glossary/abeninstance_method_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md), and which is automatically called when the class is [instantiated](../abap-glossary/abeninstantiation_glosry.md) and after the [object](../abap-glossary/abenobject_glosry.md) is created.

**instance event**

[Event](../abap-glossary/abenevent_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md) declared using [`EVENTS`](abap-declarations/abapevents.md). Instance events usually indicate status changes of [objects](../abap-glossary/abenobject_glosry.md).

**instance method**

[Method](../abap-glossary/abenmethod_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md) declared using [`METHODS`](abap-declarations/abapmethods.md), which can only be used in an [instance](../abap-glossary/abeninstance_glosry.md) of the class. Instance methods can access all [attributes](../abap-glossary/abenattribute_glosry.md) and [events](../abap-glossary/abenevent_glosry.md) of their class.

**instance operator**

[Constructor operator](../abap-glossary/abenconstructor_operator_glosry.md) [`NEW`](abap-creating-objects-and-values/abenconstructor_expression_new.md) used to [instantiate](../abap-glossary/abeninstantiation_glosry.md) [objects](../abap-glossary/abenobject_glosry.md).

**instantiation**

Creation of an [instance](../abap-glossary/abeninstance_glosry.md). [Data objects](../abap-glossary/abendata_object_glosry.md) as instances of [data types](../abap-glossary/abendata_type_glosry.md) are created implicitly when a [context](../abap-glossary/abenobj_context_glosry.md) is loaded, or explicitly using [`CREATE DATA`](abap-creating-objects-and-values/abapcreate_data.md) or [`NEW`](abap-creating-objects-and-values/abenconstructor_expression_new.md). [Objects](../abap-glossary/abenobject_glosry.md) as an instance of [classes](../abap-glossary/abenclass_glosry.md) are only created explicitly using [`CREATE OBJECT`](abap-creating-objects-and-values/abapcreate_object.md) or [`NEW`](abap-creating-objects-and-values/abenconstructor_expression_new.md).

**integer**

[Numeric data object](../abap-glossary/abennumeric_data_object_glosry.md) of ABAP or elementary object of the database with an [integer type](../abap-glossary/abeninteger_type_glosry.md).

**integer literal**

A [numeric literal](../abap-glossary/abennumeric_literal_glosry.md) of an [integer type](../abap-glossary/abeninteger_type_glosry.md).

- In general ABAP, integer literals are [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), integer literals can be [typed literals](../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Numeric Literals in ABAP](abap-declarations/abenuntyped_number_literals.md)

- [Literals in ABAP SQL](abap-database-access/abenabap_sql_literals.md)

- [Literals in CDS](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_literal_v2.md)

**integer type**

[Numeric data type](../abap-glossary/abennumeric_data_type_glosry.md) for storing [integer numbers](../abap-glossary/abeninteger_number_glosry.md) of different value ranges. The associated [built-in ABAP types](../abap-glossary/abenbuiltin_abap_type_glosry.md) are ([`b`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`s`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md)), [`i`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), and [`int8`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md). The [built-in DDIC types](../abap-glossary/abenbuiltin_ddic_type_glosry.md) are [`INT1`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT2`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT4`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`INT8`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The internal representation takes place in the integer representation of the current platform. A [data object](../abap-glossary/abendata_object_glosry.md) of an integer type is an [integer](../abap-glossary/abeninteger_glosry.md).

**interface (ABAP Objects)**

Template for the [public](../abap-glossary/abenpublic_glosry.md) [interface](../abap-glossary/abenintf_gen_glosry.md) of [classes](../abap-glossary/abenclass_glosry.md) in [ABAP Objects](../abap-glossary/abenabap_objects_glosry.md). Defined with [`INTERFACE - ENDINTERFACE`](abap-declarations/abapinterface.md), either as a [global interface](../abap-glossary/abenglobal_interface_glosry.md) in an [interface pool](../abap-glossary/abeninterface_pool_glosry.md) or as a [local interface](../abap-glossary/abenlocal_interface_glosry.md) in another [ABAP program](../abap-glossary/abenabap_program_glosry.md). An interface contains the declaration of [interface components](../abap-glossary/abeninterface_component_glosry.md) but does not contain method implementations. Can be implemented in classes using [`INTERFACES`](abap-declarations/abapinterfaces.md), which enhances the external interface of the class by adding interface components. OO interfaces are generally referred to as interfaces, unless the distinction to [general interfaces](../abap-glossary/abenintf_gen_glosry.md) needs to be made.

**interface (general)**

Boundary between two [contexts](../abap-glossary/abenobj_context_glosry.md).

- [Procedures](../abap-glossary/abenprocedure_glosry.md) have a [parameter interface](../abap-glossary/abenparameter_interface_glosry.md).

- In [classes](../abap-glossary/abenclass_glosry.md), interfaces are defined by [class components](../abap-glossary/abenclass_component_glosry.md) of the different [visibility sections](../abap-glossary/abenvisibility_section_glosry.md).

- The [public](../abap-glossary/abenpublic_glosry.md) components of classes can also be defined in standalone [interfaces](../abap-glossary/abenoo_intf_glosry.md) of [ABAP Objects](../abap-glossary/abenabap_objects_glosry.md).

- The [database interface](../abap-glossary/abendatabase_interface_glosry.md) connects an [AS ABAP](../abap-glossary/abenas_abap_glosry.md) to its [database](../abap-glossary/abendatabase_glosry.md).

- In special cases, interface work areas are used between programs of a [program group](../abap-glossary/abenprogram_group_glosry.md).

- The global data of the ABAP program or the interface work areas can be used as an interface between [ABAP programs](../abap-glossary/abenabap_program_glosry.md) and dynpros.

**interface component**

[Component](../abap-glossary/abencomponent_glosry.md) of an [interface](../abap-glossary/abenoo_intf_glosry.md). Declared in the [declaration part](../abap-glossary/abendeclaration_part_glosry.md) of an interface. Possible interface components are: [Attributes](../abap-glossary/abenattribute_glosry.md), [methods](../abap-glossary/abenmethod_glosry.md), and [events](../abap-glossary/abenevent_glosry.md).

**interface component selector**

Character `~`. An [interface component](../abap-glossary/abeninterface_component_glosry.md) `comp` of an [interface](../abap-glossary/abenoo_intf_glosry.md) `intf` can be addressed in an implementing [class](../abap-glossary/abenclass_glosry.md) or a [compound interface](../abap-glossary/abencompound_interface_glosry.md) via `intf~comp`.

**interface pool**

[ABAP program](../abap-glossary/abenabap_program_glosry.md) that contains the definition of exactly one [global interface](../abap-glossary/abenglobal_interface_glosry.md) and is loaded when using the interface. Does not support its own dynpros.

**interface reference variable**

[Object reference variable](../abap-glossary/abenobject_refer_variable_glosry.md) of the [static type](../abap-glossary/abenstatic_type_glosry.md) of an [interface](../abap-glossary/abenoo_intf_glosry.md). An interface reference variable can be used to access the visible [interface components](../abap-glossary/abeninterface_component_glosry.md) of an object that exists in the corresponding interface. This applies to both dynamic and static access.

**interface work area**

Special [data objects](../abap-glossary/abendata_object_glosry.md) that can be used as a cross-program [interface](../abap-glossary/abenintf_gen_glosry.md) between programs and dynpros, and between programs and logical databases. Interface work areas are either table work areas or common areas (obsolete). All programs in a [program group](../abap-glossary/abenprogram_group_glosry.md) access the same data of an interface work area.

**internal mode**

Obsolete name for [internal session](../abap-glossary/abeninternal_session_glosry.md).

**internal procedure call**

Call of a [processing block](../abap-glossary/abenprocessing_block_glosry.md) ([procedure](../abap-glossary/abenprocedure_glosry.md)) of the same program. The required program does not have to be reloaded into the [internal session](../abap-glossary/abeninternal_session_glosry.md).

**internal session**

Instance within an [ABAP session](../abap-glossary/abenabap_session_glosry.md) with its own [program memory](../abap-glossary/abenroll_area_glosry.md) in which the data and [objects](../abap-glossary/abenobject_glosry.md) of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) are stored during its execution. An internal session is created when an ABAP program is called in the [shared memory](../abap-glossary/abenshared_memory_glosry.md) and is preserved for as long as the main program of its main program group is executed.

**internal table**

[Dynamic data object](../abap-glossary/abendynamic_data_object_glosry.md) that consists of a sequence of lines of the same [data type](../abap-glossary/abendata_type_glosry.md). An internal table has a [table type](../abap-glossary/abentable_type_glosry.md) that specifies the [line type](../abap-glossary/abenrow_type_glosry.md), the [table category](../abap-glossary/abentable_category_glosry.md), and a [table key](../abap-glossary/abentable_key_glosry.md). The corresponding [generic data type](../abap-glossary/abengeneric_data_type_glosry.md) is [`any table`](abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md).

**iteration**

Repeated processing of a [statement block](../abap-glossary/abenstatement_block_glosry.md) in a [loop](../abap-glossary/abenloop_glosry.md) or an [expression](../abap-glossary/abenexpression_glosry.md) with an [iteration expression](../abap-glossary/abeniteration_expression_glosry.md).

**iteration expression**

Expression that executes an [iteration](../abap-glossary/abeniteration_glosry.md). An iteration expression is a subexpression of a [constructor expression](../abap-glossary/abenconstructor_expression_glosry.md) introduced using the [iteration operator](../abap-glossary/abeniteration_operator_glosry.md) [`FOR`](abap-program-flow-logic/abenfor.md) and executes [conditional iterations](abap-program-flow-logic/abenfor_conditional.md) or [table iterations](../abap-glossary/abentable_iteration_glosry.md).

**iteration operator**

The iteration operator `FOR` introduces an [iteration expression](../abap-glossary/abeniteration_expression_glosry.md) as a subexpression of a [constructor expression](../abap-glossary/abenconstructor_expression_glosry.md).

**kernel method**

[Method](../abap-glossary/abenmethod_glosry.md) that is implemented in the [kernel](../abap-glossary/abenkernel_glosry.md) of the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) instead of in an [ABAP program](../abap-glossary/abenabap_program_glosry.md).

**key table**

Superordinate term for [sorted tables](../abap-glossary/abensorted_table_glosry.md) and [hashed tables](../abap-glossary/abenhashed_table_glosry.md), in which the [primary table key](../abap-glossary/abenprimary_table_key_glosry.md), unlike [standard tables](../abap-glossary/abenstandard_table_glosry.md), has its own stable administration that allows optimized access.

**language environment**

Language-dependent settings for [ABAP programs](../abap-glossary/abenabap_program_glosry.md). The language environment includes both [language settings](../abap-glossary/abenlanguage_setting_glosry.md) and [format settings](../abap-glossary/abenformat_setting_glosry.md).

**language setting**

Part of the [language environment](../abap-glossary/abenlanguage_environment_glosry.md). The language setting of an ABAP program comprises the [logon language](../abap-glossary/abenlogon_language_glosry.md) and the [text environment language](../abap-glossary/abentext_env_langu_glosry.md) of the [text environment](../abap-glossary/abentext_environment_glosry.md).

**lazy update**

Procedure to create or update non-unique [secondary table keys](../abap-glossary/abensecondary_table_key_glosry.md) in [internal tables](../abap-glossary/abeninternal_table_glosry.md). Non-unique secondary tables keys are not updated straight after insert operations using [`INSERT`](abap-processing-internal-data/abapinsert_itab.md) or [`APPEND`](abap-processing-internal-data/abapappend.md), a block operation in which the whole table body is filled at once, or after a modifying operation using [`MODIFY`](abap-processing-internal-data/abapmodify_itab.md), [field symbols](../abap-glossary/abenfield_symbol_glosry.md), or [data references](../abap-glossary/abendata_reference_glosry.md). They are updated at the next explicit usage. See also [direct update](../abap-glossary/abendirect_update_glosry.md) and [delayed update](../abap-glossary/abendelayed_update_glosry.md).

**legacy file**

File on a [host computer](../abap-glossary/abenhost_computer_glosry.md) of an [AS instance](../abap-glossary/abenas_instance_glosry.md) that was opened using the addition `LEGACY` of the statement `OPEN DATASET`. In a legacy file, the [byte order](../abap-glossary/abenbyte_order_glosry.md) and the [code page](../abap-glossary/abencodepage_glosry.md) for handling the content of the file can be specified.

**length function**

[Description function](../abap-glossary/abendescription_function_glosry.md) that determines the length of a data object in characters or bytes.

**`LET` expression**

A `LET` expression is a subexpression of a [constructor expression](../abap-glossary/abenconstructor_expression_glosry.md) that declares [variables](../abap-glossary/abenvariable_glosry.md) or [field symbols](../abap-glossary/abenfield_symbol_glosry.md) as local helper fields.

**line type**

[Technical type property](../abap-glossary/abentechnical_type_prpt_glosry.md) of a [table type](../abap-glossary/abentable_type_glosry.md) that defines the common [data type](../abap-glossary/abendata_type_glosry.md) of the lines in an [internal table](../abap-glossary/abeninternal_table_glosry.md).

**literal**

The textual representation of a value in the [ABAP source code](../abap-glossary/abenabap_source_code_glosry.md) of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) or in a [CDS object](../abap-glossary/abencds_object_glosry.md). There are [typed literals](../abap-glossary/abentyped_literal_glosry.md) and [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md) available.

See also:

- [ABAP literal](../abap-glossary/abenabap_literal_glosry.md)

- [ABAP SQL literal](../abap-glossary/abenabap_sql_literal_glosry.md)

- [CDS literal](../abap-glossary/abencds_literal_glosry.md)

**literal operator**

The literal operator `&` joins two [text field literals](../abap-glossary/abentext_field_literal_glosry.md) or two [text string literals](../abap-glossary/abentext_string_literal_glosry.md) as a single literal or two [string templates](../abap-glossary/abenstring_template_glosry.md) as a single string template. The literal operator is supported in [ABAP literals](../abap-glossary/abenabap_literal_glosry.md) and in [ABAP SQL literals](../abap-glossary/abenabap_sql_literal_glosry.md), but not in [CDS literals](../abap-glossary/abencds_literal_glosry.md).

**load**

In ABAP, a load is a binary representation of a [repository object](../abap-glossary/abenrepository_object_glosry.md), which is optimized for fast access, in the memory or on the database. Examples of loads are program load that is made up of the byte code of the existing program or the package load.

**local class**

[Class](../abap-glossary/abenclass_glosry.md) of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) that can be accessed statically from the ABAP program only. Local classes can be created in all program types, with the exception of [interface pools](../abap-glossary/abeninterface_pool_glosry.md) and [type pools](../abap-glossary/abentype_pool_glosry.md). In particular, [class pools](../abap-glossary/abenclass_pool_glosry.md) can contain local classes for use in the [global class](../abap-glossary/abenglobal_class_glosry.md) or by frameworks. All local classes of an ABAP program share the same namespace together with the [local interfaces](../abap-glossary/abenlocal_interface_glosry.md) and the program-global [data types](../abap-glossary/abendata_type_glosry.md) declared with [`TYPES`](abap-declarations/abaptypes.md).

**local data**

Local data is declared in [procedures](../abap-glossary/abenprocedure_glosry.md) and is only known there. See also global data.

**local data queue**

Persistence layer into which data can be placed and read only in the order in which it was stored. The local data queue triggers the no-send scenario of the qRFC.

**local interface**

[Interface](../abap-glossary/abenoo_intf_glosry.md) of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) that can be accessed statically in this program only. Local interfaces can be created in all program types except for [interface pools](../abap-glossary/abeninterface_pool_glosry.md) and [type pools](../abap-glossary/abentype_pool_glosry.md). All local interfaces of an ABAP program share the same namespace together with the [local classes](../abap-glossary/abenlocal_class_glosry.md) and the program-global [data types](../abap-glossary/abendata_type_glosry.md) declared using [`TYPES`](abap-declarations/abaptypes.md).

**locator**

Pointer to substrings of [LOBs](../abap-glossary/abenlob_glosry.md) in a [database](../abap-glossary/abendatabase_glosry.md). In ABAP, locators are [LOB handles](../abap-glossary/abenlob_handle_glosry.md) and are implemented using [instances](../abap-glossary/abeninstance_glosry.md) of the corresponding [system classes](../abap-glossary/abensystem_class_glosry.md). Locators can be linked with the database in question in [ABAP SQL statements with LOBs](../abap-glossary/abenabap_sql_glosry.md). Different [locator types](../abap-glossary/abenlocator_type_glosry.md) are provided for [BLOBs](../abap-glossary/abenblob_glosry.md) and [CLOBs](../abap-glossary/abenclob_glosry.md).

**logical database**

Special [ABAP program](../abap-glossary/abenabap_program_glosry.md) that provides other ABAP programs with data from the nodes of a hierarchical tree structure (obsolete). Is either linked to an executable program in its [program properties](../abap-glossary/abenprogram_property_glosry.md) or is called using [function module](../abap-glossary/abenfunction_module_glosry.md) `LDB_PROCESS`. A logical database is made up of a hierarchical structure with nodes, an ABAP database program and its own standard selection screen. Logical databases are maintained in the Logical Database Builder.

**logical expression**

Formulation of a condition for [operands](../abap-glossary/abenoperand_glosry.md). A logical expression is a single [relational expression](../abap-glossary/abenrelational_expression_glosry.md) or is made up of multiple relational expressions combined by [Boolean operators](../abap-glossary/abenboolean_operator_glosry.md). The result of a logical expression is a [truth value](../abap-glossary/abentruth_value_glosry.md), that is, either true or false.

- In general ABAP, logical expressions are used in [control statements](../abap-glossary/abencontrol_statement_glosry.md) or other statements that contain conditions, as well as in [conditional expressions](../abap-glossary/abenconditional_expression_glosry.md) and [Boolean functions](../abap-glossary/abenboole_function_glosry.md). For further details, see the topic [Logical Expressions (`log_exp`)](abap-program-flow-logic/abenlogexp.md).

- In ABAP SQL, logical expressions are used in conditions, such as `WHERE` and `ON` conditions.

- In ABAP CDS, logical expressions are used in conditions, such as `WHERE` and `ON` conditions.

**logpoint**

In an [ABAP program](../abap-glossary/abenabap_program_glosry.md), a logpoint is defined statically as an unconditional [checkpoint](../abap-glossary/abencheckpoint_glosry.md) using the statement `LOG-POINT`, or dynamically in transaction `SDLP` or in the [ABAP development tools for Eclipse (ADT)](../abap-glossary/abenadt_glosry.md). When an active logpoint is reached, a log entry is created. A static logpoint must be assigned to a [checkpoint group](../abap-glossary/abencheckpoint_group_glosry.md) when it is created. This group controls its [activation](../abap-glossary/abenactivatable_checkpoint_glosry.md).

**loop**

[Control structure](../abap-glossary/abencontrol_structure_glosry.md) that performs an [iteration](../abap-glossary/abeniteration_glosry.md). Consists of a [statement block](../abap-glossary/abenstatement_block_glosry.md) defined by the keywords [`DO` - `ENDDO`](abap-program-flow-logic/abapdo.md), [`WHILE` - `ENDWHILE`](abap-program-flow-logic/abapwhile.md), [`LOOP` - `ENDLOOP`](abap-processing-internal-data/abaploop_at_itab.md), `PROVIDE` - `ENDPROVIDE`, [`SELECT` - `ENDSELECT`](abap-database-access/abapselect.md) and that can be executed multiple times.

**lossless assignment**

[Assignment](../abap-glossary/abenassignment_glosry.md) between two non-[compatible](../abap-glossary/abencompatible_glosry.md) [data objects](../abap-glossary/abendata_object_glosry.md), where the source field contains a valid value, the [conversion](../abap-glossary/abenconversion_glosry.md) is lossless, and the target field contains a valid value after the assignment. The [lossless operator](../abap-glossary/abenlossless_operator_glosry.md) [`EXACT`](abap-processing-internal-data/abenconstructor_expression_exact.md) and the addition `EXACT` of the obsolete statement `MOVE` [assignment](../abap-glossary/abenassignment_glosry.md) can be used to check whether an assignment is lossless.

**lossless calculation**

[Arithmetic](../abap-glossary/abenarithmetic_expression_glosry.md) calculation where no rounding occurs. The [lossless operator](../abap-glossary/abenlossless_operator_glosry.md) [`EXACT`](abap-processing-internal-data/abenconstructor_expression_exact.md) or the addition `EXACT` of the obsolete statement `COMPUTE` can be used to check whether a calculation is lossless.

**lossless operator**

[Constructor operator](../abap-glossary/abenconstructor_operator_glosry.md) [`EXACT`](abap-processing-internal-data/abenconstructor_expression_exact.md) for lossless creation of a value for a [data type](../abap-glossary/abendata_type_glosry.md).

**macro**

Combination of a statement sequence for internal reuse of [source code](../abap-glossary/abensource_code_glosry.md) within a program. In [ABAP source code](../abap-glossary/abenabap_source_code_glosry.md), macros are defined between `DEFINE` and `END-OF-DEFINITION` or in database table `TRMAC`.

**main program**

The first program of a [program group](../abap-glossary/abenprogram_group_glosry.md). The first program (executable program, module pool, or [function pool](../abap-glossary/abenfunction_pool_glosry.md)) that is loaded by a program call into an [internal session](../abap-glossary/abeninternal_session_glosry.md) is the main program of the main program group. The program (function pool or [class pool](../abap-glossary/abenclass_pool_glosry.md)), for which an additional program group is created when it is loaded is the main program of the additional program group.

**main program group**

First [program group](../abap-glossary/abenprogram_group_glosry.md) of an [internal session](../abap-glossary/abeninternal_session_glosry.md). It is created when the internal session is created through a program call. The first program in an internal session is the main program of the main program group. The runtime of the main program in the main program group determines its lifespan and that of the entire internal session.

**main session**

Obsolete name for [ABAP session](../abap-glossary/abenabap_session_glosry.md)

**master program**

[Compilation unit](../abap-glossary/abencompilation_unit_glosry.md) that is modularized into different [processing blocks](../abap-glossary/abenprocessing_block_glosry.md) which are distributed over several [include programs](../abap-glossary/abeninclude_program_glosry.md). Typical master programs are [class](../abap-glossary/abenclass_pool_glosry.md) and [function pools](../abap-glossary/abenfunction_pool_glosry.md), that are created implicitly by the development tools. The [ABAP Unit](../abap-glossary/abenabap_unit_glosry.md) tests for the units in the include programs are usually created in the [test include](../abap-glossary/abentest_include_glosry.md) of the master program.

**match function**

[Processing function](../abap-glossary/abenprocess_function_glosry.md) that returns a substring of a character string that matches a [regular expression](../abap-glossary/abenregular_expression_glosry.md).

**measuring interval**

Duration of execution of a limited measuring section.

**measuring section**

A sequence of statements delimited by `GET RUN TIME` in the program code, whose runtime is to be measured.

**member loop**

Loop at the members of a group in a [group loop](../abap-glossary/abengroup_loop_glosry.md) introduced using the statement [`LOOP AT GROUP`](abap-processing-internal-data/abaploop_at_group.md).

**mesh**

Instance of a [mesh type](../abap-glossary/abenmesh_type_glosry.md). Special [structure](../abap-glossary/abenstructure_glosry.md) whose [components](../abap-glossary/abenstructure_component_glosry.md) described as [mesh nodes](../abap-glossary/abenmesh_node_glosry.md) are exclusively [internal tables](../abap-glossary/abeninternal_table_glosry.md) that can be joined using [mesh associations](../abap-glossary/abenmesh_association_glosry.md).

**mesh association**

[Association](../abap-glossary/abenassociation_glosry.md) of a [mesh](../abap-glossary/abenmesh_glosry.md). Property of a [mesh node](../abap-glossary/abenmesh_node_glosry.md) and therefore part of the [mesh type](../abap-glossary/abenmesh_type_glosry.md). Associates mesh nodes in [mesh paths](../abap-glossary/abenmesh_path_glosry.md).

**mesh node**

Component of a [mesh](../abap-glossary/abenmesh_glosry.md). Mesh nodes are always [internal tables](../abap-glossary/abeninternal_table_glosry.md) with a structured [line type](../abap-glossary/abenrow_type_glosry.md). Mesh nodes can have [mesh associations](../abap-glossary/abenmesh_association_glosry.md) that they can address in [mesh paths](../abap-glossary/abenmesh_path_glosry.md).

**mesh path**

Chaining of multiple [mesh nodes](../abap-glossary/abenmesh_node_glosry.md) using their [mesh associations](../abap-glossary/abenmesh_association_glosry.md). A mesh path describes a set of lines in its final path node. These lines are accessed when a mesh path is used.

**mesh path expression**

A standalone specification of a [mesh path](../abap-glossary/abenmesh_path_glosry.md) in an [operand position](../abap-glossary/abenoperand_position_glosry.md) for which the same rules apply as for a [table expression](../abap-glossary/abentable_expression_glosry.md).

**mesh type**

[Data type](../abap-glossary/abendata_type_glosry.md) of a [mesh](../abap-glossary/abenmesh_glosry.md). Special [structured type](../abap-glossary/abenstructured_type_glosry.md) that contains only [table types](../abap-glossary/abentable_type_glosry.md) with structured [line types](../abap-glossary/abenrow_type_glosry.md) as [components](../abap-glossary/abenstructure_component_glosry.md) that can be linked using [mesh associations](../abap-glossary/abenmesh_association_glosry.md).

**message**

Text that can be accessed using the statement [`MESSAGE`](abap-text-repositories/abapmessage.md). Messages are always displayed in the [logon language](../abap-glossary/abenlogon_language_glosry.md), which cannot be changed during a [user session](../abap-glossary/abenuser_session_glosry.md). Message texts are organized into [message classes](../abap-glossary/abenmessage_class_glosry.md) and [message numbers](../abap-glossary/abenmessage_number_glosry.md) and are maintained in the transaction message maintenance. When a message is accessed using the statement [`MESSAGE`](abap-text-repositories/abapmessage.md), it is classified with a [message type](../abap-glossary/abenmessage_type_glosry.md) that defines the behavior of the message. Messages are also used as exception texts of [exception classes](../abap-glossary/abenexception_class_glosry.md).

**message class**

Identifier that groups [messages](../abap-glossary/abenmessage_glosry.md) in an application area.

**message number**

Number that identifies the [messages](../abap-glossary/abenmessage_glosry.md) of a [message class](../abap-glossary/abenmessage_class_glosry.md).

**message type**

Must be specified when the statement [`MESSAGE`](abap-text-repositories/abapmessage.md) is used to send a [message](../abap-glossary/abenmessage_glosry.md). It determines the representation of the message in the SAP GUI and the subsequent program flow. The possible message types are [information message](../abap-glossary/abeninformation_message_glosry.md), [status message](../abap-glossary/abenstatus_message_glosry.md), [error message](../abap-glossary/abenerror_message_glosry.md), [warning](../abap-glossary/abenwarning_glosry.md), [termination message](../abap-glossary/abentermination_message_glosry.md), and [exit message](../abap-glossary/abenexit_message_glosry.md).

**method**

[Procedure](../abap-glossary/abenprocedure_glosry.md) that is declared as a [component](../abap-glossary/abencomponent_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md) or of an [interface](../abap-glossary/abenoo_intf_glosry.md). The two possible methods are [instance methods](../abap-glossary/abeninstance_method_glosry.md) and [static methods](../abap-glossary/abenstatic_method_glosry.md). A method can be implemented only in the [implementation part](../abap-glossary/abenimplementation_part_glosry.md) of its class, between [`METHOD`](abap-program-structure/abapmethod.md) and [`ENDMETHOD`](abap-program-structure/abapendmethod.md).

**method chaining**

Chained calls of [functional methods](../abap-glossary/abenfunctional_method_glosry.md). Either a [chained method call](../abap-glossary/abenchained_method_call_glosry.md) or a [chained attribute access](../abap-glossary/abenchained_attribute_acc_glosry.md).

**module pool**

[ABAP program](../abap-glossary/abenabap_program_glosry.md) that normally contains dynpros and dialog modules, and is started using transaction codes.

**multiplication assignment operator**

[Calculation assignment operator](../abap-glossary/abencalc_assignment_op_glosry.md) `*=` that multiplies values in an assignment.

**multitenancy**

Principle of software architecture in which a single software instance is run for different tenants on a single server. In a multitenancy [AS ABAP](../abap-glossary/abenas_abap_glosry.md), [application clients](../abap-glossary/abenapplication_client_glosry.md) assume the role of tenants. Multitenancy is not supported by the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) in the current release.

**named data object**

[Data object](../abap-glossary/abendata_object_glosry.md) that can be identified via a name. Named data objects are [constants](../abap-glossary/abenconstant_glosry.md), [variables](../abap-glossary/abenvariable_glosry.md), and [text symbols](../abap-glossary/abentext_symbol_glosry.md) and can be stored in the [stack](../abap-glossary/abenstack_glosry.md) or as [instance attributes](../abap-glossary/abeninstance_attribute_glosry.md) in the [heap](../abap-glossary/abenheap_glosry.md). See also [unnamed data object](../abap-glossary/abenunnamed_data_object_glosry.md).

**named include**

*-\>* [component group](../abap-glossary/abencomponent_group_glosry.md)

**narrowing cast**

*-\>* [Downcast](../abap-glossary/abendown_cast_glosry.md)

**nested interface**

*-\>* [Compound interface](../abap-glossary/abencompound_interface_glosry.md)

**nested structure**

[Structure](../abap-glossary/abenstructure_glosry.md) with one or more [substructures](../abap-glossary/abensubstructure_glosry.md). A nested structure can contain [boxed components](../abap-glossary/abenboxed_component_glosry.md).

**non-blocking mode**

Any statements that block the program flow are not allowed in an [ABAP programs](../abap-glossary/abenabap_program_glosry.md) that is processed in non-blocking mode. There are values of the non-blocking mode for APC and ADF.

**Non-Unicode ABAP**

Obsolete [language version](../abap-glossary/abenabap_version_glosry.md) of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) in which the [Unicode checks](../abap-glossary/abenunicode_check_glosry.md) are not effective. A program with this language version cannot be executed in [Unicode systems](../abap-glossary/abenunicode_system_glosry.md). In the current [AS ABAP](../abap-glossary/abenas_abap_glosry.md) release, only Unicode systems are supported. Therefore, Non-Unicode ABAP can no longer be used.

**non-Unicode program**

[ABAP program](../abap-glossary/abenabap_program_glosry.md) written in [ABAP language version](../abap-glossary/abenabap_version_glosry.md) Non-Unicode ABAP.

**null indicator**

[ABAP SQL indicator](../abap-glossary/abenabap_sql_indicator_glosry.md) in a structured target area of an [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) [query](../abap-glossary/abenasql_query_glosry.md). The components or bits of a null indicator indicate which columns of the result set contain the [null value](../abap-glossary/abennull_value_glosry.md) and which do not.

**null reference**

[Initial value](../abap-glossary/abeninitial_value_glosry.md) of a [reference variable](../abap-glossary/abenreference_variable_glosry.md). The null reference does not point to an [object](../abap-glossary/abenobject_glosry.md) and can be assigned to any reference variable. [Data objects](../abap-glossary/abendata_object_glosry.md) accessed using the null reference generally produce an [uncatchable exception](../abap-glossary/abenuncatchable_exception_glosry.md). Method calls using the null reference produce a [catchable exception](../abap-glossary/abencatchable_exception_glosry.md).

**numeric data object**

[Data object](../abap-glossary/abendata_object_glosry.md) that can be interpreted numerically if the content is appropriate. In addition to data objects with [numeric data types](../abap-glossary/abennumeric_data_type_glosry.md), [byte-like](../abap-glossary/abenbyte_like_data_object_glosry.md) and [character-like data objects](../abap-glossary/abencharlike_data_object_glosry.md) can also be numeric.

**numeric data type**

[Data type](../abap-glossary/abendata_type_glosry.md) whose [data objects](../abap-glossary/abendata_object_glosry.md) contain numeric values in platform-dependent encoding. These data types are [integer type](../abap-glossary/abeninteger_type_glosry.md), [packed number type](../abap-glossary/abenpacked_number_type_glosry.md), [decimal floating pointing number type](../abap-glossary/abendecfloat_type_glosry.md) and [binary floating pointing number type](../abap-glossary/abenbinfloat_type_glosry.md). The corresponding [generic data type](../abap-glossary/abengeneric_data_type_glosry.md) is [`numeric`](abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md).

**numeric expression**

Represents a numeric value. A numeric expression is a [constructor expression](../abap-glossary/abenconstructor_glosry.md), [arithmetic expression](../abap-glossary/abenarithmetic_expression_glosry.md), [table expression](../abap-glossary/abentable_expression_glosry.md), or a [function](../abap-glossary/abenfunction_glosry.md) whose return value has a [numeric data type](../abap-glossary/abennumeric_data_type_glosry.md).

**numeric expression position**

[Read position](../abap-glossary/abenread_position_glosry.md) in which not only a [numeric data object](../abap-glossary/abennumeric_data_object_glosry.md) that can be converted into the operand type can be specified, but also a [numeric expression](../abap-glossary/abennumerical_expression_glosry.md).

**numeric function**

[Built-in function](../abap-glossary/abenbuiltin_function_glosry.md) that calculates numeric values.

**numeric literal**

A [literal](../abap-glossary/abenabap_literal_glosry.md) that has a [numeric data type](../abap-glossary/abennumeric_data_type_glosry.md) and whose characters represent a numeric value.

- In general ABAP, numeric literals are [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), numeric literals can be [typed literals](../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Numeric Literals in ABAP](abap-declarations/abenuntyped_number_literals.md)

- [Literals in ABAP SQL](abap-database-access/abenabap_sql_literals.md)

- [Literals in CDS](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_literal_v2.md)

**numeric operand position**

[Operand position](../abap-glossary/abenoperand_position_glosry.md) with numeric [operand type](../abap-glossary/abenoperand_type_glosry.md), in which a [numeric data object](../abap-glossary/abennumeric_data_object_glosry.md) that can be converted into the operand type can be specified. See also [numeric expression position](../abap-glossary/abennumerical_expr_position_glosry.md).

**numeric text field**

[Character-like data object](../abap-glossary/abencharlike_data_object_glosry.md) of ABAP or elementary object of the database with a [numeric text field type](../abap-glossary/abennumeric_text_field_type_glosry.md).

**numeric text field type**

[Character-like data type](../abap-glossary/abencharlike_data_type_glosry.md) for storing [numeric texts](../abap-glossary/abennumeric_text_glosry.md) of fixed length. The associated [built-in ABAP type](../abap-glossary/abenbuiltin_abap_type_glosry.md) is [`n`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md). The [built-in DDIC types](../abap-glossary/abenbuiltin_ddic_type_glosry.md) are [`NUMC`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`ACCP`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The internal representation takes place in the [character representation](../abap-glossary/abenchar_representation_glosry.md) of the current [code page](../abap-glossary/abencodepage_glosry.md). A [data object](../abap-glossary/abendata_object_glosry.md) of this type is a [numeric text field](../abap-glossary/abennumeric_text_field_glosry.md).

**object**

[Instance](../abap-glossary/abeninstance_glosry.md) of a [type](../abap-glossary/abentype_glosry.md). Either an instance of a [class](../abap-glossary/abenclass_glosry.md) or, as a [data object](../abap-glossary/abendata_object_glosry.md), an instance of a [data type](../abap-glossary/abendata_type_glosry.md). Exists in the [internal session](../abap-glossary/abeninternal_session_glosry.md) of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) or as a shared object in the [shared memory](../abap-glossary/abenshared_memory_glosry.md). There are also persistent objects in the [database](../abap-glossary/abendatabase_glosry.md).

**object component selector**

Character `->`. Also referred to as [instance component selector](../abap-glossary/abeninstance_comp_selector_glosry.md). Each visible [component](../abap-glossary/abencomponent_glosry.md) `comp` of a [data object](../abap-glossary/abendata_object_glosry.md) or an [instance](../abap-glossary/abeninstance_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md) can be addressed using `ref->comp` if `ref` is a [reference variable](../abap-glossary/abenreference_variable_glosry.md) that refers to the object.

**object context**

Environment of an [object](../abap-glossary/abenobject_glosry.md). Determines its visibility and lifetime. Possible contexts are [procedures](../abap-glossary/abenprocedure_glosry.md), [instances](../abap-glossary/abeninstance_glosry.md) of [classes](../abap-glossary/abenclass_glosry.md), classes, and [programs](../abap-glossary/abenabap_program_glosry.md).

**object plug-in**

Object plug-ins are used to make modification-free functional [enhancements](../abap-glossary/abenenhancement_glosry.md) to ABAP programs. They are instances of [BAdI implementation classes](../abap-glossary/abenbadi_implement_class_glosry.md) and are administered by [BAdI objects](../abap-glossary/abenbadi_object_glosry.md). Object plug-ins are created when the [`GET BADI`](abap-enhancements/abapget_badi.md) statement is executed and in accordance with the filter specifications.

**object reference**

[Reference](../abap-glossary/abenreference_glosry.md) that points to an [instance](../abap-glossary/abeninstance_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md). An non-initial object reference is always a [heap reference](../abap-glossary/abenheap_reference_glosry.md). See also [weak reference](../abap-glossary/abenweak_reference_glosry.md).

**object reference variable**

[Reference variable](../abap-glossary/abenreference_variable_glosry.md) for [object references](../abap-glossary/abenobject_reference_glosry.md). Object reference variables can be either [class reference variables](../abap-glossary/abenclass_reference_variabl_glosry.md) or [interface reference variables](../abap-glossary/abeninterface_ref_variable_glosry.md).

**Object Services**

OS for short. [Interfaces](../abap-glossary/abenoo_intf_glosry.md) and [classes](../abap-glossary/abenclass_glosry.md) from the [class library](../abap-glossary/abenclass_library_glosry.md) with the prefixes `IF_OS_` and `CL_OS_`. Object services provide persistence services and transaction services that are used to manage persistent objects and object-oriented transactions. There is also a query service for finding and loading persistent objects.

**object transaction**

The transaction code of an object transaction is linked with a [method](../abap-glossary/abenmethod_glosry.md) of a local or global [class](../abap-glossary/abenclass_glosry.md). When the transaction is called, the associated program is loaded, for [instance methods](../abap-glossary/abeninstance_method_glosry.md) an [object](../abap-glossary/abenobject_glosry.md) of the class is created, and the method is executed. Object transactions can be connected to a transaction service of the Object Services.

**object type**

Description of an [object](../abap-glossary/abenobject_glosry.md) in [ABAP Objects](../abap-glossary/abenabap_objects_glosry.md). Either a [class](../abap-glossary/abenclass_glosry.md) for the entire object or [interface](../abap-glossary/abenoo_intf_glosry.md) for a part of an object. The associated [generic data type](../abap-glossary/abengeneric_data_type_glosry.md) is [`object`](abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md). Object types are either defined as [program global type](../abap-glossary/abenprogram_global_type_glosry.md) in an [ABAP program](../abap-glossary/abenabap_program_glosry.md) or as a [global type](../abap-glossary/abenglobal_type_glosry.md) in the [class library](../abap-glossary/abenclass_library_glosry.md).

**obsolete language element**

[ABAP language element](../abap-glossary/abenabap_language_element_glosry.md) that still exists in the language for reasons of downward compatibility, but should no longer be used. Most obsolete language elements are allowed only outside [classes](../abap-glossary/abenclass_glosry.md).

**offset/length specification**

Access to subareas of a [data object](../abap-glossary/abendata_object_glosry.md) by appending `[+off][(len)]` to the name of the data object.

**operand**

A component of an [ABAP statement](../abap-glossary/abenabap_statement_glosry.md) or of a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md) at an [operand position](../abap-glossary/abenoperand_position_glosry.md). An operand can be an [elementary operand](../abap-glossary/abenelementary_operand_glosry.md) or an [expression](../abap-glossary/abenexp_glosry.md).

There are different types of operands:

- [ABAP operands](../abap-glossary/abenabap_operand_glosry.md)

- [CDS operands](../abap-glossary/abencds_operand_glosry.md)

**operand position**

Position of an [ABAP statement](../abap-glossary/abenabap_statement_glosry.md) or of a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md) at which an [operand](../abap-glossary/abenoperand_glosry.md) is listed. There are [read](../abap-glossary/abenread_position_glosry.md) and [write positions](../abap-glossary/abenwrite_position_glosry.md). In an ABAP statement, such an operand position is typed with an [operand type](../abap-glossary/abenoperand_type_glosry.md) and appropriate [data objects](../abap-glossary/abendata_object_glosry.md) or [expressions](../abap-glossary/abenexpression_glosry.md) can be specified. The operand positions for the latter are [expression positions](../abap-glossary/abenexpression_position_glosry.md). Besides that there are other operand positions, where types, callable units or other external resources such as [CDS entities](../abap-glossary/abencds_entity_glosry.md) or [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) can be specified as operands.

**operand type**

[Data type](../abap-glossary/abendata_type_glosry.md) with which an [operand position](../abap-glossary/abenoperand_position_glosry.md) is typed. The operand type can be complete or generic. An [operand](../abap-glossary/abenoperand_glosry.md) must match the operand type. Depending on the statement, [type conversions](../abap-glossary/abentype_conversion_glosry.md) or [castings](../abap-glossary/abencast_casting_glosry.md) take place for incompatible operands. In [inline declarations](../abap-glossary/abeninline_declaration_glosry.md), the operand types determine the declared data type. For [constructor expressions](../abap-glossary/abenconstructor_expression_glosry.md), the operand type can be used to infer the type of the result.

**operator**

Component of an [ABAP statement](../abap-glossary/abenabap_statement_glosry.md) or of a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md) that, when combined with [operands](../abap-glossary/abenoperand_glosry.md), forms an [expression](../abap-glossary/abenexp_glosry.md). When the statement is executed, an operation is executed for two operands connected by one operator, and the result is processed further in the statement. There are [arithmetic](../abap-glossary/abenarithmetic_operator_glosry.md), [bit](../abap-glossary/abenbit_operator_glosry.md), [string](../abap-glossary/abenstring_operator_glosry.md), [Boolean](../abap-glossary/abenboolean_operator_glosry.md), [relational](../abap-glossary/abenrel_operator_glosry.md), and [assignment operators](../abap-glossary/abenassignment_operator_glosry.md). There are also operators that do not combine operands, but perform other operations in [operand positions](../abap-glossary/abenoperand_position_glosry.md). Operators of this type are the [dereferencing operator](../abap-glossary/abendereferencing_operat_glosry.md), [declarations operators](../abap-glossary/abendeclaration_operator_glosry.md), and [constructor operators](../abap-glossary/abenconstructor_operator_glosry.md). Finally, the [literal operator](../abap-glossary/abenassignment_operator_glosry.md) is used to combine two [literals](../abap-glossary/abenabap_literal_glosry.md).

**output parameter**

[Formal parameter](../abap-glossary/abenformal_parameter_glosry.md) whose value is set during the call and is made available in the [actual parameter](../abap-glossary/abenactual_parameter_glosry.md) after the call.

**output statement**

Statement for writing into a list. Output statements are `WRITE` and `ULINE`. There are also statements for positioning the list cursor.

**output stream**

*-\>* [Writer stream](../abap-glossary/abenwriter_stream_glosry.md)

**packed number literal**

A [numeric literal](../abap-glossary/abennumeric_literal_glosry.md) of [packed number type](../abap-glossary/abenpacked_number_type_glosry.md).

- In general ABAP, packed number literals are [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), packed number literals can be [typed literals](../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Numeric Literals in ABAP](abap-declarations/abenuntyped_number_literals.md)

- [Literals in ABAP SQL](abap-database-access/abenabap_sql_literals.md)

- [Literals in CDS](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_literal_v2.md)

**packed number type**

[Numeric data type](../abap-glossary/abennumeric_data_type_glosry.md) for saving [fixed point numbers](../abap-glossary/abenfixed_point_number_glosry.md) with a fixed number of [decimal places](../abap-glossary/abendecimal_place_glosry.md) The associated [built-in ABAP type](../abap-glossary/abenbuiltin_abap_type_glosry.md) is [`p`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md). The [built-in DDIC type](../abap-glossary/abenbuiltin_ddic_type_glosry.md) is [`DEC`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The number of decimal places is a property of the data type and not, as with [floating point numbers](../abap-glossary/abenfloating_point_number_glosry.md), a property of the data itself. Calculations with packed numbers are performed using [fixed point arithmetic](../abap-glossary/abenfixed_point_arithmetic_glosry.md). The internal representation uses the [BCD](../abap-glossary/abenbcd_glosry.md) format. A [data object](../abap-glossary/abendata_object_glosry.md) of a packed number type is a [packed number](../abap-glossary/abenpacked_number_glosry.md).

**parallel Remote Function Call**

pRFC for short. Extension of the asynchronous remote function call that enables parallelization to be controlled.

**parameter interface**

[Interface](../abap-glossary/abenintf_gen_glosry.md) of a [procedure](../abap-glossary/abenprocedure_glosry.md). Consists of [formal parameters](../abap-glossary/abenformal_parameter_glosry.md) and specifies the possible [exceptions](../abap-glossary/abenexception_glosry.md) of the procedure.

**pass by reference**

A method of passing data from [actual parameters](../abap-glossary/abenactual_parameter_glosry.md) to [formal parameters](../abap-glossary/abenformal_parameter_glosry.md) when a [procedure](../abap-glossary/abenprocedure_glosry.md) is called, which is defined in the [parameter interface](../abap-glossary/abenparameter_interface_glosry.md) of the procedure. Pass by reference does not create a local [data object](../abap-glossary/abendata_object_glosry.md) for the actual parameter. Instead a reference to the actual parameter is passed to the procedure and it works with the actual parameter itself. [Input parameters](../abap-glossary/abeninput_parameter_glosry.md) passed by reference must not be modified in the procedure. See also [pass by value](../abap-glossary/abenpass_by_value_glosry.md).

**pass by value**

Method of passing data from [actual parameters](../abap-glossary/abenactual_parameter_glosry.md) to [formal parameters](../abap-glossary/abenformal_parameter_glosry.md) when a [procedure](../abap-glossary/abenprocedure_glosry.md) is called, which is defined in the [parameter interface](../abap-glossary/abenparameter_interface_glosry.md) of the procedure. Pass by value creates a local [data object](../abap-glossary/abendata_object_glosry.md) as a copy of the actual parameter. [Output parameters](../abap-glossary/abenoutput_parameter_glosry.md) and [return values](../abap-glossary/abenreturn_value_glosry.md) are initialized when the procedure is called. [Input parameters](../abap-glossary/abeninput_parameter_glosry.md) and [input/output parameters](../abap-glossary/abeninput_output_parameter_glosry.md) are passed the value of the actual parameter when the procedure is called. Modified formal parameters are only passed to the actual parameter if the procedure has been processed without errors, that is, when the last statement is reached or when it is exited via [`RETURN`](abap-calling-and-exiting-program-units/abapreturn.md) (or [`EXIT`](abap-calling-and-exiting-program-units/abapexit_processing_blocks.md) or [`CHECK`](abap-calling-and-exiting-program-units/abapcheck_processing_blocks.md)). See also [pass by reference](../abap-glossary/abenpass_by_reference_glosry.md).

**path expression**

A sequence of [associations](../abap-glossary/abenassociation_glosry.md) specified at an operand position. Either an [SQL path expression](../abap-glossary/abensql_path_expression_glosry.md) or a [mesh path expression](../abap-glossary/abenmesh_path_expression_glosry.md).

**path specification**

*-\>* [Path expression](../abap-glossary/abenpath_expression_glosry.md)

**PCP**

*-\>* Push Channel Protocol

**PCRE regular expression**

[Perl Compatible Regular expression](../abap-glossary/abenpcre_glosry.md) that is expressed in [PCRE syntax](abap-processing-internal-data/abenregex_pcre_syntax.md) and processed by the [PCRE2 Library](https://www.pcre.org/) implemented in the [ABAP Kernel](../abap-glossary/abenkernel_glosry.md) or by the [PCRE1 Library](https://www.pcre.org/) of the [SAP HANA Database](../abap-glossary/abenhana_database_glosry.md). See also [XPath regular expression](../abap-glossary/abenxpath_regex_glosry.md), [XSD regular expression](../abap-glossary/abenxsd_regex_glosry.md) and [POSIX regular expression](../abap-glossary/abenposix_regex_glosry.md) (obsolete).

**Perl Compatible Regular Expression**

PCRE for short. [Regular expressions](../abap-glossary/abenregular_expression_glosry.md) using the same syntax and semantics as [Perl 5](https://www.perl.org/). In general, ABAP supports [PCRE syntax](abap-processing-internal-data/abenregex_pcre_syntax.md) for regular expressions by implementing the [PCRE2 library](https://www.pcre.org/) in the [ABAP kernel](../abap-glossary/abenkernel_glosry.md). [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) supports PCRE by using the PCRE1 library implemented in the [SAP HANA database](../abap-glossary/abenhana_database_glosry.md).

**persistence service**

An object service used for the administration of persistent objects.

**persistent class**

Special [class](../abap-glossary/abenclass_glosry.md) whose [attributes](../abap-glossary/abenattribute_glosry.md) are linked to [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) via object-relational mapping. Can be created using the Mapping Assistant in Class Builder. The [objects](../abap-glossary/abenobject_glosry.md) of persistent classes are managed by object services.

**persistent object**

[Object](../abap-glossary/abenobject_glosry.md) in a persistent class whose [attributes](../abap-glossary/abenattribute_glosry.md) are saved as database content after the runtime of an [ABAP program](../abap-glossary/abenabap_program_glosry.md). Persistent objects are managed by object services.

**physical file name**

Platform-dependent name of a file on the [AS instance](../abap-glossary/abenas_instance_glosry.md) [host computer](../abap-glossary/abenhost_computer_glosry.md). The statements of the ABAP file interface work directly with the physical file names. Physical file names can be linked to logical file names to enable platform-independent and secure programming.

**POSIX regular expression**

[Regular expression](../abap-glossary/abenregular_expression_glosry.md) in accordance with [POSIX](https://en.wikipedia.org/wiki/POSIX) standard 1003.2. ABAP supports [POSIX syntax](abap-obsolete-language-elements/abenregex_posix_syntax.md) for regular expressions by implementing the [Boost.Regex Library](http://www.boost.org/doc/libs/1_31_0/libs/regex/doc/index.html) in the [ABAP kernel](../abap-glossary/abenkernel_glosry.md). Regular expressions in POSIX syntax are obsolete in ABAP and should be migrated to [PCRE regular expressions](../abap-glossary/abenpcre_regex_glosry.md), [XPath regular expressions](../abap-glossary/abenxpath_regex_glosry.md) or [XSD regular expressions](../abap-glossary/abenxsd_regex_glosry.md).

**pragma**

[Program directive](../abap-glossary/abenprogram_directive_glosry.md) to ABAP Compiler and the extended program check to hide warnings from the [syntax check](../abap-glossary/abensyntax_check_glosry.md) and hide messages of the extended check.

**predicate**

[Relational expression](../abap-glossary/abenrelational_expression_glosry.md) qualifying an [operand](../abap-glossary/abenoperand_glosry.md). Implemented in ABAP using [predicate expressions](../abap-glossary/abenpredicate_expression_glosry.md), [predicate functions](../abap-glossary/abenpredicate_function_glosry.md), and [predicative method calls](../abap-glossary/abenpredicative_method_call_glosry.md).

**predicate expression**

[Relational expression](../abap-glossary/abenrelational_expression_glosry.md) with the [predicate operator](../abap-glossary/abenpredicate_operator_glosry.md) [`IS`](abap-program-flow-logic/abenpredicate_expressions.md).

**predicate function**

[Logical function](../abap-glossary/abenlogic_function_glosry.md) that returns a [truth value](../abap-glossary/abentruth_value_glosry.md) and can be used in the same way as a [relational expression](../abap-glossary/abenrelational_expression_glosry.md).

**predicate method**

[Functional method](../abap-glossary/abenfunctional_method_glosry.md) whose [return value](../abap-glossary/abenreturn_value_glosry.md) has the type `abap_bool` from the [type pool](../abap-glossary/abentype_pool_glosry.md) `ABAP`. A predicate method is particularly well suited for [predicative method calls](../abap-glossary/abenpredicative_method_call_glosry.md), but is not a prerequisite.

**predicate operator**

[Relational operator](../abap-glossary/abenrel_operator_glosry.md) [`IS`](abap-program-flow-logic/abenpredicate_expressions.md) for use in a [predicate expression](../abap-glossary/abenpredicate_expression_glosry.md).

**predicative method call**

Call of a [functional method](../abap-glossary/abenfunctional_method_glosry.md) as the only [ABAP operand](../abap-glossary/abenabap_operand_glosry.md) of a [relational expression](../abap-glossary/abenrelational_expression_glosry.md). The result of the relational expression is true if the result of the [functional method call](../abap-glossary/abenfunctional_method_call_glosry.md) is not initial. See also [predicate method](../abap-glossary/abenpredicate_method_glosry.md).

**prefix namespace**

[Namespace](../abap-glossary/abennamespace_glosry.md) for [repository objects](../abap-glossary/abenrepository_object_glosry.md) of SAP departments, SAP partners, and SAP customers that can be requested from SAP. The names of the repository objects of a prefix namespace are introduced with a [namespace prefix](../abap-glossary/abenname_space_prefix_glosry.md).

**pRFC**

*-\>* parallel remote function call

**primary table index**

[Table index](../abap-glossary/abentable_index_glosry.md) of [index tables](../abap-glossary/abenindex_table_glosry.md) ([standard tables](../abap-glossary/abenstandard_table_glosry.md) and [sorted tables](../abap-glossary/abensorted_table_glosry.md)). Every index table has a primary table index, administrated by the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md), which contains a unique line number for each table line. The primary table index of an index table is updated each time a line is added or deleted from an internal table.

**primary table key**

Each [internal table](../abap-glossary/abeninternal_table_glosry.md) has a primary [table key](../abap-glossary/abentable_key_glosry.md) that is either a user-defined key or the [standard key](../abap-glossary/abenstandard_key_glosry.md). In [hashed tables](../abap-glossary/abenhashed_table_glosry.md), the primary key is a [hash key](../abap-glossary/abenhash_key_glosry.md) and in [sorted tables](../abap-glossary/abensorted_table_glosry.md), the primary key is a [sorted key](../abap-glossary/abensorted_key_glosry.md). Both table types are [key tables](../abap-glossary/abenkey_table_glosry.md) for which key access is optimized, and the primary key thus has its own administration. The key fields of these tables are write-protected when individual lines are accessed. [Standard tables](../abap-glossary/abenstandard_table_glosry.md) also have a primary key, but the corresponding access is not optimized, there is no separate key administration, and the key fields are not write-protected.

**private**

Term in [ABAP Objects](../abap-glossary/abenabap_objects_glosry.md). A private [component](../abap-glossary/abenclass_component_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md) can be accessed only by the class itself and its [friends](../abap-glossary/abenfriend_glosry.md), which also only can create [objects](../abap-glossary/abenobject_glosry.md) of a class with private instances. The private [visibility section](../abap-glossary/abenvisibility_section_glosry.md) of a class is declared in its [declaration part](../abap-glossary/abendeclaration_part_glosry.md) using the statement [`PRIVATE SECTION`](abap-declarations/abapprivate.md).

**procedure**

[Processing block](../abap-glossary/abenprocessing_block_glosry.md) that can be called using an [ABAP statement](../abap-glossary/abenabap_statement_glosry.md). After ending a procedure, processing continues behind the call position in the ABAP program. A procedure has a [parameter interface](../abap-glossary/abenparameter_interface_glosry.md) and a local [data area](../abap-glossary/abendata_area_glosry.md). Possible procedures are [methods](../abap-glossary/abenmethod_glosry.md), [function modules](../abap-glossary/abenfunction_module_glosry.md), and [subroutines](../abap-glossary/abensubroutine_glosry.md).

**processing block**

Indivisible and non-nestable modularization unit of an [ABAP program](../abap-glossary/abenabap_program_glosry.md). Possible processing blocks are [procedures](../abap-glossary/abenprocedure_glosry.md), dialog modules, and [event blocks](../abap-glossary/abenevent_block_glosry.md). They contain statements that are structured into [statement blocks](../abap-glossary/abenstatement_block_glosry.md) by [control structures](../abap-glossary/abencontrol_structure_glosry.md). Each non-declarative statement in an ABAP program is part of a processing block.

**program check**

The ABAP program check includes the [syntax check](../abap-glossary/abensyntax_check_glosry.md) and the extended program check.

**program constructor**

[Event block](../abap-glossary/abenevent_block_glosry.md) initiated by the [`LOAD-OF-PROGRAM`](abap-program-structure/abapload-of-program.md) [event keyword](../abap-glossary/abenevent_keyword_glosry.md) that, except for [type pools](../abap-glossary/abentype_pool_glosry.md), [class pools](../abap-glossary/abenclass_pool_glosry.md), and [interface pools](../abap-glossary/abeninterface_pool_glosry.md), is executed when a program is loaded into an [internal session](../abap-glossary/abeninternal_session_glosry.md).

**program constructor event**

[ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) [event](../abap-glossary/abenevent_glosry.md) that occurs once only when an [ABAP program](../abap-glossary/abenabap_program_glosry.md) (not a [class pool](../abap-glossary/abenclass_pool_glosry.md)) is loaded in the [internal session](../abap-glossary/abeninternal_session_glosry.md) to call the [program constructor](../abap-glossary/abenprogram_constructor_glosry.md). The corresponding [event keyword](../abap-glossary/abenevent_keyword_glosry.md) is [`LOAD-OF-PROGRAM`](abap-program-structure/abapload-of-program.md).

**program directive**

A program directive is a special construct in [ABAP source code](../abap-glossary/abenabap_source_code_glosry.md) that modifies the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) rather than affecting the program flow directly.

**program global data**

Global data for short. [Data object](../abap-glossary/abendata_object_glosry.md) that is declared in an [ABAP program](../abap-glossary/abenabap_program_glosry.md) and is known in the entire program behind its declaration. Global data is declared in the [global declaration part](../abap-glossary/abenglobal_declaration_sect_glosry.md) of a program. See also local data.

**program global type**

[Data type](../abap-glossary/abendata_type_glosry.md) or [object type](../abap-glossary/abenobject_type_glosry.md) that is defined in an [ABAP program](../abap-glossary/abenabap_program_glosry.md) and is known in the entire program behind its declaration. Global types are declared in the [global declaration part](../abap-glossary/abenglobal_declaration_sect_glosry.md) of a program using the statements [`TYPES`](abap-declarations/abaptypes.md), [`CLASS`](abap-declarations/abapclass.md), and [`INTERFACE`](abap-declarations/abapinterface.md).

**program group**

Organizational unit of programs in the [internal session](../abap-glossary/abeninternal_session_glosry.md). There is always one main program group and multiple additional program groups. Each program group has a main program. An additional program group is always created when [function pools](../abap-glossary/abenfunction_pool_glosry.md) and [class pools](../abap-glossary/abenclass_pool_glosry.md) are loaded. If, however, using a program that is not a function pool or class pool causes the program to be loaded, it is loaded into the program group of the consumer. All programs of a program group share the interface work areas declared using `TABLES`, `NODES`, and `COMMON PART`. Within a program group, `CALL SCREEN` can call the dynpros of the main program only.

**program name**

Unique identification of an ABAP program in the [repository](../abap-glossary/abenrepository_glosry.md). A program name must consist of at least one character and can have a maximum of 30 alphanumeric characters, including underscores.

**program property**

Property of an [ABAP program](../abap-glossary/abenabap_program_glosry.md). Program properties are used to administrate the program and affect how it is handled in [syntax checks](../abap-glossary/abensyntax_check_glosry.md) and in the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md). Examples of important program properties are program type or the [ABAP language version](../abap-glossary/abenabap_version_glosry.md), which specifies whether or not a program has the ABAP language version [Standard ABAP](../abap-glossary/abenstandard_abap_glosry.md).

**program type**

[Program property](../abap-glossary/abenprogram_property_glosry.md) of an [ABAP program](../abap-glossary/abenabap_program_glosry.md). Defines which [processing blocks](../abap-glossary/abenprocessing_block_glosry.md) can be contained in a program and how the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) executes the program. Possible program types include executable program, [class pool](../abap-glossary/abenclass_pool_glosry.md), [function pool](../abap-glossary/abenfunction_pool_glosry.md), [interface pool](../abap-glossary/abeninterface_pool_glosry.md), module pool, subroutine pool, [type pool](../abap-glossary/abentype_pool_glosry.md), and [include program](../abap-glossary/abeninclude_program_glosry.md). The program type is maintained in the ABAP Editor in the program properties, or by the relevant tool.

**program-initiating statement**

The first statement in every standalone [ABAP program](../abap-glossary/abenabap_program_glosry.md).

**protected**

Term in [ABAP Objects](../abap-glossary/abenabap_objects_glosry.md). A protected [component](../abap-glossary/abenclass_component_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md) can be accessed only by the class itself or by its subclasses. Only the class itself and its subclasses can create [objects](../abap-glossary/abenobject_glosry.md) in the case of a protected instantiation. Here, [friends](../abap-glossary/abenfriend_glosry.md) of the class have the same rights as the class itself. The protected [visibility section](../abap-glossary/abenvisibility_section_glosry.md) of a class is declared in the statement [`PROTECTED SECTION`](abap-declarations/abapprotected.md) in the [declaration section](../abap-glossary/abendeclaration_part_glosry.md).

**pseudo comment**

[Program directive](../abap-glossary/abenprogram_directive_glosry.md) in the form of a special [line end comment](../abap-glossary/abenendline_comment_glosry.md). A pseudo comment begins with the expression `#EC` or `#AU` and suppresses either a message of the extended program check or of the Code Inspector, or determines the test properties for a [test class](../abap-glossary/abentest_class_glosry.md). Pseudo comments are only still required for suppressing Code Inspector messages and are otherwise obsolete.

**pseudo component**

Expression `table_line` that can be specified in accesses to [internal tables](../abap-glossary/abeninternal_table_glosry.md) instead of a [structure component](../abap-glossary/abenstructure_component_glosry.md). The entire line of the internal table is then interpreted as the only component. The name `table_line` is a reserved name. In ABAP and in [ABAP Dictionary](../abap-dictionary-ddic/abenabap_dictionary.md), no structure components called `table_line` can be defined or created.

**pseudo reference**

The identifier `super` that can be specified in the implementation of a redefined [instance method](../abap-glossary/abeninstance_method_glosry.md) or an [instance constructor](../abap-glossary/abeninstance_constructor_glosry.md) instead of a [reference variable](../abap-glossary/abenreference_variable_glosry.md) in order to call the implementation of the [method](../abap-glossary/abenmethod_glosry.md) to be called in the direct [superclass](../abap-glossary/abensuperclass_glosry.md).

**public**

Term in [ABAP Objects](../abap-glossary/abenabap_objects_glosry.md). A public [component](../abap-glossary/abenclass_component_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md) can be accessed at any point at which the class is known. In case of a public instantiation, [objects](../abap-glossary/abenobject_glosry.md) can be created at every point at which a class is known. The public [visibility section](../abap-glossary/abenvisibility_section_glosry.md) of a class is declared in its [declaration part](../abap-glossary/abendeclaration_part_glosry.md) using the statement [`PUBLIC SECTION`](abap-declarations/abappublic.md).

**qRFC**

*-\>* queued remote function call

**query service**

An object service for searching for and loading of persistent objects.

**queued Remote Function Call**

qRFC for short. Obsolete extension of the transactional remote function call enabling a call sequence to be determined.

**Rabax**

Short for Runtime exit. Rabax is an internal SAP term describing a program crash after a [runtime error](../abap-glossary/abenruntime_error_glosry.md). The corresponding [ABAP kernel](../abap-glossary/abenkernel_glosry.md) module, also called Rabax, performs the tasks required to complete the [internal session](../abap-glossary/abeninternal_session_glosry.md) and creates the associated [short dump](../abap-glossary/abenshort_dump_glosry.md).

**ranges condition**

[Comparison expressions](../abap-glossary/abencomparison_expression_glosry.md) joined from the content of a [ranges table](../abap-glossary/abenranges_table_glosry.md).

**ranges table**

[Internal table](../abap-glossary/abeninternal_table_glosry.md) with the columns `SIGN`, `OPTION`, `LOW`, and `HIGH`. Declared with the addition [`TYPE RANGE OF`](abap-declarations/abaptypes_ranges.md) of the statements [`DATA`](abap-declarations/abapdata.md) and [`TYPES`](abap-declarations/abaptypes.md), or the obsolete statement `RANGES`. A ranges table is used to store a [ranges condition](../abap-glossary/abenranges_condition_glosry.md) internally. A ranges table can be evaluated in a [comparison expression](../abap-glossary/abenrelational_expression_glosry.md) using the [comparison operator](../abap-glossary/abencomp_operator_glosry.md) [`IN`](abap-program-flow-logic/abenlogexp_select_option.md), where each line of the table represents a separate comparison. A selection table declared with `SELECT-OPTIONS` has the same structure as a ranges table.

**read position**

[Operand position](../abap-glossary/abenoperand_position_glosry.md) in which the [operand](../abap-glossary/abenoperand_glosry.md) is read only.

**read/write position**

[Write position](../abap-glossary/abenwrite_position_glosry.md) in which the [operand](../abap-glossary/abenoperand_glosry.md) is read and written..

**reader stream**

Also referred to as [input stream](../abap-glossary/abeninput_stream_glosry.md). Either a [data stream](../abap-glossary/abendata_stream_glosry.md) that is connected to a [streaming data source](../abap-glossary/abenstreaming_data_source_glosry.md) or a filter stream that reads data from another stream. The direction of a reader stream is always away from the data source. Data can only be read from a reader stream.

**redefinition**

Term in [ABAP Objects](../abap-glossary/abenabap_objects_glosry.md). In a redefinition, an [instance method](../abap-glossary/abeninstance_method_glosry.md) in a [subclass](../abap-glossary/abensubclass_glosry.md) can be reimplemented without changing the [parameter interface](../abap-glossary/abenparameter_interface_glosry.md).

**reduction operator**

[Constructor operator](../abap-glossary/abenconstructor_operator_glosry.md) [`REDUCE`](abap-program-flow-logic/abenconstructor_expression_reduce.md) for constructing a value using [iteration expressions](../abap-glossary/abeniteration_expression_glosry.md) with [`FOR`](abap-program-flow-logic/abenfor.md). See also [table reduction](../abap-glossary/abentable_reduction_glosry.md).

**reference**

Content of [reference variables](../abap-glossary/abenreference_variable_glosry.md). A valid reference refers to a [data object](../abap-glossary/abendata_object_glosry.md) ([data reference](../abap-glossary/abendata_reference_glosry.md)) or an [instance](../abap-glossary/abeninstance_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md) ([object reference](../abap-glossary/abenobject_reference_glosry.md)). References in reference variables are either [heap references](../abap-glossary/abenheap_reference_glosry.md) or [stack references](../abap-glossary/abenstack_reference_glosry.md). Internally, [strings](../abap-glossary/abenstring_glosry.md), [internal tables](../abap-glossary/abeninternal_table_glosry.md), and [boxed components](../abap-glossary/abenboxed_component_glosry.md) are also addressed via references. From a technical point of view, an object in ABAP is referenced in multiple layers. A reference is the address of an internal header (object header, string header, or table header), which contains the address of the actual object and other administrative information such as the [data type](../abap-glossary/abendata_type_glosry.md) of a referenced data object.

**reference operator**

[Constructor operator](../abap-glossary/abenconstructor_operator_glosry.md) [`REF`](abap-processing-internal-data/abenconstructor_expression_ref.md) used to construct a [data reference](../abap-glossary/abendata_reference_glosry.md) to a [data object](../abap-glossary/abendata_object_glosry.md).

**reference semantics**

Reference semantics means that the [reference](../abap-glossary/abenreference_glosry.md) itself is used when accessing a [deep](../abap-glossary/abendeep_glosry.md) [data object](../abap-glossary/abendata_object_glosry.md). In ABAP, reference semantics apply to [assignments](../abap-glossary/abenassignment_glosry.md) and [comparisons](../abap-glossary/abencomparison_glosry.md) of [reference variables](../abap-glossary/abenreference_variable_glosry.md) but not when accessing [dynamic data objects](../abap-glossary/abendynamic_data_object_glosry.md) or [field symbols](../abap-glossary/abenfield_symbol_glosry.md). See also [value semantics](../abap-glossary/abenvalue_semantics_glosry.md).

**reference type**

A reference type describes [reference variables](../abap-glossary/abenreference_variable_glosry.md), that is, the [data objects](../abap-glossary/abendata_object_glosry.md) that contain [references](../abap-glossary/abenreference_glosry.md). See also [static type](../abap-glossary/abenstatic_type_glosry.md).

**reference variable**

[Data object](../abap-glossary/abendata_object_glosry.md) that contains a [reference](../abap-glossary/abenreference_glosry.md). Reference variables are either [data reference variables](../abap-glossary/abendata_reference_variable_glosry.md) or [object reference variables](../abap-glossary/abenobject_refer_variable_glosry.md). Reference variables have a length of 8 bytes and are opaque, which means the reference cannot be accessed directly. They are typed with the addition [`REF TO`](abap-declarations/abaptypes_references.md) that defines their [static type](../abap-glossary/abenstatic_type_glosry.md). The static type is always more general than or the same as the [dynamic type](../abap-glossary/abendynamic_type_glosry.md). For assignments between reference variables, [reference semantics](../abap-glossary/abenreference_semantics_glosry.md) apply.

**relational expression**

[Expression](../abap-glossary/abenexpression_glosry.md) whose result is a [truth value](../abap-glossary/abentruth_value_glosry.md). Relational expressions include [comparison expressions](../abap-glossary/abencomparison_expression_glosry.md) and [predicates](../abap-glossary/abenpredicate_glosry.md). A single relational expression or multiple relational expressions combined using [Boolean operators](../abap-glossary/abenboolean_operator_glosry.md) form a [logical expression](../abap-glossary/abenlogical_expression_glosry.md) in ABAP.

**relative type name**

[Type name](../abap-glossary/abentype_name_glosry.md) specified when defining a [data type](../abap-glossary/abendata_type_glosry.md), a [class](../abap-glossary/abenclass_glosry.md), or an [interface](../abap-glossary/abenoo_intf_glosry.md). The identity of the actual [type](../abap-glossary/abentype_glosry.md) described by a relative type name depends on the [context](../abap-glossary/abenobj_context_glosry.md) because local definitions hide global definitions. See also [absolute type name](../abap-glossary/abenabsolute_typename_glosry.md).

**Remote Function Call**

RFC for short. Call of a [function module](../abap-glossary/abenfunction_module_glosry.md) using the RFC interface Calls be made in the same or in different systems. The target system is determined using an RFC destination. Connections are possible between different [AS ABAP](../abap-glossary/abenas_abap_glosry.md) or between an AS ABAP and an external system. In non-SAP systems, specially programmed functions whose [interface](../abap-glossary/abenintf_gen_glosry.md) simulates a function module are called in external systems instead of function modules. Function calls can be synchronous, asynchronous, or transactional.

**remote user**

[User](../abap-glossary/abenabap_user_glosry.md) that is logged on to an [AS ABAP](../abap-glossary/abenas_abap_glosry.md) via remote function call. The logon data and the [authorization](../abap-glossary/abenauthorization_glosry.md) can be declared in the RFC destination.

**remote-enabled function module**

RFM for short. [Function module](../abap-glossary/abenfunction_module_glosry.md) that is marked as *remote-enabled* in its properties and can be called using remote function call.

**repeat function**

[Processing function](../abap-glossary/abenprocess_function_glosry.md) that lengthens a string through repetition.

**replace function**

[Process function](../abap-glossary/abenprocess_function_glosry.md) that scans a string for a specified substring and replaces it with another string.

**report**

The process of reading and displaying data, for example in a list. Outdated term for an executable program that only executes reporting.

**reporting event**

[Event](../abap-glossary/abenevent_glosry.md) of the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) that occurs in executable programs when these are started via a `SUBMIT` or via a report transaction. Reporting events map the IPO principle of reporting when used with a logical database. The [event key words](../abap-glossary/abenevent_keyword_glosry.md) assigned to reporting events are `INITIALIZATION`, `START-OF-SELECTION`, `GET`, and `END-OF-SELECTION`.

**repository object**

Repository objects are development objects in the [ABAP repository](../abap-glossary/abenabap_repository_glosry.md) such as [ABAP programs](../abap-glossary/abenabap_program_glosry.md), [classes](../abap-glossary/abenclass_glosry.md), [CDS entities](../abap-glossary/abencds_entity_glosry.md), [dictionary objects](../abap-glossary/abendictionary_object_glosry.md), or [CDS objects](../abap-glossary/abencds_object_glosry.md). They are maintained using ABAP Workbench tools or [ABAP development tools for Eclipse (ADT)](../abap-glossary/abenadt_glosry.md). The names of repository objects are stored in upper case. Each repository object is assigned to a [package](../abap-glossary/abenpackage_glosry.md) and therefore has an interface to the [Change and Transport System (CTS)](../abap-glossary/abencts_glosry.md).

**restricted ABAP language version**

[ABAP language version](../abap-glossary/abenabap_version_glosry.md) that is restricted as follows:

- The ABAP language scope is limited.

- Access to other repository objects is restricted by [released APIs](../abap-glossary/abenreleased_api_glosry.md).

Restricted ABAP language versions are:

- [ABAP for Cloud Development](../abap-glossary/abenabap_for_cloud_dev_glosry.md)

- [ABAP for Key Users](../abap-glossary/abenabap_for_key_users_glosry.md)

[Standard ABAP](../abap-glossary/abenstandard_abap_glosry.md) is an [unrestricted ABAP language version](../abap-glossary/abenunrestricted_version_glosry.md).

**result position**

[Write position](../abap-glossary/abenwrite_position_glosry.md) where [writable expressions](../abap-glossary/abenwritable_expression_glosry.md) can be specified in addition to [variables](../abap-glossary/abenvariable_glosry.md).

**resumable exception**

[Class-based exception](../abap-glossary/abenclass_based_exception_glosry.md) that is raised by the addition `RESUMABLE` of the statement [`RAISE EXCEPTION`](abap-program-flow-logic/abapraise_exception_class.md) or by the addition [`THROW`](abap-program-flow-logic/abenconditional_expression_result.md) in a [conditional expression](abap-program-flow-logic/abenconditional_expressions.md). When a resumable exception is handled in a [`CATCH`](abap-program-flow-logic/abapcatch_try.md) block, processing can be resumed using the statement [`RESUME`](abap-program-flow-logic/abapresume.md) directly after the raising statement if the context of the exception still exists. The property of resumability of an exception can be lost when the exception is propagated from [procedures](../abap-glossary/abenprocedure_glosry.md) if it is not marked as resumable in all relevant [parameter interfaces](../abap-glossary/abenparameter_interface_glosry.md) by the addition `RESUMABLE` in the `RAISING` declaration of the procedures.

**return code**

Numeric value that is placed in the [system field](../abap-glossary/abensystem_field_glosry.md) [`sy-subrc`](abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md) for many [ABAP statements](../abap-glossary/abenabap_statement_glosry.md) when the statement is executed. The value 0 usually indicates a successful completion.

**return value**

The result of [functional methods](../abap-glossary/abenfunctional_method_glosry.md), [built-in functions](../abap-glossary/abenbuiltin_function_glosry.md), and [CDS scalar functions](../abap-glossary/abencds_scalar_function_glosry.md).

- In the [ABAP language](../abap-glossary/abenabala_glosry.md), the result of functional methods is the [formal parameter](../abap-glossary/abenformal_parameter_glosry.md) defined by the addition [`RETURNING`](abap-declarations/abapmethods_functional.md) of the statement [`[CLASS-]`](abap-declarations/abapclass-methods.md)[`METHODS`](abap-declarations/abapmethods.md).

- in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), the result of a CDS scalar function whose data type is defined after the addition [`RETURNS`](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_scalar_function.md).

**returning parameter**

*-\>* [return value](../abap-glossary/abenreturn_value_glosry.md)

**reverse function**

[Processing function](../abap-glossary/abenprocess_function_glosry.md) that returns a string in reverse order.

**RFC**

*-\>* remote function call

**RFC client**

Instance of a system that calls services using RFC.

**RFC destination**

An RFC destination contains the connection parameters for remote function calls. It contains the connection type, the target system, and the partner program. Connections that only affect another [AS ABAP](../abap-glossary/abenas_abap_glosry.md) can be classified as trusted systems. RFC destinations are managed statically using the transaction `SM59` or dynamically using the class `CL_DYNAMIC_DESTINATION`.

**RFC interface**

Interface for remote function calls (RFC). The RFC interface consists of an interface for [ABAP programs](../abap-glossary/abenabap_program_glosry.md) and interfaces for non-ABAP programs.

**RFC processing**

Processing of a remote function call using the RFC interface in an RFM.

**RFC server**

Instance of a system that provides services that can be called using RFC.

**RFC server group**

Group of multiple [AS instances](../abap-glossary/abenas_instance_glosry.md) of an [AS ABAP](../abap-glossary/abenas_abap_glosry.md) that are provided to process asynchronous remote function calls (RFC) concurrently. RFC server groups are created using transaction code `RZ12`.

**RFC session**

[User session](../abap-glossary/abenuser_session_glosry.md) for RFC processing. An RFC session is opened using a remote function call.

**RFM**

Remote-enabled function module *-\>*.

**root class**

[Superclass](../abap-glossary/abensuperclass_glosry.md) shared by all [subclasses](../abap-glossary/abensubclass_glosry.md) of an [inheritance tree](../abap-glossary/abeninheritance_tree_glosry.md) in [single inheritance](../abap-glossary/abensingle_inheritance_glosry.md). In [ABAP Objects](../abap-glossary/abenabap_objects_glosry.md), all [classes](../abap-glossary/abenclass_glosry.md) are subclasses of the predefined [abstract](../abap-glossary/abenabstract_glosry.md) root class [`object`](abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md).

**root object**

Special shared object. [Instance](../abap-glossary/abeninstance_glosry.md) of the area root class. A non-empty area instance version must contain a root object. The [attribute](../abap-glossary/abenattribute_glosry.md) `ROOT` of an associated area handle points to the root object, which can contain references to the other shared objects of the area instance version.

**rounding function**

[Built-in function](../abap-glossary/abenbuiltin_function_glosry.md) for rounding [decimal floating point numbers](../abap-glossary/abendecfloat_glosry.md). The possible rounding functions are `round` and `rescale`.

**runtime error**

Caused by uncatchable exceptions when a program is executed, or it can be forced by the language elements [`RAISE SHORTDUMP`](abap-program-flow-logic/abapraise_shortdump.md), [`THROW SHORTDUMP`](abap-program-flow-logic/abenconditional_expression_result.md), or [`ASSERT`](abap-program-maintenance/abapassert.md) or by [exit messages](../abap-glossary/abenexit_message_glosry.md). Every runtime error terminates the program, which in turn raises a [database rollback](../abap-glossary/abendatabase_rollback_glosry.md) and is documented by default in a [short dump](../abap-glossary/abenshort_dump_glosry.md).

**Runtime Type Creation**

RTTC for short. Creation of [data types](../abap-glossary/abendata_type_glosry.md) during program runtime. Implemented using methods of the [type description classes](../abap-glossary/abentype_class_glosry.md) of [RTTS](../abap-glossary/abenrun_time_type_services_glosry.md).

**Runtime Type Identification**

RTTI for short. Determination of [data types](../abap-glossary/abendata_type_glosry.md) during program runtime. Implemented using description methods in [type description classes](../abap-glossary/abentype_class_glosry.md). Constitutes [RTTS](../abap-glossary/abenrun_time_type_services_glosry.md) together with [RTTC](../abap-glossary/abenrun_time_type_creation_glosry.md).

**Runtime Type Services**

RTTS for short. Combination of [RTTC](../abap-glossary/abenrun_time_type_creation_glosry.md) and [RTTI](../abap-glossary/abenrun_time_type_identific_glosry.md) in a class hierarchy. The RTTS methods provide information on [data types](../abap-glossary/abendata_type_glosry.md) or [classes](../abap-glossary/abenclass_glosry.md) and [interfaces](../abap-glossary/abenoo_intf_glosry.md) of [objects](../abap-glossary/abenobject_glosry.md), or they create new data types as [type description objects](../abap-glossary/abentype_object_glosry.md). RTTS is implemented as a hierarchy of [type description classes](../abap-glossary/abentype_class_glosry.md) from which type description objects can be created.

**runtime warning**

A runtime warning indicates critical situations that may cause a [runtime error](../abap-glossary/abenruntime_error_glosry.md) during program execution, such as high memory consumption. A runtime warning creates a [short dump](../abap-glossary/abenshort_dump_glosry.md), but does not terminate the current program.

**SAP XSLT processor**

System program integrated into the [ABAP kernel](../abap-glossary/abenkernel_glosry.md) to execute [XSL transformations](../abap-glossary/abenxsl_transformation_glosry.md).

**scaling**

Property of a [decimal floating point number](../abap-glossary/abendecfloat_glosry.md). A decimal floating point number can be viewed as an integer number of a given length that is scaled by dividing through a power of 10. This defines the number of [decimal places](../abap-glossary/abendecimal_place_glosry.md). In this sense, the negative exponent of a decimal floating point number is called scaling, which is applied to the mantissa. If the scaling is positive, it is equivalent to the number of decimal places. Decimal floating point numbers with the same value can have different scaling. Operations on decimal floating point numbers usually retain the scaling and therefore the number of decimal places. A [built-in function](../abap-glossary/abenbuiltin_function_glosry.md) for changing the scaling is [`rescale`](abap-processing-internal-data/abendec_floating_point_functions.md). See also [precision](../abap-glossary/abenprecision_glosry.md).

**search function**

[Description function](../abap-glossary/abendescription_function_glosry.md) that searches a character string and returns the position of the found string.

**secondary key**

*-\>* [Secondary table key](../abap-glossary/abensecondary_table_key_glosry.md)

**secondary table index**

[Table index](../abap-glossary/abentable_index_glosry.md) for the administration of [sorted](../abap-glossary/abensorted_key_glosry.md) [secondary table keys](../abap-glossary/abensecondary_table_key_glosry.md). A secondary table index of a non-unique key is not updated immediately for each line insertion or deletion in an [internal table](../abap-glossary/abeninternal_table_glosry.md); it is only updated when the internal table is accessed via the associated secondary key.

**secondary table key**

Up to 15 secondary [table keys](../abap-glossary/abentable_key_glosry.md) can be created for each [internal table](../abap-glossary/abeninternal_table_glosry.md). Possible secondary table keys are [sorted keys](../abap-glossary/abensorted_key_glosry.md) and [hash keys](../abap-glossary/abenhash_key_glosry.md). A [secondary table index](../abap-glossary/abensecondary_table_index_glosry.md) is created internally for each sorted secondary key. When internal tables are accessed, the table key to be used must be specified.

**segment function**

[Processing function](../abap-glossary/abenprocess_function_glosry.md) that returns a segment of a string.

**selection**

*-\>* [Branch](../abap-glossary/abenbranch_glosry.md)

**selection text**

Part of the [text elements](../abap-glossary/abentext_element_glosry.md) of an [ABAP program](../abap-glossary/abenabap_program_glosry.md). A selection text or a text from the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) can be assigned to every selection parameter or selection criterion defined using `PARAMETERS` or `SELECT-OPTIONS`. It is then displayed for the corresponding input fields on the selection screen.

**self-reference**

[Object reference variable](../abap-glossary/abenobject_refer_variable_glosry.md) called [`me`](abap-built-in-types-data-objects-functions-and-constructors/abenme.md) that is predefined as a local [constant](../abap-glossary/abenconstant_glosry.md) in each [instance method](../abap-glossary/abeninstance_method_glosry.md). It always references the current [instance](../abap-glossary/abeninstance_glosry.md) in which the method is being executed. The static type of `me` is the [class](../abap-glossary/abenclass_glosry.md) in which the instance method is implemented.

**sequence**

Also referred to as a series. [Control structure](../abap-glossary/abencontrol_structure_glosry.md) consisting of a [statement block](../abap-glossary/abenstatement_block_glosry.md) that is not defined by keywords and that is executed only once without a condition.

**serialization**

Transformation of ABAP data into [XML](../abap-glossary/abenxml_glosry.md) data or [JSON](../abap-glossary/abenjson_glosry.md) data. Performed either by calling an [XSLT program](../abap-glossary/abenxsl_transformation_glosry.md) or a [Simple Transformation](../abap-glossary/abensimple_transformation_glosry.md). If [XSLT](../abap-glossary/abenxslt_glosry.md) is used, the system first creates a [canonical XML representation](../abap-glossary/abencanonical_xml_represent_glosry.md) ([asXML](../abap-glossary/abenxml_glosry.md)).

**series**

*-\>* [Sequence](../abap-glossary/abensequence_glosry.md)

**SET/GET parameter**

*-\>* SPA/GPA parameter

**SFW**

*-\>* [Switch Framework](../abap-glossary/abenswitch_framework_glosry.md)

**shared memory-enabled class**

[Class](../abap-glossary/abenclass_glosry.md) whose [instances](../abap-glossary/abeninstance_glosry.md) can be stored as shared objects in area instance versions of the [shared memory](../abap-glossary/abenshared_memory_glosry.md). Shared memory-enabled classes are defined by the addition [`SHARED MEMORY ENABLED`](abap-declarations/abapclass_options.md) of the statement `CLASS`. In particular, all area root classes must be shared memory-enabled.

**shared object**

[Instance](../abap-glossary/abeninstance_glosry.md) of a shared memory-enabled class or [anonymous data object](../abap-glossary/abenanonymous_data_object_glosry.md) that is stored in an area instance version of the [shared memory](../abap-glossary/abenshared_memory_glosry.md). A shared object is created using the addition `AREA HANDLE` of statement [`CREATE OBJECT`](abap-creating-objects-and-values/abapcreate_object.md) or [`CREATE DATA`](abap-creating-objects-and-values/abapcreate_data.md). [References](../abap-glossary/abenreference_glosry.md) to shared objects are possible in other shared objects of the same area instance version and during the connection to the respective area instance version via an area handle.

**shared objects**

Concept of storing [objects](../abap-glossary/abenobject_glosry.md) as shared objects in the [shared memory](../abap-glossary/abenshared_memory_glosry.md). The storage of [instances](../abap-glossary/abeninstance_glosry.md) of [classes](../abap-glossary/abenclass_glosry.md) and of [anonymous data objects](../abap-glossary/abenanonymous_data_object_glosry.md) is supported. Any data objects can be stored as [attributes](../abap-glossary/abenattribute_glosry.md) of classes.

**shared objects memory**

Memory area of the [shared memory](../abap-glossary/abenshared_memory_glosry.md) in which shared objects are stored in area instance versions.

**sharing**

When [assignments](../abap-glossary/abenassignment_glosry.md) are made between [dynamic data objects](../abap-glossary/abendynamic_data_object_glosry.md) ([strings](../abap-glossary/abenstring_glosry.md) and [internal tables](../abap-glossary/abeninternal_table_glosry.md) of the same type) and if these data types are [passed by value](../abap-glossary/abenpass_by_value_glosry.md), for performance reasons, only the required internal administrative entries for the string or [table body](../abap-glossary/abentable_body_glosry.md) are passed ([table sharing](../abap-glossary/abentable_sharing_glosry.md) possible only if the [line type](../abap-glossary/abenrow_type_glosry.md) itself does not contain any [table types](../abap-glossary/abentable_type_glosry.md)). Sharing is kept until one of the data objects involved is accessed and changed. At this point, the actual copy process takes place. See also [initial value sharing](../abap-glossary/abeninitial_value_sharing_glosry.md).

**shift function**

[Process function](../abap-glossary/abenprocess_function_glosry.md) that shifts the content of a string.

**short dump**

Error log that is displayed and stored after a [runtime error](../abap-glossary/abenruntime_error_glosry.md) or by a [runtime warning](../abap-glossary/abenruntime_warning_glosry.md). Stored short dumps can be called using the [ABAP dump analysis](../abap-glossary/abenabap_dump_analsyis_glosry.md) tool.

**signature**

For a [procedure](../abap-glossary/abenprocedure_glosry.md), the name, all the [formal parameters](../abap-glossary/abenformal_parameter_glosry.md) of the [parameter interface](../abap-glossary/abenparameter_interface_glosry.md), and its other properties.

**similarity function**

[Description function](../abap-glossary/abendescription_function_glosry.md) that returns the similarity of one string to another string.

**single inheritance**

[Inheritance](../abap-glossary/abeninheritance_glosry.md) method where, unlike multiple inheritance, a [class](../abap-glossary/abenclass_glosry.md) can have multiple [subclasses](../abap-glossary/abensubclass_glosry.md) but only one direct [superclass](../abap-glossary/abensuperclass_glosry.md). See also [inheritance hierarchy](../abap-glossary/abeninheritance_hierarchy_glosry.md).

**soft reference**

Reference to an [object](../abap-glossary/abenobject_glosry.md) that does not keep an object alive when the available memory becomes insufficient. The class `CL_ABAP_SOFT_REFERENCE` is intended for soft references but has not yet been implemented. See also [weak reference](../abap-glossary/abenweak_reference_glosry.md).

**sorted key**

Unique or non-unique [table key](../abap-glossary/abentable_key_glosry.md) of an [internal table](../abap-glossary/abeninternal_table_glosry.md), in which the assignment to the table lines is managed using a [table index](../abap-glossary/abentable_index_glosry.md), the key entries of which are sorted in ascending order. A sorted key is the [primary table key](../abap-glossary/abenprimary_table_key_glosry.md) of a [sorted table](../abap-glossary/abensorted_table_glosry.md) and can be assigned to all internal tables as a [secondary table key](../abap-glossary/abensecondary_table_key_glosry.md). Sorting occurs according to the [comparison rules](abap-program-flow-logic/abenlogexp_rules.md) for the data types of the key fields. When an internal table is accessed using a sorted key, the response time logarithmically depends on the number of table entries because the table is accessed using a binary search.

**sorted table**

[Table category](../abap-glossary/abentable_category_glosry.md) of an [internal table](../abap-glossary/abeninternal_table_glosry.md) that is managed using a [primary table index](../abap-glossary/abenprimary_table_index_glosry.md) and is always sorted according to its [primary table key](../abap-glossary/abenprimary_table_key_glosry.md). Sorting occurs according to the [comparison rules](abap-program-flow-logic/abenlogexp_rules.md) for the data types of the key fields. The associated [generic data type](../abap-glossary/abengeneric_data_type_glosry.md) is [`sorted table`](abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md).

**source code enhancement**

A modification-free [enhancement](../abap-glossary/abenenhancement_glosry.md) to [ABAP source code](../abap-glossary/abenabap_source_code_glosry.md), where source code plug-ins are inserted into the code at [enhancement options](../abap-glossary/abenenhancement_point_glosry.md) that are defined implicitly or explicitly using the statement `ENHANCEMENT-POINT`, or that replace an enhancement option that was explicitly defined using `ENHANCEMENT-SECTION` and `END-ENHANCEMENT-SECTION`.

**source code modularization**

Splitting of the [source code](../abap-glossary/abensource_code_glosry.md) of a program into its individual parts. The source code modularization methods applied in [ABAP programs](../abap-glossary/abenabap_program_glosry.md) are [include programs](../abap-glossary/abeninclude_program_glosry.md) and macros.

**source code plug-in**

Source code plug-ins are used to make modification-free [enhancements](../abap-glossary/abenenhancement_glosry.md) to [ABAP source code](../abap-glossary/abenabap_source_code_glosry.md). Source code plug-ins are included in code by means of the statements `ENHANCEMENT` and `ENDENHANCEMENT` and are created using the Enhancement Builder tool.

**SPA/GPA parameter**

Also referred to as SET/GET parameter. A data object in the user memory that can be accessed in [ABAP programs](../abap-glossary/abenabap_program_glosry.md). SPA/GPA parameters are set using `SET PARAMETER` and read using `GET PARAMETER`. Input fields on dynpros can be linked with SPA/GPA parameters and can be prefilled with values when the dynpro is called. Moreover, user input in such fields remains stored in the corresponding SPA/GPA parameters. The names of SPA/GPA parameters are managed in the database table `TPARA`.

**spatial data**

Data that describes the position, shape, and orientation of an object in a [spatial reference system](../abap-glossary/abenspatial_ref_system_glosry.md). This allows the visualization of the position or the movement of an object. Spatial data is often represented as 2D geometries (Cartesian coordinates) but can also include the altitude for a 3D geometry. Typical geometrical forms are points, lines, and polygons.

**spatial function**

A built-in function that can be used to access, manipulate, and analyze spatial data in ABAP SQL.

**spatial reference identifier**

SRID for short. An identifier that specifies a [spatial reference system](../abap-glossary/abenspatial_ref_system_glosry.md). The default value for the identifier of the spatial reference system is 0 and indicates a Cartesian coordinate system, i.e. 2D geometries.

**spatial reference system**

A system to define the location of an object using coordinates. This system consists of various parameters that are used to represent a geometry, such as the name of the coordinate system from which the coordinates are derived. The specification of a spatial reference system is done by a [spatial reference identifier](../abap-glossary/abenspatial_ref_identifier_glosry.md) (SRID). A spatial reference system is used to bring spatial data into context.

**sRFC**

*-\>* synchronous remote function call

**SRID**

*-\>* [spatial reference identifier](../abap-glossary/abenspatial_ref_identifier_glosry.md)

**stack**

Part of the [program memory](../abap-glossary/abenroll_area_glosry.md) in which [named data objects](../abap-glossary/abennamed_data_object_glosry.md) of programs and [procedures](../abap-glossary/abenprocedure_glosry.md) are stacked. The memory used by a procedure is released again once the procedure ends. See also [heap](../abap-glossary/abenheap_glosry.md).

**stack reference**

[Reference](../abap-glossary/abenreference_glosry.md) to an [object](../abap-glossary/abenobject_glosry.md) or part of an object in the [stack](../abap-glossary/abenstack_glosry.md). A stack reference does not keep an object alive. See also [heap reference](../abap-glossary/abenheap_reference_glosry.md).

**standalone data type**

A [data type](../abap-glossary/abendata_type_glosry.md) that is defined using the statement [`TYPES`](abap-declarations/abaptypes.md) in an [ABAP program](../abap-glossary/abenabap_program_glosry.md), as a data type of the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) or as a [CDS entity](../abap-glossary/abencds_entity_glosry.md). See also [bound data type](../abap-glossary/abenbound_data_type_glosry.md).

**Standard ABAP**

[Unrestricted ABAP language version](../abap-glossary/abenunrestricted_version_glosry.md) with unrestricted language scope and unrestricted access to [repository objects](../abap-glossary/abenrepository_object_glosry.md). For Standard ABAP, the [Unicode checks](../abap-glossary/abenunicode_check_glosry.md) are effective that are required in an [Unicode systems](../abap-glossary/abenunicode_system_glosry.md). Standard ABAP is the [ABAP language version](../abap-glossary/abenabap_version_glosry.md) for [classic ABAP](../abap-glossary/abenclassic_abap_glosry.md).

**standard key**

[Primary table key](../abap-glossary/abenprimary_table_key_glosry.md) of an [internal table](../abap-glossary/abeninternal_table_glosry.md), whose [key fields](../abap-glossary/abenkey_field_glosry.md) in a structured [line type](../abap-glossary/abenrow_type_glosry.md) are all table fields with [character-like data types](../abap-glossary/abencharlike_data_type_glosry.md) and [byte-like data types](../abap-glossary/abenbyte_like_data_typ_glosry.md). If the line type contains [substructures](../abap-glossary/abensubstructure_glosry.md), they are broken down into elementary [components](../abap-glossary/abenstructure_component_glosry.md). The standard key for non-structured line types is the entire table line, if the line type itself is not a table type. If there are no corresponding table fields, or the line type itself is a table type, the standard key of [standard tables](../abap-glossary/abenstandard_table_glosry.md) is empty or contains no key fields.

**standard table**

[Table category](../abap-glossary/abentable_category_glosry.md) of an [internal table](../abap-glossary/abeninternal_table_glosry.md) that is managed using a [primary table index](../abap-glossary/abenprimary_table_index_glosry.md) and that has no unique [primary table key](../abap-glossary/abenprimary_table_key_glosry.md). When a standard table is accessed using its primary table key, it is searched linearly. [Secondary table keys](../abap-glossary/abensecondary_table_key_glosry.md) can be defined for more efficient key access to standard tables. The associated [generic data type](../abap-glossary/abengeneric_data_type_glosry.md) is [`[standard] table`](abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md).

**standard type**

[Complete data type](../abap-glossary/abencomplete_data_type_glosry.md) used for [generically typed](../abap-glossary/abengeneric_typing_glosry.md) [field symbols](../abap-glossary/abenfield_symbol_glosry.md) or [formal parameters](../abap-glossary/abenformal_parameter_glosry.md) if their data type is required for compilation, or if a `LIKE` reference is made to a generic field symbol, to which no memory area is assigned. Different standard types are defined for replacement parameters of optional formal parameters, generically typed field symbols, and for [inline declarations](../abap-glossary/abeninline_declaration_glosry.md), where they depend on the current statement.

**start node**

- In a [ABAP SQL hierarchy](../abap-glossary/abensql_hierarchy_glosry.md), a [hierarchy node](../abap-glossary/abenhierarchy_node_glosry.md) from which a [hierarchy node navigator](../abap-glossary/abenhierarchy_node_navi_glosry.md) determines further hierarchy nodes and adds them to its result set.

- In a [mesh](../abap-glossary/abenmesh_glosry.md), a [mesh node](../abap-glossary/abenmesh_node_glosry.md) for which a [mesh association](../abap-glossary/abenmesh_association_glosry.md) is defined is the association's start node.

**start value**

Value specified when a [data object](../abap-glossary/abendata_object_glosry.md) is declared. The data object is filled with this value when it is created. The start value is set using the [`VALUE`](abap-declarations/abapdata_options.md) addition of the [`DATA`](abap-declarations/abapdata.md) statement. If the `VALUE` addition is not used, the system uses the type-specific [initial value](../abap-glossary/abeninitial_value_glosry.md).

**statement block**

Structural unit within [control structures](../abap-glossary/abencontrol_structure_glosry.md) that consists of one or more successive statements. The statements of a statement block are processed sequentially. Statement blocks can again contain control structures.

**Static ABAP with restricted object use**

Obsolete [ABAP language version](../abap-glossary/abenabap_version_glosry.md) with restricted use of [repository objects](../abap-glossary/abenrepository_object_glosry.md) in which all language elements of [Standard ABAP](../abap-glossary/abenstandard_abap_glosry.md) except dynamic language elements are allowed.

**static attribute**

[Attribute](../abap-glossary/abenattribute_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md) declared using [`CLASS-DATA`](abap-declarations/abapclass-data.md) that is valid independent of the class [instance](../abap-glossary/abeninstance_glosry.md). The content of the static attributes determines the instance-dependent state of a class.

**static box**

[Boxed component](../abap-glossary/abenboxed_component_glosry.md) for supporting [initial value sharing](../abap-glossary/abeninitial_value_sharing_glosry.md) when the initial value exists only once on the [AS instance](../abap-glossary/abenas_instance_glosry.md). A static box is declared using the `BOXED` addition when defining [substructures](../abap-glossary/abensubstructure_glosry.md) using [`TYPES`](abap-declarations/abaptypes_boxed.md) or when declaring structured [attributes](../abap-glossary/abenattribute_glosry.md) of [classes](../abap-glossary/abenclass_glosry.md) or [interfaces](../abap-glossary/abenoo_intf_glosry.md) using [`DATA`](abap-declarations/abapdata_boxed.md).

**static class**

[Class](../abap-glossary/abenclass_glosry.md) that only contains [static components](../abap-glossary/abenstatic_component_glosry.md) and no [instance components](../abap-glossary/abeninstance_component_glosry.md).

**static component**

Superordinate term for [static attribute](../abap-glossary/abenstatic_attribute_glosry.md), [static event](../abap-glossary/abenstatic_event_glosry.md), and [static method](../abap-glossary/abenstatic_method_glosry.md). The static components of a [class](../abap-glossary/abenclass_glosry.md) can be addressed using the name of the class. A class that only contains static components is referred to as a [static class](../abap-glossary/abenstatic_class_glosry.md).

**static constructor**

[Constructor](../abap-glossary/abenconstructor_glosry.md) that is declared as a [static method](../abap-glossary/abenstatic_method_glosry.md) under the name [`class_constructor`](abap-abap-objects/abenconstructor.md) in the [public](../abap-glossary/abenpublic_glosry.md) [visibility section](../abap-glossary/abenvisibility_section_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md). It is called automatically prior to the first use of the class in an [internal session](../abap-glossary/abeninternal_session_glosry.md).

**static data object**

[Data object](../abap-glossary/abendata_object_glosry.md) for which all attributes, including memory use, are specified statically by the [data type](../abap-glossary/abendata_type_glosry.md). Apart from [reference variables](../abap-glossary/abenreference_variable_glosry.md), all static data objects are [flat](../abap-glossary/abenflat_glosry.md). See also [dynamic data object](../abap-glossary/abendynamic_data_object_glosry.md).

**static event**

[Event](../abap-glossary/abenevent_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md) declared using [`CLASS-EVENTS`](abap-declarations/abapclass-events.md) that can be raised independently of a class [instance](../abap-glossary/abeninstance_glosry.md).

**static method**

[Method](../abap-glossary/abenmethod_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md) declared using [`CLASS-METHODS`](abap-declarations/abapclass-methods.md) that can be used independently of a class [instance](../abap-glossary/abeninstance_glosry.md). Static methods can only access [static attributes](../abap-glossary/abenstatic_attribute_glosry.md) and [static events](../abap-glossary/abenstatic_event_glosry.md) of their own class.

**static type**

[Data type](../abap-glossary/abendata_type_glosry.md) of a [reference variable](../abap-glossary/abenreference_variable_glosry.md) ([reference type](../abap-glossary/abenreference_type_glosry.md)). It determines the [objects](../abap-glossary/abenobject_glosry.md) a reference variable can point to. For [object reference variables](../abap-glossary/abenobject_refer_variable_glosry.md), the static type is a [class](../abap-glossary/abenclass_glosry.md) or an [interface](../abap-glossary/abenoo_intf_glosry.md). For [data reference variables](../abap-glossary/abendata_reference_variable_glosry.md), the static type is a data type. The static type is always more general than or the same as the [dynamic type](../abap-glossary/abendynamic_type_glosry.md).

**status message**

[Message](../abap-glossary/abenmessage_glosry.md) of [message type](../abap-glossary/abenmessage_type_glosry.md) `S`. Status messages are displayed in the status bar of the GUI window of the next dynpro in the.

**step**

*-\>* background task

**stopping point**

*-\>* [Breakpoint](../abap-glossary/abenbreakpoint_glosry.md)

**stored procedure**

[Database procedure](../abap-glossary/abendatabase_procedure_glosry.md). Procedural [database object](../abap-glossary/abendb_object_glosry.md) that can be implemented and called depending on the platform. A stored procedure generally combines sequences of multiple [SQL](../abap-glossary/abensql_glosry.md) statements and contains additional instructions for controlling the sequence. [ABAP-managed](../abap-glossary/abenabap_managed_db_object_glosry.md) stored procedures are [AMDP procedures](../abap-glossary/abenamdp_procedure_glosry.md) and [AMDP functions](../abap-glossary/abenamdp_function_glosry.md).

**stream direction**

Property of a [stream](../abap-glossary/abenstream_glosry.md). Either a [reader stream](../abap-glossary/abenreader_stream_glosry.md) or a [writer stream](../abap-glossary/abenwriter_stream_glosry.md).

**streaming data sink**

Repository in which a writer [data stream](../abap-glossary/abendata_stream_glosry.md) stores its data in [streaming](../abap-glossary/abenstreaming_glosry.md). A streaming data sink can be an external resource such as a [LOB](../abap-glossary/abenlob_glosry.md) column of a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) or a file, or an internal resource such as a [string](../abap-glossary/abenstring_glosry.md) or an [internal table](../abap-glossary/abeninternal_table_glosry.md). [Streaming](../abap-glossary/abenstreaming_glosry.md) is currently implemented for [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md), [strings](../abap-glossary/abenstring_glosry.md), and [internal tables](../abap-glossary/abeninternal_table_glosry.md).

**streaming data source**

Repository from which a reader [data stream](../abap-glossary/abendata_stream_glosry.md) takes its data in [streaming](../abap-glossary/abenstreaming_glosry.md). A streaming data source can be an external resource such as a [LOB](../abap-glossary/abenlob_glosry.md) column of a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) or a file, or an internal resource such as a [string](../abap-glossary/abenstring_glosry.md) or an [internal table](../abap-glossary/abeninternal_table_glosry.md). [Streaming](../abap-glossary/abenstreaming_glosry.md) is currently implemented for [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md), [strings](../abap-glossary/abenstring_glosry.md), and [internal tables](../abap-glossary/abeninternal_table_glosry.md).

**string**

[Dynamic data object](../abap-glossary/abendynamic_data_object_glosry.md) of variable length, either a [text string](../abap-glossary/abentext_string_glosry.md) or a [byte string](../abap-glossary/abenbyte_string_glosry.md).

**string function**

[Built-in function](../abap-glossary/abenbuiltin_function_glosry.md) that processes [strings](../abap-glossary/abenstring_glosry.md). There are [character string functions](../abap-glossary/abencstring_function_glosry.md) and [byte chain functions](../abap-glossary/abenbyte_chain_function_glosry.md).

**string literal**

Either [text string literal](../abap-glossary/abentext_string_literal_glosry.md) or [byte string literal](../abap-glossary/abenbyte_string_literal_glosry.md).

**string operator**

Combines two character-like [operands](../abap-glossary/abenabap_operand_glosry.md) in a [string expression](../abap-glossary/abenstring_expression_glosry.md). The only string operator currently possible is the [concatenation operator](../abap-glossary/abenconcatenation_operator_glosry.md) [`&&`](abap-processing-internal-data/abenstring_operators.md), which concatenates the two operands into one string.

**structural fragment view**

Fragment View for short. Splits [structures](../abap-glossary/abenstructure_glosry.md) into [alignment gaps](../abap-glossary/abenalignment_gap_glosry.md), [character-like](../abap-glossary/abencharlike_data_object_glosry.md) and [byte-like](../abap-glossary/abenbyte_like_data_object_glosry.md) areas, [numeric data objects](../abap-glossary/abennumeric_data_object_glosry.md), [strings](../abap-glossary/abenstring_glosry.md), [time stamp fields](../abap-glossary/abentimestamp_field_glosry.md), [reference variables](../abap-glossary/abenreference_variable_glosry.md), and [internal tables](../abap-glossary/abeninternal_table_glosry.md).

**structure**

[Data object](../abap-glossary/abendata_object_glosry.md) with a [structured type](../abap-glossary/abenstructured_type_glosry.md) that consists of [structure components](../abap-glossary/abenstructure_component_glosry.md). In [ABAP programs](../abap-glossary/abenabap_program_glosry.md), whole structures or just components of structures can be accessed. Structures that contain only [character-like](../abap-glossary/abencharlike_data_object_glosry.md), [flat](../abap-glossary/abenflat_glosry.md) [components](../abap-glossary/abenstructure_component_glosry.md) can also be handled like [elementary data objects](../abap-glossary/abenelementary_data_object_glosry.md).

**structure component**

A [component](../abap-glossary/abencomponent_glosry.md) of a [structure](../abap-glossary/abenstructure_glosry.md).

**structure component selector**

Character `-`. A [structure component](../abap-glossary/abenstructure_component_glosry.md) `comp` of a [structure](../abap-glossary/abenstructure_glosry.md) `struc` can be addressed using `struc-comp`.

**structured type**

[Data type](../abap-glossary/abendata_type_glosry.md) of a [structure](../abap-glossary/abenstructure_glosry.md). It contains other data types as [structure components](../abap-glossary/abenstructure_component_glosry.md). A named structured type is either defined as a [DDIC structure](../abap-glossary/abenddic_structure_glosry.md), a [CDS entity](../abap-glossary/abencds_entity_glosry.md) or inside an [ABAP program](../abap-glossary/abenabap_program_glosry.md) using the statement [`TYPES BEGIN OF`](abap-declarations/abaptypes_struc.md).

**subclass**

[Class](../abap-glossary/abenclass_glosry.md) that is derived by [inheritance](../abap-glossary/abeninheritance_glosry.md) from a [superclass](../abap-glossary/abensuperclass_glosry.md).

**subroutine**

Obsolete [procedure](../abap-glossary/abenprocedure_glosry.md) that can be defined in any [ABAP program](../abap-glossary/abenabap_program_glosry.md) (except [type pools](../abap-glossary/abentype_pool_glosry.md), [class pools](../abap-glossary/abenclass_pool_glosry.md), and [interface pools](../abap-glossary/abeninterface_pool_glosry.md)), however, can only be implemented outside [classes](../abap-glossary/abenclass_glosry.md) between the statements [`FORM`](abap-obsolete-language-elements/abapform.md) and [`ENDFORM`](abap-obsolete-language-elements/abapform.md). The statement [`PERFORM`](abap-calling-and-exiting-program-units/abapperform.md) can be used to call the subroutines of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) and of any other programs.

**subroutine pool**

[ABAP program](../abap-glossary/abenabap_program_glosry.md) that usually contains [subroutines](../abap-glossary/abensubroutine_glosry.md) that are called from other ABAP programs. It does not support its own dynpros.

**substring function**

[Processing function](../abap-glossary/abenprocess_function_glosry.md) that returns a substring of a string.

**substructure**

Structured [component](../abap-glossary/abenstructure_component_glosry.md) of a [nested structure](../abap-glossary/abennested_structure_glosry.md). The direct predecessor of a substructure is its [superstructure](../abap-glossary/abensuperstructure_glosry.md). A substructure can be declared as a [boxed component](../abap-glossary/abenboxed_component_glosry.md).

**subtraction assignment operator**

[Calculation assignment operator](../abap-glossary/abencalc_assignment_op_glosry.md) `-=` that subtracts values in an assignment.

**superclass**

[Class](../abap-glossary/abenclass_glosry.md) from which [subclasses](../abap-glossary/abensubclass_glosry.md) are derived through [inheritance](../abap-glossary/abeninheritance_glosry.md).

**superstructure**

Direct predecessor of a [substructure](../abap-glossary/abensubstructure_glosry.md) in a [nested structure](../abap-glossary/abennested_structure_glosry.md).

**synchronous Remote Function Call**

sRFC for short. Remote function call in which the calling program waits for the end of processing of the remotely called function.

**syntax check**

Static check performed on [ABAP source code](../abap-glossary/abenabap_source_code_glosry.md) to check whether the syntax is formally correct. The syntax check is called in the ABAP Editor via *Program -\> Check -\> Syntax* or via the statement `SYNTAX-CHECK`. An automatic syntax check that checks the source code while it is entered can be configured in the [ABAP development tools for Eclipse (ADT)](../abap-glossary/abenadt_glosry.md).

**syntax error**

Violation of the ABAP syntax rules. A program that has syntax errors cannot be executed. Syntax errors are returned after the [syntax check](../abap-glossary/abensyntax_check_glosry.md) that can be called in ABAP Editor.

**system class**

[Class](../abap-glossary/abenclass_glosry.md) of the [class library](../abap-glossary/abenclass_library_glosry.md) in which language-related functionality is implemented. Its name usually starts with `CL_ABAP_`, `CL_SYSTEM_`, or `CX_SY_` (in the case of [exception classes](../abap-glossary/abenexception_class_glosry.md)). An overview of all ABAP system classes can be displayed using the corresponding [input help](../abap-glossary/abeninput_help_glosry.md) of the Class Builder.

**system command injection**

Injection of malicious operating system statements by an attacker. System command injections are possible whenever programs use external statements or parts of statements that are transferred to the operating system without being checked or escaped.

**system field**

A built-in [data object](../abap-glossary/abendata_object_glosry.md) that is filled depending on the context by the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) and analyzed in the program.

**system interface**

[Interface](../abap-glossary/abenclass_glosry.md) of the [class library](../abap-glossary/abenclass_library_glosry.md) that is included in [system classes](../abap-glossary/abensystem_class_glosry.md) and is used to implement system functions in separate classes or is required as a [tag interface](../abap-glossary/abentag_interface_glosry.md). The name usually begins with `IF_ABAP_` or `IF_SYSTEM_`. Using the [input help](../abap-glossary/abeninput_help_glosry.md) for`IF_ABAP_*` or `IF_SYSTEM_*` in the Class Builder can give an overview of all system interfaces.

**system program**

[ABAP program](../abap-glossary/abenabap_program_glosry.md) that is part of the [AS ABAP](../abap-glossary/abenas_abap_glosry.md) infrastructure. System programs generally work with data from client-independent [system tables](../abap-glossary/abensystem_table_glosry.md), but also with data of special [clients](../abap-glossary/abenclient_glosry.md).

**system time**

[Local time](../abap-glossary/abenlocal_time_glosry.md) in the [system time zone](../abap-glossary/abensystem_time_zone_glosry.md) of the [AS ABAP](../abap-glossary/abenas_abap_glosry.md).

**table body**

All lines in an [internal table](../abap-glossary/abeninternal_table_glosry.md). Internal table and table body are identical for internal tables without a [header line](../abap-glossary/abenheader_line_glosry.md). For internal tables with a header line, the table body denotes the actual tabular data and can be addressed by attaching `[]` to the table name.

**table category**

[Technical type property](../abap-glossary/abentechnical_type_prpt_glosry.md) of a [table type](../abap-glossary/abentable_type_glosry.md) that specifies the storage and primary access method. Table categories include [standard tables](../abap-glossary/abenstandard_table_glosry.md), [sorted tables](../abap-glossary/abensorted_table_glosry.md), and [hashed tables](../abap-glossary/abenhashed_table_glosry.md).

**table comprehension**

Creates the content of an [internal table](../abap-glossary/abeninternal_table_glosry.md) by evaluating one or more tables using [table iterations](../abap-glossary/abentable_iteration_glosry.md) with [iteration expressions](../abap-glossary/abeniteration_expression_glosry.md) within a [constructor expression](../abap-glossary/abenconstructor_expression_glosry.md) with the [instance operator](../abap-glossary/abeninstance_operator_glosry.md) [`NEW`](abap-creating-objects-and-values/abennew_constructor_params_itab.md) or the [value operator](../abap-glossary/abenvalue_operator_glosry.md) [`VALUE`](abap-creating-objects-and-values/abenvalue_constructor_params_itab.md).

**table expression**

A table expression reads a line from an [internal table](../abap-glossary/abeninternal_table_glosry.md) and returns it as a result. [Mesh path expressions](../abap-glossary/abenmesh_path_expression_glosry.md) are a special form of table expressions that can be used in the same way as table expressions.

**table filtering**

Creates the content of an [internal table](../abap-glossary/abeninternal_table_glosry.md) by filtering the lines of an internal table in a [constructor expression](../abap-glossary/abenconstructor_expression_glosry.md) with the [filter operator](../abap-glossary/abenfilter_operator_glosry.md) [`FILTER`](abap-processing-internal-data/abenconstructor_expression_filter.md).

**table index**

An [index](../abap-glossary/abenindex_glosry.md) of an [internal table](../abap-glossary/abeninternal_table_glosry.md) managed by the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md). A [primary table index](../abap-glossary/abenprimary_table_index_glosry.md) is used for [index tables](../abap-glossary/abenindex_table_glosry.md) and [secondary table indexes](../abap-glossary/abensecondary_table_index_glosry.md) are used for the management of [sorted](../abap-glossary/abensorted_key_glosry.md) [secondary table keys](../abap-glossary/abensecondary_table_index_glosry.md). The line numbers of every table index start at 1 and run consecutively with no gaps up to the current number of lines in the table. If necessary, the physical index is changed to a logical index, which increases runtime demand. The logical index is created in exactly the moment in which a line is inserted before another line, the order of the table lines is changed, or if any line except for the bottom line is deleted.

**table iteration**

Sequential evaluation of an [internal table](../abap-glossary/abeninternal_table_glosry.md). Either in a [loop](../abap-glossary/abenloop_glosry.md) introduced using [`LOOP AT`](abap-processing-internal-data/abaploop_at_itab_variants.md) or `PROVIDE` or with the corresponding [variants](abap-processing-internal-data/abenfor_itab.md) of an [iteration expression](../abap-glossary/abeniteration_expression_glosry.md).

**table key**

Columns of an [internal table](../abap-glossary/abeninternal_table_glosry.md) or [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) whose content identifies table lines. For internal tables, distinction is made between [primary table keys](../abap-glossary/abenprimary_table_key_glosry.md) and [secondary table keys](../abap-glossary/abensecondary_table_key_glosry.md), which are [technical type properties](../abap-glossary/abentechnical_type_prpt_glosry.md) of the [table type](../abap-glossary/abentable_type_glosry.md).

**table parameter**

An obsolete [formal parameter](../abap-glossary/abenformal_parameter_glosry.md) of [function modules](../abap-glossary/abenfunction_module_glosry.md) or [subroutines](../abap-glossary/abensubroutine_glosry.md) typed as a [standard table](../abap-glossary/abenstandard_table_glosry.md) with a [header line](../abap-glossary/abenheader_line_glosry.md). A table parameter is defined using the addition `TABLES` to the statements [`FUNCTION`](abap-program-structure/abenfunction.md) and [`FORM`](abap-obsolete-language-elements/abapform.md).

**table reduction**

Creates the content of a [data object](../abap-glossary/abendata_object_glosry.md) by evaluating one or more [internal tables](../abap-glossary/abeninternal_table_glosry.md) using [table iterations](../abap-glossary/abentable_iteration_glosry.md) with [iteration expressions](../abap-glossary/abeniteration_expression_glosry.md) in a [constructor expression](../abap-glossary/abenconstructor_expression_glosry.md) with the [reduction operator](../abap-glossary/abenreduce_operator_glosry.md) [`REDUCE`](abap-program-flow-logic/abenconstructor_expression_reduce.md). This usually reduces the content of the internal table to a less complex data object.

**table sharing**

[Sharing](../abap-glossary/abensharing_glosry.md) of [internal tables](../abap-glossary/abeninternal_table_glosry.md) in [assignments](../abap-glossary/abenassignment_glosry.md) and [pass by value](../abap-glossary/abenpass_by_value_glosry.md). Table sharing only occurs between similar tables if their [line types](../abap-glossary/abenrow_type_glosry.md) do not themselves contain any [table types](../abap-glossary/abentable_type_glosry.md).

**table type**

[Data type](../abap-glossary/abendata_type_glosry.md) of an [internal table](../abap-glossary/abeninternal_table_glosry.md). Defines the [line type](../abap-glossary/abenrow_type_glosry.md), [table category](../abap-glossary/abentable_category_glosry.md), and [table key](../abap-glossary/abentable_key_glosry.md) of an internal table, as well as an [initial memory requirement](../abap-glossary/abeninitial_mem_req_glosry.md). The table type can be [generic](../abap-glossary/abengeneric_data_type_glosry.md) with regard to the key. A table type can either be defined in [ABAP programs](../abap-glossary/abenabap_program_glosry.md) using the addition [`TABLE OF`](abap-declarations/abaptypes_itab.md) or as a [DDIC table type](../abap-dictionary-ddic/ddic-data-types/abenddic_table_types.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md).

**table work area**

Structured interface work area that is declared using the statements `TABLES` or `NODES` with reference to an identically named structure or [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) of the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md).

**tag interface**

Special predefined global interface. By implementing or including a tag interface, [classes](../abap-glossary/abenclass_glosry.md) or other [interfaces](../abap-glossary/abenoo_intf_glosry.md) are particularly tagged for the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md). A tag interface generally does not contain its own [interface components](../abap-glossary/abeninterface_component_glosry.md) but instead assigns a particular task to the integrating classes or interfaces and changes the way they are handled by the ABAP Compiler.

**technical type name**

Internal name of a of a [data type](../abap-glossary/abendata_type_glosry.md) that only exists as a [bound data type](../abap-glossary/abenbound_data_type_glosry.md) of a [data object](../abap-glossary/abendata_object_glosry.md). A technical type name can be part of an [absolute type name](../abap-glossary/abenabsolute_typename_glosry.md) and retrieved by [RTTI](../abap-glossary/abenrun_time_type_identific_glosry.md). [RTTI](../abap-glossary/abenrun_time_type_identific_glosry.md). In the ABAP language version [ABAP for Cloud Development](../abap-glossary/abenabap_for_cloud_dev_glosry.md) it cannot be used in dynamic type specifications.

**technical type property**

Property of a [data type](../abap-glossary/abendata_type_glosry.md) that is important for the [compatibility](../abap-glossary/abencompatible_glosry.md) with other data types except [reference types](../abap-glossary/abenreference_type_glosry.md). For [elementary data types](../abap-glossary/abenelementary_data_type_glosry.md), this concerns the [built-in ABAP type](../abap-glossary/abenbuiltin_abap_type_glosry.md), the length of the [fraction portion](../abap-glossary/abendecimal_place_glosry.md) and the number of decimal places. For [structured types](../abap-glossary/abenstructured_type_glosry.md), this concerns how the type is constructed from [substructures](../abap-glossary/abensubstructure_glosry.md) and elementary data types. For [table types](../abap-glossary/abentable_type_glosry.md), this concerns the [table category](../abap-glossary/abentable_category_glosry.md), the [line type](../abap-glossary/abenrow_type_glosry.md), and the [table key](../abap-glossary/abentable_key_glosry.md). For [mesh types](../abap-glossary/abenmesh_type_glosry.md), this concerns the layout of components and their [mesh associations](../abap-glossary/abenmesh_association_glosry.md).

**termination message**

[Message](../abap-glossary/abenmessage_glosry.md) of [message type](../abap-glossary/abenmessage_type_glosry.md) *A*. Termination messages are displayed in a dialog box, create a [database rollback](../abap-glossary/abendatabase_rollback_glosry.md), and terminate the running program.

**test class**

A test class in a narrower sense is a special local or global [class](../abap-glossary/abenclass_glosry.md) in which tests for [ABAP Unit](../abap-glossary/abenabap_unit_glosry.md) are implemented in the form of test methods. [Test methods](../abap-glossary/abentest_method_glosry.md) can be implemented in a test class. A test class groups together related tests that use the same [fixture](../abap-glossary/abenfixture_glosry.md). Test classes are defined using the [`FOR TESTING`](abap-program-maintenance/abapclass_for_testing.md) addition of the [`CLASS`](abap-declarations/abapclass_definition.md) statement. Test classes can only be used as part of [test runs](../abap-glossary/abentest_run_glosry.md) and, by default, are not generated in production systems. Test doubles and other auxiliary classes required for testing should also be defined with [`FOR TESTING`](abap-program-maintenance/abapclass_for_testing.md) but do not contain any test methods and are not test classes in a narrower sense.

**test include**

Special include program in which the [test classes](../abap-glossary/abentest_class_glosry.md) of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) are listed. Except for test includes for [class pools](../abap-glossary/abenclass_pool_glosry.md) and [function pools](../abap-glossary/abenfunction_pool_glosry.md) no test includes can currently be created. The associated ABAP Workbench tools or [ABAP development tools for Eclipse (ADT)](../abap-glossary/abenadt_glosry.md) access the associated test include automatically. The name of the test include of a class pool ends with `CCAU` and the name of a function pool ends with `T99`. For other programs, the naming convention of the test include is the name of the program that is padded with `=` up to and including the 34th position and ending in `T`.

**test method**

Special [instance method](../abap-glossary/abeninstance_method_glosry.md) of a [test class](../abap-glossary/abentest_class_glosry.md) in which a test is implemented. Test methods are defined using the addition [`FOR TESTING`](abap-program-maintenance/abapmethods_testing.md) of the statement [`METHODS`](abap-declarations/abapmethods.md), and called during a [test run](../abap-glossary/abentest_run_glosry.md) of the [ABAP Unit](../abap-glossary/abenabap_unit_glosry.md) tool.

**test relation**

Relation between a [test class](../abap-glossary/abentest_class_glosry.md) or a [test method](../abap-glossary/abentest_method_glosry.md) and another [repository object](../abap-glossary/abenrepository_object_glosry.md). A test relation is defined by the special [ABAP Doc comment](../abap-glossary/abenabap_doc_comment_glosry.md) [`"! @testing`](abap-program-maintenance/abentest_relations.md) and allows repository objects to be tested with [ABAP Unit](../abap-glossary/abenabap_unit_glosry.md) in [ADT](../abap-glossary/abenadt_glosry.md) that do not support test classes themselves.

**test run**

Execution of a [test task](../abap-glossary/abentest_task_glosry.md) in [ABAP Unit](../abap-glossary/abenabap_unit_glosry.md). Test runs for test tasks of an individual program can be started directly in the corresponding editor via *Program* or *Function Module -\> Test -\> Unit Test* or *Class -\> Unit Test*. More extensive test runs can be executed using Code Inspector. The results of a test run are displayed in the ABAP Unit interface.

**test seam**

[Seam](../abap-glossary/abenseam_glosry.md) enclosed by the statements [`TEST-SEAM`](abap-program-maintenance/abaptest-seam.md) and [`END-TEST-SEAM`](abap-program-maintenance/abapend-test-seam.md) in production code and replaced by an [injection](../abap-glossary/abeninjection_glosry.md) when [unit tests](../abap-glossary/abenunit_test_glosry.md) are executed.

**test task**

Combination of tests of one or more ABAP programs in [ABAP Unit](../abap-glossary/abenabap_unit_glosry.md) for which a [test run](../abap-glossary/abentest_run_glosry.md) can be executed.

**text element**

Component of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) that contains texts that can be accessed in the ABAP program. The possible text elements are text symbols, [list headers](../abap-glossary/abentext_symbol_glosry.md) (standard page headers), and selection texts The text elements are created in multilingual [text pools](../abap-glossary/abentext_pool_glosry.md) of the program and can be used by loading a text pool in the program. Text elements are maintained using the transaction code `SE32`.

**text environment**

The text environment is part of the [language settings](../abap-glossary/abenlanguage_setting_glosry.md) of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) and consists of a [text environment language](../abap-glossary/abentext_env_langu_glosry.md), the [system code page](../abap-glossary/abensystem_codepage_glosry.md), and a [locale](../abap-glossary/abenlocale_glosry.md). All programs of an [internal session](../abap-glossary/abeninternal_session_glosry.md) have a common text environment.

**text field**

[Character-like data object](../abap-glossary/abencharlike_data_object_glosry.md) of ABAP or elementary object of the database with a [text field type](../abap-glossary/abentext_field_type_glosry.md).

In dynpros, a text field is a screen element that is used purely for displaying text and on which no user actions are possible. A text field of a dynpro is not linked to a dynpro field.

**text field literal**

A [character literal](../abap-glossary/abencharacter_literal_glosry.md) of the [text field type](../abap-glossary/abentext_field_type_glosry.md) [`c`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) or [`CHAR`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the length of the specified characters. A text field literal can be linked to a [text symbol](../abap-glossary/abentext_symbol_glosry.md).

- In general ABAP, text field literals are [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md) delimited by single quotes.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), text field literals can be [typed literals](../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Character Literals in ABAP](abap-declarations/abenuntyped_character_literals.md)

- [Literals in ABAP SQL](abap-database-access/abenabap_sql_literals.md)

- [Literals in CDS](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_literal_v2.md)

**text field type**

[Character-like data type](../abap-glossary/abencharlike_data_type_glosry.md) for storing [character strings](../abap-glossary/abencharacter_string_glosry.md) of fixed length. The associated [built-in ABAP type](../abap-glossary/abenbuiltin_abap_type_glosry.md) is [`c`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md). The [built-in DDIC types](../abap-glossary/abenbuiltin_ddic_type_glosry.md) are [`CHAR`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`LCHR`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The internal representation takes place in the [character representation](../abap-glossary/abenchar_representation_glosry.md) of the current [code page](../abap-glossary/abencodepage_glosry.md). A [data object](../abap-glossary/abendata_object_glosry.md) of a text field type is a [text field](../abap-glossary/abentext_field_glosry.md).

**text literal**

*-\>* [Character literal](../abap-glossary/abencharacter_literal_glosry.md)

**text pool**

Component of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) that contains the [text elements](../abap-glossary/abentext_element_glosry.md) of the program. Multiple text pools can be defined in various languages for a program.

**text string**

[Character-like data object](../abap-glossary/abencharlike_data_object_glosry.md) of ABAP or elementary object of the database with a [text string type](../abap-glossary/abentext_string_type_glosry.md).

**text string literal**

A [character literal](../abap-glossary/abencharacter_literal_glosry.md) of the [text string](../abap-glossary/abentext_string_type_glosry.md) type [`string`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md).

- In general ABAP, text string literals are [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md) delimited by backquotes.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), text string literals can be [typed literals](../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Character Literals in ABAP](abap-declarations/abenuntyped_character_literals.md)

- [Literals in ABAP SQL](abap-database-access/abenabap_sql_literals.md)

- [Literals in CDS](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_literal_v2.md)

**text string type**

[Character-like data type](../abap-glossary/abencharlike_data_type_glosry.md) for storing [character strings](../abap-glossary/abencharacter_string_glosry.md) of variable length. The associated [built-in ABAP type](../abap-glossary/abenbuiltin_abap_type_glosry.md) is [`string`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md). The [built-in DDIC types](../abap-glossary/abenbuiltin_ddic_type_glosry.md) are [`STRING`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`SSTRING`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The internal representation takes place in the [character representation](../abap-glossary/abenchar_representation_glosry.md) of the current [code page](../abap-glossary/abencodepage_glosry.md). Internal administration takes place using an internal [reference](../abap-glossary/abenreference_glosry.md) and the data type is [deep](../abap-glossary/abendeep_glosry.md). A [data object](../abap-glossary/abendata_object_glosry.md) of a text field type is a [text string](../abap-glossary/abentext_string_glosry.md).

**text symbol**

[Named data object](../abap-glossary/abennamed_data_object_glosry.md) of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) maintained as part of the [text elements](../abap-glossary/abentext_element_glosry.md) of the program and addressed in the program using the name `text-idf`.

**text-like data type**

[Data type](../abap-glossary/abendata_type_glosry.md) whose [data objects](../abap-glossary/abendata_object_glosry.md) contain texts. The corresponding [built-in data types](../abap-glossary/abenbuiltin_data_type_glosry.md) are [`c`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) and [`string`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md). The corresponding [generic data type](../abap-glossary/abengeneric_data_type_glosry.md) is [`csequence`](abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md).

**time field**

[Data object](../abap-glossary/abendata_object_glosry.md) of [time type](../abap-glossary/abentime_type_glosry.md) [`t`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md) for storing a character-like [time](../abap-glossary/abenday_time_glosry.md). Valid values have the format *hhmmss*. The internal representation takes place in the [character representation](../abap-glossary/abenchar_representation_glosry.md) of the current [code page](../abap-glossary/abencodepage_glosry.md). For assignments, data objects with [numeric data types](../abap-glossary/abennumeric_data_type_glosry.md) and for calculations, the content of the time field is converted to the number of seconds since 00:00:00.

**time stamp**

Combined [date](../abap-glossary/abendate_glosry.md)/[time](../abap-glossary/abentime_glosry.md) specification for determining a point in time. Time stamps of the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) are [POSIX time stamps](../abap-glossary/abenposix_timestamp_glosry.md) independent of time zone. They are represented in a [time stamp field](../abap-glossary/abentimestamp_field_glosry.md) with the [time stamp type](../abap-glossary/abentimestamp_field_glosry.md) [`utclong`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md) or as [time stamps in packed numbers](abap-processing-internal-data/abentime_stamps_packed.md) whose data type is defined using the [DDIC data elements](../abap-glossary/abendata_element_glosry.md) `TIMESTAMP` or `TIMESTAMPL` from the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md).

**time stamp type**

[Data type](../abap-glossary/abendata_type_glosry.md) [`utclong`](abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md) for saving an [UTC time stamp](../abap-glossary/abenutc_timestamp_glosry.md) in a [time stamp field](../abap-glossary/abentimestamp_field_glosry.md).

**time-stamp-like expression position**

[Read position](../abap-glossary/abenread_position_glosry.md) in which a [time stamp field](../abap-glossary/abentimestamp_field_glosry.md), as well as an [expression](../abap-glossary/abencharlike_expression_glosry.md) can be specified whose result has a [time stamp type](../abap-glossary/abentimestamp_type_glosry.md).

**token**

Elementary component of an [ABAP statement](../abap-glossary/abenabap_statement_glosry.md), into which the compiler breaks down statements into tokens. Tokens are [ABAP words](../abap-glossary/abenabap_word_glosry.md), [ABAP operands](../abap-glossary/abenabap_operand_glosry.md), [operators](../abap-glossary/abenoperator_glosry.md), and certain special characters.

**top include**

[Include program](../abap-glossary/abeninclude_program_glosry.md) used for the [global declaration part](../abap-glossary/abenglobal_declaration_sect_glosry.md) of an [ABAP program](../abap-glossary/abenabap_program_glosry.md). No [processing blocks](../abap-glossary/abenprocessing_block_glosry.md) should be implemented in top includes. This is checked by the extended program check. The corresponding top include is included whenever an individual include program of an ABAP program is compiled.

**top level transaction**

The first program of a call sequence. The ABAP memory assigned to a call sequence is retained for as long as the [internal session](../abap-glossary/abeninternal_session_glosry.md) of the top level transaction remains loaded. The initial SAP Easy Access program does not usually work as a top level transaction, except in area instance versions.

**transaction**

Execution of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) using a transaction code. There are dialog, report, parameter, variant, and `OO` transactions. A transaction is started by entering the transaction code in the command field on the standard toolbar or by using the statements `CALL TRANSACTION` or `LEAVE TO TRANSACTION`.

At SAP, database transactions are referred to as [database LUWs](../abap-glossary/abendatabase_luw_glosry.md).

In a business context, for example in [RAP](../abap-glossary/abenrap_glosry.md), a transaction is refers to the result of a business-related operation that accesses and modifies data. When completed, a consistent state of data is produced.

**transaction service**

Object service for updating persistent objects.

**transactional contract**

Specifies which ABAP statements and operations are allowed and which are not allowed in a [transactional phase](../abap-glossary/abentr_phase_glosry.md). The following transactional contracts are available, each of which specifies restrictions to ensure transactional consistency: `SAVE`, `MODIFY`, `FUNCTIONAL`, `SURFACE`, `READ`, `COMPLETE`. The `SAVE` and `MODIFY` contracts are implicitly enabled in both transactional phases.

The transactional contracts can be set explicitly by [API classifications](abap-database-access/abapapi_classification.md) (starting with `IF_ABAP_TX...`, for example, `IF_ABAP_TX_SAVE`). In the [controlled SAP LUW](../abap-glossary/abencontrolled_sap_luw_glosry.md) and when in a transactional context, transactional contracts are checked.

For example, an API contains database changes and has the classification `IF_ABAP_TX_SAVE`. The classification ensures that the API is not called in the modify [transactional phase](../abap-glossary/abentr_phase_glosry.md) by causing a violation that is either logged or results in a [runtime error](../abap-glossary/abenruntime_error_glosry.md).

**transactional phase**

Specifies the concrete phase of a transaction. It is either the modify or the save transactional phase. They are set either implicitly, as in the case of, for example, [RAP handler](../abap-glossary/abenabp_handler_method_glosry.md) and [saver](../abap-glossary/abenabp_saver_method_glosry.md) methods, or explicitly using the static methods of class [`CL_ABAP_TX`](abap-database-access/abaprap_cl_abap_tx.md).

In a [RAP transaction](../abap-glossary/abenrap_luw_glosry.md), the transactional phases are as follows:

- Modify: Includes the [RAP interaction phase](../abap-glossary/abenrap_int_phase_glosry.md) and the [early save phase](../abap-glossary/abenearly_rap_save_phase_glosry.md) of the [RAP save sequence](../abap-glossary/abenrap_save_seq_glosry.md).

- Save: Includes the [RAP late save phase](../abap-glossary/abenlate_rap_save_phase_glosry.md).

**transactional Remote Function Call**

tRFC for short. Obsolete remote function call in which the function called remotely is registered for execution and started using the statement [`COMMIT WORK`](abap-database-access/abapcommit.md).

**transformation source code**

[Source code](../abap-glossary/abensource_code_glosry.md) of [XSLT programs](../abap-glossary/abenxslt_program_glosry.md) and [Simple Transformations](../abap-glossary/abensimple_transformation_glosry.md) processed in the Transformation Editor.

**translate function**

[Processing function](../abap-glossary/abenprocess_function_glosry.md) that translates characters in a string into other characters.

**tRFC**

*-\>* transactional remote function call

**trusted system**

[AS ABAP](../abap-glossary/abenas_abap_glosry.md) that is classified as a trusted caller of remote function calls in a trusting system. The trusted system provides the RFC client. The system is classified in transaction `SMT1`. Trusted systems log on to the trusting system without passing a password. User-specific logon data is checked in the trusting system.

**trusting system**

[AS ABAP](../abap-glossary/abenas_abap_glosry.md) that trusts a trusted system in calls using Remote Function Call. The trusting system provides the RFC server. The trusting systems can be listed in a trusted system using transaction code `SMT2`.

**truth value**

A truth value is either true or false. In ABAP, truth values only occur as the result of [logical expressions](../abap-glossary/abenlogical_expression_glosry.md). [Data types](../abap-glossary/abendata_type_glosry.md) for [Boolean data objects](../abap-glossary/abenboolean_data_object_glosry.md) that can accept truth values are not supported. Instead, a truth value can be evaluated as the result of a [Boolean function](../abap-glossary/abenboole_function_glosry.md).

**type**

Abstract description of an [object](../abap-glossary/abenobject_glosry.md). Either a [data type](../abap-glossary/abendata_type_glosry.md) for a [data object](../abap-glossary/abendata_object_glosry.md) or an [object type](../abap-glossary/abenobject_type_glosry.md) for an object in [ABAP Objects](../abap-glossary/abenabap_objects_glosry.md). The associated [generic data type](../abap-glossary/abengeneric_data_type_glosry.md) is [`any`](abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md). All types share the same [namespace](abap-syntax-elements-of-an-abap-program/abennaming_conventions.md).

**type conversion**

Converts the content of a [data object](../abap-glossary/abendata_object_glosry.md) according to the associated [conversion rules](../abap-glossary/abenconversion_rule_glosry.md). Type conversions occur implicitly in [assignments](../abap-glossary/abenassignment_glosry.md) between data objects with different [data types](../abap-glossary/abendata_type_glosry.md) or can be performed explicitly using the [conversion operator](../abap-glossary/abenconversion_operator_glosry.md) [`CONV`](abap-creating-objects-and-values/abenconstructor_expression_value.md).

**type description class**

[System class](../abap-glossary/abensystem_class_glosry.md) of the [runtime type services](../abap-glossary/abenrun_time_type_services_glosry.md). The [static methods](../abap-glossary/abenstatic_method_glosry.md) of a type description classes create [type description objects](../abap-glossary/abentype_object_glosry.md) from existing types or construct new types.

**type description object**

Instance of a [type description class](../abap-glossary/abentype_class_glosry.md). Type description objects describe a [type](../abap-glossary/abentype_glosry.md). Type description objects are created using the static methods of the type description classes. The type description class and possible attributes of type description objects determine the [technical properties](../abap-glossary/abentechnical_type_prpt_glosry.md) of the type. [References](../abap-glossary/abenreference_glosry.md) to type description objects can be used, for example, after the addition `HANDLE` of the statements [`CREATE DATA`](abap-creating-objects-and-values/abapcreate_data_handle.md) and [`ASSIGN`](abap-processing-internal-data/abapassign_casting.md).

**type group**

*-\>* [type pool](../abap-glossary/abentype_pool_glosry.md)

**type name**

Name of a [type](../abap-glossary/abentype_glosry.md). In a program, only the [relative type name](../abap-glossary/abenrelative_type_name_glosry.md) is known and statically usable. An [absolute type name](../abap-glossary/abenabsolute_typename_glosry.md) can be used to specify dynamic types.

**type pool**

[ABAP program](../abap-glossary/abenabap_program_glosry.md), administrated by the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md), that is introduced by the statement `TYPE-POOL` and which contains the definitions of globally visible [data types](../abap-glossary/abendata_type_glosry.md), [constants](../abap-glossary/abenconstant_glosry.md), and macros. A type pool is loaded the first time its data types and constants are used. It does not support own dynpros.

**typing**

[Generic](../abap-glossary/abengeneric_typing_glosry.md) or [complete](../abap-glossary/abencomplete_typing_glosry.md) definition of a [data type](../abap-glossary/abendata_type_glosry.md) for [formal parameters](../abap-glossary/abenformal_parameter_glosry.md) or [field symbols](../abap-glossary/abenfield_symbol_glosry.md). Specifies in which operand positions a formal parameter or field symbol can be used and which type properties are used. When parameters are passed, it is checked whether the data type of the assigned [actual parameter](../abap-glossary/abenactual_parameter_glosry.md), or memory area is [compatible](../abap-glossary/abencompatible_glosry.md) with the typing.

**uncatchable exception**

[Exception](../abap-glossary/abenexception_glosry.md) that is not assigned to an [exception class](../abap-glossary/abenexception_class_glosry.md) and that cannot be handled in the program by [`TRY - CATCH - ENDTRY`](abap-program-flow-logic/abaptry.md). Uncatchable exceptions are raised by the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) and are usually a response to error situations that cannot be handled properly in the program. An uncatchable exception always produces a [runtime error](../abap-glossary/abenruntime_error_glosry.md).

**Unicode**

Language-independent [character set](../abap-glossary/abencharacter_set_glosry.md) for international data processing ([www.unicode.org](http://www.unicode.org)). Subset of the [`UCS`](../abap-glossary/abenucs_glosry.md) character set according to ISO-10646. Unicode can represent 1114111 different characters numbered hexadecimally from `U+0000` to `U+10FFFF`. The Unicode character set is normally accessed using a [UTF](../abap-glossary/abenutf_glosry.md) or [`UCS`](../abap-glossary/abenucs2_glosry.md) [character representation](../abap-glossary/abenchar_representation_glosry.md).

**Unicode check**

[Syntax check](../abap-glossary/abensyntax_check_glosry.md) for [ABAP programs](../abap-glossary/abenabap_program_glosry.md) that are to be executed in a [Unicode system](../abap-glossary/abenunicode_system_glosry.md). The Unicode check is carried out for [ABAP language versions](../abap-glossary/abenabap_version_glosry.md) [Standard ABAP](../abap-glossary/abenstandard_abap_glosry.md) or higher. Only Unicode systems are supported in the current [AS ABAP](../abap-glossary/abenas_abap_glosry.md) release and therefore no programs of the obsolete ABAP language version Obsolete ABAP (Non-Unicode) are supported.

**Unicode program**

[ABAP program](../abap-glossary/abenabap_program_glosry.md) written in [ABAP language version](../abap-glossary/abenabap_version_glosry.md) [Standard ABAP](../abap-glossary/abenstandard_abap_glosry.md) or higher.

**unit test**

A unit test is created and executed by developers to verify the functional correctness of individual software units. A software unit is defined in this case, as a non-trivial code unit in which certain input has a verifiable effect. [Procedures](../abap-glossary/abenprocedure_glosry.md) are a typical example for these units in ABAP. Procedures are the smallest functional components of larger units such as [classes](../abap-glossary/abenclass_glosry.md) or [function pools](../abap-glossary/abenfunction_pool_glosry.md). Unit tests determine during the development and quality assurance stages that the individual components of a larger software unit work correctly. Unit tests are developed and executed in [ABAP Unit](../abap-glossary/abenabap_unit_glosry.md).

**unnamed data object**

[Data object](../abap-glossary/abendata_object_glosry.md) that cannot be addressed by a name. Unnamed data objects are [literals](../abap-glossary/abenabap_literal_glosry.md) and [anonymous data objects](../abap-glossary/abenanonymous_data_object_glosry.md).

**unrestricted ABAP language version**

[ABAP language version](../abap-glossary/abenabap_version_glosry.md) that is not restricted regarding the ABAP language scope and access to other repository objects. [Standard ABAP](../abap-glossary/abenstandard_abap_glosry.md) is unrestricted. See also [restricted ABAP language versions](../abap-glossary/abenrestricted_version_glosry.md).

**untyped literal**

A [literal](../abap-glossary/abenliteral_glosry.md) whose [data type](../abap-glossary/abendata_type_glosry.md) is implicitly derived from its value or its delimiter. Both untyped [numeric literals](../abap-glossary/abennumeric_literal_glosry.md) and untyped [character literals](../abap-glossary/abencharacter_literal_glosry.md) exist. See also [typed literal](../abap-glossary/abentyped_literal_glosry.md).

**upcast**

Also referred to as a widening cast. [Assignment](../abap-glossary/abenassignment_glosry.md) between [reference variables](../abap-glossary/abenreference_variable_glosry.md), where the [static type](../abap-glossary/abenstatic_type_glosry.md) of the target variables is more general or identical to the static type of the source variables. An upcast does not have to be performed explicitly. See [downcast](../abap-glossary/abendown_cast_glosry.md).

**update**

Execution of update function modules that are registered using `CALL FUNCTION ... IN UPDATE TASK` and triggered by [`COMMIT WORK`](abap-database-access/abapcommit.md). Updates are used to bundle the changing database accesses of an [SAP LUW](../abap-glossary/abensap_luw_glosry.md) in a [database LUW](../abap-glossary/abendatabase_luw_glosry.md). See also synchronous, asynchronous, and local updates.

**update function module**

[Function module](../abap-glossary/abenfunction_module_glosry.md) for which the property *update module* is marked in the Function Builder. It is the basis of the update function. An update function module generally contains changing database accesses and the statement `CALL FUNCTION ... IN UPDATE TASK` can be used to register it for later execution with the statement [`COMMIT WORK`](abap-database-access/abapcommit.md). When an update function module is created, it is assigned either a high or low priority level.

**update module**

*-\>* Update function module

**user date**

[Local date](../abap-glossary/abenlocal_date_glosry.md) of an [ABAP user](../abap-glossary/abenabap_user_glosry.md) in the [user time zone](../abap-glossary/abenuser_time_zone_glosry.md).

**user name**

Name of an [ABAP user](../abap-glossary/abenabap_user_glosry.md) that is required for logging on to a [user session](../abap-glossary/abenuser_session_glosry.md) in the [AS ABAP](../abap-glossary/abenas_abap_glosry.md). Together with the [password](../abap-glossary/abenpassword_glosry.md), the user name allows authorized use of an AS ABAP.

**user time**

[Local time](../abap-glossary/abenlocal_time_glosry.md) of an [ABAP user](../abap-glossary/abenabap_user_glosry.md) in the [user time zone](../abap-glossary/abenuser_time_zone_glosry.md).

**user time zone**

[Time zone](../abap-glossary/abentime_zone_glosry.md) defined in the [user master record](../abap-glossary/abenuser_master_record_glosry.md) for the local [user time](../abap-glossary/abenuser_time_glosry.md).

**UTC time stamp**

[Time stamp](../abap-glossary/abentime_stamp_glosry.md) referring to the [UTC](../abap-glossary/abenutc_glosry.md) reference time. The time stamps of the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) are UTC time stamps, but as [POSIX time stamps](../abap-glossary/abenposix_timestamp_glosry.md) they do not support [leap seconds](../abap-glossary/abenleap_second_glosry.md).

**UUID**

Short for Universal Unique Identifier. Universally unique identifier that is generated in accordance with [OSF standards](http://www.opengroup.org/onlinepubs/9629399/apdxa.htm) from the system time stamp and the network address. In ABAP, a UUID can be created using the [system class](../abap-glossary/abensystem_class_glosry.md) `CL_SYSTEM_UUID` and the [SQL function](../abap-glossary/abensql_function_glosry.md) [`UUID`](abap-database-access/abensql_uuid.md).

**value operator**

[Constructor operator](../abap-glossary/abenconstructor_operator_glosry.md) [`VALUE`](abap-creating-objects-and-values/abenconstructor_expression_value.md) used to construct values of a [data type](../abap-glossary/abendata_type_glosry.md).

**value range**

Set of valid values for a [data object](../abap-glossary/abendata_object_glosry.md). The values that are valid for a data object are determined by its [data type](../abap-glossary/abendata_type_glosry.md). In [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md), the term value range indicates a [semantic property](../abap-dictionary-ddic/ddic-data-types/abenddic_domains_sema.md) of a [DDIC domain](../abap-glossary/abendomain_glosry.md).

**value semantics**

Value semantics means that the referenced data object or the dereferenced [reference](../abap-glossary/abenreference_glosry.md) is used when accessing a [deep](../abap-glossary/abendeep_glosry.md) [data object](../abap-glossary/abendata_object_glosry.md). In ABAP, value semantics apply when accessing [dynamic data objects](../abap-glossary/abendynamic_data_object_glosry.md) and [field symbols](../abap-glossary/abenfield_symbol_glosry.md). See also [reference semantics](../abap-glossary/abenreference_semantics_glosry.md).

**variable**

[Named data object](../abap-glossary/abennamed_data_object_glosry.md) whose value can be changed during the runtime of an [ABAP program](../abap-glossary/abenabap_program_glosry.md). See also [immutable variable](../abap-glossary/abenimmutable_variable_glosry.md).

**visibility section**

The [declaration part](../abap-glossary/abendeclaration_part_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md) can be divided into up to three visibility sections. These areas are [public](../abap-glossary/abenpublic_glosry.md), [protected](../abap-glossary/abenprotected_glosry.md), or [private](../abap-glossary/abenprivate_glosry.md). They define the visibility of the [components](../abap-glossary/abenclass_component_glosry.md) of the class and therefore the [interfaces](../abap-glossary/abenintf_gen_glosry.md) of the class towards all users allowed by the [package check](../abap-glossary/abenpackage_concept_glosry.md) concept.

**warning**

[Message](../abap-glossary/abenmessage_glosry.md) of [message type](../abap-glossary/abenmessage_type_glosry.md) *W*. Warnings during PAI processing of dynpros make screen fields ready for input again.

**weak reference**

Reference to an [object](../abap-glossary/abenobject_glosry.md) of a [class](../abap-glossary/abenclass_glosry.md) that is ignored when the [Garbage Collector](../abap-glossary/abengarbage_collector_glosry.md) is executed, unlike [object references](../abap-glossary/abenobject_reference_glosry.md) in [reference variables](../abap-glossary/abenreference_variable_glosry.md). An object that is only pointed to by weak references is deleted by the Garbage Collector.

**WebSocket protocol**

`WSP` for short. A TCP based protocol for the bidirectional communication between a client and a server. Using ABAP Push Channels, an [AS ABAP](../abap-glossary/abenas_abap_glosry.md) can be used as a server and as a client for the WebSocket protocol.

[***-\>* More about**](http://tools.ietf.org/html/rfc6455)

**widening cast**

*-\>* [upcast](../abap-glossary/abenup_cast_glosry.md)

**wildcard character**

Character that substitutes other content. In [relational expressions](../abap-glossary/abencomparison_expression_glosry.md) with the operators [`CP`](abap-program-flow-logic/abenlogexp_strings.md) and [`NP`](abap-program-flow-logic/abenlogexp_strings.md), `*` usually stands for any [string](../abap-glossary/abencharacter_string_glosry.md) and `+` for any individual character. In [SQL conditions](../abap-glossary/abensql_cond_glosry.md) with the [operator](../abap-glossary/abenoperator_glosry.md) [`LIKE`](abap-database-access/abenwhere_logexp_like.md), `%` stands for any string and `_` for individual characters. In [regular expressions](../abap-glossary/abenregular_expression_glosry.md), an extended set of special characters is used to define patterns. The special functions of wildcard characters can be switched off using [escape characters](../abap-glossary/abenescape_character_glosry.md)

**work area**

Description for a [data object](../abap-glossary/abendata_object_glosry.md) that is particularly useful when working with [internal tables](../abap-glossary/abeninternal_table_glosry.md) or [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) as a source for changing operations or as a target for reading operations.

**writable expression**

Expression representing an operand that can be written to. Writable expressions are certain [constructor expressions](../abap-glossary/abenconstructor_expression_glosry.md) using [`NEW`](abap-creating-objects-and-values/abennew_constructor_params_class.md) and [`CAST`](abap-processing-internal-data/abenconstructor_expression_cast.md) or [table expressions](../abap-glossary/abentable_expression_glosry.md). A writable expression can be specified in a [result position](../abap-glossary/abenresult_position_glosry.md).

**write lock**

Area lock on an area instance version in the shared objects memory. A write lock enables to create a new area instance version.

**write position**

[Operand position](../abap-glossary/abenoperand_position_glosry.md) in which the [operand](../abap-glossary/abenabap_operand_glosry.md) is written to. There are [read/write positions](../abap-glossary/abenread_write_position_glosry.md), where an operand is read-accessed before writing and [write-only positions](../abap-glossary/abenwrite_only_position_glosry.md) where no read access occurs.

**write-only position**

[Write position](../abap-glossary/abenwrite_position_glosry.md) in which the [operand](../abap-glossary/abenabap_operand_glosry.md) is only written to but not read-accessed. See [declaration position](../abap-glossary/abendeclaration_position_glosry.md).

**writer stream** Also referred to as output stream. Either a [data stream](../abap-glossary/abendata_stream_glosry.md) that is connected to a [streaming data sink](../abap-glossary/abenstreaming_data_sink_glosry.md) or a filter stream that writes data to another stream. The direction of a writer stream always goes toward the data sink. In a writer stream data can only be written.
