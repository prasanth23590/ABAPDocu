---
title: "News for ABAP Release 9.12"
source_file: abennews-912.html
section: "ABAP Release News > News for ABAP Release 9.1x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 9.12

The kernel release for ABAP release 9.12 is 9.12.

## ABAP Dictionary

| Modification                 | Description                                                                                                                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Empty Key of Table Types** | [Empty table keys](../../abap-programming-language/abap-data-types-and-data-objects/abenitab_empty_key.md) that are available in ABAP language since 7.40, SP02, can now also be defined for [DDIC table types](../../abap-glossary/abenddic_table_type_glosry.md) for [standard tables](../../abap-glossary/abenstandard_table_glosry.md). |

## ABAP CDS Access Control

| Modification                                                                           | Description                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Session Variables and Enumerated Constants on the Right Side of Literal Conditions** | Literal conditions in CDS roles now support session variables and enumerated constants on the right side of the logical expression. For details, see the topic [CDS DCL - `DEFINE ROLE`, `literal_condition`](../../abap-core-data-services-abap-cds/abap-cds-access-control/abencds_f1_cond_literal.md). |

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
<td><strong>CDS Propagated Buffer</strong></td>
<td><p><a href="abencds_buffer_propagation_glosry.html">CDS buffer propagation</a> can be defined for <a href="abencds_v2_view_glosry.html">CDS view entities</a> and <a href="abencds_transactional_pv_glosry.html">CDS transactional queries</a> now:</p>
<ul>
<li>Buffer propagation can be enabled and disabled with the annotation <a href="abencds_1859277801_anno.html"><code class="ph codeph">AbapCatalog.entityBuffer.propagationAllowed: true\|false</code></a></li>
<li>The propagated fields can be specified in a <a href="abencds_prop_buffer_glosry.html">CDS propagated buffer</a> defined by <a href="abencds_propagate_buffer.html"><code class="ph codeph">PROPAGATE VIEW ENTITY BUFFER ON cds_entity ...</code></a></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>CDS Aspects</strong></td>
<td><a href="abencds_aspects.html">CDS aspects</a> can now be used to define reusable elements of CDS entities using the syntax <a href="abencds_define_aspect.html"><code class="ph codeph">DEFINE ASPECT</code></a>. The syntax <a href="abencds_bind_aspect.html"><code class="ph codeph">BIND ASPECT</code></a> binds the aspect to a CDS view entity, and with the syntax <a href="abencds_include_aspect.html"><code class="ph codeph">INCLUDE</code></a>, individual components of the CDS aspect can be included in the select list of the CDS view entity and CDS projection views.</td>
</tr>
<tr class="odd">
<td><strong>CDS External Entities</strong></td>
<td>A new kind of CDS entity is available: the <a href="abencds_external_entity_glosry.html">CDS external entity</a>. CDS external entities can be used to access data from external database systems within the AS ABAP. They are defined using the statement <a href="abencds_define_external_entity.html"><code class="ph codeph">DEFINE EXTERNAL ENTITY</code></a>. The properties of the connection between an external entity and the external system are configured using a <a href="abencds_logical_schema_glosry.html">CDS logical external schema</a>.</td>
</tr>
<tr class="even">
<td><strong>Client Parameter in SQL Functions</strong></td>
<td><p>For the following built-in functions, the session variable <a href="abencds_session_variable_v2.html"><code class="ph codeph">$session.client</code></a> must be passed to the optional formal parameter <code class="ph codeph">client</code> in <a href="abenabap_for_cloud_dev_glosry.html">ABAP for Cloud Development</a>:</p>
<ul>
<li><a href="abencds_conv_func_unit_curr_v2.html"><code class="ph codeph">UNIT_CONVERSION</code></a></li>
<li><a href="abencds_conv_func_unit_curr_v2.html"><code class="ph codeph">CURRENCY_CONVERSION</code></a></li>
<li><a href="abencds_timezone_functions_v2.html"><code class="ph codeph">ABAP_SYSTEM_TIMEZONE</code></a></li>
<li><a href="abencds_timezone_functions_v2.html"><code class="ph codeph">ABAP_USER_TIMEZONE</code></a></li>
<li><a href="abencds_date_time_conversions_v2.html"><code class="ph codeph">TSTMP_TO_DATS</code></a></li>
<li><a href="abencds_date_time_conversions_v2.html"><code class="ph codeph">TSTMP_TO_TIMS</code></a></li>
<li><a href="abencds_date_time_conversions_v2.html"><code class="ph codeph">TSTMP_TO_DST</code></a></li>
<li><p><a href="abencds_date_time_conversions_v2.html"><code class="ph codeph">DATS_TIMS_TO_TSTMP</code></a></p>
<p>The same holds for usage of these functions in <a href="abencds_v1_view_glosry.html">CDS DDIC-based views</a>.</p></li>
</ul></td>
</tr>
</tbody>
</table>

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
<td><strong>Harmonization of Table Expressions and <code class="ph codeph">READ TABLE</code> Statement</strong></td>
<td><p>The <a href="abentable_exp_itab_line.html">variants</a> for specifying a table line in table expressions are now mapped exactly to the respective variants of the <a href="abapread_table.html"><code class="ph codeph">READ TABLE</code></a> statement. The same rules apply and the same syntax warnings can occur. For that, the internal behavior of the variants</p>
<p><a href="abentable_exp_itab_line.html"><code class="ph codeph">[KEY keyname [COMPONENTS]] ...</code></a></p>
<p>was adjusted to match the behavior of the respective <a href="abapread_table_free.html"><code class="ph codeph">READ</code> variants</a> and a new variant</p>
<p><a href="abentable_exp_itab_line.html"><code class="ph codeph">TABLE KEY keyname [COMPONENTS] ...</code></a></p>
<p>was introduced for <a href="abapread_table_key.html"><code class="ph codeph">READ ... WITH TABLE KEY ...</code></a>.</p>
<p>Before, the syntax of the existing variants was not stringently mapped. Despite this adjustment, the behavior of existing programs is not changed. The adjustment offers new possibilities, such as specifying only a part of a table key or specifying additional search fields with a table key. Some new syntax warnings regarding performance might show up and can be either corrected or hidden by a pragma.</p></td>
</tr>
</tbody>
</table>

## ABAP RESTful Application Programming Model

In release 9.12, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### ABAP EML

| Modification                         | Description                                                                                                                                                                                          |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`FORWARDING PRIVILEGED` Addition** | Using the [`FORWARDING PRIVILEGED`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapeml_privileged.md) addition in `READ`, `MODIFY`, and `GET PERMISSIONS` statements, you can pass on the privileged context in subsequent ABAP EML requests. |
| **Modification**                     | ABAP EML [read operations](../../abap-rap-business-objects/abap-for-rap-business-objects/abapread_entity_entities.md) are not allowed in the [RAP late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md).                                                         |
| **ABP Auxiliary Class**              | [ABP auxiliary classes](../../abap-glossary/abenabp_aux_class_glosry.md), which enable extended access rights to a referenced RAP BO, are possible now. Find more information [here](../../abap-rap-business-objects/abap-for-rap-business-objects/abaprap_auxiliary_class.md).    |

### RAP BDL

| Modification                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ABP Auxiliary Class**                                                  | The new statement [`auxiliary class`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_auxiliary_class.md) can be used to specify one or more [ABP auxiliary classes](../../abap-glossary/abenabp_aux_class_glosry.md) that allow the outsourcing of functionality from an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). The primary purpose of an ABP auxiliary class is to allow developers to concurrently implement [RAP behavior](../../abap-glossary/abenrap_behavior_glosry.md).                              |
| **Abstract BDEF, `with hierarchy like entity`**                          | The new addition [`with hierarchy like entity`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_bdef_abstract_header.md) can now be used in the [RAP behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md) of an [abstract behavior definition](../../abap-glossary/abencds_abstract_bdef_glosry.md). It imposes stricter syntax checks to ensure compatibility between the hierarchical BDEF derived type of the abstract BDEF in question and the structured type of the underlying CDS entity. |
| **BDEF Alternative Keys for Managed and Unmanaged Behavior Definitions** | [BDEF pure keys](../../abap-glossary/abenrap_pure_key_glosry.md) and [BDEF secondary keys](../../abap-glossary/abenrap_secondary_key_glosry.md) are now available. They define the signature of a [RAP key function](../../abap-glossary/abenrap_key_function_glosry.md).                                                                                                                                                                                                                              |
| **Explicit Save Order**                                                  | You can explicitly define the save order using [`save after`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_save_after.md).                                                                                                                                                                                                                                                                                                                                                          |
