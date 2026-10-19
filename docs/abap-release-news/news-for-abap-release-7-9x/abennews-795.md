---
title: "News for ABAP Release 7.95"
source_file: abennews-795.html
section: "ABAP Release News > News for ABAP Release 7.9x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.95

The kernel release for ABAP release 7.95 is 7.95.

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
<td><strong>Removal of Extensibility Annotations</strong></td>
<td><p>The following <a href="abenddicddl_define_ext_annos.html">extensibility annotations</a> are no longer available for <a href="abendictionary_object_glosry.html">dictionary objects</a> and they are no longer required for <a href="abenc0_contract_glosry.html">C0 release</a> of a DDIC object:</p>
<ul>
<li><a href="abenddicddl_define_ext_annos.html"><code class="ph codeph">@AbapCatalog.enhancement.quotaShareCustomer</code></a></li>
<li><a href="abenddicddl_define_ext_annos.html"><code class="ph codeph">@AbapCatalog.enhancement.quotaSharePartner</code></a></li>
</ul></td>
</tr>
</tbody>
</table>

## ABAP SQL

| Modification               | Description                                                                                                                                           |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Caching of Hierarchies** | The new addition `CACHE` for [`SELECT, FROM HIERARCHY`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_generator.md) allows the caching policy to be defined for hierarchies. |

## ABAP Keyword Documentation

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Documentation Language</strong></td>
<td>From release 7.95 on, the ABAP Keyword Documentation is delivered and supported in English only.</td>
</tr>
<tr class="even">
<td><strong>CDS Annotation Documentation</strong></td>
<td><p>From release 7.95 on, properties and documentation for <a href="abencds_annotation_glosry.html">CDS annotations</a> delivered as <a href="abensap_annotation_glosry.html">SAP annotations</a> are shown under <a href="abencds_annotations_ktd_docu.html">ABAP CDS - SAP Annotation Documentation</a>. If available, the <a href="abenktd_glosry.html">KTD</a> of an annotation definition is embedded there and/or links to help portal documentation are shown.</p>
<p>The documentation of the <a href="abenabap_annotation_glosry.html">ABAP annotations</a> that formerly appeared at their point of use in the ABAP Keyword Documentation was migrated to KTDs and is shown under <a href="abencds_abap_annos.html">ABAP Annotations</a> now.</p></td>
</tr>
</tbody>
</table>

## ABAP RESTful Application Programming Model

In release 7.95, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

| Modification     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BDEF Friends** | The new optional addition [`with friends`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_with_friends.md) can be used to specify one or more [BDEF extensions](../../abap-glossary/abenrap_extension_glosry.md) as [BDEF friends](../../abap-glossary/abenrap_bdef_friend_glosry.md). A BDEF friend has unrestricted access to all components of the original [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md). For example, a BDEF friend can call [internal RAP BO operations](../../abap-glossary/abenrap_internal_operation_glosry.md) and read or modify RAP BO entities [`IN LOCAL MODE`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapin_local_mode.md). BDEF friends can be used for modularization purposes. |
