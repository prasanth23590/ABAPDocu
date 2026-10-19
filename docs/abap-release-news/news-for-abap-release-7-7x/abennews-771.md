---
title: "News for ABAP Release 7.71"
source_file: abennews-771.html
section: "ABAP Release News > News for ABAP Release 7.7x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.71

The kernel release for ABAP release 7.71 is 7.71.

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
<td><strong>Null Values in the Table Buffer</strong></td>
<td><p>The <a href="abentable_buffer_glosry.html">table buffer</a> now supports real <a href="abennull_value_glosry.html">null values</a>. In <a href="abentable_buffering_glosry.html">table buffering</a>, null values are no longer transformed to type-dependent initial values. When the buffer is accessed, the same results are produced as when the database is accessed directly. The corresponding restrictions now no longer apply. The following are some of the aspects affected:</p>
<ul>
<li><a href="abenabap_sql_stmt_logexp.html">Relational expressions</a> with operands that contain null values. The result of a comparison of this type is now also unknown when the comparison is made in the buffer (except in the expression <a href="abenwhere_logexp_null.html"><code class="ph codeph">IS [NOT] NULL</code></a>).</li>
<li>If used, <a href="abenwhere_logexp_null.html"><code class="ph codeph">IS [NOT] NULL</code></a> no longer bypasses table buffering.</li>
<li>Accesses to <a href="abencds_v1_buffering.html">buffered CDS views</a>. When the buffer is accessed, the same results are now produced as when the database is accessed directly. Null values are often produced by <a href="abencds_joined_data_source_v1.html">outer joins</a> or in expressions such as <a href="abencds_case_expression_v1.html">case distinction</a> expressions. The restriction specifying that only those CDS views are buffered whose elements do not contain <a href="abennull_value_glosry.html">null values</a> no longer applies.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Date/Time Functions</strong></td>
<td><p>ABAP SQL now supports the following new date/time functions:</p>
<ul>
<li><a href="abensql_time_func.html">Time functions</a></li>
<li><code class="ph codeph">TIMS_IS_VALID</code></li>
<li><a href="abensql_timestamp_func.html">Time stamp functions</a></li>
<li><code class="ph codeph">TSTMP_IS_VALID</code></li>
<li><code class="ph codeph">TSTMP_CURRENT_UTCTIMESTAMP</code></li>
<li><code class="ph codeph">TSTMP_SECONDS_BETWEEN</code></li>
<li><code class="ph codeph">TSTMP_ADD_SECONDS</code></li>
<li><a href="abensql_date_time_conversions.html">Date/time conversions</a></li>
<li><code class="ph codeph">TSTMP_TO_DATS</code></li>
<li><code class="ph codeph">TSTMP_TO_TIMS</code></li>
<li><code class="ph codeph">TSTMP_TO_DST</code></li>
<li><code class="ph codeph">DATS_TIMS_TO_TSTMP</code></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Restrictions Removed</strong></td>
<td>For <a href="abensql_engine_expr.html">certain SQL expressions and functions</a>, an ABAP SQL read statement no longer bypasses <a href="abentable_buffering_glosry.html">table buffering</a>.</td>
</tr>
<tr class="even">
<td><strong>Weaker Check</strong></td>
<td>ABAP SQL statements that exploit a database property not supported by all database platforms no longer produce a syntax check warning.</td>
</tr>
<tr class="odd">
<td><strong>New Check</strong></td>
<td>If the data of the <a href="abapselect_itab.html">internal table</a> needs to be transported to the database in cases where the internal table is used as a <a href="abapselect_data_source.html">data source</a> of the ABAP SQL statement <a href="abapselect.html"><code class="ph codeph">SELECT</code></a>, a syntax check warning occurs that can be hidden using the pragma <code class="ph codeph">##itab_db_select</code>.</td>
</tr>
</tbody>
</table>
