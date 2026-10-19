---
title: "DDIC Glossary"
source_file: abenddic_glossary.html
section: "ABAP Dictionary (DDIC)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC Glossary

In the following, terms of the [ABAP Glossary](../abap-glossary/abenabap_glossary.md) are listed, that are relevant for ABAP Dictionary.

**ABAP Dictionary**

Persistent storage for [data types](../abap-glossary/abendata_type_glosry.md) that are visible in all [repository objects](../abap-glossary/abenrepository_object_glosry.md). In particular, [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) or DDIC views on the [standard database](../abap-glossary/abenstandard_db_glosry.md) that can be used in [ABAP programs](../abap-glossary/abenabap_program_glosry.md) and in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) are defined in the ABAP Dictionary. [Dictionary objects](../abap-glossary/abendictionary_object_glosry.md) are maintained using the ABAP Dictionary tool in ABAP Workbench (transaction `SE11`) or using the [ABAP development tools for Eclipse (ADT)](../abap-glossary/abenadt_glosry.md).

**append search help**

[Search help](../abap-glossary/abensearch_help_glosry.md) of the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) that is appended to another search help. Search helps delivered by SAP can be appended in customer systems by append search helps without making modifications.

**append structure**

[Structure](../abap-glossary/abenstructure_glosry.md) of the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) that is appended to a different DDIC structure or [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) thus adding its [structure components](../abap-glossary/abenstructure_component_glosry.md) to them. Append structures and database tables can be used to add components to structures and database tables delivered by SAP without making modifications to them.

**application table**

[DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) with [client column](../abap-glossary/abenclient_column_glosry.md). An application table contains [client-dependent](../abap-glossary/abenclient_dependent_glosry.md) data that is processed by [application programs](../abap-glossary/abenapplication_program_glosry.md).

**binary floating point number type**

[Numeric data type](../abap-glossary/abennumeric_data_type_glosry.md) used for the binary representation of numbers with mantissa and exponents. The associated [built-in ABAP type](../abap-glossary/abenbuiltin_abap_type_glosry.md) is [`f`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md). The [built-in DDIC type](../abap-glossary/abenbuiltin_ddic_type_glosry.md) is [`FLTP`](ddic-built-in-data-types/abenddic_builtin_types.md). The internal representation is in accordance with the norm IEEE-754 (double precision) by one bit for the plus/minus sign, 11 bits for the binary exponent, and 52 bits for the mantissa, whereby [decimal numbers](../abap-glossary/abendecimal_number_glosry.md) can be represented by 17 [places](../abap-glossary/abenplace_glosry.md). A [data object](../abap-glossary/abendata_object_glosry.md) of a binary floating point number type is a [binary floating point number](../abap-glossary/abenbinfloat_glosry.md).

**built-in DDIC type**

[Built-in](../abap-glossary/abenbuiltin_data_type_glosry.md) [elementary data type](../abap-glossary/abenelementary_data_type_glosry.md) of the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). Built-in DDIC types can be used to define types in ABAP Dictionary and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) but cannot be used in [ABAP programs](../abap-glossary/abenabap_program_glosry.md) directly.

**byte field type**

[Byte-like data type](../abap-glossary/abenbyte_like_data_typ_glosry.md) for storing [byte strings](../abap-glossary/abenbyte_string_glosry.md) of fixed length. The associated [built-in ABAP type](../abap-glossary/abenbuiltin_abap_type_glosry.md) is [`x`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md). The [built-in DDIC types](../abap-glossary/abenbuiltin_ddic_type_glosry.md) are [`RAW`](ddic-built-in-data-types/abenddic_builtin_types.md) and [`LRAW`](ddic-built-in-data-types/abenddic_builtin_types.md). A [data object](../abap-glossary/abendata_object_glosry.md) of a byte field type is a [byte field](../abap-glossary/abenbyte_field_glosry.md).

**byte string type**

[Byte-like data type](../abap-glossary/abenbyte_like_data_typ_glosry.md) for storing [byte chains](../abap-glossary/abenbyte_chain_glosry.md) of variable length. The associated [built-in ABAP type](../abap-glossary/abenbuiltin_abap_type_glosry.md) is [`xstring`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md). The [built-in DDIC type](../abap-glossary/abenbuiltin_ddic_type_glosry.md) is [`RAWSTRING`](ddic-built-in-data-types/abenddic_builtin_types.md). Internal administration takes place using an internal [reference](../abap-glossary/abenreference_glosry.md) and the data type is [deep](../abap-glossary/abendeep_glosry.md). A [data object](../abap-glossary/abendata_object_glosry.md) of a byte field type is a [byte string](../abap-glossary/abenbyte_string_glosry.md).

**check table**

[DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) whose [primary key](../abap-glossary/abenprimary_key_glosry.md) appears as a [foreign key](../abap-glossary/abenforeign_key_glosry.md) in a [foreign key table](../abap-glossary/abenforeign_key_table_glosry.md).

**client column**

First column and [key field](../abap-glossary/abenkey_field_glosry.md) of [client-dependent](../abap-glossary/abenclient_dependent_glosry.md) [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) or DDIC views of the type `CLNT` for storing the [client ID](../abap-glossary/abenclient_identifier_glosry.md). By default, [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) statements work with automatic [client handling](../abap-glossary/abenclient_handling_glosry.md). Database tables with a client column are generally [application tables](../abap-glossary/abenapplication_table_glosry.md) but can also contain administrative data. Database tables without a client column are called [system tables](../abap-glossary/abensystem_table_glosry.md).

**client-dependent**

A [SQL data source](../abap-glossary/abensql_data_source_glosry.md) for which an implicit [client handling](../abap-glossary/abenclient_handling_glosry.md) takes place when accessed with [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md).

- A [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) or DDIC view in [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) is client-dependent if the first column is a [client column](../abap-glossary/abenclient_column_glosry.md). The system table `T000`, which contains the [AS ABAP](../abap-glossary/abenas_abap_glosry.md) [client IDs](../abap-glossary/abenclient_identifier_glosry.md), is an exception to this rule.

- The client dependency of a [CDS entity](../abap-glossary/abencds_entity_glosry.md) is determined by its data sources. Client handling is by done implicitly by filtering the [session variable](../abap-glossary/abensession_variable_glosry.md) `$session.client`.

- The client dependency of [CDS DDIC-based views (obsolete)](../abap-glossary/abencds_v1_view_glosry.md) is declared in the [CDS source code](../abap-glossary/abencds_source_code_glosry.md) by the [ABAP annotation](../abap-glossary/abenabap_annotation_glosry.md) `@CLientHandling.type`.

See also: [client-independent](../abap-glossary/abenclient_independent_glosry.md).

**cluster table**

Before [ABAP release](../abap-glossary/abenabap_release_glosry.md) 7.73, [table category](ddic-database-tables/abenddic_database_tables_tab_cat.md) of a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) in [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). A cluster table was not defined as such on the [database](../abap-glossary/abendatabase_glosry.md). Instead, multiple cluster tables were stored in a table cluster in the database. Only [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) could be used to access cluster tables, whereby certain restrictions applied. Cluster tables are no longer supported as of ABAP release 7.73. Any existing cluster tables were converted to [transparent tables](../abap-glossary/abentransparent_table_glosry.md).

**conversion exit**

A conversion exit defines rules that overwrite standard conversions that take place when values are passed as input from user interfaces to ABAP or as output from ABAP to user interfaces. Version exits can be linked to UI elements in different ways. Conversion exits can be implemented by conversion routines and can be assigned directly to a dynpro field or a [DDIC domain](../abap-glossary/abendomain_glosry.md). The conversion routines execute the conversions implicitly for such dynpro fields and also in the statements `WRITE` and `WRITE TO` for [data objects](../abap-glossary/abendata_object_glosry.md) that refer to such domains.

**conversion routine**

A conversion routine is a [function module](../abap-glossary/abenfunction_module_glosry.md) that implements a part of a [conversion exit](../abap-glossary/abenconversion_exit_glosry.md). For each conversion exit, there is a function module for input and a function module for output using the naming convention `CONVERSION_EXIT_....._INPUT|OUTPUT` where the dots are the name of the conversion exit.

**currency code**

Content of a [currency key](../abap-glossary/abencurrency_key_glosry.md). Valid currency codes are defined in the database table `TCURC`. The database table `TCURX` contains the currency code for currencies whose number of decimal places is not two.

**currency field**

A currency field is linked to a [currency key](../abap-glossary/abencurrency_key_glosry.md) and it is used for entering an amount in a particular currency. Currency fields are available in [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) (DDIC) and in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), but the possible data types and handling differs.

See also:

- [DDIC currency field](../abap-glossary/abenddic_currency_field_glosry.md)

- [ABAP CDS amount field](../abap-glossary/abencds_amount_field_glosry.md)

**currency key**

Component of a [DDIC structure](../abap-glossary/abenddic_structure_glosry.md), or [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md), or DDIC view of the type [`CUKY`](ddic-built-in-data-types/abenddic_builtin_types.md) defined in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). A currency key can be linked to a [currency field](../abap-glossary/abencurrency_field_glosry.md) of a structure, database table, or view. The currency key contains a [currency code](../abap-glossary/abencurrency_id_glosry.md) from the database table `TCURC`, and is used to define the currency for the currency field. By default, the number of decimal places of a currency is always two. Currencies with a different number of decimal places must be entered additionally in the table `TCURX`, where the number of decimal places can be defined explicitly.

**customizing include**

[Structure](../abap-glossary/abenstructure_glosry.md) of the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md), with a name prefixed by `CI_` for customers and `SI_` for partners and that is in the customer namespace. Customizing includes in SAP structures are usually empty. They are not linked with existing structures, they simply reserve their names. In customer or partner systems, these includes can be enhanced in customizing by actually creating the included customizing includes and using customizing transactions to assign them [structure components](../abap-glossary/abenstructure_component_glosry.md).

**database field**

Smallest logical unit of the [structure](../abap-glossary/abenstructure_glosry.md) of a [database table](../abap-glossary/abendatabase_table_glosry.md). The properties of a database field of a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) are defined by a [DDIC data element](../abap-glossary/abendata_element_glosry.md).

**database procedure proxy**

[Repository object](../abap-glossary/abenrepository_object_glosry.md) in [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) that represents an [SQLScript procedure](../abap-glossary/abensql_script_procedure_glosry.md) of the [SAP HANA database](../abap-glossary/abenhana_database_glosry.md) with respect to ABAP programs and which is addressed in the statement `CALL DATABASE PROCEDURE`. Database procedure proxies are supported by SAP HANA XSA but not by SAP HANA XSC.

**DDIC**

Short for [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md), based on its former name, *Data Dictionary*.

**DDIC annotation**

A DDIC annotation adds metadata to a DDIC object. It can be used, for example, to add technical or semantic properties to a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) or a [DDIC structure](../abap-glossary/abenddic_structure_glosry.md).

**DDIC append view**

Object in [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) with which a [DDIC database view](../abap-glossary/abendatabase_view_glosry.md) can be enhanced without modification by adding additional fields of its base tables.

**DDIC currency field**

Component of a [DDIC structure](../abap-glossary/abenddic_structure_glosry.md), or [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md), or DDIC view of type `CURR` defined in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). It is used for entering an amount in a particular currency. The content of a currency field is interpreted as an integer in the smallest units of the currency. A currency field must be linked with a [currency key](../abap-glossary/abencurrency_key_glosry.md) of a structure, database table, or view that specifies the currency and number of decimal places.

Related terms:

- [currency field](../abap-glossary/abencurrency_field_glosry.md)

- [ABAP CDS amount field](../abap-glossary/abencds_amount_field_glosry.md)

**DDIC data element**

[Repository object](../abap-glossary/abenrepository_object_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) that defines an [elementary data type](../abap-glossary/abenelementary_data_type_glosry.md) or a [reference type](../abap-glossary/abenreference_type_glosry.md). In addition to [technical type properties](../abap-glossary/abentechnical_type_prpt_glosry.md), it specifies the semantic meaning of a ([database](../abap-glossary/abendatabase_field_glosry.md)) [field](../abap-glossary/abenfield_glosry.md) (e.g., the header for tabular representations or documentation text). Properties such as [data type](../abap-glossary/abendata_type_glosry.md), length, and so on, are defined directly in the data element or are copied from a [DDIC domain](../abap-glossary/abendomain_glosry.md).

**DDIC database table**

Database table defined in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) as an [ABAP-managed database object](../abap-glossary/abenabap_dictionary_glosry.md). Each database table has a unique [primary index](../abap-glossary/abenprimary_index_glosry.md) and can have additional [secondary indexes](../abap-glossary/abensecondary_index_glosry.md). [Foreign key dependencies](../abap-glossary/abenforeign_key_dependency_glosry.md) can exist between individual DDIC database tables. A DDIC database table is generally defined as a [transparent table](../abap-glossary/abentransparent_table_glosry.md) in the [database](../abap-glossary/abendatabase_glosry.md) of the AS ABAP. All DDIC database tables defined in ABAP Dictionary can be referenced as a [data type](../abap-glossary/abendata_type_glosry.md) like [DDIC structures](../abap-glossary/abenddic_structure_glosry.md) and can be accessed using [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md). During development, the content of DDIC database tables can be monitored using the Data Browser.

**DDIC database view**

General DDIC table view in [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) for multiple [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md). The instance of a DDIC database view as an [ABAP-managed database object](../abap-glossary/abenabap_managed_db_object_glosry.md) is an [SQL view](../abap-glossary/abensql_view_glosry.md) in the [ABAP database schema](../abap-glossary/abenabap_db_schema_glosry.md) of the [standard database](../abap-glossary/abenstandard_db_glosry.md).

**DDIC DDL**

Short for [Dictionary DDL](../abap-glossary/abendictionary_ddl_glosry.md).

**DDIC dependency rule**

[Database object](../abap-glossary/abendb_object_glosry.md) of the [SAP HANA database](../abap-glossary/abenhana_database_glosry.md). A dependency rule can be defined for [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) and derives additional conditions from a selection condition, used by the optimizer of the [database system](../abap-glossary/abendatabase_system_glosry.md) to extend the read access to these database tables. On an [AS ABAP](../abap-glossary/abenas_abap_glosry.md), a dependency rules can be defined as a [HANA tuning object](../abap-glossary/abenhana_tuning_object_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md).

**DDIC domain**

[Repository object](../abap-glossary/abenrepository_object_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) that describes the properties of [DDIC data elements](../abap-glossary/abendata_element_glosry.md), such as [data type](../abap-glossary/abendata_type_glosry.md) or value range. A domain can be linked with any number of data elements.

**DDIC dynamic cache**

[SAP HANA tuning object](../abap-glossary/abenhana_tuning_object_glosry.md) defined using the statement [`DEFINE DYNAMIC CACHE`](ddic-tuning-objects/abenddicddl_define_dynamic_cache.md) in [DDIC DDL](../abap-glossary/abenddic_dcl_glosry.md). A DDIC dynamic cache can improve performance when a view is accessed repeatedly. At the same time, a dynamic cache guarantees up-to-date data.

A DDIC dynamic cache is integrated into [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) as a wrapper for an SAP HANA dynamic result cache.

See also:

- [View cache](../abap-glossary/abenview_cache_glosry.md)

- [static view cache](../abap-glossary/abenstatic_view_cache_glosry.md)

**DDIC extension**

Object in [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) that extends a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) or a [DDIC structure](../abap-glossary/abenddic_structure_glosry.md).

**DDIC external view**

A special DDIC view that defines an SAP HANA view of the SAP HANA Repository in ABAP programs. A DDIC external view can be used like a [structured type](../abap-glossary/abenstructured_type_glosry.md) and specified as a source in reading [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) statements. External views are supported by SAP HANA XSA but not by SAP HANA XSC.

**DDIC help view**

Special DDIC table view of the [ABAP Dictionary](abenabap_dictionary.md) for multiple [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) that is not instantiated as an [SQL view](../abap-glossary/abensql_view_glosry.md) on the [database](../abap-glossary/abendatabase_glosry.md).

**DDIC maintenance view**

Special DDIC table view of the [ABAP Dictionary](abenabap_dictionary.md) for multiple [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) that are not instantiated as an [SQL view](../abap-glossary/abensql_view_glosry.md) on the [database](../abap-glossary/abendatabase_glosry.md).

**DDIC projection view**

Special DDIC table view of the [ABAP Dictionary](abenabap_dictionary.md) for a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md). A DDIC projection view is not instantiated as an [SQL view](../abap-glossary/abensql_view_glosry.md) on the [database](../abap-glossary/abendatabase_glosry.md).

**DDIC quantity field**

Component of a [DDIC structure](../abap-glossary/abenddic_structure_glosry.md), or [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md), or DDIC view of type `QUAN` defined in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). A quantity field must be linked to a [unit key](../abap-glossary/abenunit_glosry.md) of a structure, database table, or view. This key determines the unit of the quantity field.

See also:

- [quantity field](../abap-glossary/abenquantity_glosry.md)

- [ABAP CDS quantity field](../abap-glossary/abencds_quantity_glosry.md)

**DDIC runtime object**

Summary of all relevant properties of a [data type](../abap-glossary/abendata_type_glosry.md) defined in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). A DDIC runtime object is created when a dictionary object is activated and is stored as an entry in the name table (nametab). The [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) accesses the DDIC runtime object when types from the ABAP Dictionary are used.

**DDIC structure**

[Structured type](../abap-glossary/abenstructured_type_glosry.md) defined as a [DDIC type](../abap-glossary/abenddic_type_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md).

**DDIC table type**

[Table type](../abap-glossary/abentable_type_glosry.md) for an [internal table](../abap-glossary/abeninternal_table_glosry.md) defined as a [DDIC type](../abap-glossary/abenddic_type_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md).

**DDIC table view**

DDIC view on [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) of the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) that can only be defined in the form-based [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) tool of the ABAP Workbench. Table views can be [DDIC database views](../abap-glossary/abendatabase_view_glosry.md), DDIC projection views, DDIC maintenance views, and DDIC help views.

**DDIC type**

[Data type](../abap-glossary/abendata_type_glosry.md) defined as a [global type](../abap-glossary/abenglobal_type_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). DDIC types are always data types, while global [object types](../abap-glossary/abenobject_type_glosry.md) are defined in the [class library](../abap-glossary/abenclass_library_glosry.md). In particular [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) and DDIC views can be used as DDIC types in ABAP programs.

**DDIC view**

[View](../abap-glossary/abenview_glosry.md) defined in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). Either a DDIC table view or an DDIC external view.

**decimal floating point number type**

[Numeric data type](../abap-glossary/abennumeric_data_type_glosry.md) for the decimal storage of numbers with mantissa and exponents. The associated [built-in ABAP types](../abap-glossary/abenbuiltin_abap_type_glosry.md) are [`decfloat16`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) and [`decfloat34`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md). The [built-in DDIC types](../abap-glossary/abenbuiltin_ddic_type_glosry.md) are [`DECFLOAT16`](ddic-built-in-data-types/abenddic_builtin_types.md), [`DF16_DEC`](ddic-built-in-data-types/abenddic_builtin_types.md), [`DF16_RAW`](ddic-built-in-data-types/abenddic_builtin_types.md), [`DECFLOAT34`](ddic-built-in-data-types/abenddic_builtin_types.md), [`DF34_DEC`](ddic-built-in-data-types/abenddic_builtin_types.md) and [`DF34_RAW`](ddic-built-in-data-types/abenddic_builtin_types.md). The internal representation follows the standard IEEE-754-2008, where [decimal numbers](../abap-glossary/abendecimal_number_glosry.md) with 16 or 34 [places](../abap-glossary/abenplace_glosry.md) are accurately represented in the mantissa. A decimal floating point number has an additional [scaling](../abap-glossary/abenscale_glosry.md) property. A [data object](../abap-glossary/abendata_object_glosry.md) of a decimal floating point number type is a [decimal floating point number](../abap-glossary/abendecfloat_glosry.md).

**dictionary**

*-\>* [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md)

**dictionary DDL**

Data definition language ([DDL](../abap-glossary/abenddl_glosry.md)) of the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) for the definition of [ABAP-managed database objects](../abap-glossary/abenabap_managed_db_object_glosry.md) in the [ABAP development tools for Eclipse (ADT)](../abap-glossary/abenadt_glosry.md). Dictionary DDL contains language elements for [structures](../abap-glossary/abenstructure_glosry.md), [append structures](../abap-glossary/abenappend_structure_glosry.md), [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) and [HANA tuning objects](../abap-glossary/abenhana_tuning_object_glosry.md). Dictionary DDL is based on the syntax of [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md).

**dictionary object**

DDIC object for short. [Repository object](../abap-glossary/abenrepository_object_glosry.md) defined in [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). Examples of dictionary objects are global [data types](../abap-glossary/abendata_type_glosry.md), [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md), and DDIC views.

**DRUL source code**

Source code for [dependency rules](../abap-glossary/abendependency_rule_glosry.md) in [Dictionary DDL](../abap-glossary/abendictionary_ddl_glosry.md).

**DTDC source code**

Source code for [dynamic caches](../abap-glossary/abendynamic_cache_glosry.md) in [Dictionary DDL](../abap-glossary/abendictionary_ddl_glosry.md).

**export/import table**

[Transparent](../abap-glossary/abentransparent_table_glosry.md) [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) with the required structure for storing [data clusters](../abap-glossary/abendata_cluster_glosry.md) in database tables and in cross-transaction application buffers of the [shared memory](../abap-glossary/abenshared_memory_glosry.md). Data clusters are exported to export/import tables using the statement [`EXPORT`](../abap-programming-language/abap-data-cluster/abapexport_data_cluster.md) and imported again using the statement [`IMPORT`](../abap-programming-language/abap-data-cluster/abapimport_data_cluster.md).

**extension index**

[Index](../abap-glossary/abenindex_glosry.md) of a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) that is created as a separate [repository object](../abap-glossary/abenrepository_object_glosry.md). An extension index can be created to extend an existing database table without modifying the original object. During an upgrade, the extension index is automatically applied without any modification adjustment.

**field exit**

Obsolete customer exit that can be linked with [DDIC data elements](../abap-glossary/abendata_element_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) in customer systems. If a dynpro field is defined with reference to such a data element, a function module named `FIELD_EXIT_dtel` is called during the data transport from the dynpro to the ABAP program at the event PAI. Here, `dtel` is the name of the data element. The value of the dynpro field can be modified in the function module. The function module of a field exit cannot be debugged at present.

**fixed value**

A single value specified for a [DDIC domain](../abap-glossary/abendomain_glosry.md) as part of its value range.

**[***-\>* More about**](ddic-data-types/abenddic_domains_sema.md)**

**fixed value append**

A fixed value append defines [fixed values](../abap-glossary/abenfixed_value_glosry.md) and/or intervals that are appended to an existing [DDIC domain](../abap-glossary/abendomain_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). Domains delivered by SAP can be enhanced in customer systems by means of fixed value appends without modification.

**foreign key**

One or more columns of a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) ([foreign key table](../abap-glossary/abenforeign_key_table_glosry.md)) that are [primary keys](../abap-glossary/abenprimary_key_glosry.md) of another database table ([check table](../abap-glossary/abencheck_table_glosry.md)).

**foreign key dependency**

Relationship between a [foreign key table](../abap-glossary/abenforeign_key_table_glosry.md) and a [check table](../abap-glossary/abencheck_table_glosry.md). A foreign key table usually only contains entries for which the content of the [foreign key](../abap-glossary/abenforeign_key_glosry.md) also occurs as content of the [primary key](../abap-glossary/abenprimary_key_glosry.md) in the check table.

**foreign key field**

Field in a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) to which a [check table](../abap-glossary/abencheck_table_glosry.md) is assigned. Part of the [foreign key](../abap-glossary/abenforeign_key_glosry.md) of a [foreign key table](../abap-glossary/abenforeign_key_table_glosry.md).

**foreign key table**

[DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) that contains [foreign keys](../abap-glossary/abenforeign_key_glosry.md).

**fuzzy search index**

[Index](../abap-glossary/abenindex_glosry.md) of the [SAP HANA database](../abap-glossary/abenhana_database_glosry.md) that database that provides fast error-tolerant text search, where a query returns records even when the search term contains additional or missing characters or other types of spelling errors. The [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) allows fuzzy search indexes to be created for [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md).

**geodata type**

Data type for geometric data. The [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) currently supports the built-in data type [`GEOM_EWKB`](ddic-built-in-data-types/abenddic_builtin_types.md).

**geospatial data**

*-\>* [spatial data](../abap-glossary/abenspatial_data_glosry.md)

**global temporary table**

GTT for short. [Table category](ddic-database-tables/abenddic_database_tables_tab_cat.md) of a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). A GTT is used to store temporary data that is deleted at the end of each [database LUW](../abap-glossary/abendatabase_luw_glosry.md). Only [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) should be used to access global temporary tables defined in the ABAP Dictionary.

**global type**

[Data type](../abap-glossary/abendata_type_glosry.md) or [object type](../abap-glossary/abenobject_type_glosry.md) that is visible as a [repository object](../abap-glossary/abenrepository_object_glosry.md) in the entire [AS ABAP](../abap-glossary/abenas_abap_glosry.md). Global data types are defined as [DDIC types](../abap-glossary/abenddic_type_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) or as [CDS types](../abap-glossary/abencds_type_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). Global object types are defined as [global classes](../abap-glossary/abenglobal_class_glosry.md) or as [global interfaces](../abap-glossary/abenglobal_interface_glosry.md) in the [class library](../abap-glossary/abenclass_library_glosry.md). All these global types share the same namespace. Besides these global types, data types defined in the public [visibility section](../abap-glossary/abenvisibility_section_glosry.md) of global classes or in global interfaces can also be used globally.

**HANA tuning object**

A [tuning object](../abap-glossary/abentuning_object_glosry.md) that defines technical settings for an ABAP Dictionary object on the [SAP HANA database](../abap-glossary/abenhana_database_glosry.md). HANA tuning objects are defined in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) in [DDIC DDL](../abap-glossary/abenddic_dcl_glosry.md) and they are a wrapper for settings on the [SAP HANA database](../abap-glossary/abenhana_database_glosry.md). Currently, there are the following HANA tuning objects:

- [DDIC dependency rules](../abap-glossary/abendependency_rule_glosry.md)

- [DDIC dynamic caches](../abap-glossary/abendynamic_cache_glosry.md)

**include structure**

Abbreviated as include. [Structure](../abap-glossary/abenstructure_glosry.md) of the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) that is included in another structure.

**index**

Selected columns of a [database table](../abap-glossary/abendatabase_table_glosry.md) that are sorted in order and stored as a copy in the [database system](../abap-glossary/abendatabase_system_glosry.md), and which point to the actual rows. For the database tables of an [AS ABAP](../abap-glossary/abenas_abap_glosry.md) that are defined in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md), there is always a [primary index](../abap-glossary/abenprimary_index_glosry.md), and additional [secondary indexes](../abap-glossary/abensecondary_index_glosry.md) can also be created. In [internal tables](../abap-glossary/abeninternal_table_glosry.md) there may be one or more [table indexes](../abap-glossary/abentable_index_glosry.md).

**INDX-type table**

Obsolete name for export/import tables.

**infotype**

Special [structure](../abap-glossary/abenstructure_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). The statement `INFOTYPES` creates special [internal tables](../abap-glossary/abeninternal_table_glosry.md) of this structure, which can be processed in a `PROVIDE` [loop](../abap-glossary/abenloop_glosry.md).

**initial value**

The ABAP runtime framework defines an initial value for each [data type](../abap-glossary/abendata_type_glosry.md). The initial values of the [elementary data types](../abap-glossary/abenelementary_data_type_glosry.md) depend on the corresponding [built-in ABAP type](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md). The initial value of [reference types](../abap-glossary/abenreference_type_glosry.md) is the [null reference](../abap-glossary/abennull_reference_glosry.md). The initial value of an [internal table](../abap-glossary/abeninternal_table_glosry.md) is an empty table without lines. The initial value of [structured types](../abap-glossary/abenstructured_type_glosry.md) is produced from the initial values of the individual [structure components](../abap-glossary/abenstructure_component_glosry.md). The statement [`CLEAR`](../abap-programming-language/abap-processing-internal-data/abapclear.md) with no additions sets a [data object](../abap-glossary/abendata_object_glosry.md) to the appropriate initial value for its type. Initial values are also assigned to most [built-in data types](ddic-built-in-data-types/abenddic_builtin_types.md) in [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md), but those are not evaluated in ABAP programs.

**integer type**

[Numeric data type](../abap-glossary/abennumeric_data_type_glosry.md) for storing [integer numbers](../abap-glossary/abeninteger_number_glosry.md) of different value ranges. The associated [built-in ABAP types](../abap-glossary/abenbuiltin_abap_type_glosry.md) are ([`b`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), [`s`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md)), [`i`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), and [`int8`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md). The [built-in DDIC types](../abap-glossary/abenbuiltin_ddic_type_glosry.md) are [`INT1`](ddic-built-in-data-types/abenddic_builtin_types.md), [`INT2`](ddic-built-in-data-types/abenddic_builtin_types.md), [`INT4`](ddic-built-in-data-types/abenddic_builtin_types.md) and [`INT8`](ddic-built-in-data-types/abenddic_builtin_types.md). The internal representation takes place in the integer representation of the current platform. A [data object](../abap-glossary/abendata_object_glosry.md) of an integer type is an [integer](../abap-glossary/abeninteger_glosry.md).

**join**

A combination of two [SQL data sources](../abap-glossary/abensql_data_source_glosry.md) into one result set, consisting of columns of both data sources. The rows of the result set are determined by the [join type](../abap-glossary/abenjoin_type_glosry.md) and by [join conditions](../abap-glossary/abenjoin_condition_glosry.md) between columns of the data sources. The relation between the rows of the data sources can be expressed by a [cardinality](../abap-glossary/abencardinality_glosry.md). Joins can be implemented in ABAP as follows:

- DDIC views in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md)

- [Join expressions](../abap-glossary/abenjoin_expression_glosry.md) in [queries](../abap-glossary/abenasql_query_glosry.md) of [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md)

- [Join expressions](../abap-glossary/abenjoin_expression_glosry.md) in the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) of [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md)

Furthermore, [CDS associations](../abap-glossary/abencds_association_glosry.md) and [CTE associations](../abap-glossary/abencte_association_glosry.md) define join relationships that are instantiated when the associations are used in [SQL path expressions](../abap-glossary/abensql_path_expression_glosry.md).

**lock object**

[Repository object](../abap-glossary/abenrepository_object_glosry.md) defined in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) that is used as the basis for SAP locks. In a lock object [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) are specified to which a common [lock](../abap-glossary/abenlock_glosry.md) is to be applied and which are linked by [foreign key dependencies](../abap-glossary/abenforeign_key_dependency_glosry.md). When a lock object is created, two lock function modules are automatically generated.

[***-\>* More about**](https://help.sap.com/docs/ABAP_PLATFORM_NEW/ec1c9c8191b74de98feb94001a95dd76/cf21eea5446011d189700000e8322d00)

**mass activation**

Activation of multiple objects in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) using the mass activator.

**mass activator**

[System program](../abap-glossary/abensystem_program_glosry.md) `RADMASG0` for the mass activation of objects in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md).

**matchcode object**

Predecessor of [search helps](../abap-glossary/abensearch_help_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md).

**name table**

Nametab for short. A native [database table](../abap-glossary/abendatabase_table_glosry.md) that stores the [DDIC runtime objects](../abap-glossary/abenddic_runtime_object_glosry.md) of [data types](../abap-glossary/abendata_type_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). It contains nametab headers and nametab field descriptions. The name table is persisted as the native database table DDNTT and is not defined as a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) in the ABAP Dictionary. This means that it cannot be accessed using ABAP SQL or ABAP CDS. The name table is accessed internally in the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) or by using APIs.

The former table DDNTF for separate storage of the field descriptions is not supported any more.

**nametab**

*-\>* Name table

**nametab field descriptions**

A part of the name table for [DDIC runtime objects](../abap-glossary/abenddic_runtime_object_glosry.md) of [data types](../abap-glossary/abendata_type_glosry.md) from the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md), used for the properties of structure components.

**nametab header**

A part of the name table for [DDIC runtime objects](../abap-glossary/abenddic_runtime_object_glosry.md) of [data types](../abap-glossary/abendata_type_glosry.md) from the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md), used for the properties of the entire object.

**numeric text field type**

[Character-like data type](../abap-glossary/abencharlike_data_type_glosry.md) for storing [numeric texts](../abap-glossary/abennumeric_text_glosry.md) of fixed length. The associated [built-in ABAP type](../abap-glossary/abenbuiltin_abap_type_glosry.md) is [`n`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md). The [built-in DDIC types](../abap-glossary/abenbuiltin_ddic_type_glosry.md) are [`NUMC`](ddic-built-in-data-types/abenddic_builtin_types.md) and [`ACCP`](ddic-built-in-data-types/abenddic_builtin_types.md). The internal representation takes place in the [character representation](../abap-glossary/abenchar_representation_glosry.md) of the current [code page](../abap-glossary/abencodepage_glosry.md). A [data object](../abap-glossary/abendata_object_glosry.md) of this type is a [numeric text field](../abap-glossary/abennumeric_text_field_glosry.md).

**packed number type**

[Numeric data type](../abap-glossary/abennumeric_data_type_glosry.md) for saving [fixed point numbers](../abap-glossary/abenfixed_point_number_glosry.md) with a fixed number of [decimal places](../abap-glossary/abendecimal_place_glosry.md) The associated [built-in ABAP type](../abap-glossary/abenbuiltin_abap_type_glosry.md) is [`p`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md). The [built-in DDIC type](../abap-glossary/abenbuiltin_ddic_type_glosry.md) is [`DEC`](ddic-built-in-data-types/abenddic_builtin_types.md). The number of decimal places is a property of the data type and not, as with [floating point numbers](../abap-glossary/abenfloating_point_number_glosry.md), a property of the data itself. Calculations with packed numbers are performed using [fixed point arithmetic](../abap-glossary/abenfixed_point_arithmetic_glosry.md). The internal representation uses the [BCD](../abap-glossary/abenbcd_glosry.md) format. A [data object](../abap-glossary/abendata_object_glosry.md) of a packed number type is a [packed number](../abap-glossary/abenpacked_number_glosry.md).

**pooled table**

Before [ABAP release](../abap-glossary/abenabap_release_glosry.md) 7.73, [table category](ddic-database-tables/abenddic_database_tables_tab_cat.md) of a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). A pooled table was not defined as such on the [database](../abap-glossary/abendatabase_glosry.md). Instead, multiple pooled tables were stored in a table pool in the database. Only [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) could be used to access pooled tables whilst certain other restrictions also applied. Pooled tables are no longer supported since ABAP release 7.73. Any existing pooled tables were transformed to [transparent tables](../abap-glossary/abentransparent_table_glosry.md).

**primary index**

Unique [index](../abap-glossary/abenindex_glosry.md) of a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) defined in [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). The index is assembled from the [key fields](../abap-glossary/abenkey_field_glosry.md) of the [primary key](../abap-glossary/abenprimary_key_glosry.md). When a table is activated in the ABAP Dictionary, the primary index is created automatically using the primary key fields of the table. Certain [internal tables](../abap-glossary/abeninternal_table_glosry.md) have a [primary table index](../abap-glossary/abenprimary_table_index_glosry.md).

**replacement object**

A replacement object is a [CDS view](../abap-glossary/abencds_view_glosry.md) that can be specified for a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) or a [DDIC database view](../abap-glossary/abendatabase_view_glosry.md). In case of a read access using [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md), the replacement object is addressed instead of the original object.

**search help**

A [repository object](../abap-glossary/abenrepository_object_glosry.md) maintained in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) to create value lists. It supplies input fields on dynpros with single or multicolumn [input helps](../abap-glossary/abeninput_help_glosry.md). Search helps can be linked in the ABAP Dictionary with [structure components](../abap-glossary/abenstructure_component_glosry.md), [DDIC data elements](../abap-glossary/abendata_element_glosry.md), and [check tables](../abap-glossary/abencheck_table_glosry.md). A search help enables searches for input values using associated data, without the need to know the exact spelling of the value.

[***-\>* More about**](https://help.sap.com/docs/ABAP_PLATFORM_NEW/ec1c9c8191b74de98feb94001a95dd76/cf21ee2b446011d189700000e8322d00)

**secondary index**

[Index](../abap-glossary/abenindex_glosry.md) of [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) defined in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) that can be created in addition to the [primary index](../abap-glossary/abenprimary_index_glosry.md). Creating secondary indexes can improve the performance when accessing databases that evaluate the indexes of the [database](../abap-glossary/abendatabase_glosry.md). A secondary index can be unique, but it does not have to be. A [secondary table index](../abap-glossary/abensecondary_table_index_glosry.md) can be assigned to [internal tables](../abap-glossary/abeninternal_table_glosry.md).

**spatial data**

Data that describes the position, shape, and orientation of an object in a [spatial reference system](../abap-glossary/abenspatial_ref_system_glosry.md). This allows the visualization of the position or the movement of an object. Spatial data is often represented as 2D geometries (Cartesian coordinates) but can also include the altitude for a 3D geometry. Typical geometrical forms are points, lines, and polygons.

**spatial reference identifier**

SRID for short. An identifier that specifies a [spatial reference system](../abap-glossary/abenspatial_ref_system_glosry.md). The default value for the identifier of the spatial reference system is 0 and indicates a Cartesian coordinate system, i.e. 2D geometries.

**spatial reference system**

A system to define the location of an object using coordinates. This system consists of various parameters that are used to represent a geometry, such as the name of the coordinate system from which the coordinates are derived. The specification of a spatial reference system is done by a [spatial reference identifier](../abap-glossary/abenspatial_ref_identifier_glosry.md) (SRID). A spatial reference system is used to bring spatial data into context.

**standalone data type**

A [data type](../abap-glossary/abendata_type_glosry.md) that is defined using the statement [`TYPES`](../abap-programming-language/abap-declarations/abaptypes.md) in an [ABAP program](../abap-glossary/abenabap_program_glosry.md), as a data type of the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) or as a [CDS entity](../abap-glossary/abencds_entity_glosry.md). See also [bound data type](../abap-glossary/abenbound_data_type_glosry.md).

**standard index**

[Index](../abap-glossary/abenindex_glosry.md) of a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) that is created and transported as a part of the respective [dictionary object](../abap-glossary/abendictionary_object_glosry.md).

**structured type**

[Data type](../abap-glossary/abendata_type_glosry.md) of a [structure](../abap-glossary/abenstructure_glosry.md). It contains other data types as [structure components](../abap-glossary/abenstructure_component_glosry.md). A named structured type is either defined as a [DDIC structure](../abap-glossary/abenddic_structure_glosry.md), a [CDS entity](../abap-glossary/abencds_entity_glosry.md) or inside an [ABAP program](../abap-glossary/abenabap_program_glosry.md) using the statement [`TYPES BEGIN OF`](../abap-programming-language/abap-declarations/abaptypes_struc.md).

**system table**

[Client-independent](../abap-glossary/abenclient_independent_glosry.md) [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) without a [client column](../abap-glossary/abenclient_column_glosry.md). A system table contains data that is not specific for a client and that is generally only processed by [system programs](../abap-glossary/abensystem_program_glosry.md).

**table buffering**

[Buffering](../abap-glossary/abensap_buffering_old_glosry.md) of data from [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md), [DDIC database views](../abap-glossary/abendatabase_view_glosry.md), or from [CDS entities](../abap-glossary/abencds_entity_glosry.md) in a [table buffer](../abap-glossary/abentable_buffer_glosry.md) in the [shared memory](../abap-glossary/abenshared_memory_glosry.md) of the current [AS instance](../abap-glossary/abenas_instance_glosry.md). Whether and how a DDIC database table or a DDIC database view is buffered is determined by its [technical settings](ddic-database-tables/abenddic_database_tables_buffer.md). For a CDS entity, the buffering is determined by annotations and a [CDS entity buffer](../abap-glossary/abencds_entity_buffer_glosry.md). Buffering is managed by the [database interface](../abap-glossary/abendatabase_interface_glosry.md). Table buffering is applied implicitly when the database is accessed using [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and from classic dynpros. In ABAP SQL, the [ABAP SQL in-memory engine](../abap-glossary/abenabap_sql_inmemeng_glosry.md) processes the tabular data in the table buffer.

**table cluster**

Before [ABAP release](../abap-glossary/abenabap_release_glosry.md) 7.73, [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) in the [database](../abap-glossary/abendatabase_glosry.md) that contains the data of multiple cluster tables. Cluster tables are no longer supported and all table clusters have been removed.

**table key**

Columns of an [internal table](../abap-glossary/abeninternal_table_glosry.md) or [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) whose content identifies table lines. For internal tables, distinction is made between [primary table keys](../abap-glossary/abenprimary_table_key_glosry.md) and [secondary table keys](../abap-glossary/abensecondary_table_key_glosry.md), which are [technical type properties](../abap-glossary/abentechnical_type_prpt_glosry.md) of the [table type](../abap-glossary/abentable_type_glosry.md).

**table pool**

Before [ABAP release](../abap-glossary/abenabap_release_glosry.md) 7.73, [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) in the [database](../abap-glossary/abendatabase_glosry.md) that contains the data of multiple pooled tables. Pooled tables are no longer supported and all table pools have been removed.

**text field type**

[Character-like data type](../abap-glossary/abencharlike_data_type_glosry.md) for storing [character strings](../abap-glossary/abencharacter_string_glosry.md) of fixed length. The associated [built-in ABAP type](../abap-glossary/abenbuiltin_abap_type_glosry.md) is [`c`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md). The [built-in DDIC types](../abap-glossary/abenbuiltin_ddic_type_glosry.md) are [`CHAR`](ddic-built-in-data-types/abenddic_builtin_types.md) and [`LCHR`](ddic-built-in-data-types/abenddic_builtin_types.md). The internal representation takes place in the [character representation](../abap-glossary/abenchar_representation_glosry.md) of the current [code page](../abap-glossary/abencodepage_glosry.md). A [data object](../abap-glossary/abendata_object_glosry.md) of a text field type is a [text field](../abap-glossary/abentext_field_glosry.md).

**text language**

Semantic property of a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) that affects data transport between non-Unicode and [Unicode systems](../abap-glossary/abenunicode_system_glosry.md).

**text table**

Special [foreign key table](../abap-glossary/abenforeign_key_table_glosry.md) whose [primary key](../abap-glossary/abenprimary_key_glosry.md) consists of the [foreign key](../abap-glossary/abenforeign_key_glosry.md), that is, the primary key of the [check table](../abap-glossary/abencheck_table_glosry.md) and a language key of the type [`LANG`](ddic-built-in-data-types/abenddic_builtin_types.md). A text table contains language-dependent texts that are assigned to the lines of the check table.

**time stamp**

Combined [date](../abap-glossary/abendate_glosry.md)/[time](../abap-glossary/abentime_glosry.md) specification for determining a point in time. Time stamps of the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) are [POSIX time stamps](../abap-glossary/abenposix_timestamp_glosry.md) independent of time zone. They are represented in a [time stamp field](../abap-glossary/abentimestamp_field_glosry.md) with the [time stamp type](../abap-glossary/abentimestamp_field_glosry.md) [`utclong`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md) or as [time stamps in packed numbers](../abap-programming-language/abap-processing-internal-data/abentime_stamps_packed.md) whose data type is defined using the [DDIC data elements](../abap-glossary/abendata_element_glosry.md) `TIMESTAMP` or `TIMESTAMPL` from the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md).

**transparent table**

[Table category](ddic-database-tables/abenddic_database_tables_tab_cat.md) of a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) that has exactly one identically named instance with the same columns as the definition in the ABAP Dictionary. Besides using [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md), the data of transparent tables can also be processed using Native SQL and [AMDP](../abap-glossary/abenamdp_glosry.md) and outside [AS ABAP](../abap-glossary/abenas_abap_glosry.md) by using the programming interface of the database. The latter is not recommended.

**tuning object**

A [repository object](../abap-glossary/abenrepository_object_glosry.md) that defines technical settings for certain repository objects. A tuning object can be defined and transported separately from the repository object for which it is defined. The following types of tuning objects are currently available:

- [HANA tuning objects](../abap-glossary/abenhana_tuning_object_glosry.md) defined in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) in [DDIC DDL](../abap-glossary/abenddic_dcl_glosry.md).

- [ABAP tuning objects](../abap-glossary/abenabap_tuning_object_glosry.md) defined as [CDS objects](../abap-glossary/abencds_object_glosry.md) in [CDS DDL](../abap-glossary/abencds_ddl_glosry.md).

**unit ID**

Content of a [unit key](../abap-glossary/abenunit_glosry.md).

**unit key**

Component of a [DDIC structure](../abap-glossary/abenddic_structure_glosry.md), or [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) of type UNIT defined in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). A unit key can be linked to a [quantity field](../abap-glossary/abenquantity_glosry.md) of a structure, database table, or view. The unit key can contain a [unit ID](../abap-glossary/abenunit_id_glosry.md), and defines the unit for the quantity field.

**value help**

*-\>* [Input help](../abap-glossary/abeninput_help_glosry.md)

**value range**

Set of valid values for a [data object](../abap-glossary/abendata_object_glosry.md). The values that are valid for a data object are determined by its [data type](../abap-glossary/abendata_type_glosry.md). In [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md), the term value range indicates a [semantic property](ddic-data-types/abenddic_domains_sema.md) of a [DDIC domain](../abap-glossary/abendomain_glosry.md).

**value table**

Semantic property of a [DDIC domain](../abap-glossary/abendomain_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). The value table is the default value for the [check table](../abap-glossary/abencheck_table_glosry.md) of table fields defined with reference to the domain.

**writable database object**

A [repository object](../abap-glossary/abenrepository_object_glosry.md) that allows modifying data on the database.

- In [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), [CDS table entities](../abap-glossary/abencds_table_entity_glosry.md), [writable CDS view entities](../abap-glossary/abenwritable_v2_glosry.md), and [writable CDS external entities](../abap-glossary/abenwritable_ee_glosry.md) allow for the modification of data with the [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) statements [`INSERT`](../abap-programming-language/abap-database-access/abapinsert_dbtab.md), [`UPDATE`](../abap-programming-language/abap-database-access/abapupdate.md), [`MODIFY`](../abap-programming-language/abap-database-access/abapmodify_dbtab.md), and [`DELETE`](../abap-programming-language/abap-database-access/abapdelete_dbtab.md).

- In [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md), [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) and DDIC table views allow data change operations.
