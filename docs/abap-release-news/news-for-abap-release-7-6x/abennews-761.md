---
title: "News for ABAP Release 7.61"
source_file: abennews-761.html
section: "ABAP Release News > News for ABAP Release 7.6x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.61

The kernel release for ABAP release 7.61 is 7.44.

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
<td><strong>SQL Expressions</strong></td>
<td>From ABAP release 7.61, other <a href="abapsql_expr.html">SQL expressions</a> can be used as operands in a <a href="abensql_cast.html">cast expression</a> and <code class="ph codeph">FLTP</code> is not the only data type that can be specified.</td>
</tr>
<tr class="even">
<td><strong><code class="ph codeph">ON</code> Conditions</strong></td>
<td><p>From ABAP release 7.61, it is possible to</p>
<ul>
<li>Use <a href="abensql_expression_glosry.html">SQL expressions</a> of the left side of the <a href="abapselect_join.html"><code class="ph codeph">ON</code></a> condition of any join.</li>
<li>Use the expression <a href="abenwhere_logexp_null.html"><code class="ph codeph">IS [NOT] NULL</code></a> in an <a href="abapselect_join.html"><code class="ph codeph">ON</code></a> condition of an outer join.</li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Unions</strong></td>
<td>As of ABAP release 7.61, the <a href="abencds_set_operators_glosry.html">set operator</a> <a href="abapunion.html"><code class="ph codeph">UNION</code></a> can also be used in <a href="abensubquery_glosry.html">subqueries</a>.</td>
</tr>
<tr class="even">
<td><strong>Host Expressions</strong></td>
<td>From ABAP release 7.61, <a href="abenabap_sql_host_expressions.html">host expressions</a> can also be specified as an operand <code class="ph codeph">n</code> after <a href="abapselect_up_to_offset.html"><code class="ph codeph">UP TO</code></a> and <a href="abapinto_clause.html"><code class="ph codeph">PACKAGE SIZE</code></a> in the <a href="abapselect.html"><code class="ph codeph">SELECT</code></a> statement.</td>
</tr>
<tr class="odd">
<td><strong>Access to CDS Entities</strong></td>
<td><p>From ABAP release 7.61, the new <a href="abencds_table_function_glosry.html">CDS table functions</a> can also be specified as data sources of a <a href="abapselect.html"><code class="ph codeph">SELECT</code></a> statement alongside <a href="abencds_view_glosry.html">CDS views</a>.</p>
<p>If an input parameter of a <a href="abencds_entity_glosry.html">CDS entity</a> is annotated with the new annotation <a href="abencds_f1_parameter_annotations.html"><code class="ph codeph">@Environment.systemField</code></a>, ABAP SQL can pass the system value that matches the value of the annotation implicitly. The <a href="abenannotation_value_glosry.html">annotation value</a> <a href="abencds_f1_parameter_annotations.html"><code class="ph codeph">#CLIENT</code></a> even prevents an actual parameter from being passed to input parameters explicitly that are annotated in this way for client IDs.</p></td>
</tr>
<tr class="even">
<td><strong>Arrangement of <code class="ph codeph">SELECT</code> Clauses and <code class="ph codeph">FROM</code> Clauses</strong></td>
<td>From ABAP release 7.61, the <a href="abapfrom_clause.html"><code class="ph codeph">FROM</code> clause</a> of a <a href="abapselect.html"><code class="ph codeph">SELECT</code> statement</a> can also be specified in front of the <a href="abapselect_clause.html"><code class="ph codeph">SELECT</code> clause</a>. In this case, the <code class="ph codeph">SELECT</code> clause must be introduced using the new addition <a href="abapselect.html"><code class="ph codeph">FIELDS</code></a>. This arrangement supports tools such as Code Completion.</td>
</tr>
</tbody>
</table>

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
<td><strong>CDS Table Functions</strong></td>
<td>The new CDS DDL statement <a href="abencds_f1_define_table_function.html"><code class="ph codeph">DEFINE TABLE FUNCTION</code></a> can be used to define <a href="abencds_table_function_glosry.html">CDS table functions</a> as a new category of <a href="abencds_entity_glosry.html">CDS entities</a>. In platform-dependent SQL, a CDS table function is implemented in an associated <a href="abenamdp_function_method_glosry.html">AMDP function implementation</a>.</td>
</tr>
<tr class="even">
<td><strong>Annotation for Input Parameters</strong></td>
<td>An <a href="abencds_f1_param.html">input parameter</a> of a <a href="abencds_view_glosry.html">CDS view</a> or a <a href="abencds_table_function_glosry.html">CDS table function</a> can now be annotated with an annotation <a href="abencds_f1_parameter_annotations.html"><code class="ph codeph">@Environment.systemField</code></a>. The potential values of the annotation assign ABAP system fields to the input parameters. If a <a href="abencds_entity_glosry.html">CDS entity</a> of this type is used a <a href="abapselect_data_source.html">data source</a> in ABAP SQL, the assigned values can be passed implicitly. In particular, the value <a href="abencds_f1_parameter_annotations.html"><code class="ph codeph">#CLIENT</code></a> enables the client ID of the <a href="abencurrent_client_glosry.html">current client</a> to be passed implicitly, which provides support for client handling in platform-dependent SQL of the implementation of a CDS table function.</td>
</tr>
<tr class="odd">
<td><strong>API for Evaluation of Annotations</strong></td>
<td>The class <code class="ph codeph">CL_DD_DDL_ANNOTATION_SERVICE</code> has been made available for evaluating annotations. It contains methods used to read the <a href="abencds_annotation_glosry.html">annotations</a> of <a href="abencds_entity_glosry.html">CDS entities</a> from the associated system tables.</td>
</tr>
<tr class="even">
<td><strong>Expressions and Functions</strong></td>
<td><p>The following enhancements have been implemented:</p>
<ul>
<li>The new date function <a href="abencds_date_functions_v1.html"><code class="ph codeph">DATS_IS_VALID</code></a> checks the validity of dates.</li>
<li>The new time function <a href="abencds_time_functions_v1.html"><code class="ph codeph">TIMS_IS_VALID</code></a> checks the validity of times.</li>
<li>The new time stamp functions <a href="abencds_timestamp_functions_v1.html"><code class="ph codeph">TSTMP_IS_VALID</code></a>, <a href="abencds_timestamp_functions_v1.html"><code class="ph codeph">TSTMP_CURRENT_UTCTIMESTAMP</code></a>, <a href="abencds_timestamp_functions_v1.html"><code class="ph codeph">TSTMP_SECONDS_BETWEEN</code></a>, and <a href="abencds_timestamp_functions_v1.html"><code class="ph codeph">TSTMP_ADD_SECONDS</code></a> perform operations with UTC <a href="abentime_stamps_packed.html">time stamps in packed numbers</a>.</li>
<li><p><a href="abencds_cast_expression_v1.html"><code class="ph codeph">CAST</code> expressions</a> can now be used to cast operands of the types <code class="ph codeph">DATS</code> and <code class="ph codeph">TIMS</code> to <code class="ph codeph">CHAR</code> (if the length of the target type is sufficient).</p>
<p>The following changes have been made:</p></li>
<li>In <a href="abencds_cast_expression_v1.html"><code class="ph codeph">CAST</code> expressions</a>, the restriction no longer applies that casts of operands of the types <code class="ph codeph">DEC</code>, <code class="ph codeph">CURR</code>, and <code class="ph codeph">QUAN</code> to the same types expect the target type to be long enough. In casts from <code class="ph codeph">NUMC</code> to <code class="ph codeph">NUMC</code>, however, the lengths must now match exactly.</li>
<li>In the <a href="abencds_conversion_functions_v1.html">conversion functions</a> <code class="ph codeph">UNIT_CONVERSION</code> and <code class="ph codeph">DECIMAL_SHIFT</code>, the result type was set to the data type <a href="abenddic_builtin_types.html"><code class="ph codeph">QUAN</code></a> or <a href="abenddic_builtin_types.html"><code class="ph codeph">CURR</code></a> with length 31 and 14 decimal places.</li>
<li>In the function <a href="abencds_date_functions_v1.html"><code class="ph codeph">DATS_ADD_MONTHS</code></a>, an invalid input date is now initialized or set to the value <em>00010101</em> and no longer produces an error.</li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Extensions</strong></td>
<td><p>The statement <a href="abencds_extend_view.html"><code class="ph codeph">EXTEND VIEW</code></a> for <a href="abencds_view_extend_glosry.html">CDS DDIC-based view extensions</a> was expanded as follows:</p>
<ul>
<li><a href="abencds_association_glosry.html">CDS associations</a> for the <code class="ph codeph">SELECT</code> statement of the extended CDS view can now be specified after <code class="ph codeph">EXTEND VIEW</code>.</li>
<li>The following can now be specified in the extension list <code class="ph codeph">select_list_extension</code>:</li>
<li><a href="abencds_parameter_v1.html">Input parameters</a> of the extended CDS view</li>
<li><a href="abencds_path_expression_v1.html">Path expressions</a> for dedicated CDS associations and CDS associations of the extended CDS view</li>
<li><a href="abencds_special_functions_v1.html">Special functions</a></li>
</ul></td>
</tr>
</tbody>
</table>

## AMDP

| Modification                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **AMDP Table Functions**                         | Alongside the existing [AMDP procedures](../../abap-glossary/abenamdp_procedure_glosry.md), the [AMDP](../../abap-glossary/abenamdp_glosry.md) framework now also supports [AMDP table functions](../../abap-glossary/abenamdp_table_function_glosry.md) in the form of [table functions](../../abap-glossary/abentable_function_glosry.md) in the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md). AMDP table functions now have the new addition [`BY DATABASE FUNCTION`](../../abap-programming-language/abap-database-access/abapmethod_by_db_proc.md) of the statement `METHOD` in implementations of [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md) in [AMDP classes](../../abap-glossary/abenamdp_class_glosry.md). These methods are known as [AMDP function implementations](../../abap-glossary/abenamdp_function_method_glosry.md) to distinguish them from the existing [AMDP procedure implementations](../../abap-glossary/abenamdp_procedure_method_glosry.md). Unlike AMDP procedure implementations, AMDP function implementations have a tabular return value, but cannot be called like regular [functional methods](../../abap-glossary/abenfunctional_method_glosry.md) in ABAP. |
| **AMDP Table Functions for AMDP Methods**        | In other [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md) and using the associated SQL syntax, it is possible to access the [AMDP table function](../../abap-glossary/abenamdp_function_glosry.md) of an [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md) with an explicitly defined parameter interface                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **AMDP Table Functions for CDS Table Functions** | An [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md) in whose declaration the addition [`FOR TABLE FUNCTION`](../../abap-programming-language/abap-database-access/abapclass-methods_for_tabfunc.md) is specified implements a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md) from [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md). The parameter interface of an AMDP function implementation of this type is specified by the definition of the CDS table function. The associated [AMDP](../../abap-glossary/abenamdp_table_function_glosry.md) function is executed as a data source of an Open ABAP SQL read statement when accessing the CDS table function directly or indirectly.                                                                                                                                                                                                                                                                                                                                                             |
