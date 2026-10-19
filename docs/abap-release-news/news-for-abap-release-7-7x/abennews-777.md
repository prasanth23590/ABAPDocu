---
title: "News for ABAP Release 7.77"
source_file: abennews-777.html
section: "ABAP Release News > News for ABAP Release 7.7x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.77

The kernel release for ABAP release 7.77 is 7.77.

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
<td><strong>New Built-In Data Types</strong></td>
<td><p>The following new <a href="abenddic_builtin_types_intro.html">built-in data types</a> were introduced in ABAP Dictionary:</p>
<ul>
<li><a href="abenddic_decimal_floating_point.html">Decimal floating point numbers</a></li>
<li><a href="abenddic_builtin_types.html"><code class="ph codeph">DECFLOAT16</code></a></li>
<li><a href="abenddic_builtin_types.html"><code class="ph codeph">DECFLOAT34</code></a></li>
<li><a href="abenddic_date_time_types.html">Date fields, time fields, and time stamp fields</a></li>
<li><a href="abenddic_builtin_types.html"><code class="ph codeph">DATN</code></a></li>
<li><a href="abenddic_builtin_types.html"><code class="ph codeph">TIMN</code></a></li>
<li><a href="abenddic_builtin_types.html"><code class="ph codeph">UTCLONG</code></a></li>
<li><a href="abenddic_geo_data.html">Geodata types</a></li>
<li><p><a href="abenddic_builtin_types.html"><code class="ph codeph">GEOM_EWKB</code></a></p>
<p>These data types are currently only supported by SAP HANA databases. These types can be mapped to HANA-specific data types but not to other vendor-specific data types. <a href="abenabap_managed_db_object_glosry.html">ABAP-managed database objects</a> where these types are used can only be created on SAP HANA databases.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Dynamic Cached Views</strong></td>
<td><a href="abendynamic_cache_glosry.html">Dynamic cached views</a> are a kind of <a href="abenhana_tuning_object_glosry.html">HANA tuning object</a> defined using the statement <a href="abenddicddl_define_dynamic_cache.html"><code class="ph codeph">DEFINE DYNAMIC CACHE</code></a>. A dynamic cache is a DDIC integration of an SAP HANA <a href="https://help.sap.com/docs/SAP_HANA_PLATFORM/bed8c14f9f024763b0777aa72b5436f6/bc12a173118548e9be8b69f1d62dfae1"><em>Dynamic Result Cache</em></a>.</td>
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
<td><strong>New Date Functions</strong></td>
<td><p>ABAP CDS now supports the following new date functions:</p>
<ul>
<li><a href="abencds_date_functions_v1.html"><code class="ph codeph">DATN_DAYS_BETWEEN</code></a></li>
<li><a href="abencds_date_functions_v1.html"><code class="ph codeph">DATN_ADD_DAYS</code></a></li>
<li><a href="abencds_date_functions_v1.html"><code class="ph codeph">DATN_ADD_MONTHS</code></a></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>New Time Stamp Functions</strong></td>
<td><p>ABAP CDS now supports the following new time stamp functions:</p>
<ul>
<li><a href="abencds_timestamp_functions_v1.html"><code class="ph codeph">UTCL_CURRENT</code></a></li>
<li><a href="abencds_timestamp_functions_v1.html"><code class="ph codeph">UTCL_ADD_SECONDS</code></a></li>
<li><a href="abencds_timestamp_functions_v1.html"><code class="ph codeph">UTCL_SECONDS_BETWEEN</code></a></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>New Date/Time Conversion Functions</strong></td>
<td><p>ABAP CDS now supports the following new <a href="abencds_date_time_conversions_v1.html">date/time conversion functions</a>:</p>
<ul>
<li><a href="abencds_date_time_conversions_v1.html"><code class="ph codeph">TSTMPL_TO_UTCL</code></a> and <a href="abencds_date_time_conversions_v1.html"><code class="ph codeph">TSTMPL_FROM_UTCL</code></a></li>
<li><a href="abencds_date_time_conversions_v1.html"><code class="ph codeph">DATS_TO_DATN</code></a> and <a href="abencds_date_time_conversions_v1.html"><code class="ph codeph">DATS_FROM_DATN</code></a></li>
<li><a href="abencds_date_time_conversions_v1.html"><code class="ph codeph">TIMS_TO_TIMN</code></a> and <a href="abencds_date_time_conversions_v1.html"><code class="ph codeph">TIMS_FROM_TIMN</code></a></li>
</ul></td>
</tr>
</tbody>
</table>

## Data Types

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>New Built-In ABAP Type <code class="ph codeph">utclong</code></strong></td>
<td><p>The new built-in <a href="abentimestamp_type_glosry.html">time stamp type</a> <a href="abenbuiltin_types_date_time.html"><code class="ph codeph">utclong</code></a> makes it possible to declare <a href="abentimestamp_field_glosry.html">time stamp fields</a> for <a href="abenutc_timestamp_glosry.html">UTC time stamps</a> according to the <a href="abenposix_timestamp_glosry.html">POSIX standard</a>. The new data type is taken into account in all relevant positions. Important points are:</p>
<ul>
<li>The associated data type in ABAP Dictionary was introduced with the name <a href="abenddic_builtin_types.html"><code class="ph codeph">UTCLONG</code></a>.</li>
<li>The <a href="abenbuiltin_types_date_time.html">value range</a> of the new data type are <a href="abentime_stamp_glosry.html">time stamps</a> between <em>0001-01-01T00:00:00.0000000</em> and <em>9999-12-31T23:59:59.9999999</em> plus a special initial value.</li>
<li>In assignments and comparisons, the data type <code class="ph codeph">utclong</code> can only be <a href="abenconversion_type_utclong.html">converted</a> to the types <code class="ph codeph">c</code> and <code class="ph codeph">string</code>, and vice versa. In assignments, any attempt to perform another conversion raises an exception of the new class <code class="ph codeph">CX_SY_CONVERSION_NOT_SUPPORTED</code>.</li>
<li>Time stamp fields are formatted specially in <a href="abenstring_template_glosry.html">string templates</a>.</li>
<li><p>There is a <a href="abenabap_xslt_asxml_elementary.html">mapping rule</a> for <a href="abenasxml_glosry.html">asXML</a>.</p>
<p>Time stamp fields must meet an <a href="abenalignment.html">alignment requirement</a>. Their memory address must be divisible by eight.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## String Processing

| Modification                      | Description                                                                                                                                                                                                                                                                                 |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Decimal Places in Time Stamps** | In [embedded expressions](../../abap-programming-language/abap-processing-internal-data/abenstring_templates_expressions.md) of [string templates](../../abap-glossary/abenstring_template_glosry.md), the formatting option `DECIMALS` can now be combined with `TIMESTAMP` and `TIME ZONE` to define the number of decimal places in UTC time stamps in packed numbers. |

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
<td><strong>Extensions of the <code class="ph codeph">INTO</code> Clause</strong></td>
<td><p>The <a href="abapinto_clause.html"><code class="ph codeph">INTO</code> clause</a> has been extended as follows:</p>
<ul>
<li>The new addition <a href="abapselect_into_target.html"><code class="ph codeph">NEW</code></a> can be used to implicitly create anonymous data objects as target areas. The addition <code class="ph codeph">NEW</code> now also makes inline declarations using <a href="abapselect_into_target.html"><code class="ph codeph">@DATA(...)</code></a> possible when using dynamic tokens.</li>
<li>The new addition <a href="abapselect_indicators.html"><code class="ph codeph">INDICATORS</code></a> can be used to specify a <a href="abennull_indicator_glosry.html">null indicator</a>.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Extension of the <code class="ph codeph">CAST</code> Matrix</strong></td>
<td>The matrix of types that can be converted to each other using a <a href="abensql_cast.html"><code class="ph codeph">CAST</code></a> expression was revised. In particular, the <a href="abennews-777.html#data-types">new data types</a> in ABAP Dictionary are respected. The new types <code class="ph codeph">DECFLOAT16</code> and <code class="ph codeph">DECFLOAT34</code> can also be specified after the addition <a href="abapselect_avg_as.html"><code class="ph codeph">AS</code></a> of the aggregate function <code class="ph codeph">AVG</code>.</td>
</tr>
<tr class="odd">
<td><strong>Extension of Arithmetic Expressions</strong></td>
<td>In <a href="abensql_arith.html">arithmetic expressions</a>, decimal floating point expressions with operators of types <code class="ph codeph">DECFLOAT16</code> or <code class="ph codeph">DECFLOAT34</code> are possible now.</td>
</tr>
<tr class="even">
<td><strong>New Built-In Functions</strong></td>
<td><p>ABAP SQL Now supports the following new built-in functions:</p>
<ul>
<li><a href="abensql_uuid.html"><code class="ph codeph">UUID</code></a></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>New Window Functions</strong></td>
<td><p>ABAP SQL now supports the following new <a href="abenwindow_function_glosry.html">window functions</a> in <a href="abenwindow_expression_glosry.html">window expressions</a>:</p>
<ul>
<li><a href="abensql_win_func.html"><code class="ph codeph">LEAD</code></a> and <a href="abensql_win_func.html"><code class="ph codeph">LAG</code></a>.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>SQL Conditions</strong></td>
<td><p>The <a href="abenasql_cond.html">SQL conditions</a> were revised as follows:</p>
<ul>
<li>Unlike in all other <a href="abenabap_sql_stmt_logexp.html">relational expressions</a> in ABAP SQL, the relational expression <a href="abenwhere_logexp_null.html"><code class="ph codeph">IS [NOT] NULL</code></a> can now be used to check <a href="abenlob_glosry.html">LOBs</a> and <a href="abengeo_data_type_glosry.html">geodata types</a>.</li>
<li>A new variant of the operator <a href="abenwhere_logexp_list_in.html"><code class="ph codeph">IN</code></a> can be used to compare multiple operands with a list of value tuples.</li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Hierarchy Navigators</strong></td>
<td><p>The <a href="abenhierarchy_agg_navi_glosry.html">hierarchy aggregate navigators</a> were revised as follows:</p>
<ul>
<li>New <code class="ph codeph">WITH</code> additions in the hierarchy navigator <a href="abenselect_hierarchy_desc_agg.html"><code class="ph codeph">HIERARCHY_DESCENDANTS_AGGREGATE</code></a> make it possible to evaluate the aggregate functions specified using <code class="ph codeph">MEASURES</code> for further row sets in the hierarchy.</li>
<li>The new hierarchy navigator <a href="abenselect_hierarchy_ancs_agg.html"><code class="ph codeph">HIERARCHY_ANCESTORS_AGGREGATE</code></a> makes it possible to calculate aggregate functions for ancestor nodes and also supports the new aggregate function <a href="abensql_agg_func.html"><code class="ph codeph">PRODUCT</code></a>.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Syntax Check for Literals and Host Constants</strong></td>
<td>The fact that conversions of <a href="abenhost_variable_glosry.html">host variables</a> in read positions need to be <a href="abapmove_exact.html">lossless</a> is checked for <a href="abenabap_sql_untyped_literals.html">untyped literals</a> and <a href="abenhost_constant_glosry.html">host constants</a> in the strict syntax check modes from ABAP release 7.62 and ABAP release 7.63 and hence can produce syntax errors.</td>
</tr>
</tbody>
</table>

## Messages

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Implicit Message Type in <code class="ph codeph">IF_T100_DYN_MSG</code></strong></td>
<td><p>If the object reference variable <code class="ph codeph">oref</code> in the variant <a href="abapmessage_msg.html"><code class="ph codeph">MESSAGE oref</code></a> of the statement <a href="abapmessage.html"><code class="ph codeph">MESSAGE</code></a> points to an object that implements the system interface <a href="abenif_t100_dyn_msg.html"><code class="ph codeph">IF_T100_DYN_MSG</code></a>, the addition <code class="ph codeph">TYPE</code> can be omitted and the message type from the interface attribute <code class="ph codeph">MSGTY</code> of the object is used implicitly.</p>
<p>Until now, however, the statement <code class="ph codeph">MESSAGE oref</code> could only have the further additions <a href="abapmessage_raising.html"><code class="ph codeph">RAISING</code></a> and <a href="abapmessage.html"><code class="ph codeph">DISPLAY LIKE</code></a> if <code class="ph codeph">TYPE</code> was specified explicitly. These additions are now also possible if <code class="ph codeph">TYPE</code> is not specified.</p></td>
</tr>
</tbody>
</table>

## ABAP CDS Access Control

| Modification                                                               | Description                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Addition `COMBINATION MODE OR\|AND` of the Statement `GRANT SELECT ON`** | The optional addition [`COMBINATION MODE`](../../abap-core-data-services-abap-cds/abap-cds-access-control/abencds_dcl_role_cond_rule.md) can now be used to define how the access conditions of multiple CDS access rules for the same CDS entity are combined.                                                   |
| **Addition `REDEFINITION` of the Statement `GRANT SELECT ON`**             | The addition [`REDEFINITION`](../../abap-core-data-services-abap-cds/abap-cds-access-control/abencds_dcl_role_cond_rule.md) is used to indicate that the specified CDS access rule is the only existing access rule and any other access rules are ignored.                                                       |
| **Addition `IN SCENARIO` of the Statement `GRANT SELECT ON`**              | The optional addition [`IN SCENARIO`](../../abap-core-data-services-abap-cds/abap-cds-access-control/abencds_f1_cond_pfcg.md) can be used to apply the switchable authorization check to an authorization object.                                                                                                 |
| **Generic Aspect Condition of the Statement `DEFINE ROLE`**                | An aspect condition can now be used to specify the [generic aspect](../../abap-core-data-services-abap-cds/abap-cds-access-control/abencds_f1_cond_aspect.md) defined in an aspect definition in the right side introduced by `ASPECT`.                                                                           |
| **New Variant `INHERITING CONDITIONS FROM SUPER`**                         | There is now another [variant](../../abap-core-data-services-abap-cds/abap-cds-access-control/abencds_f1_cond_inherit.md) of the inheritance condition in an access rule of the statement `DEFINE ROLE`, which applies the access conditions from `SUPER`.                                                        |
| **`REPLACING` Operator `ELEMENT ... WITH`**                                | Any number of [`ELEMENT`](../../abap-core-data-services-abap-cds/abap-cds-access-control/abencds_f1_cond_inherit.md) operators can be used to transform conditions that use fields of the inherited entity to a different field of the inheriting entity.                                                         |
| **Definition of a Generic Aspect**                                         | A [generic aspect](../../abap-core-data-services-abap-cds/abap-cds-access-control/abencds_f1_define_generic_aspect.md) can now be defined as part of a CDS access policy itself defined using `DEFINE ACCESSPOLICY`.                                                                                              |
| **Access Control for ABAP CDS Hierarchies**                                | ABAP CDS hierarchies can now be protected using access control with some [restrictions](../../abap-core-data-services-abap-cds/abap-cds-access-control/abencds_f1_dcl_hierarchies.md).                                                                                                                            |
| **DCL Restrictions for CDS Transactional Queries**                         | Transactional queries apply the [access control](../../abap-core-data-services-abap-cds/abap-cds-access-control/abencds_f1_dcl_projection_views.md) of the underlying CDS entity with restrictions.                                                                                                               |
| **`VOID`**                                                                 | The new addition [`VOID`](../../abap-core-data-services-abap-cds/abap-cds-access-control/abencds_dcl_role_conditions.md) can be specified in an access condition. It defines that the access condition in question is ignored.                                                                                    |
| **`CONSTRAINT ID`**                                                        | The new addition [`CONSTRAINT ID`](../../abap-core-data-services-abap-cds/abap-cds-access-control/abencds_f1_define_pfcg_mapping.md) can be specified in a PFCG mapping as part of a CDS access policy. It defines further restrictions for authorization fields of authorization objects in a CDS access policy. |

## ABAP RESTful Application Programming Model

In release 7.77, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

| Modification                   | Description                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Managed RAP BO**             | The new statement [`managed`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_impl_type.md) can be used to create [managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md) within the framework of the ABAP RESTful Application Programming Model. This scenario is intended for greenfield developments that are developed from scratch. Standard operations and services are provided by the RAP framework. |
| **Business Object Projection** | The new statement [`projection`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_impl_type.md) can be used to create [projections](../../abap-glossary/abenrap_projection_bo_glosry.md) of a business object. This projects and aliases a subset of a business object for a specific business service within the framework of the ABAP RESTful Application Programming Model.                                            |
