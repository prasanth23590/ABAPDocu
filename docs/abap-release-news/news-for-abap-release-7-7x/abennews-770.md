---
title: "News for ABAP Release 7.70"
source_file: abennews-770.html
section: "ABAP Release News > News for ABAP Release 7.7x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.70

The kernel release for ABAP release 7.70 is 7.70.

## ABAP Dictionary

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Expanded Limits</strong></td>
<td><p>The following limits now apply to the number of fields and the length of the structure of a <a href="abenddic_db_table_glosry.html">DDIC database table</a>, of a <a href="abendatabase_view_glosry.html">DDIC database view</a>, and of a <a href="abencds_view_glosry.html">CDS view</a>:</p>
<ul>
<li>Database tables</li>
<li>A database table that is not part of the software component <code class="ph codeph">SAP_BASIS</code> can now contain 1000 fields for the storage type Row Store and 1500 fields for the storage type Column Store. The total of all field lengths is no longer checked in ABAP Dictionary.</li>
<li>A database table that is part of the software component <code class="ph codeph">SAP_BASIS</code> can contain a maximum of 749 fields (as before) and the total of the field lengths in ABAP Dictionary is still restricted to 4030.</li>
<li>DDIC database views and CDS views</li>
<li>A view that is not part of the software component <code class="ph codeph">SAP_BASIS</code> can contain 1500 view fields. The total of all field lengths is no longer checked in ABAP Dictionary.</li>
<li>A view that is part of the software component <code class="ph codeph">SAP_BASIS</code> can contain a maximum of 749 fields (as before) and the total of the field lengths in ABAP Dictionary is still restricted to 4096.</li>
</ul></td>
</tr>
</tbody>
</table>

## ABAP SQL

| Modification             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Restrictions Removed** | ABAP SQL read statements no longer bypass [table buffering](../../abap-glossary/abentable_buffering_glosry.md) in cases where a column is specified on the right side of [comparisons](../../abap-programming-language/abap-database-access/abenwhere_logexp_compare.md) or of [`BETWEEN`](../../abap-programming-language/abap-database-access/abenwhere_logexp_interval.md) in an [SQL condition](../../abap-programming-language/abap-database-access/abenasql_cond.md) that is not required to identify a single row or a generic range. The prerequisite for this is that both operands are numeric but do not have the type `DF16_DEC` or `DF34_DEC`, that both operands are character-like, or that both operands have the type `RAW` with the same lengths. |

## ABAP CDS

| Modification                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CDS Abstract Entities**                | An [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) defines the type properties of a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) without creating an instance of a database object. A CDS abstract entity is defined using [`DEFINE ABSTRACT ENTITY`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_define_abstract_entity.md) in a [CDS data definition](../../abap-glossary/abencds_data_definition_glosry.md).                                                                                                                                        |
| **Metadata Extensions for CDS Entities** | The variant [`ANNOTATE ENTITY`](../../abap-core-data-services-abap-cds/abap-cds-annotations/abencds_f1_annotate_view.md) was added to the previous statement [`ANNOTATE VIEW`](../../abap-core-data-services-abap-cds/abap-cds-annotations/abencds_f1_annotate_view.md). This makes it possible to define [CDS metadata extensions](../../abap-glossary/abencds_metadata_extension_glosry.md) for any [CDS entities](../../abap-glossary/abencds_entity_glosry.md) with the exception of [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md). Metadata extensions of this type can contain entity annotations, parameter annotations, and element annotations. |

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
<td><strong>Restrictions Removed</strong></td>
<td><p>The following restrictions were removed:</p>
<ul>
<li>Tabular input parameters are now allowed in <a href="abenamdp_function_method_glosry.html">AMDP function implementations</a> for <a href="abenamdp_table_function_glosry.html">AMDP table functions</a>. Previously, only elementary input parameters were allowed. In AMDP function implementations for <a href="abencds_table_function_glosry.html">CDS table functions</a>, however, the restriction that only elementary input parameters are allowed still applies.</li>
<li>Tabular input parameters of <a href="abenamdp_procedure_method_glosry.html">AMDP procedure implementations</a> and of <a href="abenamdp_function_method_glosry.html">AMDP function implementations</a> can now be made optional using <a href="abapmethods_parameters.html"><code class="ph codeph">OPTIONAL</code></a>, but it is still not possible to specify a start value with <a href="abapmethods_parameters.html"><code class="ph codeph">DEFAULT</code></a>.</li>
</ul></td>
</tr>
</tbody>
</table>

## Exception Handling

| Modification                             | Description                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Setting the Attribute `IS_RESUMABLE`** | The attribute `IS_RESUMABLE` of an [exception object](../../abap-glossary/abenexception_object_glosry.md) is now set after exceptions raised by the statement [`RAISE RESUMABLE EXCEPTION`](../../abap-programming-language/abap-program-flow-logic/abapraise_exception_class.md) only if the [`CATCH`](../../abap-programming-language/abap-program-flow-logic/abapcatch_try.md) statement in question has the addition `BEFORE UNWIND`. Previously in catches, the attribute was set for every exception raised in this way. |

## Further Changes

| Modification     | Description                                                                                                                                                                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Modification** | In ABAP release 7.70, a new [ABAP version](../../abap-glossary/abenabap_version_glosry.md) [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md) was introduced. The internal version ID in the column `UCCHECK` of the system table `TRDIR` is *5*. |
