---
title: "News for ABAP Release 7.78"
source_file: abennews-778.html
section: "ABAP Release News > News for ABAP Release 7.7x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.78

The kernel release for ABAP release 7.78 is 7.78.

## ABAP CDS

| Modification                   | Description                                                                                                                                                                                                                            |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CDS View Entity Extensions** | The new statement [`EXTEND VIEW ENTITY`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_extend_view_entity.md) of the DDL of ABAP CDS makes it possible to add new view fields to existing CDS views entities and CDS projection views by using CDS view entity extensions. |

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
<td><strong>New Aggregate Function <code class="ph codeph">ALLOW_PRECISION_LOSS</code></strong></td>
<td><p>ABAP SQL now supports the following new <a href="abenaggregate_function_glosry.html">aggregate function</a> in combination with the <a href="abenaggregate_expression_glosry.html">aggregate expression</a> <a href="abensql_agg_func.html"><code class="ph codeph">SUM</code></a>:</p>
<ul>
<li><a href="abapselect_allow_precision_loss.html"><code class="ph codeph">ALLOW_PRECISION_LOSS</code></a></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Optional Window Frame Specification within a Window Function</strong></td>
<td>The optional <a href="abapselect_over.html">window frame specification</a> allows a subset of rows within a window, called a frame, to be defined. Frames are determined with respect to the current row, which enables the frame to move within a window.</td>
</tr>
<tr class="odd">
<td><strong>New Window Functions <code class="ph codeph">FIRST_VALUE</code> and <code class="ph codeph">LAST_VALUE</code></strong></td>
<td><p>ABAP SQL now supports the following new <a href="abenwindow_function_glosry.html">window functions</a> in <a href="abenwindow_expression_glosry.html">window expressions</a>:</p>
<ul>
<li><a href="abensql_win_func.html"><code class="ph codeph">FIRST_VALUE</code></a> and <a href="abensql_win_func.html"><code class="ph codeph">LAST_VALUE</code></a>.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>New Date/Time Conversion Functions</strong></td>
<td><p>ABAP SQL now supports the following new <a href="abensql_date_time_conversions.html">date/time conversion functions</a>:</p>
<ul>
<li><a href="abensql_date_time_conversions.html"><code class="ph codeph">TSTMPL_TO_UTCL</code></a> and <a href="abensql_date_time_conversions.html"><code class="ph codeph">TSTMPL_FROM_UTCL</code></a></li>
<li><a href="abensql_date_time_conversions.html"><code class="ph codeph">DATS_TO_DATN</code></a> and <a href="abensql_date_time_conversions.html"><code class="ph codeph">DATS_FROM_DATN</code></a></li>
<li><a href="abensql_date_time_conversions.html"><code class="ph codeph">TIMS_TO_TIMN</code></a> and <a href="abensql_date_time_conversions.html"><code class="ph codeph">TIMS_FROM_TIMN</code></a></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>New Time Stamp Functions</strong></td>
<td><p>ABAP SQL now supports the following new <a href="abensql_timestamp_func.html">time stamp functions</a>:</p>
<ul>
<li><a href="abensql_timestamp_func.html"><code class="ph codeph">UTCL_CURRENT</code></a>, <a href="abensql_timestamp_func.html"><code class="ph codeph">UTCL_ADD_SECONDS</code></a>, and <a href="abensql_timestamp_func.html"><code class="ph codeph">UTCL_SECONDS_BETWEEN</code></a>.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>New Date Functions</strong></td>
<td><p>ABAP SQL now supports the following new <a href="abensql_date_func.html">date functions</a>:</p>
<ul>
<li><a href="abensql_date_func.html"><code class="ph codeph">DATN_DAYS_BETWEEN</code></a>, <a href="abensql_date_func.html"><code class="ph codeph">DATN_ADD_DAYS</code></a>, and <a href="abensql_date_func.html"><code class="ph codeph">DATN_ADD_MONTHS</code></a>.</li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>New Additions After the <code class="ph codeph">ORDER BY</code> Clause</strong></td>
<td><p>ABAP SQL now supports the following additions after the <a href="abaporderby_clause.html"><code class="ph codeph">ORDER BY</code></a> clause:</p>
<ul>
<li><a href="abaporderby_clause.html"><code class="ph codeph">NULLS FIRST</code></a> and <a href="abaporderby_clause.html"><code class="ph codeph">NULLS LAST</code></a>.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>New Aggregate Functions</strong></td>
<td><p>ABAP SQL now supports the following new <a href="abensql_agg_func.html">aggregate functions</a>:</p>
<ul>
<li><code class="ph codeph">MEDIAN</code>, <code class="ph codeph">STDDEV</code>, <code class="ph codeph">VAR</code>, <code class="ph codeph">CORR</code>, and <code class="ph codeph">CORR_SPEARMAN</code>.</li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>New Geometry Conversion Function <code class="ph codeph">as_geo_json</code></strong></td>
<td><p>ABAP SQL now supports the following new <a href="abensql_geo_conv_func.html">geometry conversion function</a>:</p>
<ul>
<li><a href="abensql_geo_conv_func.html"><code class="ph codeph">as_geo_json</code></a></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>SQL Conditions Revised</strong></td>
<td><p>The following SQL conditions were revised:</p>
<ul>
<li>The operator <a href="abenwhere_logexp_list_in.html"><code class="ph codeph">IN</code></a> can now be used with a <a href="abenwhere_logexp_list_in.html">subquery that returns value tuples</a>.</li>
<li><a href="abenabap_sql_builtin_functions.html">SQL functions</a> and <a href="abensql_cast.html">cast expressions</a> can now be used as operands on the right side of <a href="abenwhere_logexp_compare.html">comparison operators</a>.</li>
</ul></td>
</tr>
</tbody>
</table>

## ABAP CDS Access Control

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Check with <code class="ph codeph">element IS [NOT] INITIAL</code> in a Literal Condition</strong></td>
<td>In a literal condition, <code class="ph codeph">IS [NOT] INITIAL</code> can now be used to check whether the value of the left side matches (does not match) the initial value of the ABAP data type that matches the element.</td>
</tr>
<tr class="even">
<td><strong>Addition <code class="ph codeph">bypass when</code></strong></td>
<td>The addition <a href="abencds_f1_cond_pfcg.html"><code class="ph codeph">BYPASS WHEN</code></a> can now be used to specify a bypass condition for an element. If the condition is met, the element in question is not used for authorization filtering.</td>
</tr>
<tr class="odd">
<td><strong>Check on the User Name in User Conditions</strong></td>
<td><p>When the user name is checked in <a href="abencds_f1_cond_user.html">user conditions</a>, the following can now be checked instead of the user name:</p>
<ul>
<li>The value of the alias.</li>
<li>The number of the business partner assigned to the user.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Data Types</strong></td>
<td>The operand that can be specified on the left side of a condition of an access rule of a CDS role can now have the built-in ABAP Dictionary <a href="abencds_f1_dcl_cond_data_types.html">data type</a> <code class="ph codeph">RAW</code>.</td>
</tr>
<tr class="odd">
<td><strong>Aspect Bypass Conditions</strong></td>
<td><code class="ph codeph">IS [NOT] INITIAL</code> and <code class="ph codeph">IS INITIAL OR NULL</code> are now possible as <a href="abencds_f1_define_generic_aspect.html">aspect bypass conditions</a>.</td>
</tr>
</tbody>
</table>

## Exception Handling

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Declaration of <code class="ph codeph">CX_NO_CHECK</code> Exceptions</strong></td>
<td><p>Exceptions of category <code class="ph codeph">CX_NO_CHECK</code> are always declared implicitly in interfaces of procedures and can always be propagated.</p>
<p>Now it is also possible to declare exceptions of category <code class="ph codeph">CX_NO_CHECK</code> with <code class="ph codeph">RAISING</code> in procedure interfaces, for example for <a href="abapmethods_general.html">methods</a>. This allows it to document the possible occurrence of such exceptions and to change the category of existing exceptions to <code class="ph codeph">CX_NO_CHECK</code> without leading to syntax errors in procedure interfaces.</p></td>
</tr>
</tbody>
</table>

## ABAP RESTful Application Programming Model

In release 7.78, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

| Modification                       | Description                                                                                                                                                                                           |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Type Mapping**                   | The new statement [`mapping for`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_type_mapping.md) can be used to map field names from legacy code to field names from the current data model. Available for unmanaged and managed RAP BOs. |
| **Additional Save in Managed BOs** | The new statement [`with additional save`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_saving.md) can be used to enhance the default save sequence in a managed RAP BO.                                                                 |
| **Unmanaged Save in Managed BOs**  | The new statement [`with unmanaged save`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_saving.md) can be used to implement an own saving strategy in a managed RAP BO.                                                                   |
| **Implementation Grouping**        | The new statement [`group`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_grouping.md) can be used to divide the implementation-relevant parts of a BO's business logic into several groups for behavior implementation.                  |
