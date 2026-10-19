---
title: "News for ABAP Release 9.16"
source_file: abennews-916.html
section: "ABAP Release News > News for ABAP Release 9.1x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 9.16

The kernel release for ABAP release 9.16 is 9.16.

## Expressions and Functions

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Numeric Functions for Statistics and Probability Theory in ABAP</strong></td>
<td><p>The following numeric functions are now available:</p>
<ul>
<li><a href="abenerror_functions.html"><code class="ph codeph">erf</code>, <code class="ph codeph">erfc</code>, <code class="ph codeph">erf_inv</code>, and <code class="ph codeph">erfc_inv</code></a> for calculations with <a href="abenfloating_point_number_glosry.html">floating point numbers</a> and <a href="abendecfloat_glosry.html">decimal floating points numbers</a> implement the error function, the complementary error function and their inverses.</li>
<li><a href="abengamma_functions.html"><code class="ph codeph">gamma</code> and <code class="ph codeph">log_gamma</code></a> implement the gamma and log gamma functions for calculations with floating point numbers and decimal floating points numbers.</li>
<li><a href="abenlower_gamma_functions.html"><code class="ph codeph">gamma_lower</code></a> implements the lower incomplete gamma function and its inverse for calculations with floating point numbers and decimal floating points numbers.</li>
</ul></td>
</tr>
</tbody>
</table>

## System Classes

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>System Classes for Probability Distribution</strong></td>
<td><p>Two new system classes for probability distribution are available:</p>
<ul>
<li><code class="ph codeph">CL_ABAP_PROB_DISTRIBUTION</code> defines probability distributions in ABAP for probabilities of a <a href="abenfloating_point_number_glosry.html">floating point</a> data type.</li>
<li><code class="ph codeph">CL_ABAP_PROB_DISTRIBUTION_DF34</code> defines probability distributions in ABAP for probabilities of the built-in data type <a href="abenbuiltin_types_numeric.html"><code class="ph codeph">decfloat34</code></a>.</li>
</ul>
<p>Both classes allow the generation of random numbers and calculation of quantile, probabilities, and other aspects. The first release includes the following distributions: normal, log-normal, gamma, exponential, and uniform <code class="ph codeph">int</code>/<code class="ph codeph">int8</code> distributions. Discrete and continuous distributions are supported.</p></td>
</tr>
<tr class="even">
<td><strong>Mathematical Constants</strong></td>
<td><p>The following constants for minimum and maximum values are now available as part of class <code class="ph codeph">CL_ABAP_MATH</code>:</p>
<ul>
<li>Minimal positive and not subnormal value for type <code class="ph codeph">decfloat34</code> and <code class="ph codeph">decfloat16</code></li>
<li>Maximal value for type <code class="ph codeph">decfloat34</code> and <code class="ph codeph">decfloat16</code></li>
<li>Smallest floating point number &gt; 0</li>
<li>Difference between smallest floating point number &gt; 1 and 1</li>
</ul>
<p>In addition, the following common mathematical constants are available in class <code class="ph codeph">CL_ABAP_MATH</code>:</p>
<ul>
<li>Euler's constant e</li>
<li>pi</li>
<li>pi squared</li>
<li>pi / 2</li>
<li>pi / 4</li>
<li>Square root of 2, 3, and pi</li>
<li>Decimal logarithm (log10) and binary logarithm (log2) of e</li>
<li>Decimal logarithm of the numbers 2 and 10</li>
</ul>
<p>These constants are available as floating point numbers (<code class="ph codeph">f</code>) and as <code class="ph codeph">decfloat34</code> numbers.</p></td>
</tr>
</tbody>
</table>

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
<td><strong>Non-numeric Results in Aggregate Functions</strong></td>
<td>The result of the aggregate functions <a href="abensql_agg_func.html"><code class="ph codeph">MIN</code></a> and <a href="abensql_agg_func.html"><code class="ph codeph">MAX</code></a> can now be non-numeric for <a href="abapselect_over.html">window expressions</a> and <a href="abenselect_hierarchy_desc_agg.html">hierarchy aggregate navigators</a>.</td>
</tr>
<tr class="even">
<td><strong>Aggregate Functions in Hierarchy Aggregate Navigators</strong></td>
<td>The aggregate function <a href="abensql_agg_func.html"><code class="ph codeph">AVG</code></a> can now be used for the hierarchy aggregate navigator <a href="abenselect_hierarchy_desc_agg.html"><code class="ph codeph">HIERARCHY_DESCENDANTS_AGGREGATE</code></a> if a <code class="ph codeph">JOIN</code> condition is not defined and for the hierarchy aggregate navigator <a href="abenselect_hierarchy_ancs_agg.html"><code class="ph codeph">HIERARCHY_ANCESTORS_AGGREGATE</code></a>.</td>
</tr>
<tr class="odd">
<td><strong>New Spatial Functions</strong></td>
<td><p>The following <a href="abensql_spatial_func.html">spatial functions</a> are now available:</p>
<ul>
<li><code class="ph codeph">ST_3DLENGTH</code></li>
<li><code class="ph codeph">ST_ASMVTGEOM</code></li>
<li><code class="ph codeph">ST_BUFFER</code></li>
<li><code class="ph codeph">ST_CLOSESTPOINTOFAPPROACH</code></li>
<li><code class="ph codeph">ST_FRECHETDISTANCE</code></li>
<li><code class="ph codeph">ST_INTERIORRINGN</code></li>
<li><code class="ph codeph">ST_ISVALIDTRAJECTORY</code></li>
<li><code class="ph codeph">ST_MAKEPOLYGON</code></li>
<li><code class="ph codeph">ST_NEW_POINT</code></li>
<li><code class="ph codeph">ST_NEW_POINTM</code></li>
<li><code class="ph codeph">ST_NEW_POINTZ</code></li>
<li><code class="ph codeph">ST_NEW_POINTZM</code></li>
<li><code class="ph codeph">ST_REMOVEPOINT</code></li>
<li><code class="ph codeph">ST_REVERSE</code></li>
<li><code class="ph codeph">ST_TOUCHES</code></li>
<li><code class="ph codeph">ST_WITHIN</code></li>
</ul></td>
</tr>
<tr class="even">
<td><strong><code class="ph codeph">DISTINCT</code> in <code class="ph codeph">OVER</code> Clause</strong></td>
<td>The addition <code class="ph codeph">DISTINCT</code> is now allowed for the aggregate function <code class="ph codeph">COUNT</code> in a <a href="abensql_win_func.html">window expression</a>.</td>
</tr>
<tr class="odd">
<td><strong>Enhancement of <code class="ph codeph">LPAD</code> and <code class="ph codeph">RPAD</code> Functions</strong></td>
<td>The length <code class="ph codeph">len</code> of the <a href="abensql_string_func.html"><code class="ph codeph">LPAD</code></a> and <a href="abensql_string_func.html"><code class="ph codeph">RPAD</code></a> functions can now be a host variable or an SQL expression. Additionally, the length of <code class="ph codeph">len</code> can be less than 1 and greater than 1333. Both functions can produce the result type <code class="ph codeph">SSTRING</code> with an undefined length.</td>
</tr>
<tr class="even">
<td><strong>New Aggregate Spatial Functions</strong></td>
<td><p>The following <a href="abensql_spatial_func_a.html">aggregate spatial functions</a> are now available:</p>
<ul>
<li><code class="ph codeph">ST_ALPHASHAPEAGGR</code></li>
<li><code class="ph codeph">ST_ALPHASHAPEAREAAGGR</code></li>
<li><code class="ph codeph">ST_ASESRIJSON_MULTICOLUMN</code></li>
<li><code class="ph codeph">ST_ASGEOJSON_MULTICOLUMN</code></li>
<li><code class="ph codeph">ST_ASMVT</code></li>
<li><code class="ph codeph">ST_ASSVGAGGR</code></li>
<li><code class="ph codeph">ST_COLLECTAGGR</code></li>
<li><code class="ph codeph">ST_CONCAVEHULLAGGR</code></li>
<li><code class="ph codeph">ST_CONVEXHULLAGGR</code></li>
<li><code class="ph codeph">ST_ENVELOPEAGGR</code></li>
<li><code class="ph codeph">ST_INTERSECTIONAGGR</code></li>
<li><code class="ph codeph">ST_UNIONAGGR</code></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>New SQL Functions <code class="ph codeph">GREATEST</code> and <code class="ph codeph">LEAST</code></strong></td>
<td>The SQL functions <a href="abensql_arith_func.html"><code class="ph codeph">GREATEST</code></a> and <a href="abensql_arith_func.html"><code class="ph codeph">LEAST</code></a> are now available. These functions determine the largest and smallest value of a set of arguments.</td>
</tr>
<tr class="even">
<td><strong>Retain Nulls in Level-Based Hierarchy</strong></td>
<td>By default, in <a href="abenselect_hierarchy_gen_level.html">level-based hierarchies</a>, if one level column of a row of the data source contains the null value, the row is not included in the SQL hierarchy. With <code class="ph codeph">retain nulls @policy</code> and the value set to <code class="ph codeph">not_trailing</code>, the null value is handled like a normal value in all but the last level.</td>
</tr>
</tbody>
</table>

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
<td><strong>Stricter Rules for Association <code class="ph codeph">ON</code> Conditions in CDS Custom Entities</strong></td>
<td><p>Stricter rules for the association <code class="ph codeph">ON</code> condition for CDS custom entities have been implemented. For details, see <a href="abencds_f1_custom_association.html">CDS DDL - <code class="ph codeph">DEFINE CUSTOM ENTITY</code>, <code class="ph codeph">association</code></a>.</p>
<p>The same rules also apply if other CDS entities define associations with a CDS custom entity as an association target.</p></td>
</tr>
<tr class="even">
<td><strong>New Element Annotations</strong></td>
<td><p>The following <a href="abencds_abap_annos.html">ABAP annotations</a> are now supported as <a href="abencds_f1_element_annotation.html">element annotations</a> with the annotation <a href="abencds_annotations_scopes.html">scope</a> <code class="ph codeph">#ELEMENT</code>.</p>
<ul>
<li><a href="abencds_58258031_anno.html"><code class="ph codeph">AbapCatalog.typeSpec.conversionExit</code></a></li>
<li><a href="abencds_1569826112_anno.html"><code class="ph codeph">AbapCatalog.typeSpec.outputLength</code></a></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>CDS Table Entity, Table Buffering</strong></td>
<td><p><a href="abentable_buffering_glosry.html">Table buffering</a> can be defined for <a href="abencds_table_entity_glosry.html">CDS table entities</a> now:</p>
<ul>
<li>Table buffering can be enabled and disabled with the annotation <a href="abencds_table_entity_buffering.html"><code class="ph codeph">@AbapCatalog.entityBuffer.definitionAllowed: true\|false</code></a></li>
<li>The <a href="abenbuffer_type.html">buffering type</a> can be specified with a CDS table entity buffer defined by <a href="abencds_define_view_entity_buffer.html"><code class="ph codeph">DEFINE TABLE ENTITY BUFFER ON cds_table_entity ...</code></a></li>
</ul>
<p>Table buffering can be defined differently for the layers core, localization, industry, partner and customer.</p></td>
</tr>
<tr class="even">
<td><strong>Static External Entities</strong></td>
<td>With the first release of <a href="abencds_external_entity_glosry.html">CDS external entities</a>, only <a href="abencds_dynamic_ee_glosry.html">dynamic external entities</a> were available. Now, <a href="abencds_static_ee_glosry.html">static external entities</a> are also available. They are defined using the addition <a href="abencds_define_external_entity.html"><code class="ph codeph">PROVIDED BY logical_external_schema</code></a> in the data definition.</td>
</tr>
<tr class="odd">
<td><strong>CDS Static Caches</strong></td>
<td><a href="abenstatic_view_cache_glosry.html">Static caches</a> are now available in ABAP CDS. These can lead to performance gains when aggregated data is cached.</td>
</tr>
</tbody>
</table>

## ABAP RESTful Application Programming Model

In release 9.16, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

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
<td><strong>RAP Change Documents</strong></td>
<td><a href="abenrap_change_documents_glosry.html">RAP change documents</a> are now available. They can be used to log changes of persisted RAP BO data in a <a href="abenchange_document_obj_glosry.html">change document object</a>.</td>
</tr>
<tr class="even">
<td><strong>RAP Copy Action</strong></td>
<td>A new <a href="abenrap_hierarchy_action_glosry.html">RAP hierarchy action</a> is available that can be used in editable treeview scenarios: the <a href="abenrap_copy_action_glosry.html">RAP copy action</a>. It is defined using the syntax addition <a href="abenbdl_copy_action.html"><code class="ph codeph">copy action</code></a>.</td>
</tr>
<tr class="odd">
<td><strong>Dedicated Authorizations for Create-by-Association Operations</strong></td>
<td><a href="abenrap_auth_dep_ent_glosry.html">RAP authorization dependent entities</a> use the authorization control that is defined on the related authorization master entity. For <a href="abenrap_cba_operation_glosry.html">RAP create-by-association operations</a> on an authorization-dependent entity, the system applies the authorization check for updates of the authorization master entity by default. For create by association on <a href="abento_child_association_glosry.html">CDS to-child associations</a>, you can now deviate from this default and specify separate authorizations for create-by-association operations.</td>
</tr>
<tr class="even">
<td><strong>RAP Collaborative Draft</strong></td>
<td>A new <a href="abenrap_draft_handling_glosry.html">RAP draft handling</a> with collaborative capabilities is now available. The <a href="abenrap_collaborative_draft_glosry.html">RAP collaborative draft</a> allows multiple users to work concurrently on the same draft instance. It is defined using the syntax <a href="abenbdl_with_coll_draft.html"><code class="ph codeph">with collaborative draft</code></a>.</td>
</tr>
<tr class="odd">
<td><strong>Authorization Context for Disable: New Options</strong></td>
<td><p>New options are available for the <a href="abencds_auth_context_glosry.html">authorization context</a> after the addition <a href="abenbdl_def_auth_context.html"><code class="ph codeph">for disable</code></a>:</p>
<ul>
<li><a href="abenbdl_def_auth_context.html"><code class="ph codeph">determination</code></a>: The <a href="abenbdl_determinations.html">determinations</a> that are invoked during the <a href="abenrap_save_seq_glosry.html">RAP save sequence</a> automatically skip the authorization objects listed in the associated authorization context <code class="ph codeph">ContextName</code>.</li>
<li><a href="abenbdl_def_auth_context.html"><code class="ph codeph">validation</code></a>: The <a href="abenbdl_validations.html">validations</a> that are invoked during the save sequence automatically skip the authorization objects listed in the associated authorization context <code class="ph codeph">ContextName</code>.</li>
</ul>
<p>The new options are only available for the <a href="abencds_bdef_impl_type_glosry.html">BDEF implementation type</a>.</p></td>
</tr>
<tr class="even">
<td><strong>Privileged Mode in Association-Related Operations in Cross-BO Scenarios</strong></td>
<td>In <a href="abencds_cross_bo_assoc_glosry.html">cross-BO</a> scenarios, when association-related ABAP EML requests on the <a href="abenassociation_source_glosry.html">association source</a> are performed and specify <code class="ph codeph">IN LOCAL MODE</code> (such as <a href="abenrap_rba_operation_glosry.html">read-by-association</a> or <a href="abenrap_cba_operation_glosry.html">create-by-association</a> operations), the <a href="abenassociation_target_glosry.html">association target</a>'s implementation of the operation is accessed in privileged mode (not in local mode), bypassing the association target's authorization checks. This applies only if the association target is specified with a <a href="abenrap_privileged_mode_glosry.html">privileged</a> context.</td>
</tr>
<tr class="odd">
<td><strong>Draft Scope Definition in Cross-BO Scenarios</strong></td>
<td>In cross-BO scenarios, you can now define a <a href="abendraft_scope_glosry.html">draft scope</a> to facilitate cross-BO draft management. Within a defined draft scope, you can edit multiple related <a href="abenbusiness_object_glosry.html">business objects</a> as a single logical unit of work, ensuring consistency and supporting complex transactional scenarios.</td>
</tr>
</tbody>
</table>

### ABAP EML

| Modification                                                                   | Description                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Retry Feature for RAP Local Event Executions**                               | An automatic retry feature is now available to ensure [RAP local events](../../abap-rap-business-objects/abap-for-rap-business-objects/abenmethod_for_entity_event.md) execute in case of temporary issues like locks on RAP BO instances. The framework will attempt to retry up to three times. You can design your implementation for the framework to automatically retry event execution after a specified time. |
| **New Method `GET_PRIVILEGED_ACCESS_PROFILE` of the `CL_ABAP_BEHV_AUX` Class** | Returns information about the privileged context. It can be used for the save phase only.                                                                                                                                                                                                                                                                 |

## Transformations

| Modification                                      | Description                                                                                                                          |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **New Addition `JSON` for `CALL TRANSFORMATION`** | The new additions [`SOURCE JSON`](../../abap-programming-language/abap-data-interchange-formats/abapcall_transformation.md) and [`RESULT JSON`](../../abap-programming-language/abap-data-interchange-formats/abapcall_transformation.md) are now available. |
