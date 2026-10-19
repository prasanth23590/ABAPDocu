---
title: "ABAP SQL - Glossary"
source_file: abensql_glossary.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Glossary

In the following, terms of the [ABAP Glossary](../../abap-glossary/abenabap_glossary.md) are listed that are relevant for ABAP SQL.

**ABAP SQL**

ABAP SQL is a subset of [SQL](../../abap-glossary/abensql_glosry.md) implemented by [ABAP statements](../../abap-glossary/abenabap_statement_glosry.md), which includes the [DQL](../../abap-glossary/abendql_glosry.md) and [DML](../../abap-glossary/abendml_glosry.md) parts for [CRUD](../../abap-glossary/abencrud_glosry.md) operations. ABAP SQL statements are processed by the [ABAP SQL engine](../../abap-glossary/abenabap_sql_engine_glosry.md) that either uses

- the [ABAP SQL interface](../../abap-glossary/abenabap_sql_interface_glosry.md) of the [database interface](../../abap-glossary/abendatabase_interface_glosry.md) to access the [standard database](../../abap-glossary/abenstandard_db_glosry.md) of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) or a secondary database.

- or the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) to access the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) or [internal tables](../../abap-glossary/abeninternal_table_glosry.md)

ABAP SQL can be used to read ([`SELECT`](abapselect.md), [`WITH`](abapwith.md). `FETCH`) and modify ([`INSERT`](abapinsert_dbtab.md), [`UPDATE`](abapupdate.md), [`MODIFY`](abapmodify_dbtab.md), or [`DELETE`](abapdelete_dbtab.md)) data in [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md) defined in the [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md). [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md), DDIC views, and all [CDS persistent entities](../../abap-glossary/abencds_sql_entity_glosry.md) can be used directly as [data sources](../../abap-glossary/abensql_data_source_glosry.md) in ABAP SQL.

**ABAP SQL connection object**

An instance of a class that implements `IF_ABAP_SQL_CONNECTION` and represents a valid [database connection](../../abap-glossary/abendatabase_connection_glosry.md).

**ABAP SQL engine**

Part of the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md) that processes [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statements. ABAP SQL statements are either processed by the [ABAP SQL interface](../../abap-glossary/abenabap_sql_interface_glosry.md) and passed to the [standard database](../../abap-glossary/abenstandard_db_glosry.md) of the [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) or by the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md).

**ABAP SQL hierarchy**

A tabular [SQL data source](../../abap-glossary/abensql_data_source_glosry.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) whose rows contain the content of the [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md) of a [parent-child hierarchy](../../abap-glossary/abenpcr_hierarchy_glosry.md). An ABAP SQL hierarchy is either a [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md) or a [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md). Special [hierarchy columns](../../abap-glossary/abenhierarchy_column_glosry.md) contain [hierarchy attributes](../../abap-glossary/abenhierarchy_attribute_glosry.md) of the individual hierarchy nodes in the SQL hierarchy. SQL hierarchies are either created using a [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md), an existing [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md), or a [CTE hierarchy](../../abap-glossary/abencte_hierarchy_glosry.md). SQL hierarchies can be used in the [`FROM`](abapfrom_clause.md) clause and as the source of special [hierarchy navigators](../../abap-glossary/abenhierarchy_navigator_glosry.md).

**ABAP SQL in-memory engine**

Part of the [ABAP SQL engine](../../abap-glossary/abenabap_sql_engine_glosry.md) for processing [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statements which [read](abenabap_sql_reading.md) tabular data in the memory of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). The ABAP SQL in-memory engine is used by ABAP SQL when accessing the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) or when [internal tables](../../abap-glossary/abeninternal_table_glosry.md) are specified in the [`FROM`](abapselect_itab.md) clause. The ABAP SQL in-memory engine supports a large subset of ABAP SQL but there are also some restrictions.

**ABAP SQL indicator**

[Substructure](../../abap-glossary/abensubstructure_glosry.md) or component with a [byte field type](../../abap-glossary/abenbyte_field_type_glosry.md) that can be used either in read statements as a [null indicator](../../abap-glossary/abennull_indicator_glosry.md) or in write statements as a [set indicator](../../abap-glossary/abenset_indicator_glosry.md). In read statements, the indicators can store information while in write statements, indicators can be used to mark columns for change. ABAP SQL indicators can be created as [indicator structures](../../abap-glossary/abenindicator_structure_glosry.md).

**ABAP SQL interface**

Part of the [database interface](../../abap-glossary/abendatabase_interface_glosry.md) responsible for [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statements. The ABAP SQL interface transforms ABAP SQL statements that access the [standard database](../../abap-glossary/abenstandard_db_glosry.md) of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) to vendor-specific [SQL](../../abap-glossary/abensql_glosry.md) and forwards the results to the [database system](../../abap-glossary/abendatabase_system_glosry.md).

**ABAP SQL literal**

An [ABAP literal](../../abap-glossary/abenabap_literal_glosry.md) used in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md). In contrast to general ABAP, in ABAP SQL, both [typed literals](../../abap-glossary/abentyped_literal_glosry.md) and [untyped literal](../../abap-glossary/abenuntyped_literal_glosry.md) are available.

**ABAP SQL query**

[Database query](../../abap-glossary/abendb_query_glosry.md) that is implemented in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) with the [DQL](../../abap-glossary/abendql_glosry.md) language element `SELECT`. The [clauses and additions](abenselect_clauses.md) of `SELECT` define the result set returned by the database. &#x200E;See [main query](../../abap-glossary/abenmainquery_glosry.md) and [subquery](../../abap-glossary/abensubquery_glosry.md).

**ADBC connection object**

An instance of a class that implements `IF_SQL_CONNECTION` and represents a valid [database connection](../../abap-glossary/abendatabase_connection_glosry.md).

**aggregate**

The result of an [aggregate function](../../abap-glossary/abenaggregate_function_glosry.md). Can be determined using aggregate functions in an ABAP SQL [`SELECT`](abapselect.md) statement or in the [`SELECT`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_aggregate_functions_v2.md) list of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md).

**aggregate expression**

In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) or in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md), an aggregate expression uses an [aggregate function](../../abap-glossary/abenaggregate_function_glosry.md) to determine a value from the values of a column of the result set of a [query](../../abap-glossary/abenasql_query_glosry.md).

- [Aggregate expressions in ABAP SQL](abapselect_aggregate.md)

- [Aggregate expressions in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_aggregate_functions_v2.md)

**aggregate function**

A function that processes multiple values together and returns a single value as a result. The calculation is done in the [database system](../../abap-glossary/abendatabase_system_glosry.md). An aggregate function can be used in an [aggregate expression](../../abap-glossary/abenaggregate_expression_glosry.md). In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), it can also be used as a [window function](../../abap-glossary/abenwindow_function_glosry.md) in a [window expression](../../abap-glossary/abenwindow_expression_glosry.md), and in a [hierarchy aggregate navigator](../../abap-glossary/abenhierarchy_agg_navi_glosry.md).

- [Aggregate functions in ABAP SQL](abensql_agg_func.md)

- [Aggregate functions in ABAP CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_aggregate_functions_v2.md)

**alias name**

A name that is assigned as a substitute name to an element, an object, etc. The following alias names can be defined in ABAP:

- The statement [`ALIASES`](../abap-declarations/abapaliases.md) can be used to declare an alias name for an [interface component](../../abap-glossary/abeninterface_component_glosry.md) in a [class](../../abap-glossary/abenclass_glosry.md) or in a [compound interface](../../abap-glossary/abencompound_interface_glosry.md).

- The addition [`ALIAS`](../abap-declarations/abaptypes_primary_key.md) can be used to specify an alias for the [primary table key](../../abap-glossary/abenprimary_key_glosry.md) and [secondary table key](../../abap-glossary/abensecondary_key_glosry.md) when declaring an [internal table](../../abap-glossary/abeninternal_table_glosry.md).

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), the addition `AS` can be used to define aliases for columns of the result set in a [`SELECT`](abapselect_list.md) list or for data sources in the [`FROM`](abapfrom_clause.md) clause.

- In [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), the addition `AS` can be used to define aliases for elements in the `SELECT` list or for [CDS associations](../../abap-glossary/abencds_association_glosry.md).

**arithmetic expression**

Formulation of an arithmetic calculation.

- In general ABAP, an [arithmetic expression](../abap-processing-internal-data/abapcompute_arith.md) is a [calculation expression](../../abap-glossary/abencalculation_expression_glosry.md). It is assigned a [calculation type](../../abap-glossary/abencalculation_type_glosry.md) that is used to execute the calculation. The result of an arithmetic expression is a numeric value that exists in the calculation type. Arithmetic expressions occur in the [read positions of specific statements](../abap-operands/abenoperands_expressions.md).

- In ABAP SQL, [arithmetic expressions](abensql_arith.md) are [SQL expressions](../../abap-glossary/abensql_expression_glosry.md).

- In ABAP CDS, [arithmetic expressions](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_arithmetic_expression_v2.md) can be used in the `SELECT` list of CDS view entities.

**arithmetic operator**

Combines two numeric [operands](../../abap-glossary/abenoperand_glosry.md) in an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md).

- In ABAP, arithmetic operators are [`+`](../abap-processing-internal-data/abenarith_operators.md), [`-`](../abap-processing-internal-data/abenarith_operators.md), [`*`](../abap-processing-internal-data/abenarith_operators.md), [`/`](../abap-processing-internal-data/abenarith_operators.md), [`DIV`](../abap-processing-internal-data/abenarith_operators.md), [`MOD`](../abap-processing-internal-data/abenarith_operators.md), and [`**`](../abap-processing-internal-data/abenarith_operators.md). See the topic [`arith_exp` - Arithmetic Operators](../abap-processing-internal-data/abenarith_operators.md) for further details.

- In ABAP SQL, arithmetic operators are [`+`](abensql_arith.md), [`-`](abensql_arith.md), [`*`](abensql_arith.md), [`/`](abensql_arith.md).

- In ABAP CDS, arithmetic operators are [`+`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_arithmetic_expression_v2.md), [`-`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_arithmetic_expression_v2.md), [`*`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_arithmetic_expression_v2.md), [`/`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_arithmetic_expression_v2.md).

**binary floating point literal**

A [numeric literal](../../abap-glossary/abennumeric_literal_glosry.md) that has the [binary floating point data type](../../abap-glossary/abenbinfloat_glosry.md) [`f`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) or [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Not available in general ABAP.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), binary floating point literals are available as [typed literals](../../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Literals in ABAP SQL](abenabap_sql_literals.md)

- [Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_literal_v2.md).

**Boolean operator**

Negates or combines [logical expressions](../../abap-glossary/abenlogical_expression_glosry.md). Boolean operators belong to the [logical operators](../../abap-glossary/abenlogical_operator_glosry.md) that are used in [logical expressions](../../abap-glossary/abenlogical_expression_glosry.md).

- In ABAP, the possible Boolean operators are [`NOT`](../abap-program-flow-logic/abenlogexp_not.md), [`AND`](../abap-program-flow-logic/abenlogexp_and.md), [`OR`](../abap-program-flow-logic/abenlogexp_or.md), and [`EQUIV`](../abap-program-flow-logic/abenlogexp_equiv.md).

- In ABAP SQL, the possible Boolean operators are `NOT`, `AND`, `OR`. For further details, see the topic [`sql_cond` - `AND`, `OR`, `NOT`, `( )`](abenwhere_logexp_andornot.md).

- In ABAP CDS, the possible Boolean operators are `NOT`, `AND`, `OR`. For further details, see the topic [CDS DDL - CDS View Entity, `cds_cond`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_conditional_expression_v2.md).

**built-in function**

A predefined function in ABAP, ABAP SQL, and ABAP CDS.

- In ABAP, built-in functions can be used as [expressions](../../abap-glossary/abenexpression_glosry.md) in [certain operand positions](../abap-operands/abenoperands_expressions.md). [Numeric functions](../../abap-glossary/abenmathematical_funktion_glosry.md), [string functions](../../abap-glossary/abenstring_function_glosry.md), [table functions](../../abap-glossary/abentable_function_glosry.md), and [byte chain functions](../../abap-glossary/abenbyte_chain_function_glosry.md) that have a return value of the corresponding data type can be distinguished. [Description functions](../../abap-glossary/abendescription_function_glosry.md) that provide information on data objects, are also available. The names of the built-in functions are a subset of the [reserved names](../../abap-glossary/abenabap_word_glosry.md). For further details, see the topic [Built-In Functions](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md).

- For ABAP SQL, [built-in functions](abensql_builtin_func.md) are part of the [SQL expressions](../../abap-glossary/abensql_expression_glosry.md).

- For built-in functions in ABAP CDS, see the topic [CDS built-in function](../../abap-glossary/abencds_builtin_func_glosry.md).

[Actual parameters](../../abap-glossary/abenactual_parameter_glosry.md) passed to the [formal parameters](../../abap-glossary/abenformal_parameter_glosry.md) of built-in functions are called also called [arguments](../../abap-glossary/abenargument_glosry.md) of the function.

**byte field literal**

A [literal](../../abap-glossary/abenabap_literal_glosry.md) of the [byte field type](../../abap-glossary/abenbyte_field_type_glosry.md) [`x`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md) or [`RAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the length of the specified bytes. Only [typed](../../abap-glossary/abentyped_literal_glosry.md) byte field literals are available.

- Not available in general ABAP.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), byte field literals are available as [typed literals](../../abap-glossary/abentyped_literal_glosry.md)

See also:

- [Typed Literals in ABAP SQL](abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_typed_literal_v2.md)

**byte string literal**

A [literal](../../abap-glossary/abenabap_literal_glosry.md) of the [byte string type](../../abap-glossary/abenbyte_string_type_glosry.md) [`xstring`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md) or [`RAWSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Not available in general ABAP.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), byte string literals are available as [typed literals](../../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_typed_literal_v2.md)

**case distinction**

[Control structure](../../abap-glossary/abencontrol_structure_glosry.md) with the [control statement](../../abap-glossary/abencontrol_statement_glosry.md) [`CASE`](../abap-program-flow-logic/abapcase.md) or [`CASE TYPE OF`](../abap-program-flow-logic/abapcase_type.md), [condition expression](../../abap-glossary/abenconditional_expression_glosry.md) with the [conditional operator](../../abap-glossary/abenconditional_operator_glosry.md) [`SWITCH`](../abap-program-flow-logic/abenconditional_expression_switch.md), [`CASE`](abensql_case.md) expression in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), or [`CASE`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_case_expression_v2.md) expression in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). In a case distinction, the value of an [operand](../../abap-glossary/abenoperand_glosry.md) determines which of multiple source code sections is executed. In the ABAP language, there are only [simple case distinctions](../../abap-glossary/abensimple_case_glosry.md). In ABAP CDS and ABAP SQL, there are [simple case distinctions](../../abap-glossary/abensimple_case_glosry.md) and [complex case distinctions](../../abap-glossary/abencomplex_case_glosry.md).

**cast**

In ABAP, see [casting](../../abap-glossary/abencast_casting_glosry.md). In [SQL](../../abap-glossary/abensql_glosry.md), a cast is a type conversion.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), the operator [`CAST`](abensql_cast.md) is used.

- In the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) of [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), the operator `CAST` is used (see [cast in CDS view entities](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_cast_expression_v2.md) or [cast in CDS DDIC-based views (obsolete)](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_cast_expression_v1.md)).

**CDS/CTE association path**

A sequence of [CDS associations](../../abap-glossary/abencds_association_glosry.md) and [CTE associations](../../abap-glossary/abencte_association_glosry.md) that associate [CDS entities](../../abap-glossary/abencds_entity_glosry.md) and [common table expressions](../../abap-glossary/abencommon_table_expression_glosry.md) with [association targets](../../abap-glossary/abenassociation_target_glosry.md). In other words, a mixture of CDS and CTE association paths. CDS or CTE association paths can be specified in the form of [SQL path expressions](../../abap-glossary/abensql_path_expression_glosry.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md).

**character literal**

Also referred to as text literal. A [literal](../../abap-glossary/abenabap_literal_glosry.md) with a [character-like data type](../../abap-glossary/abencharlike_data_type_glosry.md) whose value is a [character string](../../abap-glossary/abencharacter_string_glosry.md).

- In general ABAP, character literals are [untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md).

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), character literals can be [typed literals](../../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Character Literals in ABAP](../abap-declarations/abenuntyped_character_literals.md)

- [Literals in ABAP SQL](abenabap_sql_literals.md)

- [Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_literal_v2.md)

**client dependency**

Property of a [SQL data source](../../abap-glossary/abensql_data_source_glosry.md). A SQL data source can be [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md) or [client-independent](../../abap-glossary/abenclient_independent_glosry.md). When accessing a client-dependent SQL data source in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), an implicit [client handling](../../abap-glossary/abenclient_handling_glosry.md) takes place.

**client handling**

Processing of the application data of a [client](../../abap-glossary/abenclient_glosry.md). When accessing [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md) [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md) or [views](../../abap-glossary/abenview_glosry.md), [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statements use [implicit client](abenabap_sql_client_handling.md) handling, which by default accesses the [current client](../../abap-glossary/abencurrent_client_glosry.md). By using additions to the ABAP SQL statements, the implicit client handling can be switched to other clients. The client handling of [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md) can be defined with special [AMDP options](abapmethods_amdp_options_client.md).

**client isolation**

Client isolation on an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) means that an [ABAP user](../../abap-glossary/abenabap_user_glosry.md) has access to data of the [current client](../../abap-glossary/abencurrent_client_glosry.md) only. In [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md), client isolation is enforced as follows:

- Implicit [client handling](../../abap-glossary/abenclient_handling_glosry.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md).

- [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md) can access [client-safe](../../abap-glossary/abenclient_safe_glosry.md) [repository objects](../../abap-glossary/abenrepository_object_glosry.md) only.

- [CDS entities](../../abap-glossary/abencds_entity_glosry.md) that are [released APIs](../../abap-glossary/abenreleased_api_glosry.md) must be [client-safe](../../abap-glossary/abenclient_safe_glosry.md).

**client literal**

A [literal](../../abap-glossary/abenabap_literal_glosry.md) that contains a [client ID](../../abap-glossary/abenclient_identifier_glosry.md) and has the data type [`CLNT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Not available in general ABAP.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), client literals are available as [typed literals](../../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_typed_literal_v2.md)

**client-dependent**

A [SQL data source](../../abap-glossary/abensql_data_source_glosry.md) for which an implicit [client handling](../../abap-glossary/abenclient_handling_glosry.md) takes place when accessed with [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md).

- A [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md) or DDIC view in [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md) is client-dependent if the first column is a [client column](../../abap-glossary/abenclient_column_glosry.md). The system table `T000`, which contains the [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) [client IDs](../../abap-glossary/abenclient_identifier_glosry.md), is an exception to this rule.

- The client dependency of a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) is determined by its data sources. Client handling is by done implicitly by filtering the [session variable](../../abap-glossary/abensession_variable_glosry.md) `$session.client`.

- The client dependency of [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) is declared in the [CDS source code](../../abap-glossary/abencds_source_code_glosry.md) by the [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) `@CLientHandling.type`.

See also: [client-independent](../../abap-glossary/abenclient_independent_glosry.md).

**client-independent**

A [SQL data source](../../abap-glossary/abensql_data_source_glosry.md) that is not [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md). Client-independent SQL data sources contain data that is not specific to a [client](../../abap-glossary/abenclient_glosry.md) and should be accessed by [system programs](../../abap-glossary/abensystem_program_glosry.md). See also [system table](../../abap-glossary/abensystem_table_glosry.md).

**coalesce function**

A [built-in function](../../abap-glossary/abenbuiltin_function_glosry.md) that returns the first non-zero expression in a list of expressions. Available in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) and [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md).

**column selector**

Character `~`. A column `col` of a [data source](abapselect_data_source.md) can be addressed in a [query](../../abap-glossary/abenasql_query_glosry.md) of [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) using `name~col`, where `name` is the name of the entity in which the column is defined. This type of addressing is necessary if, when multiple database tables are accessed, the name of a column occurs in a number of different database tables, when a comparison of a [SQL condition](../../abap-glossary/abensql_cond_glosry.md) compares two columns.

**common table expression**

CTE for short. Common table expressions are defined in the [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statement [`WITH`](abapwith.md) via [subqueries](../../abap-glossary/abensubquery_glosry.md). The [main query](../../abap-glossary/abenmainquery_glosry.md) of the `WITH` statement accesses its common table expressions.

**comparison operator**

[Relational operator](../../abap-glossary/abenrel_operator_glosry.md) that combines two or more [operands](../../abap-glossary/abenoperand_glosry.md) of a [comparison expression](../../abap-glossary/abencomparison_expression_glosry.md) or of an [SQL condition](../../abap-glossary/abensql_cond_glosry.md).

**complex case distinction**

Also searched case. A [case distinction](../../abap-glossary/abencase_distinction_glosry.md) that evaluates logical expressions to determine which statements to execute. Available in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) and [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md).

**correlated subquery**

[Subquery](../../abap-glossary/abensubquery_glosry.md) that uses columns of the surrounding [query](../../abap-glossary/abenasql_query_glosry.md) in its [SQL conditions](../../abap-glossary/abensql_cond_glosry.md). It must be possible to assign the column to a [SQL data source](../../abap-glossary/abensql_data_source_glosry.md) in the surrounding query. A correlated subquery is evaluated for each individual row of the result set of the surrounding query.

**cross join**

A [join type](../../abap-glossary/abenjoin_type_glosry.md) for which the rows of the result set are determined by a cross product of the result sets of both [SQL data sources](../../abap-glossary/abensql_data_source_glosry.md). The result set contains all possible combinations of rows.

**CTE**

Common Table Expression *-\>* [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md)

**CTE association**

[Association](../../abap-glossary/abenassociation_glosry.md) that is defined for a [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) ([CTE](../../abap-glossary/abencte_glosry.md)) and can be used in the [queries](../../abap-glossary/abenasql_query_glosry.md) of its [`WITH`](abapwith.md) statement in [SQL path expressions](../../abap-glossary/abensql_path_expression_glosry.md). A CTE association is defined in the definition of the common table expression using the addition [`WITH ASSOCIATIONS JOIN`](abapwith_associations_defining.md).

**CTE association path**

A sequence of [CTE associations](../../abap-glossary/abencte_association_glosry.md) that link [common table expressions](../../abap-glossary/abencommon_table_expression_glosry.md) with [association targets](../../abap-glossary/abenassociation_target_glosry.md). CTE association paths can be specified in the form of [SQL path expressions](../../abap-glossary/abensql_path_expression_glosry.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md).

**CTE hierarchy**

[Common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) ([CTE](../../abap-glossary/abencte_glosry.md)) that can be used as an [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) in the subsequent [queries](../../abap-glossary/abenasql_query_glosry.md) of its [`WITH`](abapwith.md) statement. A CTE hierarchy is created when the common table expression is defined using the addition [`WITH HIERARCHY`](abapwith_hierarchy.md).

**currency field literal**

A [literal](../../abap-glossary/abenabap_literal_glosry.md) of the data type [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Not available in general ABAP.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), currency field literals are available as [typed literals](../../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_typed_literal_v2.md)

**currency key literal**

A [literal](../../abap-glossary/abenabap_literal_glosry.md) of the data type [`CUKY`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) that contains a [currency code](../../abap-glossary/abencurrency_id_glosry.md).

- Not available in general ABAP.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), currency key literals are available as [typed literals](../../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_typed_literal_v2.md)

**current client**

The current client of a [user session](../../abap-glossary/abenuser_session_glosry.md) is the [client](../../abap-glossary/abenclient_glosry.md) whose [client ID](../../abap-glossary/abenclient_identifier_glosry.md) was specified during [logon](../../abap-glossary/abenlogon_glosry.md). ABAP

**database cursor**

Pointer to the result set of a database selection. The database cursor is always assigned to a line of the result set. In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), cursor handling is implicit, except for the statements `OPEN CURSOR`, `FETCH`, and `CLOSE CURSOR`. A program can open a maximum of 17 database cursors simultaneously using the [ABAP SQL interface](../../abap-glossary/abenabap_sql_interface_glosry.md).

**database hint**

An extension of the SQL standard that tells a [database system](../../abap-glossary/abendatabase_system_glosry.md) or the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) how to execute an access. Database hints are usually dependent on the database system and its release. In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), database hints can be specified using the addition [`%_HINTS`](abenabap_sql_db_hints.md). In [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), the annotation [`Consumption.dbHints`](../../abap-core-data-services-abap-cds/abap-cds-annotations/abencds_710938603-_anno.md) can be used.

**database query**

Query for short. A database query is used to retrieve data from [database tables](../../abap-glossary/abendatabase_table_glosry.md). In [SQL](../../abap-glossary/abensql_glosry.md), queries are generally expressed in its subset [DQL](../../abap-glossary/abendql_glosry.md) (Data Query Language). In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) a query is called [ABAP SQL Query](../../abap-glossary/abenasql_query_glosry.md). In [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), queries appear in the SQL-part of the definitions of [CDS views](../../abap-glossary/abencds_view_glosry.md).

**date literal**

A [literal](../../abap-glossary/abenabap_literal_glosry.md) that contains a date. It has the data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Not available in general ABAP.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), date literals are available as [typed literals](../../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_typed_literal_v2.md)

**DCL**

Short for Data Control Language. A subset of [SQL](../../abap-glossary/abensql_glosry.md). The statements of the DCL perform authorization and consistency checks on [relational databases](../../abap-glossary/abenrelational_database_glosry.md).

- [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) does not support DCL. On an Application Server ABAP, the functionality of the [DCL](../../abap-glossary/abencds_dcl_glosry.md) is implemented using [authorization objects](../../abap-glossary/abenauthorization_object_glosry.md) and SAP locks.

- [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) provides a [DCL](../../abap-glossary/abencds_dcl_glosry.md) that implements an [access control](../../abap-glossary/abencds_access_control_glosry.md), where database objects can be linked to authorization objects of AS ABAP.

**DDL**

Short for Data Definition Language. A subset of [SQL](../../abap-glossary/abensql_glosry.md). The statements in the DDL create and delete the objects of a [relational database](../../abap-glossary/abenrelational_database_glosry.md). In an ABAP system, [ABAP-managed database objects](../../abap-glossary/abenabap_managed_db_object_glosry.md) are edited using tools and frameworks in [AS ABAP](../../abap-glossary/abenas_abap_glosry.md), such as [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md), [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), and [AMDP](../../abap-glossary/abenamdp_glosry.md), where [DDIC DDL](../../abap-glossary/abenddic_dcl_glosry.md), [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md), or Native SQL are used. [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) does not support DDL.

**decimal floating point literal**

A [numeric literal](../../abap-glossary/abennumeric_literal_glosry.md) of a [decimal floating point type](../../abap-glossary/abendecfloat_type_glosry.md).

- Not available in general ABAP.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), decimal floating point literals are available as [typed literals](../../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_typed_literal_v2.md)

**DML**

Short for Data Manipulation Language. Subset of [SQL](../../abap-glossary/abensql_glosry.md). The statements in DML perform [CUD](../../abap-glossary/abencud_glosry.md) operations on [relational](../../abap-glossary/abenrelational_database_glosry.md) [database tables](../../abap-glossary/abendatabase_table_glosry.md). In the ABAP language, DML is implemented predominantly by the statements for [write accesses](abenabap_sql_writing.md) of [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md). **Note:** Sometimes the term DML also includes the statements of [DQL](../../abap-glossary/abendql_glosry.md).

**DQL**

Short for Data Query Language. Subset of [SQL](../../abap-glossary/abensql_glosry.md). The statements in DQL perform read operations on [relational](../../abap-glossary/abenrelational_database_glosry.md) [database tables](../../abap-glossary/abendatabase_table_glosry.md). In the ABAP language, DQL is implemented predominantly by the statements for [read accesses](abenabap_sql_reading.md) of [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md). In [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), the DQL statement `SELECT` is embedded in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) for [CDS views](../../abap-glossary/abencds_view_glosry.md). **Note:** Sometimes the statements of DQL are included in the term [DML](../../abap-glossary/abendml_glosry.md).

**filter condition**

Specifies a condition for a [CDS association](../../abap-glossary/abencds_association_glosry.md) or [CTE association](../../abap-glossary/abencte_association_glosry.md) in an [SQL path expression](../../abap-glossary/abensql_path_expression_glosry.md).

**grouping set**

Grouping sets are used in the [`GROUP BY`](abapgroupby_clause.md) clause of a [query](../../abap-glossary/abenasql_query_glosry.md). A grouping set is specified either as an empty grouping set or as a comma-separated list. Columns and SQL expressions can also be used in the list. The `GROUP BY` addition `GROUPING SETS` makes it possible to define multiple grouping sets under a `GROUP BY` clause. The grouping sets are aggregated separately and merged into one result set.

**hierarchy aggregate navigator**

A [hierarchy navigator](../../abap-glossary/abenhierarchy_navigator_glosry.md) that accesses specific [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md) of a [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md), such as [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md) or [ancestor nodes](../../abap-glossary/abenancestor_node_glosry.md), and applies [aggregate functions](../../abap-glossary/abenaggregate_function_glosry.md) to them.

**hierarchy association**

A [CDS association](../../abap-glossary/abencds_association_glosry.md) or [CTE association](../../abap-glossary/abencte_association_glosry.md) used to define the [parent-child relationships](../../abap-glossary/abenpcr_glosry.md) of a [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) or [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md). A hierarchy association is always a [self-association](../../abap-glossary/abenself_association_glosry.md).

**hierarchy attribute**

A component of the tabular result set of a [hierarchy function](../../abap-glossary/abenhierarchy_function_glosry.md) that contains hierarchy-specific information for each row. When a [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) is accessed in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), the hierarchy attributes can be included in the result set as [hierarchy columns](../../abap-glossary/abenhierarchy_column_glosry.md) of [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md). The hierarchy attributes can be used to define elements of the CDS hierarchy can be used in the definition of a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md).

**hierarchy column**

A column of the result set of an [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) [query](../../abap-glossary/abenasql_query_glosry.md) on a [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) or on a [hierarchy navigator](../../abap-glossary/abenhierarchy_navigator_glosry.md) containing a [hierarchy attribute](../../abap-glossary/abenhierarchy_attribute_glosry.md). A hierarchy column must first be specified explicitly in the [`SELECT`](abapselect_list.md) list before it can be included in the result set.

**hierarchy edge**

The relationship between the [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md) of a [hierarchy](../../abap-glossary/abenhierarchy_glosry.md). The hierarchy edges in [ABAP SQL hierarchies](../../abap-glossary/abensql_hierarchy_glosry.md) created by a [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) or in a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md) are [parent-child relationships](../../abap-glossary/abenpcr_glosry.md).

**hierarchy function**

In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), a special [table function](../../abap-glossary/abentable_function_glosry.md) for processing [ABAP SQL hierarchies](../../abap-glossary/abensql_hierarchy_glosry.md). A [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md), for example, is used to create SQL hierarchies, whereas [hierarchy navigators](../../abap-glossary/abenhierarchy_navigator_glosry.md) are used to access them. In the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md), there are built-in hierarchy functions that are wrapped by ABAP SQL and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md).

**hierarchy generator**

A [hierarchy function](../../abap-glossary/abenhierarchy_function_glosry.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) that creates a [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) either as a [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md) or a [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md).

**hierarchy navigator**

A [hierarchy function](../../abap-glossary/abenhierarchy_function_glosry.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) that accesses a [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md).

**hierarchy node navigator**

A [hierarchy navigator](../../abap-glossary/abenhierarchy_navigator_glosry.md) that accesses specific [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md) in an ABAP [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md), such as [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md), [ancestor nodes](../../abap-glossary/abenancestor_node_glosry.md), or [sibling nodes](../../abap-glossary/abensibling_node_glosry.md).

**hierarchy source**

A [SQL data source](../../abap-glossary/abensql_data_source_glosry.md) that exposes a [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md) and can be used as a source of a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md) or the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) of [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md).

**host constant**

[Host variable](../../abap-glossary/abenhost_variable_glosry.md) for which the ABAP [data object](../../abap-glossary/abendata_object_glosry.md) is a [constant](../../abap-glossary/abenconstant_glosry.md).

**host expression**

ABAP-[expression](../../abap-glossary/abenexpression_glosry.md) specified in an operand position of an [ABAP SQL](abenabap_sql_host_expressions.md) statement. Host expressions are always specified in parentheses preceded by the [escape character](../../abap-glossary/abenescape_character_glosry.md) `@`: `@( ... )`.

**host variable**

ABAP [data object](../../abap-glossary/abendata_object_glosry.md) specified in an operand position of an [ABAP SQL](abenabap_sql_host_variables.md) statement or of a statically embedded Native SQL statement. The ABAP data object can be a [variable](../../abap-glossary/abenvariable_glosry.md) or a [constant](../../abap-glossary/abenconstant_glosry.md) (see [host constant](../../abap-glossary/abenhost_constant_glosry.md)). In ABAP SQL, a host variable must be prefixed with the [escape character](../../abap-glossary/abenescape_character_glosry.md) `@` ; in Native SQL with the escape character `:`. In ADBC, the placeholder `?` to which ABAP data objects are bound, is used instead of host variables.

**indicator structure**

[Substructure](../../abap-glossary/abensubstructure_glosry.md) of a [structured type](../../abap-glossary/abenstructured_type_glosry.md). The indicator structure is the last component of the structured type and mirrors the preceding components. The components of the substructure serve as indicators for features of the preceding components. Besides actual indicator structures, there are also [condensed indicator structures](../../abap-glossary/abencondensed_ind_structure_glosry.md) that are realized by [byte fields](../../abap-glossary/abenbyte_field_glosry.md) where the individual bits serve as indicators. Indicator structures can be defined with the addition [`WITH INDICATORS`](../abap-declarations/abaptypes_indicators.md) of the statement [`TYPES`](../abap-declarations/abaptypes_indicators.md) and can be used as [ABAP SQL indicators](../../abap-glossary/abenabap_sql_indicator_glosry.md). In the latter case, also [inline declarations](../../abap-glossary/abeninline_declaration_glosry.md) are possible.

**integer literal**

A [numeric literal](../../abap-glossary/abennumeric_literal_glosry.md) of an [integer type](../../abap-glossary/abeninteger_type_glosry.md).

- In general ABAP, integer literals are [untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md).

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), integer literals can be [typed literals](../../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Numeric Literals in ABAP](../abap-declarations/abenuntyped_number_literals.md)

- [Literals in ABAP SQL](abenabap_sql_literals.md)

- [Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_literal_v2.md)

**join**

A combination of two [SQL data sources](../../abap-glossary/abensql_data_source_glosry.md) into one result set, consisting of columns of both data sources. The rows of the result set are determined by the [join type](../../abap-glossary/abenjoin_type_glosry.md) and by [join conditions](../../abap-glossary/abenjoin_condition_glosry.md) between columns of the data sources. The relation between the rows of the data sources can be expressed by a [cardinality](../../abap-glossary/abencardinality_glosry.md). Joins can be implemented in ABAP as follows:

- DDIC views in the [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md)

- [Join expressions](../../abap-glossary/abenjoin_expression_glosry.md) in [queries](../../abap-glossary/abenasql_query_glosry.md) of [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md)

- [Join expressions](../../abap-glossary/abenjoin_expression_glosry.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) of [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md)

Furthermore, [CDS associations](../../abap-glossary/abencds_association_glosry.md) and [CTE associations](../../abap-glossary/abencte_association_glosry.md) define join relationships that are instantiated when the associations are used in [SQL path expressions](../../abap-glossary/abensql_path_expression_glosry.md).

**join condition**

A [SQL condition](../../abap-glossary/abensql_cond_glosry.md) or a [CDS DDL condition](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_conditional_expression_v2.md) specified after the addition `ON` of a [join expression](../../abap-glossary/abenjoin_expression_glosry.md). Also called `ON` condition.

**join expression**

The implementation of a [join](../../abap-glossary/abenjoin_glosry.md) in [SQL](../../abap-glossary/abensql_glosry.md) using the addition `JOIN`. Join expressions can be defined in [queries](../../abap-glossary/abenasql_query_glosry.md), defined by the [`SELECT`](abapselect.md) statement of [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), the [`SELECT` statement in CDS view entities](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_select_statement_v2.md), or the [`SELECT` statement in CDS DDIC-based views (obsolete)](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_select_statement_v2.md).

**join type**

The join type determines, together with the [join conditions](../../abap-glossary/abenjoin_condition_glosry.md) of a [join expression](../../abap-glossary/abenjoin_expression_glosry.md), how the rows of its result set are combined from its [SQL data sources](../../abap-glossary/abensql_data_source_glosry.md). [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) support [inner joins](../../abap-glossary/abeninner_join_glosry.md), [outer joins](../../abap-glossary/abenouter_join_glosry.md) ([left](../../abap-glossary/abenleft_outer_join_glosry.md) and [right](../../abap-glossary/abenright_outer_join_glosry.md)), and [cross joins](../../abap-glossary/abencross_join_glosry.md).

**language key literal**

A [literal](../../abap-glossary/abenabap_literal_glosry.md) of the data type [`LANG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) that contains a language key.

- Not available in general ABAP.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), language key literals are available as [typed literals](../../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_typed_literal_v2.md)

**left outer join**

A [join type](../../abap-glossary/abenjoin_type_glosry.md) that determines the same rows as an [inner join](../../abap-glossary/abeninner_join_glosry.md) and an additional row for each row of the left [SQL data source](../../abap-glossary/abensql_data_source_glosry.md) that is not included by the [join conditions](../../abap-glossary/abenjoin_condition_glosry.md). In these rows, the columns coming from the right data source contain [null values](../../abap-glossary/abennull_value_glosry.md).

**level-based hierarchy**

An [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) that is generated from a [SQL data source](../../abap-glossary/abensql_data_source_glosry.md) where certain columns define from left to right the [hierarchy levels](../../abap-glossary/abenhierarchy_level_glosry.md) and where each row content of these columns represents a path from a [start node](../../abap-glossary/abenstart_node_glosry.md) to a [leaf node](../../abap-glossary/abenleaf_node_glosry.md) that spans these levels. In a level-based hierarchy, all [leaf nodes](../../abap-glossary/abenleaf_node_glosry.md) have the same level that is the highest level defined in the data source. For each leaf node, a similar set of [ancestor nodes](../../abap-glossary/abenancestor_node_glosry.md) is generated for the lower levels of the data source. In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), the addition [`LEVELS`](abenselect_hierarchy_gen_level.md) of the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](abenselect_hierarchy_generator.md) can be used to generate level-based hierarchies.

**leveled hierarchy**

*-\>* [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md)

**literal**

The textual representation of a value in the [ABAP source code](../../abap-glossary/abenabap_source_code_glosry.md) of an [ABAP program](../../abap-glossary/abenabap_program_glosry.md) or in a [CDS object](../../abap-glossary/abencds_object_glosry.md). There are [typed literals](../../abap-glossary/abentyped_literal_glosry.md) and [untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md) available.

See also:

- [ABAP literal](../../abap-glossary/abenabap_literal_glosry.md)

- [ABAP SQL literal](../../abap-glossary/abenabap_sql_literal_glosry.md)

- [CDS literal](../../abap-glossary/abencds_literal_glosry.md)

**literal operator**

The literal operator `&` joins two [text field literals](../../abap-glossary/abentext_field_literal_glosry.md) or two [text string literals](../../abap-glossary/abentext_string_literal_glosry.md) as a single literal or two [string templates](../../abap-glossary/abenstring_template_glosry.md) as a single string template. The literal operator is supported in [ABAP literals](../../abap-glossary/abenabap_literal_glosry.md) and in [ABAP SQL literals](../../abap-glossary/abenabap_sql_literal_glosry.md), but not in [CDS literals](../../abap-glossary/abencds_literal_glosry.md).

**LOB handle**

An object from one of the [system classes](../../abap-glossary/abensystem_class_glosry.md) that support [streaming](abenabap_sql_streaming.md) and [locators](abenlocators.md) for [LOBs](../../abap-glossary/abenlob_glosry.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md). These classes all implement the [interface](../../abap-glossary/abenoo_intf_glosry.md) `IF_ABAP_DB_LOB_HANDLE`. See also: [LOB Handle Structure](../../abap-glossary/abenlob_handle_structure_glosry.md).

**LOB handle component**

[Reference type](../../abap-glossary/abenreference_type_glosry.md) or [reference variable](../../abap-glossary/abenreference_variable_glosry.md) in a [LOB handle structure](../../abap-glossary/abenlob_handle_structure_glosry.md). The [static type](../../abap-glossary/abenstatic_type_glosry.md) of such a component must be less specific or the same as the [class](../../abap-glossary/abenclass_glosry.md) of a [LOB handle](../../abap-glossary/abenlob_handle_glosry.md) and must contain the [interface](../../abap-glossary/abenoo_intf_glosry.md) `IF_ABAP_DB_LOB_HANDLE`.

**LOB handle structure**

The [structure](../../abap-glossary/abenstructure_glosry.md) of a special [work area](../../abap-glossary/abenwork_area_glosry.md) to support [streaming](../../abap-glossary/abenstreaming_glosry.md) and [locators](../../abap-glossary/abenlocator_glosry.md) for [LOBs](../../abap-glossary/abenlob_glosry.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md). LOB handle structures have the same components as [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md), DDIC views, or [CDS entities](../../abap-glossary/abencds_entity_glosry.md). However, there is at least one component which is assigned to a LOB, which is not a [string](../../abap-glossary/abenstring_glosry.md) but instead a [LOB handle component](../../abap-glossary/abenlob_handle_component_glosry.md). A LOB handle structure can be defined component by component with [ABAP statements](../../abap-glossary/abenabap_statement_glosry.md) or in the [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md), or it can be derived by referencing a structure that contains [LOBs](../../abap-glossary/abenlob_glosry.md).

**locator**

Pointer to substrings of [LOBs](../../abap-glossary/abenlob_glosry.md) in a [database](../../abap-glossary/abendatabase_glosry.md). In ABAP, locators are [LOB handles](../../abap-glossary/abenlob_handle_glosry.md) and are implemented using [instances](../../abap-glossary/abeninstance_glosry.md) of the corresponding [system classes](../../abap-glossary/abensystem_class_glosry.md). Locators can be linked with the database in question in [ABAP SQL statements with LOBs](../../abap-glossary/abenabap_sql_glosry.md). Different [locator types](../../abap-glossary/abenlocator_type_glosry.md) are provided for [BLOBs](../../abap-glossary/abenblob_glosry.md) and [CLOBs](../../abap-glossary/abenclob_glosry.md).

**logical expression**

Formulation of a condition for [operands](../../abap-glossary/abenoperand_glosry.md). A logical expression is a single [relational expression](../../abap-glossary/abenrelational_expression_glosry.md) or is made up of multiple relational expressions combined by [Boolean operators](../../abap-glossary/abenboolean_operator_glosry.md). The result of a logical expression is a [truth value](../../abap-glossary/abentruth_value_glosry.md), that is, either true or false.

- In general ABAP, logical expressions are used in [control statements](../../abap-glossary/abencontrol_statement_glosry.md) or other statements that contain conditions, as well as in [conditional expressions](../../abap-glossary/abenconditional_expression_glosry.md) and [Boolean functions](../../abap-glossary/abenboole_function_glosry.md). For further details, see the topic [Logical Expressions (`log_exp`)](../abap-program-flow-logic/abenlogexp.md).

- In ABAP SQL, logical expressions are used in conditions, such as `WHERE` and `ON` conditions.

- In ABAP CDS, logical expressions are used in conditions, such as `WHERE` and `ON` conditions.

**main query**

[ABAP SQL query](../../abap-glossary/abenasql_query_glosry.md) that is implemented in an [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) as a standalone [`SELECT`](abapselect.md) statement, a closing `SELECT` statement of a [`WITH`](abapwith.md) statement, or a closing `SELECT` statement of an `OPEN` `CURSOR` statement.

**null value**

A special value returned by a [database](../../abap-glossary/abendatabase_glosry.md) to indicate an undefined value or result. There are no special null values in ABAP. In assignments made to ABAP [data objects](../../abap-glossary/abendata_object_glosry.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), Native SQL, and [AMDP](../../abap-glossary/abenamdp_glosry.md), null values are transformed to type-dependent [initial values](../../abap-glossary/abeninitial_value_glosry.md). The [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md) for accessing the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and [internal tables](../../abap-glossary/abeninternal_table_glosry.md) as [data sources](abapselect_itab.md) of [ABAP SQL queries](../../abap-glossary/abenasql_query_glosry.md), however, handles null values as null values.

[ABAP SQL - Null Values](abenabap_sql_null_values.md)

[ABAP CDS - Null Values](../../abap-core-data-services-abap-cds/abencds_null_values.md)

**numeric literal**

A [literal](../../abap-glossary/abenabap_literal_glosry.md) that has a [numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md) and whose characters represent a numeric value.

- In general ABAP, numeric literals are [untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md).

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), numeric literals can be [typed literals](../../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Numeric Literals in ABAP](../abap-declarations/abenuntyped_number_literals.md)

- [Literals in ABAP SQL](abenabap_sql_literals.md)

- [Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_literal_v2.md)

**numeric text literal**

A [literal](../../abap-glossary/abenabap_literal_glosry.md) that contains [numeric text](../../abap-glossary/abennumeric_text_glosry.md) and has the length of the specified characters. The data type is [`n`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) or [`NUMC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Not available in general ABAP.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), numeric text literals are available as [untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md).

- In [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), numeric text literals can be [typed literals](../../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Literals in ABAP SQL](abenabap_sql_literals.md)

- [Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_literal_v2.md)

**Open SQL**

Former name for [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md).

**outer join**

A [type of join](../../abap-glossary/abenjoin_type_glosry.md). There are two types of outer joins:

- [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md)

- [right outer join](../../abap-glossary/abenright_outer_join_glosry.md)

**packed number literal**

A [numeric literal](../../abap-glossary/abennumeric_literal_glosry.md) of [packed number type](../../abap-glossary/abenpacked_number_type_glosry.md).

- In general ABAP, packed number literals are [untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md).

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), packed number literals can be [typed literals](../../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Numeric Literals in ABAP](../abap-declarations/abenuntyped_number_literals.md)

- [Literals in ABAP SQL](abenabap_sql_literals.md)

- [Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_literal_v2.md)

**parent-child-based hierarchy**

An [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) that is generated from a [parent-child relationship](../../abap-glossary/abenpcr_glosry.md). A parent-child-based hierarchy is based on a [SQL data source](../../abap-glossary/abensql_data_source_glosry.md) that exposes a [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md) that defines the parent-child relationship between columns of the data source. [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) can access parent-child-based hierarchies generated by a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md), by the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) using the addition [`CHILD TO PARENT ASSOCIATION`](abenselect_hierarchy_gen_assoc.md), or by a [CTE hierarchy](../../abap-glossary/abencte_hierarchy_glosry.md).

**path expression**

A sequence of [associations](../../abap-glossary/abenassociation_glosry.md) specified at an operand position. Either an [SQL path expression](../../abap-glossary/abensql_path_expression_glosry.md) or a [mesh path expression](../../abap-glossary/abenmesh_path_expression_glosry.md).

**path specification**

*-\>* [Path expression](../../abap-glossary/abenpath_expression_glosry.md)

**period**

The time interval whose limits are defined by the content of the columns of a [temporal SQL hierarchy](../../abap-glossary/abentemporal_hierarchy_glosry.md). These columns are defined when the [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) is created.

**Perl Compatible Regular Expression**

PCRE for short. [Regular expressions](../../abap-glossary/abenregular_expression_glosry.md) using the same syntax and semantics as [Perl 5](https://www.perl.org/). In general, ABAP supports [PCRE syntax](../abap-processing-internal-data/abenregex_pcre_syntax.md) for regular expressions by implementing the [PCRE2 library](https://www.pcre.org/) in the [ABAP kernel](../../abap-glossary/abenkernel_glosry.md). [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) supports PCRE by using the PCRE1 library implemented in the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md).

**quantity field literal**

A [literal](../../abap-glossary/abenabap_literal_glosry.md) of the data type [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Not available in general ABAP.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), quantity field literals are available as [typed literals](../../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_typed_literal_v2.md)

**query**

*-\>* [database query](../../abap-glossary/abendb_query_glosry.md)

**ranking function**

[Window function](../../abap-glossary/abenwindow_function_glosry.md) that assigns a criterion for the ranking within the [window](../../abap-glossary/abenwindow_glosry.md) for a line of a window on the result set of a [query](../../abap-glossary/abenasql_query_glosry.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md). The calculation is executed in the [database system](../../abap-glossary/abendatabase_system_glosry.md).

**right outer join**

A [type of join](../../abap-glossary/abenjoin_type_glosry.md) that determines the same rows as an [inner join](../../abap-glossary/abeninner_join_glosry.md) and an additional row for each row of the right [SQL data source](../../abap-glossary/abensql_data_source_glosry.md) that is not included by the [join conditions](../../abap-glossary/abenjoin_condition_glosry.md). In these rows, the columns coming from the left data source contain [null values](../../abap-glossary/abennull_value_glosry.md).

**root node set**

The set of [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md) of a [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) that are determined by their start condition. The elements of the root node set are [root nodes](../../abap-glossary/abenroot_node_glosry.md).

**scalar subquery**

[Subquery](../../abap-glossary/abensubquery_glosry.md) with a single-column result set. The [`SELECT` list](abapselect_list.md) of the subquery contains one element only.

**set expression**

Expression behind the addition [`SET`](abapupdate_source.md) of an [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) [`UPDATE`](abapupdate.md) statement.

**set indicator**

[ABAP SQL indicator](../../abap-glossary/abenabap_sql_indicator_glosry.md) in a [work area](../../abap-glossary/abenwork_area_glosry.md) or an [internal table](../../abap-glossary/abeninternal_table_glosry.md). The components of a set indicator indicate the columns of a [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md) to be changed using the [`UPDATE`](abapupdate.md) statement.

**set operator**

A set operator merges the result sets of multiple queries into a single result set. In [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) and [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), the following set operators are available:

- `EXCEPT` returns all distinct rows of the first result set that are not part of the following result sets.

- `INTERSECT` returns all distinct rows that are part of all result sets.

- `UNION` merges the result sets of all queries.

[Set operators in CDS view entities](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_set_operators.md)

[Set operators in ABAP SQL](abapunion.md)

**simple case distinction**

A [case distinction](../../abap-glossary/abencase_distinction_glosry.md) that matches an operand to another operand specified in one or more `WHEN` clauses. Available in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) and [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md).

**source cardinality**

The [cardinality](../../abap-glossary/abencardinality_glosry.md) of a [join](../../abap-glossary/abenjoin_glosry.md) or [association](../../abap-glossary/abenassociation_glosry.md) consists of a source cardinality and a [target cardinality](../../abap-glossary/abentarget_cardinality_glosry.md). The source cardinality describes the number of matching entries for the entries of the joined data source. For example, a source cardinality of one means that each record of the joined data source has zero or one matching entry in the original data source.

**SQL condition**

Logical expression in an [ABAP SQL statement](../../abap-glossary/abenabap_sql_glosry.md).

**SQL expression**

An [expression](../../abap-glossary/abenexp_glosry.md) in an [ABAP SQL statement](../../abap-glossary/abenabap_sql_glosry.md) or in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) that is evaluated by the database.

- [SQL expressions in ABAP SQL](abapsql_expr.md)

- [SQL expressions in CDS DDL](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_expressions_v2.md)

**SQL function**

Built-in database platform function that can be used in [SQL](../../abap-glossary/abensql_glosry.md). In [ABAP SQL](abenabap_sql_functions.md) and in the [CDS DDL](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_builtin_functions_v2.md) in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), a set of SQL functions can be accessed platform-independently.

**SQL injection**

Injection of malicious [SQL](../../abap-glossary/abensql_glosry.md) statements by an attacker. SQL injections are possible whenever programs use external statements or parts of statements that are then are transferred to the [database system](../../abap-glossary/abendatabase_system_glosry.md) without being checked or escaped. In ABAP, SQL injections must be prevented by appropriate checks or escaping whenever [tokens](../../abap-glossary/abentoken_glosry.md) are specified dynamically in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), when ADBC is used, and during generic programming.

**SQL operand**

Elementary operand in an [ABAP SQL statement](../../abap-glossary/abenabap_sql_glosry.md). SQL operands are columns of [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md) or [views](../../abap-glossary/abenview_glosry.md) defined in the [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md), [host variables](../../abap-glossary/abenhost_variable_glosry.md), or [host expressions](../../abap-glossary/abenhost_expression_glosry.md).

**SQL path expression**

Specifies a [CDS association path](../../abap-glossary/abencds_association_path_glosry.md), a [CTE association path](../../abap-glossary/abencte_association_path_glosry.md), or a [CDS/CTE association path](../../abap-glossary/abencds_cte_assoc_path_glosry.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) or [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md). A SQL path expression can be used as a data source, or for specifying a [SQL path target field](../../abap-glossary/abensql_target_field_glosry.md) in an operand position. For this, [CDS associations](../../abap-glossary/abencds_association_glosry.md) and [CTE associations](../../abap-glossary/abencte_association_glosry.md) are implicitly transformed into [joins](../../abap-glossary/abenjoin_glosry.md). See

- [Path Expression in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_path_expression_v2.md)

- [Path Expression in ABAP SQL](abenabap_sql_path.md).

**SQL path target field**

A field that is specified behind a [SQL path expression](../../abap-glossary/abensql_path_expression_glosry.md).

**SQL trace**

Trace function used to analyze the [SQL](../../abap-glossary/abensql_glosry.md) statements passed from the [database interface](../../abap-glossary/abendatabase_interface_glosry.md) to the [database system](../../abap-glossary/abendatabase_interface_glosry.md). It can be called from the tools [ABAP Debugger](../../abap-glossary/abenabap_debugger_glosry.md) or performance trace (transaction `ST05`).

**start node**

- In a [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md), a [hierarchy node](../../abap-glossary/abenhierarchy_node_glosry.md) from which a [hierarchy node navigator](../../abap-glossary/abenhierarchy_node_navi_glosry.md) determines further hierarchy nodes and adds them to its result set.

- In a [mesh](../../abap-glossary/abenmesh_glosry.md), a [mesh node](../../abap-glossary/abenmesh_node_glosry.md) for which a [mesh association](../../abap-glossary/abenmesh_association_glosry.md) is defined is the association's start node.

**string literal**

Either [text string literal](../../abap-glossary/abentext_string_literal_glosry.md) or [byte string literal](../../abap-glossary/abenbyte_string_literal_glosry.md).

**subquery**

[ABAP SQL query](../../abap-glossary/abenasql_query_glosry.md) that is used in an [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statement for subqueries. Subqueries are possible in [SQL conditions](../../abap-glossary/abensql_cond_glosry.md), for the definition of a [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) after [`WITH`](abapwith.md), or as a [data source](abapinsert_from_select.md) of an [`INSERT`](abapinsert_dbtab.md) or [`MODIFY`](abapmodify_dbtab.md) statement.

**table buffer**

An area in the [shared memory](../../abap-glossary/abenshared_memory_glosry.md) for [table buffering](../../abap-glossary/abentable_buffering_glosry.md). The table buffer is managed by the [database interface](../../abap-glossary/abendatabase_interface_glosry.md) and when accessed by [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), tables in the table buffer are processed by the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md).

**table buffering**

[Buffering](../../abap-glossary/abensap_buffering_old_glosry.md) of data from [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md), [DDIC database views](../../abap-glossary/abendatabase_view_glosry.md), or from [CDS entities](../../abap-glossary/abencds_entity_glosry.md) in a [table buffer](../../abap-glossary/abentable_buffer_glosry.md) in the [shared memory](../../abap-glossary/abenshared_memory_glosry.md) of the current [AS instance](../../abap-glossary/abenas_instance_glosry.md). Whether and how a DDIC database table or a DDIC database view is buffered is determined by its [technical settings](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_buffer.md). For a CDS entity, the buffering is determined by annotations and a [CDS entity buffer](../../abap-glossary/abencds_entity_buffer_glosry.md). Buffering is managed by the [database interface](../../abap-glossary/abendatabase_interface_glosry.md). Table buffering is applied implicitly when the database is accessed using [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and from classic dynpros. In ABAP SQL, the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) processes the tabular data in the table buffer.

**temporal SQL hierarchy**

A special [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) that only contains [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md) that meet certain conditions for time intervals. When the SQL hierarchy is created with the addition [`PERIOD`](abenselect_hierarchy_generator.md) in [ABAP SQL](abenabap_sql.md) or [`PERIOD`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_define_hierarchy.md) in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), columns of the [SQL data source](../../abap-glossary/abensql_data_source_glosry.md) of the hierarchy are defined as interval limits of so-called [periods](../../abap-glossary/abenperiod_glosry.md) and a time interval is specified for the [root node set](../../abap-glossary/abenroot_node_set_glosry.md). [Validity intervals](../../abap-glossary/abenvalidity_interval_glosry.md) are determined as intersections of these time intervals. Only nodes with non-empty validity intervals are included in the hierarchy. The validity intervals of [child nodes](../../abap-glossary/abenchild_node_glosry.md) result from their period and the validity interval of the [parent node](../../abap-glossary/abenparent_node_glosry.md).

**text field literal**

A [character literal](../../abap-glossary/abencharacter_literal_glosry.md) of the [text field type](../../abap-glossary/abentext_field_type_glosry.md) [`c`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) or [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the length of the specified characters. A text field literal can be linked to a [text symbol](../../abap-glossary/abentext_symbol_glosry.md).

- In general ABAP, text field literals are [untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md) delimited by single quotes.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), text field literals can be [typed literals](../../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Character Literals in ABAP](../abap-declarations/abenuntyped_character_literals.md)

- [Literals in ABAP SQL](abenabap_sql_literals.md)

- [Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_literal_v2.md)

**text literal**

*-\>* [Character literal](../../abap-glossary/abencharacter_literal_glosry.md)

**text string literal**

A [character literal](../../abap-glossary/abencharacter_literal_glosry.md) of the [text string](../../abap-glossary/abentext_string_type_glosry.md) type [`string`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md).

- In general ABAP, text string literals are [untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md) delimited by backquotes.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), text string literals can be [typed literals](../../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Character Literals in ABAP](../abap-declarations/abenuntyped_character_literals.md)

- [Literals in ABAP SQL](abenabap_sql_literals.md)

- [Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_literal_v2.md)

**time literal**

A [literal](../../abap-glossary/abenabap_literal_glosry.md) of the data type [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Not available in general ABAP.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), time literals are available as [typed literals](../../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_typed_literal_v2.md)

**time stamp literal**

A [literal](../../abap-glossary/abenabap_literal_glosry.md) of the data type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Not available in general ABAP.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), time stamp literals are available as [typed literals](../../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_typed_literal_v2.md)

**typed literal**

A [literal](../../abap-glossary/abenliteral_glosry.md) whose [data type](../../abap-glossary/abendata_type_glosry.md) is specified explicitly.

See also [untyped literal](../../abap-glossary/abenuntyped_literal_glosry.md).

**unit key literal**

A [literal](../../abap-glossary/abenabap_literal_glosry.md) of the data type [`UNIT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) that contains a [unit key](../../abap-glossary/abenunit_glosry.md).

- Not available in general ABAP.

- In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md), unit key literals are available as [typed literals](../../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_typed_literal_v2.md)

**untyped literal**

A [literal](../../abap-glossary/abenliteral_glosry.md) whose [data type](../../abap-glossary/abendata_type_glosry.md) is implicitly derived from its value or its delimiter. Both untyped [numeric literals](../../abap-glossary/abennumeric_literal_glosry.md) and untyped [character literals](../../abap-glossary/abencharacter_literal_glosry.md) exist. See also [typed literal](../../abap-glossary/abentyped_literal_glosry.md).

**validity interval**

The time interval that is assigned to each [hierarchy node](../../abap-glossary/abenhierarchy_node_glosry.md) of a [temporal SQL hierarchy](../../abap-glossary/abentemporal_hierarchy_glosry.md). The validity interval is the intersection of the validity interval of the [ancestor node](../../abap-glossary/abenancestor_node_glosry.md) and the [period](../../abap-glossary/abenperiod_glosry.md) of the current node.

**value function**

A [window function](../../abap-glossary/abenwindow_function_glosry.md) that determines a value from a different row of the window for a row of a [window](../../abap-glossary/abenwindow_glosry.md) in the result set of a [query](../../abap-glossary/abenasql_query_glosry.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md). The calculation is executed in the [database system](../../abap-glossary/abendatabase_system_glosry.md).

**window**

On a user interface, a window is a framed area on the screen. A window in SAP GUI is referred to as a GUI window.

In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), a window is a subset of the result set of a [query](../../abap-glossary/abenasql_query_glosry.md) defined by a [window expression](../../abap-glossary/abenwindow_expression_glosry.md) to whose rows a [window function](../../abap-glossary/abenwindow_function_glosry.md) is applied.

**window expression**

In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), a window expression uses [`OVER`](abapselect_over.md) to define a subset of the result set of a [query](../../abap-glossary/abenwindow_function_glosry.md) and applies a [window function](../../abap-glossary/abenwindow_function_glosry.md) to it.

**window function**

A function that is specified in front of the definition of a [window](../../abap-glossary/abenwindow_glosry.md) in an [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) [window expression](../../abap-glossary/abenwindow_expression_glosry.md) and that evaluates the rows of the window. A window function is either an [aggregate function](../../abap-glossary/abenaggregate_function_glosry.md), a [ranking function](../../abap-glossary/abenranking_function_glosry.md), or a [value function](../../abap-glossary/abenvalue_function_glosry.md).
