---
title: "ABAP CDS - Scopes for Annotations"
source_file: abencds_annotations_scopes.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - Specifying Annotations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Scopes for Annotations

The [annotation syntax](abencds_annotations_syntax.md) for [CDS annotations](abencds_annotations.md) can be specified in ABAP CDS source code in scopes that are defined with the `@Scope` annotation in the corresponding annotation definition.

The following table shows the enumeration symbols that can be used as annotation values for `@Scope` and the corresponding source code positions.

<table>
<thead>
<tr class="header">
<th><strong>Scope</strong></th>
<th><strong>Source Code Position</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">#ACCESSPOLICY</code></td>
<td><a href="abencds_f1_define_accesspolicy.html">Access Policy</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">#ANNOTATE</code></td>
<td><a href="abencds_f1_metadata_ext_annos.html">Meta Data Extension</a></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">#ANNOTATION</code></td>
<td>Annotation Definition</td>
</tr>
<tr class="even">
<td><code class="ph codeph">#ASPECT</code></td>
<td><a href="abencds_ddl_aspect_anno.html">Aspect</a></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">#CUSTOM_ENTITY</code></td>
<td><a href="abencds_f1_entity_annotations.html">Custom Entity</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">#ELEMENT</code></td>
<td><a href="abencds_f1_element_annotation.html">Element</a></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">#ENTITY</code></td>
<td><a href="abencds_f1_entity_annotations.html">Entity</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">#ENTITY_ASPECT</code></td>
<td><a href="abencds_f1_dcl_as_annotations.html">User-defined Aspect</a></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">#ENUM_VALUE</code></td>
<td><a href="abencds_define_enum_type.html">Enumerated Constant</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">#EXTEND_VIEW</code></td>
<td><a href="abencds_f1_extend_view_annotations.html">View Extension</a></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">#EXTERNAL_ENTITY</code></td>
<td><a href="abencds_ee_annotations.html">External Entity</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">#HIERARCHY</code></td>
<td><a href="abencds_f1_hierarchy_annotations.html">Hierarchy</a></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">#OPERATION</code></td>
<td><code class="ph codeph">Not yet implemented</code></td>
</tr>
<tr class="even">
<td><code class="ph codeph">#PARAMETER</code></td>
<td><a href="abencds_f1_parameter_annotations.html">Parameter</a></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">#PFCG_MAPPING</code></td>
<td><a href="abencds_f1_define_pfcg_mapping.html">PFCG Mapping</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">#ROLE</code></td>
<td><a href="abencds_f1_dcl_role_annotations.html">Role</a></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">#SERVICE</code></td>
<td><a href="abencds_define_service_annos.html">Service Definition</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">#SIMPLE_TYPE</code></td>
<td><p><a href="abencds_simple_type_anno.html">Simple Type</a></p>
<p><a href="abencds_enum_type_anno.html">Enumerated Type</a></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">#TABLE_ENTITY</code></td>
<td><a href="abencds_define_table_entity.html">Table Entity</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">#TABLE_FUNCTION</code></td>
<td><a href="abencds_f1_function_annotations.html">Table Function</a></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">#VIEW</code></td>
<td><p><a href="abencds_define_view_v1.html">DDIC based View</a></p>
<p><a href="abencds_view_entity_anno.html">View Entity</a></p>
<p><a href="abencds_proj_view_annotations.html">Projection View</a></p></td>
</tr>
</tbody>
</table>

## Hint

The annotations specified in the source code of a CDS entity can be annotated or overridden using the annotations of [CDS metadata extensions](../../abap-glossary/abencds_metadata_extension_glosry.md).
