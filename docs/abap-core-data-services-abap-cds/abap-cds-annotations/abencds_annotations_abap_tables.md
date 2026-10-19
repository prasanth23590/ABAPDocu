---
title: "ABAP CDS - ABAP Annotation Syntax"
source_file: abencds_annotations_abap_tables.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - ABAP Annotations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - ABAP Annotation Syntax

The following tables summarize the [annotation syntax](../../abap-glossary/abencds_annotation_syntax_glosry.md) and [properties](abencds_sap_anno_props.md) of all [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) and [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md) in ABAP CDS. The first column contains links to more detailed information.

Only those annotations are shown that can be used in the current ABAP language version.

- [AbapCatalog-Annotations](abencds_annotations_abap_tables.md#abapcatalog-annotations)

- [AccessControl-Annotations](abencds_annotations_abap_tables.md#accesscontrol-annotations)

- [Aggregation-Annotations](abencds_annotations_abap_tables.md#aggregation-annotations)

- [API-Annotations](abencds_annotations_abap_tables.md#api-annotations)

- [ClientHandling-Annotations](abencds_annotations_abap_tables.md#clienthandling-annotations)

- [EndUserText-Annotations](abencds_annotations_abap_tables.md#endusertext-annotations)

- [Environment-Annotations](abencds_annotations_abap_tables.md#environment-annotations)

- [MappingRole-Annotations](abencds_annotations_abap_tables.md#mappingrole-annotations)

- [Metadata-Annotations](abencds_annotations_abap_tables.md#metadata-annotations)

- [ObjectModel-Annotations](abencds_annotations_abap_tables.md#objectmodel-annotations)

- [Semantics-Annotations](abencds_annotations_abap_tables.md#semantics-annotations)

## AbapCatalog-Annotations

<table>
<thead>
<tr class="header">
<th><strong>Syntax</strong></th>
<th><strong>Scope</strong></th>
<th><strong>Type</strong></th>
<th><strong>Enums</strong></th>
<th><strong>Default</strong></th>
<th><strong>Text</strong></th>
<th><strong>MDE</strong></th>
<th><strong>API</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abencds_368297892_anno.html"><code class="ph codeph">AbapCatalog.amdp.allowedForWrite</code></a></td>
<td><code class="ph codeph">#TABLE_ENTITY</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_1619044161-_anno.html"><code class="ph codeph">AbapCatalog.buffering.numberOfKeyFields</code></a></td>
<td><code class="ph codeph">#VIEW</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">000</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_1242119123-_anno.html"><code class="ph codeph">AbapCatalog.buffering.status</code></a></td>
<td><code class="ph codeph">#VIEW</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#ACTIVE</code></p>
<p><code class="ph codeph">#NOT_ALLOWED</code></p>
<p><code class="ph codeph">#SWITCHED_OFF</code></p></td>
<td><code class="ph codeph">#SWITCHED_OFF</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_464103458_anno.html"><code class="ph codeph">AbapCatalog.buffering.type</code></a></td>
<td><code class="ph codeph">#VIEW</code></td>
<td><code class="ph codeph">String(10)</code></td>
<td><p><code class="ph codeph">#FULL</code></p>
<p><code class="ph codeph">#GENERIC</code></p>
<p><code class="ph codeph">#NONE</code></p>
<p><code class="ph codeph">#SINGLE</code></p></td>
<td><code class="ph codeph">#NONE</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_1687178802-_anno.html"><code class="ph codeph">AbapCatalog.compiler.compareFilter</code></a></td>
<td><code class="ph codeph">#VIEW</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_67699033-_anno.html"><code class="ph codeph">AbapCatalog.dataMaintenance</code></a></td>
<td><p><code class="ph codeph">#HIERARCHY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#ALLOWED</code></p>
<p><code class="ph codeph">#DISPLAY_ONLY</code></p>
<p><code class="ph codeph">#NOT_ALLOWED</code></p>
<p><code class="ph codeph">#RESTRICTED</code></p></td>
<td><code class="ph codeph">#RESTRICTED</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_680013611-_anno.html"><code class="ph codeph">AbapCatalog.dbHints[ ].dbSystem</code></a></td>
<td><code class="ph codeph">#VIEW</code></td>
<td><code class="ph codeph">String(3)</code></td>
<td><p><code class="ph codeph">#ADA</code></p>
<p><code class="ph codeph">#ALL</code></p>
<p><code class="ph codeph">#ASE</code></p>
<p><code class="ph codeph">#DB2</code></p>
<p><code class="ph codeph">#DB4</code></p>
<p><code class="ph codeph">#DB6</code></p>
<p><code class="ph codeph">#HDB</code></p>
<p><code class="ph codeph">#INF</code></p>
<p><code class="ph codeph">#MSS</code></p>
<p><code class="ph codeph">#ORA</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_828976635-_anno.html"><code class="ph codeph">AbapCatalog.dbHints[ ].hint</code></a></td>
<td><code class="ph codeph">#VIEW</code></td>
<td><code class="ph codeph">String(1298)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_61840010-_anno.html"><code class="ph codeph">AbapCatalog.deliveryClass</code></a></td>
<td><code class="ph codeph">#TABLE_ENTITY</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#APPLICATION_DATA</code></p>
<p><code class="ph codeph">#CUSTOMIZING_DATA</code></p>
<p><code class="ph codeph">#LOCAL_DATA</code></p>
<p><code class="ph codeph">#SYSTEM_ADMINISTRATIVE_DATA</code></p>
<p><code class="ph codeph">#SYSTEM_DATA</code></p>
<p><code class="ph codeph">#SYSTEM_EDITABLE_DATA</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2036691489-_anno.html"><code class="ph codeph">AbapCatalog.entityBuffer.definitionAllowed</code></a></td>
<td><p><code class="ph codeph">#TABLE_ENTITY</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_1760222934_anno.html"><code class="ph codeph">AbapCatalog.entityBuffer.definitionType[ ]</code></a></td>
<td><code class="ph codeph">#VIEW</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#DELEGATED</code></p>
<p><code class="ph codeph">#MATERIALIZED</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_1859277801_anno.html"><code class="ph codeph">AbapCatalog.entityBuffer.propagationAllowed</code></a></td>
<td><code class="ph codeph">#VIEW</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_2031682287_anno.html"><code class="ph codeph">AbapCatalog.extensibility.allowNewCompositions</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_1925198989-_anno.html"><code class="ph codeph">AbapCatalog.extensibility.allowNewDatasources</code></a></td>
<td><code class="ph codeph">#VIEW</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_1373877666-_anno.html"><code class="ph codeph">AbapCatalog.extensibility.dataSources[ ]</code></a></td>
<td><code class="ph codeph">#VIEW</code></td>
<td><code class="ph codeph">LocalDefinitionRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_864724495_anno.html"><code class="ph codeph">AbapCatalog.extensibility.elementSuffix</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(3)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_1159849682_anno.html"><code class="ph codeph">AbapCatalog.extensibility.extensible</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#SERVICE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_699341645-_anno.html"><code class="ph codeph">AbapCatalog.extensibility.quota.maximumBytes</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_1345726382_anno.html"><code class="ph codeph">AbapCatalog.extensibility.quota.maximumFields</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_450773322_anno.html"><code class="ph codeph">AbapCatalog.preserveKey</code></a></td>
<td><code class="ph codeph">#VIEW</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_873797739_anno.html"><code class="ph codeph">AbapCatalog.sqlViewAppendName</code></a></td>
<td><code class="ph codeph">#EXTEND_VIEW</code></td>
<td><code class="ph codeph">String(16)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_253495944_anno.html"><code class="ph codeph">AbapCatalog.sqlViewName</code></a></td>
<td><code class="ph codeph">#VIEW</code></td>
<td><code class="ph codeph">String(16)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2016919924-_anno.html"><code class="ph codeph">AbapCatalog.typeSpec.changeDocumentRelevant</code></a></td>
<td><code class="ph codeph">#SIMPLE_TYPE</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_58258031_anno.html"><code class="ph codeph">AbapCatalog.typeSpec.conversionExit</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">String(5)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_1569826112_anno.html"><code class="ph codeph">AbapCatalog.typeSpec.outputLength</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_801468554-_anno.html"><code class="ph codeph">AbapCatalog.viewEnhancementCategory[ ]</code></a></td>
<td><code class="ph codeph">#VIEW</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#GROUP_BY</code></p>
<p><code class="ph codeph">#NONE</code></p>
<p><code class="ph codeph">#PROJECTION_LIST</code></p>
<p><code class="ph codeph">#UNION</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>

## AccessControl-Annotations

<table>
<thead>
<tr class="header">
<th><strong>Syntax</strong></th>
<th><strong>Scope</strong></th>
<th><strong>Type</strong></th>
<th><strong>Enums</strong></th>
<th><strong>Default</strong></th>
<th><strong>Text</strong></th>
<th><strong>MDE</strong></th>
<th><strong>API</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abencds_1180334353_anno.html"><code class="ph codeph">AccessControl.authorizationCheck</code></a></td>
<td><p><code class="ph codeph">#EXTERNAL_ENTITY</code></p>
<p><code class="ph codeph">#HIERARCHY</code></p>
<p><code class="ph codeph">#TABLE_ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#CHECK</code></p>
<p><code class="ph codeph">#MANDATORY</code></p>
<p><code class="ph codeph">#NOT_ALLOWED</code></p>
<p><code class="ph codeph">#NOT_REQUIRED</code></p>
<p><code class="ph codeph">#PRIVILEGED_ONLY</code></p></td>
<td><code class="ph codeph">#NOT_REQUIRED</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>

## Aggregation-Annotations

<table>
<thead>
<tr class="header">
<th><strong>Syntax</strong></th>
<th><strong>Scope</strong></th>
<th><strong>Type</strong></th>
<th><strong>Enums</strong></th>
<th><strong>Default</strong></th>
<th><strong>Text</strong></th>
<th><strong>MDE</strong></th>
<th><strong>API</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abencds_741130102_anno.html"><code class="ph codeph">Aggregation.default</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#AVG</code></p>
<p><code class="ph codeph">#COUNT_DISTINCT</code></p>
<p><code class="ph codeph">#FORMULA</code></p>
<p><code class="ph codeph">#MAX</code></p>
<p><code class="ph codeph">#MIN</code></p>
<p><code class="ph codeph">#NONE</code></p>
<p><code class="ph codeph">#NOP</code></p>
<p><code class="ph codeph">#SUM</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>

## API-Annotations

<table>
<thead>
<tr class="header">
<th><strong>Syntax</strong></th>
<th><strong>Scope</strong></th>
<th><strong>Type</strong></th>
<th><strong>Enums</strong></th>
<th><strong>Default</strong></th>
<th><strong>Text</strong></th>
<th><strong>MDE</strong></th>
<th><strong>API</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abencds_1318352950-_anno.html"><code class="ph codeph">API.element.decommissioningPlannedForYearMonth</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(7)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1839662893-_anno.html"><code class="ph codeph">API.element.releaseState</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#DECOMMISSIONED</code></p>
<p><code class="ph codeph">#DEPRECATED</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1922632877-_anno.html"><code class="ph codeph">API.element.successor</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>

## ClientHandling-Annotations

<table>
<thead>
<tr class="header">
<th><strong>Syntax</strong></th>
<th><strong>Scope</strong></th>
<th><strong>Type</strong></th>
<th><strong>Enums</strong></th>
<th><strong>Default</strong></th>
<th><strong>Text</strong></th>
<th><strong>MDE</strong></th>
<th><strong>API</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abencds_1114072352_anno.html"><code class="ph codeph">ClientHandling.algorithm</code></a></td>
<td><p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#AUTOMATED</code></p>
<p><code class="ph codeph">#NONE</code></p>
<p><code class="ph codeph">#SESSION_VARIABLE</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1549616294_anno.html"><code class="ph codeph">ClientHandling.clientSafe</code></a></td>
<td><p><code class="ph codeph">#HIERARCHY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_613831553_anno.html"><code class="ph codeph">ClientHandling.type</code></a></td>
<td><p><code class="ph codeph">#TABLE_ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#CLIENT_DEPENDENT</code></p>
<p><code class="ph codeph">#CLIENT_INDEPENDENT</code></p>
<p><code class="ph codeph">#INHERITED</code></p></td>
<td><code class="ph codeph">#INHERITED</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>

## EndUserText-Annotations

<table>
<thead>
<tr class="header">
<th><strong>Syntax</strong></th>
<th><strong>Scope</strong></th>
<th><strong>Type</strong></th>
<th><strong>Enums</strong></th>
<th><strong>Default</strong></th>
<th><strong>Text</strong></th>
<th><strong>MDE</strong></th>
<th><strong>API</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abencds_92083118_anno.html"><code class="ph codeph">EndUserText.heading</code></a></td>
<td><code class="ph codeph">#SIMPLE_TYPE</code></td>
<td><code class="ph codeph">String(55)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_924137870_anno.html"><code class="ph codeph">EndUserText.label</code></a></td>
<td><p><code class="ph codeph">#ACCESSPOLICY</code></p>
<p><code class="ph codeph">#ASPECT</code></p>
<p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#ENTITY_ASPECT</code></p>
<p><code class="ph codeph">#ENUM_VALUE</code></p>
<p><code class="ph codeph">#EXTEND_VIEW</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#PFCG_MAPPING</code></p>
<p><code class="ph codeph">#ROLE</code></p>
<p><code class="ph codeph">#SERVICE</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_26162021_anno.html"><code class="ph codeph">EndUserText.quickInfo</code></a></td>
<td><p><code class="ph codeph">#ANNOTATE</code></p>
<p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY_ASPECT</code></p>
<p><code class="ph codeph">#ENUM_VALUE</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">String(100)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>

## Environment-Annotations

<table>
<thead>
<tr class="header">
<th><strong>Syntax</strong></th>
<th><strong>Scope</strong></th>
<th><strong>Type</strong></th>
<th><strong>Enums</strong></th>
<th><strong>Default</strong></th>
<th><strong>Text</strong></th>
<th><strong>MDE</strong></th>
<th><strong>API</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abencds_1000560355-_anno.html"><code class="ph codeph">Environment.sql.passValue</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_1937921420_anno.html"><code class="ph codeph">Environment.systemField</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#CLIENT</code></p>
<p><code class="ph codeph">#SYSTEM_DATE</code></p>
<p><code class="ph codeph">#SYSTEM_LANGUAGE</code></p>
<p><code class="ph codeph">#SYSTEM_TIME</code></p>
<p><code class="ph codeph">#USER</code></p>
<p><code class="ph codeph">#USER_DATE</code></p>
<p><code class="ph codeph">#USER_TIMEZONE</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>

## MappingRole-Annotations

<table>
<thead>
<tr class="header">
<th><strong>Syntax</strong></th>
<th><strong>Scope</strong></th>
<th><strong>Type</strong></th>
<th><strong>Enums</strong></th>
<th><strong>Default</strong></th>
<th><strong>Text</strong></th>
<th><strong>MDE</strong></th>
<th><strong>API</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abencds_984551930-_anno.html"><code class="ph codeph">MappingRole</code></a></td>
<td><code class="ph codeph">#ROLE</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>

## Metadata-Annotations

<table>
<thead>
<tr class="header">
<th><strong>Syntax</strong></th>
<th><strong>Scope</strong></th>
<th><strong>Type</strong></th>
<th><strong>Enums</strong></th>
<th><strong>Default</strong></th>
<th><strong>Text</strong></th>
<th><strong>MDE</strong></th>
<th><strong>API</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abencds_1985816297-_anno.html"><code class="ph codeph">Metadata.allowExtensions</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1433174898-_anno.html"><code class="ph codeph">Metadata.ignorePropagatedAnnotations</code></a></td>
<td><code class="ph codeph">#VIEW</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_195182532_anno.html"><code class="ph codeph">Metadata.layer</code></a></td>
<td><code class="ph codeph">#ANNOTATE</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><p><code class="ph codeph">#CORE</code></p>
<p><code class="ph codeph">#CUSTOMER</code></p>
<p><code class="ph codeph">#INDUSTRY</code></p>
<p><code class="ph codeph">#LOCALIZATION</code></p>
<p><code class="ph codeph">#PARTNER</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>

## ObjectModel-Annotations

<table>
<thead>
<tr class="header">
<th><strong>Syntax</strong></th>
<th><strong>Scope</strong></th>
<th><strong>Type</strong></th>
<th><strong>Enums</strong></th>
<th><strong>Default</strong></th>
<th><strong>Text</strong></th>
<th><strong>MDE</strong></th>
<th><strong>API</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abencds_763589850-_anno.html"><code class="ph codeph">ObjectModel.query.implementedBy</code></a></td>
<td><p><code class="ph codeph">#CUSTOM_ENTITY</code></p>
<p><code class="ph codeph">#ENTITY</code></p></td>
<td><code class="ph codeph">String(255)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_1091668137-_anno.html"><code class="ph codeph">ObjectModel.usageType.dataClass</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#CUSTOMIZING</code></p>
<p><code class="ph codeph">#MASTER</code></p>
<p><code class="ph codeph">#META</code></p>
<p><code class="ph codeph">#MIXED</code></p>
<p><code class="ph codeph">#ORGANIZATIONAL</code></p>
<p><code class="ph codeph">#TRANSACTIONAL</code></p></td>
<td><code class="ph codeph">#MIXED</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1255374604-_anno.html"><code class="ph codeph">ObjectModel.usageType.serviceQuality</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#A</code></p>
<p><code class="ph codeph">#B</code></p>
<p><code class="ph codeph">#C</code></p>
<p><code class="ph codeph">#D</code></p>
<p><code class="ph codeph">#P</code></p>
<p><code class="ph codeph">#X</code></p></td>
<td><code class="ph codeph">#X</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1163152301_anno.html"><code class="ph codeph">ObjectModel.usageType.sizeCategory</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p></td>
<td><code class="ph codeph">String(3)</code></td>
<td><p><code class="ph codeph">#L</code></p>
<p><code class="ph codeph">#M</code></p>
<p><code class="ph codeph">#S</code></p>
<p><code class="ph codeph">#XL</code></p>
<p><code class="ph codeph">#XXL</code></p></td>
<td><code class="ph codeph">#S</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1555784333_anno.html"><code class="ph codeph">ObjectModel.virtualElementCalculatedBy</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(255)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
</tbody>
</table>

## Semantics-Annotations

<table>
<thead>
<tr class="header">
<th><strong>Syntax</strong></th>
<th><strong>Scope</strong></th>
<th><strong>Type</strong></th>
<th><strong>Enums</strong></th>
<th><strong>Default</strong></th>
<th><strong>Text</strong></th>
<th><strong>MDE</strong></th>
<th><strong>API</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abencds_689127610-_anno.html"><code class="ph codeph">Semantics.amount.currencyCode</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1954553685-_anno.html"><code class="ph codeph">Semantics.currencyCode</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_653082254-_anno.html"><code class="ph codeph">Semantics.quantity.unitOfMeasure</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_772720932-_anno.html"><code class="ph codeph">Semantics.unitOfMeasure</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>
