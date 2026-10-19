---
title: "News for ABAP Release 7.93"
source_file: abennews-793.html
section: "ABAP Release News > News for ABAP Release 7.9x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.93

The kernel release for ABAP release 7.93 is 7.93.

## AMDP

| Modification                             | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **New AMDP Option `CLIENT INDEPENDENT`** | The new addition [`CLIENT INDEPENDENT`](../../abap-programming-language/abap-database-access/abapmethods_amdp_options_client.md) can be used after [`AMDP OPTIONS`](../../abap-programming-language/abap-database-access/abapmethods_amdp_options.md) to declare an [AMDP method](../../abap-glossary/abenamdp_method_glosry.md) as [client-independent](../../abap-glossary/abenclient_independent_glosry.md). When used, only client-independent database objects can be accessed and specified after the addition [`USING`](../../abap-programming-language/abap-database-access/abapmethod_by_db_proc.md). |

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
<td><strong>ADT Documentation Layout</strong></td>
<td><p>From Release 7.93 on, the ABAP Keyword Documentation presents a new layout in <a href="abenadt_glosry.html">ABAP development tools for Eclipse (ADT)</a> where a toggle between <em>Standard ABAP</em> and <em>ABAP Cloud</em> is also available. The new layout includes:</p>
<ul>
<li>New header bar with links to the mail feedback and the web version</li>
<li>Highlighted key blocks for hints, code blocks, and others</li>
<li>Tables with zebra stripes</li>
</ul></td>
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
<td><strong>CDS Scalar Functions</strong></td>
<td><p>The new <a href="abencds_object_glosry.html">CDS object</a> is available: the <a href="abencds_scalar_function_glosry.html">CDS scalar function</a>. It is defined using the <a href="abencds_ddl_glosry.html">CDS DDL</a> statement <a href="abencds_define_scalar_function.html"><code class="ph codeph">DEFINE SCALAR FUNCTION</code></a>.</p>
<p>As of this release, scalar functions are available for two different runtimes:</p>
<ul>
<li>The HANA SQL runtime. <a href="abencds_sql_scalar_glosry.html">SQL-based scalar functions</a> can be created internally at SAP as <a href="abencds_system_func_glosry.html">CDS system functions</a>, or externally by customers and partners as <a href="abencds_user_func_glosry.html">CDS user-defined functions</a>.</li>
<li>The <a href="abenabap_ae_glosry.html">ABAP Analytical Engine</a>. Analytical scalar functions can be created internally at SAP only. They are delivered to customers as <a href="abencds_system_func_glosry.html">CDS system functions</a>.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Extension of the <code class="ph codeph">CAST</code> Matrix</strong></td>
<td><p>The matrix of types that can be converted to each other using <code class="ph codeph">CAST</code> has been enhanced for <a href="abencds_ddic_based_entity_glosry.html">CDS DDIC-based views (obsolete)</a> and for <a href="abencds_v2_view_glosry.html">CDS view entities</a>. Data types <code class="ph codeph">DECFLOAT16</code> and <code class="ph codeph">DECFLOAT34</code> can now be cast into data type <code class="ph codeph">CURR</code>.</p>
<ul>
<li>See topic <a href="abencds_cast_expression_v1.html">CDS DDL - DDIC-Based View, <code class="ph codeph">cast_expr</code></a> and</li>
<li>topic <a href="abencds_cast_expression_v2.html">CDS DDL - CDS View Entity, <code class="ph codeph">cast_expr</code></a></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Release of CDS Enumerated Types</strong></td>
<td><p><a href="abencds_enum_type_glosry.html">CDS enumerated types</a> define <a href="abenenum_type_glosry.html">enumerated types</a> natively in <a href="abenabap_cds_glosry.html">ABAP CDS</a>. The syntax statement for defining a CDS enumerated type is <a href="abencds_define_enum_type.html"><code class="ph codeph">DEFINE TYPE ENUM</code></a>.</p>
<p>CDS enumerated types can be used as follows:</p>
<ul>
<li>In ABAP CDS for typing and casting, as operands in expressions, and in comparisons.</li>
<li>In ABAP for typing after the <code class="ph codeph">TYPES</code> statement.</li>
<li>In ABAP SQL as elementary operands and in cast expressions.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>CDS Transactional Interface, <code class="ph codeph">WHERE</code> Clause</strong></td>
<td>A <a href="abencds_interface_cond_expr.html"><code class="ph codeph">WHERE</code></a> condition is now available also for <a href="abencds_trans_interface_glosry.html">CDS transactional interfaces</a> to restrict the result set that is returned when the transactional interface is accessed.</td>
</tr>
<tr class="odd">
<td><strong><code class="ph codeph">$projection</code> References on Path Expressions</strong></td>
<td>A reuse expression <a href="abencds_reusable_expression_v2.html"><code class="ph codeph">$projection.Field</code></a> can now also be used to reuse fields selected via a <a href="abencds_path_expression_v2.html">path expression</a>.</td>
</tr>
</tbody>
</table>

## Internal Tables

| Modification                                       | Description                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Improved Optimization of the `WHERE` Condition** | The improved [`optimization of the WHERE condition`](../../abap-programming-language/abap-processing-internal-data/abenitab_where_optimization.md) introduced in [`release 7.91`](abennews-791.md) was extended by respecting any [`binary comparison operators`](../../abap-programming-language/abap-program-flow-logic/abenlogexp_any_operand.md) and also [`BETWEEN`](../../abap-programming-language/abap-program-flow-logic/abenlogexp_between.md) for sorted keys. |

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
<td><strong>System Classes for Numbers</strong></td>
<td><p>Two new system classes for numeric calculations are available:</p>
<ul>
<li><a href="abencl_abap_bigint_doc.html"><code class="ph codeph">CL_ABAP_BIGINT</code></a> contains methods for calculations with any size of integer in ABAP.</li>
<li><a href="abencl_abap_rational_doc.html"><code class="ph codeph">CL_ABAP_RATIONAL</code></a> contains methods for calculating with rational numbers without any precision loss.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>New Class <code class="ph codeph">CL_ABAP_DIFF</code></strong></td>
<td>The new class <a href="abencl_abap_diff.html"><code class="ph codeph">CL_ABAP_DIFF</code></a> compares the content of internal tables and returns information about any differences found.</td>
</tr>
<tr class="odd">
<td><strong>New Methods in <code class="ph codeph">CL_ABAP_TSTMP</code></strong></td>
<td>The new methods <code class="ph codeph">MOVE_TRUNC</code>, <code class="ph codeph">MOVE_TO_SHORT_TRUNC</code>, <code class="ph codeph">ADD_TO_SHORT_TRUNC</code> and <code class="ph codeph">SUBTRACTSECS_TO_SHORT_TRUNC</code> of system class <a href="abencl_abap_tstmp.html"><code class="ph codeph">CL_ABAP_TSTMP</code></a> round the fractional seconds of long UTC time stamps down while the existing methods <code class="ph codeph">MOVE</code>, <code class="ph codeph">MOVE_TO_SHORT</code>, <code class="ph codeph">ADD_TO_SHORT</code> and <code class="ph codeph">SUBTRACTSECS_TO_SHORT</code> round commercially. Since the latter might be unexpected, the new methods can be used now in order to preserve the integer part of a long time stamp.</td>
</tr>
<tr class="even">
<td><strong>New Method in <code class="ph codeph">CL_ABAP_BEHV_AUX</code></strong></td>
<td>Using the new method <code class="ph codeph">GET_CURRENT_PHASE</code>, you get information about the current RAP transactional phase.</td>
</tr>
</tbody>
</table>

## ABAP RESTful Application Programming Model

In release 7.93, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

| Modification                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Interface BDEF, `use event`**                        | In [RAP interface behavior definitions](../../abap-glossary/abencds_interface_bdef_glosry.md), [RAP business events](../../abap-glossary/abenrap_entity_event_glosry.md) can be reused using the syntax [`use event`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_use_projection.md).                                                                                                                                                                                                                                                                                                                                                                                           |
| **RAP Derived Events**                                 | [RAP derived events](../../abap-glossary/abenrap_derived_event_glosry.md) allow the reuse of existing [RAP business events](../../abap-glossary/abenrap_entity_event_glosry.md) with a custom payload. RAP derived events are available in managed and unmanaged RAP BOs and in [base BDEF extensions](../../abap-glossary/abenrap_base_bdef_ext_glosry.md). They are defined using the syntax [`managed event`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_managed_event.md).                                                                                                                                                                                                                   |
| **Draft Action Activate Optimized**                    | The optional addition [`optimized`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_draft_action.md) is now available for the [draft action `Activate`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_draft_action.md). SAP recommends always using this addition, since it speeds up the activation of draft instances.                                                                                                                                                                                                                                                                                                                                                            |
| **`with managed instance filter`**                     | The optional addition [`with managed instance filter`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_mngd_instance_check_proj.md) is available for [projection BDEFs](../../abap-glossary/abencds_proj_bdef_glosry.md) and [interface BDEFs](../../abap-glossary/abencds_interface_bdef_glosry.md). If specified, the [`WHERE`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_proj_view_cond_expr.md) condition of the underlying [CDS transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md) or [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) is evaluated when the BDEF is accessed with [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md) or [OData](../../abap-glossary/abenodata_glosry.md) requests from Web clients. |
| **Redefined Parameters, Projection or Interface BDEF** | The input or output parameter of a [RAP action](../../abap-glossary/abenrap_action_glosry.md), [RAP function](../../abap-glossary/abenrap_function_glosry.md), or a [RAP business event](../../abap-glossary/abenrap_entity_event_glosry.md) that is [reused](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_use_projection.md) in a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md) or an [interface BDEF](../../abap-glossary/abencds_interface_bdef_glosry.md) can optionally be replaced with its own projection-specific structure using the syntax additions [`deep parameter`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_redefine_param.md) or [`deep result`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_redefine_param.md).                                                   |
| **Draft Action `AdditionalSave`**                      | A new [draft action](../../abap-glossary/abenrap_bo_draft_action_glosry.md) is available, [`draft action AdditionalSave`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_draft_action.md). This draft action allows users to define a custom saving strategy for draft instances. It is intended in particular for draft actions with a user-defined implementation, defined using the addition [`with additional implementation`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_draft_action.md).                                                                                                                                                                                                   |
