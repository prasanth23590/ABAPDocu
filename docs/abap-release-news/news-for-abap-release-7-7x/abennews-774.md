---
title: "News for ABAP Release 7.74"
source_file: abennews-774.html
section: "ABAP Release News > News for ABAP Release 7.7x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.74

The kernel release for ABAP release 7.74 is 7.74.

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
<td><strong>Hierarchy Load Options</strong></td>
<td>The <a href="abencds_f1_define_hierarchy.html">hierarchy generator</a> <a href="abencds_f1_define_hierarchy.html"><code class="ph codeph">DEFINE HIERARCHY</code></a> can now use the new addition <code class="ph codeph">LOAD BULK|INCREMENTAL|load_option</code> to specify the load policy for a generated hierarchy.</td>
</tr>
<tr class="even">
<td><strong>Handling of Annotation Values</strong></td>
<td><p>A change in the handling of <a href="abenannotation_value_glosry.html">annotation values</a> has been introduced with the following consequences:</p>
<ul>
<li>Annotations that require an <a href="abencds_annotations_syntax_value.html">enumeration symbol</a> as annotation value no longer accept string values. They only accept enumeration symbols. Example: Until release 7.74, the following was accepted: <code class="ph codeph">@AccessControl.authorizationCheck: '#CHECK'</code>. From release 7.74, this is no longer accepted. The quotation marks must be removed.</li>
<li><p>If <em>#</em> is the first or the only character of <code class="ph codeph">EndUserText.label</code> or <code class="ph codeph">EndUserText.quickInfo</code>, then it is not removed from the unescaped value any more.</p>
<p>These changes are slightly incompatible.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Assignments

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Calculation Assignments</strong></td>
<td><p>A <a href="abencalculation_assignment_glosry.html">calculation assignment</a> is an <a href="abenassignment_glosry.html">assignment</a> with an</p>
<ul>
<li><a href="abenadd_assignment_op_glosry.html">addition assignment operator</a> (<a href="abencalculation_assignments.html"><code class="ph codeph">+=</code></a>)</li>
<li><a href="abensub_assignment_op_glosry.html">subtraction assignment operator</a> (<a href="abencalculation_assignments.html"><code class="ph codeph">-=</code></a>)</li>
<li><a href="abenmult_assignment_op_glosry.html">multiplication assignment operator</a> (<a href="abencalculation_assignments.html"><code class="ph codeph">*=</code></a>)</li>
<li><a href="abendiv_assignment_op_glosry.html">division assignment operator</a> (<a href="abencalculation_assignments.html"><code class="ph codeph">/=</code></a>)</li>
<li><p><a href="abenconcat_assignment_op_glosry.html">concatenation assignment operator</a> (<a href="abencalculation_assignment_string.html"><code class="ph codeph">&amp;&amp;=</code></a>).</p>
<p>A calculation takes place when the assignment is made. These new operators make the statements <a href="abapadd.html"><code class="ph codeph">ADD</code></a>, <a href="abapsubtract_multiply_divide.html"><code class="ph codeph">SUBTRACT</code></a>, <a href="abapsubtract_multiply_divide.html"><code class="ph codeph">MULTIPLY</code></a>, and <a href="abapsubtract_multiply_divide.html"><code class="ph codeph">DIVIDE</code></a> obsolete.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## ABAP SQL

| Modification                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Definition of Associations**               | When associations of a [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) are exposed using the addition [`WITH ASSOCIATIONS`](../../abap-programming-language/abap-database-access/abapwith_associations.md), new [CTE associations](../../abap-glossary/abencte_association_glosry.md) can be defined by specifying [`JOIN TO ONE|MANY`](../../abap-programming-language/abap-database-access/abapwith_associations_defining.md). These CTE associations can be used in the subsequent queries of the current [`WITH`](../../abap-programming-language/abap-database-access/abapwith.md) statement, either in [path expressions](../../abap-programming-language/abap-database-access/abenabap_sql_path.md) or as [hierarchy associations](../../abap-glossary/abenhierarchy_association_glosry.md) in the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_generator.md). |
| **Temporal SQL Hierarchies**                 | The [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_generator.md) can now use the new addition `PERIOD FROM TO VALID FROM TO` to create [temporal SQL hierarchies](../../abap-glossary/abentemporal_hierarchy_glosry.md) in which the hierarchy nodes are limited by time intervals.                                                                                                                                                                                                                                                                                                                                                                          |
| **Aggregate Expressions in SQL Expressions** | From ABAP release 7.74, [aggregate expressions](../../abap-programming-language/abap-database-access/abapselect_aggregate.md) can be specified as operands of SQL expressions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
