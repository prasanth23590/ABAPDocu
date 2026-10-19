---
title: "ABAP CDS Glossary"
source_file: abencds_glossary.html
section: "ABAP Core Data Services (ABAP CDS)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS Glossary

In the following, terms of the ABAP Glossary are listed that are relevant for ABAP CDS.

**ABAP annotation**

[SAP annotation](../abap-glossary/abensap_annotation_glosry.md) that can be specified in [CDS source code](../abap-glossary/abencds_source_code_glosry.md) and that is evaluated by the ABAP Core Data Services framework, namely the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) itself. Any other [CDS annotations](../abap-glossary/abencds_annotation_glosry.md) are [framework-specific annotations](../abap-glossary/abenfrmwrk_annotation_glosry.md) and must be evaluated by their own frameworks.

**ABAP CDS**

*-\>* [ABAP Core Data Services](../abap-glossary/abenabap_core_data_services_glosry.md)

**ABAP Core Data Services**

ABAP CDS for short. An infrastructure for defining and consuming semantically rich data models on [AS ABAP](../abap-glossary/abenas_abap_glosry.md). ABAP CDS provides different languages for defining metadata realized as [CDS objects](../abap-glossary/abencds_object_glosry.md). ABAP CDS is based on SQL but provides more features and sublanguages than SQL.

**ABAP tuning object**

Synonym for app-server tuning object. A [tuning object](../abap-glossary/abentuning_object_glosry.md) that defines the technical settings for a [CDS entity](../abap-glossary/abencds_entity_glosry.md) on [AS ABAP](../abap-glossary/abenas_abap_glosry.md). ABAP tuning objects are defined as [CDS objects](../abap-glossary/abencds_object_glosry.md) in [CDS source code](../abap-glossary/abencds_source_code_glosry.md). Currently, there are the following ABAP tuning objects:

- [CDS entity buffers](../abap-glossary/abencds_entity_buffer_glosry.md)

**aggregate**

The result of an [aggregate function](../abap-glossary/abenaggregate_function_glosry.md). Can be determined using aggregate functions in an ABAP SQL [`SELECT`](../abap-programming-language/abap-database-access/abapselect.md) statement or in the [`SELECT`](abap-cds-data-definitions/abencds_aggregate_functions_v2.md) list of a [CDS view entity](../abap-glossary/abencds_v2_view_glosry.md).

**aggregate expression**

In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) or in [CDS DDL](../abap-glossary/abencds_ddl_glosry.md), an aggregate expression uses an [aggregate function](../abap-glossary/abenaggregate_function_glosry.md) to determine a value from the values of a column of the result set of a [query](../abap-glossary/abenasql_query_glosry.md).

- [Aggregate expressions in ABAP SQL](../abap-programming-language/abap-database-access/abapselect_aggregate.md)

- [Aggregate expressions in CDS](abap-cds-data-definitions/abencds_aggregate_functions_v2.md)

**aggregate function**

A function that processes multiple values together and returns a single value as a result. The calculation is done in the [database system](../abap-glossary/abendatabase_system_glosry.md). An aggregate function can be used in an [aggregate expression](../abap-glossary/abenaggregate_expression_glosry.md). In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md), it can also be used as a [window function](../abap-glossary/abenwindow_function_glosry.md) in a [window expression](../abap-glossary/abenwindow_expression_glosry.md), and in a [hierarchy aggregate navigator](../abap-glossary/abenhierarchy_agg_navi_glosry.md).

- [Aggregate functions in ABAP SQL](../abap-programming-language/abap-database-access/abensql_agg_func.md)

- [Aggregate functions in ABAP CDS](abap-cds-data-definitions/abencds_aggregate_functions_v2.md)

**alias name**

A name that is assigned as a substitute name to an element, an object, etc. The following alias names can be defined in ABAP:

- The statement [`ALIASES`](../abap-programming-language/abap-declarations/abapaliases.md) can be used to declare an alias name for an [interface component](../abap-glossary/abeninterface_component_glosry.md) in a [class](../abap-glossary/abenclass_glosry.md) or in a [compound interface](../abap-glossary/abencompound_interface_glosry.md).

- The addition [`ALIAS`](../abap-programming-language/abap-declarations/abaptypes_primary_key.md) can be used to specify an alias for the [primary table key](../abap-glossary/abenprimary_key_glosry.md) and [secondary table key](../abap-glossary/abensecondary_key_glosry.md) when declaring an [internal table](../abap-glossary/abeninternal_table_glosry.md).

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md), the addition `AS` can be used to define aliases for columns of the result set in a [`SELECT`](../abap-programming-language/abap-database-access/abapselect_list.md) list or for data sources in the [`FROM`](../abap-programming-language/abap-database-access/abapfrom_clause.md) clause.

- In [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), the addition `AS` can be used to define aliases for elements in the `SELECT` list or for [CDS associations](../abap-glossary/abencds_association_glosry.md).

**analytical formula**

An analytical formula is an element of a [CDS analytical projection view](../abap-glossary/abencds_analytical_pv_glosry.md) that is added as a new element in the projection layer and performs a calculation.

**analytical scalar function**

[CDS scalar function](../abap-glossary/abencds_scalar_function_glosry.md) that is evaluated by an analytical runtime environment. Analytical scalar functions can be used in [analytical projection views](../abap-glossary/abencds_analytical_pv_glosry.md) in operand positions that expect a scalar value.

Analytical scalar functions are [system functions](../abap-glossary/abencds_system_func_glosry.md). They can only be defined and implemented internally by SAP. They are available for internal and external use in [CDS analytical queries](../abap-glossary/abencds_analytic_query_glosry.md).

For a list of analytical scalar functions delivered by SAP, see [ABAP CDS - Analytical Scalar Functions](abap-cds-data-definitions/abencds_ana_scalar_function.md).

**analytical selection**

Also called restricted measure. An analytical selection is an element of a [CDS analytical projection view](../abap-glossary/abencds_analytical_pv_glosry.md) that is newly added in the projection layer. A selection is defined by means of a [selection-related case expression](abap-cds-data-definitions/abencds_case_expression_apv.md).

**annotation array**

[CDS annotation](../abap-glossary/abencds_annotation_glosry.md) defined with the addition `array of` in its [annotation definition](../abap-glossary/abencds_anno_definition_glosry.md). When an annotation array is specified in [annotation syntax](../abap-glossary/abencds_annotation_syntax_glosry.md), any number of similar elements are listed in square brackets [`[ ]`](abap-cds-annotations/abencds_annotations_syntax.md).

**annotation value**

A value specified for a [CDS annotation](../abap-glossary/abencds_annotation_glosry.md) in the [CDS annotation syntax](../abap-glossary/abencds_annotation_syntax_glosry.md). The possible values can be specified in the [CDS annotation definition](../abap-glossary/abencds_anno_definition_glosry.md) using a type specification, enumeration symbols, and a default value.

**arithmetic expression**

Formulation of an arithmetic calculation.

- In general ABAP, an [arithmetic expression](../abap-programming-language/abap-processing-internal-data/abapcompute_arith.md) is a [calculation expression](../abap-glossary/abencalculation_expression_glosry.md). It is assigned a [calculation type](../abap-glossary/abencalculation_type_glosry.md) that is used to execute the calculation. The result of an arithmetic expression is a numeric value that exists in the calculation type. Arithmetic expressions occur in the [read positions of specific statements](../abap-programming-language/abap-operands/abenoperands_expressions.md).

- In ABAP SQL, [arithmetic expressions](../abap-programming-language/abap-database-access/abensql_arith.md) are [SQL expressions](../abap-glossary/abensql_expression_glosry.md).

- In ABAP CDS, [arithmetic expressions](abap-cds-data-definitions/abencds_arithmetic_expression_v2.md) can be used in the `SELECT` list of CDS view entities.

**arithmetic operator**

Combines two numeric [operands](../abap-glossary/abenoperand_glosry.md) in an [arithmetic expression](../abap-glossary/abenarithmetic_expression_glosry.md).

- In ABAP, arithmetic operators are [`+`](../abap-programming-language/abap-processing-internal-data/abenarith_operators.md), [`-`](../abap-programming-language/abap-processing-internal-data/abenarith_operators.md), [`*`](../abap-programming-language/abap-processing-internal-data/abenarith_operators.md), [`/`](../abap-programming-language/abap-processing-internal-data/abenarith_operators.md), [`DIV`](../abap-programming-language/abap-processing-internal-data/abenarith_operators.md), [`MOD`](../abap-programming-language/abap-processing-internal-data/abenarith_operators.md), and [`**`](../abap-programming-language/abap-processing-internal-data/abenarith_operators.md). See the topic [`arith_exp` - Arithmetic Operators](../abap-programming-language/abap-processing-internal-data/abenarith_operators.md) for further details.

- In ABAP SQL, arithmetic operators are [`+`](../abap-programming-language/abap-database-access/abensql_arith.md), [`-`](../abap-programming-language/abap-database-access/abensql_arith.md), [`*`](../abap-programming-language/abap-database-access/abensql_arith.md), [`/`](../abap-programming-language/abap-database-access/abensql_arith.md).

- In ABAP CDS, arithmetic operators are [`+`](abap-cds-data-definitions/abencds_arithmetic_expression_v2.md), [`-`](abap-cds-data-definitions/abencds_arithmetic_expression_v2.md), [`*`](abap-cds-data-definitions/abencds_arithmetic_expression_v2.md), [`/`](abap-cds-data-definitions/abencds_arithmetic_expression_v2.md).

**association source**

Data source that serves as the source of an [association](../abap-glossary/abenassociation_glosry.md).

**association target**

Data source that serves as the target of an [association](../abap-glossary/abenassociation_glosry.md).

**base type**

Technical storage type of [enumerated constants](../abap-glossary/abenenumerated_constant_glosry.md), [enumerated variables](../abap-glossary/abenenumerated_variable_glosry.md), and [CDS enumerated elements](../abap-glossary/abencds_enum_element_glosry.md). In ABAP CDS, the base type of an [enumerated type](../abap-glossary/abenenum_type_glosry.md) is also used for compatibility checks in cast expressions and in comparisons. In ABAP, the base type of an enumerated type can be used in special conversions using [`CONV`](../abap-programming-language/abap-processing-internal-data/abenconv_constructor_enum.md). A base type is [flat](../abap-glossary/abenflat_glosry.md), [elementary](../abap-glossary/abenelementary_data_type_glosry.md), and has a maximum length of 16 bytes.

**binary floating point literal**

A [numeric literal](../abap-glossary/abennumeric_literal_glosry.md) that has the [binary floating point data type](../abap-glossary/abenbinfloat_glosry.md) [`f`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) or [`FLTP`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Not available in general ABAP.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), binary floating point literals are available as [typed literals](../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_literals.md)

- [Literals in CDS](abap-cds-data-definitions/abencds_literal_v2.md).

**built-in function**

A predefined function in ABAP, ABAP SQL, and ABAP CDS.

- In ABAP, built-in functions can be used as [expressions](../abap-glossary/abenexpression_glosry.md) in [certain operand positions](../abap-programming-language/abap-operands/abenoperands_expressions.md). [Numeric functions](../abap-glossary/abenmathematical_funktion_glosry.md), [string functions](../abap-glossary/abenstring_function_glosry.md), [table functions](../abap-glossary/abentable_function_glosry.md), and [byte chain functions](../abap-glossary/abenbyte_chain_function_glosry.md) that have a return value of the corresponding data type can be distinguished. [Description functions](../abap-glossary/abendescription_function_glosry.md) that provide information on data objects, are also available. The names of the built-in functions are a subset of the [reserved names](../abap-glossary/abenabap_word_glosry.md). For further details, see the topic [Built-In Functions](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md).

- For ABAP SQL, [built-in functions](../abap-programming-language/abap-database-access/abensql_builtin_func.md) are part of the [SQL expressions](../abap-glossary/abensql_expression_glosry.md).

- For built-in functions in ABAP CDS, see the topic [CDS built-in function](../abap-glossary/abencds_builtin_func_glosry.md).

[Actual parameters](../abap-glossary/abenactual_parameter_glosry.md) passed to the [formal parameters](../abap-glossary/abenformal_parameter_glosry.md) of built-in functions are called also called [arguments](../abap-glossary/abenargument_glosry.md) of the function.

**byte field literal**

A [literal](../abap-glossary/abenabap_literal_glosry.md) of the [byte field type](../abap-glossary/abenbyte_field_type_glosry.md) [`x`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md) or [`RAW`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the length of the specified bytes. Only [typed](../abap-glossary/abentyped_literal_glosry.md) byte field literals are available.

- Not available in general ABAP.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), byte field literals are available as [typed literals](../abap-glossary/abentyped_literal_glosry.md)

See also:

- [Typed Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](abap-cds-data-definitions/abencds_typed_literal_v2.md)

**byte string literal**

A [literal](../abap-glossary/abenabap_literal_glosry.md) of the [byte string type](../abap-glossary/abenbyte_string_type_glosry.md) [`xstring`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md) or [`RAWSTRING`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Not available in general ABAP.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), byte string literals are available as [typed literals](../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](abap-cds-data-definitions/abencds_typed_literal_v2.md)

**case distinction**

[Control structure](../abap-glossary/abencontrol_structure_glosry.md) with the [control statement](../abap-glossary/abencontrol_statement_glosry.md) [`CASE`](../abap-programming-language/abap-program-flow-logic/abapcase.md) or [`CASE TYPE OF`](../abap-programming-language/abap-program-flow-logic/abapcase_type.md), [condition expression](../abap-glossary/abenconditional_expression_glosry.md) with the [conditional operator](../abap-glossary/abenconditional_operator_glosry.md) [`SWITCH`](../abap-programming-language/abap-program-flow-logic/abenconditional_expression_switch.md), [`CASE`](../abap-programming-language/abap-database-access/abensql_case.md) expression in [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md), or [`CASE`](abap-cds-data-definitions/abencds_case_expression_v2.md) expression in [CDS DDL](../abap-glossary/abencds_ddl_glosry.md). In a case distinction, the value of an [operand](../abap-glossary/abenoperand_glosry.md) determines which of multiple source code sections is executed. In the ABAP language, there are only [simple case distinctions](../abap-glossary/abensimple_case_glosry.md). In ABAP CDS and ABAP SQL, there are [simple case distinctions](../abap-glossary/abensimple_case_glosry.md) and [complex case distinctions](../abap-glossary/abencomplex_case_glosry.md).

**cast**

In ABAP, see [casting](../abap-glossary/abencast_casting_glosry.md). In [SQL](../abap-glossary/abensql_glosry.md), a cast is a type conversion.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md), the operator [`CAST`](../abap-programming-language/abap-database-access/abensql_cast.md) is used.

- In the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) of [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), the operator `CAST` is used (see [cast in CDS view entities](abap-cds-data-definitions/abencds_cast_expression_v2.md) or [cast in CDS DDIC-based views (obsolete)](abap-cds-obsolete-language-elements/abencds_cast_expression_v1.md)).

**CDS**

*-\>* [Core Data Services](../abap-glossary/abencore_data_services_glosry.md)

**CDS abstract entity**

A [CDS transient entity](../abap-glossary/abencds_non_sql_entity_glosry.md) defined using [`DEFINE ABSTRACT ENTITY`](abap-cds-data-definitions/abencds_f1_define_abstract_entity.md) in a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md). A CDS abstract entity defines the type properties of a [CDS entity](../abap-glossary/abencds_entity_glosry.md) without defining a database object.

**CDS abstract entity extension**

[CDS entity extension](../abap-glossary/abencds_entity_extend_glosry.md) of a [CDS abstract entity](../abap-glossary/abencds_abstract_entity_glosry.md). A CDS abstract entity extension can be used to add elements to an abstract entity without making any modifications to the original entity. It is defined using the statement [`EXTEND ABSTRACT ENTITY`](abap-cds-data-definitions/abencds_extend_abstract_entity.md).

**CDS access condition**

Condition in a [CDS role](../abap-glossary/abencds_role_glosry.md) defined in an [access rule](../abap-glossary/abenaccess_rule_glosry.md) of the statement [`DEFINE ROLE`](abap-cds-access-control/abencds_f1_define_role.md) for a [CDS entity](../abap-glossary/abencds_entity_glosry.md). [CDS access control](../abap-glossary/abencds_access_control_glosry.md) evaluates the access conditions of a CDS entity by default when [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) is used to access objects. Access conditions can include for example [PFCG conditions](../abap-glossary/abenpfcg_condition_glosry.md), [literal conditions](../abap-glossary/abenliteral_condition_glosry.md), [user conditions](../abap-glossary/abenuser_condition_glosry.md), and other conditions.

**CDS access control**

Implicit restriction applied to a selection of [CDS entities](../abap-glossary/abencds_entity_glosry.md) when accessing objects with [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) using [access conditions](../abap-glossary/abenaccess_condition_glosry.md) defined in [CDS roles](../abap-glossary/abencds_role_glosry.md). CDS access control is switched on by default for each [CDS view entity](../abap-glossary/abencds_v2_view_glosry.md), [CDS DDIC-based view (obsolete)](../abap-glossary/abencds_v1_view_glosry.md), and [CDS table function](../abap-glossary/abencds_table_function_glosry.md). It can be switched off for individual views and table functions using a view annotation or [table function annotation](abap-cds-data-definitions/abencds_f1_function_annotations.md).

**CDS access policy**

Framework defined in the [DCL](../abap-glossary/abendcl_glosry.md) of the [ABAP Core Data Services](../abap-glossary/abenabap_core_data_services_glosry.md) using [`DEFINE ACCESSPOLICY`](abap-cds-access-control/abencds_f1_define_accesspolicy.md). Currently, only one CDS access policy is used as a frame for the definition of exactly one [PFCG mapping](../abap-glossary/abencds_pfcg_mapping_glosry.md).

**CDS access rule**

An access rule formulates an [access condition](../abap-glossary/abenaccess_condition_glosry.md) for a [CDS entity](../abap-glossary/abencds_entity_glosry.md) or guarantees open access in a [CDS role](../abap-glossary/abencds_role_glosry.md).

**CDS amount field**

A component of a [CDS entity](../abap-glossary/abencds_entity_glosry.md) of data type `CURR`, `DECFLOAT34`, `DEC`, or `FLTP` in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). It is used for entering an amount in a particular currency. The content of an amount field is interpreted as an integer in the smallest unit of the currency. An ABAP CDS amount field must be linked with a [currency key](../abap-glossary/abencurrency_key_glosry.md) of the same CDS entity that specifies the currency and the number of decimal places.

Related terms:

- [currency field](../abap-glossary/abencurrency_field_glosry.md)

- [DDIC currency field](../abap-glossary/abenddic_currency_field_glosry.md)

**CDS analytical cube view**

[CDS view entity](../abap-glossary/abencds_v2_view_glosry.md) or [CDS DDIC-based view (obsolete)](../abap-glossary/abencds_v1_view_glosry.md) annotated with [`@Analytics.dataCategory: #CUBE`](abap-cds-annotations/abencds_annotations_frmwrk_tables.md). Serves as a data source for [CDS analytical projection views](../abap-glossary/abencds_analytical_pv_glosry.md).

**CDS analytical dimension field**

An analytical dimension field is an element of an [analytical cube view](../abap-glossary/abencds_analytical_cube_glosry.md) that describes a characteristic of the view's subject and that can be used for [grouping](abap-cds-data-definitions/abencds_group_by_v2.md) or filtering. For example if a view describes a sales order, the following columns can be dimensions: customer, date, region.

**CDS analytical dimension view**

[CDS view entity](../abap-glossary/abencds_v2_view_glosry.md) or [CDS DDIC-based view (obsolete)](../abap-glossary/abencds_v1_view_glosry.md) annotated with [`@Analytics.dataCategory: #DIMENSION`](abap-cds-annotations/abencds_annotations_frmwrk_tables.md). Can serve as a data source for CDS analytical projection views.

**CDS analytical measure field**

An analytical measure field is a field of an [analytical cube view](../abap-glossary/abencds_analytical_cube_glosry.md) or an [analytical dimension view](../abap-glossary/abencds_anal_dim_view_glosry.md) that contains measurable data. In other words, an analytical measure field can be any field that contains quantifiable data that can be calculated, for example, the total price of all sales order positions.

**CDS analytical projection view**

Synonym for [CDS analytical query](../abap-glossary/abencds_analytic_query_glosry.md). [CDS projection view](../abap-glossary/abencds_projection_view_glosry.md) that is intended for modeling analytical queries within a CDS data model. It is processed by the [ABAP Analytical Engine](../abap-glossary/abenabap_ae_glosry.md) and has to be exposed as an [InA](../abap-glossary/abenina_protocol_glosry.md) service. A CDS analytical projection view is defined using the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) statement [`DEFINE TRANSIENT VIEW ENTITY AS PROJECTION ON`](abap-cds-data-definitions/abencds_define_view_as_analytical.md) and it must have the [provider contract](abap-cds-data-definitions/abencds_pv_provider_contract.md) set to `ANALYTICAL_QUERY`. A CDS analytical projection view is a [CDS transient entity](../abap-glossary/abencds_non_sql_entity_glosry.md).

**CDS analytical query**

[*-\>* CDS analytical projection view](../abap-glossary/abencds_analytical_pv_glosry.md)

**CDS annotation**

A CDS annotation adds metadata to a [CDS object](../abap-glossary/abencds_object_glosry.md) that goes beyond the syntax features of [SQL](../abap-glossary/abensql_glosry.md). An annotation is specified using the [annotation syntax](../abap-glossary/abencds_annotation_syntax_glosry.md) in the [CDS source code](../abap-glossary/abencds_source_code_glosry.md) of the CDS object. CDS annotations and their syntax are defined using [CDS annotation definitions](../abap-glossary/abencds_anno_definition_glosry.md). SAP delivers a predefined set of [SAP annotations](../abap-glossary/abensap_annotation_glosry.md).

**CDS annotation definition**

Defines a [CDS annotation](../abap-glossary/abencds_annotation_glosry.md) as a [CDS object](../abap-glossary/abencds_object_glosry.md) using the statement `DEFINE ANNOTATION` in [`DDLA` source code](../abap-glossary/abenddla_source_code_glosry.md) in [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). A CDS annotation definition specifies the [CDS annotation syntax](../abap-glossary/abencds_annotation_syntax_glosry.md) that is to be used when the annotation is specified in [CDS source code](../abap-glossary/abencds_source_code_glosry.md).

**CDS annotation syntax**

Syntax for specifying a [CDS annotation](../abap-glossary/abencds_annotation_glosry.md) in [CDS source code](../abap-glossary/abencds_source_code_glosry.md). The CDS annotation syntax is fixed and the [CDS annotation definition](../abap-glossary/abencds_anno_definition_glosry.md) specifies further rules for the use of the respective annotation.

**CDS aspect**

CDS object available in ABAP CDS. The following types of CDS aspects are available:

- [CDS DDL aspect](abap-cds-data-definitions/abencds_ddl_aspect_glosry.md)

- [CDS DCL aspect](../abap-glossary/abencds_dcl_aspect_glosry.md)

**CDS association**

An [association](../abap-glossary/abenassociation_glosry.md) of [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). Associations define [join](../abap-glossary/abenjoin_glosry.md) relationships between [association sources](../abap-glossary/abenassociation_source_glosry.md) and [association targets](../abap-glossary/abenassociation_target_glosry.md). CDS associations can be defined for [CDS view entities](../abap-glossary/abencds_v2_view_glosry.md), [CDS DDIC-based views (obsolete)](../abap-glossary/abencds_v1_view_glosry.md), [CDS projection views](../abap-glossary/abencds_projection_view_glosry.md), [CDS custom entities](../abap-glossary/abencds_custom_entity_glosry.md), and [CDS abstract entities](../abap-glossary/abencds_abstract_entity_glosry.md) using the addition `ASSOCIATION` in the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). They can be evaluated in [CDS DDL](../abap-glossary/abencds_ddl_glosry.md), [CDS DCL](../abap-glossary/abencds_dcl_glosry.md), and in [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) using [SQL path expressions](../abap-glossary/abensql_path_expression_glosry.md). [To-child associations](../abap-glossary/abento_child_association_glosry.md) and [to-parent associations](../abap-glossary/abento_parent_association_glosry.md) are specialized associations that together build a [CDS composition](../abap-glossary/abencds_composition_glosry.md) relationship for the [CDS composition tree](../abap-glossary/abencds_composition_tree_glosry.md) of a [RAP business object](../abap-glossary/abenrap_bo_glosry.md).

**CDS association path**

A sequence of [CDS associations](../abap-glossary/abencds_association_glosry.md). CDS association paths can be specified in the form of [SQL path expressions](../abap-glossary/abensql_path_expression_glosry.md) in [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md).

**CDS buffer propagation**

Buffer propagation means that the joins defined by a [CDS association](../abap-glossary/abencds_association_glosry.md) are processed by the [ABAP SQL in-memory engine](../abap-glossary/abenabap_sql_inmemeng_glosry.md) on data stored in the [table buffer](../abap-glossary/abentable_buffer_glosry.md). Instead of using joins instantiated on the [SAP HANA database](../abap-glossary/abenhana_database_glosry.md), temporary joins for processing the table buffer are established on the [AS ABAP](../abap-glossary/abenas_abap_glosry.md). This can lead to performance gains.

**CDS built-in function**

A predefined function in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) that can be used in operand positions of [CDS entities](../abap-glossary/abencds_entity_glosry.md). ABAP CDS offers [numeric functions](abap-cds-data-definitions/abencds_sql_functions_numeric_v2.md), [string functions](abap-cds-data-definitions/abencds_sql_functions_character_v2.md), and [date and time functions](abap-cds-data-definitions/abencds_date_time_functions_v2.md) that have a return value of the corresponding data type. [Conversion functions](abap-cds-data-definitions/abencds_conversion_functions_v2.md) are available to perform conversions between data types.

**CDS built-in type**

[Built-in](../abap-glossary/abenbuiltin_data_type_glosry.md) [elementary](../abap-glossary/abenelementary_data_type_glosry.md) [CDS type](../abap-glossary/abencds_type_glosry.md). CDS built-in types are based on the [built-in Dictionary types](../abap-glossary/abenbuiltin_ddic_type_glosry.md) and the same rules apply as to the corresponding built-in ABAP Dictionary types. CDS built-in types can be used for the typing of [CDS elements](../abap-glossary/abencds_element_glosry.md), [CDS parameters](../abap-glossary/abencds_parameter_glosry.md), and [CDS simple types](../abap-glossary/abencds_simple_type_glosry.md), and for casting in ABAP CDS.

**CDS calculated quantity**

A component of a [CDS view entity](../abap-glossary/abencds_v2_view_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). A calculated quantity is always the result of a calculation using [CDS amount](../abap-glossary/abencds_amount_field_glosry.md) and / or [CDS quantity fields](../abap-glossary/abencds_quantity_glosry.md). The DDIC data type is `DECFLOAT34`. An ABAP CDS calculated quantity must be linked with a [CDS calculated unit](../abap-glossary/abencds_calculated_unit_glosry.md) of the same CDS view entity that specifies a user-defined unit for the calculated quantity.

**CDS calculated unit**

A component of a [CDS view entity](../abap-glossary/abencds_v2_view_glosry.md) of data type `CHAR` that specifies a user-defined unit which is not contained in any list of predefined values. A CDS calculated unit can be linked with a [CDS calculated quantity](abap-cds-data-types/abencds_calculated_quantity.md) of the same CDS view entity.

**CDS child entity**

Any [CDS entity](../abap-glossary/abencds_entity_glosry.md) of a [CDS composition tree](../abap-glossary/abencds_composition_tree_glosry.md) other than the [root entity](../abap-glossary/abenroot_entity_glosry.md). A child entity is defined as the [composition target](../abap-glossary/abencomposition_target_glosry.md) of a [to-child association](../abap-glossary/abento_child_association_glosry.md) in its [parent entity](../abap-glossary/abenparent_entity_glosry.md) and has a [to-parent association](../abap-glossary/abento_parent_association_glosry.md) to its parent entity. A child entity has exactly one parent entity.

**CDS composition**

A CDS composition consists of a [to-parent association](../abap-glossary/abento_parent_association_glosry.md) and a [to-child association](../abap-glossary/abento_child_association_glosry.md). A CDS composition defines an existential dependency between two entities, where the [child entity](../abap-glossary/abenchild_entity_glosry.md) cannot exist without the [parent entity](../abap-glossary/abenparent_entity_glosry.md).

**CDS composition path**

A sequence of [CDS compositions](../abap-glossary/abencds_composition_glosry.md) that link the [CDS entities](../abap-glossary/abencds_entity_glosry.md) of a [CDS composition tree](../abap-glossary/abencds_composition_tree_glosry.md). CDS composition paths can be specified like [CDS association paths](../abap-glossary/abencds_association_path_glosry.md) in [SQL path expressions](../abap-glossary/abensql_path_expression_glosry.md).

**CDS composition tree**

A [tree hierarchy](../abap-glossary/abentree_hierarchy_glosry.md) of a [RAP business object](../abap-glossary/abenrap_bo_glosry.md) that consists of [parent entities](../abap-glossary/abenparent_entity_glosry.md) and [child entities](../abap-glossary/abenparent_entity_glosry.md) that are themselves defined using [CDS compositions](../abap-glossary/abencds_composition_glosry.md). The top parent entity of a CDS composition tree is the [root entity](../abap-glossary/abenroot_entity_glosry.md) which represents the business object.

**CDS condition**

Logical expression in a CDS operand position.

**CDS custom entity**

A [CDS transient entity](../abap-glossary/abencds_non_sql_entity_glosry.md) defined using [`DEFINE CUSTOM ENTITY`](abap-cds-data-definitions/abencds_f1_define_custom_entity.md) in a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md). A CDS custom entity allows developers to implement their own data retrieval using the [ABAP language](../abap-glossary/abenabala_glosry.md). The data retrieval is implemented by a method of an [ABAP class](../abap-programming-language/abap-declarations/abapclass.md) that is called when accessing the custom entity in a framework such as the [RAP query engine](../abap-glossary/abenrap_query_engine_glosry.md). Custom entities cannot be used in [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md). In [RAP](../abap-glossary/abenrap_glosry.md), custom entities are used as the data model basis for [unmanaged queries](../abap-glossary/abenrap_unmanged_query_glosry.md).

**CDS custom entity extension**

[CDS entity extension](../abap-glossary/abencds_entity_extend_glosry.md) of a [CDS custom entity](../abap-glossary/abencds_custom_entity_glosry.md). A CDS custom entity extension can be used to add elements to a custom entity without making any modifications to the original entity. It is defined using the statement [`EXTEND CUSTOM ENTITY`](abap-cds-data-definitions/abencds_extend_custom_entity.md).

**CDS data definition**

A definition or extension of a [CDS entity](../abap-glossary/abencds_entity_glosry.md) using [language elements](abap-cds-data-definitions/abencds_f1_ddl_syntax.md) of the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) in [DDL source code](../abap-glossary/abenddl_source_code_glosry.md). A CDS data definition might also contain [DQL](../abap-glossary/abendql_glosry.md) parts that define the data retrieval. For example, the DQL statement `SELECT` is embedded in [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) for [CDS views](../abap-glossary/abencds_view_glosry.md).

**CDS DCL**

Data control language ([DCL](../abap-glossary/abendcl_glosry.md)) of [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) used to define [CDS roles](../abap-glossary/abencds_role_glosry.md) and [CDS access policies](../abap-glossary/abencds_access_policy_glosry.md) in [DCL source code](../abap-glossary/abendcl_source_code_glosry.md) in [CDS access control](../abap-glossary/abencds_access_control_glosry.md).

**CDS DCL aspect**

Object used for the definition of user-specific values and their use in the conditions of a [CDS role](../abap-glossary/abencds_role_glosry.md). Currently, the predefined aspects `pfcg_auth` and `user` are available, plus the user-defined aspects defined with [`DEFINE ASPECT`](abap-cds-access-control/abencds_f1_define_generic_aspect.md).

**CDS DDIC-based entity (obsolete)**

A [CDS persistent entity](../abap-glossary/abencds_sql_entity_glosry.md) for which a [CDS-managed DDIC view (obsolete)](../abap-glossary/abencds_mngdddic_view_glosry.md) is created in the ABAP Dictionary alongside the CDS entity upon activation.

There is only one kind of DDIC-based entity available, namely [CDS DDIC-based views](../abap-glossary/abencds_v1_view_glosry.md).

**CDS DDIC-based view**

An obsolete type of [CDS view](../abap-glossary/abencds_view_glosry.md) that is technically based on a [CDS-managed DDIC view (obsolete)](../abap-glossary/abencds_mngdddic_view_glosry.md) in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md). A CDS DDIC-based view (obsolete) is defined with the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) statement [`DEFINE VIEW ddic_based_view`](abap-cds-obsolete-language-elements/abencds_define_view_v1.md).

**CDS DDIC-based view extension**

A [CDS entity extension](../abap-glossary/abencds_entity_extend_glosry.md) of a [CDS DDIC-based view](../abap-glossary/abencds_v1_view_glosry.md). A CDS DDIC-based view extension can be used to add elements and/or clauses to a view without making any modifications to the original view. It is defined using the statement [`EXTEND VIEW`](abap-cds-data-definitions/abencds_extend_view.md).

**CDS DDL**

The data definition language of [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). Besides CDS DDL for [CDS data definitions](../abap-glossary/abencds_data_definition_glosry.md), there two further dialects, namely [CDS DDLA](../abap-glossary/abencds_ddla_glosry.md) and [CDS DDLX](../abap-glossary/abencds_ddlx_glosry.md).

**CDS DDL aspect**

A [CDS object](../abap-glossary/abencds_object_glosry.md) defined in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) that defines reusable components for [CDS entities](../abap-glossary/abencds_entity_glosry.md). A [CDS aspect](abap-cds-data-definitions/abencds_aspects.md) is defined using the syntax [`DEFINE ASPECT`](abap-cds-data-definitions/abencds_define_aspect.md). An aspect can be included in one or more [CDS data definitions](../abap-glossary/abencds_data_definition_glosry.md) by a [CDS aspect binding](../abap-glossary/abencds_ddl_aspect_binding_glosry.md).

**CDS DDL aspect binding**

An optional component of a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md), specified in front of the [`SELECT`](abap-cds-data-definitions/abencds_select_statement_v2.md) list. With a CDS aspect binding, a [CDS aspect](../abap-glossary/abencds_aspect_glosry.md) is bound to a CDS data definition using the syntax [`BIND ASPECT`](abap-cds-data-definitions/abencds_bind_aspect.md). This makes the elements of the aspect available for use in an operand position of the data definition, using the syntax [`INCLUDE`](abap-cds-data-definitions/abencds_include_aspect.md).

**CDS DDL expression**

Expression in a CDS DDL operand position that is passed to the database system for evaluation.

**CDS DDLA**

A [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) dialect that contains language elements for [CDS annotation definitions](../abap-glossary/abencds_anno_definition_glosry.md) in [DDLA source code](../abap-glossary/abenddla_source_code_glosry.md).

**CDS DDLX**

A [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) dialect that contains language elements for [CDS metadata extensions](../abap-glossary/abencds_metadata_extension_glosry.md) in [DDLX source code](../abap-glossary/abenddlx_source_code_glosry.md).

**CDS delegated buffer**

A [CDS view entity buffer](../abap-glossary/abencds_entity_buffer_glosry.md) that delegates the buffer usage from one CDS entity to its base entity, which avoids numerous entries of the same data in the memory of the [AS ABAP](../abap-glossary/abenabap_glossary.md). This can improve performance.

Defined using the syntax [`TYPE DELEGATED`](abap-cds-tuning-objects/abencds_define_delegated_buffer.md) in the definition of a CDS entity buffer.

**CDS element**

An element in a [CDS entity](../abap-glossary/abencds_entity_glosry.md). A CDS element is defined in an element list of a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md) and is a [structure component](../abap-glossary/abenstructure_component_glosry.md) of the [structured type](../abap-glossary/abenstructured_type_glosry.md) defined by the CDS entity. CDS elements can be, for example, [CDS source fields](../abap-glossary/abencds_field_glosry.md), [CDS literals](../abap-glossary/abencds_literal_glosry.md), or [CDS DDL expressions](../abap-glossary/abencds_expression_glosry.md).

**CDS entity**

[CDS object](../abap-glossary/abencds_object_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). A CDS entity is defined in a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md) using the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) of ABAP CDS in [DDL source code](../abap-glossary/abenddl_source_code_glosry.md). A CDS entity is defined when it is activated. Within CDS, a CDS entity can access other entities. Currently, there are the following CDS entities available:

- [CDS table entities](../abap-glossary/abencds_table_entity_glosry.md)

- [CDS view entities](../abap-glossary/abencds_v2_view_glosry.md)

- [CDS projection views](../abap-glossary/abencds_projection_view_glosry.md)

- [CDS table functions](../abap-glossary/abencds_table_function_glosry.md)

- [CDS external entities](../abap-glossary/abencds_external_entity_glosry.md)

- [CDS hierarchies](../abap-glossary/abencds_hierarchy_glosry.md)

- [CDS custom entities](../abap-glossary/abencds_custom_entity_glosry.md)

- [CDS abstract entities](../abap-glossary/abencds_abstract_entity_glosry.md)

- [CDS DDIC-based entities](../abap-glossary/abencds_ddic_based_entity_glosry.md).

In [ABAP programs](../abap-glossary/abenabap_program_glosry.md), a CDS entity can be used as a [global type](../abap-glossary/abenglobal_type_glosry.md) and [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) read statements can be used to access CDS entities.

CDS entities that are [writable database objects](../abap-glossary/abenwritable_db_obj_glosry.md) can be used in ABAP SQL read access for inserting, modifying, or deleting data on the database.

**CDS entity buffer**

An [ABAP tuning object](../abap-glossary/abenabap_tuning_object_glosry.md) that defines [table buffering](../abap-glossary/abentable_buffering_glosry.md) settings for [CDS entities](../abap-glossary/abencds_entity_glosry.md). The following types of CDS entity buffers are available:

- [CDS view entity buffer](../abap-glossary/abencds_view_entity_b_glosry.md)

- [CDS table entity buffer](../abap-glossary/abencds_table_entity_b_glosry.md)

- [CDS propagated buffer](../abap-glossary/abencds_prop_buffer_glosry.md)

Sometimes, *CDS entity buffer* is also used as a synonym for the area of the [table buffer](../abap-glossary/abentable_buffer_glosry.md) in the [shared memory](../abap-glossary/abenshared_memory_glosry.md) where data from CDS entities is buffered.

**CDS entity extension**

A transportable extension of a [CDS entity](../abap-glossary/abencds_entity_glosry.md). A CDS entity extension can be used to add elements and/or clauses to a CDS entity without making any modifications to the original entity.

There are currently four different statements that can be used to extend a CDS entity in [CDS DDL](../abap-glossary/abencds_ddl_glosry.md):

- [`EXTEND VIEW ENTITY`](abap-cds-data-definitions/abencds_extend_view_entity.md): [CDS view entity extension](../abap-glossary/abencds_view_entity_extend_glosry.md) for a [CDS view entity](../abap-glossary/abencds_v2_view_glosry.md) or a [CDS projection view](../abap-glossary/abencds_projection_view_glosry.md).

- [`EXTEND CUSTOM ENTITY`](abap-cds-data-definitions/abencds_extend_custom_entity.md) [CDS custom entity extension](../abap-glossary/abencds_cus_entity_extend_glosry.md) for a [CDS custom entity](../abap-glossary/abencds_custom_entity_glosry.md).

- [`EXTEND ABSTRACT ENTITY`](abap-cds-data-definitions/abencds_extend_abstract_entity.md) [CDS abstract entity extension](../abap-glossary/abencds_abs_entity_extend_glosry.md) for a [CDS abstract entity](../abap-glossary/abencds_abstract_entity_glosry.md).

- [`EXTEND VIEW`](abap-cds-data-definitions/abencds_extend_view.md) [CDS DDIC-based view extension](../abap-glossary/abencds_view_extend_glosry.md) for a [CDS DDIC-based view (obsolete)](../abap-glossary/abencds_v1_view_glosry.md).

**CDS enumerated element**

[CDS element](../abap-glossary/abencds_element_glosry.md) that is typed with a [CDS enumerated type](../abap-glossary/abencds_enum_type_glosry.md). A CDS enumerated element can only contain one of the [enumerated values](../abap-glossary/abenenumerated_value_glosry.md) of the respective enumerated type.

**CDS enumerated type**

[CDS user-defined type](../abap-glossary/abencds_user_defined_type_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) that defines an [enumerated type](../abap-glossary/abenenum_type_glosry.md). A CDS enumerated type is defined using the statement [`DEFINE TYPE ENUM`](abap-cds-data-definitions/abencds_define_enum_type.md).

**CDS external entity**

A [CDS persistent entity](../abap-glossary/abencds_sql_entity_glosry.md) defined using [`DEFINE EXTERNAL ENTITY`](abap-cds-data-definitions/abencds_define_external_entity.md) in a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md). A CDS external entity can be used to access data from external database systems within the [AS ABAP](../abap-glossary/abenas_abap_glosry.md). The external systems can be other [SAP HANA](../abap-glossary/abenhana_database_glosry.md) or non-SAP HANA database systems. The properties of the connection between an external entity and the external system are configured using a [logical external schema](../abap-glossary/abencds_logical_schema_glosry.md). The connection is managed using [SAP HANA Smart Data Access](../abap-glossary/abensap_hana_sda_glosry.md). The following types of external entities are available:

- [dynamic external entities](../abap-glossary/abencds_dynamic_ee_glosry.md)

- [static external entities](../abap-glossary/abencds_static_ee_glosry.md)

- [writable external entities](../abap-glossary/abenwritable_ee_glosry.md)

**CDS function**

Function in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) that can be used in operand positions of [CDS entities](../abap-glossary/abencds_entity_glosry.md). A CDS function can be a [user-defined function](../abap-glossary/abencds_user_func_glosry.md), a [built-in function](../abap-glossary/abencds_builtin_func_glosry.md), or a [system function](../abap-glossary/abencds_system_func_glosry.md).

**CDS function definition**

A [CDS object](../abap-glossary/abencds_object_glosry.md) that defines a [CDS function](../abap-glossary/abencds_function_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). Currently, [CDS scalar function definitions](../abap-glossary/abencds_dsfd_glosry.md) are the only type of CDS function definition available.

**CDS generic type**

[Built-in](../abap-glossary/abenbuiltin_data_type_glosry.md) [generic](../abap-glossary/abengeneric_data_type_glosry.md) [CDS type](../abap-glossary/abencds_type_glosry.md). The generic CDS types are: `any` and `numeric`. Generic CDS types can be used for the typing of parameters of [CDS scalar functions](../abap-glossary/abencds_scalar_function_glosry.md).

**CDS hierarchy**

A [CDS persistent entity](../abap-glossary/abencds_sql_entity_glosry.md) defined using [`DEFINE HIERARCHY`](abap-cds-data-definitions/abencds_f1_define_hierarchy.md) in a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md). A CDS hierarchy allows the retrieval of the nodes of hierarchical data. In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) read statements, a CDS hierarchy can be accessed as a [ABAP SQL hierarchy](../abap-glossary/abensql_hierarchy_glosry.md). Additional [hierarchy columns](../abap-glossary/abenhierarchy_column_glosry.md) containing the [hierarchy attributes](../abap-glossary/abenhierarchy_attribute_glosry.md) are available.

**CDS literal**

An elementary [CDS operand](../abap-glossary/abencds_operand_glosry.md) defined by the textual specification of a value in a [CDS object](../abap-glossary/abencds_object_glosry.md). ABAP CDS provides [typed literals](../abap-glossary/abentyped_literal_glosry.md) and [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

**CDS literal condition**

Part of an [access condition](../abap-glossary/abenaccess_condition_glosry.md) in a [CDS role](../abap-glossary/abencds_role_glosry.md) that associates an element of a [CDS entity](../abap-glossary/abencds_entity_glosry.md) with a literal value.

**CDS localized field**

A [SQL path target field](../abap-glossary/abensql_target_field_glosry.md) in a [CDS entity](../abap-glossary/abencds_entity_glosry.md) whose original data source is a [CDS text provider view](../abap-glossary/abencds_text_provider_glosry.md) and that is automatically displayed in the user's logon language. Defined using the keyword [`LOCALIZED`](abap-cds-data-definitions/abencds_localized.md). Currently available in [CDS projection views](../abap-glossary/abencds_projection_view_glosry.md) only.

**CDS logical external schema**

A logical database schema that maps one or more [CDS external entities](../abap-glossary/abencds_external_entity_glosry.md) to a concrete physical external system or database, and a specific [database schema](../abap-glossary/abendatabase_schema_glosry.md) in such a remote system. A logical external schema is represented by a transportable [repository object](../abap-glossary/abenrepository_object_glosry.md) whose configuration specifies the connection details required by the [SAP HANA remote source](../abap-glossary/abensap_hana_remote_source_glosry.md) to connect to an external system.

**CDS metadata extension**

Short MDE. A [CDS object](../abap-glossary/abencds_object_glosry.md) of the [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) is defined in [`DDLX` source code](../abap-glossary/abenddlx_source_code_glosry.md) with [language elements](abap-cds-annotations/abencds_f1_ddlx_syntax.md) of the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md). In a CDS metadata extension, [CDS annotations](../abap-glossary/abencds_annotation_glosry.md) are specified for a [CDS entity](../abap-glossary/abencds_entity_glosry.md) outside its [data definition](../abap-glossary/abencds_data_definition_glosry.md). A CDS metadata extension is always assigned to a layer such as industry, partner or customer.

**CDS object**

A [repository object](../abap-glossary/abenrepository_object_glosry.md) of [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). CDS objects are, for example, [CDS entities](../abap-glossary/abencds_entity_glosry.md), [CDS annotation definitions](../abap-glossary/abencds_anno_definition_glosry.md), [CDS metadata extensions](../abap-glossary/abencds_metadata_extension_glosry.md), [CDS roles](../abap-glossary/abencds_role_glosry.md), [CDS user-defined types](../abap-glossary/abencds_user_defined_type_glosry.md), [CDS functions](../abap-glossary/abencds_function_glosry.md), and [ABAP tuning objects](../abap-glossary/abenabap_tuning_object_glosry.md).

**CDS operand**

A syntax element of a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md) at an operand position. Defined directly or as a [formal parameter](../abap-glossary/abenformal_parameter_glosry.md), [built-in function](../abap-glossary/abenbuiltin_function_glosry.md), or [expression](../abap-glossary/abenexpression_glosry.md). Operands can be combined with [operators](../abap-glossary/abenoperator_glosry.md) to form [expressions](../abap-glossary/abenexpression_glosry.md) that in turn can be listed at certain [operand positions](../abap-glossary/abenoperand_position_glosry.md).

**More about:**

- [CDS Operands in CDS View Entities](abap-cds-data-definitions/abencds_operands_and_expr_v2.md)

- [CDS Operands in CDS DDIC-based Views](abap-cds-obsolete-language-elements/abencds_operands_and_expr_v1.md)

**CDS parameter**

An input parameter of a [CDS object](../abap-glossary/abencds_object_glosry.md). A CDS parameter can be defined, for example, in the parameter list of a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md) or of a [CDS scalar function definition](../abap-glossary/abencds_dsfd_glosry.md). When a CDS object with parameters is used in another CDS object or in an [ABAP SQL statement](../abap-glossary/abenabap_sql_glosry.md), actual parameters must be assigned to their CDS parameters.

**CDS parent entity**

A [CDS entity](../abap-glossary/abencds_entity_glosry.md) of a [CDS composition tree](../abap-glossary/abencds_composition_tree_glosry.md) that uses a [to-child association](../abap-glossary/abento_child_association_glosry.md) to define a [child entity](../abap-glossary/abenchild_entity_glosry.md). A parent entity can have multiple child entities. Each child entity must define and expose a [to-parent association](../abap-glossary/abento_parent_association_glosry.md) to its parent entity.

**CDS persistent entity**

A [CDS entity](../abap-glossary/abencds_entity_glosry.md) for which an artifact is created on the database and which can be used as a data source in [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md), such as a [CDS view entity](../abap-glossary/abencds_v2_view_glosry.md) or a [CDS table function](../abap-glossary/abencds_table_function_glosry.md).

See also: [CDS transient entity](../abap-glossary/abencds_non_sql_entity_glosry.md)

**CDS PFCG condition**

Part of an [access condition](../abap-glossary/abenaccess_condition_glosry.md) in a [CDS role](../abap-glossary/abencds_role_glosry.md) that uses an [authorization object](../abap-glossary/abenauthorization_object_glosry.md) to associate an element of a [CDS entity](../abap-glossary/abencds_entity_glosry.md) with the [authorizations](../abap-glossary/abenauthorization_glosry.md) of the current [ABAP user](../abap-glossary/abenabap_user_glosry.md).

**CDS PFCG mapping**

A PFCG mapping associates [CDS elements](../abap-glossary/abencds_element_glosry.md) with [authorization fields](../abap-glossary/abenauthorization_field_glosry.md). It is defined using [`DEFINE PFCG_MAPPING`](abap-cds-access-control/abencds_f1_define_pfcg_mapping.md) as part of a [CDS access policy](../abap-glossary/abencds_access_policy_glosry.md) and can be used in [PFCG conditions](../abap-glossary/abenpfcg_condition_glosry.md).

**CDS prebound parameter**

In [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), a prebound parameter overwrites a parameter binding in a CDS association. Overwriting parameter bindings is usually forbidden, but it can be allowed to be defined using the keyword `default` in the CDS association definition. This definition can both be the initial definition within an entity or the exposure of an association in the projection list.

Prebound parameters are relevant in cases where the parameter binding can already be specified when the association is defined. As a result, the prebound parameter does not need to be specified every time when the association is used to read elements.

**CDS projected entity**

Used in the context of [CDS projection views](../abap-glossary/abencds_projection_view_glosry.md). The [CDS view entity](../abap-glossary/abencds_v2_view_glosry.md) that is used as the basis of a CDS projection view, and that is defined after the addition `AS PROJECTION ON` is called projected entity.

**CDS projection view**

A special [CDS view entity](../abap-glossary/abencds_v2_view_glosry.md) that is based on another [CDS view entity](../abap-glossary/abencds_v2_view_glosry.md) (called [projected entity](../abap-glossary/abencds_pv_projected_entity_glosry.md)). CDS projection views adapt a CDS data model for service-specific use cases. A CDS projection view is defined with the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) statement `DEFINE [TRANSIENT] VIEW ENTITY AS PROJECTION`.

The following types of CDS projection views are available:

- [CDS transactional queries](../abap-glossary/abencds_transactional_pv_glosry.md)

- [CDS transactional interfaces](../abap-glossary/abencds_trans_interface_glosry.md)

- [CDS analytical projection views](../abap-glossary/abencds_analytical_pv_glosry.md)

**CDS propagated buffer (obsolete)**

A [CDS entity buffer](../abap-glossary/abencds_entity_buffer_glosry.md) that defines [SQL path target fields](../abap-glossary/abensql_target_field_glosry.md) for [buffer propagation](../abap-glossary/abencds_buffer_propagation_glosry.md). Defined using the syntax [`PROPAGATE VIEW ENTITY BUFFER`](abap-cds-obsolete-language-elements/abencds_propagate_buffer.md).

**CDS provider contract**

In [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), a provider contract specifies the scenario in which a [CDS object](../abap-glossary/abencds_object_glosry.md) is used. Depending on the scenario, different rules apply to the definition of the object in question. Each provider contract imposes a different set of syntax checks.

Currently, the following CDS objects can have a provider contract:

- [CDS projection views](../abap-glossary/abencds_projection_view_glosry.md), see the topic [`PROVIDER CONTRACT`](abap-cds-data-definitions/abencds_pv_provider_contract.md) for more details.

- [CDS service definition](../abap-glossary/abencds_service_definition_glosry.md), see the topic [`PROVIDER CONTRACTS`](abap-cds-service-definitions/abensrvd_provider_contract.md) for more details.

**CDS quantity field**

A component of a [CDS entity](../abap-glossary/abencds_entity_glosry.md) of data type `QUAN`, `DECFLOAT16`, `DECFLOAT34`, `DEC`, `FLTP`, `INT1`, `INT2`, or `INT4` in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). It is used for entering a quantity in a particular unit. An ABAP CDS quantity field must be linked with a [unit key](../abap-glossary/abenunit_glosry.md) of the same CDS entity that specifies the unit of measurement and the number of decimal places.

Related terms:

- [quantity field](../abap-glossary/abenquantity_glosry.md)

- [DDIC quantity field](../abap-glossary/abenddic_quantity_glosry.md)

**CDS role**

A [CDS object](../abap-glossary/abencds_object_glosry.md) defined using the statement [`DEFINE ROLE`](abap-cds-access-control/abencds_f1_define_role.md) in a [DCL source code](../abap-glossary/abendcl_source_code_glosry.md) in the [CDS DCL](../abap-glossary/abencds_dcl_glosry.md) of [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). This object applies [CDS access control](../abap-glossary/abencds_access_control_glosry.md) based on [access conditions](../abap-glossary/abenaccess_condition_glosry.md) when [CDS persistent entities](../abap-glossary/abencds_sql_entity_glosry.md) are accessed using [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md). The access conditions of a CDS role evaluate the classic [authorizations](../abap-glossary/abenauthorization_glosry.md) of the current user.

**CDS root entity**

The top [CDS entity](../abap-glossary/abencds_entity_glosry.md) of a [CDS composition tree](../abap-glossary/abencds_composition_tree_glosry.md). The addition `ROOT` must be specified in the definition of a root entity with [CDS DDL](../abap-glossary/abencds_ddl_glosry.md). A root entity can be part of exactly one [RAP BO](../abap-glossary/abenrap_bo_glosry.md). A CDS root entity is typically a [CDS parent entity](../abap-glossary/abenparent_entity_glosry.md) and it is typically used as a [RAP BO root entity](../abap-glossary/abenrap_bo_root_entity_glosry.md) in the context of the [ABAP RESTful Application Programming Model](../abap-glossary/abenarap_glosry.md).

**CDS scalar function**

[CDS function](../abap-glossary/abencds_function_glosry.md) that operates on a single input data set and returns a scalar (that means [elementary](../abap-glossary/abenelementary_data_type_glosry.md)) return value as result. A CDS scalar function is defined using [`DEFINE SCALAR FUNCTION`](abap-cds-data-definitions/abencds_define_scalar_function.md) in a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md). CDS scalar functions can be [user-defined functions](../abap-glossary/abencds_user_func_glosry.md) or [system functions](../abap-glossary/abencds_system_func_glosry.md).

There are [analytical scalar functions](../abap-glossary/abencds_ana_scalar_glosry.md) and [SQL-based scalar functions](../abap-glossary/abencds_sql_scalar_glosry.md).

A scalar function can have one or more [scalar function implementation references](abap-cds-data-definitions/abencds_scalar_func_impl_ref.md) that bind it to implementations in different environments, such as an SQL environment or the [ABAP Analytical Engine](../abap-glossary/abenabap_ae_glosry.md).

**CDS scalar function definition**

[CDS object](../abap-glossary/abencds_object_glosry.md) that defines a [CDS scalar function](../abap-glossary/abencds_scalar_function_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). A CDS scalar function definition is defined using the statement [`DEFINE SCALAR FUNCTION`](abap-cds-data-definitions/abencds_define_scalar_function.md).

**CDS scalar function implementation reference**

[Repository object](../abap-glossary/abenrepository_object_glosry.md) that binds a [CDS scalar function](../abap-glossary/abencds_scalar_function_glosry.md) to a runtime environment. In case of an [SQL-based scalar function](../abap-glossary/abencds_sql_scalar_glosry.md), the scalar function implementation reference also specifies the [AMDP function implementation](../abap-glossary/abenamdp_function_method_glosry.md) that implements the scalar function in question.

**CDS schema notation**

CSN for short. Notation for compact representations of data models, such as data models defined with [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). SAP standard format for metadata exchange between data models of different technology stacks, for example between [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) and SAP Analytics Cloud (SAC).

**CDS SDL**

The Service Definition Language of [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). CDS SDL contains language elements for [CDS service definitions](../abap-glossary/abencds_service_definition_glosry.md) in [`SDL` source code](../abap-glossary/abensdl_source_code_glosry.md).

**CDS service definition**

A CDS service definition is a [CDS object](../abap-glossary/abencds_object_glosry.md) that exposes [CDS entities](../abap-glossary/abencds_object_glosry.md) for a [business service](../abap-glossary/abenbs_glosry.md). A CDS service definition is defined by the [CDS SDL](../abap-glossary/abencds_sdl_glosry.md) language elements of [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) in [`SDL` source code](../abap-glossary/abensdl_source_code_glosry.md).

**CDS service definition extension**

A transportable extension of a [CDS service definition](../abap-glossary/abencds_service_definition_glosry.md) using the [CDS SDL](../abap-glossary/abencds_sdl_glosry.md) statement [`EXTEND SERVICE`](abap-cds-service-definitions/abensrvd_extend_service.md). A CDS service definition extension can add further entities to an existing CDS service definition without modifying the original service definition.

**CDS simple type**

[CDS user-defined type](../abap-glossary/abencds_user_defined_type_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) that defines an [elementary data type](../abap-glossary/abenelementary_data_type_glosry.md). A CDS simple type is defined using the statement [`DEFINE TYPE`](abap-cds-data-definitions/abencds_define_simple_type.md).

**CDS source code**

The [source code](../abap-glossary/abensource_code_glosry.md) for the definition of a [CDS object](../abap-glossary/abencds_object_glosry.md). There are different kinds of CDS source code, such as

- [DDL source code](../abap-glossary/abenddl_source_code_glosry.md) for [CDS data definitions](../abap-glossary/abencds_data_definition_glosry.md)

- [DDLA source code](../abap-glossary/abenddla_source_code_glosry.md) for [CDS annotation definitions](../abap-glossary/abencds_anno_definition_glosry.md)

- [DDLX source code](../abap-glossary/abenddlx_source_code_glosry.md) for [CDS metadata extensions](../abap-glossary/abencds_metadata_extension_glosry.md)

- [DCL source code](../abap-glossary/abendcl_source_code_glosry.md) for [CDS roles](../abap-glossary/abencds_role_glosry.md)

- [SDL source code](../abap-glossary/abensdl_source_code_glosry.md) for [CDS service definitions](../abap-glossary/abencds_service_definition_glosry.md)

The different types of source code have different editors in [ADT](../abap-glossary/abenadt_glosry.md), which are documented there. The CDS objects defined in CDS source code are transported using the source code.

**CDS source field**

A field of a data source of a [CDS entity](../abap-glossary/abencds_entity_glosry.md) that can be used as a [CDS element](../abap-glossary/abencds_element_glosry.md) and at different operand positions of that CDS entity.

**CDS source type**

Denotes the type of [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md). The following categories are available:

- [CDS view entities](../abap-glossary/abencds_v2_view_glosry.md)

- [CDS projection views](../abap-glossary/abencds_projection_view_glosry.md)

- [CDS table functions](../abap-glossary/abencds_table_function_glosry.md)

- [CDS table entities](../abap-glossary/abencds_table_entity_glosry.md)

- [CDS hierarchies](../abap-glossary/abencds_hierarchy_glosry.md)

- [CDS custom entities](../abap-glossary/abencds_custom_entity_glosry.md)

- [CDS abstract entities](../abap-glossary/abencds_abstract_entity_glosry.md)

- [CDS DDIC-based views (obsolete)](../abap-glossary/abencds_v1_view_glosry.md)

- [CDS DDIC-based view extension](../abap-glossary/abencds_view_extend_glosry.md)

- [CDS view entity extension](../abap-glossary/abencds_view_entity_extend_glosry.md)

All available CDS source types are listed in the domain `DDDDLSRCTYPE`.

**CDS SQL query**

A [database query](../abap-glossary/abendb_query_glosry.md) that is implemented in the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) as a part of the definition of a [view entity](../abap-glossary/abencds_v2_view_glosry.md) using the SQL language element [`SELECT`](abap-cds-data-definitions/abencds_select_statement_v2.md). The clauses and additions of `SELECT` define the result set returned by the database. &#x200E;

**CDS system entity**

A [CDS entity](../abap-glossary/abencds_entity_glosry.md) delivered with an [ABAP system](../abap-glossary/abenabap_system_glosry.md) that implements basic functionality, such as generating a series of integers (`SERIES_GENERATE_INTEGER`). It can be used as data source of other CDS entities or in [queries](../abap-glossary/abenasql_query_glosry.md) of [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md).

**CDS system function**

A [CDS function](../abap-glossary/abencds_function_glosry.md) delivered as part of the [ABAP technology](../abap-glossary/abenabap_techno_glosry.md) that implements basic functionality. Currently, SAP delivers [analytical scalar functions](../abap-glossary/abencds_ana_scalar_glosry.md) and [SQL-based scalar functions](../abap-glossary/abencds_sql_scalar_glosry.md) as system functions. System functions are classified with the [C1 contract](../abap-glossary/abenc1_contract_glosry.md) for use internally in the system.

**CDS system table function**

A [CDS system entity](../abap-glossary/abencds_system_entity_glosry.md) that is realized as [CDS table function](../abap-glossary/abencds_table_function_glosry.md).

**CDS table entity**

A [CDS persistent entity](../abap-glossary/abencds_sql_entity_glosry.md) that defines a [database table](../abap-glossary/abendatabase_table_glosry.md) in ABAP CDS. A table entity is defined as a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md) using the statement [`DEFINE TABLE ENTITY`](abap-cds-data-definitions/abencds_table_entities.md).

**CDS table entity buffer**

A [CDS entity buffer](../abap-glossary/abencds_entity_buffer_glosry.md) that defines the kind of [table buffering](../abap-glossary/abentable_buffering_glosry.md) for a [CDS table entity](../abap-glossary/abencds_table_entity_glosry.md). Defined using the statement [`DEFINE TABLE ENTITY BUFFER`](abap-cds-tuning-objects/abencds_define_view_entity_buffer.md).

**CDS table function**

A [CDS persistent entity](../abap-glossary/abencds_sql_entity_glosry.md) defined using [`DEFINE TABLE FUNCTION`](abap-cds-data-definitions/abencds_f1_define_table_function.md) in a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md). Each CDS table function is linked with an [AMDP table function](../abap-glossary/abenamdp_table_function_glosry.md) in which it is implemented using [SQLScript](../abap-glossary/abensql_script_glosry.md). A CDS table function returns a tabular result set.

**CDS text association**

A regular [CDS association](../abap-glossary/abencds_association_glosry.md) whose [association target](../abap-glossary/abenassociation_target_glosry.md) is a [CDS text provider view](../abap-glossary/abencds_text_provider_glosry.md). The [target cardinality](../abap-glossary/abentarget_cardinality_glosry.md) of a CDS text association is `TO MANY`. CDS text associations are used for defining [CDS localized fields](../abap-glossary/abencds_localized_field_glosry.md).

**CDS text provider view**

A [CDS entity](../abap-glossary/abencds_entity_glosry.md) whose [primary key](../abap-glossary/abenprimary_key_glosry.md) consists of multiple [key fields](../abap-glossary/abenkey_field_glosry.md), one of which is of data type [`LANG`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and length 1. A text provider view typically contains one or more text fields for which translations in different languages are maintained. A text provider view can serve as an [association target](../abap-glossary/abenassociation_target_glosry.md) for a [CDS text association](../abap-glossary/abencds_text_association_glosry.md).

**CDS to-child association**

A specialized [CDS association](../abap-glossary/abencds_association_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_core_data_services_glosry.md) that is defined in the [parent entity](../abap-glossary/abenparent_entity_glosry.md) and points to the [child entity](../abap-glossary/abenchild_entity_glosry.md) using the syntax statement [`COMPOSITION OF`](abap-cds-data-definitions/abencds_composition_v2.md). In combination with the [to-parent association](../abap-glossary/abento_parent_association_glosry.md), they define a [CDS composition](../abap-glossary/abencds_composition_glosry.md) relationship. The CDS compositions are the basis for the [CDS composition tree](../abap-glossary/abencds_composition_tree_glosry.md) of a [RAP business object](../abap-glossary/abenrap_bo_glosry.md).

**CDS to-parent association**

A specialized [CDS association](../abap-glossary/abencds_association_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_core_data_services_glosry.md) that is defined in the [child entity](../abap-glossary/abenchild_entity_glosry.md) and points to the [parent entity](../abap-glossary/abenparent_entity_glosry.md) using the syntax statement [`ASSOCIATION TO PARENT`](abap-cds-data-definitions/abencds_to_parent_assoc_v2.md). In combination with the [to-child association](../abap-glossary/abento_child_association_glosry.md), they define a [CDS composition](../abap-glossary/abencds_composition_glosry.md) relationship. The CDS compositions are the basis for the [CDS composition tree](../abap-glossary/abencds_composition_tree_glosry.md) of a [RAP business object](../abap-glossary/abenrap_bo_glosry.md).

**CDS transactional interface**

A CDS transactional interface is a [CDS projection view](../abap-glossary/abencds_projection_view_glosry.md) that is intended to serve as stable public interface for consumption. A CDS transactional interface should be classified by a [release contract](../abap-glossary/abenrelease_contract_glosry.md) and thus serve as [released API](../abap-glossary/abenreleased_api_glosry.md). They are typically used in the context of the [ABAP RESTful Application Programming Model](../abap-glossary/abenarap_glosry.md) to provide the basis for a [RAP BO interface](../abap-glossary/abenrap_bo_interface_glosry.md). A CDS transactional interface is defined using the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) statement [`DEFINE VIEW ENTITY AS PROJECTION ON`](abap-cds-data-definitions/abencds_define_view_as_interface.md) and it must have its [provider contract](abap-cds-data-definitions/abencds_pv_provider_contract.md) set to `TRANSACTIONAL_INTERFACE`. A CDS transactional interface is a [CDS persistent entity](../abap-glossary/abencds_sql_entity_glosry.md).

**CDS transactional query**

A [CDS projection view](../abap-glossary/abencds_projection_view_glosry.md) that is intended for modeling transactional queries. A transactional query is typically used in the context of the [ABAP RESTful Application Programming Model](../abap-glossary/abenarap_glosry.md) to adapt a CDS data model for service-specific use cases. A transactional query is defined using the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) statement [`DEFINE VIEW ENTITY AS PROJECTION ON`](abap-cds-data-definitions/abencds_define_view_as_projection.md) and it must have the [provider contract](abap-cds-data-definitions/abencds_pv_provider_contract.md) set to `TRANSACTIONAL_QUERY`. A CDS transactional query is a [CDS persistent entity](../abap-glossary/abencds_sql_entity_glosry.md).

**CDS transient entity**

A [CDS entity](../abap-glossary/abencds_entity_glosry.md) for which no [ABAP-managed database object](../abap-glossary/abenabap_managed_db_object_glosry.md) is created and which cannot be used in read access in [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and ABAP CDS.

Currently, the following transient entities are available:

- [CDS custom entities](../abap-glossary/abencds_custom_entity_glosry.md)

- [CDS abstract entities](../abap-glossary/abencds_abstract_entity_glosry.md)

- [CDS analytical queries](../abap-glossary/abencds_analytic_query_glosry.md)

See also: [CDS persistent entity](../abap-glossary/abencds_sql_entity_glosry.md)

**CDS type**

[Data type](../abap-glossary/abendata_type_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). There are [CDS user-defined types](../abap-glossary/abencds_user_defined_type_glosry.md), [CDS built-in types](../abap-glossary/abencds_built_in_type_glosry.md), and [CDS generic types](../abap-glossary/abencds_generic_type_glosry.md).

**CDS type definition**

A definition of a [CDS user-defined type](../abap-glossary/abencds_user_defined_type_glosry.md) using [language elements](abap-cds-data-definitions/abencds_f1_ddl_syntax.md) of the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md).

**CDS user-defined function**

Custom function in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) that allows developers to define and implement their own custom logic and reuse it in operand positions of [CDS entities](../abap-glossary/abencds_entity_glosry.md). [SQL-based scalar functions](../abap-glossary/abencds_sql_scalar_glosry.md) are the only type of CDS user-defined functions available.

**CDS user-defined type**

A [CDS object](../abap-glossary/abencds_object_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). CDS user-defined types can be used for typing, casting, and as operands of expressions in [CDS entities](../abap-glossary/abencds_entity_glosry.md) and in other [CDS objects](../abap-glossary/abencds_object_glosry.md) and in ABAP after the addition `TYPES`. A CDS user-defined type can be enriched with metadata using [CDS annotations](../abap-glossary/abencds_annotation_glosry.md). Currently, the following CDS user-defined types are available:

- [CDS simple type](../abap-glossary/abencds_simple_type_glosry.md)

- [CDS enumerated type](../abap-glossary/abencds_enum_type_glosry.md)

**CDS variant**

[CDS object](../abap-glossary/abencds_object_glosry.md) of [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) defined in the [ADT](../abap-glossary/abenadt_glosry.md). A CDS variant consists of a name, which can be used to link a [CDS metadata extension](../abap-glossary/abencds_metadata_extension_glosry.md) to the CDS variant in the statement [`ANNOTATE`](abap-cds-annotations/abencds_f1_ddlx_syntax.md). When evaluating annotations, a CDS variant can be specified to select the corresponding CDS metadata extension during the [evaluation of the metadata extensions](abap-cds-annotations/abencds_meta_data_extension_eval.md).

## Caution

**CDS variants are not currently released for general use. It is not possible to define standalone CDS variants and the use of CDS variants in metadata extensions produces a syntax check warning.**

**CDS view**

A [CDS entity](../abap-glossary/abencds_entity_glosry.md) defined in a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md) that implements a [view](../abap-glossary/abenview_glosry.md). There are three types of CDS views:

- [CDS view entity](../abap-glossary/abencds_v2_view_glosry.md) defined by [`DEFINE VIEW ENTITY`](abap-cds-data-definitions/abencds_define_view_entity.md).

- [CDS projection view](../abap-glossary/abencds_projection_view_glosry.md) defined by [`DEFINE VIEW ENTITY AS PROJECTION`](abap-cds-data-definitions/abencds_define_view_as_projection.md).

- [CDS DDIC-based view (obsolete)](../abap-glossary/abencds_v1_view_glosry.md) defined by [`DEFINE VIEW`](abap-cds-obsolete-language-elements/abencds_define_view_v1.md).

Read access on a CDS view is possible using [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) or from other CDS entities.

**CDS view entity**

A [view](../abap-glossary/abenview_glosry.md) defined in [ABAP CDS](../abap-glossary/abencds_glosry.md) as a [CDS persistent entity](../abap-glossary/abencds_sql_entity_glosry.md) with the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) statement [`DEFINE VIEW ENTITY`](abap-cds-data-definitions/abencds_define_view_entity.md).

**CDS view entity buffer**

A [CDS entity buffer](../abap-glossary/abencds_entity_buffer_glosry.md) that defines the kind of [table buffering](../abap-glossary/abentable_buffering_glosry.md) for a [CDS entity](../abap-glossary/abencds_entity_glosry.md). Defined using the statement [`DEFINE VIEW ENTITY BUFFER`](abap-cds-tuning-objects/abencds_define_view_entity_buffer.md).

**CDS view entity extension**

[CDS entity extension](../abap-glossary/abencds_entity_extend_glosry.md) of a [CDS view entity](../abap-glossary/abencds_v2_view_glosry.md) or a [CDS projection view](../abap-glossary/abencds_projection_view_glosry.md). A CDS view entity extension can be used to add elements and/or clauses to a view without making any modifications to the original view. It is defined using the statement [`EXTEND VIEW ENTITY`](abap-cds-data-definitions/abencds_extend_view_entity.md).

**CDS virtual element**

An element in the element list of a [CDS DDL aspect](abap-cds-data-definitions/abencds_ddl_aspect_glosry.md) or a [projection view](../abap-glossary/abencds_projection_view_glosry.md). In projection views, this element is not included in the [projected entity](../abap-glossary/abencds_pv_projected_entity_glosry.md). Virtual elements are not persistent on the database, but calculated during runtime, usually in [ABAP classes](../abap-glossary/abenclass_glosry.md). In order to fill and analyze the virtual elements of a projection view, special frameworks like the [RAP query engine](../abap-glossary/abenrap_query_engine_glosry.md) have to be involved.

**CDS-Based Enterprise Search**

The ABAP-CDS-specific version of the [SAP Enterprise Search](../abap-glossary/abensap_enterprisesearch_glosry.md) technology. It is based on [CDS view entities](../abap-glossary/abencds_v2_view_glosry.md) in the backend. These view entities are annotated with [framework-specific annotations](../abap-glossary/abenfrmwrk_annotation_glosry.md) from the [`EnterpriseSearch`](abap-cds-annotations/abencds_enterprisesearch_f.md) domain. The annotations define search capabilities and they also trigger the generation of a [CDS-based search connector](../abap-glossary/abencds_search_connector_glosry.md). CDS-based enterprise search provides enhanced search capabilities in SAP Fiori launchpad.

**CDS-based search connector**

A [search connector](../abap-glossary/abensearch_connector_glosry.md) that enables communication between an [ABAP system](../abap-glossary/abenabap_system_glosry.md) and the [SAP HANA database](../abap-glossary/abenhana_database_glosry.md) in the context of [CDS-based enterprise search](../abap-glossary/abencds_enterprisesearch_glosry.md).

**CDS-managed DDIC view**

An obsolete [DDIC database view](../abap-glossary/abendatabase_view_glosry.md) of the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) that is created in addition to the [CDS entity](../abap-glossary/abencds_entity_glosry.md) when a [CDS DDIC-based view (obsolete)](../abap-glossary/abencds_v1_view_glosry.md) is activated. CDS-managed DDIC views are used as technical foundations for a CDS view of this type, but should not be used directly in ABAP or ABAP CDS.

**CDS/CTE association path**

A sequence of [CDS associations](../abap-glossary/abencds_association_glosry.md) and [CTE associations](../abap-glossary/abencte_association_glosry.md) that associate [CDS entities](../abap-glossary/abencds_entity_glosry.md) and [common table expressions](../abap-glossary/abencommon_table_expression_glosry.md) with [association targets](../abap-glossary/abenassociation_target_glosry.md). In other words, a mixture of CDS and CTE association paths. CDS or CTE association paths can be specified in the form of [SQL path expressions](../abap-glossary/abensql_path_expression_glosry.md) in [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md).

**character literal**

Also referred to as text literal. A [literal](../abap-glossary/abenabap_literal_glosry.md) with a [character-like data type](../abap-glossary/abencharlike_data_type_glosry.md) whose value is a [character string](../abap-glossary/abencharacter_string_glosry.md).

- In general ABAP, character literals are [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), character literals can be [typed literals](../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Character Literals in ABAP](../abap-programming-language/abap-declarations/abenuntyped_character_literals.md)

- [Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_literals.md)

- [Literals in CDS](abap-cds-data-definitions/abencds_literal_v2.md)

**client dependency**

Property of a [SQL data source](../abap-glossary/abensql_data_source_glosry.md). A SQL data source can be [client-dependent](../abap-glossary/abenclient_dependent_glosry.md) or [client-independent](../abap-glossary/abenclient_independent_glosry.md). When accessing a client-dependent SQL data source in [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md), an implicit [client handling](../abap-glossary/abenclient_handling_glosry.md) takes place.

**client handling**

Processing of the application data of a [client](../abap-glossary/abenclient_glosry.md). When accessing [client-dependent](../abap-glossary/abenclient_dependent_glosry.md) [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) or [views](../abap-glossary/abenview_glosry.md), [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) statements use [implicit client](../abap-programming-language/abap-database-access/abenabap_sql_client_handling.md) handling, which by default accesses the [current client](../abap-glossary/abencurrent_client_glosry.md). By using additions to the ABAP SQL statements, the implicit client handling can be switched to other clients. The client handling of [AMDP methods](../abap-glossary/abenamdp_method_glosry.md) can be defined with special [AMDP options](../abap-programming-language/abap-database-access/abapmethods_amdp_options_client.md).

**client isolation**

Client isolation on an [AS ABAP](../abap-glossary/abenas_abap_glosry.md) means that an [ABAP user](../abap-glossary/abenabap_user_glosry.md) has access to data of the [current client](../abap-glossary/abencurrent_client_glosry.md) only. In [ABAP Cloud](../abap-glossary/abenabap_cloud_glosry.md), client isolation is enforced as follows:

- Implicit [client handling](../abap-glossary/abenclient_handling_glosry.md) in [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md).

- [AMDP methods](../abap-glossary/abenamdp_method_glosry.md) can access [client-safe](../abap-glossary/abenclient_safe_glosry.md) [repository objects](../abap-glossary/abenrepository_object_glosry.md) only.

- [CDS entities](../abap-glossary/abencds_entity_glosry.md) that are [released APIs](../abap-glossary/abenreleased_api_glosry.md) must be [client-safe](../abap-glossary/abenclient_safe_glosry.md).

**client literal**

A [literal](../abap-glossary/abenabap_literal_glosry.md) that contains a [client ID](../abap-glossary/abenclient_identifier_glosry.md) and has the data type [`CLNT`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Not available in general ABAP.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), client literals are available as [typed literals](../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](abap-cds-data-definitions/abencds_typed_literal_v2.md)

**client-dependent**

A [SQL data source](../abap-glossary/abensql_data_source_glosry.md) for which an implicit [client handling](../abap-glossary/abenclient_handling_glosry.md) takes place when accessed with [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md).

- A [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) or DDIC view in [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) is client-dependent if the first column is a [client column](../abap-glossary/abenclient_column_glosry.md). The system table `T000`, which contains the [AS ABAP](../abap-glossary/abenas_abap_glosry.md) [client IDs](../abap-glossary/abenclient_identifier_glosry.md), is an exception to this rule.

- The client dependency of a [CDS entity](../abap-glossary/abencds_entity_glosry.md) is determined by its data sources. Client handling is by done implicitly by filtering the [session variable](../abap-glossary/abensession_variable_glosry.md) `$session.client`.

- The client dependency of [CDS DDIC-based views (obsolete)](../abap-glossary/abencds_v1_view_glosry.md) is declared in the [CDS source code](../abap-glossary/abencds_source_code_glosry.md) by the [ABAP annotation](../abap-glossary/abenabap_annotation_glosry.md) `@CLientHandling.type`.

See also: [client-independent](../abap-glossary/abenclient_independent_glosry.md).

**client-independent**

A [SQL data source](../abap-glossary/abensql_data_source_glosry.md) that is not [client-dependent](../abap-glossary/abenclient_dependent_glosry.md). Client-independent SQL data sources contain data that is not specific to a [client](../abap-glossary/abenclient_glosry.md) and should be accessed by [system programs](../abap-glossary/abensystem_program_glosry.md). See also [system table](../abap-glossary/abensystem_table_glosry.md).

**client-safe**

A [repository object](../abap-glossary/abenrepository_object_glosry.md) that accesses [client-dependent](../abap-glossary/abenclient_dependent_glosry.md) [SQL data sources](../abap-glossary/abensql_data_source_glosry.md) is client-safe, if it can access data of one [client](../abap-glossary/abenclient_glosry.md) only. Such repository objects support the concept of [client isolation](../abap-glossary/abenclient_isolation_glosry.md) for [AMDP methods](../abap-glossary/abenamdp_method_glosry.md):

- AMDP methods that have the [ABAP language version](../abap-glossary/abenabap_version_glosry.md) [ABAP for Cloud Development](../abap-glossary/abenabap_for_cloud_dev_glosry.md) or are a [released API](../abap-glossary/abenreleased_api_glosry.md) with a [C1 contract](../abap-glossary/abenc1_contract_glosry.md) or a [C4 contract](../abap-glossary/abenc4_contract_glosry.md) must be [client-safe](../abap-programming-language/abap-database-access/abenamdp_client_safety.md) and must access client-safe objects only.

- For a [CDS entity](../abap-glossary/abencds_entity_glosry.md), an [annotation](../abap-glossary/abencds_annotation_glosry.md) [`ClientHandling.clientSafe`](abap-cds-annotations/abencds_1549616294_anno.md) can be specified that enforces checks that guarantee its client safety. For CDS entities that do not have this annotations but are [released APIs](../abap-glossary/abenreleased_api_glosry.md), the checks are done implicitly.

A repository object that accesses only [client-independent](../abap-glossary/abenclient_independent_glosry.md) SQL data sources is implicitly client-safe.

**coalesce function**

A [built-in function](../abap-glossary/abenbuiltin_function_glosry.md) that returns the first non-zero expression in a list of expressions. Available in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) and [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md).

**complex case distinction**

Also searched case. A [case distinction](../abap-glossary/abencase_distinction_glosry.md) that evaluates logical expressions to determine which statements to execute. Available in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) and [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md).

**composition source**

Data source that serves as the source of a [CDS composition](../abap-glossary/abencds_composition_glosry.md).

**composition target**

Data source that serves as the target of a [CDS composition](../abap-glossary/abencds_composition_glosry.md).

**constant**

In ABAP, a [named data object](../abap-glossary/abennamed_data_object_glosry.md) whose value cannot be changed during the runtime of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) or a [procedure](../abap-glossary/abenprocedure_glosry.md). In [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), constants appear as components of [CDS enumerated types](../abap-glossary/abencds_enum_type_glosry.md).

**core annotation**

*-\>* [ABAP annotation](../abap-glossary/abenabap_annotation_glosry.md)

**Core Data Services**

*-\>* [ABAP Core Data Services](../abap-glossary/abenabap_core_data_services_glosry.md)

**cross join**

A [join type](../abap-glossary/abenjoin_type_glosry.md) for which the rows of the result set are determined by a cross product of the result sets of both [SQL data sources](../abap-glossary/abensql_data_source_glosry.md). The result set contains all possible combinations of rows.

**CSN**

*-\>* [CDS schema notation](../abap-glossary/abencds_schema_notation_glosry.md)

**currency field**

A currency field is linked to a [currency key](../abap-glossary/abencurrency_key_glosry.md) and it is used for entering an amount in a particular currency. Currency fields are available in [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) (DDIC) and in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), but the possible data types and handling differs.

See also:

- [DDIC currency field](../abap-glossary/abenddic_currency_field_glosry.md)

- [ABAP CDS amount field](../abap-glossary/abencds_amount_field_glosry.md)

**currency field literal**

A [literal](../abap-glossary/abenabap_literal_glosry.md) of the data type [`CURR`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Not available in general ABAP.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), currency field literals are available as [typed literals](../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](abap-cds-data-definitions/abencds_typed_literal_v2.md)

**currency key literal**

A [literal](../abap-glossary/abenabap_literal_glosry.md) of the data type [`CUKY`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) that contains a [currency code](../abap-glossary/abencurrency_id_glosry.md).

- Not available in general ABAP.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), currency key literals are available as [typed literals](../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](abap-cds-data-definitions/abencds_typed_literal_v2.md)

**current client**

The current client of a [user session](../abap-glossary/abenuser_session_glosry.md) is the [client](../abap-glossary/abenclient_glosry.md) whose [client ID](../abap-glossary/abenclient_identifier_glosry.md) was specified during [logon](../abap-glossary/abenlogon_glosry.md).

**database query**

Query for short. A database query is used to retrieve data from [database tables](../abap-glossary/abendatabase_table_glosry.md). In [SQL](../abap-glossary/abensql_glosry.md), queries are generally expressed in its subset [DQL](../abap-glossary/abendql_glosry.md) (Data Query Language). In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) a query is called [ABAP SQL Query](../abap-glossary/abenasql_query_glosry.md). In [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), queries appear in the SQL-part of the definitions of [CDS views](../abap-glossary/abencds_view_glosry.md).

**DCL**

Short for Data Control Language. A subset of [SQL](../abap-glossary/abensql_glosry.md). The statements of the DCL perform authorization and consistency checks on [relational databases](../abap-glossary/abenrelational_database_glosry.md).

- [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) does not support DCL. On an Application Server ABAP, the functionality of the [DCL](../abap-glossary/abencds_dcl_glosry.md) is implemented using [authorization objects](../abap-glossary/abenauthorization_object_glosry.md) and SAP locks.

- [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) provides a [DCL](../abap-glossary/abencds_dcl_glosry.md) that implements an [access control](../abap-glossary/abencds_access_control_glosry.md), where database objects can be linked to authorization objects of AS ABAP.

**DCL source code**

[CDS source code](../abap-glossary/abencds_source_code_glosry.md) for the definition of [CDS roles](../abap-glossary/abencds_role_glosry.md) and of [CDS access policies](../abap-glossary/abencds_access_policy_glosry.md) for [CDS access control](../abap-glossary/abencds_access_control_glosry.md) in the [CDS DCL](../abap-glossary/abencds_dcl_glosry.md) in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md).

**DDL**

Short for Data Definition Language. A subset of [SQL](../abap-glossary/abensql_glosry.md). The statements in the DDL create and delete the objects of a [relational database](../abap-glossary/abenrelational_database_glosry.md). In an ABAP system, [ABAP-managed database objects](../abap-glossary/abenabap_managed_db_object_glosry.md) are edited using tools and frameworks in [AS ABAP](../abap-glossary/abenas_abap_glosry.md), such as [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md), [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), and [AMDP](../abap-glossary/abenamdp_glosry.md), where [DDIC DDL](../abap-glossary/abenddic_dcl_glosry.md), [CDS DDL](../abap-glossary/abencds_ddl_glosry.md), or Native SQL are used. [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) does not support DDL.

**DDL source code**

The [CDS source code](../abap-glossary/abencds_source_code_glosry.md) for [CDS data definitions](../abap-glossary/abencds_data_definition_glosry.md) or their extensions in [CDS DDL](../abap-glossary/abencds_ddl_glosry.md). See also [`DDLA` source code](../abap-glossary/abenddla_source_code_glosry.md) and [`DDLX` source code](../abap-glossary/abenddlx_source_code_glosry.md).

**DDLA source code**

[CDS source code](../abap-glossary/abencds_source_code_glosry.md) for [CDS annotation definitions](../abap-glossary/abencds_anno_definition_glosry.md) in [CDS DDLA](../abap-glossary/abencds_ddla_glosry.md).

**DDLX source code**

[CDS source code](../abap-glossary/abencds_source_code_glosry.md) for [CDS metadata extensions](../abap-glossary/abencds_metadata_extension_glosry.md) in [CDS DDLX](../abap-glossary/abencds_ddlx_glosry.md).

**decimal floating point literal**

A [numeric literal](../abap-glossary/abennumeric_literal_glosry.md) of a [decimal floating point type](../abap-glossary/abendecfloat_type_glosry.md).

- Not available in general ABAP.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), decimal floating point literals are available as [typed literals](../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](abap-cds-data-definitions/abencds_typed_literal_v2.md)

**DML**

Short for Data Manipulation Language. Subset of [SQL](../abap-glossary/abensql_glosry.md). The statements in DML perform [CUD](../abap-glossary/abencud_glosry.md) operations on [relational](../abap-glossary/abenrelational_database_glosry.md) [database tables](../abap-glossary/abendatabase_table_glosry.md). In the ABAP language, DML is implemented predominantly by the statements for [write accesses](../abap-programming-language/abap-database-access/abenabap_sql_writing.md) of [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md). **Note:** Sometimes the term DML also includes the statements of [DQL](../abap-glossary/abendql_glosry.md).

**DQL**

Short for Data Query Language. Subset of [SQL](../abap-glossary/abensql_glosry.md). The statements in DQL perform read operations on [relational](../abap-glossary/abenrelational_database_glosry.md) [database tables](../abap-glossary/abendatabase_table_glosry.md). In the ABAP language, DQL is implemented predominantly by the statements for [read accesses](../abap-programming-language/abap-database-access/abenabap_sql_reading.md) of [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md). In [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), the DQL statement `SELECT` is embedded in [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) for [CDS views](../abap-glossary/abencds_view_glosry.md). **Note:** Sometimes the statements of DQL are included in the term [DML](../abap-glossary/abendml_glosry.md).

**dynamic external entity**

A [CDS external entity](../abap-glossary/abencds_external_entity_glosry.md) that does not specify a [logical external schema](../abap-glossary/abencds_logical_schema_glosry.md) in its [data definition](../abap-glossary/abencds_data_definition_glosry.md), but instead uses the addition [`PROVIDED AT RUNTIME`](abap-cds-data-definitions/abencds_define_external_entity.md). The logical external schema for a dynamic external entity must be provided as a part of the [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) `SELECT` statement when accessing the external entity, using a `PROVIDED BY` clause. Dynamic external entities can only be accessed by ABAP SQL; they cannot be used as a data source for other [CDS entities](../abap-glossary/abencds_entity_glosry.md).

**enumerated structure**

A constant [structure](../abap-glossary/abenconstant_glosry.md) declared in the definition of an [enumerated type](../abap-glossary/abenenumerated_type_glosry.md), whose components contain all [enumerated values](../abap-glossary/abenenumerated_value_glosry.md) of the enumerated type. The components are special [enumerated objects](../abap-glossary/abenenumerated_object_glosry.md). For an [ABAP enumerated type](../abap-glossary/abenenumerated_type_glosry.md), the declaration of an enumerated structure is optional. A [CDS enumerated type](../abap-glossary/abencds_enum_type_glosry.md) is always connected to an enumerated structure. See also [enumerated constant](../abap-glossary/abenenumerated_constant_glosry.md).

**enumerated type**

Enum for short. An enumerated type is a [data type](../abap-glossary/abendata_type_glosry.md) that specifies a value set in addition to the actual type properties. Enumerated types can be defined in ABAP with [`TYPES BEGIN OF ENUM`](../abap-programming-language/abap-declarations/abaptypes_enum.md) or in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) with [`DEFINE TYPE ENUM`](abap-cds-data-definitions/abencds_define_enum_type.md).

See also:

- [ABAP enumerated type](../abap-glossary/abenenumerated_type_glosry.md)

- [CDS enumerated type](../abap-glossary/abencds_enum_type_glosry.md)

**enumerated value**

An enumerated value is an allowed value of an [enumerated variable](../abap-glossary/abenenumerated_variable_glosry.md) or a [CDS enumerated element](../abap-glossary/abencds_enum_element_glosry.md). The possible enumerated values are defined in the definition of the respective [enumerated type](../abap-glossary/abenenum_type_glosry.md) as the values of [enumerated constants](../abap-glossary/abenenumerated_constant_glosry.md) or of components of an [enumerated structure](../abap-glossary/abenenumerated_structure_glosry.md). The technical data type of an enumerated value is the [base type](../abap-glossary/abenbase_type_glosry.md) of the enumerated type.

- [Enumerated types in ABAP](../abap-programming-language/abap-processing-internal-data/abenenumerated_types_usage.md)

- [Enumerated types in ABAP CDS](abap-cds-data-definitions/abencds_enumeration_types.md)

**enumeration**

*-\>* [enumerated type](../abap-glossary/abenenum_type_glosry.md)

**filter condition**

Specifies a condition for a [CDS association](../abap-glossary/abencds_association_glosry.md) or [CTE association](../abap-glossary/abencte_association_glosry.md) in an [SQL path expression](../abap-glossary/abensql_path_expression_glosry.md).

**framework-specific annotation**

[SAP annotation](../abap-glossary/abensap_annotation_glosry.md) that is evaluated by a framework of an SAP software component.

**grouping set**

Grouping sets are used in the [`GROUP BY`](../abap-programming-language/abap-database-access/abapgroupby_clause.md) clause of a [query](../abap-glossary/abenasql_query_glosry.md). A grouping set is specified either as an empty grouping set or as a comma-separated list. Columns and SQL expressions can also be used in the list. The `GROUP BY` addition `GROUPING SETS` makes it possible to define multiple grouping sets under a `GROUP BY` clause. The grouping sets are aggregated separately and merged into one result set.

**inheritance condition**

Part of an [access condition](../abap-glossary/abenaccess_condition_glosry.md) in a [CDS role](../abap-glossary/abencds_role_glosry.md) that inherits conditions from another [CDS role](../abap-glossary/abencds_role_glosry.md) or a different [CDS entity](../abap-glossary/abencds_entity_glosry.md).

**integer literal**

A [numeric literal](../abap-glossary/abennumeric_literal_glosry.md) of an [integer type](../abap-glossary/abeninteger_type_glosry.md).

- In general ABAP, integer literals are [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), integer literals can be [typed literals](../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Numeric Literals in ABAP](../abap-programming-language/abap-declarations/abenuntyped_number_literals.md)

- [Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_literals.md)

- [Literals in CDS](abap-cds-data-definitions/abencds_literal_v2.md)

**join**

A combination of two [SQL data sources](../abap-glossary/abensql_data_source_glosry.md) into one result set, consisting of columns of both data sources. The rows of the result set are determined by the [join type](../abap-glossary/abenjoin_type_glosry.md) and by [join conditions](../abap-glossary/abenjoin_condition_glosry.md) between columns of the data sources. The relation between the rows of the data sources can be expressed by a [cardinality](../abap-glossary/abencardinality_glosry.md). Joins can be implemented in ABAP as follows:

- DDIC views in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md)

- [Join expressions](../abap-glossary/abenjoin_expression_glosry.md) in [queries](../abap-glossary/abenasql_query_glosry.md) of [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md)

- [Join expressions](../abap-glossary/abenjoin_expression_glosry.md) in the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) of [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md)

Furthermore, [CDS associations](../abap-glossary/abencds_association_glosry.md) and [CTE associations](../abap-glossary/abencte_association_glosry.md) define join relationships that are instantiated when the associations are used in [SQL path expressions](../abap-glossary/abensql_path_expression_glosry.md).

**join condition**

A [SQL condition](../abap-glossary/abensql_cond_glosry.md) or a [CDS DDL condition](abap-cds-data-definitions/abencds_conditional_expression_v2.md) specified after the addition `ON` of a [join expression](../abap-glossary/abenjoin_expression_glosry.md). Also called `ON` condition.

**join expression**

The implementation of a [join](../abap-glossary/abenjoin_glosry.md) in [SQL](../abap-glossary/abensql_glosry.md) using the addition `JOIN`. Join expressions can be defined in [queries](../abap-glossary/abenasql_query_glosry.md), defined by the [`SELECT`](../abap-programming-language/abap-database-access/abapselect.md) statement of [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md), the [`SELECT` statement in CDS view entities](abap-cds-data-definitions/abencds_select_statement_v2.md), or the [`SELECT` statement in CDS DDIC-based views (obsolete)](abap-cds-data-definitions/abencds_select_statement_v2.md).

**join type**

The join type determines, together with the [join conditions](../abap-glossary/abenjoin_condition_glosry.md) of a [join expression](../abap-glossary/abenjoin_expression_glosry.md), how the rows of its result set are combined from its [SQL data sources](../abap-glossary/abensql_data_source_glosry.md). [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) support [inner joins](../abap-glossary/abeninner_join_glosry.md), [outer joins](../abap-glossary/abenouter_join_glosry.md) ([left](../abap-glossary/abenleft_outer_join_glosry.md) and [right](../abap-glossary/abenright_outer_join_glosry.md)), and [cross joins](../abap-glossary/abencross_join_glosry.md).

**language key literal**

A [literal](../abap-glossary/abenabap_literal_glosry.md) of the data type [`LANG`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) that contains a language key.

- Not available in general ABAP.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), language key literals are available as [typed literals](../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](abap-cds-data-definitions/abencds_typed_literal_v2.md)

**leaf entity**

A [CDS entity](../abap-glossary/abencds_entity_glosry.md) of a [CDS composition tree](../abap-glossary/abencds_composition_tree_glosry.md) of a [RAP business object](../abap-glossary/abenrap_bo_glosry.md) that does not have any [child entities](../abap-glossary/abenchild_entity_glosry.md). The [root entity](../abap-glossary/abenroot_entity_glosry.md) can also be a leaf entity.

**left outer join**

A [join type](../abap-glossary/abenjoin_type_glosry.md) that determines the same rows as an [inner join](../abap-glossary/abeninner_join_glosry.md) and an additional row for each row of the left [SQL data source](../abap-glossary/abensql_data_source_glosry.md) that is not included by the [join conditions](../abap-glossary/abenjoin_condition_glosry.md). In these rows, the columns coming from the right data source contain [null values](../abap-glossary/abennull_value_glosry.md).

**literal**

The textual representation of a value in the [ABAP source code](../abap-glossary/abenabap_source_code_glosry.md) of an [ABAP program](../abap-glossary/abenabap_program_glosry.md) or in a [CDS object](../abap-glossary/abencds_object_glosry.md). There are [typed literals](../abap-glossary/abentyped_literal_glosry.md) and [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md) available.

See also:

- [ABAP literal](../abap-glossary/abenabap_literal_glosry.md)

- [ABAP SQL literal](../abap-glossary/abenabap_sql_literal_glosry.md)

- [CDS literal](../abap-glossary/abencds_literal_glosry.md)

**logical expression**

Formulation of a condition for [operands](../abap-glossary/abenoperand_glosry.md). A logical expression is a single [relational expression](../abap-glossary/abenrelational_expression_glosry.md) or is made up of multiple relational expressions combined by [Boolean operators](../abap-glossary/abenboolean_operator_glosry.md). The result of a logical expression is a [truth value](../abap-glossary/abentruth_value_glosry.md), that is, either true or false.

- In general ABAP, logical expressions are used in [control statements](../abap-glossary/abencontrol_statement_glosry.md) or other statements that contain conditions, as well as in [conditional expressions](../abap-glossary/abenconditional_expression_glosry.md) and [Boolean functions](../abap-glossary/abenboole_function_glosry.md). For further details, see the topic [Logical Expressions (`log_exp`)](../abap-programming-language/abap-program-flow-logic/abenlogexp.md).

- In ABAP SQL, logical expressions are used in conditions, such as `WHERE` and `ON` conditions.

- In ABAP CDS, logical expressions are used in conditions, such as `WHERE` and `ON` conditions.

**main annotation**

Also called root annotation. The [CDS annotation](../abap-glossary/abencds_annotation_glosry.md) defined after the statement `DEFINE ANNOTATION` in a [CDS annotation definition](../abap-glossary/abencds_annotation_glosry.md), or a name of an [annotation](../abap-glossary/abencds_annotation_glosry.md) specified on its own or in front of a period in the [annotation syntax](../abap-glossary/abencds_annotation_syntax_glosry.md). A main annotation can be structured using [subannotations](../abap-glossary/abensub_annotation_glosry.md).

**null value**

A special value returned by a [database](../abap-glossary/abendatabase_glosry.md) to indicate an undefined value or result. There are no special null values in ABAP. In assignments made to ABAP [data objects](../abap-glossary/abendata_object_glosry.md) in [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md), Native SQL, and [AMDP](../abap-glossary/abenamdp_glosry.md), null values are transformed to type-dependent [initial values](../abap-glossary/abeninitial_value_glosry.md). The [ABAP SQL in-memory engine](../abap-programming-language/abap-database-access/abenabap_sql_inmemeng.md) for accessing the [table buffer](../abap-glossary/abentable_buffer_glosry.md) and [internal tables](../abap-glossary/abeninternal_table_glosry.md) as [data sources](../abap-programming-language/abap-database-access/abapselect_itab.md) of [ABAP SQL queries](../abap-glossary/abenasql_query_glosry.md), however, handles null values as null values.

[ABAP SQL - Null Values](../abap-programming-language/abap-database-access/abenabap_sql_null_values.md)

[ABAP CDS - Null Values](abencds_null_values.md)

**numeric literal**

A [literal](../abap-glossary/abenabap_literal_glosry.md) that has a [numeric data type](../abap-glossary/abennumeric_data_type_glosry.md) and whose characters represent a numeric value.

- In general ABAP, numeric literals are [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), numeric literals can be [typed literals](../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Numeric Literals in ABAP](../abap-programming-language/abap-declarations/abenuntyped_number_literals.md)

- [Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_literals.md)

- [Literals in CDS](abap-cds-data-definitions/abencds_literal_v2.md)

**numeric text literal**

A [literal](../abap-glossary/abenabap_literal_glosry.md) that contains [numeric text](../abap-glossary/abennumeric_text_glosry.md) and has the length of the specified characters. The data type is [`n`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) or [`NUMC`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Not available in general ABAP.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md), numeric text literals are available as [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

- In [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), numeric text literals can be [typed literals](../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_literals.md)

- [Literals in CDS](abap-cds-data-definitions/abencds_literal_v2.md)

**operand**

A component of an [ABAP statement](../abap-glossary/abenabap_statement_glosry.md) or of a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md) at an [operand position](../abap-glossary/abenoperand_position_glosry.md). An operand can be an [elementary operand](../abap-glossary/abenelementary_operand_glosry.md) or an [expression](../abap-glossary/abenexp_glosry.md).

There are different types of operands:

- [ABAP operands](../abap-glossary/abenabap_operand_glosry.md)

- [CDS operands](../abap-glossary/abencds_operand_glosry.md)

**operand position**

Position of an [ABAP statement](../abap-glossary/abenabap_statement_glosry.md) or of a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md) at which an [operand](../abap-glossary/abenoperand_glosry.md) is listed. There are [read](../abap-glossary/abenread_position_glosry.md) and [write positions](../abap-glossary/abenwrite_position_glosry.md). In an ABAP statement, such an operand position is typed with an [operand type](../abap-glossary/abenoperand_type_glosry.md) and appropriate [data objects](../abap-glossary/abendata_object_glosry.md) or [expressions](../abap-glossary/abenexpression_glosry.md) can be specified. The operand positions for the latter are [expression positions](../abap-glossary/abenexpression_position_glosry.md). Besides that there are other operand positions, where types, callable units or other external resources such as [CDS entities](../abap-glossary/abencds_entity_glosry.md) or [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) can be specified as operands.

**operator**

Component of an [ABAP statement](../abap-glossary/abenabap_statement_glosry.md) or of a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md) that, when combined with [operands](../abap-glossary/abenoperand_glosry.md), forms an [expression](../abap-glossary/abenexp_glosry.md). When the statement is executed, an operation is executed for two operands connected by one operator, and the result is processed further in the statement. There are [arithmetic](../abap-glossary/abenarithmetic_operator_glosry.md), [bit](../abap-glossary/abenbit_operator_glosry.md), [string](../abap-glossary/abenstring_operator_glosry.md), [Boolean](../abap-glossary/abenboolean_operator_glosry.md), [relational](../abap-glossary/abenrel_operator_glosry.md), and [assignment operators](../abap-glossary/abenassignment_operator_glosry.md). There are also operators that do not combine operands, but perform other operations in [operand positions](../abap-glossary/abenoperand_position_glosry.md). Operators of this type are the [dereferencing operator](../abap-glossary/abendereferencing_operat_glosry.md), [declarations operators](../abap-glossary/abendeclaration_operator_glosry.md), and [constructor operators](../abap-glossary/abenconstructor_operator_glosry.md). Finally, the [literal operator](../abap-glossary/abenassignment_operator_glosry.md) is used to combine two [literals](../abap-glossary/abenabap_literal_glosry.md).

**outer join**

A [type of join](../abap-glossary/abenjoin_type_glosry.md). There are two types of outer joins:

- [left outer join](../abap-glossary/abenleft_outer_join_glosry.md)

- [right outer join](../abap-glossary/abenright_outer_join_glosry.md)

**packed number literal**

A [numeric literal](../abap-glossary/abennumeric_literal_glosry.md) of [packed number type](../abap-glossary/abenpacked_number_type_glosry.md).

- In general ABAP, packed number literals are [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), packed number literals can be [typed literals](../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Numeric Literals in ABAP](../abap-programming-language/abap-declarations/abenuntyped_number_literals.md)

- [Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_literals.md)

- [Literals in CDS](abap-cds-data-definitions/abencds_literal_v2.md)

**path expression**

A sequence of [associations](../abap-glossary/abenassociation_glosry.md) specified at an operand position. Either an [SQL path expression](../abap-glossary/abensql_path_expression_glosry.md) or a [mesh path expression](../abap-glossary/abenmesh_path_expression_glosry.md).

**path specification**

*-\>* [Path expression](../abap-glossary/abenpath_expression_glosry.md)

**quantity field literal**

A [literal](../abap-glossary/abenabap_literal_glosry.md) of the data type [`QUAN`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Not available in general ABAP.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), quantity field literals are available as [typed literals](../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](abap-cds-data-definitions/abencds_typed_literal_v2.md)

**query**

*-\>* [database query](../abap-glossary/abendb_query_glosry.md)

**replacement object**

A replacement object is a [CDS view](../abap-glossary/abencds_view_glosry.md) that can be specified for a [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) or a [DDIC database view](../abap-glossary/abendatabase_view_glosry.md). In case of a read access using [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md), the replacement object is addressed instead of the original object.

**return value**

The result of [functional methods](../abap-glossary/abenfunctional_method_glosry.md), [built-in functions](../abap-glossary/abenbuiltin_function_glosry.md), and [CDS scalar functions](../abap-glossary/abencds_scalar_function_glosry.md).

- In the [ABAP language](../abap-glossary/abenabala_glosry.md), the result of functional methods is the [formal parameter](../abap-glossary/abenformal_parameter_glosry.md) defined by the addition [`RETURNING`](../abap-programming-language/abap-declarations/abapmethods_functional.md) of the statement [`[CLASS-]`](../abap-programming-language/abap-declarations/abapclass-methods.md)[`METHODS`](../abap-programming-language/abap-declarations/abapmethods.md).

- in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), the result of a CDS scalar function whose data type is defined after the addition [`RETURNS`](abap-cds-data-definitions/abencds_define_scalar_function.md).

**reuse expression**

A [CDS element](../abap-glossary/abencds_element_glosry.md) that reuses an expression from the `SELECT` list of the same entity using the syntax [`$projection`](abap-cds-data-definitions/abencds_reusable_expression_v2.md).

**right outer join**

A [type of join](../abap-glossary/abenjoin_type_glosry.md) that determines the same rows as an [inner join](../abap-glossary/abeninner_join_glosry.md) and an additional row for each row of the right [SQL data source](../abap-glossary/abensql_data_source_glosry.md) that is not included by the [join conditions](../abap-glossary/abenjoin_condition_glosry.md). In these rows, the columns coming from the left data source contain [null values](../abap-glossary/abennull_value_glosry.md).

**root annotation**

*-\>* [main annotation](../abap-glossary/abenmain_annotation_glosry.md)

**SAP annotation**

[CDS annotation](../abap-glossary/abencds_annotation_glosry.md) delivered by SAP as a [CDS annotation definition](../abap-glossary/abencds_anno_definition_glosry.md). There are the following categories of SAP annotations:

- [ABAP annotations](../abap-glossary/abenabap_annotation_glosry.md), which are evaluated by the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) for every [CDS object](../abap-glossary/abencds_object_glosry.md).

- [Framework-specific annotations](../abap-glossary/abenfrmwrk_annotation_glosry.md), which are evaluated by the frameworks of other software components.

**SDL source code**

[CDS source code](../abap-glossary/abencds_source_code_glosry.md) for [CDS service definitions](../abap-glossary/abencds_service_definition_glosry.md) in [CDS SDL](../abap-glossary/abencds_sdl_glosry.md).

**self-association**

An [association](../abap-glossary/abenassociation_glosry.md) in which the [association source](../abap-glossary/abenassociation_source_glosry.md) and the [association target](../abap-glossary/abenassociation_target_glosry.md) are the same. Also referred to as reflexive association.

**service binding**

SB for short. A service binding is a [repository object](../abap-glossary/abenrepository_object_glosry.md) that binds a [CDS service definition](../abap-glossary/abencds_service_definition_glosry.md) to a communication protocol and publishes it as a [business service](../abap-glossary/abenbs_glosry.md) of [AS ABAP](../abap-glossary/abenas_abap_glosry.md).

**session variable**

A global variable of a [database system](../abap-glossary/abendatabase_system_glosry.md) that contains information about the current context. The [SAP HANA database](../abap-glossary/abenhana_database_glosry.md) has special ABAP-specific session variables whose content matches the value of certain [ABAP system fields](../abap-glossary/abensystem_field_glosry.md) when accessed from ABAP. In [CDS views](../abap-glossary/abencds_view_glosry.md), these ABAP-specific session variables can be accessed on all supported platforms.

**set operator**

A set operator merges the result sets of multiple queries into a single result set. In [CDS view entities](../abap-glossary/abencds_v2_view_glosry.md) and [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md), the following set operators are available:

- `EXCEPT` returns all distinct rows of the first result set that are not part of the following result sets.

- `INTERSECT` returns all distinct rows that are part of all result sets.

- `UNION` merges the result sets of all queries.

[Set operators in CDS view entities](abap-cds-data-definitions/abencds_set_operators.md)

[Set operators in ABAP SQL](../abap-programming-language/abap-database-access/abapunion.md)

**simple case distinction**

A [case distinction](../abap-glossary/abencase_distinction_glosry.md) that matches an operand to another operand specified in one or more `WHEN` clauses. Available in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) and [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md).

**source cardinality**

The [cardinality](../abap-glossary/abencardinality_glosry.md) of a [join](../abap-glossary/abenjoin_glosry.md) or [association](../abap-glossary/abenassociation_glosry.md) consists of a source cardinality and a [target cardinality](../abap-glossary/abentarget_cardinality_glosry.md). The source cardinality describes the number of matching entries for the entries of the joined data source. For example, a source cardinality of one means that each record of the joined data source has zero or one matching entry in the original data source.

**SQL expression**

An [expression](../abap-glossary/abenexp_glosry.md) in an [ABAP SQL statement](../abap-glossary/abenabap_sql_glosry.md) or in [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) that is evaluated by the database.

- [SQL expressions in ABAP SQL](../abap-programming-language/abap-database-access/abapsql_expr.md)

- [SQL expressions in CDS DDL](abap-cds-data-definitions/abencds_expressions_v2.md)

**SQL function**

Built-in database platform function that can be used in [SQL](../abap-glossary/abensql_glosry.md). In [ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_functions.md) and in the [CDS DDL](abap-cds-data-definitions/abencds_builtin_functions_v2.md) in [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), a set of SQL functions can be accessed platform-independently.

**SQL path expression**

Specifies a [CDS association path](../abap-glossary/abencds_association_path_glosry.md), a [CTE association path](../abap-glossary/abencte_association_path_glosry.md), or a [CDS/CTE association path](../abap-glossary/abencds_cte_assoc_path_glosry.md) in [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) or [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). A SQL path expression can be used as a data source, or for specifying a [SQL path target field](../abap-glossary/abensql_target_field_glosry.md) in an operand position. For this, [CDS associations](../abap-glossary/abencds_association_glosry.md) and [CTE associations](../abap-glossary/abencte_association_glosry.md) are implicitly transformed into [joins](../abap-glossary/abenjoin_glosry.md). See

- [Path Expression in CDS](abap-cds-data-definitions/abencds_path_expression_v2.md)

- [Path Expression in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_path.md).

**SQL path target field**

A field that is specified behind a [SQL path expression](../abap-glossary/abensql_path_expression_glosry.md).

**SQL-based scalar function**

[CDS scalar function](../abap-glossary/abencds_scalar_function_glosry.md) that is evaluated by an SQL environment. SQL-based scalar functions can be used in [CDS view entities](../abap-glossary/abencds_v2_view_glosry.md) in operand positions that expect scalar values.

SQL-based scalar functions can be [user-defined functions](../abap-glossary/abencds_user_func_glosry.md) or [system functions](../abap-glossary/abencds_system_func_glosry.md).

A CDS scalar function consists of three development objects:

- A [CDS entity](../abap-glossary/abencds_entity_glosry.md) defined using [`DEFINE SCALAR FUNCTION`](abap-cds-data-definitions/abencds_define_scalar_function.md) in a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md).

- A [scalar function implementation reference](abap-cds-data-definitions/abencds_scalar_func_impl_ref.md) that binds the scalar function to the SQL environment and to an [AMDP function implementation](../abap-glossary/abenamdp_function_method_glosry.md).

- An [AMDP function](../abap-glossary/abenamdp_function_glosry.md) that implements the scalar function as [database function](../abap-glossary/abendatabase_function_glosry.md).

**standalone data type**

A [data type](../abap-glossary/abendata_type_glosry.md) that is defined using the statement [`TYPES`](../abap-programming-language/abap-declarations/abaptypes.md) in an [ABAP program](../abap-glossary/abenabap_program_glosry.md), as a data type of the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) or as a [CDS entity](../abap-glossary/abencds_entity_glosry.md). See also [bound data type](../abap-glossary/abenbound_data_type_glosry.md).

**static cache**

A static cache improves performance when a view is repeatedly accessed on an SAP HANA database. Called a [*static result cache*](https://help.sap.com/docs/SAP_HANA_PLATFORM/bed8c14f9f024763b0777aa72b5436f6/8ea43b3ff2e541e398e27d7e5caefab7) on SAP HANA. The cache is kept stable for a predefined retention time, and invalidated when this time is over.

**static external entity**

A [CDS external entity](../abap-glossary/abencds_external_entity_glosry.md) that uses the addition `PROVIDED BY` to specify a [logical external schema](../abap-glossary/abencds_logical_schema_glosry.md) in its [data definition](../abap-glossary/abencds_data_definition_glosry.md). Static external entities can be used as data sources in [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) `SELECT` statements, in other [CDS entities](../abap-glossary/abencds_entity_glosry.md), and in [ABAP Managed Database Procedures](../abap-glossary/abenabap_managed_db_proc_glosry.md) (AMDP).

**string literal**

Either [text string literal](../abap-glossary/abentext_string_literal_glosry.md) or [byte string literal](../abap-glossary/abenbyte_string_literal_glosry.md).

**structured type**

[Data type](../abap-glossary/abendata_type_glosry.md) of a [structure](../abap-glossary/abenstructure_glosry.md). It contains other data types as [structure components](../abap-glossary/abenstructure_component_glosry.md). A named structured type is either defined as a [DDIC structure](../abap-glossary/abenddic_structure_glosry.md), a [CDS entity](../abap-glossary/abencds_entity_glosry.md) or inside an [ABAP program](../abap-glossary/abenabap_program_glosry.md) using the statement [`TYPES BEGIN OF`](../abap-programming-language/abap-declarations/abaptypes_struc.md).

**sub-annotation**

[CDS annotation](../abap-glossary/abencds_annotation_glosry.md) that is specified in curly brackets `{ }` in an [annotation definition](../abap-glossary/abencds_anno_definition_glosry.md) after another annotation. When specifying a sub-annotation in [annotation syntax](../abap-glossary/abencds_annotation_syntax_glosry.md), curly brackets [`{ }`](abap-cds-annotations/abencds_annotations_syntax.md) or [structured names](abap-cds-annotations/abencds_annotations_syntax_name.md) separated by periods are also used.

**table buffering**

[Buffering](../abap-glossary/abensap_buffering_old_glosry.md) of data from [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md), [DDIC database views](../abap-glossary/abendatabase_view_glosry.md), or from [CDS entities](../abap-glossary/abencds_entity_glosry.md) in a [table buffer](../abap-glossary/abentable_buffer_glosry.md) in the [shared memory](../abap-glossary/abenshared_memory_glosry.md) of the current [AS instance](../abap-glossary/abenas_instance_glosry.md). Whether and how a DDIC database table or a DDIC database view is buffered is determined by its [technical settings](../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_buffer.md). For a CDS entity, the buffering is determined by annotations and a [CDS entity buffer](../abap-glossary/abencds_entity_buffer_glosry.md). Buffering is managed by the [database interface](../abap-glossary/abendatabase_interface_glosry.md). Table buffering is applied implicitly when the database is accessed using [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and from classic dynpros. In ABAP SQL, the [ABAP SQL in-memory engine](../abap-glossary/abenabap_sql_inmemeng_glosry.md) processes the tabular data in the table buffer.

**text field literal**

A [character literal](../abap-glossary/abencharacter_literal_glosry.md) of the [text field type](../abap-glossary/abentext_field_type_glosry.md) [`c`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) or [`CHAR`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the length of the specified characters. A text field literal can be linked to a [text symbol](../abap-glossary/abentext_symbol_glosry.md).

- In general ABAP, text field literals are [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md) delimited by single quotes.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), text field literals can be [typed literals](../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Character Literals in ABAP](../abap-programming-language/abap-declarations/abenuntyped_character_literals.md)

- [Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_literals.md)

- [Literals in CDS](abap-cds-data-definitions/abencds_literal_v2.md)

**text literal**

*-\>* [Character literal](../abap-glossary/abencharacter_literal_glosry.md)

**text string literal**

A [character literal](../abap-glossary/abencharacter_literal_glosry.md) of the [text string](../abap-glossary/abentext_string_type_glosry.md) type [`string`](../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md).

- In general ABAP, text string literals are [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md) delimited by backquotes.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), text string literals can be [typed literals](../abap-glossary/abentyped_literal_glosry.md) or [untyped literals](../abap-glossary/abenuntyped_literal_glosry.md).

See also:

- [Character Literals in ABAP](../abap-programming-language/abap-declarations/abenuntyped_character_literals.md)

- [Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_literals.md)

- [Literals in CDS](abap-cds-data-definitions/abencds_literal_v2.md)

**time literal**

A [literal](../abap-glossary/abenabap_literal_glosry.md) of the data type [`TIMN`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`TIMS`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Not available in general ABAP.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), time literals are available as [typed literals](../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](abap-cds-data-definitions/abencds_typed_literal_v2.md)

**time stamp literal**

A [literal](../abap-glossary/abenabap_literal_glosry.md) of the data type [`UTCLONG`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Not available in general ABAP.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), time stamp literals are available as [typed literals](../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](abap-cds-data-definitions/abencds_typed_literal_v2.md)

**tuning object**

A [repository object](../abap-glossary/abenrepository_object_glosry.md) that defines technical settings for certain repository objects. A tuning object can be defined and transported separately from the repository object for which it is defined. The following types of tuning objects are currently available:

- [HANA tuning objects](../abap-glossary/abenhana_tuning_object_glosry.md) defined in the [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md) in [DDIC DDL](../abap-glossary/abenddic_dcl_glosry.md).

- [ABAP tuning objects](../abap-glossary/abenabap_tuning_object_glosry.md) defined as [CDS objects](../abap-glossary/abencds_object_glosry.md) in [CDS DDL](../abap-glossary/abencds_ddl_glosry.md).

**typed literal**

A [literal](../abap-glossary/abenliteral_glosry.md) whose [data type](../abap-glossary/abendata_type_glosry.md) is specified explicitly.

See also [untyped literal](../abap-glossary/abenuntyped_literal_glosry.md).

**unit key literal**

A [literal](../abap-glossary/abenabap_literal_glosry.md) of the data type [`UNIT`](../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) that contains a [unit key](../abap-glossary/abenunit_glosry.md).

- Not available in general ABAP.

- In [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), unit key literals are available as [typed literals](../abap-glossary/abentyped_literal_glosry.md).

See also:

- [Typed Literals in ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql_typed_literals.md)

- [Typed Literals in CDS](abap-cds-data-definitions/abencds_typed_literal_v2.md)

**user condition**

Part of an [access condition](../abap-glossary/abenaccess_condition_glosry.md) in a [CDS role](../abap-glossary/abencds_role_glosry.md) that compares an element of a [CDS entity](../abap-glossary/abencds_entity_glosry.md) with the current [user name](../abap-glossary/abenuser_name_glosry.md).

**writable CDS external entity**

A [dynamic external entity](../abap-glossary/abencds_dynamic_ee_glosry.md) that allows modifying data on an external database system using the [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) [`INSERT`](../abap-programming-language/abap-database-access/abapinsert_dbtab.md), [`UPDATE`](../abap-programming-language/abap-database-access/abapupdate.md), [`MODIFY`](../abap-programming-language/abap-database-access/abapmodify_dbtab.md), and [`DELETE`](../abap-programming-language/abap-database-access/abapdelete_dbtab.md) operations. It is defined using the statement [`WRITABLE`](abap-cds-data-definitions/abencds_writable_ee.md) in the [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md). An [ABAP SQL connection object](../abap-glossary/abenabap_sql_conn_obj_glosry.md) is required to establish a [service connection](../abap-glossary/abenservice_connection_glosry.md) and enable the [logical external schema](../abap-glossary/abencds_logical_schema_glosry.md) for write access.

**writable CDS view entity**

A [CDS view entity](../abap-glossary/abencds_v2_view_glosry.md) that allows modifying data on the database using the [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) [`INSERT`](../abap-programming-language/abap-database-access/abapinsert_dbtab.md), [`UPDATE`](../abap-programming-language/abap-database-access/abapupdate.md), [`MODIFY`](../abap-programming-language/abap-database-access/abapmodify_dbtab.md), and [`DELETE`](../abap-programming-language/abap-database-access/abapdelete_dbtab.md) operations. Defined using the statement [`WRITABLE`](abap-cds-data-definitions/abencds_define_wrtbl_view_v2.md).

**writable database object**

A [repository object](../abap-glossary/abenrepository_object_glosry.md) that allows modifying data on the database.

- In [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md), [CDS table entities](../abap-glossary/abencds_table_entity_glosry.md), [writable CDS view entities](../abap-glossary/abenwritable_v2_glosry.md), and [writable CDS external entities](../abap-glossary/abenwritable_ee_glosry.md) allow for the modification of data with the [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) statements [`INSERT`](../abap-programming-language/abap-database-access/abapinsert_dbtab.md), [`UPDATE`](../abap-programming-language/abap-database-access/abapupdate.md), [`MODIFY`](../abap-programming-language/abap-database-access/abapmodify_dbtab.md), and [`DELETE`](../abap-programming-language/abap-database-access/abapdelete_dbtab.md).

- In [ABAP Dictionary](../abap-glossary/abenabap_dictionary_glosry.md), [DDIC database tables](../abap-glossary/abenddic_db_table_glosry.md) and DDIC table views allow data change operations.
