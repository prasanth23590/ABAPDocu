---
title: "RAP BDL - Feature Tables"
source_file: abenrap_feature_table.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP BDL - Syntax"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP BDL - Feature Tables

The following sections shows all available language elements of the [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) and their release dates.

- [BDL](abenrap_feature_table.md#bdl)

  - [RAP Behavior Definitions](abenrap_feature_table.md#rap-behavior-definitions)

  - [BDEF Extensions](abenrap_feature_table.md#bdef-extensions)

## BDL

### RAP Behavior Definitions

**RAP Behavior Definition Header**

The following tables list the keywords that can be used in BDEFs of type managed, unmanaged, and projection. If the release dates differ per implementation type, the release dates are given per implementation type.

<table>
<thead>
<tr class="header">
<th><strong>Language Element</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>ABAP Release, quarterly</strong></th>
<th><strong>ABAP Release, on-premise</strong></th>
<th><a href="abensap_btp_abap_env_glosry.html"><strong>SAP BTP ABAP environment</strong></a></th>
<th><a href="abensap_s4hana_cpub_glosry.html"><strong>SAP S/4HANA Cloud Public Edition</strong></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abenbdl_impl_type.html"><code class="ph codeph">managed</code></a></td>
<td>Defines a <a href="abenmanaged_rap_bo_glosry.html">managed RAP BO</a>.</td>
<td>7.77</td>
<td>7.54</td>
<td>1905</td>
<td>1905</td>
</tr>
<tr class="even">
<td><a href="abenbdl_impl_type.html"><code class="ph codeph">unmanaged</code></a></td>
<td>Defines an <a href="abenunmanaged_rap_bo_glosry.html">unmanaged RAP BO</a>.</td>
<td>7.73</td>
<td>7.53</td>
<td>1805</td>
<td>1805</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">managed by BOPF</code></td>
<td>Defines a <a href="abenrap_bopf_bo_glosry.html">BOPF-based RAP BO</a>.</td>
<td>-</td>
<td>7.58</td>
<td>-</td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="abenbdl_impl_type.html"><code class="ph codeph">projection</code></a></td>
<td>Defines a projection RAP BO.</td>
<td>7.77</td>
<td>7.54</td>
<td>1905</td>
<td>1905</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_in_class_unique.html"><code class="ph codeph">implementation in class [unique]</code></a></td>
<td>Class for manual method implementation.</td>
<td>7.77</td>
<td>7.54</td>
<td>1905</td>
<td>1905</td>
</tr>
<tr class="even">
<td><a href="abenbdl_strict_1.html"><code class="ph codeph">strict</code></a></td>
<td>Enables <a href="abenrap_strict_mode_glosry.html">BDEF strict mode</a>.</td>
<td>7.84</td>
<td>7.56</td>
<td>2105</td>
<td>2105</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_strict_2.html"><code class="ph codeph">strict(2)</code></a></td>
<td>Enables <a href="abenrap_strict_mode_glosry.html">BDEF strict mode, version 2</a>.</td>
<td>7.89</td>
<td>7.57</td>
<td>2208</td>
<td>2208</td>
</tr>
<tr class="even">
<td><a href="abenbdl_auxiliary_class.html"><code class="ph codeph">auxiliary class</code></a></td>
<td>Specifies one or more <a href="abenabp_aux_class_glosry.html">ABP auxiliary classes</a> that allow the outsourcing of functionality from an <a href="abenbehavior_pool_glosry.html">ABAP behavior pool</a>.</td>
<td>9.12</td>
<td>8.16</td>
<td>2408</td>
<td>2408</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_extensible.html"><code class="ph codeph">extensible</code></a></td>
<td><a href="abenrap_ext_enablement_glosry.html">RAP extensibility enablement</a> for managed and unmanaged RAP BOs and for projection BDEFs.</td>
<td>7.89</td>
<td>7.57</td>
<td>2208</td>
<td>2208</td>
</tr>
<tr class="even">
<td><a href="abenbdl_extensible.html"><code class="ph codeph">with validations on save \lbr with determinations on save \lbr with determinations on modify \lbr with additional save \lbr (extensible)</code></a></td>
<td><p><a href="abenrap_ext_enablement_glosry.html">RAP extensibility enablement</a>.</p>
<p>Currently only available for managed RAP BOs.</p></td>
<td>7.89</td>
<td>7.57</td>
<td>2208</td>
<td>2208</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_mngd_instance_check_proj.html"><code class="ph codeph">with managed instance filter</code></a></td>
<td>Optional addition for <a href="abencds_proj_bdef_glosry.html">projection BDEFs</a> and <a href="abencds_interface_bdef_glosry.html">interface BDEFs</a>. If specified, the <a href="abencds_proj_view_cond_expr.html"><code class="ph codeph">WHERE</code></a> condition of the underlying <a href="abencds_transactional_pv_glosry.html">CDS transactional query</a> or <a href="abencds_trans_interface_glosry.html">CDS transactional interface</a> is evaluated when the BDEF is accessed with <a href="abenabap_eml_glosry.html">ABAP EML</a> or <a href="abenodata_glosry.html">OData</a> requests from Web clients.</td>
<td>7.93</td>
<td>7.58</td>
<td>2308</td>
<td>2308</td>
</tr>
<tr class="even">
<td><a href="abenbdl_with_draft.html"><code class="ph codeph">with draft</code></a></td>
<td>Enables <a href="abenrap_exclusive_draft_glosry.html">RAP exclusive draft</a>.</td>
<td>7.81</td>
<td>7.55</td>
<td>2008</td>
<td>2008</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_with_coll_draft.html"><code class="ph codeph">with collaborative draft</code></a></td>
<td>Enables <a href="abenrap_collaborative_draft_glosry.html">RAP collaborative draft</a>.</td>
<td>9.16</td>
<td>8.16</td>
<td>2508</td>
<td>2508</td>
</tr>
<tr class="even">
<td><code class="ph codeph">with BOPF draft</code></td>
<td>Enables draft handling in a <a href="abenrap_bopf_bo_glosry.html">BOPF-based RAP BO</a>.</td>
<td>-</td>
<td>7.58</td>
<td>-</td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_use_projection.html"><code class="ph codeph">use draft</code></a></td>
<td>Reuse of <a href="abenrap_draft_handling_glosry.html">RAP draft handling</a> in a <a href="abencds_proj_bdef_glosry.html">CDS projection BDEF</a>.</td>
<td>7.77</td>
<td>7.54</td>
<td>1909</td>
<td>1909</td>
</tr>
<tr class="even">
<td><a href="abenbdl_use_projection.html"><code class="ph codeph">use draft as dependent</code></a></td>
<td>Used in <a href="abencds_proj_bdef_glosry.html">projection BDEFs</a> within cross-BO scenarios to enable <a href="abendraft_scope_glosry.html">draft scope</a> functionality. Turns the respective BO into a <a href="abenrap_dependent_draft_bo_glosry.html">dependent draft BO</a>.</td>
<td>9.16</td>
<td>8.16</td>
<td>2508</td>
<td>2508</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_use_projection.html"><code class="ph codeph">use side effects</code></a></td>
<td>Reuse of <a href="abenrap_side_effects_glosry.html">RAP side effects</a> in a <a href="abencds_proj_bdef_glosry.html">CDS projection BDEF</a>.</td>
<td>7.91</td>
<td>7.58</td>
<td>2302</td>
<td>2302</td>
</tr>
<tr class="even">
<td><a href="abenbdl_privileged_mode.html"><code class="ph codeph">with privileged mode</code></a></td>
<td>Enables <a href="abenrap_privileged_mode_glosry.html">BDEF privileged mode</a>.</td>
<td><p>7.83.</p>
<p>Obsolete as of 7.89</p></td>
<td><p>7.56</p>
<p>Obsolete as of 7.57</p></td>
<td>2102. Obsolete as of 2208.</td>
<td>2102. Obsolete as of 2208.</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_privileged_mode.html"><code class="ph codeph">with privileged mode disabling</code></a></td>
<td>Enables <a href="abenrap_privileged_mode_glosry.html">BDEF privileged mode</a> for managed and unmanaged RAP BOs.</td>
<td>7.89</td>
<td>7.56</td>
<td>2208</td>
<td>2208</td>
</tr>
<tr class="even">
<td><a href="abenbdl_privileged_mode.html"><code class="ph codeph">with privileged mode disabling base context [and]</code></a></td>
<td>Enables <a href="abenrap_privileged_mode_glosry.html">BDEF privileged mode</a> in projection BDEFs.</td>
<td>7.86</td>
<td>7.57</td>
<td>2111</td>
<td>2111</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_foreign.html"><code class="ph codeph">foreign entity</code></a></td>
<td>Defines an entity which is not part of the BO structure as component for the response structures, thus enabling message mapping for other BOs.</td>
<td><p>Unmanaged RAP BO: 7.73</p>
<p>Managed RAP BO: 7.77</p>
<p>Service Projection: 7.77</p></td>
<td><p>Unmanaged RAP BO: 7.53</p>
<p>Managed RAP BO: 7.54</p>
<p>Projection BDEF: 7.54</p></td>
<td><p>Unmanaged: 1808</p>
<p>Managed: 1908</p>
<p>Projection: 1908</p></td>
<td><p>Unmanaged: 1808</p>
<p>Managed: 1908</p>
<p>Projection: 1908</p></td>
</tr>
<tr class="even">
<td><a href="abenbdl_save_after.html"><code class="ph codeph">save after</code></a></td>
<td>Explicitly sets the save order</td>
<td>9.12</td>
<td>8.16</td>
<td>2408</td>
<td>2408</td>
</tr>
</tbody>
</table>

**Entity Behavior Definition**

<table>
<thead>
<tr class="header">
<th><strong>Language Element</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>ABAP Release, quarterly</strong></th>
<th><strong>ABAP Release, on-premise</strong></th>
<th><a href="abensap_btp_abap_env_glosry.html"><strong>SAP BTP ABAP environment</strong></a></th>
<th><a href="abensap_s4hana_cpub_glosry.html"><strong>SAP S/4HANA Cloud Public Edition</strong></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abenbdl_define_beh.html"><code class="ph codeph">define behavior for...alias</code></a></td>
<td>Defines an <a href="abencds_entity_bdef_glosry.html">entity behavior definition</a>.</td>
<td><p>Unmanaged RAP BO: 7.73</p>
<p>Managed RAP BO: 7.77</p>
<p>Service Projection: 7.77</p></td>
<td><p>Unmanaged: 7.53</p>
<p>Managed: 7.54</p>
<p>Projection: 7.54</p></td>
<td><p>Unmanaged: 1808</p>
<p>Managed: 1908</p>
<p>Projection: 1908</p></td>
<td><p>Unmanaged: 1808</p>
<p>Managed: 1908</p>
<p>Projection: 1908</p></td>
</tr>
</tbody>
</table>

**Authorization Context Definition**

| **Language Element**                                                                                                                  | **Meaning**                                                                                                                                                                                                                                                                                                                                                               | **ABAP Release, quarterly** | **ABAP Release, on-premise** | [**SAP BTP ABAP environment**](../../abap-glossary/abensap_btp_abap_env_glosry.md) | [**SAP S/4HANA Cloud Public Edition**](../../abap-glossary/abensap_s4hana_cpub_glosry.md) |
|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------|------------------------------------------------------------------|-------------------------------------------------------------------------|
| [`define authorization context ... \lbr [for disable {modify\|read\|modify,read}]`](abenbdl_def_auth_context.md)                    | Defines an [authorization context](../../abap-glossary/abencds_auth_context_glosry.md) that lists [authorization objects](../../abap-glossary/abenauthorization_object_glosry.md) that can be skipped when the respective authorization context is activated.                                                                                                                                                 | 7.85                        | 7.56                         | 2108                                                             | 2108                                                                    |
| [`save:early`, `save:late`](abenbdl_def_auth_context.md), [authorization context for disable](../../abap-glossary/abencds_auth_context_glosry.md)     | The options [`save:early`](abenbdl_def_auth_context.md) and [`save:late`](abenbdl_def_auth_context.md) can be specified after [`define authorization context ContextName for disable`](abenbdl_def_auth_context.md) to skip [authorization objects](../../abap-glossary/abenauthorization_object_glosry.md) during certain [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md).     | 7.91                        | 7.58                         | 2302                                                             | 2302                                                                    |
| [`determination`, `validation`](abenbdl_def_auth_context.md), [authorization context for disable](../../abap-glossary/abencds_auth_context_glosry.md) | The options [`determination`](abenbdl_def_auth_context.md) and [`validation`](abenbdl_def_auth_context.md) can be specified after [`define authorization context ContextName for disable`](abenbdl_def_auth_context.md) to skip [authorization objects](../../abap-glossary/abenauthorization_object_glosry.md) during certain [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md). | 9.16                        | 8.16                         | 2508                                                             | 2508                                                                    |
| [`define own authorization context`](abenbdl_def_own_auth_context.md)                                                               | Defines an [own authorization context](../../abap-glossary/abencds_own_ac_glosry.md) that documents authorization objects used in the implementation of the RAP BO in question.                                                                                                                                                                                                             | 7.86                        | 7.57                         | 2111                                                             | 2111                                                                    |
| [`define own authorization context by privileged mode [and]{...}`](abenbdl_def_own_auth_context.md)                                 | Defines an [own authorization context](../../abap-glossary/abencds_own_ac_glosry.md)                                                                                                                                                                                                                                                                                                        | 7.89                        | 7.56                         | 2208                                                             | 2208                                                                    |

**Entity Behavior Characteristics**

<table>
<thead>
<tr class="header">
<th><strong>Language Element</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>ABAP Release, quarterly</strong></th>
<th><strong>ABAP Release, on-premise</strong></th>
<th><a href="abensap_btp_abap_env_glosry.html"><strong>SAP BTP ABAP environment</strong></a></th>
<th><a href="abensap_s4hana_cpub_glosry.html"><strong>SAP S/4HANA Cloud Public Edition</strong></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abenbdl_persistent_table.html"><code class="ph codeph">persistent table</code></a></td>
<td>Defines a persistent database table in a managed RAP BO.</td>
<td>7.77</td>
<td>7.54</td>
<td>1908</td>
<td>1908</td>
</tr>
<tr class="even">
<td><a href="abenbdl_draft_table.html"><code class="ph codeph">draft table</code></a></td>
<td>Defines the <a href="abendraft_table_glosry.html">draft database table</a> used to store draft data.</td>
<td>7.81</td>
<td>7.55</td>
<td>2008</td>
<td>2008</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_draft_query_view.html"><code class="ph codeph">query</code></a></td>
<td>Defines a <a href="abendraft_query_view_glosry.html">draft query view</a> for a draft database table.</td>
<td>7.89</td>
<td>7.57</td>
<td>2208</td>
<td>2208</td>
</tr>
<tr class="even">
<td><a href="abenbdl_saving.html"><code class="ph codeph">with additional save</code></a></td>
<td>User-defined saving strategy for managed RAP BOs.</td>
<td>7.78</td>
<td>7.55</td>
<td>1911</td>
<td>1911</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_saving.html"><code class="ph codeph">with unmanaged save</code></a></td>
<td>User-defined saving strategy for managed RAP BOs.</td>
<td>7.78</td>
<td>7.55</td>
<td>1911</td>
<td>1911</td>
</tr>
<tr class="even">
<td><a href="abenbdl_saving.html"><code class="ph codeph">and cleanup</code></a></td>
<td>User-defined saving strategy for managed RAP BOs.</td>
<td>7.83</td>
<td>7.56</td>
<td>2102</td>
<td>2102</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_saving.html"><code class="ph codeph">with full data</code></a></td>
<td>User-defined saving strategy for managed RAP BOs.</td>
<td>7.88</td>
<td>7.57</td>
<td>2205</td>
<td>2205</td>
</tr>
<tr class="even">
<td><a href="abenbdl_etag.html"><code class="ph codeph">etag master</code></a>, <a href="abenbdl_etag.html"><code class="ph codeph">etag dependent</code></a>, <a href="abenbdl_etag.html"><code class="ph codeph">total etag</code></a></td>
<td>Defines an ETag field for optimistic concurrency control.</td>
<td><p>Unmanaged RAP BO: 7.73</p>
<p>Managed RAP BO: 7.77</p>
<p>Service Projection: 7.77</p></td>
<td><p>Unmanaged: 7.53</p>
<p>Managed: 7.54</p>
<p>Projection:7.54</p></td>
<td><p>Unmanaged: 1808</p>
<p>Managed: 1908</p>
<p>Projection: 1908</p></td>
<td><p>Unmanaged: 1808</p>
<p>Managed: 1908</p>
<p>Projection: 1908</p></td>
</tr>
<tr class="odd">
<td><a href="abenbdl_use_projection.html"><code class="ph codeph">use etag</code></a></td>
<td>Reuse of ETag fields for optimistic concurrency control in a <a href="abencds_proj_bdef_glosry.html">CDS projection BDEF</a>.</td>
<td>7.77</td>
<td>7.54</td>
<td>1908</td>
<td>1908</td>
</tr>
<tr class="even">
<td><a href="abenbdl_locking.html"><code class="ph codeph">lock master</code></a></td>
<td>Defines pessimistic concurrency control in managed or unmanaged RAP BOs.</td>
<td><p>Unmanaged RAP BO: 7.73</p>
<p>Managed RAP BO: 7.77</p></td>
<td><p>Unmanaged RAP BO: 7.53</p>
<p>Managed RAP BO: 7.54</p></td>
<td><p>Unmanaged: 1808</p>
<p>Managed: 1908</p></td>
<td><p>Unmanaged: 1808</p>
<p>Managed: 1908</p></td>
</tr>
<tr class="odd">
<td><a href="abenbdl_locking.html"><code class="ph codeph">unmanaged (lock master)</code></a></td>
<td>Implementation exit for pessimistic concurrency control in managed RAP BOs.</td>
<td>7.80</td>
<td>7.55</td>
<td>2005</td>
<td>2005</td>
</tr>
<tr class="even">
<td><a href="abenbdl_locking.html"><code class="ph codeph">lock dependent</code></a></td>
<td>Defines pessimistic concurrency control in managed or unmanaged RAP BOs.</td>
<td><p>Unmanaged RAP BO: 7.73</p>
<p>Managed RAP BO: 7.77</p></td>
<td><p>Unmanaged RAP BO: 7.53</p>
<p>Managed RAP BO: 7.54</p></td>
<td><p>Unmanaged: 1808</p>
<p>Managed: 1908</p></td>
<td><p>Unmanaged: 1808</p>
<p>Managed: 1908</p></td>
</tr>
<tr class="odd">
<td><a href="abenbdl_lock_none.html"><code class="ph codeph">lock:none</code></a></td>
<td>RAP BO operation addition that prevents the locking mechanism for a certain RAP BO entity.</td>
<td>7.82</td>
<td>7.56</td>
<td>2011</td>
<td>2011</td>
</tr>
<tr class="even">
<td><a href="abenbdl_authorization.html"><code class="ph codeph">authorization master( global )</code></a></td>
<td>Defines global <a href="abenrap_auth_control_glosry.html">RAP authorization control</a> for managed and unmanaged RAP BOs.</td>
<td>7.82</td>
<td>7.56</td>
<td>2011</td>
<td>2011</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_authorization.html"><code class="ph codeph">authorization master ( instance )</code></a></td>
<td>Defines instance <a href="abenrap_auth_control_glosry.html">RAP authorization control</a> for managed and unmanaged RAP BOs.</td>
<td>7.77</td>
<td>7.54</td>
<td>1908</td>
<td>1908</td>
</tr>
<tr class="even">
<td><a href="abenbdl_authorization.html"><code class="ph codeph">authorization dependent</code></a></td>
<td><a href="abenrap_auth_control_glosry.html">RAP authorization control</a> for managed and unmanaged RAP BOs.</td>
<td>7.77</td>
<td>7.54</td>
<td>1908</td>
<td>1908</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_authorization_projection.html"><code class="ph codeph">authorization ( global ) \lbr \| ( instance ) \lbr \| ( global, instance )</code></a></td>
<td>Defines <a href="abenrap_auth_control_glosry.html">RAP authorization control</a> for projection BDEFs.</td>
<td>7.84</td>
<td>7.56</td>
<td>2105</td>
<td>2105</td>
</tr>
<tr class="even">
<td><a href="abenbdl_authorization.html"><code class="ph codeph">authorization:update</code></a></td>
<td><a href="abenbdl_operations_additions.html">RAP BO operation addition</a> to delegate <a href="abenrap_auth_control_glosry.html">RAP authorization control</a>.</td>
<td>7.85</td>
<td>7.56</td>
<td>2108</td>
<td>2108</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_authorization.html"><code class="ph codeph">authorization:none</code></a></td>
<td><a href="abenbdl_operations_additions.html">RAP BO operation addition</a> to exclude a RAP BO operation from <a href="abenrap_auth_control_glosry.html">RAP authorization control</a>.</td>
<td>7.77</td>
<td>7.54</td>
<td>1908</td>
<td>1908</td>
</tr>
<tr class="even">
<td><a href="abenbdl_actions_auth_global.html"><code class="ph codeph">authorization:global</code></a></td>
<td><a href="abenbdl_operations_additions.html">RAP BO operation addition</a> that replaces the <a href="abenrap_auth_control_glosry.html">RAP authorization control</a> that is specified in the <a href="abenrap_auth_ma_ent_glosry.html">authorization master entity</a> and applies global authorization checks instead.</td>
<td>7.92</td>
<td>7.58</td>
<td>2305</td>
<td>2308</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_actions_auth_instance.html"><code class="ph codeph">authorization:instance</code></a></td>
<td><a href="abenbdl_operations_additions.html">RAP BO operation addition</a> that replaces the <a href="abenrap_auth_control_glosry.html">RAP authorization control</a> that is specified in the <a href="abenrap_auth_ma_ent_glosry.html">authorization master entity</a> and applies instance authorization checks instead.</td>
<td>7.92</td>
<td>7.58</td>
<td>2305</td>
<td>2308</td>
</tr>
<tr class="even">
<td><a href="abenbdl_change_documents.html"><code class="ph codeph">changedocuments master</code></a></td>
<td>Enables logging of changes using a change document object.</td>
<td>9.16</td>
<td>7.58</td>
<td>2508</td>
<td>2508</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_change_documents.html"><code class="ph codeph">asynchronous</code></a>, RAP change documents</td>
<td>Option to enable asynchronous writing of a change log.</td>
<td>9.16</td>
<td>8.16</td>
<td>2508</td>
<td>2508</td>
</tr>
<tr class="even">
<td><a href="abenbdl_change_documents.html"><code class="ph codeph">utc</code></a>, RAP change documents</td>
<td>Defines that the time data for change documents is recorded in UTC format.</td>
<td>9.16</td>
<td>8.16</td>
<td>2508</td>
<td>2508</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_change_documents.html"><code class="ph codeph">for persistent tables</code></a>, RAP change documents</td>
<td>Defines that the field information of the RAP persistent tables is evaluated for change logging. Not available in ABAP Cloud.</td>
<td>not available</td>
<td>8.16</td>
<td>not available</td>
<td>not available</td>
</tr>
<tr class="even">
<td><a href="abenbdl_change_documents.html"><code class="ph codeph">changedocuments dependent</code></a></td>
<td>Enables a RAP BO entity for change logging.</td>
<td>9.16</td>
<td>7.58</td>
<td>2508</td>
<td>2508</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_instance_hierarchy.html"><code class="ph codeph">instance hierarchy</code></a></td>
<td>Enables the editable treeview scenario for a managed or unmanaged RAP BO.</td>
<td>9.14</td>
<td>8.16</td>
<td>2502</td>
<td>2502</td>
</tr>
<tr class="even">
<td><a href="abenbdl_copy_action.html"><code class="ph codeph">copy action</code></a></td>
<td>Defines a <a href="abenrap_copy_action_glosry.html">RAP copy action</a>.</td>
<td>9.16</td>
<td>8.16</td>
<td>2508</td>
<td>2508</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_reorder_action.html"><code class="ph codeph">field ( hierarchy-index )</code></a></td>
<td>Specifies a hierarchy index field for a managed <a href="abenrap_reorder_action_glosry.html">reorder action</a>.</td>
<td>9.14</td>
<td>7.58</td>
<td>2502</td>
<td>2502</td>
</tr>
<tr class="even">
<td><a href="abenbdl_reorder_action.html"><code class="ph codeph">ascending association</code></a></td>
<td>Specifies an ascending association for a managed <a href="abenrap_reorder_action_glosry.html">reorder action</a>.</td>
<td>9.14</td>
<td>7.58</td>
<td>2502</td>
<td>2502</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_reorder_action.html"><code class="ph codeph">descending association ... [with cascading delete]</code></a></td>
<td>Specifies a descending association for a managed <a href="abenrap_reorder_action_glosry.html">reorder action</a>.</td>
<td>9.14</td>
<td>7.58</td>
<td>2502</td>
<td>2502</td>
</tr>
<tr class="even">
<td><a href="abenbdl_reorder_action.html"><code class="ph codeph">reorder action</code></a></td>
<td>Defines a <a href="abenrap_reorder_action_glosry.html">RAP reorder action</a>. <a href="abenrap_reorder_action_glosry.html">reorder action</a>.</td>
<td>9.14</td>
<td>7.58</td>
<td>2502</td>
<td>2502</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_early_numb.html"><code class="ph codeph">early numbering</code></a></td>
<td>Defines unmanaged <a href="abenrap_early_numbering_glosry.html">early numbering</a> for all primary key fields of a business object entity.</td>
<td>7.83</td>
<td>7.56</td>
<td>2102</td>
<td>2102</td>
</tr>
<tr class="even">
<td><a href="abenbdl_late_numbering.html"><code class="ph codeph">late numbering</code></a></td>
<td>Enables gapless assignment for unique keys when creating new entity instances in managed and unmanaged RAP BOs.</td>
<td><p>Unmanaged RAP BO without draft: 7.73</p>
<p>Unmanaged RAP BO with draft and Managed RAP BO: 7.86</p></td>
<td><p>Unmanaged RAP BO without draft: 7.53</p>
<p>Unmanaged RAP BO with draft and Managed RAP BO: 7.57</p></td>
<td><p>Unmanaged RAP BO without draft: 1805</p>
<p>Unmanaged RAP BO with draft and Managed RAP BO: 2111</p></td>
<td><p>Unmanaged RAP BO without draft: 1805</p>
<p>Unmanaged RAP BO with draft and Managed RAP BO: 2111</p></td>
</tr>
</tbody>
</table>

**Entity Behavior Body**

<table>
<thead>
<tr class="header">
<th><strong>Language Element</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>ABAP Release, quarterly</strong></th>
<th><strong>ABAP Release, on-premise</strong></th>
<th><a href="abensap_btp_abap_env_glosry.html"><strong>SAP BTP ABAP environment</strong></a></th>
<th><a href="abensap_s4hana_cpub_glosry.html"><strong>SAP S/4HANA Cloud Public Edition</strong></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abenbdl_field_char.html"><code class="ph codeph">field(readonly)</code></a></td>
<td>Defines a <a href="abenrap_field_char_glosry.html">RAP field characteristic</a>.</td>
<td><p>Unmanaged RAP BO: 7.76</p>
<p>Managed RAP BO: 7.77</p></td>
<td><p>Unmanaged RAP BO: 7.54</p>
<p>Managed RAP BO: 7.54</p></td>
<td><p>Unmanaged: 1905</p>
<p>Managed: 1908</p></td>
<td><p>Unmanaged: 1905</p>
<p>Managed: 1908</p></td>
</tr>
<tr class="even">
<td><a href="abenbdl_field_char.html"><code class="ph codeph">field(mandatory)</code></a></td>
<td>Defines a <a href="abenrap_field_char_glosry.html">RAP field characteristic</a>.</td>
<td><p>Unmanaged RAP BO: 7.76</p>
<p>Managed RAP BO: 7.77</p></td>
<td><p>Unmanaged RAP BO: 7.54</p>
<p>Managed RAP BO: 7.54</p></td>
<td><p>Unmanaged: 1905</p>
<p>Managed: 1908</p></td>
<td><p>Unmanaged: 1905</p>
<p>Managed: 1908</p></td>
</tr>
<tr class="odd">
<td><a href="abenbdl_field_char.html"><code class="ph codeph">field (features:instance)</code></a></td>
<td>Defines a <a href="abenrap_field_char_glosry.html">RAP field characteristic</a>.</td>
<td>7.77</td>
<td>7.54</td>
<td>1908</td>
<td>1908</td>
</tr>
<tr class="even">
<td><a href="abenbdl_field_char.html"><code class="ph codeph">field (mandatory:create)</code></a></td>
<td>Defines a <a href="abenrap_field_char_glosry.html">RAP field characteristic</a>.</td>
<td>7.81</td>
<td>7.55</td>
<td>2008</td>
<td>2008</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_field_char.html"><code class="ph codeph">field (readonly:update)</code></a></td>
<td>Defines a <a href="abenrap_field_char_glosry.html">RAP field characteristic</a>.</td>
<td>7.81</td>
<td>7.55</td>
<td>2008</td>
<td>2008</td>
</tr>
<tr class="even">
<td><a href="abenbdl_field_char.html"><code class="ph codeph">field (numbering:managed)</code></a></td>
<td>Defines managed internal numbering for a field in a managed RAP BO.</td>
<td>7.79</td>
<td>7.55</td>
<td>2002</td>
<td>2002</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_field_char.html"><code class="ph codeph">field (suppress)</code></a></td>
<td>Defines a <a href="abenrap_field_char_glosry.html">RAP field characteristic</a>.</td>
<td><p>Managed RAP BO: 7.88</p>
<p>Unmanaged RAP BO: 7.87</p>
<p>Service Projection: 7.84</p></td>
<td><p>Managed: 7.57</p>
<p>Unmanaged: 7.57</p>
<p>Projection: 7.56</p></td>
<td><p>Managed: 2205</p>
<p>Unmanaged: 2202</p>
<p>Projection: 2105</p></td>
<td><p>Managed: 2205</p>
<p>Unmanaged: 2202</p>
<p>Projection: 2105</p></td>
</tr>
<tr class="even">
<td><a href="abenbdl_field_char.html"><code class="ph codeph">field (notrigger:warn)</code></a></td>
<td>Defines a <a href="abenrap_field_char_glosry.html">RAP field characteristic</a>.</td>
<td>7.90</td>
<td>7.58</td>
<td>2211</td>
<td>2211</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_augment_projection.html"><code class="ph codeph">field (modify)</code></a></td>
<td>Augmentation of a <a href="abencds_virtual_element_glosry.html">CDS virtual element</a> in a <a href="abencds_proj_bdef_glosry.html">CDS projection BDEF</a>.</td>
<td>7.82</td>
<td>7.56</td>
<td>2011</td>
<td>2011</td>
</tr>
<tr class="even">
<td><a href="abenbdl_grouping.html"><code class="ph codeph">group</code></a></td>
<td>Splits the implementation-relevant parts of a business object's logic into multiple groups to allow simultaneous work.</td>
<td>7.78</td>
<td>7.55</td>
<td>1911</td>
<td>1911</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_standard_operations.html"><code class="ph codeph">create</code></a>, <a href="abenbdl_standard_operations.html"><code class="ph codeph">update</code></a>, <a href="abenbdl_standard_operations.html"><code class="ph codeph">delete</code></a></td>
<td>Enables <a href="abencrud_glosry.html">CRUD operations</a> for a managed or unmanaged RAP business object.</td>
<td><p>Unmanaged RAP BO: 7.73</p>
<p>Managed RAP BO: 7.77</p></td>
<td><p>Unmanaged: 7.53</p>
<p>Managed: 7.54</p></td>
<td><p>Unmanaged: 1805</p>
<p>Managed: 1905</p></td>
<td><p>Unmanaged: 1805</p>
<p>Managed: 1905</p></td>
</tr>
<tr class="even">
<td><a href="abenbdl_use_projection.html"><code class="ph codeph">use</code></a></td>
<td>Reuse of <a href="abenrap_bo_operation_glosry.html">RAP BO operations</a> in a <a href="abencds_proj_bdef_glosry.html">CDS projection BDEF</a>.</td>
<td>7.81</td>
<td>7.55</td>
<td>2008</td>
<td>2008</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_association.html"><code class="ph codeph">association ... abbreviation ... [without response]</code></a></td>
<td>Enables read-by-association and create-by-association operations for associations.</td>
<td><p>Unmanaged RAP BO: 7.73</p>
<p>Managed RAP BO: 7.77</p></td>
<td><p>Unmanaged: 7.53</p>
<p>Managed: 7.54</p></td>
<td><p>Unmanaged: 1805</p>
<p>Managed: 1905</p></td>
<td><p>Unmanaged: 1805</p>
<p>Managed: 1905</p></td>
</tr>
<tr class="even">
<td><a href="abenbdl_action.html"><code class="ph codeph">action ... [external]</code></a></td>
<td>Defines a <a href="abenrap_action_glosry.html">RAP action</a>.</td>
<td><p>Unmanaged RAP BO: 7.73</p>
<p>Managed RAP BO: 7.77</p></td>
<td><p>Unmanaged: 7.53</p>
<p>Managed: 7.54</p></td>
<td><p>Unmanaged: 1805</p>
<p>Managed: 1905</p></td>
<td><p>Unmanaged: 1805</p>
<p>Managed: 1905</p></td>
</tr>
<tr class="odd">
<td><a href="abenbdl_action.html"><code class="ph codeph">static (action)</code></a></td>
<td>Defines a static <a href="abenrap_action_glosry.html">RAP action</a>.</td>
<td><p>Unmanaged RAP BO: 7.73</p>
<p>Managed RAP BO: 7.77</p></td>
<td><p>Unmanaged: 7.53</p>
<p>Managed: 7.54</p></td>
<td><p>Unmanaged: 1805</p>
<p>Managed: 1905</p></td>
<td><p>Unmanaged: 1805</p>
<p>Managed: 1905</p></td>
</tr>
<tr class="even">
<td><a href="abenbdl_action_repeatable.html"><code class="ph codeph">repeatable (action or function)</code></a></td>
<td>Defines a <a href="abenrap_repeatable_action_glosry.html">RAP repeatable operation</a>.</td>
<td>7.89</td>
<td>7.57</td>
<td>2208</td>
<td>2208</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_action_factory.html"><code class="ph codeph">factory (action)</code></a></td>
<td>Defines a <a href="abenrap_factory_action_glosry.html">RAP factory action</a>.</td>
<td><p>Unmanaged RAP BO: 7.76</p>
<p>Managed RAP BO: 7.86</p></td>
<td><p>Unmanaged: 7.54</p>
<p>Managed: 7.57</p></td>
<td><p>Unmanaged RAP BO: 1905</p>
<p>Managed RAP BO: 2111</p></td>
<td><p>Unmanaged RAP BO: 1905</p>
<p>Managed RAP BO: 2111</p></td>
</tr>
<tr class="even">
<td><a href="abenbdl_action_default_factory.html"><code class="ph codeph">default</code></a></td>
<td>Defines a default static factory action.</td>
<td>7.90</td>
<td>7.58</td>
<td>2211</td>
<td>2211</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_action_onsave.html"><code class="ph codeph">save(finalize \lbr \| adjustnumbers \lbr \| finalize, adjustnumbers) \lbr(action)</code></a></td>
<td>Defines a <a href="abenrap_save_action_glosry.html">RAP save action</a>.</td>
<td>7.89</td>
<td>7.57</td>
<td>2208</td>
<td>2208</td>
</tr>
<tr class="even">
<td><a href="abenbdl_function.html"><code class="ph codeph">function ... [external]</code></a></td>
<td>Defines a <a href="abenrap_function_glosry.html">RAP function</a>.</td>
<td><p>Unmanaged RAP BO: 7.73</p>
<p>Managed RAP BO: 7.77</p></td>
<td><p>Unmanaged: 7.53</p>
<p>Managed: 7.54</p></td>
<td><p>Unmanaged: 1805</p>
<p>Managed: 1905</p></td>
<td><p>Unmanaged: 1805</p>
<p>Managed: 1905</p></td>
</tr>
<tr class="odd">
<td><a href="abenbdl_determine_action.html"><code class="ph codeph">determine action</code></a></td>
<td>Defines a <a href="abenrap_bo_det_action_glosry.html">determine action</a> that allows a <a href="abenrap_bo_consumer_glosry.html">RAP BO consumer</a> to execute <a href="abenrap_determination_glosry.html">determinations</a> and <a href="abenrap_validation_glosry.html">validations</a> on request.</td>
<td>7.81</td>
<td>7.55</td>
<td>2008</td>
<td>2008</td>
</tr>
<tr class="even">
<td><a href="abenbdl_determine_action.html"><code class="ph codeph">always (determine action)</code></a></td>
<td>Ignores the trigger condition of a <a href="abenrap_bo_det_action_glosry.html">determine action</a>.</td>
<td>7.82</td>
<td>7.56</td>
<td>2011</td>
<td>2011</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_recommendations.html"><code class="ph codeph">RAP - recommendation function</code></a></td>
<td>Defines a function for <a href="abenrecommendation_glosry.html">RAP recommendations</a></td>
<td>9.18</td>
<td>8.24</td>
<td>2602</td>
<td>2602</td>
</tr>
<tr class="even">
<td><code class="ph codeph"> draft action Edit \lbr\| draft action Activate \lbr\| draft action Discard \lbr\| draft action Resume [with additional implementation] \lbr\| draft determine action Prepare</code></td>
<td>Defines a draft action in a draft-enabled scenario.</td>
<td>7.81</td>
<td>7.55</td>
<td>2008</td>
<td>2008</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_draft_action.html"><code class="ph codeph">draft action AdditionalSave</code></a></td>
<td><a href="abenrap_bo_draft_action_glosry.html">RAP BO draft action</a> that allows users to define a custom saving strategy for draft instances.</td>
<td>7.93</td>
<td>7.58</td>
<td>2308</td>
<td>2308</td>
</tr>
<tr class="even">
<td><a href="abenbdl_draft_action.html"><code class="ph codeph">draft action Share</code></a></td>
<td><a href="abenrap_bo_draft_action_glosry.html">RAP BO draft action</a> that checks if the respective users are allowed to be added to the user list of the draft instance and switches an <a href="abenrap_exclusive_draft_glosry.html">RAP exclusive draft</a> into a <a href="abenrap_collaborative_draft_glosry.html">RAP collaborative draft</a> if not done before.</td>
<td>9.17</td>
<td>8.24</td>
<td>2508</td>
<td>2508</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_draft_action.html"><code class="ph codeph">with additional implementation</code></a></td>
<td>Implementation exit for draft actions that allows a user-defined implementation of the draft action in question.</td>
<td>7.81</td>
<td>7.55</td>
<td>2008</td>
<td>2008</td>
</tr>
<tr class="even">
<td><a href="abenbdl_draft_action.html"><code class="ph codeph">optimized</code></a></td>
<td>Recommended addition to the draft action <code class="ph codeph">Activate</code> that speeds up the activation of draft instances.</td>
<td>7.93</td>
<td>7.58</td>
<td>2308</td>
<td>2308</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_action_input_param.html"><code class="ph codeph">parameter ... [$self]</code></a></td>
<td>Defines an input parameter for an action or function.</td>
<td><p>Unmanaged RAP BO: 7.73</p>
<p>Managed RAP BO: 7.77</p></td>
<td><p>Unmanaged: 7.53</p>
<p>Managed: 7.54</p></td>
<td><p>Unmanaged: 1805</p>
<p>Managed: 1905</p></td>
<td><p>Unmanaged: 1805</p>
<p>Managed: 1905</p></td>
</tr>
<tr class="even">
<td><a href="abenbdl_action_input_param.html"><code class="ph codeph">deep [table] (parameter)</code></a></td>
<td>Defines a deep input parameter or a deep table input parameter for an action or function.</td>
<td>7.83</td>
<td>7.56</td>
<td>2102</td>
<td>2102</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_action_output_para.html"><code class="ph codeph">result[cardinality] { $self \| entity }</code></a></td>
<td>Defines an output parameter for an action or function.</td>
<td><p>Unmanaged RAP BO: 7.73</p>
<p>Managed RAP BO: 7.77</p></td>
<td><p>Unmanaged: 7.53</p>
<p>Managed: 7.54</p></td>
<td><p>Unmanaged: 1805</p>
<p>Managed: 1905</p></td>
<td><p>Unmanaged: 1805</p>
<p>Managed: 1905</p></td>
</tr>
<tr class="even">
<td><a href="abenbdl_action_output_para.html"><code class="ph codeph">selective (result)</code></a></td>
<td>Syntax addition for an output parameter for an action or function.</td>
<td>7.79</td>
<td>7.55</td>
<td>2002</td>
<td>2002</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_action_output_para.html"><code class="ph codeph">selective (deep result)</code></a></td>
<td>Syntax addition for a deep output parameter for an action or function.</td>
<td>7.89</td>
<td>7.57</td>
<td>2208</td>
<td>2208</td>
</tr>
<tr class="even">
<td><a href="abenbdl_type_mapping.html"><code class="ph codeph">mapping for ... [control ... ] [corresponding] [except]</code></a></td>
<td>Maps field names from database tables to field names from the current data model.</td>
<td>7.78</td>
<td>7.55</td>
<td>1911</td>
<td>1911</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_validations.html"><code class="ph codeph">validation ... on save { ... }</code></a></td>
<td>Defines a validation which is called during the save sequence.</td>
<td><p>Unmanaged RAP BO: 7.73</p>
<p>Managed RAP BO: 7.77</p></td>
<td><p>Unmanaged: 7.53</p>
<p>Managed: 7.54</p></td>
<td><p>Unmanaged: 1808</p>
<p>Managed: 1908</p></td>
<td><p>Unmanaged: 1808</p>
<p>Managed: 1908</p></td>
</tr>
<tr class="even">
<td><a href="abenbdl_determinations.html"><code class="ph codeph">determination ... on save { ... } \| on modify { ... }</code></a></td>
<td>Defines a determination which is called during the save sequence or immediately after data has been changed.</td>
<td><p>Unmanaged RAP BO: 7.73</p>
<p>Managed RAP BO: 7.77</p></td>
<td><p>Unmanaged: 7.53</p>
<p>Managed: 7.54</p></td>
<td><p>Unmanaged: 1808</p>
<p>Managed: 1908</p></td>
<td><p>Unmanaged: 1808</p>
<p>Managed: 1908</p></td>
</tr>
<tr class="odd">
<td><a href="abenbdl_actions_fc.html"><code class="ph codeph">features: global</code></a></td>
<td>RAP BO operation addition that defines global feature control for a RAP BO operation.</td>
<td>7.82</td>
<td>7.56</td>
<td>2011</td>
<td>2011</td>
</tr>
<tr class="even">
<td><a href="abenbdl_actions_fc.html"><code class="ph codeph">features: instance</code></a></td>
<td>RAP BO operation addition that defines instance feature control for a RAP BO operation.</td>
<td>7.77</td>
<td>7.54</td>
<td>1908</td>
<td>1908</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_internal.html"><code class="ph codeph">internal</code></a></td>
<td>Defines a RAP BO operation as internal.</td>
<td><p>Unmanaged RAP BO: 7.73</p>
<p>Managed RAP BO: 7.77</p></td>
<td><p>Unmanaged: 7.53</p>
<p>Managed: 7.54</p></td>
<td><p>Unmanaged: 1805</p>
<p>Managed: 1905</p></td>
<td><p>Unmanaged: 1805</p>
<p>Managed: 1905</p></td>
</tr>
<tr class="even">
<td><a href="abenbdl_precheck.html"><code class="ph codeph">precheck</code></a></td>
<td>Prevents illegal changes from reaching the application buffer by prechecking modify operations.</td>
<td>7.81</td>
<td>7.55</td>
<td>2008</td>
<td>2008</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_default_function.html"><code class="ph codeph">default function</code></a></td>
<td>Defines a <a href="abenrap_bo_defaulting_glosry.html">RAP default values function</a> for a RAP BO operation that defaults values for fields or input parameters on the user interface.</td>
<td>7.94</td>
<td>8.16</td>
<td>2311</td>
<td>2402</td>
</tr>
<tr class="even">
<td><a href="abenbdl_keyfunction.html"><code class="ph codeph">key ... function ...</code></a></td>
<td>Defines a <a href="abenrap_key_function_glosry.html">RAP key function</a> for a <a href="abenrap_alternative_key_glosry.html">BDEF alternative key</a>.</td>
<td>7.96</td>
<td>8.16</td>
<td>2405</td>
<td>2408</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_augment_projection.html"><code class="ph codeph">augment</code></a></td>
<td>Augments modify requests on the projection layer in a <a href="abencds_proj_bdef_glosry.html">CDS projection BDEF</a>.</td>
<td>7.82</td>
<td>7.56</td>
<td>2011</td>
<td>2011</td>
</tr>
<tr class="even">
<td><a href="abenbdl_event.html"><code class="ph codeph">event ... [[deep] parameter]</code></a></td>
<td>Defines a <a href="abenrap_entity_event_glosry.html">RAP business event</a> in a <a href="abenmanaged_rap_bo_glosry.html">managed</a> or <a href="abenunmanaged_rap_bo_glosry.html">unmanaged RAP BO</a>.</td>
<td>7.89</td>
<td>7.57</td>
<td>2208</td>
<td>2208</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_event_side_effect.html"><code class="ph codeph">event ... for side effects</code></a></td>
<td>Defines a <a href="abenrap_entity_event_glosry.html">RAP business event</a> for an <a href="abenrap_event_sideef_glosry.html">event-driven side effect</a></td>
<td>9.14</td>
<td>8.16</td>
<td>2502</td>
<td>2502</td>
</tr>
<tr class="even">
<td><a href="abenbdl_managed_event.html"><code class="ph codeph">managed event ... on ... parameter</code></a></td>
<td>Defines a <a href="abenrap_derived_event_glosry.html">RAP derived event</a> in a <a href="abenmanaged_rap_bo_glosry.html">managed</a> or <a href="abenunmanaged_rap_bo_glosry.html">unmanaged RAP BO</a>.</td>
<td>7.93</td>
<td>7.58</td>
<td>2308</td>
<td>2308</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_side_effects.html"><code class="ph codeph">side effects { ... [executed on ... ] affects ...; }</code></a></td>
<td>Defines a <a href="abenrap_side_effects_glosry.html">RAP side effect</a> in a <a href="abenmanaged_rap_bo_glosry.html">managed</a>, <a href="abenunmanaged_rap_bo_glosry.html">unmanaged</a>, or <a href="abencds_proj_bdef_glosry.html">projection BDEF</a>.</td>
<td>7.91</td>
<td>7.58</td>
<td>2302</td>
<td>2302</td>
</tr>
<tr class="even">
<td><a href="abenbdl_side_effects.html"><code class="ph codeph">executed on global</code></a><code class="ph codeph"> (side effects)</code></td>
<td>Defines a <a href="abenrap_side_effects_glosry.html">RAP side effect</a> for which the determine action is triggered whenever the user requests a global refresh.</td>
<td>9.17</td>
<td>8.24</td>
<td>2511</td>
<td>2602</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_changedocs_options.html"><code class="ph codeph">changedocuments([create:{none\|key\|data}]\lbr [,update:{none\|key\|data}]\lbr [,delete:{none\|key\|data}])</code></a></td>
<td>Defines logging options for RAP change documents.</td>
<td>9.16</td>
<td>7.58</td>
<td>2508</td>
<td>2508</td>
</tr>
<tr class="even">
<td><a href="abenbdl_define_key.html"><code class="ph codeph">define secondary key</code></a></td>
<td><a href="abenbdl_define_key.html"><code class="ph codeph">define pure key</code></a></td>
<td>Defines an <a href="abenrap_alternative_key_glosry.html">alternative key</a> in a managed or unmanaged RAP behavior definition.</td>
<td>9.12</td>
<td>8.16</td>
<td>2408</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_link_unlink_action.html"><code class="ph codeph">link action \| unlink action</code></a></td>
<td><a href="abenbdl_assoc_nonstand_ops.html">Non-standard operation for associations</a>. Links/unlinks a RAP BO entity instance to another RAP BO entity instance by setting the foreign key.</td>
<td>9.14</td>
<td>8.16</td>
<td>2502</td>
<td>2502</td>
</tr>
<tr class="even">
<td><a href="abenbdl_inverse_funct.html"><code class="ph codeph">inverse function</code></a></td>
<td><a href="abenbdl_assoc_nonstand_ops.html">Non-standard operation for associations</a>. Receives the values of the foreign key fields of the association target instances as input and provides the corresponding association source instances as result.</td>
<td>9.14</td>
<td>8.16</td>
<td>2502</td>
<td>2502</td>
</tr>
<tr class="odd">
<td><a href="abenbdl_use_projection.html"><code class="ph codeph">use association _assoc { with dependent draft; }</code></a></td>
<td>Used in <a href="abencds_proj_bdef_glosry.html">projection BDEFs</a> within cross-BO scenarios to enable <a href="abendraft_scope_glosry.html">draft scope</a> functionality. Turns the respective BO into a <a href="abenrap_principal_draft_bo_glosry.html">principal draft BO</a>.</td>
<td>9.16</td>
<td>8.16</td>
<td>2508</td>
<td>2508</td>
</tr>
</tbody>
</table>

**Interface Behavior Definitions**

| **Language Element**                                                               | **Meaning**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **ABAP Release, quarterly** | **ABAP Release, on-premise** | [**SAP BTP ABAP environment**](../../abap-glossary/abensap_btp_abap_env_glosry.md) | [**SAP S/4HANA Cloud Public Edition**](../../abap-glossary/abensap_s4hana_cpub_glosry.md) |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------|------------------------------------------------------------------|-------------------------------------------------------------------------|
| [`interface`](abenbdl_impl_type.md)                                              | Defines a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 7.88                        | 7.57                         | 2205                                                             | 2205                                                                    |
| [`extensible`](abenbdl_bo_interface_header.md)                                   | Declares a RAP BO interface as extensible.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 7.89                        | 7.57                         | 2208                                                             | 2208                                                                    |
| [`with managed instance filter`](abenbdl_mngd_instance_check_proj.md)            | Optional addition for [projection BDEFs](../../abap-glossary/abencds_proj_bdef_glosry.md) and [interface BDEFs](../../abap-glossary/abencds_interface_bdef_glosry.md). If specified, the [`WHERE`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_proj_view_cond_expr.md) condition of the underlying [CDS transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md) or [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) is evaluated when the BDEF is accessed with [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md) or [OData](../../abap-glossary/abenodata_glosry.md) requests from Web clients. | 7.93                        | 7.58                         | 2308                                                             | 2308                                                                    |
| [`define behavior for ... alias ... external`](abenbdl_define_beh_interface.md). | Entity behavior definition of an interface BDEF.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 7.88                        | 7.57                         | 2205                                                             | 2205                                                                    |
| [`use collaborative draft`](abenbdl_bo_interface_header.md)                      | Reuse of [RAP collaborative draft](../../abap-glossary/abenrap_collaborative_draft_glosry.md) from the base BO.                                                                                                                                                                                                                                                                                                                                                                                                                    | 9.17                        | 8.24                         | 2508                                                             | 2508                                                                    |
| [`use draft`](abenbdl_bo_interface_header.md)                                    | Reuses the draft-handling from the base BO.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 7.88                        | 7.57                         | 2205                                                             | 2205                                                                    |
| [`use side effects`](abenbdl_use_projection.md)                                  | Reuse of [RAP side effects](../../abap-glossary/abenrap_side_effects_glosry.md) from the base BO.                                                                                                                                                                                                                                                                                                                                                                                                                                  | 7.91                        | 7.58                         | 2302                                                             | 2302                                                                    |
| [`use event`](abenbdl_use_projection.md)                                         | Reuses a [RAP business event](../../abap-glossary/abenrap_entity_event_glosry.md) from the base BO.                                                                                                                                                                                                                                                                                                                                                                                                                                | 7.93                        | 7.58                         | 2308                                                             | 2308                                                                    |
| [`use etag`](abenbdl_define_beh_interface.md).                                   | Reuses the ETag from the base BO.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 7.88                        | 7.57                         | 2205                                                             | 2205                                                                    |
| [`with privileged mode`](abenbdl_bo_interface_header.md).                        | [BDEF privileged mode](../../abap-glossary/abenrap_privileged_mode_glosry.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 7.88                        | 7.57                         | 2205                                                             | 2205                                                                    |
| [`foreign entity`](abenbdl_bo_interface_header.md).                              | Defines a [RAP foreign entity](../../abap-glossary/abenrap_foreign_entity_glosry.md) for message mapping.                                                                                                                                                                                                                                                                                                                                                                                                                          | 7.88                        | 7.57                         | 2205                                                             | 2205                                                                    |
| [`field(readonly)`](abenbdl_field_interface.md)                                  | [RAP field characteristic](../../abap-glossary/abenrap_field_char_glosry.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 7.90                        | 7.58                         | 2211                                                             | 2211                                                                    |
| [`field(mandatory:create)`](abenbdl_field_interface.md)                          | [RAP field characteristic](../../abap-glossary/abenrap_field_char_glosry.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 7.90                        | 7.58                         | 2211                                                             | 2211                                                                    |
| [`field(readonly:update)`](abenbdl_field_interface.md)                           | [RAP field characteristic](../../abap-glossary/abenrap_field_char_glosry.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 7.90                        | 7.58                         | 2211                                                             | 2211                                                                    |
| [`field(suppress)`](abenbdl_field_interface.md)                                  | [RAP field characteristic](../../abap-glossary/abenrap_field_char_glosry.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 7.90                        | 7.58                         | 2211                                                             | 2211                                                                    |

**Abstract Behavior Definitions**

| **Language Element**                                                               | **Meaning**                                                                                                                                                                                                                           | **ABAP Release, quarterly** | **ABAP Release, on-premise** | [**SAP BTP ABAP environment**](../../abap-glossary/abensap_btp_abap_env_glosry.md) | [**SAP S/4HANA Cloud Public Edition**](../../abap-glossary/abensap_s4hana_cpub_glosry.md) |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------|------------------------------------------------------------------|-------------------------------------------------------------------------|
| [`abstract`](abenbdl_impl_type.md)                                               | Defines an abstract BDEF.                                                                                                                                                                                                             | 7.83                        | 7.56                         | 2102                                                             | 2102                                                                    |
| [`with hierarchy`](abenbdl_bdef_abstract_header.md)                              | Causes the construction of a new kind of BDEF derived type. Only available in abstract BDEFs.                                                                                                                                         | 7.83                        | 7.56                         | 2102                                                             | 2102                                                                    |
| [`with hierarchy like entity`](abenbdl_bdef_abstract_header.md)                  | Ensures that the BDEF derived type is equivalent to the structure type of the underlying CDS abstract entity, thereby ensuring compatibility.                                                                                         | 9.12                        | 8.16                         | 2408                                                             | 2408                                                                    |
| [`with control`](abenbdl_define_beh_abstract.md)                                 | Optional addition of the `define behavior` statement that is only available in abstract BDEFs. Adds the `%control` structure to the corresponding derived type structure.                                                             | 7.85                        | 7.56                         | 2108                                                             | 2108                                                                    |
| [`scalar entity`](abenbdl_define_beh_abstract.md)                                | Alternative to an entity behavior definition that is only available in abstract BDEFs. Integrates a node of the CDS composition tree into the hierarchical derived type of the abstract BDEF as a scalar type.                        | 7.83                        | 7.56                         | 2102                                                             | 2102                                                                    |
| [`association ... [with hierarchy]`](abenbdl_association_abstract.md)            | In an abstract BDEF, an association can be defined with the optional addition `with hierarchy`. This addition is available for to-parent associations and cross-BO associations to include them multiple times in the type structure. | 7.83                        | 7.56                         | 2102                                                             | 2102                                                                    |
| [`deep mapping for ... [corresponding] [sub]`](abenbdl_type_mapping_abstract.md) | Defines a deep mapping in an abstract BDEF.                                                                                                                                                                                           | 7.83                        | 7.56                         | 2102                                                             | 2102                                                                    |
| [`mandatory:execute`](abenbdl_field_abstract.md) as field attribute              | Field attribute that declares a field of an abstract BDEF as mandatory.                                                                                                                                                               | 7.88                        | 7.57                         | 2205                                                             | 2205                                                                    |
| [`mandatory:execute`](abenbdl_association_abstract.md) for associations          | Attribute that can be used for associations in abstract BDEFs to declare an association of an abstract BDEF as mandatory.                                                                                                             | 7.94                        | 7.58                         | 2311                                                             | 2402                                                                    |

### BDEF Extensions

**Keywords and Additions**

This list displays special language elements for BDEF extensions. You can also use statements from [CDS behavior definitions](../../abap-glossary/abencds_behavior_definition_glosry.md).

| **Language Element**                                                        | **Meaning**                                                                                                                                                                                                                   | **ABAP Release, quarterly** | **ABAP Release, on-premise** | [**SAP BTP ABAP environment**](../../abap-glossary/abensap_btp_abap_env_glosry.md) | [**SAP S/4HANA Cloud Public Edition**](../../abap-glossary/abensap_s4hana_cpub_glosry.md) |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|------------------------------|------------------------------------------------------------------|-------------------------------------------------------------------------|
| [`extension`](abenbdl_extensibility_managed_unm.md)                       | Defines a [BDEF extension](../../abap-glossary/abenrap_extension_glosry.md).                                                                                                                                                                    | 7.89                        | 7.57                         | 2208                                                             | 2208                                                                    |
| [`extensible`](abenbdl_extensible.md)                                     | [RAP extensibility enablement](../../abap-glossary/abenrap_ext_enablement_glosry.md) for a [BDEF extension](../../abap-glossary/abenrap_extension_glosry.md). Prerequisite for [extension layering](../../abap-glossary/abenrap_ext_layering_glosry.md).                            | 7.91                        | 7.58                         | 2302                                                             | 2302                                                                    |
| [`with friends`](abenbdl_with_friends.md)                                 | Optional addition that can be used to declare one or more BDEF extensions as [friends](../../abap-glossary/abenrap_bdef_friend_glosry.md) of the current behavior definition. BDEF friends have enhanced access rights to the BDEF in question. | 7.95                        | 8.16                         | 2402                                                             | 2402                                                                    |
| [`extend behavior for`](abenbdl_extend_beh.md)                            | Defines a [RAP entity behavior extension](../../abap-glossary/abenrap_behavior_extension_glosry.md).                                                                                                                                            | 7.89                        | 7.57                         | 2208                                                             | 2208                                                                    |
| [`extend own authorization context`](abenbdl_extend_own_auth_context.md). | Extends an [own authorization context](../../abap-glossary/abencds_own_ac_glosry.md).                                                                                                                                                           | 7.89                        | 7.57                         | 2208                                                             | 2208                                                                    |
| [`extend determine action`](abenbdl_determine_action_ext.md)              | Extends an existing [RAP BO determine action](../../abap-glossary/abenrap_bo_det_action_glosry.md).                                                                                                                                             | 7.89                        | 7.57                         | 2208                                                             | 2208                                                                    |
| [`extend draft determine action Prepare`](abenbdl_draft_action_ext.md)    | Extends an existing [draft determine action Prepare](../../abap-glossary/abenrap_bo_draft_action_glosry.md).                                                                                                                                    | 7.89                        | 7.57                         | 2208                                                             | 2208                                                                    |
| [`extend mapping for`](abenbdl_type_mapping_ext.md)                       | Extends an existing [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md).                                                                                                                                                     | 7.89                        | 7.57                         | 2208                                                             | 2208                                                                    |
| [`extension for projection`](abenbdl_extensibility_projection.md)         | Extends a [RAP projection behavior definition](../../abap-glossary/abencds_proj_bdef_glosry.md).                                                                                                                                                | 7.89                        | 7.57                         | 2208                                                             | 2208                                                                    |
| [`ancestor association`](abenbdl_ancestor_ext.md)                         | Defines a CDS association as ancestor association. The [association target](../../abap-glossary/abenassociation_target_glosry.md) must be an extension node.                                                                                    | 7.89                        | 7.57                         | 2208                                                             | 2208                                                                    |
| [`extension for abstract`](abenbdl_extension_for_abstract.md)             | Extends an [abstract behavior definition](../../abap-glossary/abencds_abstract_bdef_glosry.md).                                                                                                                                                 | 7.91                        | 7.58                         | 2302                                                             | 2302                                                                    |
