---
title: "News for ABAP Release 7.86"
source_file: abennews-786.html
section: "ABAP Release News > News for ABAP Release 7.8x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.86

The kernel release for ABAP release 7.86 is 7.86.

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
<td><strong>CDS View Entity, Extended Cast Matrix</strong></td>
<td>In <a href="abencds_v2_view_glosry.html">CDS view entities</a>, <a href="abencds_cast_expression_v2.html">casting</a> from data type <code class="ph codeph">FLTP</code> into data types <code class="ph codeph">DEC</code>, <code class="ph codeph">CURR</code>, <code class="ph codeph">QUAN</code>, <code class="ph codeph">INT1</code>, <code class="ph codeph">INT2</code>, <code class="ph codeph">INT4</code>, <code class="ph codeph">INT8</code>, <code class="ph codeph">DECFLOAT16</code>, and <code class="ph codeph">DECFLOAT34</code> is now possible.</td>
</tr>
<tr class="even">
<td><strong>CDS View Entity, Application Session Variables</strong></td>
<td><p>In <a href="abencds_v2_view_glosry.html">CDS view entities</a>, two new <a href="abencds_session_var_application_v2.html">application session variables</a> are available:</p>
<ul>
<li><a href="abencds_session_var_application_v2.html"><code class="ph codeph">bs_system_id</code></a></li>
<li><a href="abencds_session_var_application_v2.html"><code class="ph codeph">bs_zone_id</code></a></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>CDS Analytical Projection Views</strong></td>
<td><a href="abencds_analytical_query_apv.html">CDS analytical projection views</a> for modelling analytical queries are available. A CDS analytical projection view is defined using <a href="abencds_define_view_as_analytical.html"><code class="ph codeph">DEFINE TRANSIENT VIEW ENTITY AS PROJECTION ON</code></a>. The value for the <a href="abencds_pv_provider_contract.html">provider contract</a> must be set to <code class="ph codeph">ANALYTICAL_QUERY</code>.</td>
</tr>
<tr class="even">
<td><strong>CDS Transactional Interface</strong></td>
<td>A new type of <a href="abencds_projection_view_glosry.html">CDS projection view</a> is available: the <a href="abencds_trans_interface_glosry.html">CDS transactional interface</a>. CDS transactional interfaces serve as stable public interface layer in a CDS data model. They are typically used in the context of the <a href="abenarap_glosry.html">ABAP RESTful Application Programming Model</a> to provide the basis for a <a href="abenrap_bo_interface_glosry.html">RAP BO interface</a>. A CDS transactional interface view is defined using <a href="abencds_define_view_as_interface.html"><code class="ph codeph">DEFINE VIEW ENTITY AS PROJECTION ON</code></a>. The value for the <a href="abencds_pv_provider_contract.html">provider contract</a> must be set to <code class="ph codeph">TRANSACTIONAL_INTERFACE</code>.</td>
</tr>
<tr class="odd">
<td><strong>Support of Input Parameters of Type <code class="ph codeph">abap.string</code></strong></td>
<td><p>Data type <code class="ph codeph">abap.string</code> is now supported for <a href="abencds_f1_param.html">input parameters</a> in the <a href="abencds_parameter_list_v2.html">parameter list</a> of a <a href="abencds_v2_view_glosry.html">CDS view entity</a> and in the <a href="abencds_f1_func_parameter_list.html">parameter list</a> of a <a href="abencds_table_function_glosry.html">CDS table function</a>.</p>
<p>Data type <code class="ph codeph">abap.string</code> is now supported when <a href="abencds_select_parameters_v2.html">binding actual parameters to the input parameters</a> of a CDS view entity, if a CDS table function is used as <a href="abencds_data_source_v2.html">data source</a> after <code class="ph codeph">FROM</code>.</p></td>
</tr>
</tbody>
</table>

## Structure Component Selector

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Dynamic Component</strong></td>
<td><p>The following syntax can be used for the <a href="abenstructure_component_selector.html">structure component selector <code class="ph codeph">-</code></a> to access components dynamically now:</p>
<p><code class="ph codeph">... struct-(comp)</code></p></td>
</tr>
</tbody>
</table>

## ABAP RESTful Application Programming Model

In release 7.86, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

| Modification                                                     | Description                                                                                                                                                          |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **RAP Late Numbering for Managed and for Draft-Enabled RAP BOs** | [RAP late numbering](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_late_numbering.md) is now also available for managed RAP BOs, managed draft-enabled RAP BOs, and for unmanaged draft-enabled RAP BOs. |
| **Instance-Bound Factory Actions for Managed RAP BOs**           | [Instance-bound factory actions](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_action_factory.md) are now also available for managed RAP BOs.                                                            |
| **BDEF Privileged Mode for RAP Projection BOs**                  | A new syntax variant of [`with privileged mode`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_privileged_mode.md) is now available for RAP projection BOs.                                              |
