---
title: "ABAP CDS - Framework-Specific Annotation Syntax"
source_file: abencds_annotations_frmwrk_tables.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - Framework-Specific Annotations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Framework-Specific Annotation Syntax

The following tables summarize the [annotation syntax](../../abap-glossary/abencds_annotation_syntax_glosry.md) and [properties](abencds_sap_anno_props.md) of all [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) and [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md) in ABAP CDS. The first column contains links to more detailed information.

Only those annotations are shown that can be used in the current ABAP language version.

- [AccessControl-Annotations](abencds_annotations_frmwrk_tables.md#accesscontrol-annotations)

- [Aggregation-Annotations](abencds_annotations_frmwrk_tables.md#aggregation-annotations)

- [Analytics-Annotations](abencds_annotations_frmwrk_tables.md#analytics-annotations)

- [AnalyticsDetails-Annotations](abencds_annotations_frmwrk_tables.md#analyticsdetails-annotations)

- [Consumption-Annotations](abencds_annotations_frmwrk_tables.md#consumption-annotations)

- [DataIntegration-Annotations](abencds_annotations_frmwrk_tables.md#dataintegration-annotations)

- [DefaultAggregation-Annotations](abencds_annotations_frmwrk_tables.md#defaultaggregation-annotations)

- [EnterpriseSearch-Annotations](abencds_annotations_frmwrk_tables.md#enterprisesearch-annotations)

- [Event-Annotations](abencds_annotations_frmwrk_tables.md#event-annotations)

- [ObjectModel-Annotations](abencds_annotations_frmwrk_tables.md#objectmodel-annotations)

- [OData-Annotations](abencds_annotations_frmwrk_tables.md#odata-annotations)

- [Search-Annotations](abencds_annotations_frmwrk_tables.md#search-annotations)

- [Semantics-Annotations](abencds_annotations_frmwrk_tables.md#semantics-annotations)

- [UI-Annotations](abencds_annotations_frmwrk_tables.md#ui-annotations)

- [VDM-Annotations](abencds_annotations_frmwrk_tables.md#vdm-annotations)

- [Workflow-Annotations](abencds_annotations_frmwrk_tables.md#workflow-annotations)

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
<td><a href="abencds_956586857-_anno.html"><code class="ph codeph">AccessControl.auditing.specification</code></a></td>
<td><p><code class="ph codeph">#TABLE_ENTITY</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(1000)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_102413712-_anno.html"><code class="ph codeph">AccessControl.auditing.type</code></a></td>
<td><p><code class="ph codeph">#TABLE_ENTITY</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(20)</code></td>
<td><code class="ph codeph">#CUSTOM</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_64119063-_anno.html"><code class="ph codeph">AccessControl.authorizationCheckMandatory[ ]</code></a></td>
<td><p><code class="ph codeph">#EXTERNAL_ENTITY</code></p>
<p><code class="ph codeph">#HIERARCHY</code></p>
<p><code class="ph codeph">#TABLE_ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#DELETE</code></p>
<p><code class="ph codeph">#INSERT</code></p>
<p><code class="ph codeph">#SELECT</code></p>
<p><code class="ph codeph">#UPDATE</code></p></td>
<td><code class="ph codeph">-</code></td>
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
<td><a href="abencds_1871137401-_anno.html"><code class="ph codeph">Aggregation.allowPrecisionLoss</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_1540548770_anno.html"><code class="ph codeph">Aggregation.exception</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#AVG</code></p>
<p><code class="ph codeph">#COUNT</code></p>
<p><code class="ph codeph">#COUNT_DISTINCT</code></p>
<p><code class="ph codeph">#FIRST</code></p>
<p><code class="ph codeph">#LAST</code></p>
<p><code class="ph codeph">#MAX</code></p>
<p><code class="ph codeph">#MEDIAN</code></p>
<p><code class="ph codeph">#MIN</code></p>
<p><code class="ph codeph">#NHA</code></p>
<p><code class="ph codeph">#STANDARD_DEVIATION</code></p>
<p><code class="ph codeph">#SUM</code></p>
<p><code class="ph codeph">#VARIANCE</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1237865219-_anno.html"><code class="ph codeph">Aggregation.referenceElement[ ]</code></a></td>
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

## Analytics-Annotations

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
<td><a href="abencds_235480066-_anno.html"><code class="ph codeph">Analytics.association.toDocumentStorage</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1043132933_anno.html"><code class="ph codeph">Analytics.constraints.filter</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#UNIQUE_PER_CELL</code></p>
<p><code class="ph codeph">#UNIQUE_PER_QUERY</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_568606453-_anno.html"><code class="ph codeph">Analytics.dataCategory</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#AGGREGATIONLEVEL</code></p>
<p><code class="ph codeph">#CUBE</code></p>
<p><code class="ph codeph">#DIMENSION</code></p>
<p><code class="ph codeph">#DOCSTORE</code></p>
<p><code class="ph codeph">#FACT</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_554014380_anno.html"><code class="ph codeph">Analytics.document.defaultAssociationToStorage</code></a></td>
<td><code class="ph codeph">#VIEW</code></td>
<td><code class="ph codeph">AssociationRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_355403503-_anno.html"><code class="ph codeph">Analytics.document.reference</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_669838829-_anno.html"><code class="ph codeph">Analytics.document.semantics</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#DOCUMENT</code></p>
<p><code class="ph codeph">#ID</code></p>
<p><code class="ph codeph">#INFOPROV</code></p>
<p><code class="ph codeph">#KYFNM</code></p>
<p><code class="ph codeph">#OWNER</code></p>
<p><code class="ph codeph">#PROPERTY</code></p>
<p><code class="ph codeph">#QPROV</code></p>
<p><code class="ph codeph">#SELECTIONS</code></p>
<p><code class="ph codeph">#SESSION_ID</code></p>
<p><code class="ph codeph">#STATUS</code></p>
<p><code class="ph codeph">#SVA_INFOPROV</code></p>
<p><code class="ph codeph">#TAG</code></p>
<p><code class="ph codeph">#TIMESTAMP</code></p>
<p><code class="ph codeph">#TYPE</code></p>
<p><code class="ph codeph">#VERSION</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1209697303-_anno.html"><code class="ph codeph">Analytics.document.serviceClassName</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_732025797_anno.html"><code class="ph codeph">Analytics.document.storageForEntity[ ]</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">EntityRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_228695892-_anno.html"><code class="ph codeph">Analytics.document.type</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(4)</code></td>
<td><p><code class="ph codeph">#DOC</code></p>
<p><code class="ph codeph">#HIO</code></p>
<p><code class="ph codeph">#HNM</code></p>
<p><code class="ph codeph">#HNO</code></p>
<p><code class="ph codeph">#SVA</code></p>
<p><code class="ph codeph">#SVH</code></p>
<p><code class="ph codeph">#TRA</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_814069367-_anno.html"><code class="ph codeph">Analytics.excludeFromRuntimeExtensibility</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2109597745_anno.html"><code class="ph codeph">Analytics.hidden</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_111006225_anno.html"><code class="ph codeph">Analytics.hints</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(1298)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_1635461139_anno.html"><code class="ph codeph">Analytics.internalName</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#DEFAULT</code></p>
<p><code class="ph codeph">#GLOBAL</code></p>
<p><code class="ph codeph">#LOCAL</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_881299780-_anno.html"><code class="ph codeph">Analytics.query</code></a></td>
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
<td><a href="abencds_1739792800-_anno.html"><code class="ph codeph">Analytics.settings.characteristicStructure.hierarchy.childNodePosition</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(5)</code></td>
<td><p><code class="ph codeph">#ABOVE</code></p>
<p><code class="ph codeph">#BELOW</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1791326552-_anno.html"><code class="ph codeph">Analytics.settings.columns.hierarchicalDisplay.active</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_31741450-_anno.html"><code class="ph codeph">Analytics.settings.columns.hierarchicalDisplay.expandTo</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_922459005_anno.html"><code class="ph codeph">Analytics.settings.columns.totalsLocation</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(10)</code></td>
<td><p><code class="ph codeph">#LEFT</code></p>
<p><code class="ph codeph">#RIGHT</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1374018734_anno.html"><code class="ph codeph">Analytics.settings.dataRetrieval</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#ALL_AT_ONCE</code></p>
<p><code class="ph codeph">#ON_HIERARCHY_DRILLDOWN</code></p>
<p><code class="ph codeph">#ON_NAVIGATION</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_33267603-_anno.html"><code class="ph codeph">Analytics.settings.displayOriginalInitialValue</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p>
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
<td><a href="abencds_1870062620-_anno.html"><code class="ph codeph">Analytics.settings.enforceSerialExecution</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1445898426_anno.html"><code class="ph codeph">Analytics.settings.initialValueForMissingText</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
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
<td><a href="abencds_1037361749_anno.html"><code class="ph codeph">Analytics.settings.maxProcessingEffort</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#HIGH</code></p>
<p><code class="ph codeph">#LOW</code></p>
<p><code class="ph codeph">#MEDIUM</code></p>
<p><code class="ph codeph">#UNLIMITED</code></p></td>
<td><code class="ph codeph">#HIGH</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1189019006_anno.html"><code class="ph codeph">Analytics.settings.measureStructure.hierarchy.childNodePosition</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(5)</code></td>
<td><p><code class="ph codeph">#ABOVE</code></p>
<p><code class="ph codeph">#BELOW</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1870969825-_anno.html"><code class="ph codeph">Analytics.settings.olapPushdown</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#BASIC</code></p>
<p><code class="ph codeph">#MAX</code></p>
<p><code class="ph codeph">#OFF</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2067852096-_anno.html"><code class="ph codeph">Analytics.settings.rows.hierarchicalDisplay.active</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1295952820_anno.html"><code class="ph codeph">Analytics.settings.rows.hierarchicalDisplay.expandTo</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1838938954_anno.html"><code class="ph codeph">Analytics.settings.rows.totalsLocation</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(10)</code></td>
<td><p><code class="ph codeph">#BOTTOM</code></p>
<p><code class="ph codeph">#TOP</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1999912159_anno.html"><code class="ph codeph">Analytics.settings.runtimeExtensibility.allowed</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1693486678_anno.html"><code class="ph codeph">Analytics.settings.valueHelp.supressInitialValue</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
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
<td><a href="abencds_2016857059-_anno.html"><code class="ph codeph">Analytics.settings.zeroValues.handling</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#HIDE</code></p>
<p><code class="ph codeph">#HIDE_IF_ALL</code></p>
<p><code class="ph codeph">#SHOW</code></p></td>
<td><code class="ph codeph">#SHOW</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1301366722-_anno.html"><code class="ph codeph">Analytics.settings.zeroValues.hideOnAxis</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#COLUMNS</code></p>
<p><code class="ph codeph">#ROWS</code></p>
<p><code class="ph codeph">#ROWS_COLUMNS</code></p></td>
<td><code class="ph codeph">#ROWS_COLUMNS</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1915515413_anno.html"><code class="ph codeph">Analytics.technicalName</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#HIERARCHY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(28)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1152620375-_anno.html"><code class="ph codeph">Analytics.variableCheck.implementedBy</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p>
<p><code class="ph codeph">#VIEW</code></p></td>
<td><code class="ph codeph">String(255)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>

## AnalyticsDetails-Annotations

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
<td><a href="abencds_1211955043-_anno.html"><code class="ph codeph">AnalyticsDetails.elimination.pair[ ].dimension1</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_785013031_anno.html"><code class="ph codeph">AnalyticsDetails.elimination.pair[ ].dimension2</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1795438715-_anno.html"><code class="ph codeph">AnalyticsDetails.elimination.rule</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#ELIMINATE_IF_ALL</code></p>
<p><code class="ph codeph">#ELIMINATE_IF_ONE</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1873151419_anno.html"><code class="ph codeph">AnalyticsDetails.exceptionAggregationSteps[ ].exceptionAggregationBehavior</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(14)</code></td>
<td><p><code class="ph codeph">#AVG</code></p>
<p><code class="ph codeph">#COUNT</code></p>
<p><code class="ph codeph">#COUNT_DISTINCT</code></p>
<p><code class="ph codeph">#FIRST</code></p>
<p><code class="ph codeph">#LAST</code></p>
<p><code class="ph codeph">#MAX</code></p>
<p><code class="ph codeph">#MEDIAN</code></p>
<p><code class="ph codeph">#MIN</code></p>
<p><code class="ph codeph">#NHA</code></p>
<p><code class="ph codeph">#STD</code></p>
<p><code class="ph codeph">#SUM</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_273130070_anno.html"><code class="ph codeph">AnalyticsDetails.exceptionAggregationSteps[ ].exceptionAggregationElements[ ]</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_741079388-_anno.html"><code class="ph codeph">AnalyticsDetails.query.axis</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#COLUMNS</code></p>
<p><code class="ph codeph">#FREE</code></p>
<p><code class="ph codeph">#ROWS</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_459989353-_anno.html"><code class="ph codeph">AnalyticsDetails.query.cellReference.characteristicStructureElement</code></a></td>
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
<td><a href="abencds_678776589_anno.html"><code class="ph codeph">AnalyticsDetails.query.cellReference.measureStructureElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1413766833-_anno.html"><code class="ph codeph">AnalyticsDetails.query.collisionHandling.decimals</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#CONCURRENT</code></p>
<p><code class="ph codeph">#DEFAULT</code></p>
<p><code class="ph codeph">#THIS</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1480232296_anno.html"><code class="ph codeph">AnalyticsDetails.query.collisionHandling.formula</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#CONCURRENT</code></p>
<p><code class="ph codeph">#DEFAULT</code></p>
<p><code class="ph codeph">#THIS</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1267460590_anno.html"><code class="ph codeph">AnalyticsDetails.query.collisionHandling.scaling</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#CONCURRENT</code></p>
<p><code class="ph codeph">#DEFAULT</code></p>
<p><code class="ph codeph">#THIS</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1908756799_anno.html"><code class="ph codeph">AnalyticsDetails.query.collisionHandling.semanticObject</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#CONCURRENT</code></p>
<p><code class="ph codeph">#DEFAULT</code></p>
<p><code class="ph codeph">#THIS</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1483832130_anno.html"><code class="ph codeph">AnalyticsDetails.query.decimals</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1081205336_anno.html"><code class="ph codeph">AnalyticsDetails.query.display</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#KEY</code></p>
<p><code class="ph codeph">#KEY_TEXT</code></p>
<p><code class="ph codeph">#TEXT</code></p>
<p><code class="ph codeph">#TEXT_KEY</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_900971148_anno.html"><code class="ph codeph">AnalyticsDetails.query.displayHierarchy</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#FILTER</code></p>
<p><code class="ph codeph">#FILTER_ONLY</code></p>
<p><code class="ph codeph">#OFF</code></p>
<p><code class="ph codeph">#ON</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1595836893_anno.html"><code class="ph codeph">AnalyticsDetails.query.elementHierarchy.initiallyCollapsed</code></a></td>
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
<td><a href="abencds_337532032-_anno.html"><code class="ph codeph">AnalyticsDetails.query.elementHierarchy.parent</code></a></td>
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
<td><a href="abencds_730974330_anno.html"><code class="ph codeph">AnalyticsDetails.query.formula</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(1298)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1105022108_anno.html"><code class="ph codeph">AnalyticsDetails.query.hidden</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1808598258_anno.html"><code class="ph codeph">AnalyticsDetails.query.hierarchyAssociation</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">AssociationRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1237616442_anno.html"><code class="ph codeph">AnalyticsDetails.query.hierarchyBinding[ ].type</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#CONSTANT</code></p>
<p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SYSTEM_FIELD</code></p>
<p><code class="ph codeph">#USER_INPUT</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1727265990-_anno.html"><code class="ph codeph">AnalyticsDetails.query.hierarchyBinding[ ].value</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(512)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_123301363_anno.html"><code class="ph codeph">AnalyticsDetails.query.hierarchyBinding[ ].variableSequence</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1919098161-_anno.html"><code class="ph codeph">AnalyticsDetails.query.hierarchyInitialLevel</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_416832717_anno.html"><code class="ph codeph">AnalyticsDetails.query.hierarchySettings.childNodePosition</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(10)</code></td>
<td><p><code class="ph codeph">#ABOVE</code></p>
<p><code class="ph codeph">#BELOW</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_68026887-_anno.html"><code class="ph codeph">AnalyticsDetails.query.hierarchySettings.hideNodeWithOneChild</code></a></td>
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
<td><a href="abencds_1179977864_anno.html"><code class="ph codeph">AnalyticsDetails.query.hierarchySettings.hidePostedNodesValues</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1535828704_anno.html"><code class="ph codeph">AnalyticsDetails.query.ignoreFurtherFilter.forAllElements</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_362709383_anno.html"><code class="ph codeph">AnalyticsDetails.query.ignoreFurtherFilter.forElement[ ]</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1556465713-_anno.html"><code class="ph codeph">AnalyticsDetails.query.isCell</code></a></td>
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
<td><a href="abencds_794884207_anno.html"><code class="ph codeph">AnalyticsDetails.query.keyDisplay</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#COMPOUND</code></p>
<p><code class="ph codeph">#CONTEXT_DEPENDENT</code></p>
<p><code class="ph codeph">#NOT_COMPOUND</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1799227771_anno.html"><code class="ph codeph">AnalyticsDetails.query.onCharacteristicStructure</code></a></td>
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
<td><a href="abencds_1458726059-_anno.html"><code class="ph codeph">AnalyticsDetails.query.resultValueHelpSource</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(10)</code></td>
<td><p><code class="ph codeph">#DIMENSION</code></p>
<p><code class="ph codeph">#QUERY</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1572845230_anno.html"><code class="ph codeph">AnalyticsDetails.query.resultValuesSource</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(10)</code></td>
<td><p><code class="ph codeph">#CUBE</code></p>
<p><code class="ph codeph">#DIMENSION</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_624410338_anno.html"><code class="ph codeph">AnalyticsDetails.query.reverseSign</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_941665532_anno.html"><code class="ph codeph">AnalyticsDetails.query.scaling</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_882208844-_anno.html"><code class="ph codeph">AnalyticsDetails.query.sortDirection</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#ASC</code></p>
<p><code class="ph codeph">#DESC</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1919095871-_anno.html"><code class="ph codeph">AnalyticsDetails.query.temporalJoin.derivationType</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#FIRST_DAY</code></p>
<p><code class="ph codeph">#LAST_DAY</code></p>
<p><code class="ph codeph">#OFFSET</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_672966127-_anno.html"><code class="ph codeph">AnalyticsDetails.query.temporalJoin.matchTextValidityPeriod</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1885827575-_anno.html"><code class="ph codeph">AnalyticsDetails.query.temporalJoin.offsetOfDays</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_180977041_anno.html"><code class="ph codeph">AnalyticsDetails.query.temporalJoin.timeElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1587493176_anno.html"><code class="ph codeph">AnalyticsDetails.query.totals</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#CONDITIONAL</code></p>
<p><code class="ph codeph">#HIDE</code></p>
<p><code class="ph codeph">#SHOW</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1253171795-_anno.html"><code class="ph codeph">AnalyticsDetails.query.variableSequence</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_870991642_anno.html"><code class="ph codeph">AnalyticsDetails.variable.defaultHierarchyNode.node[ ].element</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_72996958_anno.html"><code class="ph codeph">AnalyticsDetails.variable.defaultHierarchyNode.node[ ].value</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1232610243-_anno.html"><code class="ph codeph">AnalyticsDetails.variable.defaultHierarchyNode.nodeType</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1477228996-_anno.html"><code class="ph codeph">AnalyticsDetails.variable.defaultRanges[ ].high</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_672255340-_anno.html"><code class="ph codeph">AnalyticsDetails.variable.defaultRanges[ ].low</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_698268564-_anno.html"><code class="ph codeph">AnalyticsDetails.variable.defaultRanges[ ].option</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(2)</code></td>
<td><p><code class="ph codeph">#BT</code></p>
<p><code class="ph codeph">#CP</code></p>
<p><code class="ph codeph">#EQ</code></p>
<p><code class="ph codeph">#GE</code></p>
<p><code class="ph codeph">#GT</code></p>
<p><code class="ph codeph">#LE</code></p>
<p><code class="ph codeph">#LT</code></p>
<p><code class="ph codeph">#NB</code></p>
<p><code class="ph codeph">#NE</code></p>
<p><code class="ph codeph">#NP</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_913820777-_anno.html"><code class="ph codeph">AnalyticsDetails.variable.defaultRanges[ ].sign</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(1)</code></td>
<td><p><code class="ph codeph">#E</code></p>
<p><code class="ph codeph">#I</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_767114265-_anno.html"><code class="ph codeph">AnalyticsDetails.variable.defaultValue</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1200112008_anno.html"><code class="ph codeph">AnalyticsDetails.variable.defaultValueHigh</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2056058507-_anno.html"><code class="ph codeph">AnalyticsDetails.variable.hierarchyAssociation</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">AssociationRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_989212596_anno.html"><code class="ph codeph">AnalyticsDetails.variable.hierarchyBinding[ ].type</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#CONSTANT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SYSTEM_FIELD</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1820352587-_anno.html"><code class="ph codeph">AnalyticsDetails.variable.hierarchyBinding[ ].value</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(512)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1614358293_anno.html"><code class="ph codeph">AnalyticsDetails.variable.hierarchyBinding[ ].variableSequence</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1715668707-_anno.html"><code class="ph codeph">AnalyticsDetails.variable.mandatory</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2020456524-_anno.html"><code class="ph codeph">AnalyticsDetails.variable.multipleSelections</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_923050150-_anno.html"><code class="ph codeph">AnalyticsDetails.variable.referenceElement</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_802091487_anno.html"><code class="ph codeph">AnalyticsDetails.variable.selectionType</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#HIERARCHY_NODE</code></p>
<p><code class="ph codeph">#INTERVAL</code></p>
<p><code class="ph codeph">#RANGE</code></p>
<p><code class="ph codeph">#SINGLE</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1412905580-_anno.html"><code class="ph codeph">AnalyticsDetails.variable.usageType</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#FILTER</code></p>
<p><code class="ph codeph">#FORMULA</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>

## Consumption-Annotations

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
<td><a href="abencds_1540815607_anno.html"><code class="ph codeph">Consumption.cacheSettings.refreshForbidden</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_66994189_anno.html"><code class="ph codeph">Consumption.cacheSettings.usage</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#CLIENT_CONTROLLED</code></p>
<p><code class="ph codeph">#MANDATORY</code></p>
<p><code class="ph codeph">#NOT_ALLOWED</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1542401044_anno.html"><code class="ph codeph">Consumption.cacheSettings.useNonTransactional</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_710938603-_anno.html"><code class="ph codeph">Consumption.dbHints[ ]</code></a></td>
<td><code class="ph codeph">#VIEW</code></td>
<td><code class="ph codeph">String(1298)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1396898918_anno.html"><code class="ph codeph">Consumption.defaultValue</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1904654104-_anno.html"><code class="ph codeph">Consumption.derivation.binding[ ].targetElement</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1180704550_anno.html"><code class="ph codeph">Consumption.derivation.binding[ ].targetParameter</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1193562477-_anno.html"><code class="ph codeph">Consumption.derivation.binding[ ].type</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#CONSTANT</code></p>
<p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SYSTEM_FIELD</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_922158943_anno.html"><code class="ph codeph">Consumption.derivation.binding[ ].value</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(512)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_351463783-_anno.html"><code class="ph codeph">Consumption.derivation.lookupEntity</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">EntityRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1339521172-_anno.html"><code class="ph codeph">Consumption.derivation.pfcgMapping</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1413788360-_anno.html"><code class="ph codeph">Consumption.derivation.resultAggregation</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#AVG</code></p>
<p><code class="ph codeph">#COUNT_DISTINCT</code></p>
<p><code class="ph codeph">#MAX</code></p>
<p><code class="ph codeph">#MIN</code></p>
<p><code class="ph codeph">#SUM</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1524598949_anno.html"><code class="ph codeph">Consumption.derivation.resultAggregationHigh</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#AVG</code></p>
<p><code class="ph codeph">#COUNT_DISTINCT</code></p>
<p><code class="ph codeph">#MAX</code></p>
<p><code class="ph codeph">#MIN</code></p>
<p><code class="ph codeph">#SUM</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_913041005_anno.html"><code class="ph codeph">Consumption.derivation.resultElement</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2091380562_anno.html"><code class="ph codeph">Consumption.derivation.resultElementHigh</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1854637833_anno.html"><code class="ph codeph">Consumption.derivation.resultHierarchyNode.mapping[ ].hierarchyElement</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1606829147_anno.html"><code class="ph codeph">Consumption.derivation.resultHierarchyNode.mapping[ ].lookupElement</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2076986893_anno.html"><code class="ph codeph">Consumption.derivation.resultHierarchyNode.nodeTypeElement</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1346100757_anno.html"><code class="ph codeph">Consumption.dynamicLabel.binding[ ].element</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1540292092-_anno.html"><code class="ph codeph">Consumption.dynamicLabel.binding[ ].format</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#KEY</code></p>
<p><code class="ph codeph">#KEY_CONCATENATED</code></p>
<p><code class="ph codeph">#KEY_INTERNAL</code></p>
<p><code class="ph codeph">#TEXT</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1633227914_anno.html"><code class="ph codeph">Consumption.dynamicLabel.binding[ ].index</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2079780457_anno.html"><code class="ph codeph">Consumption.dynamicLabel.binding[ ].length</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_595704331_anno.html"><code class="ph codeph">Consumption.dynamicLabel.binding[ ].offset</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_31561499-_anno.html"><code class="ph codeph">Consumption.dynamicLabel.binding[ ].parameter</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ParameterRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_874563402-_anno.html"><code class="ph codeph">Consumption.dynamicLabel.binding[ ].replaceWith</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(11)</code></td>
<td><p><code class="ph codeph">#DIFFERENCE</code></p>
<p><code class="ph codeph">#HIGH</code></p>
<p><code class="ph codeph">#LOW</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_456525016-_anno.html"><code class="ph codeph">Consumption.dynamicLabel.label</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_657148619_anno.html"><code class="ph codeph">Consumption.filter.businessDate.at</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1645754370_anno.html"><code class="ph codeph">Consumption.filter.defaultHierarchyNode.node[ ].element</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1562025248-_anno.html"><code class="ph codeph">Consumption.filter.defaultHierarchyNode.node[ ].value</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(512)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1532918077_anno.html"><code class="ph codeph">Consumption.filter.defaultHierarchyNode.nodeType</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_467685227-_anno.html"><code class="ph codeph">Consumption.filter.defaultValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1959431186_anno.html"><code class="ph codeph">Consumption.filter.defaultValueHigh</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_250664068_anno.html"><code class="ph codeph">Consumption.filter.hidden</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1285144265-_anno.html"><code class="ph codeph">Consumption.filter.hierarchyAssociation</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">AssociationRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1575871936-_anno.html"><code class="ph codeph">Consumption.filter.hierarchyBinding[ ].type</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#CONSTANT</code></p>
<p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SYSTEM_FIELD</code></p>
<p><code class="ph codeph">#USER_INPUT</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_691490181_anno.html"><code class="ph codeph">Consumption.filter.hierarchyBinding[ ].value</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(512)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_835409933_anno.html"><code class="ph codeph">Consumption.filter.hierarchyBinding[ ].variableSequence</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1041639879-_anno.html"><code class="ph codeph">Consumption.filter.mandatory</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_370562965-_anno.html"><code class="ph codeph">Consumption.filter.multipleSelections</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1846298436-_anno.html"><code class="ph codeph">Consumption.filter.selectionType</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#HIERARCHY_NODE</code></p>
<p><code class="ph codeph">#INTERVAL</code></p>
<p><code class="ph codeph">#RANGE</code></p>
<p><code class="ph codeph">#SINGLE</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_207868793_anno.html"><code class="ph codeph">Consumption.hidden</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_165233041_anno.html"><code class="ph codeph">Consumption.hierarchyNodeSelection.defaultHierarchyNode.node[ ].element</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2133955186-_anno.html"><code class="ph codeph">Consumption.hierarchyNodeSelection.defaultHierarchyNode.node[ ].value</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(512)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1690282172-_anno.html"><code class="ph codeph">Consumption.hierarchyNodeSelection.defaultHierarchyNode.nodeType</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1142889310-_anno.html"><code class="ph codeph">Consumption.hierarchyNodeSelection.hierarchyBinding[ ].type</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#CONSTANT</code></p>
<p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SYSTEM_FIELD</code></p>
<p><code class="ph codeph">#USER_INPUT</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1730821167_anno.html"><code class="ph codeph">Consumption.hierarchyNodeSelection.hierarchyBinding[ ].value</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">String(512)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1510613406_anno.html"><code class="ph codeph">Consumption.hierarchyNodeSelection.hierarchyBinding[ ].variableSequence</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1535740973-_anno.html"><code class="ph codeph">Consumption.hierarchyNodeSelection.hierarchyElement</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1394995008_anno.html"><code class="ph codeph">Consumption.hierarchyNodeSelection.multipleSelections</code></a></td>
<td><code class="ph codeph">#PARAMETER</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_443217666_anno.html"><code class="ph codeph">Consumption.ranked</code></a></td>
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
<td><a href="abencds_226548257-_anno.html"><code class="ph codeph">Consumption.semanticObject</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1706614704_anno.html"><code class="ph codeph">Consumption.semanticObjectMapping.additionalBinding[ ].element</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(40)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_745512240-_anno.html"><code class="ph codeph">Consumption.semanticObjectMapping.additionalBinding[ ].localElement</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1783365650_anno.html"><code class="ph codeph">Consumption.semanticObjectMapping.element</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(40)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_27509916-_anno.html"><code class="ph codeph">Consumption.valueHelpDefault.binding.usage</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#FILTER</code></p>
<p><code class="ph codeph">#FILTER_AND_DISPLAY</code></p>
<p><code class="ph codeph">#FILTER_AND_RESULT</code></p>
<p><code class="ph codeph">#RESULT</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1864856196-_anno.html"><code class="ph codeph">Consumption.valueHelpDefault.display</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_884538153-_anno.html"><code class="ph codeph">Consumption.valueHelpDefault.fetchValues</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#AUTOMATICALLY_WHEN_DISPLAYED</code></p>
<p><code class="ph codeph">#ON_EXPLICIT_REQUEST</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1455457562-_anno.html"><code class="ph codeph">Consumption.valueHelpDefault.initialValueIsSignificant</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_805715173_anno.html"><code class="ph codeph">Consumption.valueHelpDefinition[ ].additionalBinding[ ].element</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">String(40)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1228689791-_anno.html"><code class="ph codeph">Consumption.valueHelpDefinition[ ].additionalBinding[ ].localConstant</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">String(255)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_274352458-_anno.html"><code class="ph codeph">Consumption.valueHelpDefinition[ ].additionalBinding[ ].localElement</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_945672507_anno.html"><code class="ph codeph">Consumption.valueHelpDefinition[ ].additionalBinding[ ].localParameter</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">ParameterRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1532597711-_anno.html"><code class="ph codeph">Consumption.valueHelpDefinition[ ].additionalBinding[ ].parameter</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">String(40)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1441351652_anno.html"><code class="ph codeph">Consumption.valueHelpDefinition[ ].additionalBinding[ ].usage</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#FILTER</code></p>
<p><code class="ph codeph">#FILTER_AND_DISPLAY</code></p>
<p><code class="ph codeph">#FILTER_AND_RESULT</code></p>
<p><code class="ph codeph">#RESULT</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2114743873_anno.html"><code class="ph codeph">Consumption.valueHelpDefinition[ ].distinctValues</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_517749277_anno.html"><code class="ph codeph">Consumption.valueHelpDefinition[ ].enabled</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1864468220_anno.html"><code class="ph codeph">Consumption.valueHelpDefinition[ ].entity.element</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">String(40)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1955238469-_anno.html"><code class="ph codeph">Consumption.valueHelpDefinition[ ].entity.name</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">EntityRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1197602852-_anno.html"><code class="ph codeph">Consumption.valueHelpDefinition[ ].label</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1501489672_anno.html"><code class="ph codeph">Consumption.valueHelpDefinition[ ].presentationVariantQualifier</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_431826238-_anno.html"><code class="ph codeph">Consumption.valueHelpDefinition[ ].qualifier</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1546657336_anno.html"><code class="ph codeph">Consumption.valueHelpDefinition[ ].useForValidation</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>

## DataIntegration-Annotations

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
<td><a href="abencds_698663424_anno.html"><code class="ph codeph">DataIntegration.dataProduct.category</code></a></td>
<td><code class="ph codeph">#SERVICE</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#ANALYTICAL</code></p>
<p><code class="ph codeph">#BUSINESS_OBJECT</code></p>
<p><code class="ph codeph">#OTHER</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1781823284_anno.html"><code class="ph codeph">DataIntegration.dataProduct.customDataProvider.implementedBy</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(255)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2129591621_anno.html"><code class="ph codeph">DataIntegration.dataProduct.name</code></a></td>
<td><code class="ph codeph">#SERVICE</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_458873111-_anno.html"><code class="ph codeph">DataIntegration.dataProduct.outputPorts[ ].service</code></a></td>
<td><code class="ph codeph">#SERVICE</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_238239693-_anno.html"><code class="ph codeph">DataIntegration.dataProduct.release.successors[ ].service</code></a></td>
<td><code class="ph codeph">#SERVICE</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1329702853_anno.html"><code class="ph codeph">DataIntegration.dataProduct.release.version.major</code></a></td>
<td><code class="ph codeph">#SERVICE</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1912854538-_anno.html"><code class="ph codeph">DataIntegration.dataProduct.release.version.minor</code></a></td>
<td><code class="ph codeph">#SERVICE</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1872835334-_anno.html"><code class="ph codeph">DataIntegration.dataProduct.release.version.patch</code></a></td>
<td><code class="ph codeph">#SERVICE</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1620739584-_anno.html"><code class="ph codeph">DataIntegration.dataProduct.transformTo</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#BOOLEAN</code></p>
<p><code class="ph codeph">#DATE</code></p>
<p><code class="ph codeph">#DATETIME</code></p>
<p><code class="ph codeph">#DECIMAL</code></p>
<p><code class="ph codeph">#STRING</code></p>
<p><code class="ph codeph">#TIME</code></p>
<p><code class="ph codeph">#TIMESTAMP</code></p>
<p><code class="ph codeph">#UUID</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1407986582-_anno.html"><code class="ph codeph">DataIntegration.dataProduct.type</code></a></td>
<td><code class="ph codeph">#SERVICE</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#DERIVED</code></p>
<p><code class="ph codeph">#PRIMARY</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1249954665_anno.html"><code class="ph codeph">DataIntegration.deltaReplication.ignoredDataSources[ ]</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_994227313-_anno.html"><code class="ph codeph">DataIntegration.deltaReplication.intended</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
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

## DefaultAggregation-Annotations

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
<td><a href="abencds_1815801967_anno.html"><code class="ph codeph">DefaultAggregation</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#AVG</code></p>
<p><code class="ph codeph">#COUNT</code></p>
<p><code class="ph codeph">#COUNT_DISTINCT</code></p>
<p><code class="ph codeph">#FORMULA</code></p>
<p><code class="ph codeph">#MAX</code></p>
<p><code class="ph codeph">#MIN</code></p>
<p><code class="ph codeph">#NONE</code></p>
<p><code class="ph codeph">#SUM</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>

## EnterpriseSearch-Annotations

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
<td><a href="abencds_821107140_anno.html"><code class="ph codeph">EnterpriseSearch.filteringAttribute.caseInsensitiveAggregation</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1653445419-_anno.html"><code class="ph codeph">EnterpriseSearch.filteringAttribute.considerNullValues</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_790523918_anno.html"><code class="ph codeph">EnterpriseSearch.filteringAttribute.default</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_107008934-_anno.html"><code class="ph codeph">EnterpriseSearch.filteringAttribute.displayPosition</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2023162591-_anno.html"><code class="ph codeph">EnterpriseSearch.filteringFacet.caseInsensitiveAggregation</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_211393441-_anno.html"><code class="ph codeph">EnterpriseSearch.filteringFacet.collapse</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_292724122_anno.html"><code class="ph codeph">EnterpriseSearch.filteringFacet.complexFilter</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_546378851_anno.html"><code class="ph codeph">EnterpriseSearch.filteringFacet.considerNullValues</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1899861934_anno.html"><code class="ph codeph">EnterpriseSearch.filteringFacet.dateIntervalDefinition</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(10)</code></td>
<td><p><code class="ph codeph">#FIVE_YEARS</code></p>
<p><code class="ph codeph">#ONE_YEAR</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1873115543_anno.html"><code class="ph codeph">EnterpriseSearch.filteringFacet.default</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1949728172_anno.html"><code class="ph codeph">EnterpriseSearch.filteringFacet.displayPosition</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1916299268_anno.html"><code class="ph codeph">EnterpriseSearch.filteringFacet.iconUrl</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_743834510_anno.html"><code class="ph codeph">EnterpriseSearch.filteringFacet.noIntervals</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_826819764_anno.html"><code class="ph codeph">EnterpriseSearch.filteringFacet.numberOfValues</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_550889622_anno.html"><code class="ph codeph">EnterpriseSearch.filteringFacet.order.by</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><p><code class="ph codeph">#FILTER_ELEMENT_LABEL</code></p>
<p><code class="ph codeph">#FILTER_ELEMENT_VALUE</code></p>
<p><code class="ph codeph">#NUMBER_OF_HITS</code></p></td>
<td><code class="ph codeph">#NUMBER_OF_HITS</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1002432260_anno.html"><code class="ph codeph">EnterpriseSearch.filteringFacet.order.byReference</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_328055812_anno.html"><code class="ph codeph">EnterpriseSearch.filteringFacet.order.direction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(4)</code></td>
<td><p><code class="ph codeph">#ASC</code></p>
<p><code class="ph codeph">#DESC</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_525210926-_anno.html"><code class="ph codeph">EnterpriseSearch.freeStyleField.importance</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(6)</code></td>
<td><p><code class="ph codeph">#HIGH</code></p>
<p><code class="ph codeph">#LOW</code></p>
<p><code class="ph codeph">#MEDIUM</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1827692517-_anno.html"><code class="ph codeph">EnterpriseSearch.freeStyleField.withAutoCompletion</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1280040647_anno.html"><code class="ph codeph">EnterpriseSearch.model</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_25459512-_anno.html"><code class="ph codeph">EnterpriseSearch.modelName</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1749113809_anno.html"><code class="ph codeph">EnterpriseSearch.modelNamePlural</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1434397866-_anno.html"><code class="ph codeph">EnterpriseSearch.navigation.intentBased.semanticObject</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_772988979_anno.html"><code class="ph codeph">EnterpriseSearch.navigation.mailApp</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1121305493_anno.html"><code class="ph codeph">EnterpriseSearch.navigation.telephoneApp</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_978621620-_anno.html"><code class="ph codeph">EnterpriseSearch.navigation.urlBased.urlField</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1190380558-_anno.html"><code class="ph codeph">EnterpriseSearch.nls.alternativeNames[ ]</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p></td>
<td><code class="ph codeph">String(128)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1022957433_anno.html"><code class="ph codeph">EnterpriseSearch.nls.boolean.falseValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1488939870-_anno.html"><code class="ph codeph">EnterpriseSearch.nls.boolean.trueValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_908968922_anno.html"><code class="ph codeph">EnterpriseSearch.nls.boolean.unknownValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_405857169-_anno.html"><code class="ph codeph">EnterpriseSearch.nls.compoundElements[ ].alternativeNames[ ]</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(128)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1004946012_anno.html"><code class="ph codeph">EnterpriseSearch.nls.compoundElements[ ].elements[ ]</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1344331421_anno.html"><code class="ph codeph">EnterpriseSearch.nls.compoundElements[ ].name</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(128)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_689480502_anno.html"><code class="ph codeph">EnterpriseSearch.nls.notRelevant</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1808548897-_anno.html"><code class="ph codeph">EnterpriseSearch.nls.valueEnumeration.entityBased.codeElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_794742634_anno.html"><code class="ph codeph">EnterpriseSearch.nls.valueEnumeration.entityBased.entity</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">EntityRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_29787506-_anno.html"><code class="ph codeph">EnterpriseSearch.nls.valueEnumeration.entityBased.textElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2086819586-_anno.html"><code class="ph codeph">EnterpriseSearch.nls.valueEnumeration.standard</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1912468767_anno.html"><code class="ph codeph">EnterpriseSearch.nls.valueExamples[ ]</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(128)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1229344236-_anno.html"><code class="ph codeph">EnterpriseSearch.nls.variantElements[ ].alternativeNames[ ]</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(128)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_735964257-_anno.html"><code class="ph codeph">EnterpriseSearch.nls.variantElements[ ].elements[ ]</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1677138952-_anno.html"><code class="ph codeph">EnterpriseSearch.nls.variantElements[ ].name</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(128)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_518284083_anno.html"><code class="ph codeph">EnterpriseSearch.responseField.contactPhoto</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_321204668_anno.html"><code class="ph codeph">EnterpriseSearch.responseField.longText</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1423781203_anno.html"><code class="ph codeph">EnterpriseSearch.responseField.standard.displayPosition</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_949259184_anno.html"><code class="ph codeph">EnterpriseSearch.responseField.thumbNail</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1933209145_anno.html"><code class="ph codeph">EnterpriseSearch.resultItemKey[ ]</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1387304987_anno.html"><code class="ph codeph">EnterpriseSearch.title.subTitleField</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1589352869_anno.html"><code class="ph codeph">EnterpriseSearch.title.titleField</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>

## Event-Annotations

| **Syntax**                                                                | **Scope**  | **Type**      | **Enums** | **Default** | **Text** | **MDE** | **API**                           |
|---------------------------------------------------------------------------|------------|---------------|-----------|-------------|----------|---------|-----------------------------------|
| [`Event.context.attribute`](abencds_2123008750-_anno.md)                | `#ELEMENT` | `String(20)`  | `-`       | `-`         | `-`      | `X`     | `RELEASED_FOR_SAP_CLOUD_PLATFORM` |
| [`Event.context.position`](abencds_123886785-_anno.md)                  | `#ELEMENT` | `Integer`     | `-`       | `-`         | `-`      | `X`     | `RELEASED_FOR_SAP_CLOUD_PLATFORM` |
| [`Event.element.externalName`](abencds_1689242704_anno.md)              | `#ELEMENT` | `String(128)` | `-`       | `-`         | `-`      | `-`     | `RELEASED_FOR_SAP_CLOUD_PLATFORM` |
| [`Event.previousValue.element`](abencds_207123953_anno.md)              | `#ELEMENT` | `ElementRef`  | `-`       | `-`         | `-`      | `-`     | `RELEASED_FOR_SAP_CLOUD_PLATFORM` |
| [`Event.qualifiesEventType`](abencds_992525611_anno.md)                 | `#ELEMENT` | `Boolean`     | `-`       | `true`      | `-`      | `-`     | `RELEASED_FOR_SAP_CLOUD_PLATFORM` |
| [`Event.raisedAt.dateTime`](abencds_829829382_anno.md)                  | `#ELEMENT` | `Boolean`     | `-`       | `true`      | `-`      | `-`     | `RELEASED_FOR_SAP_CLOUD_PLATFORM` |
| [`Event.sapObjectNodeTypeKey[ ].aliases[ ]`](abencds_816706202_anno.md) | `#ENTITY`  | `String(30)`  | `-`       | `-`         | `-`      | `-`     | `RELEASED_FOR_SAP_CLOUD_PLATFORM` |
| [`Event.sapObjectNodeTypeKey[ ].element`](abencds_788469658_anno.md)    | `#ENTITY`  | `String(30)`  | `-`       | `-`         | `-`      | `-`     | `RELEASED_FOR_SAP_CLOUD_PLATFORM` |

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
<td><a href="abencds_1631540097_anno.html"><code class="ph codeph">ObjectModel.association.toDerivationFunction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_556934736-_anno.html"><code class="ph codeph">ObjectModel.association.toHierarchy</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_91716332-_anno.html"><code class="ph codeph">ObjectModel.collectiveValueHelp.for.element</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_1108938853-_anno.html"><code class="ph codeph">ObjectModel.dataCategory</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#HIERARCHY</code></p>
<p><code class="ph codeph">#TEXT</code></p>
<p><code class="ph codeph">#VALUE_HELP</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_511174217_anno.html"><code class="ph codeph">ObjectModel.filter.enabled</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_339592116-_anno.html"><code class="ph codeph">ObjectModel.foreignKey.association</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">AssociationRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_472801206-_anno.html"><code class="ph codeph">ObjectModel.leadingEntity.name</code></a></td>
<td><code class="ph codeph">#SERVICE</code></td>
<td><code class="ph codeph">EntityRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_987989212_anno.html"><code class="ph codeph">ObjectModel.modelingPattern</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><p><code class="ph codeph">#ANALYTICAL_CUBE</code></p>
<p><code class="ph codeph">#ANALYTICAL_DIMENSION</code></p>
<p><code class="ph codeph">#ANALYTICAL_DOCUMENT_STORE</code></p>
<p><code class="ph codeph">#ANALYTICAL_FACT</code></p>
<p><code class="ph codeph">#ANALYTICAL_KPI</code></p>
<p><code class="ph codeph">#ANALYTICAL_PARENT_CHILD_HIERARCHY_NODE</code></p>
<p><code class="ph codeph">#ANALYTICAL_QUERY</code></p>
<p><code class="ph codeph">#COLLECTIVE_VALUE_HELP</code></p>
<p><code class="ph codeph">#DATA_STRUCTURE</code></p>
<p><code class="ph codeph">#DERIVATION_FUNCTION</code></p>
<p><code class="ph codeph">#ENTERPRISE_SEARCH_PROVIDER</code></p>
<p><code class="ph codeph">#EXTERNAL_DATA_PROVIDER</code></p>
<p><code class="ph codeph">#LANGUAGE_DEPENDENT_TEXT</code></p>
<p><code class="ph codeph">#NONE</code></p>
<p><code class="ph codeph">#OUTPUT_EMAIL_DATA_PROVIDER</code></p>
<p><code class="ph codeph">#OUTPUT_FORM_DATA_PROVIDER</code></p>
<p><code class="ph codeph">#OUTPUT_PARAMETER_DETERMINATION_DATA_SOURCE</code></p>
<p><code class="ph codeph">#PARENT_CHILD_HIERARCHY_NODE_PROVIDER</code></p>
<p><code class="ph codeph">#SITUATION_ANCHOR</code></p>
<p><code class="ph codeph">#SITUATION_DATACONTEXT</code></p>
<p><code class="ph codeph">#SITUATION_TRIGGER</code></p>
<p><code class="ph codeph">#TRANSACTIONAL_ENTITY</code></p>
<p><code class="ph codeph">#TRANSACTIONAL_INTERFACE</code></p>
<p><code class="ph codeph">#TRANSACTIONAL_PROJECTED_ENTITY</code></p>
<p><code class="ph codeph">#TRANSACTIONAL_QUERY</code></p>
<p><code class="ph codeph">#UNIT_CONVERION_RATE</code></p>
<p><code class="ph codeph">#VALUE_HELP_PROVIDER</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_902373299-_anno.html"><code class="ph codeph">ObjectModel.origin[ ].codes[ ]</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_884998118-_anno.html"><code class="ph codeph">ObjectModel.origin[ ].layer</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#CUSTOMER</code></p>
<p><code class="ph codeph">#INDUSTRY</code></p>
<p><code class="ph codeph">#LOCALIZATION</code></p>
<p><code class="ph codeph">#PARTNER</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1541735823-_anno.html"><code class="ph codeph">ObjectModel.query.combinedCountAndDataRetrievalEnabled</code></a></td>
<td><p><code class="ph codeph">#CUSTOM_ENTITY</code></p>
<p><code class="ph codeph">#ENTITY</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_1426106406_anno.html"><code class="ph codeph">ObjectModel.representativeKey</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p></td>
<td><code class="ph codeph">KeyElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1776194829_anno.html"><code class="ph codeph">ObjectModel.resultSet.sizeCategory</code></a></td>
<td><p><code class="ph codeph">#CUSTOM_ENTITY</code></p>
<p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p></td>
<td><code class="ph codeph">String(3)</code></td>
<td><p><code class="ph codeph">#XS</code></p>
<p><code class="ph codeph">#XXS</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_83620759-_anno.html"><code class="ph codeph">ObjectModel.sapObjectNodeType.name</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_1392253137-_anno.html"><code class="ph codeph">ObjectModel.sapObjectNodeTypeReference</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_969786454-_anno.html"><code class="ph codeph">ObjectModel.semanticKey[ ]</code></a></td>
<td><p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#TABLE_FUNCTION</code></p></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_953677833-_anno.html"><code class="ph codeph">ObjectModel.sort.enabled</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_257610249-_anno.html"><code class="ph codeph">ObjectModel.sort.transformedBy</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(255)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_684104273-_anno.html"><code class="ph codeph">ObjectModel.supportedCapabilities[ ]</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><p><code class="ph codeph">#ANALYTICAL_DIMENSION</code></p>
<p><code class="ph codeph">#ANALYTICAL_DOCUMENT_STORE</code></p>
<p><code class="ph codeph">#ANALYTICAL_KPI</code></p>
<p><code class="ph codeph">#ANALYTICAL_PARENT_CHILD_HIERARCHY_NODE</code></p>
<p><code class="ph codeph">#ANALYTICAL_PROVIDER</code></p>
<p><code class="ph codeph">#ANALYTICAL_QUERY</code></p>
<p><code class="ph codeph">#CDS_MODELING_ASSOCIATION_TARGET</code></p>
<p><code class="ph codeph">#CDS_MODELING_DATA_SOURCE</code></p>
<p><code class="ph codeph">#COLLECTIVE_VALUE_HELP</code></p>
<p><code class="ph codeph">#DATA_STRUCTURE</code></p>
<p><code class="ph codeph">#DERIVATION_FUNCTION</code></p>
<p><code class="ph codeph">#ENTERPRISE_SEARCH_PROVIDER</code></p>
<p><code class="ph codeph">#EXTERNAL_DATA_PROVIDER</code></p>
<p><code class="ph codeph">#EXTRACTION_DATA_SOURCE</code></p>
<p><code class="ph codeph">#KEY_USER_COPYING_TEMPLATE</code></p>
<p><code class="ph codeph">#LANGUAGE_DEPENDENT_TEXT</code></p>
<p><code class="ph codeph">#ODM_COMPLIANT_PROVIDER</code></p>
<p><code class="ph codeph">#OUTPUT_EMAIL_DATA_PROVIDER</code></p>
<p><code class="ph codeph">#OUTPUT_FORM_DATA_PROVIDER</code></p>
<p><code class="ph codeph">#OUTPUT_PARAMETER_DETERMINATION_DATA_SOURCE</code></p>
<p><code class="ph codeph">#PARENT_CHILD_HIERARCHY_NODE_PROVIDER</code></p>
<p><code class="ph codeph">#SEARCHABLE_ENTITY</code></p>
<p><code class="ph codeph">#SITUATION_ANCHOR</code></p>
<p><code class="ph codeph">#SITUATION_DATACONTEXT</code></p>
<p><code class="ph codeph">#SITUATION_TRIGGER</code></p>
<p><code class="ph codeph">#SQL_DATA_SOURCE</code></p>
<p><code class="ph codeph">#TRANSACTIONAL_PROVIDER</code></p>
<p><code class="ph codeph">#UI_PROVIDER_PROJECTION_SOURCE</code></p>
<p><code class="ph codeph">#UNIT_CONVERION_RATE</code></p>
<p><code class="ph codeph">#VALUE_HELP_PROVIDER</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_155024245-_anno.html"><code class="ph codeph">ObjectModel.text.association</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">AssociationRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_81808902-_anno.html"><code class="ph codeph">ObjectModel.text.control</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p></td>
<td><code class="ph codeph">String(60)</code></td>
<td><p><code class="ph codeph">#ASSOCIATED_TEXT_UI_HIDDEN</code></p>
<p><code class="ph codeph">#NONE</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1468318600_anno.html"><code class="ph codeph">ObjectModel.text.element[ ]</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1465379351_anno.html"><code class="ph codeph">ObjectModel.text.reference.association</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">AssociationRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_486564725-_anno.html"><code class="ph codeph">ObjectModel.unitConversionRate.association</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">AssociationRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_777237863_anno.html"><code class="ph codeph">ObjectModel.value.derivedFrom[ ]</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_1465014012-_anno.html"><code class="ph codeph">ObjectModel.virtualElementDependsOn[ ]</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
</tbody>
</table>

## OData-Annotations

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
<td><a href="abencds_452750455_anno.html"><code class="ph codeph">OData.action[ ].localName</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_99617042_anno.html"><code class="ph codeph">OData.action[ ].name</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(128)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_626623472_anno.html"><code class="ph codeph">OData.applySupportedForAggregation</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#FULL</code></p>
<p><code class="ph codeph">#NONE</code></p>
<p><code class="ph codeph">#RESTRICTED</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_455433406-_anno.html"><code class="ph codeph">OData.draftSessionSupported</code></a></td>
<td><code class="ph codeph">#SERVICE</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_814310721-_anno.html"><code class="ph codeph">OData.entitySet.name</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_1422061889-_anno.html"><code class="ph codeph">OData.entityType.name</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(128)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_1179260535_anno.html"><code class="ph codeph">OData.etag</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_253752354-_anno.html"><code class="ph codeph">OData.hierarchy.recursiveHierarchy[ ].entity.name</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">EntityRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_311850322-_anno.html"><code class="ph codeph">OData.property.name</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(128)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_1730876588_anno.html"><code class="ph codeph">OData.property.valueControl</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_1996983346-_anno.html"><code class="ph codeph">OData.schema.name</code></a></td>
<td><code class="ph codeph">#SERVICE</code></td>
<td><code class="ph codeph">String(128)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
</tbody>
</table>

## Search-Annotations

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
<td><a href="abencds_1489485690-_anno.html"><code class="ph codeph">Search.defaultSearchElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_294491798-_anno.html"><code class="ph codeph">Search.fuzzinessThreshold</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Decimal(3,2)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1895951254-_anno.html"><code class="ph codeph">Search.mode</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><code class="ph codeph">#IDENTIFIER</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1594409060-_anno.html"><code class="ph codeph">Search.ranking</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(6)</code></td>
<td><p><code class="ph codeph">#HIGH</code></p>
<p><code class="ph codeph">#LOW</code></p>
<p><code class="ph codeph">#MEDIUM</code></p></td>
<td><code class="ph codeph">#MEDIUM</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1567884046_anno.html"><code class="ph codeph">Search.searchable</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_568724386-_anno.html"><code class="ph codeph">Search.termMappingDictionary</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(128)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1460214714_anno.html"><code class="ph codeph">Search.termMappingListId[ ]</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(32)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_284009624_anno.html"><code class="ph codeph">Search.textIndex.required</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
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
<td><a href="abencds_1461511500_anno.html"><code class="ph codeph">Semantics.address.city</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_266976788-_anno.html"><code class="ph codeph">Semantics.address.country</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1342434817_anno.html"><code class="ph codeph">Semantics.address.label</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1327030582_anno.html"><code class="ph codeph">Semantics.address.number</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1102495668-_anno.html"><code class="ph codeph">Semantics.address.postBox</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_689303788-_anno.html"><code class="ph codeph">Semantics.address.region</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_694562234_anno.html"><code class="ph codeph">Semantics.address.street</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_15352966-_anno.html"><code class="ph codeph">Semantics.address.streetNoNumber</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1287496915_anno.html"><code class="ph codeph">Semantics.address.subRegion</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_157700015-_anno.html"><code class="ph codeph">Semantics.address.type[ ]</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">String(10)</code></td>
<td><p><code class="ph codeph">#HOME</code></p>
<p><code class="ph codeph">#OTHER</code></p>
<p><code class="ph codeph">#PREF</code></p>
<p><code class="ph codeph">#WORK</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1448814198_anno.html"><code class="ph codeph">Semantics.address.zipCode</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2097062483-_anno.html"><code class="ph codeph">Semantics.baseUnitOfMeasure</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1161590409_anno.html"><code class="ph codeph">Semantics.booleanIndicator</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_845229671-_anno.html"><code class="ph codeph">Semantics.businessDate.at</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1488069366_anno.html"><code class="ph codeph">Semantics.businessDate.from</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1884225121_anno.html"><code class="ph codeph">Semantics.businessDate.to</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_493560921_anno.html"><code class="ph codeph">Semantics.calendar.dayOfMonth</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1867100602_anno.html"><code class="ph codeph">Semantics.calendar.dayOfYear</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_82821257-_anno.html"><code class="ph codeph">Semantics.calendar.halfyear</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1974309554-_anno.html"><code class="ph codeph">Semantics.calendar.month</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_177548655_anno.html"><code class="ph codeph">Semantics.calendar.quarter</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1677800518_anno.html"><code class="ph codeph">Semantics.calendar.week</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2066141519-_anno.html"><code class="ph codeph">Semantics.calendar.year</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1248825398-_anno.html"><code class="ph codeph">Semantics.calendar.yearHalfyear</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_7695013-_anno.html"><code class="ph codeph">Semantics.calendar.yearMonth</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1907964787-_anno.html"><code class="ph codeph">Semantics.calendar.yearQuarter</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_698696316-_anno.html"><code class="ph codeph">Semantics.calendar.yearWeek</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_166770316_anno.html"><code class="ph codeph">Semantics.conversionRate.denominator</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_834051776-_anno.html"><code class="ph codeph">Semantics.conversionRate.numerator</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_358510380_anno.html"><code class="ph codeph">Semantics.dateTime</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1424766515-_anno.html"><code class="ph codeph">Semantics.durationInDays</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_883019560-_anno.html"><code class="ph codeph">Semantics.durationInHours</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_189899413-_anno.html"><code class="ph codeph">Semantics.durationInMinutes</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2064850478_anno.html"><code class="ph codeph">Semantics.durationInSeconds</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1631214101_anno.html"><code class="ph codeph">Semantics.eMail.address</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_90607315_anno.html"><code class="ph codeph">Semantics.eMail.bcc</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1570788266-_anno.html"><code class="ph codeph">Semantics.eMail.body</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1890091459_anno.html"><code class="ph codeph">Semantics.eMail.cc</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1058208108-_anno.html"><code class="ph codeph">Semantics.eMail.from</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1565627958_anno.html"><code class="ph codeph">Semantics.eMail.keywords</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1046616751_anno.html"><code class="ph codeph">Semantics.eMail.received</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_765473691_anno.html"><code class="ph codeph">Semantics.eMail.sender</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1749414930-_anno.html"><code class="ph codeph">Semantics.eMail.subject</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2090682750_anno.html"><code class="ph codeph">Semantics.eMail.to</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_181800755-_anno.html"><code class="ph codeph">Semantics.eMail.type[ ]</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">String(10)</code></td>
<td><p><code class="ph codeph">#HOME</code></p>
<p><code class="ph codeph">#OTHER</code></p>
<p><code class="ph codeph">#PREF</code></p>
<p><code class="ph codeph">#WORK</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1919799078-_anno.html"><code class="ph codeph">Semantics.fiscal.dayOfYear</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_950905845-_anno.html"><code class="ph codeph">Semantics.fiscal.period</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_141738638-_anno.html"><code class="ph codeph">Semantics.fiscal.quarter</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1976141743-_anno.html"><code class="ph codeph">Semantics.fiscal.week</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1794007718_anno.html"><code class="ph codeph">Semantics.fiscal.year</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1656506917-_anno.html"><code class="ph codeph">Semantics.fiscal.yearPeriod</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1896152647_anno.html"><code class="ph codeph">Semantics.fiscal.yearQuarter</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1664704275-_anno.html"><code class="ph codeph">Semantics.fiscal.yearVariant</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1247688371-_anno.html"><code class="ph codeph">Semantics.fiscal.yearWeek</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1321146933-_anno.html"><code class="ph codeph">Semantics.imageUrl</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_230394003-_anno.html"><code class="ph codeph">Semantics.language</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_514907485_anno.html"><code class="ph codeph">Semantics.largeObject.acceptableMimeTypes[ ]</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(255)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1095859513-_anno.html"><code class="ph codeph">Semantics.largeObject.cacheControl.maxAge</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#LONG</code></p>
<p><code class="ph codeph">#MEDIUM</code></p>
<p><code class="ph codeph">#SHORT</code></p>
<p><code class="ph codeph">#VERY_LONG</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_362794121_anno.html"><code class="ph codeph">Semantics.largeObject.contentDispositionPreference</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#ATTACHMENT</code></p>
<p><code class="ph codeph">#INLINE</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_305473728_anno.html"><code class="ph codeph">Semantics.largeObject.fileName</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1459539484_anno.html"><code class="ph codeph">Semantics.largeObject.mimeType</code></a></td>
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
<td><a href="abencds_26368417-_anno.html"><code class="ph codeph">Semantics.mimeType</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1167533843-_anno.html"><code class="ph codeph">Semantics.name.additionalName</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1249035756_anno.html"><code class="ph codeph">Semantics.name.familyName</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1394730853_anno.html"><code class="ph codeph">Semantics.name.fullName</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_221475067-_anno.html"><code class="ph codeph">Semantics.name.givenName</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1382573248_anno.html"><code class="ph codeph">Semantics.name.jobTitle</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1674339503_anno.html"><code class="ph codeph">Semantics.name.nickName</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1789297569_anno.html"><code class="ph codeph">Semantics.name.prefix</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1286046449_anno.html"><code class="ph codeph">Semantics.name.suffix</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_404676902-_anno.html"><code class="ph codeph">Semantics.nullValueIndicatorFor</code></a></td>
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
<td><a href="abencds_39683004_anno.html"><code class="ph codeph">Semantics.organization.name</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_186087376_anno.html"><code class="ph codeph">Semantics.organization.role</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2134511127-_anno.html"><code class="ph codeph">Semantics.organization.unit</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_864612737-_anno.html"><code class="ph codeph">Semantics.quantity.unitOfMeasureIsoCode</code></a></td>
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
<td><a href="abencds_1552454084-_anno.html"><code class="ph codeph">Semantics.quantity.unitOfMeasureSapCode</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1718413646-_anno.html"><code class="ph codeph">Semantics.signReversalIndicator</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1655798361_anno.html"><code class="ph codeph">Semantics.spatialData.srid.value</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(20)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_982060907_anno.html"><code class="ph codeph">Semantics.systemDateTime.createdAt</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1631854850-_anno.html"><code class="ph codeph">Semantics.systemDateTime.lastChangedAt</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_425922347-_anno.html"><code class="ph codeph">Semantics.systemDateTime.localInstanceLastChangedAt</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_581749929-_anno.html"><code class="ph codeph">Semantics.telephone.type[ ]</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">String(10)</code></td>
<td><p><code class="ph codeph">#CELL</code></p>
<p><code class="ph codeph">#FAX</code></p>
<p><code class="ph codeph">#HOME</code></p>
<p><code class="ph codeph">#PAGER</code></p>
<p><code class="ph codeph">#PREF</code></p>
<p><code class="ph codeph">#TEXT</code></p>
<p><code class="ph codeph">#TEXT_PHONE</code></p>
<p><code class="ph codeph">#VIDEO</code></p>
<p><code class="ph codeph">#VOICE</code></p>
<p><code class="ph codeph">#WORK</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1085868017_anno.html"><code class="ph codeph">Semantics.text</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1314120847-_anno.html"><code class="ph codeph">Semantics.timeZone</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1144633199-_anno.html"><code class="ph codeph">Semantics.timeZoneReference</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1660126530_anno.html"><code class="ph codeph">Semantics.user.createdBy</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_886796743_anno.html"><code class="ph codeph">Semantics.user.lastChangedBy</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1906771207_anno.html"><code class="ph codeph">Semantics.user.localInstanceLastChangedBy</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1437732720-_anno.html"><code class="ph codeph">Semantics.uuid</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p>
<p><code class="ph codeph">#SIMPLE_TYPE</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_679526526_anno.html"><code class="ph codeph">Semantics.valueRange.exclusiveMaximum</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_728965169_anno.html"><code class="ph codeph">Semantics.valueRange.exclusiveMinimum</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_69870256_anno.html"><code class="ph codeph">Semantics.valueRange.maximum</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p></td>
<td><code class="ph codeph">String(1298)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_131711743_anno.html"><code class="ph codeph">Semantics.valueRange.minimum</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p></td>
<td><code class="ph codeph">String(1298)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>

## UI-Annotations

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
<td><a href="abencds_914962098_anno.html"><code class="ph codeph">UI.adaptationHidden</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1695349266_anno.html"><code class="ph codeph">UI.badge.headLine.criticality</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1730511305_anno.html"><code class="ph codeph">UI.badge.headLine.criticalityRepresentation</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#WITHOUT_ICON</code></p>
<p><code class="ph codeph">#WITH_ICON</code></p></td>
<td><code class="ph codeph">#WITHOUT_ICON</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_567007397-_anno.html"><code class="ph codeph">UI.badge.headLine.iconUrl</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1864604074_anno.html"><code class="ph codeph">UI.badge.headLine.label</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1837789293_anno.html"><code class="ph codeph">UI.badge.headLine.targetElement</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1676199671_anno.html"><code class="ph codeph">UI.badge.headLine.type</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#STANDARD</code></p>
<p><code class="ph codeph">#WITH_INTENT_BASED_NAVIGATION</code></p>
<p><code class="ph codeph">#WITH_NAVIGATION_PATH</code></p>
<p><code class="ph codeph">#WITH_URL</code></p></td>
<td><code class="ph codeph">#STANDARD</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_402108909_anno.html"><code class="ph codeph">UI.badge.headLine.url</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_999909159-_anno.html"><code class="ph codeph">UI.badge.headLine.urlTarget</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#BLANK</code></p>
<p><code class="ph codeph">#PARENT</code></p>
<p><code class="ph codeph">#SELF</code></p>
<p><code class="ph codeph">#TOP</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2096337270_anno.html"><code class="ph codeph">UI.badge.headLine.value</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2105013861-_anno.html"><code class="ph codeph">UI.badge.imageUrl</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1791884454_anno.html"><code class="ph codeph">UI.badge.mainInfo.criticality</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1372579104-_anno.html"><code class="ph codeph">UI.badge.mainInfo.criticalityRepresentation</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#WITHOUT_ICON</code></p>
<p><code class="ph codeph">#WITH_ICON</code></p></td>
<td><code class="ph codeph">#WITHOUT_ICON</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_276189127_anno.html"><code class="ph codeph">UI.badge.mainInfo.iconUrl</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_977752413_anno.html"><code class="ph codeph">UI.badge.mainInfo.label</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_71348517_anno.html"><code class="ph codeph">UI.badge.mainInfo.targetElement</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_33955392_anno.html"><code class="ph codeph">UI.badge.mainInfo.type</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#STANDARD</code></p>
<p><code class="ph codeph">#WITH_INTENT_BASED_NAVIGATION</code></p>
<p><code class="ph codeph">#WITH_NAVIGATION_PATH</code></p>
<p><code class="ph codeph">#WITH_URL</code></p></td>
<td><code class="ph codeph">#STANDARD</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1831807693-_anno.html"><code class="ph codeph">UI.badge.mainInfo.url</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1526430439_anno.html"><code class="ph codeph">UI.badge.mainInfo.urlTarget</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#BLANK</code></p>
<p><code class="ph codeph">#PARENT</code></p>
<p><code class="ph codeph">#SELF</code></p>
<p><code class="ph codeph">#TOP</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_697784705_anno.html"><code class="ph codeph">UI.badge.mainInfo.value</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1111520315-_anno.html"><code class="ph codeph">UI.badge.secondaryInfo.criticality</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1998465181_anno.html"><code class="ph codeph">UI.badge.secondaryInfo.criticalityRepresentation</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#WITHOUT_ICON</code></p>
<p><code class="ph codeph">#WITH_ICON</code></p></td>
<td><code class="ph codeph">#WITHOUT_ICON</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1794291622_anno.html"><code class="ph codeph">UI.badge.secondaryInfo.iconUrl</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1762658721-_anno.html"><code class="ph codeph">UI.badge.secondaryInfo.label</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2064532820-_anno.html"><code class="ph codeph">UI.badge.secondaryInfo.targetElement</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_374889579_anno.html"><code class="ph codeph">UI.badge.secondaryInfo.type</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#STANDARD</code></p>
<p><code class="ph codeph">#WITH_INTENT_BASED_NAVIGATION</code></p>
<p><code class="ph codeph">#WITH_NAVIGATION_PATH</code></p>
<p><code class="ph codeph">#WITH_URL</code></p></td>
<td><code class="ph codeph">#STANDARD</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_842092241-_anno.html"><code class="ph codeph">UI.badge.secondaryInfo.url</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1787092821-_anno.html"><code class="ph codeph">UI.badge.secondaryInfo.urlTarget</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#BLANK</code></p>
<p><code class="ph codeph">#PARENT</code></p>
<p><code class="ph codeph">#SELF</code></p>
<p><code class="ph codeph">#TOP</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2059403645-_anno.html"><code class="ph codeph">UI.badge.secondaryInfo.value</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_192507551_anno.html"><code class="ph codeph">UI.badge.title.criticality</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_959692017_anno.html"><code class="ph codeph">UI.badge.title.criticalityRepresentation</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#WITHOUT_ICON</code></p>
<p><code class="ph codeph">#WITH_ICON</code></p></td>
<td><code class="ph codeph">#WITHOUT_ICON</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1168687851-_anno.html"><code class="ph codeph">UI.badge.title.iconUrl</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1332695577-_anno.html"><code class="ph codeph">UI.badge.title.label</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_348499779_anno.html"><code class="ph codeph">UI.badge.title.targetElement</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1338816421-_anno.html"><code class="ph codeph">UI.badge.title.type</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#STANDARD</code></p>
<p><code class="ph codeph">#WITH_INTENT_BASED_NAVIGATION</code></p>
<p><code class="ph codeph">#WITH_NAVIGATION_PATH</code></p>
<p><code class="ph codeph">#WITH_URL</code></p></td>
<td><code class="ph codeph">#STANDARD</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_445507210_anno.html"><code class="ph codeph">UI.badge.title.url</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1476290379_anno.html"><code class="ph codeph">UI.badge.title.urlTarget</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#BLANK</code></p>
<p><code class="ph codeph">#PARENT</code></p>
<p><code class="ph codeph">#SELF</code></p>
<p><code class="ph codeph">#TOP</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1556044485-_anno.html"><code class="ph codeph">UI.badge.title.value</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_645917463_anno.html"><code class="ph codeph">UI.badge.typeImageUrl</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1675165992-_anno.html"><code class="ph codeph">UI.chart[ ].actions[ ].dataAction</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_962974385-_anno.html"><code class="ph codeph">UI.chart[ ].actions[ ].invocationGrouping</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#CHANGE_SET</code></p>
<p><code class="ph codeph">#ISOLATED</code></p></td>
<td><code class="ph codeph">#ISOLATED</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1383487403_anno.html"><code class="ph codeph">UI.chart[ ].actions[ ].label</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_934268340-_anno.html"><code class="ph codeph">UI.chart[ ].actions[ ].requiresContext</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_508293081-_anno.html"><code class="ph codeph">UI.chart[ ].actions[ ].semanticObject</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1657074_anno.html"><code class="ph codeph">UI.chart[ ].actions[ ].semanticObjectAction</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_290254702-_anno.html"><code class="ph codeph">UI.chart[ ].actions[ ].type</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#FOR_ACTION</code></p>
<p><code class="ph codeph">#FOR_INTENT_BASED_NAVIGATION</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_133180678-_anno.html"><code class="ph codeph">UI.chart[ ].chartType</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#AREA</code></p>
<p><code class="ph codeph">#AREA_STACKED</code></p>
<p><code class="ph codeph">#AREA_STACKED_100</code></p>
<p><code class="ph codeph">#BAR</code></p>
<p><code class="ph codeph">#BAR_DUAL</code></p>
<p><code class="ph codeph">#BAR_STACKED</code></p>
<p><code class="ph codeph">#BAR_STACKED_100</code></p>
<p><code class="ph codeph">#BAR_STACKED_DUAL</code></p>
<p><code class="ph codeph">#BAR_STACKED_DUAL_100</code></p>
<p><code class="ph codeph">#BUBBLE</code></p>
<p><code class="ph codeph">#BULLET</code></p>
<p><code class="ph codeph">#COLUMN</code></p>
<p><code class="ph codeph">#COLUMN_DUAL</code></p>
<p><code class="ph codeph">#COLUMN_STACKED</code></p>
<p><code class="ph codeph">#COLUMN_STACKED_100</code></p>
<p><code class="ph codeph">#COLUMN_STACKED_DUAL</code></p>
<p><code class="ph codeph">#COLUMN_STACKED_DUAL_100</code></p>
<p><code class="ph codeph">#COMBINATION</code></p>
<p><code class="ph codeph">#COMBINATION_DUAL</code></p>
<p><code class="ph codeph">#COMBINATION_STACKED</code></p>
<p><code class="ph codeph">#COMBINATION_STACKED_DUAL</code></p>
<p><code class="ph codeph">#DONUT</code></p>
<p><code class="ph codeph">#DONUT_100</code></p>
<p><code class="ph codeph">#HEAT_MAP</code></p>
<p><code class="ph codeph">#HORIZONTAL_AREA</code></p>
<p><code class="ph codeph">#HORIZONTAL_AREA_STACKED</code></p>
<p><code class="ph codeph">#HORIZONTAL_AREA_STACKED_100</code></p>
<p><code class="ph codeph">#HORIZONTAL_COMBINATION_DUAL</code></p>
<p><code class="ph codeph">#HORIZONTAL_COMBINATION_STACKED</code></p>
<p><code class="ph codeph">#HORIZONTAL_COMBINATION_STACKED_DUAL</code></p>
<p><code class="ph codeph">#HORIZONTAL_WATERFALL</code></p>
<p><code class="ph codeph">#LINE</code></p>
<p><code class="ph codeph">#LINE_DUAL</code></p>
<p><code class="ph codeph">#PIE</code></p>
<p><code class="ph codeph">#RADAR</code></p>
<p><code class="ph codeph">#SCATTER</code></p>
<p><code class="ph codeph">#TREE_MAP</code></p>
<p><code class="ph codeph">#VERTICAL_BULLET</code></p>
<p><code class="ph codeph">#WATERFALL</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_830899058_anno.html"><code class="ph codeph">UI.chart[ ].description</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1563888131-_anno.html"><code class="ph codeph">UI.chart[ ].dimensionAttributes[ ].dimension</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1802805886_anno.html"><code class="ph codeph">UI.chart[ ].dimensionAttributes[ ].emphasizedValues[ ]</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_921303495-_anno.html"><code class="ph codeph">UI.chart[ ].dimensionAttributes[ ].role</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(10)</code></td>
<td><p><code class="ph codeph">#CATEGORY</code></p>
<p><code class="ph codeph">#CATEGORY2</code></p>
<p><code class="ph codeph">#SERIES</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1503083881_anno.html"><code class="ph codeph">UI.chart[ ].dimensionAttributes[ ].valuesForSequentialColorLevels[ ]</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_869587742_anno.html"><code class="ph codeph">UI.chart[ ].dimensions[ ]</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1033482556-_anno.html"><code class="ph codeph">UI.chart[ ].measureAttributes[ ].asDataPoint</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1708578584_anno.html"><code class="ph codeph">UI.chart[ ].measureAttributes[ ].measure</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1869851323-_anno.html"><code class="ph codeph">UI.chart[ ].measureAttributes[ ].role</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(10)</code></td>
<td><p><code class="ph codeph">#AXIS_1</code></p>
<p><code class="ph codeph">#AXIS_2</code></p>
<p><code class="ph codeph">#AXIS_3</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_479880989_anno.html"><code class="ph codeph">UI.chart[ ].measureAttributes[ ].useSequentialColorLevels</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_802559988-_anno.html"><code class="ph codeph">UI.chart[ ].measures[ ]</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_834052954-_anno.html"><code class="ph codeph">UI.chart[ ].qualifier</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_537532627-_anno.html"><code class="ph codeph">UI.chart[ ].title</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1636411679_anno.html"><code class="ph codeph">UI.connectedFields[ ].actionGroupId</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_467191905-_anno.html"><code class="ph codeph">UI.connectedFields[ ].criticality</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_693412069-_anno.html"><code class="ph codeph">UI.connectedFields[ ].criticalityRepresentation</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#ONLY_ICON</code></p>
<p><code class="ph codeph">#WITHOUT_ICON</code></p>
<p><code class="ph codeph">#WITH_ICON</code></p></td>
<td><code class="ph codeph">#WITHOUT_ICON</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1829592951-_anno.html"><code class="ph codeph">UI.connectedFields[ ].cssDefault.width</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1567577492-_anno.html"><code class="ph codeph">UI.connectedFields[ ].dataAction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1786298792_anno.html"><code class="ph codeph">UI.connectedFields[ ].determining</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2077325348_anno.html"><code class="ph codeph">UI.connectedFields[ ].emphasized</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_679339088-_anno.html"><code class="ph codeph">UI.connectedFields[ ].exclude</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1653713076-_anno.html"><code class="ph codeph">UI.connectedFields[ ].groupLabel</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1483608320_anno.html"><code class="ph codeph">UI.connectedFields[ ].hidden</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1271131525_anno.html"><code class="ph codeph">UI.connectedFields[ ].iconUrl</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1827585618_anno.html"><code class="ph codeph">UI.connectedFields[ ].importance</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(6)</code></td>
<td><p><code class="ph codeph">#HIGH</code></p>
<p><code class="ph codeph">#LOW</code></p>
<p><code class="ph codeph">#MEDIUM</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1739020982-_anno.html"><code class="ph codeph">UI.connectedFields[ ].inline</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1858154951-_anno.html"><code class="ph codeph">UI.connectedFields[ ].invocationGrouping</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#CHANGE_SET</code></p>
<p><code class="ph codeph">#ISOLATED</code></p></td>
<td><code class="ph codeph">#ISOLATED</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_893647883-_anno.html"><code class="ph codeph">UI.connectedFields[ ].isCopyAction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1961572830_anno.html"><code class="ph codeph">UI.connectedFields[ ].isPartOfPreview</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1565071885_anno.html"><code class="ph codeph">UI.connectedFields[ ].label</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_66759668_anno.html"><code class="ph codeph">UI.connectedFields[ ].name</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1932307658-_anno.html"><code class="ph codeph">UI.connectedFields[ ].navigationAvailable</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1541300707-_anno.html"><code class="ph codeph">UI.connectedFields[ ].position</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1917677874_anno.html"><code class="ph codeph">UI.connectedFields[ ].qualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_378626638-_anno.html"><code class="ph codeph">UI.connectedFields[ ].requiresContext</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1996561677_anno.html"><code class="ph codeph">UI.connectedFields[ ].rowSpanForDuplicateValues</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1810848531_anno.html"><code class="ph codeph">UI.connectedFields[ ].semanticObject</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1082094308_anno.html"><code class="ph codeph">UI.connectedFields[ ].semanticObjectAction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1225023223_anno.html"><code class="ph codeph">UI.connectedFields[ ].semanticObjectBinding[ ].element</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1714201843-_anno.html"><code class="ph codeph">UI.connectedFields[ ].semanticObjectBinding[ ].localElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_505983237-_anno.html"><code class="ph codeph">UI.connectedFields[ ].semanticObjectBinding[ ].localParameter</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ParameterRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_108177741_anno.html"><code class="ph codeph">UI.connectedFields[ ].targetElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1970103659_anno.html"><code class="ph codeph">UI.connectedFields[ ].template</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(255)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_788036901-_anno.html"><code class="ph codeph">UI.connectedFields[ ].type</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#AS_ADDRESS</code></p>
<p><code class="ph codeph">#AS_CHART</code></p>
<p><code class="ph codeph">#AS_CONNECTED_FIELDS</code></p>
<p><code class="ph codeph">#AS_CONTACT</code></p>
<p><code class="ph codeph">#AS_DATAPOINT</code></p>
<p><code class="ph codeph">#AS_FIELDGROUP</code></p>
<p><code class="ph codeph">#AS_PRESENTATION_VARIANT</code></p>
<p><code class="ph codeph">#AS_SELECTION_PRESENTATION_VARIANT</code></p>
<p><code class="ph codeph">#FOR_ACTION</code></p>
<p><code class="ph codeph">#FOR_ACTION_GROUP</code></p>
<p><code class="ph codeph">#FOR_INTENT_BASED_NAVIGATION</code></p>
<p><code class="ph codeph">#STANDARD</code></p>
<p><code class="ph codeph">#WITH_ACTION</code></p>
<p><code class="ph codeph">#WITH_ACTION_GROUP</code></p>
<p><code class="ph codeph">#WITH_INTENT_BASED_NAVIGATION</code></p>
<p><code class="ph codeph">#WITH_NAVIGATION_PATH</code></p>
<p><code class="ph codeph">#WITH_URL</code></p></td>
<td><code class="ph codeph">#STANDARD</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1169732948_anno.html"><code class="ph codeph">UI.connectedFields[ ].url</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1603482095-_anno.html"><code class="ph codeph">UI.connectedFields[ ].urlTarget</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#BLANK</code></p>
<p><code class="ph codeph">#PARENT</code></p>
<p><code class="ph codeph">#SELF</code></p>
<p><code class="ph codeph">#TOP</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1318654673_anno.html"><code class="ph codeph">UI.connectedFields[ ].value</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_745516926_anno.html"><code class="ph codeph">UI.connectedFields[ ].valueQualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2041993037-_anno.html"><code class="ph codeph">UI.createHidden</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1635274103_anno.html"><code class="ph codeph">UI.criticalityLabels[ ].criticality</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><p><code class="ph codeph">#CRITICAL</code></p>
<p><code class="ph codeph">#NEGATIVE</code></p>
<p><code class="ph codeph">#POSITIVE</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1370873419-_anno.html"><code class="ph codeph">UI.criticalityLabels[ ].label</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1926435501-_anno.html"><code class="ph codeph">UI.criticalityLabels[ ].qualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1237184411_anno.html"><code class="ph codeph">UI.dataFieldDefault[ ].criticality</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2132440007-_anno.html"><code class="ph codeph">UI.dataFieldDefault[ ].criticalityRepresentation</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#WITHOUT_ICON</code></p>
<p><code class="ph codeph">#WITH_ICON</code></p></td>
<td><code class="ph codeph">#WITHOUT_ICON</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2038351282-_anno.html"><code class="ph codeph">UI.dataFieldDefault[ ].emphasized</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1480481653-_anno.html"><code class="ph codeph">UI.dataFieldDefault[ ].hidden</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_827725976_anno.html"><code class="ph codeph">UI.dataFieldDefault[ ].iconUrl</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1849754568-_anno.html"><code class="ph codeph">UI.dataFieldDefault[ ].importance</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(6)</code></td>
<td><p><code class="ph codeph">#HIGH</code></p>
<p><code class="ph codeph">#LOW</code></p>
<p><code class="ph codeph">#MEDIUM</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1541044164_anno.html"><code class="ph codeph">UI.dataFieldDefault[ ].isPartOfPreview</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_40443436-_anno.html"><code class="ph codeph">UI.dataFieldDefault[ ].label</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1089888552_anno.html"><code class="ph codeph">UI.dataFieldDefault[ ].qualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_558878255_anno.html"><code class="ph codeph">UI.dataFieldDefault[ ].rowSpanForDuplicateValues</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_903726639_anno.html"><code class="ph codeph">UI.dataFieldDefault[ ].semanticObject</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_642868483_anno.html"><code class="ph codeph">UI.dataFieldDefault[ ].semanticObjectAction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_69083963_anno.html"><code class="ph codeph">UI.dataFieldDefault[ ].type</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#STANDARD</code></p>
<p><code class="ph codeph">#WITH_INTENT_BASED_NAVIGATION</code></p>
<p><code class="ph codeph">#WITH_URL</code></p></td>
<td><code class="ph codeph">#STANDARD</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1012445558_anno.html"><code class="ph codeph">UI.dataFieldDefault[ ].url</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1831346677-_anno.html"><code class="ph codeph">UI.dataFieldDefault[ ].urlTarget</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#BLANK</code></p>
<p><code class="ph codeph">#PARENT</code></p>
<p><code class="ph codeph">#SELF</code></p>
<p><code class="ph codeph">#TOP</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_297342712-_anno.html"><code class="ph codeph">UI.dataFieldDefault[ ].value</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_348129968-_anno.html"><code class="ph codeph">UI.dataPoint.criticality</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1706502036_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.acceptanceRangeHighValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_291174288_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.acceptanceRangeLowValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_600063752-_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.constantThresholds[ ].acceptanceRangeHighValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_76967194-_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.constantThresholds[ ].acceptanceRangeLowValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1993846012-_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.constantThresholds[ ].aggregationLevel[ ]</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_223598049_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.constantThresholds[ ].deviationRangeHighValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_672889410_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.constantThresholds[ ].deviationRangeLowValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_505474560-_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.constantThresholds[ ].toleranceRangeHighValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_953238141-_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.constantThresholds[ ].toleranceRangeLowValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_413093737-_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.deviationRangeHighValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1824666286_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.deviationRangeHighValueElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_835111482-_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.deviationRangeLowValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1327765704_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.deviationRangeLowValueElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1759944807-_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.improvementDirection</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(8)</code></td>
<td><p><code class="ph codeph">#MAXIMIZE</code></p>
<p><code class="ph codeph">#MINIMIZE</code></p>
<p><code class="ph codeph">#TARGET</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_200046454_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.toleranceRangeHighValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_759632402_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.toleranceRangeHighValueElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_554496519_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.toleranceRangeLowValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_830552989-_anno.html"><code class="ph codeph">UI.dataPoint.criticalityCalculation.toleranceRangeLowValueElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1499292211-_anno.html"><code class="ph codeph">UI.dataPoint.criticalityRepresentation</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#WITHOUT_ICON</code></p>
<p><code class="ph codeph">#WITH_ICON</code></p></td>
<td><code class="ph codeph">#WITHOUT_ICON</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_945760540-_anno.html"><code class="ph codeph">UI.dataPoint.criticalityValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><p><code class="ph codeph">#CRITICAL</code></p>
<p><code class="ph codeph">#NEGATIVE</code></p>
<p><code class="ph codeph">#POSITIVE</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1852632786_anno.html"><code class="ph codeph">UI.dataPoint.description</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_93463976_anno.html"><code class="ph codeph">UI.dataPoint.forecastValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1775339859_anno.html"><code class="ph codeph">UI.dataPoint.hidden</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1832891608-_anno.html"><code class="ph codeph">UI.dataPoint.longDescription</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(250)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1463846906-_anno.html"><code class="ph codeph">UI.dataPoint.maximumValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_952920300_anno.html"><code class="ph codeph">UI.dataPoint.minimumValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_17739803-_anno.html"><code class="ph codeph">UI.dataPoint.qualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_989930274_anno.html"><code class="ph codeph">UI.dataPoint.referencePeriod.description</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1032228177-_anno.html"><code class="ph codeph">UI.dataPoint.referencePeriod.end</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1256446419_anno.html"><code class="ph codeph">UI.dataPoint.referencePeriod.start</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1804694756-_anno.html"><code class="ph codeph">UI.dataPoint.responsible</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_94559242_anno.html"><code class="ph codeph">UI.dataPoint.responsibleName</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1325645678_anno.html"><code class="ph codeph">UI.dataPoint.targetValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_977257222_anno.html"><code class="ph codeph">UI.dataPoint.targetValueElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1446080992-_anno.html"><code class="ph codeph">UI.dataPoint.title</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1979958765_anno.html"><code class="ph codeph">UI.dataPoint.trend</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_922869099_anno.html"><code class="ph codeph">UI.dataPoint.trendCalculation.downDifference</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_110061085-_anno.html"><code class="ph codeph">UI.dataPoint.trendCalculation.downDifferenceElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_557446502-_anno.html"><code class="ph codeph">UI.dataPoint.trendCalculation.isRelativeDifference</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2121687021-_anno.html"><code class="ph codeph">UI.dataPoint.trendCalculation.referenceValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1521241200_anno.html"><code class="ph codeph">UI.dataPoint.trendCalculation.strongDownDifference</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_191422664_anno.html"><code class="ph codeph">UI.dataPoint.trendCalculation.strongDownDifferenceElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1922359880-_anno.html"><code class="ph codeph">UI.dataPoint.trendCalculation.strongUpDifference</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_738304099-_anno.html"><code class="ph codeph">UI.dataPoint.trendCalculation.strongUpDifferenceElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1838184515-_anno.html"><code class="ph codeph">UI.dataPoint.trendCalculation.upDifference</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1061051370-_anno.html"><code class="ph codeph">UI.dataPoint.trendCalculation.upDifferenceElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_311394813_anno.html"><code class="ph codeph">UI.dataPoint.valueFormat.numberOfFractionalDigits</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1863721227_anno.html"><code class="ph codeph">UI.dataPoint.valueFormat.scaleFactor</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1590835810-_anno.html"><code class="ph codeph">UI.dataPoint.visualization</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#BULLET_CHART</code></p>
<p><code class="ph codeph">#DONUT</code></p>
<p><code class="ph codeph">#NUMBER</code></p>
<p><code class="ph codeph">#PROGRESS</code></p>
<p><code class="ph codeph">#RATING</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1921613471-_anno.html"><code class="ph codeph">UI.dataPoint.withCriticalityLabels</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1930292456_anno.html"><code class="ph codeph">UI.defaultValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_723129678-_anno.html"><code class="ph codeph">UI.deleteHidden</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1143047081_anno.html"><code class="ph codeph">UI.doNotCheckScaleOfMeasuredQuantity</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1182146754-_anno.html"><code class="ph codeph">UI.facet[ ].exclude</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_992195295-_anno.html"><code class="ph codeph">UI.facet[ ].feature</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_950827159_anno.html"><code class="ph codeph">UI.facet[ ].hidden</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2039744517-_anno.html"><code class="ph codeph">UI.facet[ ].id</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1090436236-_anno.html"><code class="ph codeph">UI.facet[ ].importance</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(6)</code></td>
<td><p><code class="ph codeph">#HIGH</code></p>
<p><code class="ph codeph">#LOW</code></p>
<p><code class="ph codeph">#MEDIUM</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1579339872_anno.html"><code class="ph codeph">UI.facet[ ].isMap</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1187851329_anno.html"><code class="ph codeph">UI.facet[ ].isPartOfPreview</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1070960628_anno.html"><code class="ph codeph">UI.facet[ ].isSummary</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_799955090_anno.html"><code class="ph codeph">UI.facet[ ].label</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_124939291-_anno.html"><code class="ph codeph">UI.facet[ ].parentId</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1370539010-_anno.html"><code class="ph codeph">UI.facet[ ].position</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1670155180_anno.html"><code class="ph codeph">UI.facet[ ].purpose</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#FILTER</code></p>
<p><code class="ph codeph">#HEADER</code></p>
<p><code class="ph codeph">#OPERATION_PARAMETER</code></p>
<p><code class="ph codeph">#QUICK_CREATE</code></p>
<p><code class="ph codeph">#QUICK_VIEW</code></p>
<p><code class="ph codeph">#STANDARD</code></p></td>
<td><code class="ph codeph">#STANDARD</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1262791765_anno.html"><code class="ph codeph">UI.facet[ ].qualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1424624683-_anno.html"><code class="ph codeph">UI.facet[ ].targetElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2033016862-_anno.html"><code class="ph codeph">UI.facet[ ].targetQualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_824350749_anno.html"><code class="ph codeph">UI.facet[ ].type</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#ADDRESS_REFERENCE</code></p>
<p><code class="ph codeph">#BADGE_REFERENCE</code></p>
<p><code class="ph codeph">#CHART_REFERENCE</code></p>
<p><code class="ph codeph">#COLLECTION</code></p>
<p><code class="ph codeph">#CONTACT_REFERENCE</code></p>
<p><code class="ph codeph">#DATAPOINT_REFERENCE</code></p>
<p><code class="ph codeph">#FIELDGROUP_REFERENCE</code></p>
<p><code class="ph codeph">#HEADERINFO_REFERENCE</code></p>
<p><code class="ph codeph">#IDENTIFICATION_REFERENCE</code></p>
<p><code class="ph codeph">#LINEITEM_REFERENCE</code></p>
<p><code class="ph codeph">#NOTE_REFERENCE</code></p>
<p><code class="ph codeph">#PRESENTATIONVARIANT_REFERENCE</code></p>
<p><code class="ph codeph">#SELECTIONPRESENTATIONVARIANT_REFERENCE</code></p>
<p><code class="ph codeph">#STATUSINFO_REFERENCE</code></p>
<p><code class="ph codeph">#URL_REFERENCE</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1253348002-_anno.html"><code class="ph codeph">UI.facet[ ].url</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1721429130-_anno.html"><code class="ph codeph">UI.facet[ ].urlTarget</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#BLANK</code></p>
<p><code class="ph codeph">#PARENT</code></p>
<p><code class="ph codeph">#SELF</code></p>
<p><code class="ph codeph">#TOP</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1829497181_anno.html"><code class="ph codeph">UI.fieldGroup[ ].actionGroupId</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_779878154-_anno.html"><code class="ph codeph">UI.fieldGroup[ ].criticality</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_662747725-_anno.html"><code class="ph codeph">UI.fieldGroup[ ].criticalityRepresentation</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#ONLY_ICON</code></p>
<p><code class="ph codeph">#WITHOUT_ICON</code></p>
<p><code class="ph codeph">#WITH_ICON</code></p></td>
<td><code class="ph codeph">#WITHOUT_ICON</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_304305186_anno.html"><code class="ph codeph">UI.fieldGroup[ ].cssDefault.width</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1274070716-_anno.html"><code class="ph codeph">UI.fieldGroup[ ].dataAction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1608251073_anno.html"><code class="ph codeph">UI.fieldGroup[ ].determining</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1833888524_anno.html"><code class="ph codeph">UI.fieldGroup[ ].emphasized</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_514524285_anno.html"><code class="ph codeph">UI.fieldGroup[ ].exclude</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1947089820-_anno.html"><code class="ph codeph">UI.fieldGroup[ ].groupLabel</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2102483571_anno.html"><code class="ph codeph">UI.fieldGroup[ ].hidden</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2098531768-_anno.html"><code class="ph codeph">UI.fieldGroup[ ].iconUrl</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2054237562_anno.html"><code class="ph codeph">UI.fieldGroup[ ].importance</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(6)</code></td>
<td><p><code class="ph codeph">#HIGH</code></p>
<p><code class="ph codeph">#LOW</code></p>
<p><code class="ph codeph">#MEDIUM</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1117262279-_anno.html"><code class="ph codeph">UI.fieldGroup[ ].inline</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1713184207_anno.html"><code class="ph codeph">UI.fieldGroup[ ].invocationGrouping</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#CHANGE_SET</code></p>
<p><code class="ph codeph">#ISOLATED</code></p></td>
<td><code class="ph codeph">#ISOLATED</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_18384578-_anno.html"><code class="ph codeph">UI.fieldGroup[ ].isCopyAction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1065854645-_anno.html"><code class="ph codeph">UI.fieldGroup[ ].isPartOfPreview</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_231786943_anno.html"><code class="ph codeph">UI.fieldGroup[ ].label</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_654694452-_anno.html"><code class="ph codeph">UI.fieldGroup[ ].navigationAvailable</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1094519055_anno.html"><code class="ph codeph">UI.fieldGroup[ ].position</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2129584915-_anno.html"><code class="ph codeph">UI.fieldGroup[ ].qualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1576926503_anno.html"><code class="ph codeph">UI.fieldGroup[ ].requiresContext</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2044004261_anno.html"><code class="ph codeph">UI.fieldGroup[ ].rowSpanForDuplicateValues</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_214828561-_anno.html"><code class="ph codeph">UI.fieldGroup[ ].semanticObject</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_490946706_anno.html"><code class="ph codeph">UI.fieldGroup[ ].semanticObjectAction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_762944345-_anno.html"><code class="ph codeph">UI.fieldGroup[ ].semanticObjectBinding[ ].element</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1314000956_anno.html"><code class="ph codeph">UI.fieldGroup[ ].semanticObjectBinding[ ].localElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_964426032-_anno.html"><code class="ph codeph">UI.fieldGroup[ ].semanticObjectBinding[ ].localParameter</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ParameterRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_183560463_anno.html"><code class="ph codeph">UI.fieldGroup[ ].targetElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1302662315_anno.html"><code class="ph codeph">UI.fieldGroup[ ].type</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#AS_ADDRESS</code></p>
<p><code class="ph codeph">#AS_CHART</code></p>
<p><code class="ph codeph">#AS_CONNECTED_FIELDS</code></p>
<p><code class="ph codeph">#AS_CONTACT</code></p>
<p><code class="ph codeph">#AS_DATAPOINT</code></p>
<p><code class="ph codeph">#AS_FIELDGROUP</code></p>
<p><code class="ph codeph">#AS_PRESENTATION_VARIANT</code></p>
<p><code class="ph codeph">#AS_SELECTION_PRESENTATION_VARIANT</code></p>
<p><code class="ph codeph">#FOR_ACTION</code></p>
<p><code class="ph codeph">#FOR_ACTION_GROUP</code></p>
<p><code class="ph codeph">#FOR_INTENT_BASED_NAVIGATION</code></p>
<p><code class="ph codeph">#STANDARD</code></p>
<p><code class="ph codeph">#WITH_ACTION</code></p>
<p><code class="ph codeph">#WITH_ACTION_GROUP</code></p>
<p><code class="ph codeph">#WITH_INTENT_BASED_NAVIGATION</code></p>
<p><code class="ph codeph">#WITH_NAVIGATION_PATH</code></p>
<p><code class="ph codeph">#WITH_URL</code></p></td>
<td><code class="ph codeph">#STANDARD</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_298816368-_anno.html"><code class="ph codeph">UI.fieldGroup[ ].url</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1395696590_anno.html"><code class="ph codeph">UI.fieldGroup[ ].urlTarget</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#BLANK</code></p>
<p><code class="ph codeph">#PARENT</code></p>
<p><code class="ph codeph">#SELF</code></p>
<p><code class="ph codeph">#TOP</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_503365987_anno.html"><code class="ph codeph">UI.fieldGroup[ ].value</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1263465086-_anno.html"><code class="ph codeph">UI.fieldGroup[ ].valueQualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1384914881_anno.html"><code class="ph codeph">UI.headerInfo.description.criticality</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1830616392_anno.html"><code class="ph codeph">UI.headerInfo.description.criticalityRepresentation</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#WITHOUT_ICON</code></p>
<p><code class="ph codeph">#WITH_ICON</code></p></td>
<td><code class="ph codeph">#WITHOUT_ICON</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1082641577-_anno.html"><code class="ph codeph">UI.headerInfo.description.iconUrl</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2034373157-_anno.html"><code class="ph codeph">UI.headerInfo.description.label</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_402638790_anno.html"><code class="ph codeph">UI.headerInfo.description.targetElement</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1640398095-_anno.html"><code class="ph codeph">UI.headerInfo.description.type</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#AS_CONNECTED_FIELDS</code></p>
<p><code class="ph codeph">#STANDARD</code></p>
<p><code class="ph codeph">#WITH_INTENT_BASED_NAVIGATION</code></p>
<p><code class="ph codeph">#WITH_NAVIGATION_PATH</code></p>
<p><code class="ph codeph">#WITH_URL</code></p></td>
<td><code class="ph codeph">#STANDARD</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1538601481-_anno.html"><code class="ph codeph">UI.headerInfo.description.url</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1913217764_anno.html"><code class="ph codeph">UI.headerInfo.description.urlTarget</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#BLANK</code></p>
<p><code class="ph codeph">#PARENT</code></p>
<p><code class="ph codeph">#SELF</code></p>
<p><code class="ph codeph">#TOP</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1787960057-_anno.html"><code class="ph codeph">UI.headerInfo.description.value</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1444182200_anno.html"><code class="ph codeph">UI.headerInfo.description.valueQualifier</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_343625352_anno.html"><code class="ph codeph">UI.headerInfo.imageUrl</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_600116933_anno.html"><code class="ph codeph">UI.headerInfo.title.criticality</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1891168930-_anno.html"><code class="ph codeph">UI.headerInfo.title.criticalityRepresentation</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#WITHOUT_ICON</code></p>
<p><code class="ph codeph">#WITH_ICON</code></p></td>
<td><code class="ph codeph">#WITHOUT_ICON</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_189616342_anno.html"><code class="ph codeph">UI.headerInfo.title.iconUrl</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_897370684_anno.html"><code class="ph codeph">UI.headerInfo.title.label</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_421745529_anno.html"><code class="ph codeph">UI.headerInfo.title.targetElement</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_962874121_anno.html"><code class="ph codeph">UI.headerInfo.title.type</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#AS_CONNECTED_FIELDS</code></p>
<p><code class="ph codeph">#STANDARD</code></p>
<p><code class="ph codeph">#WITH_INTENT_BASED_NAVIGATION</code></p>
<p><code class="ph codeph">#WITH_NAVIGATION_PATH</code></p>
<p><code class="ph codeph">#WITH_URL</code></p></td>
<td><code class="ph codeph">#STANDARD</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1633332205-_anno.html"><code class="ph codeph">UI.headerInfo.title.url</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2077601991-_anno.html"><code class="ph codeph">UI.headerInfo.title.urlTarget</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#BLANK</code></p>
<p><code class="ph codeph">#PARENT</code></p>
<p><code class="ph codeph">#SELF</code></p>
<p><code class="ph codeph">#TOP</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_648856288_anno.html"><code class="ph codeph">UI.headerInfo.title.value</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_230951473_anno.html"><code class="ph codeph">UI.headerInfo.title.valueQualifier</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_939199532_anno.html"><code class="ph codeph">UI.headerInfo.typeImageUrl</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_852067256_anno.html"><code class="ph codeph">UI.headerInfo.typeName</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_24288459-_anno.html"><code class="ph codeph">UI.headerInfo.typeNamePlural</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1308869518_anno.html"><code class="ph codeph">UI.hidden</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_172480914-_anno.html"><code class="ph codeph">UI.identification[ ].actionGroupId</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1442091304_anno.html"><code class="ph codeph">UI.identification[ ].criticality</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1659524627-_anno.html"><code class="ph codeph">UI.identification[ ].criticalityRepresentation</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#ONLY_ICON</code></p>
<p><code class="ph codeph">#WITHOUT_ICON</code></p>
<p><code class="ph codeph">#WITH_ICON</code></p></td>
<td><code class="ph codeph">#WITHOUT_ICON</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_704915140_anno.html"><code class="ph codeph">UI.identification[ ].cssDefault.width</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2061449559_anno.html"><code class="ph codeph">UI.identification[ ].dataAction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_609523937-_anno.html"><code class="ph codeph">UI.identification[ ].determining</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1549866209-_anno.html"><code class="ph codeph">UI.identification[ ].emphasized</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1360521922-_anno.html"><code class="ph codeph">UI.identification[ ].exclude</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_287818999-_anno.html"><code class="ph codeph">UI.identification[ ].hidden</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_849994507_anno.html"><code class="ph codeph">UI.identification[ ].iconUrl</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1264505495-_anno.html"><code class="ph codeph">UI.identification[ ].importance</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(6)</code></td>
<td><p><code class="ph codeph">#HIGH</code></p>
<p><code class="ph codeph">#LOW</code></p>
<p><code class="ph codeph">#MEDIUM</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_787386179_anno.html"><code class="ph codeph">UI.identification[ ].inline</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_802004590-_anno.html"><code class="ph codeph">UI.identification[ ].invocationGrouping</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#CHANGE_SET</code></p>
<p><code class="ph codeph">#ISOLATED</code></p></td>
<td><code class="ph codeph">#ISOLATED</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1626802564-_anno.html"><code class="ph codeph">UI.identification[ ].isCopyAction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1070103529_anno.html"><code class="ph codeph">UI.identification[ ].isPartOfPreview</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1924256206-_anno.html"><code class="ph codeph">UI.identification[ ].label</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_845797895-_anno.html"><code class="ph codeph">UI.identification[ ].navigationAvailable</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1369941452-_anno.html"><code class="ph codeph">UI.identification[ ].position</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_821399706_anno.html"><code class="ph codeph">UI.identification[ ].qualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1571954811-_anno.html"><code class="ph codeph">UI.identification[ ].requiresContext</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1019210747_anno.html"><code class="ph codeph">UI.identification[ ].rowSpanForDuplicateValues</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1283009334_anno.html"><code class="ph codeph">UI.identification[ ].semanticObject</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1273358515_anno.html"><code class="ph codeph">UI.identification[ ].semanticObjectAction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1073216576-_anno.html"><code class="ph codeph">UI.identification[ ].semanticObjectBinding[ ].element</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1357787778_anno.html"><code class="ph codeph">UI.identification[ ].semanticObjectBinding[ ].localElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1772280510_anno.html"><code class="ph codeph">UI.identification[ ].semanticObjectBinding[ ].localParameter</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ParameterRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1841093060-_anno.html"><code class="ph codeph">UI.identification[ ].targetElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1239070146-_anno.html"><code class="ph codeph">UI.identification[ ].type</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#AS_ADDRESS</code></p>
<p><code class="ph codeph">#AS_CHART</code></p>
<p><code class="ph codeph">#AS_CONNECTED_FIELDS</code></p>
<p><code class="ph codeph">#AS_CONTACT</code></p>
<p><code class="ph codeph">#AS_DATAPOINT</code></p>
<p><code class="ph codeph">#AS_FIELDGROUP</code></p>
<p><code class="ph codeph">#AS_PRESENTATION_VARIANT</code></p>
<p><code class="ph codeph">#AS_SELECTION_PRESENTATION_VARIANT</code></p>
<p><code class="ph codeph">#FOR_ACTION</code></p>
<p><code class="ph codeph">#FOR_ACTION_GROUP</code></p>
<p><code class="ph codeph">#FOR_INTENT_BASED_NAVIGATION</code></p>
<p><code class="ph codeph">#STANDARD</code></p>
<p><code class="ph codeph">#WITH_ACTION</code></p>
<p><code class="ph codeph">#WITH_ACTION_GROUP</code></p>
<p><code class="ph codeph">#WITH_INTENT_BASED_NAVIGATION</code></p>
<p><code class="ph codeph">#WITH_NAVIGATION_PATH</code></p>
<p><code class="ph codeph">#WITH_URL</code></p></td>
<td><code class="ph codeph">#STANDARD</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1170563889-_anno.html"><code class="ph codeph">UI.identification[ ].url</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_489410631-_anno.html"><code class="ph codeph">UI.identification[ ].urlTarget</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#BLANK</code></p>
<p><code class="ph codeph">#PARENT</code></p>
<p><code class="ph codeph">#SELF</code></p>
<p><code class="ph codeph">#TOP</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1633802514-_anno.html"><code class="ph codeph">UI.identification[ ].value</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_200925019_anno.html"><code class="ph codeph">UI.identification[ ].valueQualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_820822204-_anno.html"><code class="ph codeph">UI.inputMask.mask</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_186289328-_anno.html"><code class="ph codeph">UI.inputMask.placeholderSymbol</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(1)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_757191960_anno.html"><code class="ph codeph">UI.inputMask.rules[ ].maskSymbol</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(1)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_235272819-_anno.html"><code class="ph codeph">UI.inputMask.rules[ ].regularExpression</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#PARAMETER</code></p></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1421215833_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.criticality</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_589836983_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.criticalityCalculation.acceptanceRangeHighValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_403591873-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.criticalityCalculation.acceptanceRangeLowValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2063535132-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.criticalityCalculation.constantThresholds[ ].acceptanceRangeHighValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1936169370_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.criticalityCalculation.constantThresholds[ ].acceptanceRangeLowValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1391479045-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.criticalityCalculation.constantThresholds[ ].aggregationLevel[ ]</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2057445731-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.criticalityCalculation.constantThresholds[ ].deviationRangeHighValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_776659098_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.criticalityCalculation.constantThresholds[ ].deviationRangeLowValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1775311228_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.criticalityCalculation.constantThresholds[ ].toleranceRangeHighValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1048631461-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.criticalityCalculation.constantThresholds[ ].toleranceRangeLowValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_298576440_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.criticalityCalculation.deviationRangeHighValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_599408365-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.criticalityCalculation.deviationRangeLowValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_349205975-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.criticalityCalculation.improvementDirection</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(8)</code></td>
<td><p><code class="ph codeph">#MAXIMIZE</code></p>
<p><code class="ph codeph">#MINIMIZE</code></p>
<p><code class="ph codeph">#TARGET</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_45666855-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.criticalityCalculation.toleranceRangeHighValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_862979794_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.criticalityCalculation.toleranceRangeLowValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1683719252_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.criticalityRepresentation</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#WITHOUT_ICON</code></p>
<p><code class="ph codeph">#WITH_ICON</code></p></td>
<td><code class="ph codeph">#WITHOUT_ICON</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_856025239_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.criticalityValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><p><code class="ph codeph">#CRITICAL</code></p>
<p><code class="ph codeph">#NEGATIVE</code></p>
<p><code class="ph codeph">#POSITIVE</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_773516325-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.description</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_391950281_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.forecastValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_653447383_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.hidden</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_481597122-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.longDescription</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(250)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_774092449-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.maximumValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1102010805_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.minimumValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1476536-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.referencePeriod.description</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1941432392_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.referencePeriod.end</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1258714988_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.referencePeriod.start</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_736589333_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.responsible</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1948909084_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.responsibleName</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_259374489-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.targetValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1432705155_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.title</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1968696498-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.trend</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_165508112_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.trendCalculation.downDifference</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2140945212-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.trendCalculation.isRelativeDifference</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1084946072-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.trendCalculation.referenceValue</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_67732014_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.trendCalculation.strongDownDifference</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_185650034_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.trendCalculation.strongUpDifference</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_238794748-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.trendCalculation.upDifference</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1773719941_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.valueFormat.numberOfFractionalDigits</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1025842294_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.valueFormat.scaleFactor</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1276948481-_anno.html"><code class="ph codeph">UI.kpi[ ].dataPoint.visualization</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#BULLET_CHART</code></p>
<p><code class="ph codeph">#DONUT</code></p>
<p><code class="ph codeph">#NUMBER</code></p>
<p><code class="ph codeph">#PROGRESS</code></p>
<p><code class="ph codeph">#RATING</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_44552114-_anno.html"><code class="ph codeph">UI.kpi[ ].detail.alternativePresentationVariantQualifiers[ ]</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1543997474_anno.html"><code class="ph codeph">UI.kpi[ ].detail.defaultPresentationVariantQualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_566510180-_anno.html"><code class="ph codeph">UI.kpi[ ].detail.semanticObject</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1655633059_anno.html"><code class="ph codeph">UI.kpi[ ].detail.semanticObjectAction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1717580298_anno.html"><code class="ph codeph">UI.kpi[ ].id</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1774674454_anno.html"><code class="ph codeph">UI.kpi[ ].qualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_684578969_anno.html"><code class="ph codeph">UI.kpi[ ].selectionVariantQualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_78237851_anno.html"><code class="ph codeph">UI.kpi[ ].shortDescription</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1808225901_anno.html"><code class="ph codeph">UI.lineItem[ ].actionGroupId</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1309545091-_anno.html"><code class="ph codeph">UI.lineItem[ ].criticality</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_297561687_anno.html"><code class="ph codeph">UI.lineItem[ ].criticalityRepresentation</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#ONLY_ICON</code></p>
<p><code class="ph codeph">#WITHOUT_ICON</code></p>
<p><code class="ph codeph">#WITH_ICON</code></p></td>
<td><code class="ph codeph">#WITHOUT_ICON</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_943223464-_anno.html"><code class="ph codeph">UI.lineItem[ ].cssDefault.width</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1902929883_anno.html"><code class="ph codeph">UI.lineItem[ ].dataAction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1068374858_anno.html"><code class="ph codeph">UI.lineItem[ ].determining</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1473399405-_anno.html"><code class="ph codeph">UI.lineItem[ ].emphasized</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_62243717_anno.html"><code class="ph codeph">UI.lineItem[ ].exclude</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_729364893-_anno.html"><code class="ph codeph">UI.lineItem[ ].hidden</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1611385424-_anno.html"><code class="ph codeph">UI.lineItem[ ].iconUrl</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1089309723-_anno.html"><code class="ph codeph">UI.lineItem[ ].importance</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(6)</code></td>
<td><p><code class="ph codeph">#HIGH</code></p>
<p><code class="ph codeph">#LOW</code></p>
<p><code class="ph codeph">#MEDIUM</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_347107881_anno.html"><code class="ph codeph">UI.lineItem[ ].inline</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1287795495_anno.html"><code class="ph codeph">UI.lineItem[ ].invocationGrouping</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#CHANGE_SET</code></p>
<p><code class="ph codeph">#ISOLATED</code></p></td>
<td><code class="ph codeph">#ISOLATED</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2064820613-_anno.html"><code class="ph codeph">UI.lineItem[ ].isCopyAction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1155581801_anno.html"><code class="ph codeph">UI.lineItem[ ].isPartOfPreview</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1726122579_anno.html"><code class="ph codeph">UI.lineItem[ ].label</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1979814568_anno.html"><code class="ph codeph">UI.lineItem[ ].navigationAvailable</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_230265370-_anno.html"><code class="ph codeph">UI.lineItem[ ].position</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1484012885_anno.html"><code class="ph codeph">UI.lineItem[ ].qualifier</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_647666939-_anno.html"><code class="ph codeph">UI.lineItem[ ].requiresContext</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1340724159-_anno.html"><code class="ph codeph">UI.lineItem[ ].rowSpanForDuplicateValues</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_705821188-_anno.html"><code class="ph codeph">UI.lineItem[ ].semanticObject</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1462902374_anno.html"><code class="ph codeph">UI.lineItem[ ].semanticObjectAction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1108548272-_anno.html"><code class="ph codeph">UI.lineItem[ ].semanticObjectBinding[ ].element</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1183216817_anno.html"><code class="ph codeph">UI.lineItem[ ].semanticObjectBinding[ ].localElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_41307459_anno.html"><code class="ph codeph">UI.lineItem[ ].semanticObjectBinding[ ].localParameter</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ParameterRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_205280831_anno.html"><code class="ph codeph">UI.lineItem[ ].targetElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_347542779_anno.html"><code class="ph codeph">UI.lineItem[ ].type</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#AS_ADDRESS</code></p>
<p><code class="ph codeph">#AS_CHART</code></p>
<p><code class="ph codeph">#AS_CONNECTED_FIELDS</code></p>
<p><code class="ph codeph">#AS_CONTACT</code></p>
<p><code class="ph codeph">#AS_DATAPOINT</code></p>
<p><code class="ph codeph">#AS_FIELDGROUP</code></p>
<p><code class="ph codeph">#AS_PRESENTATION_VARIANT</code></p>
<p><code class="ph codeph">#AS_SELECTION_PRESENTATION_VARIANT</code></p>
<p><code class="ph codeph">#FOR_ACTION</code></p>
<p><code class="ph codeph">#FOR_ACTION_GROUP</code></p>
<p><code class="ph codeph">#FOR_INTENT_BASED_NAVIGATION</code></p>
<p><code class="ph codeph">#STANDARD</code></p>
<p><code class="ph codeph">#WITH_ACTION</code></p>
<p><code class="ph codeph">#WITH_ACTION_GROUP</code></p>
<p><code class="ph codeph">#WITH_INTENT_BASED_NAVIGATION</code></p>
<p><code class="ph codeph">#WITH_NAVIGATION_PATH</code></p>
<p><code class="ph codeph">#WITH_URL</code></p></td>
<td><code class="ph codeph">#STANDARD</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1326787564_anno.html"><code class="ph codeph">UI.lineItem[ ].url</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1974107530-_anno.html"><code class="ph codeph">UI.lineItem[ ].urlTarget</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#BLANK</code></p>
<p><code class="ph codeph">#PARENT</code></p>
<p><code class="ph codeph">#SELF</code></p>
<p><code class="ph codeph">#TOP</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1966244495_anno.html"><code class="ph codeph">UI.lineItem[ ].value</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1838222959-_anno.html"><code class="ph codeph">UI.lineItem[ ].valueQualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_150591737_anno.html"><code class="ph codeph">UI.masked</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_649579826_anno.html"><code class="ph codeph">UI.mediaResource.largeObject</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1508277723_anno.html"><code class="ph codeph">UI.mediaResource.url</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1476269693-_anno.html"><code class="ph codeph">UI.mediaResource.urlTarget</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#BLANK</code></p>
<p><code class="ph codeph">#PARENT</code></p>
<p><code class="ph codeph">#SELF</code></p>
<p><code class="ph codeph">#TOP</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_40183251-_anno.html"><code class="ph codeph">UI.multiLineText</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1345525584_anno.html"><code class="ph codeph">UI.note.content.mimeType</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_45167487_anno.html"><code class="ph codeph">UI.note.content.value</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_433792610_anno.html"><code class="ph codeph">UI.note.title.hidden</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_2879366-_anno.html"><code class="ph codeph">UI.note.title.value</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_1202776521-_anno.html"><code class="ph codeph">UI.note.type.languageDependent</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_1367682277_anno.html"><code class="ph codeph">UI.note.type.maxLength</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_722298920_anno.html"><code class="ph codeph">UI.note.type.multipleNotes</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="even">
<td><a href="abencds_1944862712_anno.html"><code class="ph codeph">UI.note.type.name</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></td>
</tr>
<tr class="odd">
<td><a href="abencds_1152076199_anno.html"><code class="ph codeph">UI.presentationVariant[ ].groupBy[ ]</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_397833246_anno.html"><code class="ph codeph">UI.presentationVariant[ ].id</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1844549153_anno.html"><code class="ph codeph">UI.presentationVariant[ ].includeGrandTotal</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1986479756-_anno.html"><code class="ph codeph">UI.presentationVariant[ ].initialExpansionLevel</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1925365585_anno.html"><code class="ph codeph">UI.presentationVariant[ ].maxItems</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_161382726-_anno.html"><code class="ph codeph">UI.presentationVariant[ ].qualifier</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_937506020-_anno.html"><code class="ph codeph">UI.presentationVariant[ ].recursiveHierarchyQualifier</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1885991486_anno.html"><code class="ph codeph">UI.presentationVariant[ ].requestAtLeast[ ]</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_155710428_anno.html"><code class="ph codeph">UI.presentationVariant[ ].selectionFieldsQualifier</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1682631613-_anno.html"><code class="ph codeph">UI.presentationVariant[ ].sortOrder[ ].by</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_613943470-_anno.html"><code class="ph codeph">UI.presentationVariant[ ].sortOrder[ ].direction</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(4)</code></td>
<td><p><code class="ph codeph">#ASC</code></p>
<p><code class="ph codeph">#DESC</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_774951907-_anno.html"><code class="ph codeph">UI.presentationVariant[ ].text</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1530683873-_anno.html"><code class="ph codeph">UI.presentationVariant[ ].total[ ]</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1889723134_anno.html"><code class="ph codeph">UI.presentationVariant[ ].totalBy[ ]</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_947550714_anno.html"><code class="ph codeph">UI.presentationVariant[ ].visualizations[ ].element</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1717346594-_anno.html"><code class="ph codeph">UI.presentationVariant[ ].visualizations[ ].qualifier</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_241067122_anno.html"><code class="ph codeph">UI.presentationVariant[ ].visualizations[ ].type</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#AS_CHART</code></p>
<p><code class="ph codeph">#AS_DATAPOINT</code></p>
<p><code class="ph codeph">#AS_LINEITEM</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2022813284-_anno.html"><code class="ph codeph">UI.selectionField[ ].element</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1532172068-_anno.html"><code class="ph codeph">UI.selectionField[ ].exclude</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_531194467-_anno.html"><code class="ph codeph">UI.selectionField[ ].position</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1615756015-_anno.html"><code class="ph codeph">UI.selectionField[ ].qualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_8202993-_anno.html"><code class="ph codeph">UI.selectionPresentationVariant[ ].id</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1525932436_anno.html"><code class="ph codeph">UI.selectionPresentationVariant[ ].presentationVariantQualifier</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1562223590-_anno.html"><code class="ph codeph">UI.selectionPresentationVariant[ ].qualifier</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_500346719_anno.html"><code class="ph codeph">UI.selectionPresentationVariant[ ].selectionVariantQualifier</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_600273991_anno.html"><code class="ph codeph">UI.selectionPresentationVariant[ ].text</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1222964633-_anno.html"><code class="ph codeph">UI.selectionVariant[ ].filter</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_60252014_anno.html"><code class="ph codeph">UI.selectionVariant[ ].id</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_526689087_anno.html"><code class="ph codeph">UI.selectionVariant[ ].parameters[ ].name</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ParameterRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1110677473_anno.html"><code class="ph codeph">UI.selectionVariant[ ].parameters[ ].value</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1421384984_anno.html"><code class="ph codeph">UI.selectionVariant[ ].qualifier</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1380759690_anno.html"><code class="ph codeph">UI.selectionVariant[ ].text</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_819810654-_anno.html"><code class="ph codeph">UI.selfNavigation.semanticObject</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1265348222_anno.html"><code class="ph codeph">UI.selfNavigation.semanticObjectAction</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1101284070-_anno.html"><code class="ph codeph">UI.selfNavigation.semanticObjectBinding[ ].element</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1321162686-_anno.html"><code class="ph codeph">UI.selfNavigation.semanticObjectBinding[ ].localElement</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_577883765-_anno.html"><code class="ph codeph">UI.statusInfo[ ].actionGroupId</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1806281407-_anno.html"><code class="ph codeph">UI.statusInfo[ ].criticality</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1775575399-_anno.html"><code class="ph codeph">UI.statusInfo[ ].criticalityRepresentation</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#ONLY_ICON</code></p>
<p><code class="ph codeph">#WITHOUT_ICON</code></p>
<p><code class="ph codeph">#WITH_ICON</code></p></td>
<td><code class="ph codeph">#WITHOUT_ICON</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1326720424_anno.html"><code class="ph codeph">UI.statusInfo[ ].cssDefault.width</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(20)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1190724759-_anno.html"><code class="ph codeph">UI.statusInfo[ ].dataAction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_436839286_anno.html"><code class="ph codeph">UI.statusInfo[ ].determining</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1615276321_anno.html"><code class="ph codeph">UI.statusInfo[ ].emphasized</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1452295040-_anno.html"><code class="ph codeph">UI.statusInfo[ ].exclude</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_79010829_anno.html"><code class="ph codeph">UI.statusInfo[ ].hidden</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_892226229_anno.html"><code class="ph codeph">UI.statusInfo[ ].iconUrl</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(1024)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2004414295_anno.html"><code class="ph codeph">UI.statusInfo[ ].importance</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(6)</code></td>
<td><p><code class="ph codeph">#HIGH</code></p>
<p><code class="ph codeph">#LOW</code></p>
<p><code class="ph codeph">#MEDIUM</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_998037433-_anno.html"><code class="ph codeph">UI.statusInfo[ ].inline</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2139917933-_anno.html"><code class="ph codeph">UI.statusInfo[ ].invocationGrouping</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(12)</code></td>
<td><p><code class="ph codeph">#CHANGE_SET</code></p>
<p><code class="ph codeph">#ISOLATED</code></p></td>
<td><code class="ph codeph">#ISOLATED</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1415082684-_anno.html"><code class="ph codeph">UI.statusInfo[ ].isCopyAction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1626156623-_anno.html"><code class="ph codeph">UI.statusInfo[ ].isPartOfPreview</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_900600758_anno.html"><code class="ph codeph">UI.statusInfo[ ].label</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(60)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1161735041-_anno.html"><code class="ph codeph">UI.statusInfo[ ].navigationAvailable</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_2105130218-_anno.html"><code class="ph codeph">UI.statusInfo[ ].position</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">DecimalFloat</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_440856729-_anno.html"><code class="ph codeph">UI.statusInfo[ ].qualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_43480541_anno.html"><code class="ph codeph">UI.statusInfo[ ].requiresContext</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_931175567_anno.html"><code class="ph codeph">UI.statusInfo[ ].rowSpanForDuplicateValues</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1674507306-_anno.html"><code class="ph codeph">UI.statusInfo[ ].semanticObject</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1330223575_anno.html"><code class="ph codeph">UI.statusInfo[ ].semanticObjectAction</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1159218838-_anno.html"><code class="ph codeph">UI.statusInfo[ ].semanticObjectBinding[ ].element</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1876434346_anno.html"><code class="ph codeph">UI.statusInfo[ ].semanticObjectBinding[ ].localElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_1624344965-_anno.html"><code class="ph codeph">UI.statusInfo[ ].semanticObjectBinding[ ].localParameter</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ParameterRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1166724647-_anno.html"><code class="ph codeph">UI.statusInfo[ ].targetElement</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_339885815-_anno.html"><code class="ph codeph">UI.statusInfo[ ].type</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#AS_ADDRESS</code></p>
<p><code class="ph codeph">#AS_CHART</code></p>
<p><code class="ph codeph">#AS_CONNECTED_FIELDS</code></p>
<p><code class="ph codeph">#AS_CONTACT</code></p>
<p><code class="ph codeph">#AS_DATAPOINT</code></p>
<p><code class="ph codeph">#AS_FIELDGROUP</code></p>
<p><code class="ph codeph">#AS_PRESENTATION_VARIANT</code></p>
<p><code class="ph codeph">#AS_SELECTION_PRESENTATION_VARIANT</code></p>
<p><code class="ph codeph">#FOR_ACTION</code></p>
<p><code class="ph codeph">#FOR_ACTION_GROUP</code></p>
<p><code class="ph codeph">#FOR_INTENT_BASED_NAVIGATION</code></p>
<p><code class="ph codeph">#STANDARD</code></p>
<p><code class="ph codeph">#WITH_ACTION</code></p>
<p><code class="ph codeph">#WITH_ACTION_GROUP</code></p>
<p><code class="ph codeph">#WITH_INTENT_BASED_NAVIGATION</code></p>
<p><code class="ph codeph">#WITH_NAVIGATION_PATH</code></p>
<p><code class="ph codeph">#WITH_URL</code></p></td>
<td><code class="ph codeph">#STANDARD</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1252698421_anno.html"><code class="ph codeph">UI.statusInfo[ ].url</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_932753476_anno.html"><code class="ph codeph">UI.statusInfo[ ].urlTarget</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(40)</code></td>
<td><p><code class="ph codeph">#BLANK</code></p>
<p><code class="ph codeph">#PARENT</code></p>
<p><code class="ph codeph">#SELF</code></p>
<p><code class="ph codeph">#TOP</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_645798762_anno.html"><code class="ph codeph">UI.statusInfo[ ].value</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">ElementRef</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_609091653-_anno.html"><code class="ph codeph">UI.statusInfo[ ].valueQualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_857384890-_anno.html"><code class="ph codeph">UI.textArrangement</code></a></td>
<td><p><code class="ph codeph">#ELEMENT</code></p>
<p><code class="ph codeph">#ENTITY</code></p></td>
<td><code class="ph codeph">String(13)</code></td>
<td><p><code class="ph codeph">#TEXT_FIRST</code></p>
<p><code class="ph codeph">#TEXT_LAST</code></p>
<p><code class="ph codeph">#TEXT_ONLY</code></p>
<p><code class="ph codeph">#TEXT_SEPARATE</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_759025072-_anno.html"><code class="ph codeph">UI.updateHidden</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1060479977-_anno.html"><code class="ph codeph">UI.valueCriticality[ ].criticality</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">Integer</code></td>
<td><p><code class="ph codeph">#CRITICAL</code></p>
<p><code class="ph codeph">#NEGATIVE</code></p>
<p><code class="ph codeph">#POSITIVE</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="even">
<td><a href="abencds_157193550_anno.html"><code class="ph codeph">UI.valueCriticality[ ].qualifier</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_1218774824_anno.html"><code class="ph codeph">UI.valueCriticality[ ].value</code></a></td>
<td><code class="ph codeph">#ELEMENT</code></td>
<td><code class="ph codeph">String(120)</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">X</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>

## VDM-Annotations

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
<td><a href="abencds_527004726-_anno.html"><code class="ph codeph">VDM.private</code></a></td>
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
<td><a href="abencds_1891967415-_anno.html"><code class="ph codeph">VDM.viewExtension</code></a></td>
<td><code class="ph codeph">#EXTEND_VIEW</code></td>
<td><code class="ph codeph">Boolean</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">true</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
<tr class="odd">
<td><a href="abencds_2063101229-_anno.html"><code class="ph codeph">VDM.viewType</code></a></td>
<td><code class="ph codeph">#ENTITY</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#BASIC</code></p>
<p><code class="ph codeph">#COMPOSITE</code></p>
<p><code class="ph codeph">#CONSUMPTION</code></p>
<p><code class="ph codeph">#DERIVATION_FUNCTION</code></p>
<p><code class="ph codeph">#EXTENSION</code></p>
<p><code class="ph codeph">#TRANSACTIONAL</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>

## Workflow-Annotations

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
<td><a href="abencds_1985209549_anno.html"><code class="ph codeph">Workflow.enabledFor[ ]</code></a></td>
<td><code class="ph codeph">#VIEW</code></td>
<td><code class="ph codeph">String(30)</code></td>
<td><p><code class="ph codeph">#CUSTOM_TASK_ATTRIBUTES</code></p>
<p><code class="ph codeph">#RESPONSIBILITY_MANAGEMENT</code></p></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><code class="ph codeph">-</code></td>
<td><p><code class="ph codeph">RELEASED_FOR_KEY_USER_APPS</code></p>
<p><code class="ph codeph">RELEASED_FOR_SAP_CLOUD_PLATFORM</code></p></td>
</tr>
</tbody>
</table>
