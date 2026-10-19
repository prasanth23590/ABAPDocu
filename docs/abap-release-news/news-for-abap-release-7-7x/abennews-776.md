---
title: "News for ABAP Release 7.76"
source_file: abennews-776.html
section: "ABAP Release News > News for ABAP Release 7.7x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.76

The kernel release for ABAP release 7.76 is 7.76.

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
<td><strong>Annotation for Database Hints</strong></td>
<td>The <a href="abenfrmwrk_annotation_glosry.html">framework-specific annotation</a> <a href="abencds_annotations_frmwrk_tables.html"><code class="ph codeph">@Consumption.dbHints</code></a> replaces the <a href="abenabap_annotation_glosry.html">ABAP annotation</a> <a href="abencds_annotations_abap_tables.html"><code class="ph codeph">@AbapCatalog.dbHints</code></a> and makes it obsolete. The ABAP annotation is evaluated by frameworks such as SADL and not by the ABAP runtime framework.</td>
</tr>
<tr class="even">
<td><strong>Annotations for Releasing Elements</strong></td>
<td><p>The new element annotations</p>
<ul>
<li><a href="abencds_f1_element_annotation.html"><code class="ph codeph">@API.element.releaseState</code></a></li>
<li><p><a href="abencds_f1_element_annotation.html"><code class="ph codeph">@API.element.successor</code></a></p>
<p>can be used to override releases of the individual elements and successors can be specified for forbidden elements.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>CDS Projection Views</strong></td>
<td>A new type of CDS entity is available: the CDS projection view. A <a href="abencds_define_view_as_projection.html">CDS projection view</a> is a direct projection of the underlying CDS view and exposes only a subset of elements of the projected entity. A CDS projection view is defined using <code class="ph codeph">DEFINE VIEW ENTITY AS PROJECTION ON</code> in a CDS data definition.</td>
</tr>
</tbody>
</table>
