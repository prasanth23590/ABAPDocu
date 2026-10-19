---
title: "News for ABAP Release 7.69"
source_file: abennews-769.html
section: "ABAP Release News > News for ABAP Release 7.6x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.69

The kernel release for ABAP release 7.69 is 7.53.

## Expressions and Functions

| Modification                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Pseudo Component `table_line` in Mapping Rules** | It is now possible to specify the [pseudo component](../../abap-glossary/abenpseudo_component_glosry.md) `table_line` as a source component of a source table in [mapping rules](../../abap-programming-language/abap-processing-internal-data/abencorresponding_constr_mapping.md) of the component operator [`CORRESPONDING`](../../abap-programming-language/abap-processing-internal-data/abenconstructor_expr_corresponding.md), if the table has an elementary row type. In all other cases, the behavior is undefined when the pseudo component is specified. |

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
<td><strong>Internal Tables as Data Sources</strong></td>
<td>An <a href="abapselect_itab.html">internal table</a> can be specified as a <a href="abapselect_data_source.html"><code class="ph codeph">data source</code></a> data source of a query. This statement cannot be executed on all database systems, if the data from the internal table needs to be passed to the database.</td>
</tr>
<tr class="even">
<td><strong>Relational Expressions</strong></td>
<td><p>The following is now possible for <a href="abenabap_sql_expr_logexp.html">conditions in expressions</a>:</p>
<ul>
<li>Size comparisons can now be made between character-like data types and are no longer restricted to numeric data types.</li>
<li>The operator <code class="ph codeph">BETWEEN</code> is also no longer restricted to numeric data types and SQL expressions can now be specified on the right side.</li>
<li>The operator <code class="ph codeph">LIKE</code> is now also supported.</li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Path Expressions</strong></td>
<td><p>The following is now possible for <a href="abenabap_sql_path.html">path expressions</a>:</p>
<ul>
<li>CDS associations can now be used whose <a href="abenassociation_target_glosry.html">association targets</a> are <a href="abencds_table_function_glosry.html">CDS table functions</a>.</li>
<li><a href="abenabap_sql_parameters.html">Parameters</a> can now be passed after the CDS associations of a <a href="abenabap_sql_path.html">path expression</a> in the <a href="abenabap_sql_columns.html">specified columns</a> of <a href="abenasql_query_glosry.html">queries</a>. Until now, this was only possible in path expressions in the <a href="abapselect_data_source.html">data source</a> of the <a href="abapfrom_clause.html"><code class="ph codeph">FROM</code> clause</a> of a <a href="abenasql_query_glosry.html">query</a>. This makes it possible to specify paths whose CDS associations have CDS entities with input parameters as data sources.</li>
<li>The <a href="abencardinality_glosry.html">cardinality</a> and type of the join expression can now be specified as attributes in the <a href="abenabap_sql_path_filter.html">square brackets</a> after the CDS associations of a <a href="abenabap_sql_path.html">path expression</a>. Until now, only filter conditions were possible.</li>
<li><a href="abenabap_sql_path_filter.html">Attributes</a> can now be specified after the CDS associations of a <a href="abenabap_sql_path.html">path expression</a> in the <a href="abenabap_sql_columns.html">specified columns</a> of <a href="abenasql_query_glosry.html">queries</a>. Until now, attributes could only be specified in path expressions in the <a href="abapselect_data_source.html">data source</a> of the <a href="abapfrom_clause.html"><code class="ph codeph">FROM</code> clause</a> of a <a href="abenasql_query_glosry.html">query</a>, and only filter conditions were possible.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Access Control</strong></td>
<td>The new addition <a href="abapselect_data_source.html"><code class="ph codeph">WITH PRIVILEGED ACCESS</code></a> disables <a href="abencds_access_control_glosry.html">CDS access control</a>.</td>
</tr>
<tr class="odd">
<td><strong><code class="ph codeph">ORDER BY</code> and <code class="ph codeph">UP TO</code>, <code class="ph codeph">OFFSET</code> in Subquery</strong></td>
<td>In a <a href="abensubquery_glosry.html">subquery</a>, it is now possible to use an <a href="abaporderby_clause.html"><code class="ph codeph">ORDER BY</code></a> clause and the additions <a href="abapselect_up_to_offset.html"><code class="ph codeph">UP TO</code></a> and <a href="abapselect_up_to_offset.html"><code class="ph codeph">OFFSET</code></a> can be used after the clause. It is not possible to execute a subquery with an <code class="ph codeph">ORDER BY</code> clause on all database systems</td>
</tr>
<tr class="even">
<td><strong>Addition <code class="ph codeph">NOT</code> for <code class="ph codeph">BETWEEN</code> and <code class="ph codeph">LIKE</code></strong></td>
<td>The addition <code class="ph codeph">NOT</code> can now be specified in front of <code class="ph codeph">BETWEEN</code> and <code class="ph codeph">LIKE</code> in <a href="abenabap_sql_expr_logexp.html">relation expressions for expressions</a>.</td>
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
<td><strong>Access Control</strong></td>
<td><p>The following enhancements have been implemented in <a href="abencds_access_control_glosry.html">CDS access control</a>:</p>
<ul>
<li><a href="abencds_role_glosry.html">CDS roles</a> can now also be defined for <a href="abencds_table_function_glosry.html">CDS table functions</a>. When a CDS table function is accessed in ABAP SQL, the access conditions are evaluated by default.</li>
<li>Extensions in DCL for defining CDS roles:</li>
<li>When <a href="abenaccess_condition_glosry.html">access conditions</a> <a href="abencds_dcl_role_cond_expr.html"><code class="ph codeph">cds_cond</code></a> are specified, there are no longer any restrictions on how Boolean operators and parentheses are used. The Boolean operator <code class="ph codeph">NOT</code> can now also be used and any combination of parentheses is possible.</li>
<li>The operators <a href="abencds_f1_cond_literal.html"><code class="ph codeph">BETWEEN</code></a> and <a href="abencds_f1_cond_literal.html"><code class="ph codeph">IS NULL</code></a> are now available for literal conditions as part of an access condition.</li>
<li>When a path is specified for an element in an <a href="abenaccess_condition_glosry.html">access condition</a>, multivalue CDS associations are now also tracked.</li>
<li>In a <a href="abencds_f1_cond_literal.html">literal condition</a> <code class="ph codeph">[NOT] LIKE</code>, it is now possible to specify an escape character using <code class="ph codeph">ESCAPE</code>.</li>
<li>Blanks are now no longer forced in certain positions.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Extensions</strong></td>
<td><a href="abencds_view_extend_glosry.html">CDS DDIC-based view extensions</a> are now connected to <a href="abenswitch_framework_glosry.html">Switch Framework</a> whenever they are defined in a <a href="abenpackage_glosry.html">package</a> that is assigned a <a href="abenswitch_glosry.html">switch</a>.</td>
</tr>
</tbody>
</table>

## Data Clusters

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>New Catchable Exceptions</strong></td>
<td><p>The following <a href="abenrabax_import_from_database.html">exceptions in <code class="ph codeph">IMPORT</code></a> were previously non-catchable but are now assigned to the exception class <code class="ph codeph">CX_SY_IMPORT_FORMAT_ERROR</code> and hence can be handled:</p>
<ul>
<li><code class="ph codeph">CONNE_ILLEGAL_TRANSPORT_HEADER</code></li>
<li><code class="ph codeph">CONNE_ILLEGAL_TRANSPORT_VERS</code></li>
<li><code class="ph codeph">CONNE_COMPRESS_FLAG_INVALID</code></li>
<li><code class="ph codeph">CONNE_CONTAINER_TOO_SHORT</code></li>
<li><code class="ph codeph">CONNE_DESCRIPTION_FLAG_INVALID</code></li>
<li><code class="ph codeph">CONVERSION_CODEPAGE_UNKNOWN</code></li>
<li><code class="ph codeph">IMPORT_DESCR_ENDMARK_MISSING</code></li>
<li><code class="ph codeph">IMPORT_UNEXPECTED_END_OF_DATA</code></li>
<li><p><code class="ph codeph">IMPORT_CONTAINER_MISSING</code></p>
<ul>
<li><code class="ph codeph">IMPORT_FROM_DATA_BUFFER_EMPTY</code> is now also <code class="ph codeph">IMPORT_CONTAINER_MISSING</code></li>
<li><code class="ph codeph">IMPORT_FROM_INTTABLE_EMPTY</code> is now also <code class="ph codeph">IMPORT_CONTAINER_MISSING</code></li>
</ul></li>
<li><code class="ph codeph">IMPORT_CONTAINER_MISSING</code></li>
<li><code class="ph codeph">IMPORT_DECOMPRESS_FAILED</code></li>
<li><code class="ph codeph">IMPORT_OBJECT_DESTROYED</code></li>
</ul></td>
</tr>
</tbody>
</table>

## ABAP Unit

| Modification       | Description                                                                                                                                                                                                                                                                                                                                                     |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Test Relations** | The special [ABAP Doc comment](../../abap-glossary/abenabap_doc_comment_glosry.md) [`"! @testing ...`](../../abap-programming-language/abap-program-maintenance/abentest_relations.md) can be used to define [test relations](../../abap-glossary/abentest_relation_glosry.md) between test classes or test methods and repository objects. This allows the tests for these repository objects to be displayed and executed in [ADT](../../abap-glossary/abenadt_glosry.md). |

## ABAP Doc

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Documentation Links</strong></td>
<td>The new syntax <code class="ph codeph">{@link ...}</code> makes it possible to link to other documentation of repository objects (or its components) in <a href="abenabap_doc_comment_glosry.html">ABAP Doc comments</a>.</td>
</tr>
<tr class="even">
<td><strong>Further Changes</strong></td>
<td><p>The following changes have also been made to <a href="abenabap_doc_comment_glosry.html">ABAP Doc comments</a>:</p>
<ul>
<li>Opening and closing tags no longer need to be specified in lowercase letters.</li>
<li>The restriction to 7 bit ASCII characters no longer applies. An ABAP Doc comment can now contain any 16 bit Unicode characters.</li>
<li><code class="ph codeph">&lt;br&gt;</code> or <code class="ph codeph">&lt;br/&gt;</code> can be used to specify a line break. <code class="ph codeph">&lt;br&gt;&lt;/br&gt;</code> should no longer be used.</li>
<li>The special characters <code class="ph codeph">@</code> and <code class="ph codeph">&lt;</code> now only need to be escaped when they are placed directly in front of another character.</li>
<li>Lists can now be nested.</li>
<li>The tags <code class="ph codeph">&lt;p&gt;</code>, <code class="ph codeph">&lt;ul&gt;</code>, or <code class="ph codeph">&lt;ol&gt;</code> can now be placed within <code class="ph codeph">&lt;h1&gt;</code>, <code class="ph codeph">&lt;h2&gt;</code>, <code class="ph codeph">&lt;h3&gt;</code>, <code class="ph codeph">&lt;p&gt;</code>, <code class="ph codeph">&lt;em&gt;</code>, or <code class="ph codeph">&lt;strong&gt;</code> tags.</li>
<li>Text can now be specified directly within <code class="ph codeph">&lt;ol&gt;</code> and <code class="ph codeph">&lt;ul&gt;</code> tags.</li>
<li>In the <code class="ph codeph">&lt;ol&gt;</code> tag, the attributes <code class="ph codeph">reversed</code>, <code class="ph codeph">start</code>, and <code class="ph codeph">type</code> can now be specified with their traditional HTML meaning.</li>
<li>The attributes specified in tags are now checked by the syntax check.</li>
</ul></td>
</tr>
</tbody>
</table>

## Further Changes

| Modification                        | Description                                                                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Surrogate Areas in iXML Library** | The iXML Library now supports [surrogate areas](../../abap-programming-language/abap-data-interchange-formats/abenabap_ixml_lib_cloud.md) with the same problems as in [ABAP](../../abap-programming-language/abap-overview/abencharacter_sets.md). |
