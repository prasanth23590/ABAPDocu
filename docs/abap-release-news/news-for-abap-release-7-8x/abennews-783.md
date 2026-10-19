---
title: "News for ABAP Release 7.83"
source_file: abennews-783.html
section: "ABAP Release News > News for ABAP Release 7.8x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.83

The kernel release for ABAP release 7.83 is 7.83.

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
<td><strong>Extension for Load Unit</strong></td>
<td><p>In ABAP Dictionary, the <a href="abenddic_database_tables_load_unit.html">load unit</a> has been extended. There are now the following settings available:</p>
<ul>
<li><code class="ph codeph">Column Preferred</code></li>
<li><code class="ph codeph">Page Preferred</code></li>
<li><code class="ph codeph">Column Enforced</code></li>
<li><code class="ph codeph">Page Enforced</code></li>
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
<td><strong>CDS View Entity, <code class="ph codeph">UNION</code> Clause</strong></td>
<td><a href="abencds_union_v2.html"><code class="ph codeph">UNION</code></a> clauses are now supported in <a href="abencds_v2_view_glosry.html">CDS view entities</a>. There are a few differences to <code class="ph codeph">UNION</code> clauses in <a href="abencds_v1_view_glosry.html">CDS DDIC-based views</a>. The most important difference is that branches of union clauses can be nested within each other in CDS view entities.</td>
</tr>
<tr class="even">
<td><strong>CDS View Entity, <code class="ph codeph">DISTINCT</code></strong></td>
<td>The addition <a href="abencds_select_statement_v2.html"><code class="ph codeph">DISTINCT</code></a> is now available for <code class="ph codeph">SELECT</code> statements in <a href="abencds_v2_view_glosry.html">CDS view entities</a>.</td>
</tr>
<tr class="odd">
<td><strong>CDS View Entity, New Conversion Functions</strong></td>
<td><p>Two new conversion functions are available in CDS view entities:</p>
<ul>
<li><a href="abencds_conv_func_unit_curr_v2.html"><code class="ph codeph">GET_NUMERIC_VALUE</code></a></li>
<li><a href="abencds_conv_func_unit_curr_v2.html"><code class="ph codeph">CURR_TO_DECFLOAT_AMOUNT</code></a></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>CDS View Entity, Typed Literals</strong></td>
<td><a href="abencds_typed_literal_v2.html">Typed literals</a> are now available for <a href="abencds_v2_view_glosry.html">CDS view entities</a>. Typed literals allow an explicit type declaration and they are available for many built-in ABAP Dictionary data types.</td>
</tr>
<tr class="odd">
<td><strong>CDS Projection View, <code class="ph codeph">PROVIDER CONTRACT</code></strong></td>
<td><p>It is now possible to specify a provider contract for <a href="abencds_projection_view_glosry.html">CDS projection views</a> using the keyword <a href="abencds_pv_provider_contract.html"><code class="ph codeph">PROVIDER CONTRACT</code></a>. The provider contract specifies in which scenario a CDS projection view is used, and the scenario in turn determines in which runtime the view is executed and which features are available.</p>
<p>In this release, there is only one provider contract option available: <code class="ph codeph">TRANSACTIONAL_QUERY</code>.</p></td>
</tr>
</tbody>
</table>

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
<td><strong>New Additions for <code class="ph codeph">MOVE-CORRESPONDING</code></strong></td>
<td><p>It is now possible to specify <a href="abapmove-corresponding.html"><code class="ph codeph">MOVE-CORRESPONDING</code></a> statements with the following additions in the context of nested tables in <a href="abendeep_structure_glosry.html">deep structures</a>. Both ensure that nested tables of the deep target structures are not deleted and new lines of nested tables in deep source structures are added:</p>
<ul>
<li><a href="abapmove-corresponding.html"><code class="ph codeph">KEEPING TARGET LINES</code></a></li>
<li><a href="abapmove-corresponding.html"><code class="ph codeph">EXPANDING NESTED TABLES KEEPING TARGET LINES</code></a></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>New Additions for the Component Operator <code class="ph codeph">CORRESPONDING</code></strong></td>
<td><p>It is now possible to specify statements with the component operator <a href="abenconstructor_expr_corresponding.html"><code class="ph codeph">CORRESPONDING</code></a> with the following additions in the context of nested tables in <a href="abendeep_structure_glosry.html">deep structures</a>. Both ensure that the nested tables of deep target structures are not deleted and new lines of nested tables in deep source structures are added:</p>
<ul>
<li><a href="abencorresponding_constr_arg_type.html"><code class="ph codeph">APPENDING BASE</code></a></li>
<li><a href="abencorresponding_constr_arg_type.html"><code class="ph codeph">DEEP APPENDING BASE</code></a></li>
</ul></td>
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
<td><strong>New String Function</strong></td>
<td>ABAP SQL now supports the new string function <a href="abensql_string_func.html"><code class="ph codeph">INITCAP</code></a>.</td>
</tr>
<tr class="even">
<td><strong>New Date and Time Functions</strong></td>
<td><p>The following new generic <a href="abenabap_sql_date_time_functions.html">date and time functions</a> are available:</p>
<p>See below.</p></td>
</tr>
<tr class="odd">
<td><strong>New Casts</strong></td>
<td><p>The following <a href="abensql_cast.html">new casts</a> are available:</p>
<p>See below.</p></td>
</tr>
<tr class="even">
<td><strong>New Set Operators</strong></td>
<td>ABAP SQL now supports the new set operators <a href="abapunion.html"><code class="ph codeph">INTERSECT</code></a> and <a href="abapunion.html"><code class="ph codeph">EXCEPT</code></a>.</td>
</tr>
<tr class="odd">
<td><strong>New Function for Unit Conversion</strong></td>
<td>ABAP SQL now supports the new function <a href="abensql_curr_unit_conv_func.html"><code class="ph codeph">UNIT_CONVERSION</code></a> for unit conversions.</td>
</tr>
<tr class="even">
<td><strong>New Expression Null</strong></td>
<td>ABAP SQL now supports the new expression <a href="abensql_null.html"><code class="ph codeph">NULL</code></a>.</td>
</tr>
</tbody>
</table>

**New Date and Time Functions** \|**SQL Function**\|**Date**\|**Time**\|**Time Stamp** \| \|:---\|:---\|:---\|:---\| \|`IS_VALID`\|[x](../../abap-programming-language/abap-database-access/abensql_date_func.md)\|[x](../../abap-programming-language/abap-database-access/abensql_time_func.md)\|[x](../../abap-programming-language/abap-database-access/abensql_timestamp_func.md) \| \|`EXTRACT_YEAR`\|[x](../../abap-programming-language/abap-database-access/abensql_date_func.md)\|-\|[x](../../abap-programming-language/abap-database-access/abensql_timestamp_func.md) \| \|`EXTRACT_MONTH`\|[x](../../abap-programming-language/abap-database-access/abensql_date_func.md)\|-\|[x](../../abap-programming-language/abap-database-access/abensql_timestamp_func.md) \| \|`EXTRACT_DAY`\|[x](../../abap-programming-language/abap-database-access/abensql_date_func.md)\|-\|[x](../../abap-programming-language/abap-database-access/abensql_timestamp_func.md) \| \|`EXTRACT_HOUR`\|-\|[x](../../abap-programming-language/abap-database-access/abensql_time_func.md)\|[x](../../abap-programming-language/abap-database-access/abensql_timestamp_func.md) \| \|`EXTRACT_MINUTE`\|-\|[x](../../abap-programming-language/abap-database-access/abensql_time_func.md)\|[x](../../abap-programming-language/abap-database-access/abensql_timestamp_func.md) \| \|`EXTRACT_SECOND`\|-\|[x](../../abap-programming-language/abap-database-access/abensql_time_func.md)\|[x](../../abap-programming-language/abap-database-access/abensql_timestamp_func.md) \| \|`DAYNAME`\|[x](../../abap-programming-language/abap-database-access/abensql_date_func.md)\|-\|[x](../../abap-programming-language/abap-database-access/abensql_timestamp_func.md) \| \|`MONTHNAME`\|[x](../../abap-programming-language/abap-database-access/abensql_date_func.md)\|-\|[x](../../abap-programming-language/abap-database-access/abensql_timestamp_func.md) \| \|`WEEKDAY`\|[x](../../abap-programming-language/abap-database-access/abensql_date_func.md)\|-\|[x](../../abap-programming-language/abap-database-access/abensql_timestamp_func.md) \| \|`DAYS_BETWEEN`\|[x](../../abap-programming-language/abap-database-access/abensql_date_func.md)\|-\|[x](../../abap-programming-language/abap-database-access/abensql_timestamp_func.md) \| \|`ADD_DAYS`\|[x](../../abap-programming-language/abap-database-access/abensql_date_func.md)\|-\|[x](../../abap-programming-language/abap-database-access/abensql_timestamp_func.md) \| \|`ADD_MONTHS`\|[x](../../abap-programming-language/abap-database-access/abensql_date_func.md)\|-\|[x](../../abap-programming-language/abap-database-access/abensql_timestamp_func.md)\|

**New Date and Time Functions** \|**Source type**\|**Numeric target type**\|**Character-like target type**\|**Date/time field as target type** \| \|:---\|:---\|:---\|:---\| \|`CHAR`, `SSTRING`, `DATS`, `TIMS`\|`INT1`, `INT2`, `INT4`, `INT8`, `DEC`, `CURR`, `QUAN`, `DECFLOAT16`, `DECFLOAT34`, `FLTP`\|-\|- \| \|`FLTP`\|`INT1`, `INT2`, `INT4`, `INT8`, `DEC`, `CURR`, `QUAN`, `DECFLOAT16`, `DECFLOAT34`\|`CHAR`, `SSTRING`\|- \| \|`DF16_DEC`, `DF34_DEC`\|`FLTP`\|-\|- \| \|`DATN`\|-\|-\|`DATS` \| \|`TIMN`\|-\|-\|`TIMS`\|

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
<td><strong>Configuration of the Documentation</strong></td>
<td><p>From release 7.83 on, important settings of the ABAP Keyword Documentation can be configured explicitly. Before, the documentation was configured implicitly from system settings.</p>
<p>The configuration of the ABAP Keyword Documentation is saved in customizing table <code class="ph codeph">ABDOCCONFIG</code>, that is maintained with transaction code <code class="ph codeph">ABAP_DOCU_CONFIG</code> (based on executable program <code class="ph codeph">ABAP_DOCU_CONFIG</code>) or with the configuration entity <code class="ph codeph">ABAP_DOCU_CONFIG_ENTITY</code>. All repository objects related to the configuration are documented.</p>
<p>The following properties can be set:</p>
<ul>
<li><p><strong>CP</strong></p>
<p>If set to <em>X</em>, the ABAP Keyword Documentation uses terms appropriate for the <a href="abensap_btp_abap_env_glosry.html">SAP BTP ABAP environment</a> (aka <a href="abensteampunk_glosry.html">Steampunk</a>) instead of <a href="abenas_abap_glosry.html">Application Server ABAP</a> in some footers and copyright texts.</p>
<p>Recommendation:</p>
<ul>
<li>Set to <em>X</em> in systems of the SAP BTP ABAP environment.</li>
<li>Set to initial in all other systems.</li>
</ul></li>
<li><p><strong>ICF</strong></p>
<p>Enables or disables the Web Version of the ABAP Keyword Documentation based on ICF nodes <code class="ph codeph">/sap/public/bc/abap/docu</code> and <code class="ph codeph">/sap/bc/abap/docu</code>. The following settings can be applied:</p>
<ul>
<li>If set to <em>X</em>, the Web Version is enabled. The execution of example programs from the Web Version is disabled.</li>
<li><p>If set to <em>E</em>, the Web Version is enabled. The execution of example programs from the Web Version is also enabled.</p>
<p>Recommendation:</p>
<ul>
<li>Set to <em>E</em> in SAP development systems.</li>
<li>Set to <em>E</em> in customer development systems.</li>
<li>Set to <em>X</em> in SAP S/4HANA.</li>
<li>Set to initial in SAP BTP ABAP environment and SAP S/4HANA Cloud.</li>
</ul></li>
</ul></li>
<li><p><strong>BATCH</strong></p>
<p>If set to <em>X</em>, the infrastructure of the ABAP Keyword Documentation is allowed to start batch jobs that prepare buffers that are needed for search in and display of the documentation.</p>
<p>Recommendation:</p>
<ul>
<li>Set to <em>X</em> in SAP S/4HANA.</li>
<li>Set to initial in SAP BTP ABAP environment.</li>
</ul></li>
<li><p><strong>MAILBOX</strong></p>
<p>If set to <em>X</em>, the ABAP Keyword Documentation display offers a function to send a feedback mail to <em><a href="mailto:abap.docu@exchange.sap.corp">abap.docu@exchange.sap.corp</a></em>. This mailbox is only available to SAP employees. Therefore, the setting makes sense for SAP's own development systems only.</p>
<p>Recommendation:</p>
<ul>
<li>Set to <em>X</em> in SAP's own development systems.</li>
<li>Set to initial in all other systems.</li>
</ul></li>
<li><p><strong>VERSION</strong> Determines the <a href="abenabap_version_glosry.html">ABAP language version</a> for which the ABAP Keyword Documentation is displayed. Allowed values are defined in domain <code class="ph codeph">ABAPVRS</code>. This setting can be overridden when calling the documentation using the respective APIs:</p>
<ul>
<li><code class="ph codeph">CL_ABAP_DOCU</code> for the SAP GUI version</li>
<li><p><code class="ph codeph">CL_ABAP_DOCU_EXTERNAL</code> for the ADT or Web version.</p>
<p>Calls to the documentation from ABAP Workbench and ADT set the language version depending on the object currently being edited. Calls to the documentation via the <code class="ph codeph">ABAPDOCU</code> and <code class="ph codeph">ABAPHELP</code> transactions use the version from <code class="ph codeph">ABDOCCONFIG</code> by default. An initial value for <code class="ph codeph">VERSION</code> in <code class="ph codeph">ABDOCCONFIG</code> displays the documentation for <a href="abenstandard_abap_glosry.html">Standard ABAP</a> (<em>X</em>).</p>
<p>Recommendation:</p>
<ul>
<li>Set to <em>X</em> in SAP S/4HANA</li>
<li>Set to <code class="ph codeph">5</code> in SAP BTP ABAP environment and SAP S/4HANA Cloud</li>
</ul>
<p>Program <code class="ph codeph">ABAP_DOCU_CONFIG</code> allows a choice to be made between different sets of parameters:</p>
<ul>
<li>Parameter set typical for SAP development systems</li>
<li>Parameter set typical for customer development systems</li>
<li>Parameter set typical for SAP S/4HANA systems</li>
<li>Parameter set typical for SAP S/4HANA Cloud ABAP environment</li>
<li>Parameter set typical for SAP BTP ABAP environment</li>
<li>Current parameter set</li>
</ul></li>
</ul></li>
</ul>
<p>The passed parameters are used as default values for a dialog window and can be overridden there.If customizing table <code class="ph codeph">ABDOCCONFIG</code> is initial in a customer system, the first call of the ABAP Keyword documentation supplies it with values recommended for an SAP S/4HANA System. In SAP's own systems, values for a SAP development system are supplied. If the table is partly filled, default values are used for the missing rows. These values are initial for all properties except <code class="ph codeph">VERSION</code>. If the language version is not passed by the caller and cannot be found in <code class="ph codeph">ABDOCCONFIG</code>, the value <em>X</em> is used and a warning is shown in the documentation display.</p></td>
</tr>
</tbody>
</table>

## ABAP RESTful Application Programming Model

In release 7.83, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

| Modification                                 | Description                                                                                                                                                                                                                               |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Unmanaged Early Numbering in Managed BOs** | The entity behavior characteristic [`early numbering`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_early_numb.md) can be used to define unmanaged [early numbering](../../abap-glossary/abenrap_early_numbering_glosry.md) for all primary key fields of a managed RAP BO.                    |
| **Implementing Cleanup in Managed BOs**      | The new addition [`and cleanup`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_saving.md) is available for additional and unmanaged save in managed RAP BOs. It allows the application developer to implement the cleanup method.                                             |
| **CDS Abstract Behavior Definitions**        | A new [implementation type](../../abap-glossary/abencds_bdef_impl_type_glosry.md) is available: the [RAP abstract behavior definition](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_abstract.md). Such abstract BDEFs mainly serve as typing mechanism for deep action or function parameters. |
