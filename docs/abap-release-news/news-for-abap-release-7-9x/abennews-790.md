---
title: "News for ABAP Release 7.90"
source_file: abennews-790.html
section: "ABAP Release News > News for ABAP Release 7.9x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.90

The kernel release for ABAP release 7.90 is 7.90.

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
<td><strong><code class="ph codeph">@AbapCatalog.preserveKey</code> is Obsolete</strong></td>
<td><p>The CDS annotation <code class="ph codeph">@AbapCatalog.preserveKey</code> is <a href="abencds_annotation_obsolete.html">obsolete</a> and has partly a different behavior now.</p>
<p>The annotation was used before Release 7.90 to define the key fields of the <a href="abencds_mngdddic_view_glosry.html">CDS-managed DDIC view</a> of an obsolete <a href="abencds_v1_view_glosry.html">CDS DDIC-based view</a>. The annotation can be kept in existing data definitions, but it does not have an effect any more and leads to a syntax check warning. The key fields of the CDS-managed DDIC view are always defined by the addition <a href="abencds_select_list_entry_v2.html"><code class="ph codeph">key</code></a> in the <code class="ph codeph">SELECT</code> list.</p>
<p>The change in behavior between 7.89 and 7.90 is incompatible. The key fields of the CDS-managed DDIC view of an obsolete CDS DDIC-based view are defined differently now for views where the annotation was not specified or where it was specified with the value <code class="ph codeph">false</code>. The value <code class="ph codeph">false</code> was used to define the key fields of the CDS-managed DDIC view as for a DDIC database views in ABAP Dictionary, regardless of the addition <code class="ph codeph">KEY</code>. It was also the standard value, when the annotation was not specified. Now, the behavior is always as for the value <code class="ph codeph">true</code>.</p></td>
</tr>
</tbody>
</table>

## Data Types

| Modification                           | Description                                                                                                                                                                                                                      |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Absolute Type Names for Line Types** | The new specification `\LINE` allows the line type of an internal table to be specified in an [absolute type name](../../abap-programming-language/abap-data-types-and-data-objects/abentype_names.md). `\LINE` can be followed by `-comp` to specify the type of a component of the line type. |

## Assignments

| Modification                        | Description                                                                                                                                                                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returning a Value with `RETURN`** | In [functional methods](../../abap-glossary/abenfunctional_method_glosry.md), the statement [`RETURN`](../../abap-programming-language/abap-calling-and-exiting-program-units/abapreturn.md) can be used to assign the result of an expression [`expr`](../../abap-programming-language/abap-calling-and-exiting-program-units/abapreturn.md) to the [return value](../../abap-glossary/abenreturn_value_glosry.md) when terminating the method. |

## ABAP SQL

| Modification                               | Description                                                                                                                    |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| **ABAP SQL Expressions on the Right Side** | [ABAP SQL expressions](../../abap-programming-language/abap-database-access/abenabap_sql_expr_logexp.md) can be defined on the right side of a condition enclosed in parentheses. |

## ABAP RESTful Application Programming Model

In release 7.90, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Interface BDEF, New Field Characteristics</strong></td>
<td><p>In <a href="abencds_interface_bdef_glosry.html">RAP interface behavior definitions</a>, the following <a href="abenrap_field_char_glosry.html">RAP field characteristics</a> are now available:</p>
<ul>
<li><a href="abenbdl_field_interface.html"><code class="ph codeph">readonly</code></a></li>
<li><a href="abenbdl_field_interface.html"><code class="ph codeph">mandatory:create</code></a></li>
<li><a href="abenbdl_field_interface.html"><code class="ph codeph">readonly:update</code></a></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Managed and Unmanaged RAP BO, New Field Characteristic</strong></td>
<td>A new <a href="abenrap_field_char_glosry.html">RAP field characteristic</a> is available for managed and unmanaged RAP BOs: <a href="abenbdl_field_char.html"><code class="ph codeph">notrigger[:warn]</code></a>. Fields with this attribute must not be used in a trigger condition of a <a href="abenrap_validation_glosry.html">RAP validation</a> or a <a href="abenrap_determination_glosry.html">RAP determination</a>.</td>
</tr>
<tr class="odd">
<td><strong>Static Default Factory Actions</strong></td>
<td>The syntax addition <a href="abenbdl_action_default_factory.html"><code class="ph codeph">default</code></a> is available for static factory actions in managed, unmanaged, and projection BDEFs. Exactly one static factory action per <a href="abenrap_bo_entity_glosry.html">RAP BO entity</a> can be defined as default static factory action. The addition <code class="ph codeph">default</code> is evaluated by consuming frameworks, such as OData.</td>
</tr>
</tbody>
</table>
