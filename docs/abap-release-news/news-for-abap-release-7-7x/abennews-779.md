---
title: "News for ABAP Release 7.79"
source_file: abennews-779.html
section: "ABAP Release News > News for ABAP Release 7.7x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.79

The kernel release for ABAP release 7.79 is 7.79.

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
<td><strong>New Window Function <code class="ph codeph">NTILE</code></strong></td>
<td><p>ABAP SQL now supports the following new <a href="abenwindow_function_glosry.html">window function</a> in <a href="abenwindow_expression_glosry.html">window expressions</a>:</p>
<ul>
<li><a href="abensql_win_func.html"><code class="ph codeph">NTILE</code></a></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><code class="ph codeph">SELECT</code>, <code class="ph codeph">INTO target</code> Modification</strong></td>
<td>When using <code class="ph codeph">SELECT, INTO target</code>, host variables can now be declared inline even when the <code class="ph codeph">FROM</code> clause is dynamic, as long as all fields of the <code class="ph codeph">SELECT</code> list are known statically. Previously, the structure of the result set, including <code class="ph codeph">SELECT</code> list, <code class="ph codeph">FROM</code> clause, and any indicators needed to be static.</td>
</tr>
<tr class="odd">
<td><strong>New Type Conversion Function <code class="ph codeph">to_clob</code></strong></td>
<td>ABAP SQL now supports the new <a href="abensql_type_conv_func.html">type conversion function</a> <a href="abensql_type_conv_func.html"><code class="ph codeph">to_clob</code></a>.</td>
</tr>
<tr class="even">
<td><strong>New Currency Conversion Function <code class="ph codeph">currency conversion</code></strong></td>
<td>ABAP SQL now supports the new currency conversion function <a href="abensql_curr_unit_conv_func.html"><code class="ph codeph">currency_conversion</code></a>.</td>
</tr>
<tr class="odd">
<td><strong>Streaming and Locators Can Now Be Used on SQL Expressions</strong></td>
<td>Streaming and locators can now be used in combination with SQL expressions such as <a href="abensql_type_conv_func.html"><code class="ph codeph">TO_CLOB</code></a>, <a href="abensql_type_conv_func.html"><code class="ph codeph">TO_BLOB</code></a>, and <a href="abensql_geo_conv_func.html"><code class="ph codeph">AS_GEO_JSON</code></a>.</td>
</tr>
</tbody>
</table>

## ABAP RESTful Application Programming Model

In release 7.79, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

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
<td><strong>Managed Internal Numbering for Managed RAP BOs</strong></td>
<td>The new statement <a href="abenbdl_field_numbering.html"><code class="ph codeph">numbering:managed</code></a> can be used to automatically generate values for primary key fields with a UUID. Available for managed RAP BOs.</td>
</tr>
<tr class="even">
<td><strong>New Options for Output Parameters</strong></td>
<td><p>For actions and functions, the <a href="abenbdl_action_output_para.html">output parameter</a> can now be an entity or a structure.</p>
<p>The addition <a href="abenbdl_action_output_para.html"><code class="ph codeph">selective</code></a> can be used for an output parameter to return only parts of the result structure.</p></td>
</tr>
</tbody>
</table>
