---
title: "News for ABAP Release 7.60"
source_file: abennews-760.html
section: "ABAP Release News > News for ABAP Release 7.6x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.60

The kernel release for ABAP release 7.60 is 7.43.

## Expressions and Functions

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Enhanced Type Interference in Constructor Expressions</strong></td>
<td><p>If the character <code class="ph codeph">#</code> is specified for the result type, enhancements were made for the following constructor expressions:</p>
<ul>
<li>In the case of the constructor operator <a href="abenconstructor_expression_reduce.html"><code class="ph codeph">REDUCE</code></a> an attempt is now made to evaluate the first declaration after <code class="ph codeph">INIT</code> if the type of the operand position cannot be identified.</li>
<li>When the constructor expressions</li>
<li><a href="abenconstructor_expression_conv.html"><code class="ph codeph">CONV #( ... )</code></a></li>
<li><a href="abenvalue_constructor_params_init.html"><code class="ph codeph">VALUE #( )</code></a></li>
<li><a href="abenconstructor_expression_reduce.html"><code class="ph codeph">REDUCE #( ... )</code></a></li>
<li><a href="abenconditional_expression_cond.html"><code class="ph codeph">COND #( ... )</code></a></li>
<li><a href="abenconditional_expression_switch.html"><code class="ph codeph">SWITCH #( ... )</code></a> are passed to generically typed formal parameters, no type could be derived for <code class="ph codeph">#</code> from the operand position until now. From ABAP release 7.60, a concrete type is derived for <code class="ph codeph">#</code> for generic formal parameter types where this is possible and feasible if this cannot be determined in any other way. This prevents syntax errors when procedures are called in cases where a previously concrete type of a formal parameter is expanded to a generic type.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Object Component Selector After Table Expressions</strong></td>
<td>From ABAP release 7.60, the <a href="abentable_exp_chaining.html">object component selector <code class="ph codeph">-&gt;</code></a> can be specified directly after <a href="abentable_expressions.html">table expressions</a> that return a reference variable. This makes it possible to access components of the referenced object. An exception are table expressions whose <a href="abentable_exp_result.html">result</a> is determined with the value operator <code class="ph codeph">VALUE</code>.</td>
</tr>
</tbody>
</table>

## Assignments

| Modification                         | Description                                                                                                                                                                                                    |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **System Class for Dynamic Mapping** | The new system class [`CL_ABAP_CORRESPONDING`](../../abap-programming-language/abap-processing-internal-data/abencl_abap_corresponding.md) makes it possible to specify dynamic mapping rules for the component-by-component assignment of structures and internal tables. |

## Exception Classes

| Modification                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **New System Interface for Messages**                    | The new system interface [`IF_T100_DYN_MSG`](../../abap-programming-language/abap-text-repositories/abenif_t100_dyn_msg.md) adds predefined attributes for the message type and the placeholders of the message to the interface [`IF_T100_MESSAGE`](../../abap-programming-language/abap-text-repositories/abenif_t100_message.md). `IF_T100_DYN_MSG` makes it possible to [associate](../../abap-programming-language/abap-program-flow-logic/abenmessage_exceptions.md) any message with exception classes.                                                                                                                                                                                                                                                                                                         |
| **`MESSAGE` Addition for `RAISE EXCEPTION` and `THROW`** | The new addition [`MESSAGE`](../../abap-programming-language/abap-program-flow-logic/abapraise_exception_message.md) of the statement [`RAISE EXCEPTION`](../../abap-programming-language/abap-program-flow-logic/abapraise_exception_class.md) and of the addition [`THROW`](../../abap-programming-language/abap-program-flow-logic/abenconditional_expression_result.md) in a [conditional expression](../../abap-programming-language/abap-program-flow-logic/abenconditional_expressions.md) associates any [message](../../abap-glossary/abenmessage_glosry.md) with an exception object. The exception class in question must include the new system interface [`IF_T100_DYN_MSG`](../../abap-programming-language/abap-text-repositories/abenif_t100_dyn_msg.md). It is also possible to use the addition with exception classes that include only the system interface [`IF_T100_MESSAGE`](../../abap-programming-language/abap-text-repositories/abenif_t100_message.md), but with restrictions. |

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
<td><strong>Unions</strong></td>
<td>From ABAP release 7.60, the set operator <a href="abapunion.html"><code class="ph codeph">UNION</code></a> creates the union of the result sets of two <a href="abapselect.html"><code class="ph codeph">SELECT</code></a> statements.</td>
</tr>
<tr class="even">
<td><strong>SQL Expressions</strong></td>
<td><p>From ABAP release 7.60, <a href="abapsql_expr.html">SQL expressions</a> can be specified in the following operand positions (except in the <code class="ph codeph">SELECT</code> list):</p>
<ul>
<li>Left side of any <a href="abapwhere.html"><code class="ph codeph">WHERE</code></a> condition</li>
<li>Left side of a <a href="abaphaving_clause.html"><code class="ph codeph">HAVING</code></a> condition</li>
<li><p>Left side of a <a href="abensql_searched_case.html">complex case distinction</a></p>
<p>If an SQL expression can be specified, any individual literals, host variables, and host expressions can also be specified.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Host Expressions</strong></td>
<td><p>From ABAP release 7.60, <a href="abenabap_sql_host_variables.html">host expressions</a> with the syntax <code class="ph codeph">@( expr )</code> can be specified in many operand positions in which <a href="abenabap_sql_host_variables.html">host variables</a> are possible. For <code class="ph codeph">expr</code>, all ABAP expressions can calls are possible that can be specified in <a href="abengeneral_expr_position_glosry.html">general expression positions</a>.</p>
<p>Operand positions for host expressions in ABAP release 7.60:</p>
<ul>
<li>Operands of <a href="abapsql_expr.html">SQL expressions</a> and hence all operand positions in which these are possible.</li>
<li>Right sides of <a href="abapwhere.html"><code class="ph codeph">WHERE</code></a>, <a href="abapselect_join.html"><code class="ph codeph">ON</code></a>, or <a href="abaphaving_clause.html"><code class="ph codeph">HAVING</code></a> conditions, except for <code class="ph codeph">LIKE</code> and <code class="ph codeph">IN</code>.</li>
<li><a href="abapselect_data_source.html">Actual parameters</a> for input parameters of CDS views.</li>
<li>Right side of a <a href="abapupdate_set_expression.html"><code class="ph codeph">SET</code> expression</a> in <code class="ph codeph">UPDATE</code>.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Columns Specified After <code class="ph codeph">BETWEEN</code></strong></td>
<td>From ABAP release 7.60, numeric columns can be specified on the right side in an interval condition using <a href="abenwhere_logexp_interval.html"><code class="ph codeph">BETWEEN</code></a>, providing the name of the database table or view is prefixed using <code class="ph codeph">~</code>.</td>
</tr>
<tr class="odd">
<td><strong>Result Type of <code class="ph codeph">COUNT</code></strong></td>
<td>From ABAP release 7.60, the result type of all aggregate functions <a href="abensql_agg_func.html"><code class="ph codeph">COUNT</code></a> is <code class="ph codeph">INT8</code>.</td>
</tr>
<tr class="even">
<td><strong>CDS Path Expressions</strong></td>
<td>From ABAP release 7.60, <a href="abenabap_sql_path.html">path expressions</a> closed with an element can be specified for columns specified in <code class="ph codeph">SELECT</code> statements that access CDS views with <a href="abencds_select_list_association_v1.html">CDS associations exposed</a> for outside use.</td>
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
<td><strong>CDS Access Control</strong></td>
<td><a href="abenabap_cds_glosry.html">ABAP CDS</a> <a href="abencds_access_control_glosry.html">access control</a> was expanded to include implicit evaluations of <a href="abencds_role_glosry.html">CDS roles</a> defined in the <a href="abenabap_cds_glosry.html">ABAP CDS</a> <a href="abencds_f1_dcl_syntax.html">CDS DCL</a> in ABAP SQL. If a <a href="abencds_entity_glosry.html">CDS entity</a> is linked with a CDS role, an additional <a href="abenaccess_condition_glosry.html">access condition</a> is checked by default when the CDS entity is accessed using ABAP SQL. Only that data is read for which the current user has an authorization or that matches a literal condition.</td>
</tr>
<tr class="even">
<td><strong>Expressions and Functions</strong></td>
<td><p>The following enhancements have been implemented:</p>
<ul>
<li>The new SQL functions <a href="abencds_sql_functions_character_v1.html"><code class="ph codeph">LENGTH</code></a>, <a href="abencds_sql_functions_character_v1.html"><code class="ph codeph">LTRIM</code></a>,<a href="abencds_sql_functions_character_v1.html"><code class="ph codeph">RTRIM</code></a>, <a href="abencds_conv_func_types_v1.html"><code class="ph codeph">BINTOHEX</code></a>, and <a href="abencds_conv_func_types_v1.html"><code class="ph codeph">HEXTOBIN</code></a> are available for <a href="abencds_view_glosry.html">CDS views</a>.</li>
<li>The special date functions <a href="abencds_date_functions_v1.html"><code class="ph codeph">DATS_DAYS_BETWEEN</code></a>, <a href="abencds_date_functions_v1.html"><code class="ph codeph">DATS_ADD_DAYS</code></a>, and <a href="abencds_date_functions_v1.html"><code class="ph codeph">DATS_ADD_MONTHS</code></a> make it possible to calculate with values of the built-in dictionary type <a href="abenddic_builtin_types.html"><code class="ph codeph">DATS</code></a> in <a href="abencds_view_glosry.html">CDS views</a>.</li>
<li>Data elements can now be specified as the target type in <a href="abencds_cast_expression_v1.html"><code class="ph codeph">CAST</code> expressions</a> in a <a href="abencds_view_glosry.html">CDS view</a>. This passes the semantic properties of the data element to the result. This also makes it possible to map more built-in types to itself than previously.</li>
</ul></td>
</tr>
</tbody>
</table>

## ABAP Unit

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Test Seams and Injections</strong></td>
<td><p><a href="abentest_seam_glosry.html">Test seams</a> and <a href="abeninjection_glosry.html">injections</a> have been introduced for unit tests in ABAP Unit. When tests are executed, code wrapped in <a href="abaptest-seam.html"><code class="ph codeph">TEST-SEAM</code></a> and <a href="abapend-test-seam.html"><code class="ph codeph">END-TEST-SEAM</code></a> as part of production code can be replaced by code from test classes wrapped by <a href="abaptest-injection.html"><code class="ph codeph">TEST-INJECTION</code></a> and <a href="abapend-test-injection.html"><code class="ph codeph">END-TEST-INJECTION</code></a>.</p>
<p>Test classes with injections must be created in <a href="abentest_include_glosry.html">test includes</a>. With the exception of test includes for class pools and function pools, no test includes can currently be created.</p></td>
</tr>
</tbody>
</table>
