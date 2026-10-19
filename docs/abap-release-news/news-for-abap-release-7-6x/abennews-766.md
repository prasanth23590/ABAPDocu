---
title: "News for ABAP Release 7.66"
source_file: abennews-766.html
section: "ABAP Release News > News for ABAP Release 7.6x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.66

The kernel release for ABAP release 7.66 is 7.50.

## Expressions and Functions

| Modification                                    | Description                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Key Specification for the `FILTER` Operator** | In the variant of the constructor expression where a [filter table](../../abap-programming-language/abap-processing-internal-data/abenconstructor_expr_filter_table.md) is specified, the addition `USING KEY` can be used either for the filter table or for the source table. Previously, the filter table had to have a sorted key or a hash key. This restriction does not apply if such a key can be specified for the source table instead. |

## ABAP SQL

| Modification                         | Description                                                                                                                                                                                                                                             |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Cardinality in `LEFT OUTER JOIN`** | In a [`LEFT OUTER JOIN`](../../abap-programming-language/abap-database-access/abapselect_join.md), an addition `ONE TO MANY` can now be specified for the [cardinality](../../abap-glossary/abencardinality_glosry.md). This is evaluated as a note for optimization by [SAP HANA databases](../../abap-glossary/abenhana_database_glosry.md). |

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
<td><strong>Cardinality in <code class="ph codeph">LEFT OUTER JOIN</code></strong></td>
<td><p>In a <a href="abencds_joined_data_source_v1.html"><code class="ph codeph">LEFT OUTER JOIN</code></a>, an addition <code class="ph codeph">TO ONE</code> or <code class="ph codeph">TO MANY</code> can be specified for the <a href="abencardinality_glosry.html">cardinality</a>. This addition is evaluated by an <a href="abenhana_database_glosry.html">SAP HANA database</a> as a note for optimization.</p>
<p>This option exists in earlier releases in ABAP CDS, but has been documented only from ABAP release 7.66. In <a href="abennews-766.html#abap-sql">ABAP SQL</a>, the corresponding syntax was introduced in ABAP release 7.66.</p></td>
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
<td><strong>Reference to ABAP Types</strong></td>
<td><p>When an <a href="abenamdp_method_glosry.html">AMDP method</a> is implemented in an AMDP class with SQLScript, the following new <a href="abenamdp_macro_glosry.html">AMDP macro</a></p>
<p><a href="abenamdp_abap_types.html"><code class="ph codeph">"$ABAP.type( [name =] abap_type )"</code></a></p>
<p>can be used to reference ABAP types. The ABAP runtime framework replaces these schemas on the database with the associated database types.</p></td>
</tr>
</tbody>
</table>
