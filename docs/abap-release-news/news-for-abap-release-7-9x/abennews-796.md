---
title: "News for ABAP Release 7.96"
source_file: abennews-796.html
section: "ABAP Release News > News for ABAP Release 7.9x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.96

The kernel release for ABAP release 7.96 is 7.96.

## ABAP CDS

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Extended Cast Matrix</strong></td>
<td>In <a href="abencds_v2_view_glosry.html">CDS view entities</a> and in <a href="abencds_v1_view_glosry.html">CDS DDIC-based views (obsolete)</a>, <a href="abencds_cast_expression_v2.html">casting</a> from the data type <code class="ph codeph">CURR</code> into the data types <code class="ph codeph">DECFLOAT16</code> and <code class="ph codeph">DECFLOAT34</code> is now possible.</td>
</tr>
<tr class="even">
<td><strong>New Analytical Scalar Functions</strong></td>
<td><p>The following <a href="abencds_ana_scalar_glosry.html">analytical scalar functions</a> are available as of ABAP release 7.96:</p>
<ul>
<li><a href="abencds_ana_scalar_function.html"><code class="ph codeph">LN</code></a></li>
<li><a href="abencds_ana_scalar_function.html"><code class="ph codeph">LOG</code></a></li>
<li><a href="abencds_ana_scalar_function.html"><code class="ph codeph">EXPONENTIAL</code></a></li>
<li><p><a href="abencds_ana_scalar_function.html"><code class="ph codeph">POWER</code></a></p>
<p>For a complete list, see the topic <a href="abencds_ana_scalar_function.html">ABAP CDS - Analytical Scalar Functions</a>.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>CDS Enumerated Elements in CDS Conditions</strong></td>
<td><a href="abencds_enum_element_glosry.html">CDS enumerated elements</a> are now also supported as left-hand operands in <a href="abenlogical_expression_glosry.html">logical expressions</a>. For more details, see the topic <a href="abencds_use_enum_type.html">CDS DDL - Using CDS Enumerated Types</a>.</td>
</tr>
<tr class="even">
<td><strong>Support of Data Types in Logical Expressions with <code class="ph codeph">IS INITIAL</code></strong></td>
<td>In logical expressions with the operator <a href="abencds_cond_expr_initial_v2.html"><code class="ph codeph">INITIAL</code></a>, the left-hand operand can now also have one of the following data types: <code class="ph codeph">RAW</code>, <code class="ph codeph">DECFLOAT16</code>, <code class="ph codeph">DECFLOAT34</code>, <code class="ph codeph">DATN</code>, <code class="ph codeph">TIMN</code>, <code class="ph codeph">UTCL</code>. This applies to all CDS entities except for <a href="abencds_v1_view_glosry.html">CDS DDIC-based view</a>.</td>
</tr>
</tbody>
</table>

## ABAP Objects

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Visibility Sections</strong></td>
<td><p>For technical reasons a <a href="abenglobal_class_glosry.html">global class</a> that can be part of an inheritance tree that is - a <a href="abensubclass_glosry.html">subclass</a> - a non-<a href="abenfinal_glosry.html">final</a> class that is not a subclass but can be a <a href="abensuperclass_glosry.html">superclass</a></p>
<p>must contain the statements <a href="abapprotected.html"><code class="ph codeph">PROTECTED SECTION</code></a> and <a href="abapprivate.html"><code class="ph codeph">PRIVATE SECTION</code></a> also for empty protected and private sections.</p>
<p>Before Release 7.96, a syntax warning occurred in case of missing protected and private sections only for non-final classes. Now the warning occurs also for final subclasses.</p></td>
</tr>
</tbody>
</table>

## Expressions

| Modification                                              | Description                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **String Expressions in `VALUE` Operator**                | String expressions can now directly be assigned to incompatible components without using `CONV` in assignments to [structure components](../../abap-programming-language/abap-creating-objects-and-values/abenvalue_constructor_params_struc.md): `VALUE ...( comp = strg_expr )` vs. `VALUE ...( comp = CONV #( strg_expr ) )`.                                                                                                                                         |
| **`FOR GROUPS ... OF` Supported for `NEW`**               | The variant [`FOR GROUPS ... OF`](../../abap-programming-language/abap-processing-internal-data/abenfor_groups_of.md) of the iteration expression [`FOR`](../../abap-programming-language/abap-program-flow-logic/abenfor.md) is now also supported for the constructor operator [`NEW`](../../abap-programming-language/abap-creating-objects-and-values/abennew_constructor_params_itab.md).                                                                                                                                                                                             |
| **Syntax Warning for Multiple Assignments of Components** | In the constructor operators [`NEW`](../../abap-programming-language/abap-creating-objects-and-values/abennew_constructor_params_struct.md) and [`VALUE`](../../abap-programming-language/abap-creating-objects-and-values/abenvalue_constructor_params_struc.md) for structures, it is not allowed to assign multiple values to a component. This leads to a syntax error, if the component is directly named. It leads now also to a syntax warning in cases, where [component groups](../../abap-glossary/abencomponent_group_glosry.md) are involved. |

## ABAP SQL

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Dynamic <code class="ph codeph">SELECT</code></strong></td>
<td>The new dynamic forms of the statements <a href="abapwith.html"><code class="ph codeph">WITH</code></a> enable fully dynamic <code class="ph codeph">SELECT</code> statements, where all clauses except the <code class="ph codeph">INTO</code> clause and the ABAP-specific additions can be specified in one dynamic token.</td>
</tr>
<tr class="even">
<td><strong><code class="ph codeph">ORDER BY n</code></strong></td>
<td>In the <a href="abaporderby_clause.html">column list</a> of the <a href="abaporderby_clause.html"><code class="ph codeph">ORDER BY</code></a> clause, a literal or a host constant of an integer type is handled as the column position in the result set of the query. This feature is available since the introduction of SQL expressions in the <a href="abaporderby_clause.html"><code class="ph codeph">ORDER BY</code></a> clause with release 7.89 but was undocumented and behaved partly undefined. With release 7.95 the behavior is defined and documented.</td>
</tr>
<tr class="odd">
<td><strong><code class="ph codeph">OPTIONS</code></strong></td>
<td>A new addition <a href="abapselect_options.html"><code class="ph codeph">OPTIONS</code></a> can and should be used in front of the ABAP-specific additions <a href="abapselect_privileged_access.html"><code class="ph codeph">PRIVILEGED ACCESS</code></a>, <a href="abapselect_bypassing_buffer.html"><code class="ph codeph">BYPASSING BUFFER</code></a> at the end of the statement <a href="abapselect.html"><code class="ph codeph">SELECT</code></a>.</td>
</tr>
<tr class="even">
<td><strong><code class="ph codeph">PROVIDED BY</code></strong></td>
<td>A new addition <a href="abapselect_data_source.html"><code class="ph codeph">PROVIDED BY</code></a> to the <a href="abapselect_data_source.html">data source</a> of the <a href="abapfrom_clause.html"><code class="ph codeph">FROM</code></a> clause specifies a <a href="abencds_logical_schema_glosry.html">logical external schema</a> in order to map a <a href="abencds_external_entity_glosry.html">CDS external entity</a> to an external system.</td>
</tr>
<tr class="odd">
<td><strong>Syntax Warning for Replacement Objects</strong></td>
<td>Each ABAP SQL access to a DDIC database table or a DDIC database view with a <a href="abenreplacement_object_glosry.html">replacement object</a> produces a syntax check warning that can be suppressed by the pragma <code class="ph codeph">##open_sql_redirect_dml[...]</code>. The pragma is used to highlight such accesses in the code and indicates the special rules that must be observed for them. Before release 7.96, only write accesses led to warnings.</td>
</tr>
<tr class="even">
<td><strong>CDS Scalar Functions</strong></td>
<td><a href="abencds_scalar_function_glosry.html">CDS scalar functions</a> can be used as <a href="abensql_expression_glosry.html">SQL expressions</a> at all operand positions where expressions are allowed.</td>
</tr>
<tr class="odd">
<td><strong>Client Parameter in SQL Functions</strong></td>
<td><p>In the following built-in functions, the optional formal parameter <code class="ph codeph">client</code> must not be used in language version ABAP for Cloud Development any more:</p>
<ul>
<li><a href="abensql_curr_unit_conv_func.html"><code class="ph codeph">UNIT_CONVERSION</code></a></li>
<li><a href="abensql_curr_unit_conv_func.html"><code class="ph codeph">CURRENCY_CONVERSION</code></a></li>
<li><a href="abensql_timezone_func.html"><code class="ph codeph">ABAP_SYSTEM_TIMEZONE</code></a></li>
<li><a href="abensql_timezone_func.html"><code class="ph codeph">ABAP_USER_TIMEZONE</code></a></li>
<li><a href="abensql_date_time_conversions.html"><code class="ph codeph">TSTMP_TO_DATS</code></a></li>
<li><a href="abensql_date_time_conversions.html"><code class="ph codeph">TSTMP_TO_TIMS</code></a></li>
<li><a href="abensql_date_time_conversions.html"><code class="ph codeph">TSTMP_TO_DST</code></a></li>
<li><a href="abensql_date_time_conversions.html"><code class="ph codeph">DATS_TIMS_TO_TSTMP</code></a></li>
</ul>
<p>Only the <a href="abencurrent_client_glosry.html">current client</a> as the default value of the parameter must be used in these functions. Passing an explicit client leads to a syntax warning and later to a syntax error.</p></td>
</tr>
</tbody>
</table>

## AMDP

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>New AMDP Option <code class="ph codeph">CDS SESSION CLIENT DEPENDENT</code></strong></td>
<td><p>The new addition <a href="abapmethods_amdp_options_client.html"><code class="ph codeph">CDS SESSION CLIENT DEPENDENT</code></a> can be used after <a href="abapmethods_amdp_options.html"><code class="ph codeph">AMDP OPTIONS</code></a> to set the HANA session variable <code class="ph codeph">CDS_CLIENT</code> to its default value and to declare the <a href="abenamdp_method_glosry.html">AMDP method</a> explicitly as <a href="abenclient_dependent_glosry.html">client-dependent</a> and to make it <a href="abenclient_safe_glosry.html">client-safe</a>.</p>
<p>The addition can be also used as an option after <a href="abapclass-methods_for_ddl_object.html"><code class="ph codeph">FOR DDL</code></a>.</p></td>
</tr>
<tr class="even">
<td><strong>Client Safety of AMDP Methods</strong></td>
<td>In order to support the concept of <a href="abenclient_isolation_glosry.html">client isolation</a>, AMDP methods can be made <a href="abenamdp_client_safety.html">client-safe</a>. This is mandatory for <a href="abenabap_for_cloud_dev_glosry.html">ABAP for Cloud Development</a>.</td>
</tr>
</tbody>
</table>

## ABAP RESTful Application Programming Model

In release 7.96, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RAP Business Events for Child Entities</strong></td>
<td><a href="abenrap_entity_event_glosry.html">RAP business events</a> can now also be defined for <a href="abenchild_entity_glosry.html">CDS child entities</a>. Up to now, a RAP business event could only be defined for the <a href="abenroot_node_glosry.html">root node</a> of a <a href="abenrap_bo_glosry.html">RAP business object</a>.</td>
</tr>
<tr class="even">
<td><strong>Subentities as Authorization Master</strong></td>
<td>You can now define <a href="abenrap_bo_entity_glosry.html">RAP BO entities</a> as <a href="abenrap_auth_ma_ent_glosry.html">RAP authorization master entity</a> that are not defined as <a href="abenrap_bo_root_entity_glosry.html">root entity</a>.</td>
</tr>
<tr class="odd">
<td><strong>Result Multiplicity in Factory Actions</strong></td>
<td><p><a href="abenrap_factory_action_glosry.html">RAP factory actions</a> now allow result multiplicity. This means that the cardinality can have one of the following values:</p>
<ul>
<li><a href="abenbdl_action_factory.html"><code class="ph codeph">[0..*]</code></a></li>
<li><p><a href="abenbdl_action_factory.html"><code class="ph codeph">[1..*]</code></a></p>
<p>A factory action can be used to create none, one, or any number of <a href="abenrap_bo_entity_inst_glosry.html">entity instances</a>.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>RAP Key Functions</strong></td>
<td><a href="abenrap_key_function_glosry.html">RAP key functions</a> are now available. A RAP key function is defined with reference to a <a href="abenrap_alternative_key_glosry.html">BDEF alternative key</a> and it returns the entity instances with matching values.</td>
</tr>
</tbody>
</table>

### ABAP EML

| Modification                                  | Description                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Commits in the Context of RAP Projections** | Regarding commits in the context of RAP projections behavior definitions (or RAP interface behavior definitions): RAP BO instances that fail to be committed in the RAP save sequence for the base RAP BO are returned to the RAP BO consumer. The messages in the `failed` RAP response parameter are automatically mapped to projections. |
