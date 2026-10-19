---
title: "News for ABAP Release 7.63"
source_file: abennews-763.html
section: "ABAP Release News > News for ABAP Release 7.6x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.63

The kernel release for ABAP release 7.63 is 7.47.

## ABAP SQL

| Modification                          | Description                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **New Addition `OFFSET` in `SELECT`** | An addition [`OFFSET`](../../abap-programming-language/abap-database-access/abapselect_up_to_offset.md) can now be specified to specify the first row of the result set.                                                                                                                                                                                                                       |
| **SQL Functions**                     | The new string functions [`LEFT`](../../abap-programming-language/abap-database-access/abensql_string_func.md), [`CONCAT_WITH_SPACE`](../../abap-programming-language/abap-database-access/abensql_string_func.md), [`INSTR`](../../abap-programming-language/abap-database-access/abensql_string_func.md), and [`RPAD`](../../abap-programming-language/abap-database-access/abensql_string_func.md) perform operations on strings. This means ABAP SQL now supports the same string functions as [ABAP CDS](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_sql_functions_character_v1.md). |
| **New Additions in `DELETE dbtab`**   | In the variant `DELETE FROM target` of the statement [`DELETE`](../../abap-programming-language/abap-database-access/abapdelete_dbtab.md), the additions [`ORDER BY`](../../abap-programming-language/abap-database-access/abapdelete_where.md), [`OFFSET`](../../abap-programming-language/abap-database-access/abapdelete_where.md), and [`UP TO`](../../abap-programming-language/abap-database-access/abapdelete_where.md) can now be specified to restrict the number of rows to delete.                                                           |

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
<td><strong>Expressions and Functions</strong></td>
<td><p>The following enhancements have been implemented:</p>
<ul>
<li><p>In a <a href="abencds_cast_expression_v1.html"><code class="ph codeph">CAST</code> expression</a>, operands of the type <code class="ph codeph">SSTRING</code> can now be cast to types other than themselves and back. Here, the type <code class="ph codeph">SSTRING</code> behaves like the data type <code class="ph codeph">CHAR</code>.</p>
<p>The following changes have been made:</p></li>
<li>In <a href="abencds_cast_expression_v1.html"><code class="ph codeph">CAST</code> expressions</a> to data elements, the restriction no longer applies that the data type, the length, and the number of decimal places of operand and target data type must match exactly. This restriction can now be applied as an optional restriction using the new addition <code class="ph codeph">PRESERVING TYPE</code>. This addition specifies explicitly that casts are to be applied to the semantic properties of a data element. <code class="ph codeph">PRESERVING TYPE</code> suppresses the syntax warning that handles casts of identical technical types.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>CDS Associations</strong></td>
<td><p>The following changes have been made:</p>
<ul>
<li><code class="ph codeph">WITH DEFAULT FILTER</code> can be used to specify a default filter condition for a <a href="abencds_association_glosry.html">CDS association</a>. This condition is used as a filter condition in a <a href="abencds_path_expression_v1.html">path expression</a> if no condition is specified for the CDS association here.</li>
<li><a href="abencds_association_glosry.html">CDS associations</a> can now be <a href="abencds_select_list_association_v1.html">exposed</a> for union sets formed with <a href="abencds_union_v1.html"><code class="ph codeph">UNION</code></a>. In this case, special rules apply.</li>
<li>In a <a href="abencds_path_expression_v1.html">path expression</a>, <a href="abencds_path_expr_card_v1.html"><code class="ph codeph">*:</code></a> can be used to declare a CDS association as a non-unique CDS association explicitly.</li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>CDS DDIC-Based View Extensions</strong></td>
<td><p>The statement <a href="abencds_extend_view.html"><code class="ph codeph">EXTEND VIEW</code></a> can now be used to extend the following CDS views too:</p>
<ul>
<li>CDS views with <a href="abencds_aggregate_functions_v1.html">aggregate expressions</a> and a <a href="abencds_group_by_v1.html"><code class="ph codeph">GROUP-BY</code> clause</a></li>
<li><p>CDS views with a <a href="abencds_union_v1.html"><code class="ph codeph">UNION</code> clause</a> for union sets</p>
<p>For extensions of the <code class="ph codeph">GROUP-BY</code> clause and <code class="ph codeph">UNION</code> clauses, the existing CDS view must contain the new <a href="abenannotation_array_glosry.html">annotation array</a> <a href="abencds_view_anno_v1.html"><code class="ph codeph">AbapCatalog.viewEnhancementCategory[ ]</code></a> with suitable values. The value <code class="ph codeph">#NONE</code> of this annotation array can be used to prevent any enhancements being made to a CDS view using CDS DDIC-based view extensions.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Key Fields</strong></td>
<td><p>The following changes have been made:</p>
<ul>
<li>The key fields of a CDS view that are defined with <a href="abencds_select_list_entry_v1.html"><code class="ph codeph">KEY</code></a> must now, like the key fields of a CDS table function, be placed without gaps at the start of the <a href="abencds_select_list_v1.html"><code class="ph codeph">SELECT</code> list</a>.</li>
<li>The new view annotation <a href="abencds_450773322_anno.html"><code class="ph codeph">AbapCatalog.preserveKey</code></a> can be used to override the default behavior of the addition <a href="abencds_select_list_entry_v1.html"><code class="ph codeph">KEY</code></a> for defining key fields of a CDS view. If the annotation is specified with the value <code class="ph codeph">true</code>, the key fields defined using <code class="ph codeph">KEY</code> are also used for the associated CDS-managed DDIC view (obsolete).</li>
</ul></td>
</tr>
</tbody>
</table>
