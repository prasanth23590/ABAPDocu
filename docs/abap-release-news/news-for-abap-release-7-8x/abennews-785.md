---
title: "News for ABAP Release 7.85"
source_file: abennews-785.html
section: "ABAP Release News > News for ABAP Release 7.8x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.85

The kernel release for ABAP release 7.85 is 7.85.

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
<td><strong>CDS Abstract Entity, To-Parent Association</strong></td>
<td>In <a href="abencds_abstract_entity_glosry.html">CDS abstract entities</a>, it is now possible to define <a href="abento_parent_association_glosry.html">to-parent associations</a> without <code class="ph codeph">ON</code> condition. The <code class="ph codeph">ON</code> condition can be left out if the association target is also a CDS abstract entity.</td>
</tr>
<tr class="even">
<td><strong>CDS View Entity, New Set Operators</strong></td>
<td><p>In <a href="abencds_v2_view_glosry.html">CDS view entities</a>, two new <a href="abencds_set_operators_glosry.html">set operators</a> are available:</p>
<ul>
<li><a href="abencds_except_v2.html"><code class="ph codeph">EXCEPT</code></a></li>
<li><a href="abencds_intersect_v2.html"><code class="ph codeph">INTERSECT</code></a></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>CDS View Entity, Extended Expression Matrix</strong></td>
<td><p>In <a href="abencds_v2_view_glosry.html">CDS view entities</a>, the expression matrix has been extended:</p>
<ul>
<li>In a <a href="abencds_searched_case_expr_v2.html">searched case expression</a>, arithmetic expressions and case expressions are supported as operands.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Migration Tool for CDS Views</strong></td>
<td><p>The following documented ABAP program is now available for migrating CDS DDIC-based views to CDS view entities:</p>
<p><code class="ph codeph">RUTDDLSV2MIGRATION</code>.</p></td>
</tr>
<tr class="odd">
<td><strong>New <code class="ph codeph">AbapCatalog</code> Annotations</strong></td>
<td><p>The following new <code class="ph codeph">AbapCatalog.extensibility</code> annotations have been released:</p>
<ul>
<li><a href="abencds_view_entity_anno.html"><code class="ph codeph">AbapCatalog.extensibility.allowNewdataSources</code></a></li>
<li><a href="abencds_view_entity_anno.html"><code class="ph codeph">AbapCatalog.extensibility.dataSources</code></a></li>
<li><a href="abencds_f1_entity_annotations.html"><code class="ph codeph">AbapCatalog.extensibility.elementSuffix</code></a></li>
<li><a href="abencds_f1_entity_annotations.html"><code class="ph codeph">AbapCatalog.extensibility.extensible</code></a></li>
<li><a href="abencds_f1_entity_annotations.html"><code class="ph codeph">AbapCatalog.extensibility.quota.maximumBytes</code></a></li>
<li><a href="abencds_f1_entity_annotations.html"><code class="ph codeph">AbapCatalog.extensibility.quota.maximumFields</code></a></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Using CDS-Managed DDIC Views is Obsolete</strong></td>
<td>For each <a href="abencds_v1_view_glosry.html">CDS DDIC-based view (obsolete)</a>, a <a href="abencds_mngdddic_view_glosry.html">CDS-managed DDIC view (obsolete)</a> is created in ABAP Dictionary upon activation. Using this <a href="abencds_mngdddic_view_glosry.html">CDS-managed DDIC view (obsolete)</a>, for example for typing or for accessing the CDS entity in question, is <a href="abencds_access_obsolete.html">obsolete</a> from now on. The reason is the release of a new type of CDS entity, the <a href="abencds_v2_view_glosry.html">CDS view entity</a>, which will replace <a href="abencds_v1_view_glosry.html">CDS DDIC-based views (obsolete)</a> in the future. CDS view entities do not have a <a href="abencds_mngdddic_view_glosry.html">CDS-managed DDIC view (obsolete)</a> attached and in case of a migration from CDS DDIC-based view (obsolete) to CDS view entity, each usage of a <a href="abencds_mngdddic_view_glosry.html">CDS-managed DDIC view (obsolete)</a> leads to a syntax error.</td>
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
<td><strong>Graceful Behavior in Access Condition Inheritance for Missing Dictionary Elements</strong></td>
<td><p>From this release on, authors of access controls can mark a subset of the CDS elements used in their access conditions as optional, so that CDS entities which inherit their access conditions are not affected by a Day-1-impact any more.</p>
<p><code class="ph codeph">GRANT SELECT ON cds_entity WITH OPTIONAL ELEMENTS ( element1 DEFAULT (TRUE|FALSE), ...) WHERE ...</code></p>
<p><a href="abencds_dcl_role_cond_rule.html">More Information</a></p></td>
</tr>
<tr class="even">
<td><strong>Unified Syntax for Authorization Objects, Authorization Fields and SACF Scenario Names</strong></td>
<td><p>At all locations of access controls, references to authorization objects, authorization fields, and SACF scenario names can be written in identifier syntax when they comply with it and in string syntax with single apostrophes as an alternative.</p>
<p>Before:</p>
<p><code class="ph codeph">( ... ) = ASPECT PFCG_AUTH( S_OBJ IN SCENARIO 'THESCENARIO' )</code></p>
<p>Now allowed:</p>
<p><code class="ph codeph">( ... ) = ASPECT PFCG_AUTH( S_OBJ IN SCENARIO TheScenario )</code></p>
<p><a href="abencds_f1_define_role.html">More Information</a></p></td>
</tr>
<tr class="odd">
<td><strong>Additional Filtering of User-Defined Aspect Usage</strong></td>
<td><p>When using user-defined aspects, these can now denominate an arbitrary set of their elements (path expressions are supported) as filter element. These filter elements can by referenced when using the user-defined aspect in an access condition.</p>
<p><code class="ph codeph">DEFINE ASPECT ... AS SELECT FROM ... WITH USER ELEMENT ... WITH FILTER ELEMENTS ( element1, element2 AS alias2 ) { ... } WHERE ( ... ) = ASPECT ... FILTER BY ( element1 = 'X' OR alias2 IS NOT NULL )</code></p>
<p><a href="abencds_f1_cond_aspect.html">More Information</a></p></td>
</tr>
<tr class="even">
<td><strong>Condition Replacement for Role-Based Inheritance</strong></td>
<td><p>The <code class="ph codeph">REPLACING</code> section formerly only available to entity-based inheritance</p>
<p><code class="ph codeph">INHERITING CONDITIONS FROM ENTITY cds_entity</code></p>
<p>is now also available for role-based inheritance</p>
<p><code class="ph codeph">INHERIT role FOR GRANT SELECT ON cds_entity</code></p>
<p><a href="abencds_f1_cond_inherit.html">More Information</a></p></td>
</tr>
<tr class="odd">
<td><strong>Generic Element Replacement for Condition Inheritance</strong></td>
<td><p>The <code class="ph codeph">REPLACING</code> section of condition inheritance now supports a generic replacement step to replace an arbitrary field or association of the inheritance source with an arbitrary field or association of the inheritance target.</p>
<p><code class="ph codeph">WHERE INHERITING CONDITIONS FROM ENTITY Source REPLACING { ELEMENT Element1OfSource WITH Element1OfTarget, ELEMENT Assoc1OfSource WITH Assoc1[r = 4].Assoc2OfTarget, ELEMENT Assoc2(p : $parameters.p1)[q = 1].Field WITH MyShortField }</code></p>
<p><a href="abencds_f1_cond_inherit_replacing.html">More Information</a></p></td>
</tr>
<tr class="even">
<td><strong>Enabling/Disabling of Access Conditions Based on the State of SACF</strong></td>
<td><p>Respecting settings in the switchable authorization framework (SACF) was already possible for dedicated PFCG conditions:</p>
<p><code class="ph codeph">ASPECT PFCG_AUTH ( S_OBJECT IN SCENARIO ... )</code></p>
<p>Now, those settings can be used to enable or disable entire condition sets:</p>
<p><code class="ph codeph">GRANT SELECT ON cds_entity WHERE SACF_CHECK_IN_USE (NAME =&gt; NEW_AUTH_SWITCH ) IS INITIAL AND ( element ) = ASPECT PFCG_AUTH( OLD_AUTH, F ) OR SACF_CHECK_IN_USE( NAME =&gt; NEW_AUTH_SWITCH ) IS NOT INITIAL AND ( element ) = ASPECT PFCG_AUTH( NEW_AUTH, F ); </code></p>
<p><a href="abencds_f1_dcl_function.html">More Information</a></p></td>
</tr>
<tr class="odd">
<td><strong>Access Conditions for CDS Hierarchies Based on Elements of the Hierarchy Directory</strong></td>
<td><p>For CDS hierarchies, access control was restricted to the use of conditions not resulting in database filtering. Now elements located in the declared hierarchy directory</p>
<p><a href="abencds_f1_define_hierarchy.html"><code class="ph codeph">DIRECTORY ... FILTER BY</code></a></p>
<p>can be used to formulate such conditions.</p></td>
</tr>
<tr class="even">
<td><strong>New DCL Function</strong></td>
<td>The following new <a href="abencds_f1_dcl_function.html">DCL function</a> is available: <a href="abencds_f1_dcl_function.html"><code class="ph codeph">OPTIONAL_ELEMENT_EXISTS</code></a>.</td>
</tr>
</tbody>
</table>

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
<td><strong>C0 Developer Extensibility for DDIC Objects</strong></td>
<td><p>The following new <a href="abenddicddl_define_ext_annos.html">extensibility annotations</a> are available for <a href="abendictionary_object_glosry.html">dictionary objects</a>. They are required for <a href="abenc0_contract_glosry.html">C0 release</a> of a DDIC object, which is a prerequisite for <a href="abendev_extensibility_glosry.html">developer extensibility</a>.</p>
<ul>
<li><a href="abenddicddl_define_ext_annos.html"><code class="ph codeph">@AbapCatalog.enhancement.fieldSuffix</code></a></li>
<li><a href="abenddicddl_define_ext_annos.html"><code class="ph codeph">@AbapCatalog.enhancement.quotaMaximumFields</code></a></li>
<li><a href="abenddicddl_define_ext_annos.html"><code class="ph codeph">@AbapCatalog.enhancement.quotaMaximumBytes</code></a></li>
<li><a href="abenddicddl_define_ext_annos.html"><code class="ph codeph">@AbapCatalog.enhancement.quotaShareCustomer</code></a></li>
<li><a href="abenddicddl_define_ext_annos.html"><code class="ph codeph">@AbapCatalog.enhancement.quotaSharePartner</code></a></li>
</ul></td>
</tr>
</tbody>
</table>

## Object Component Selector

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Dynamic Target</strong></td>
<td><p>The following syntax can be used for the <a href="abenobject_component_selector.html">object component selector <code class="ph codeph">-&gt;</code></a> to access components and attributes dynamically now:</p>
<p><code class="ph codeph">... { dref-&gt;(comp_name) } | { cref-&gt;(attr_name) } | { iref-&gt;(attr_name) } ...</code></p>
<p>Before, this was possible for <a href="abapassign_dynamic_components.html">dynamic components</a> and <a href="abapassign_mem_area_dynamic_access.html">dynamic access</a> in the statement <code class="ph codeph">ASSIGN</code> only.</p></td>
</tr>
</tbody>
</table>

## Assignments

| Modification                                           | Description                                                                                                                                                                                                                                                  |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **New Parameter for `CL_ABAP_CORRESPONDING=>EXECUTE`** | The method `EXECUTE` of the system class [`CL_ABAP_CORRESPONDING`](../../abap-programming-language/abap-processing-internal-data/abencl_abap_corresponding.md) has a new parameter `KEEPING_LINES`. It has the same effect as the additions `KEEPING TARGET LINES` in `MOVE-CORRESPONDING` or `BASE` in `CORRESPONDING`. |

## Internal Tables

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Access to Generically Typed Internal Tables</strong></td>
<td><p>Earlier, in statements for <a href="abenitab_access.html">accessing internal tables</a>, the internal table had to be known statically. The operand had to be typed at least with <code class="ph codeph">any table</code>.</p>
<p>Now, this restriction is partly removed. In the statements <a href="abapinsert_itab.html"><code class="ph codeph">INSERT</code></a>, <a href="abapappend.html"><code class="ph codeph">APPEND</code></a>, <a href="abapcollect.html"><code class="ph codeph">COLLECT</code></a>, <a href="abapmodify_itab.html"><code class="ph codeph">MODIFY</code></a>, <a href="abapdelete_itab.html"><code class="ph codeph">DELETE</code></a>, <a href="abapread_table.html"><code class="ph codeph">READ</code></a>, <a href="abaploop_at_itab_variants.html"><code class="ph codeph">LOOP</code></a>, and <a href="abapsort_itab.html"><code class="ph codeph">SORT</code></a>, operands can be field symbols and formal parameters that are typed fully generically with <code class="ph codeph">TYPE data</code> or <code class="ph codeph">TYPE any</code>. Such operands can be used as if typed with <code class="ph codeph">any table</code>. If an index access is involved, operands are still required that are typed at least with <code class="ph codeph">TYPE index_table</code>.</p>
<p>This is not yet possible in expressions as <a href="abenfor_itab.html"><code class="ph codeph">FOR expressions</code></a> or <a href="abentable_expressions.html">table expressions</a>.</p>
<p>The following was not possible in older releases.</p>
<p><code class="ph codeph">DATA itab TYPE TABLE OF scarr. FIELD-SYMBOLS &lt;itab&gt; TYPE ANY. ASSIGN itab TO &lt;itab&gt;. LOOP AT &lt;itab&gt; ASSIGNING FIELD-SYMBOL(&lt;fs&gt;). ... ENDLOOP.</code></p></td>
</tr>
</tbody>
</table>

## ABAP RESTful Application Programming Model

In release 7.85, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### ABAP Behavior Pools (ABP)

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ABAP Behavior Pools (ABP)</strong></td>
<td><p>ABAP Behavior Pools (ABP) are now available as part of the ABAP Keyword Documentation. The following topics are covered:</p>
<ul>
<li><a href="abapclass_for_behavior_of.html"><code class="ph codeph">CLASS, FOR BEHAVIOR OF</code></a></li>
<li><p><a href="abenabp_handler_class.html">RAP Handler Class</a></p>
<p><a href="abapmethods_for_rap_behv.html"><code class="ph codeph">METHODS, FOR</code></a></p></li>
<li><p><a href="abenabp_saver_class.html">RAP Saver Class</a></p>
<p><a href="abensaver_finalize.html"><code class="ph codeph">finalize</code></a></p>
<p><a href="abensaver_check_before_save.html"><code class="ph codeph">check_before_save</code></a></p>
<p><a href="abensaver_adjust_numbers.html"><code class="ph codeph">adjust_numbers</code></a></p>
<p><a href="abensaver_method_save.html"><code class="ph codeph">save</code></a></p>
<p><a href="abensaver_method_cleanup.html"><code class="ph codeph">cleanup</code></a></p>
<p><a href="abapsaver_class_cleanup_finalize.html"><code class="ph codeph">cleanup_finalize</code></a></p>
<p><a href="abaprap_saver_meth_save_modified.html"><code class="ph codeph">save_modified</code></a></p></li>
</ul></td>
</tr>
</tbody>
</table>

### RAP BDL

| Modification                                         | Description                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **RAP BO Operation Addition `authorization:update`** | The new [RAP BO operation addition](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_operations_additions.md) [`authorization:update`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_actions_auth_update.md) is available for managed and unmanaged BOs. It delegates the authorization control for an operation to the authorization control that is specified for the update operation. |
| **Abstract BDEF, `with control`**                    | The optional addition [`with control`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_define_beh_abstract.md) is available for abstract BDEFs. It adds a [`%control`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapderived_types_comp.md) structure to the corresponding derived type structure.                                                                                           |
