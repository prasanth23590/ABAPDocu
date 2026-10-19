---
title: "News for ABAP Release 7.65"
source_file: abennews-765.html
section: "ABAP Release News > News for ABAP Release 7.6x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.65

The kernel release for ABAP release 7.65 is 7.49.

## Enumerated Types

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Enumerated Types</strong></td>
<td><p>The statement <a href="abaptypes_enum.html"><code class="ph codeph">TYPES BEGIN OF ENUM</code></a> can be used to define <a href="abenenumerated_type_glosry.html">enumerated types</a> for <a href="abenenumerated_variable_glosry.html">enumerated variables</a>, which can have only <a href="abenenumerated_value_glosry.html">enumerated values</a> defined for this type.</p>
<p>The document <a href="abenenumerated_types_usage.html">Enumerated Objects</a> summarizes the properties of enumerated types and enumerated objects.</p></td>
</tr>
</tbody>
</table>

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
<td><strong>Common Table Expressions</strong></td>
<td>The new ABAP SQL statement <a href="abapwith.html"><code class="ph codeph">WITH</code></a> enables <a href="abencommon_table_expression_glosry.html">common table expressions</a> (CTEs) to be defined for use in the <code class="ph codeph">WITH</code> statement. A common table expression creates a result set that is used in the queries of the <code class="ph codeph">WITH</code> statement as a data source. The <a href="abenmainquery_glosry.html">main query</a> of the <code class="ph codeph">WITH</code> statement has an <code class="ph codeph">INTO</code> clause and transfers its result set to ABAP data objects.</td>
</tr>
<tr class="even">
<td><strong>Cross Join</strong></td>
<td>As well as an inner and outer join, it is now possible to use a <a href="abapselect_join.html">cross join</a> in a <a href="abapselect.html"><code class="ph codeph">SELECT</code> statement</a>.</td>
</tr>
<tr class="odd">
<td><strong>SQL Functions</strong></td>
<td><p>The following changes have been made:</p>
<ul>
<li>The new numeric function <a href="abensql_arith_func.html"><code class="ph codeph">DIVISION</code></a> enables divisions with decimal places.</li>
<li>The new string functions <a href="abensql_string_func.html"><code class="ph codeph">LOWER</code></a> and <a href="abensql_string_func.html"><code class="ph codeph">UPPER</code></a> implement uppercase and lowercase.</li>
<li>The new date functions <a href="abensql_date_func.html"><code class="ph codeph">DATS_IS_VALID</code></a>, <a href="abensql_date_func.html"><code class="ph codeph">DATS_DAYS_BETWEEN</code></a>, <a href="abensql_date_func.html"><code class="ph codeph">DATS_ADD_DAYS</code></a> and <a href="abensql_date_func.html"><code class="ph codeph">DATS_ADD_MONTHS</code></a> execute operations with date fields.</li>
<li>An addition <a href="abapselect_avg_as.html"><code class="ph codeph">AS dtype</code></a> can now be specified in the aggregate function <a href="abapselect_aggregate.html"><code class="ph codeph">AVG</code></a> to define the data type of the result.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Restrictions Removed</strong></td>
<td><p>The following restrictions were removed:</p>
<ul>
<li>The addition <a href="abaporderby_clause.html"><code class="ph codeph">ORDER BY PRIMARY KEY</code></a> of the <a href="abapselect.html"><code class="ph codeph">SELECT</code></a> statement can now also be specified if a column is specified multiple times in the <a href="abapselect_list.html"><code class="ph codeph">SELECT</code></a> list, without the same name being blocked by alternative names.</li>
</ul></td>
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
<td><strong>Metadata Extensions</strong></td>
<td><a href="abencds_meta_data_extensions.html">Metadata extensions</a> are new <a href="abencds_object_glosry.html">CDS objects</a> that allow <a href="abencds_annotation_glosry.html">CDS annotations</a> for a <a href="abencds_object_glosry.html">CDS entity</a> to be created and transported separately from their <a href="abenddl_source_code_glosry.html">DDL source code</a>.</td>
</tr>
<tr class="even">
<td><strong>Annotations</strong></td>
<td>For each <a href="abencds_f1_element_annotation.html">element annotation</a> that is not part of an <a href="abenannotation_array_glosry.html">annotation array</a>, the special value <a href="abencds_annotations_syntax_value.html"><code class="ph codeph">null</code></a> can be specified (without quotation marks).</td>
</tr>
<tr class="odd">
<td><strong>Cross Join</strong></td>
<td>As well as an inner and outer join, it is now possible to use a <a href="abencds_joined_data_source_v1.html">cross join</a> in a <a href="abencds_select_statement_v1.html"><code class="ph codeph">SELECT</code> statement</a>.</td>
</tr>
<tr class="even">
<td><strong>Expressions and Functions</strong></td>
<td><p>The following enhancements have been implemented:</p>
<ul>
<li><a href="abencds_aggregate_functions_v1.html">Aggregate expressions</a> can now be used as operands in a <a href="abencds_cast_expression_v1.html"><code class="ph codeph">CAST</code> expression</a>.</li>
<li>In a <a href="abencds_cast_expression_v1.html"><code class="ph codeph">CAST</code> expression</a>, the data types <code class="ph codeph">CHAR</code>, <code class="ph codeph">SSTR</code>, and <code class="ph codeph">NUMC</code> can now be cast to <code class="ph codeph">ACCP</code>, and the other way round.</li>
<li>The following additional string functions are now supported: <a href="abencds_sql_functions_character_v1.html"><code class="ph codeph">UPPER</code></a> and <a href="abencds_sql_functions_character_v1.html"><code class="ph codeph">LOWER</code></a></li>
<li>The following additional date/time functions are now supported: <a href="abencds_timezone_functions_v1.html"><code class="ph codeph">ABAP_SYSTEM_TIMEZONE</code></a>, <a href="abencds_timezone_functions_v1.html"><code class="ph codeph">ABAP_USER_TIMEZONE</code></a>, <a href="abencds_date_time_conversions_v1.html"><code class="ph codeph">TSTMP_TO_DATS</code></a>, <a href="abencds_date_time_conversions_v1.html"><code class="ph codeph">TSTMP_TO_TIMS</code></a>, <a href="abencds_date_time_conversions_v1.html"><code class="ph codeph">TSTMP_TO_DST</code></a>, and <a href="abencds_date_time_conversions_v1.html"><code class="ph codeph">DATS_TIMS_TO_TSTMP</code></a></li>
<li>An addition <a href="abencds_avg_as_v1.html"><code class="ph codeph">AS dtype</code></a> can now be specified for the <a href="abencds_aggregate_functions_v1.html">aggregate expression</a> <code class="ph codeph">AVG</code> to determine the data type of the return value.</li>
<li>A new built-in conversion function <a href="abencds_conv_func_types_v1.html"><code class="ph codeph">FLTP_TO_DEC</code></a> can be used to convert arguments of type <code class="ph codeph">FLTP</code> to packed numbers.</li>
<li><a href="abencds_builtin_functions_v1.html">Built-in functions</a> can now be specified on the right side of a <a href="abencds_conditional_expression_v1.html"><code class="ph codeph">cds_cond</code></a> condition of a <a href="abencds_cond_expr_where_v1.html"><code class="ph codeph">WHERE</code> condition</a>, an <a href="abencds_joined_data_source_v1.html"><code class="ph codeph">ON</code> condition</a>, a <a href="abencds_cond_expr_filter_v1.html">filter condition</a>, or a <a href="abencds_cond_expr_case_v1.html">complex case distinction</a>.</li>
<li><p>In <a href="abencds_conditional_expression_v1.html"><code class="ph codeph">cds_cond</code></a> conditions, fields of data sources of the type <code class="ph codeph">ACCP</code> can now be <a href="abencds_cond_expr_types_v1.html">compared</a> with fields of the same type, and with literals of the type <code class="ph codeph">NUMC</code>.</p>
<p>A <a href="abencds_literal_v1.html">literal</a> of a corresponding value is not handled as a field of type <code class="ph codeph">INT8</code>. An exception to this are literals in the definition of CDS associations.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Access Control</strong></td>
<td><p>The following enhancements have been implemented in <a href="abencds_access_control_glosry.html">CDS access control</a>:</p>
<ul>
<li>As well as <a href="abencds_dcl_role_cond_rule.html">conditional access rules</a>, there are now also <a href="abencds_dcl_role_grant_rule.html">full access rules</a>.</li>
<li>There is a new operator <code class="ph codeph">?=</code> for <a href="abencds_dcl_role_conditions.html">access conditions</a>, which checks not only for a specified value but also the initial value or the null value.</li>
<li>A new <a href="abencds_f1_cond_user.html">user condition</a> compares the value of an element of a CDS entity with the current user name.</li>
</ul></td>
</tr>
</tbody>
</table>
