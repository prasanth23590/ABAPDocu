---
title: "News for ABAP Release 7.89"
source_file: abennews-789.html
section: "ABAP Release News > News for ABAP Release 7.8x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.89

The kernel release for ABAP release 7.89 is 7.89.

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
<td><strong>CDS Custom Entity Extensions</strong></td>
<td>The new statement <a href="abencds_extend_custom_entity.html"><code class="ph codeph">EXTEND CUSTOM ENTITY</code></a> of the DDL of ABAP CDS makes it possible to add new elements to existing <a href="abencds_custom_entity_glosry.html">CDS custom entities</a> by using <a href="abencds_cus_entity_extend_glosry.html">CDS custom entity extensions</a>.</td>
</tr>
<tr class="even">
<td><strong>CDS View Entity, <code class="ph codeph">LEFT</code> and <code class="ph codeph">RIGHT</code></strong></td>
<td>In <a href="abencds_v2_view_glosry.html">CDS view entities</a>, the functions <a href="abencds_sql_functions_character_v2.html"><code class="ph codeph">LEFT</code></a> and <a href="abencds_sql_functions_character_v2.html"><code class="ph codeph">RIGHT</code></a> have been enhanced. They now accept literals, fields, parameters, expressions, and built-in functions as argument for the parameter <code class="ph codeph">len</code>.</td>
</tr>
<tr class="odd">
<td><strong>CDS View Entity, <code class="ph codeph">CASE ELSE NULL</code></strong></td>
<td>In <a href="abencds_v2_view_glosry.html">CDS view entities</a>, the addition <a href="abencds_case_expression_v2.html"><code class="ph codeph">ELSE NULL</code></a> is available in simple and complex <a href="abencds_case_expression_v2.html">case distinctions</a>. It defines the <a href="abennull_value_glosry.html">null value</a> as return value of the <code class="ph codeph">ELSE</code> branch.</td>
</tr>
<tr class="even">
<td><strong>CDS View Entity, Table Buffering</strong></td>
<td><a href="abencds_view_entity_b_glosry.html">CDS view entity buffering</a> was enhanced: <a href="abencds_v2_view_buffering.html">View on view buffering</a> is now supported, under the precondition that the CDS view entity used as data source meets certain requirements.</td>
</tr>
<tr class="odd">
<td><strong>CDS DDIC-Based Views Are Obsolete</strong></td>
<td><a href="abencds_v1_view_glosry.html">CDS DDIC-based views (obsolete)</a>, defined using the statement <a href="abencds_define_view_v1.html"><code class="ph codeph">DEFINE VIEW</code></a>, are <a href="abencds_v1_views.html">obsolete</a>. When creating new data models, <a href="abencds_v2_view_glosry.html">CDS view entities</a>, defined using <a href="abencds_define_view_entity.html"><code class="ph codeph">DEFINE VIEW ENTITY</code></a>, should be used instead.</td>
</tr>
<tr class="even">
<td><strong>ABAP Program That Lists Usages of CDS-Managed DDIC Views</strong></td>
<td><p>Using <a href="abencds_mngdddic_view_glosry.html">CDS-managed DDIC views</a> has been declared <a href="abencds_access_obsolete.html">obsolete</a>. The following ABAP program lists all <a href="abenrepository_object_glosry.html">repository objects</a> that use CDS-managed DDIC views:</p>
<p><code class="ph codeph">RUT_WHERE_USE_SQLVIEW</code>.</p></td>
</tr>
</tbody>
</table>

## ABAP CDS Access Control

| Modification                                              | Description                                                                                                                                                                                                                                                                                    |
|-----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`DEFINE ROLE` Statement Has New Addition `SWITCHABLE`** | The new addition [`SWITCHABLE`](../../abap-core-data-services-abap-cds/abap-cds-access-control/abencds_f1_define_role.md) is now available for the [`DEFINE ROLE`](../../abap-core-data-services-abap-cds/abap-cds-access-control/abencds_f1_define_role.md) statement. Using this addition, the content of the role reacts to status changes in the Switch Framework with respect to the package of the access control. |

## Assignments

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>New Dynamic Component Specification in <code class="ph codeph">ASSIGN</code></strong></td>
<td>Components of structures can be assigned to field symbols with the new syntax <a href="abapassign_dynamic_components.html"><code class="ph codeph">struc-(comp)</code></a> that largely replaces the variant <code class="ph codeph">ASSIGN COMPONENT OF</code>.</td>
</tr>
<tr class="even">
<td><strong>New Addition <code class="ph codeph">ELSE UNASSIGN</code></strong></td>
<td><p>The new addition <a href="abapassign_else_unassign.html"><code class="ph codeph">ELSE UNASSIGN</code></a> can be specified for the following variants of the statement <a href="abapassign.html"><code class="ph codeph">ASSIGN</code></a>:</p>
<ul>
<li><a href="abapassign_mem_area_dynamic_dobj.html">dynamic assignments</a></li>
<li><a href="abapassign_dynamic_components.html">assignments of dynamic components</a></li>
<li><a href="abapassign_mem_area_dynamic_access.html">dynamic access</a></li>
<li><p><a href="abapassign_mem_area_writable_exp.html">assignment of a table expression</a></p>
<p>It can be also specified with the addition <code class="ph codeph">ASSIGNING</code> of the following internal table statements:</p></li>
<li><a href="abapread_table_outdesc.html"><code class="ph codeph">READ TABLE</code></a></li>
<li><a href="abaploop_at_itab_result.html"><code class="ph codeph">LOOP AT itab</code></a></li>
<li><a href="abapinsert_itab_result.html"><code class="ph codeph">INSERT</code></a></li>
<li><a href="abapmodify_itab_result.html"><code class="ph codeph">MODIFY</code></a></li>
</ul>
<p>All these statements set <code class="ph codeph">sy-subrc</code>. If an assignment is not successful, <code class="ph codeph">sy-subrc</code> is set to the value 4 or sometimes 8. If the addition <code class="ph codeph">ELSE UNASSIGN</code> is specified, the state of the field symbol is set to unassigned in that case. The field symbol is assigned only if the assignment is successful. If <code class="ph codeph">ELSE UNASSIGN</code> is not specified, the field symbol keeps its previous state, which was the only behavior up to now. Using <code class="ph codeph">ELSE UNASSIGN</code> introduces the same behavior as for the <a href="abapassign_mem_area_static_dobj.html">static variant</a> to the above variants. In another way around, one can say that the static variant uses <code class="ph codeph">ELSE UNASSIGN</code> implicitly.</p></td>
</tr>
</tbody>
</table>

## Expressions and Functions

| Modification            | Description                                                                                                                                                                                                                                                    |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Inline Declarations** | The new [declaration operator](../../abap-glossary/abendeclaration_operator_glosry.md) [`FINAL`](../../abap-programming-language/abap-declarations/abenfinal_inline.md) declares an [immutable variable](../../abap-glossary/abenimmutable_variable_glosry.md) that cannot be assigned another value at other write positions of the same context. |

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
<td><strong>Support for <code class="ph codeph">ORDER BY</code> in the ABAP SQL In-Memory Engine</strong></td>
<td><p>The <a href="abenabap_sql_inmemeng_glosry.html">ABAP SQL in-memory engine</a> fully supports the <a href="abaporderby_clause.html"><code class="ph codeph">ORDER BY</code></a> clause now:</p>
<ul>
<li><code class="ph codeph">ORDER BY</code> no longer bypasses <a href="abentable_buffering_glosry.html">table buffering</a>. Before, it bypassed table buffering in cases where single columns were specified as sort keys and these columns were not a left-aligned subset of the primary key in the correct order or if the addition <code class="ph codeph">DESCENDING</code> was specified for a column.</li>
<li><code class="ph codeph">ORDER BY</code> can now be used with <a href="abapselect_itab.html"><code class="ph codeph">SELECT FROM @itab</code></a> without transporting the internal table to the database. This allows looping over an internal table in a sequence defined by <code class="ph codeph">ORDER BY</code> and the sorting of internal tables by expressions.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong><code class="ph codeph">ORDER BY n</code></strong></td>
<td>In the <a href="abaporderby_clause.html">column list</a> of the <a href="abaporderby_clause.html"><code class="ph codeph">ORDER BY</code></a> clause, a literal or a host constant of an integer type is handled as the column position in the result set of the query. This feature is undocumented and behaves partly undefined. With release 7.96 the behavior is defined and documented.</td>
</tr>
</tbody>
</table>

## ABAP RESTful Application Programming Model

In release 7.89, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

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
<td><strong>Define Authorization Context</strong></td>
<td>It is now possible to define <a href="abenbdl_def_auth_context.html">authorization contexts</a> in a RAP behavior definition using the keyword <code class="ph codeph">define authorization context</code>. There are different ways to activate an authorization context. When activated, all authorization objects listed in the respective context are always successful, that means, the respective authorization checks are skipped.</td>
</tr>
<tr class="even">
<td><strong>With Privileged Mode Disabling</strong></td>
<td>The new syntax <code class="ph codeph">with privileged mode disabling</code> supersedes the deprecated version <code class="ph codeph">with privileged mode</code>. The new syntax version disables an <a href="abenbdl_authorization_context.html">authorization contexts</a> when accessing the RAP BO in question with a privileged EML call.</td>
</tr>
<tr class="odd">
<td><strong>Variants to Define a RAP Own Authorization Context</strong></td>
<td><p>New variants are available for defining a <a href="abencds_own_ac_glosry.html">RAP own authorization context</a>:</p>
<ul>
<li><a href="abenbdl_def_own_auth_context.html"><code class="ph codeph">define own authorization context by privileged mode;</code></a></li>
<li><a href="abenbdl_def_own_auth_context.html"><code class="ph codeph">define own authorization context by privileged mode and { ... }</code></a></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>BDEF Extensions for RAP BOs</strong></td>
<td><a href="abenrap_extension_glosry.html">BDEF extensions</a> for RAP BOs can be defined using the statement <a href="abenbdl_extensibility_managed_unm.html"><code class="ph codeph">extension</code></a>.</td>
</tr>
<tr class="odd">
<td><strong>BDEF Extensions for RAP Projection BOs</strong></td>
<td><a href="abenrap_projec_bdef_ext_glosry.html">BDEF projection extensions</a> for <a href="abenrap_projection_bo_glosry.html">RAP projection business objects</a> can be defined using the statement <a href="abenbdl_extensibility_projection.html"><code class="ph codeph">extension for projection</code></a>.</td>
</tr>
<tr class="even">
<td><strong>New Version of BDEF Strict Mode</strong></td>
<td>A new version of <a href="abenrap_strict_mode_glosry.html">BDEF strict mode</a> is available: Strict mode version 2, specified using <a href="abenbdl_strict_2.html"><code class="ph codeph">strict(2)</code></a>. It applies even more syntax checks than the first version.</td>
</tr>
<tr class="odd">
<td><strong>Draft Query Views for Draft-Enabled RAP BOs</strong></td>
<td>The new syntax addition <a href="abenbdl_draft_query_view.html"><code class="ph codeph">query</code></a> is available to define a <a href="abendraft_query_view_glosry.html">draft query view</a> for a <a href="abendraft_rap_bo_glosry.html">draft-enabled RAP BO</a>. This addition is optional. Only in the context of <a href="abenrap_extensibility_glosry.html">RAP extensibility</a> is it a mandatory prerequisite for the <a href="abenc0_contract_glosry.html">C0 release</a> of the <a href="abencds_behavior_definition_glosry.html">CDS behavior definition</a> in question.</td>
</tr>
<tr class="even">
<td><strong><code class="ph codeph">result selective</code> for Deep Result Types</strong></td>
<td>The addition <a href="abenbdl_action_output_para.html"><code class="ph codeph">result selective</code></a> is now also possible for deep result types. It can be specified for an <a href="abenbdl_action_output_para.html">output parameter</a> of a <a href="abenrap_action_glosry.html">RAP action</a> or <a href="abenrap_function_glosry.html">RAP function</a> to return only parts of the result structure.</td>
</tr>
<tr class="odd">
<td><strong>RAP Business Events</strong></td>
<td>Using <a href="abenrap_entity_event_glosry.html">RAP business events</a>, the ABAP RESTful Application Programming Model now offers native support for event-driven architecture. RAP business events are defined with the language element <a href="abenbdl_event.html"><code class="ph codeph">event</code></a>. A flat or deep output parameter can optionally be specified.</td>
</tr>
<tr class="even">
<td><strong>RAP Save Actions with Phase Specification</strong></td>
<td><a href="abenbdl_action_onsave.html">RAP save actions</a> can now specify one or both of the <a href="abenabp_saver_method_glosry.html">RAP saver methods</a> <code class="ph codeph">finalize</code> or <code class="ph codeph">adjustnumbers</code> in brackets to indicate the RAP saver method during which the action can be executed.</td>
</tr>
<tr class="odd">
<td><strong>Repeatable RAP Actions and Functions</strong></td>
<td><a href="abenrap_action_glosry.html">RAP actions</a> and <a href="abenrap_function_glosry.html">RAP functions</a> can be defined as <a href="abenbdl_action_repeatable.html"><code class="ph codeph">repeatable</code></a>. This syntax addition explicitly allows multiple executions of the same action or function on the same <a href="abenrap_bo_entity_inst_glosry.html">RAP BO entity instance</a> within the same <a href="abenabap_eml_glosry.html">ABAP EML</a> or <a href="abenodata_glosry.html">OData</a> request. The <a href="abenrap_derived_type_glosry.html">BDEF derived type</a> of a repeatable action or function has an extra <a href="abapderived_types_cid.html"><code class="ph codeph">%cid</code></a> component, in contrast to the BDEF derived type of non-repeatable actions or function.</td>
</tr>
</tbody>
</table>

### CDS SDL

| Modification                                  | Description                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CDS Service Definition Extension**          | It is now possible to define [service definition extensions](../../abap-glossary/abencds_service_def_ext_glosry.md) in [CDS SDL](../../abap-glossary/abencds_sdl_glosry.md) using the statement [`EXTEND SERVICE`](../../abap-core-data-services-abap-cds/abap-cds-service-definitions/abensrvd_extend_service.md).                                                                                                                                                    |
| **CDS Service Definition, Provider Contract** | The new statement [`PROVIDER CONTRACTS`](../../abap-core-data-services-abap-cds/abap-cds-service-definitions/abensrvd_provider_contract.md) is now available for [CDS service definitions](../../abap-glossary/abencds_service_definition_glosry.md). A provider contract defines the type of [service binding](../../abap-glossary/abenservice_binding_glosry.md) that is to be used for a service definition. The effect is that stricter syntax checks are applied. |

### ABAP EML

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Entity Manipulation Language</strong></td>
<td><ul>
<li><p><a href="abapraise_entity_event.html"><code class="ph codeph">RAISE ENTITY EVENT</code></a></p>
<p>It is now possible to raise a <a href="abenrap_entity_event_glosry.html">RAP entity event</a> using this statement.</p></li>
<li><p><a href="abapread_entity_entities.html"><code class="ph codeph">READ</code></a> and <a href="abapmodify_entity_entities.html"><code class="ph codeph">MODIFY</code></a></p>
<p>The <code class="ph codeph">FIELDS ( ... ) WITH</code> addition for <a href="abapread_entity_entities_fields.html"><code class="ph codeph">READ</code></a> and <a href="abapmodify_entity_entities_fields.html"><code class="ph codeph">MODIFY</code></a> supports the setting of <code class="ph codeph">%control</code> regarding components in <a href="abenbdl_action_input_param.html"><code class="ph codeph">deep</code> input parameters</a> in the context of deep <a href="abenrap_action_glosry.html">action</a> and <a href="abenrap_function_glosry.html">function</a> parameters.</p></li>
</ul></td>
</tr>
</tbody>
</table>
