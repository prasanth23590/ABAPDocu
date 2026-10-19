---
title: "News for ABAP Release 7.91"
source_file: abennews-791.html
section: "ABAP Release News > News for ABAP Release 7.9x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.91

The kernel release for ABAP release 7.91 is 7.91.

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
<td><strong>CDS Analytical Projection View, Projected Entity</strong></td>
<td><a href="abencds_analytical_pv_glosry.html">CDS analytical projection views</a> can now also have <a href="abencds_anal_dim_view_glosry.html">analytical dimension views</a> as <a href="abencds_pv_projected_entity_glosry.html">projected entity</a>.</td>
</tr>
<tr class="even">
<td><strong>Release of CDS Simple Types</strong></td>
<td><a href="abencds_simple_type_glosry.html">CDS simple types</a> define <a href="abenelementary_data_type_glosry.html">elementary data types</a> natively in <a href="abenabap_cds_glosry.html">ABAP CDS</a>. A CDS simple type can be enriched with metadata using <a href="abencds_annotation_glosry.html">CDS annotations</a>. The syntax statement for defining a CDS simple type is <a href="abencds_define_simple_type.html"><code class="ph codeph">DEFINE TYPE</code></a>.</td>
</tr>
<tr class="odd">
<td><strong>New Cardinality Syntax for Associations and Joins</strong></td>
<td><p>A new syntax for specifying the <a href="abencardinality_glosry.html">cardinality</a> of <a href="abencds_association_glosry.html">CDS associations</a>, CDS <a href="abenjoin_glosry.html">joins</a>, and of filter conditions of <a href="abensql_path_expression_glosry.html">CDS path expressions</a> is now available:</p>
<p><code class="ph codeph">{MANY \| ONE \| {EXACT ONE}} TO {MANY \| ONE \| {EXACT ONE}}</code></p>
<p>This syntax allows a <a href="abensource_cardinality_glosry.html">source</a> and a <a href="abentarget_cardinality_glosry.html">target cardinality</a> to be specified, while the previously available numeric syntax only allowed the target cardinality to be specified. The new cardinality syntax can be used to improve query performance. It is available in <a href="abencds_v2_view_glosry.html">CDS view entities</a>, <a href="abencds_projection_view_glosry.html">CDS projection views</a>, <a href="abencds_custom_entity_glosry.html">CDS custom entities</a>, and <a href="abencds_abstract_entity_glosry.html">CDS abstract entities</a>.</p></td>
</tr>
</tbody>
</table>

## ABAP CDS Access Control

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>New Type of Access Rule for CDS Projection Views</strong></td>
<td>A new type of <a href="abencds_dcl_role_rules.html">access rule</a> is available for CDS projection views of type <a href="abencds_transactional_pv_glosry.html">CDS transactional query</a>: the <a href="abencds_dcl_role_proj_rule.html"><code class="ph codeph">projection_rule</code></a> defined with the statement <a href="abencds_dcl_role_proj_rule.html"><code class="ph codeph">GRANT SELECT ON ... AS PROJECTION ON ... FALLBACK ASSOCIATION ...</code></a>.</td>
</tr>
<tr class="even">
<td><strong>New DCL Functions</strong></td>
<td><p>Two new DCL functions are available:</p>
<ul>
<li><a href="abencds_f1_dcl_function.html"><code class="ph codeph">SWITCH_RUNTIME_STATE</code></a></li>
<li><p><a href="abencds_f1_dcl_function.html"><code class="ph codeph">TOGGLE_RUNTIME_STATE</code></a></p>
<p>Both functions retrieve the runtime state of a switch in the Switch Framework.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Internal Tables

| Modification                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Improved Optimization of the `WHERE` Condition** | Up to now, an [optimization of the `WHERE` condition](../../abap-programming-language/abap-processing-internal-data/abenitab_where_optimization.md) by using key access took place only under very limited circumstances where the key value pairs had to be compared explicitly for equality and combined by `AND`. Now, the compiler analyzes the `WHERE` condition thoroughly and tries itself to extract the key/value pairs that are necessary for the key access. |

## ABAP SQL

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>New Cardinality Syntax for Joins</strong></td>
<td><p>A new syntax for specifying the <a href="abencardinality_glosry.html">cardinality</a> of <a href="abenjoin_glosry.html">joins</a> is available:</p>
<p><code class="ph codeph">{MANY \| ONE \| {EXACT ONE}} TO {MANY \| ONE \| {EXACT ONE}}</code></p>
<p>This syntax allows specifying a <a href="abensource_cardinality_glosry.html">source</a> and a <a href="abentarget_cardinality_glosry.html">target cardinality</a>. The new cardinality syntax can be used to improve query performance. It can also be used in <a href="abenabap_sql_path_filter.html">SQL path expressions</a> and <a href="abapwith_associations_defining.html">CTE associations</a>.</p></td>
</tr>
<tr class="even">
<td><strong>New Addition <code class="ph codeph">PRIVILEGED ACCESS</code></strong></td>
<td>With the new addition <a href="abapselect_privileged_access.html"><code class="ph codeph">PRIVILEGED ACCESS</code></a>, <a href="abencds_access_control_glosry.html">CDS access control</a> can be disabled for a complete <code class="ph codeph">SELECT</code> statement.</td>
</tr>
</tbody>
</table>

## Assignments

| Modification                                                  | Description                                                                                                                                    |
|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **`DEFAULT` as New Addition to the `CORRESPONDING` Operator** | The addition [`DEFAULT`](../../abap-programming-language/abap-processing-internal-data/abencorresponding_constr_mapping.md) allows the assignment of values for a target component based on an expression. |

## ABAP RESTful Application Programming Model

In release 7.91, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

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
<td><strong>RAP Side Effects</strong></td>
<td><a href="abenrap_side_effects_glosry.html">RAP side effects</a> define interdependencies among RAP BO properties that trigger a reload of the affected properties on the user interface. Side effects are translated into annotations in the OData metadata of a RAP service. The syntax for defining RAP side effects is <a href="abenbdl_side_effects.html"><code class="ph codeph">side effects</code></a>.</td>
</tr>
<tr class="even">
<td><strong>Abstract BDEF Extensions</strong></td>
<td>The new statement <a href="abenbdl_extension_for_abstract.html"><code class="ph codeph">extension for abstract</code></a> of the RAP BDL makes it possible to extend <a href="abencds_abstract_bdef_glosry.html">abstract behavior definitions</a> with <a href="abenrap_abs_bdef_ext_glosry.html">abstract BDEF extensions</a>. Abstract BDEFs are mainly used as parameters for RAP actions, RAP functions, and RAP business events. An abstract BDEF extension allows you to extend these parameters.</td>
</tr>
<tr class="odd">
<td><strong>BDEF Extension Layering</strong></td>
<td>It is now possible to extend a <a href="abenrap_extension_glosry.html">BDEF extension</a> with further BDEF extensions. This is referred to as <a href="abenrap_ext_layering_glosry.html">extension layering</a>. As a prerequisite, the BDEF extension in question must be explicitly enabled for extensibility. The rules are described in the topic <a href="abenbdl_extensibility_enabling_ext.html">RAP - Extensibility Enabling for BDEF Extensions</a>. Technically, the BDEF extension that extends another extension is a regular extension and the respective rules apply.</td>
</tr>
<tr class="even">
<td><strong>Authorization Context for Disable, New Options</strong></td>
<td><p>There are further options available for the <a href="abencds_auth_context_glosry.html">authorization context for disable</a> after the addition <a href="abenbdl_def_auth_context.html"><code class="ph codeph">for disable</code></a>:</p>
<ul>
<li><a href="abenbdl_def_auth_context.html"><code class="ph codeph">save:early</code></a>: Skips the authorization checks defined in the respective authorization context in the <a href="abenearly_rap_save_phase_glosry.html">early save phases</a> <a href="abensaver_finalize.html"><code class="ph codeph">finalize</code></a> and <a href="abensaver_check_before_save.html"><code class="ph codeph">check_before_save</code></a>.</li>
<li><a href="abenbdl_def_auth_context.html"><code class="ph codeph">save:late</code></a>: Skips the authorization checks defined in the respective authorization context in the <a href="abenlate_rap_save_phase_glosry.html">late save phases</a> <a href="abensaver_adjust_numbers.html"><code class="ph codeph">adjust_numbers</code></a>, <a href="abensaver_method_save.html"><code class="ph codeph">save</code></a>, and <a href="abaprap_saver_meth_save_modified.html"><code class="ph codeph">save_modified</code></a>.</li>
</ul></td>
</tr>
</tbody>
</table>
