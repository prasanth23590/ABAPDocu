---
title: "ABAP CDS - Changing the Type of a CDS Entity"
source_file: abencds_transitions.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Changing the Type of a CDS Entity

A [CDS entity](../../abap-glossary/abencds_entity_glosry.md) can be changed into another [CDS source type](../../abap-glossary/abenddl_source_type_glosry.md) by replacing the source code. This can be done even after the respective CDS entity has been activated and transported.

Example: You have an active [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) and want to change it into a [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md).

Steps:

1.  Replace the statement [`DEFINE VIEW ENTITY CDSEntityName AS SELECT FROM ...`](abencds_define_view_entity.md) by [`DEFINE CUSTOM ENTITY EntityName...`](abencds_f1_define_custom_entity.md).

2.  Adapt the source code to comply with all rules for CDS custom entities.

3.  Activate the custom entity.

Result: The entity is changed from CDS view entity to CDS custom entity.

The following type changes are supported:

<table>
<thead>
<tr class="header">
<th><strong>From</strong></th>
<th><strong>To</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CDS view entity</td>
<td><p>- CDS custom entity</p>
<p>- CDS abstract entity</p></td>
</tr>
<tr class="even">
<td>CDS projection view</td>
<td><p>- CDS custom entity</p>
<p>- CDS abstract entity</p></td>
</tr>
<tr class="odd">
<td>CDS hierarchy</td>
<td><p>- CDS custom entity</p>
<p>- CDS abstract entity</p></td>
</tr>
<tr class="even">
<td>CDS custom entity</td>
<td><p>- CDS view entity</p>
<p>- CDS projection view</p>
<p>- CDS abstract entity</p>
<p>- CDS hierarchy</p>
<p>- CDS DDIC-based view (obsolete)</p></td>
</tr>
<tr class="odd">
<td>CDS abstract entity</td>
<td><p>- CDS view entity</p>
<p>- CDS projection view</p>
<p>- CDS custom entity</p>
<p>- CDS hierarchy</p>
<p>- CDS DDIC-based view (obsolete)</p></td>
</tr>
<tr class="even">
<td>CDS DDIC-based view (obsolete)</td>
<td><p>- CDS view entity</p>
<p>- CDS projection view</p>
<p>- CDS custom entity</p>
<p>- CDS abstract entity</p></td>
</tr>
<tr class="odd">
<td><p><a href="abencds_view_extend_glosry.html">CDS DDIC-based view extension</a></p>
<p>(<code class="ph codeph">EXTEND VIEW</code>)</p></td>
<td><p><a href="abencds_view_entity_extend_glosry.html">CDS view entity extensions</a></p>
<p>(<code class="ph codeph">EXTEND VIEW ENTITY</code>)</p></td>
</tr>
</tbody>
</table>

The names of elements from the element list, associations, annotations, and clauses can be changed freely and without any restrictions, as long as consumers of the respective CDS entity are not affected.

## Restrictions

- CDS table functions, CDS external entities, and [CDS table entities](../../abap-glossary/abencds_table_entity_glosry.md) cannot be turned into any other entity type after activation.

- Changing a [CDS view](../../abap-glossary/abencds_view_glosry.md) into a [CDS transient entity](../../abap-glossary/abencds_non_sql_entity_glosry.md) is possible only if there are no consumers. The reason is that view building on CDS custom entities and CDS abstract entities is not supported. Example: A CDS view entity which serves as data source of another CDS view entity must not be changed into a CDS custom entity.

## Hint

Certain type changes are not supported, for example, a CDS view entity cannot be changed into a CDS hierarchy. As a workaround, the CDS view entity can first be changed into a CDS custom entity and as a second step, it can be changed into a CDS hierarchy.
