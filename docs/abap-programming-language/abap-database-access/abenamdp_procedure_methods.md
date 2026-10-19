---
title: "AMDP - Procedure Implementations"
source_file: abenamdp_procedure_methods.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Procedure Implementations

An AMDP procedure implementation is an AMDP method for implementing a [database procedure](../../abap-glossary/abendatabase_procedure_glosry.md). It is declared in an [AMDP class](abenamdp_classes.md) like a regular [static method](../../abap-glossary/abenstatic_method_glosry.md) or [instance method](../../abap-glossary/abeninstance_method_glosry.md) in any [visibility section](../../abap-glossary/abenvisibility_section_glosry.md). An AMDP procedure implementation cannot be identified as an AMDP method in the declaration part of the class.

An AMDP procedure implementation is indicated as an AMDP method in the implementation part of the class using the addition [`BY DATABASE PROCEDURE`](abapmethod_by_db_proc.md) of the statement `METHOD`. At the same time, the database system where the method is to be used and the programming language of the database system used to implement the method are also defined. The database objects of the current database schema accessed in the AMDP method must be declared using an addition [`USING`](abapmethod_by_db_proc.md). If possible, the syntax check is performed on the basis of this information. When database tables defined in the ABAP Dictionary are accessed, and the access is known statically, the AMDP framework ensures that the order of the fields defined in the dictionary is respected, which can differ from the order on the database.

Using the statement [`CLASS-METHODS meth FOR SQL SERVICE`](abapclass-methods_for_sql_service.md), an AMDP procedure implementation can be exposed to external SQL access using an [SQL service](../../abap-glossary/abenabap_sql_services_glosry.md).

The following restrictions apply with respect to the [parameter interface](../../abap-glossary/abenparameter_interface_glosry.md) of an AMDP procedure implementation:

- The typing of the parameters must not be [generic](../../abap-glossary/abengeneric_typing_glosry.md).

  - Only [elementary data types](../../abap-glossary/abenelementary_data_type_glosry.md) and [table types](../../abap-glossary/abentable_type_glosry.md) with a structured row type can be used.

  - The row type of a tabular type can only contain elementary data types as components.

- A parameter must not have an [enumerated type](../../abap-glossary/abenenum_type_glosry.md) and must not have a component with an enumerated type.

- A parameter must not be typed with a data type that references one of the obsolete built-in DDIC data types [`DF16_SCL`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`DF34_SCL`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- The parameters must be declared for [pass by value](../../abap-glossary/abenpass_by_value_glosry.md) using [`VALUE`](../abap-declarations/abapmethods_parameters.md). [Pass by reference](../../abap-glossary/abenpass_by_reference_glosry.md) is not allowed.

- [Return values](../../abap-glossary/abenreturn_value_glosry.md) must not be declared using [`RETURNING`](../abap-declarations/abapmethods_functional.md).

- Only [input parameters](../../abap-glossary/abeninput_parameter_glosry.md) can be flagged as optional parameters.

  - Each elementary optional input parameter must have a replacement parameter declared using [`DEFAULT`](../abap-declarations/abapmethods_parameters.md). Only literals or constants can be specified as replacement parameters.

  - Unlike in [regular methods](../abap-declarations/abapmethods_parameters.md), a literal specified as a replacement parameter must be convertible to the data type of the input parameter. If not, a syntax error occurs.

  - Input parameters of the types `string`, `xstring`, `decfloat16`, and `decfloat34` cannot have replacement parameters and hence cannot be optional.

  - An optional tabular input parameter cannot have any replacement parameters and must be made optional instead using [`OPTIONAL`](../abap-declarations/abapmethods_parameters.md).

- Parameter names:

  - Parameter names cannot start with the characters `%_`.

  - The parameter name `connection` cannot be used in [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md).

  - The parameter name `client` is reserved for future enhancements.

  - The parameter name `endmethod` is not allowed.

- [`RAISING`](../abap-declarations/abapmethods_general.md) can be used to specify the exceptions specified under [AMDP -Exception Classes](abenamdp_exceptions.md) to handle these classes for a call. Other exceptions cannot be handled. No non-class-based exceptions can be created using the addition [`EXCEPTIONS`](../abap-declarations/abapmethods_general.md).

The following restrictions apply to method implementation:

- An AMDP method must not be empty.

- [DDL](../../abap-glossary/abenddl_glosry.md) statements are not allowed for creating, changing or deleting database objects.

- No statements are allowed that are only possible in database tables and not in views, such as `TRUNCATE TABLE` or `LOCK TABLE`.

- Local temporary database objects cannot be accessed.

- Executing transactional statements is not allowed. In particular, no [database commits](abendb_commit.md) and [database rollbacks](abendb_rollback.md) using `COMMIT` and `ROLLBACK` statements are allowed. This also applies to called procedures. [LUWs](../../abap-glossary/abenluw_glosry.md) should always be handled in the ABAP program to ensure data consistency between procedures.

- Writes cannot be performed on database tables where [table buffering](../../abap-glossary/abentable_buffering_glosry.md) is switched on, since SQLScript accesses are ignored by buffer synchronizations.

- AMDP methods do not have any implicit enhancement options.

The following additional restrictions apply in the current ABAP language version [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md):

- The AMDP procedure implementation must be restricted to reads by using the addition [`AMDP OPTIONS READ-ONLY`](abapmethods_amdp_options.md) in declarations of the AMDP method or by using the addition [`OPTIONS READ-ONLY`](abapmethod_by_db_proc.md) in implementations of the AMDP method.

- AMDP methods must be [client-safe](../../abap-glossary/abenclient_safe_glosry.md) by using one of the AMDP options [`CDS SESSION CLIENT DEPENDENT`](abapmethods_amdp_options_client.md) or [`CLIENT INDEPENDENT`](abapmethods_amdp_options_client.md).

- The AMDP procedure must be implemented in [SQLScript](../../abap-glossary/abensql_script_glosry.md).

- [Repository objects](../../abap-glossary/abenrepository_object_glosry.md) that are used in the AMDP procedure implementation must be released for ABAP for Cloud Development.

- For [CDS entities](../../abap-glossary/abencds_entity_glosry.md), such as [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) and [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md), the name of the [CDS entity](../../abap-glossary/abencds_entity_glosry.md) must be specified after the [`USING`](abapmethod_by_db_proc.md) addition in the implementation of the AMDP method. The name of a [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md) or [AMDP function](../../abap-glossary/abenamdp_function_glosry.md) is not possible.

- Only objects in the current [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md) can be accessed in the implementation. Other prefixes or corresponding [AMDP macros](../../abap-glossary/abenamdp_macro_glosry.md) are not allowed.

- Any statements that could potentially cause problems are not allowed in the implementation. For example, no `CE_...` SQLScript operators are allowed and [session variables](../../abap-glossary/abensession_variable_glosry.md) cannot be accessed.

Further restrictions may apply depending on the programming language of the database system and these are listed in the corresponding sections:

- [SQLScript for the SAP HANA Database](abenamdp_hdb_sqlscript.md)

## Hints

- It is strongly recommended that only the character set 7-bit ASCII is used when implementing an AMDP method.

- When passed to an actual parameter, a [null value](../../abap-glossary/abennull_value_glosry.md) is passed to its type-dependent initial value.

- The use of dynamic programming techniques is strongly discouraged, even if it is allowed by the programming language of the database system.

  - The existence of other database objects cannot be checked or guaranteed when they are accessed dynamically. This is particularly relevant when other AMDP methods are called.

  - When database tables in the ABAP Dictionary are accessed dynamically, the AMDP framework cannot respect the order of the fields defined in the ABAP Dictionary and the order of fields on the database, which might be different, is used instead. This can produce the incorrect values when making assignments to ABAP data objects declared with respect to the ABAP Dictionary.

  - In dynamic accesses, it is not possible to prevent writes from being performed on database tables with activated table buffering, which can cause inconsistencies in buffer synchronizations.
