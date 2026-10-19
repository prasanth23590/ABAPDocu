---
title: "News for ABAP Release 9.14"
source_file: abennews-914.html
section: "ABAP Release News > News for ABAP Release 9.1x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 9.14

The kernel release for ABAP release 9.14 is 9.14.

## ABAP CDS

| Modification                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Writable CDS View Entities**                                            | CDS view entities can now be defined as writable using the syntax [`WRITABLE`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_wrtbl_view_v2.md). Some restrictions apply, which are listed in the respective chapter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **CDS Table Entities**                                                    | A new kind of CDS entity is available: the [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md). A CDS table entity defines a database table in ABAP CDS using the statement [`DEFINE TABLE ENTITY`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_table_entity.md). CDS table entities are the [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md) successor of [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md).                                                                                                                                                                                                                                                                                                                                            |
| **CDS Service Definitions Can Now Expose AMDP Procedure Implementations** | The new keyword [`EXPOSE METHOD`](../../abap-core-data-services-abap-cds/abap-cds-service-definitions/abensrvd_define_service.md) can now be used in [CDS service definitions](../../abap-glossary/abencds_service_definition_glosry.md) for exposing [AMDP procedure implementations](../../abap-glossary/abenamdp_procedure_method_glosry.md) for consumption in a [business service](../../abap-glossary/abenbs_glosry.md).                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Writable CDS External Entities**                                        | [CDS external entities](../../abap-glossary/abencds_external_entity_glosry.md) can now be defined as [writable](../../abap-glossary/abenwritable_ee_glosry.md) using the syntax [`WRITABLE`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_writable_ee.md). Writable external entities allow modifying data on external database systems using the [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) [`INSERT`](../../abap-programming-language/abap-database-access/abapinsert_dbtab.md), [`UPDATE`](../../abap-programming-language/abap-database-access/abapupdate.md), [`MODIFY`](../../abap-programming-language/abap-database-access/abapmodify_dbtab.md), and [`DELETE`](../../abap-programming-language/abap-database-access/abapdelete_dbtab.md) operations. An [ABAP SQL connection object](../../abap-glossary/abenabap_sql_conn_obj_glosry.md) is required to establish a [service connection](../../abap-glossary/abenservice_connection_glosry.md) and enable the [logical external schema](../../abap-glossary/abencds_logical_schema_glosry.md) for write access. |

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
<td><strong>Connection Objects</strong></td>
<td>An <a href="abenabap_sql_conn_obj_glosry.html">ABAP SQL connection object</a> implementing the interface <a href="abenif_abap_sql_connection.html"><code class="ph codeph">IF_ABAP_SQL_CONNECTION</code></a> represents a <a href="abendatabase_connection_glosry.html">database connection</a> that can be used behind the <code class="ph codeph">CONNECTION</code> addition of ABAP SQL statements. Connection objects enable using <a href="abenservice_connection_glosry.html">service connections</a> in <a href="abenabap_cloud_glosry.html">ABAP Cloud</a>.</td>
</tr>
<tr class="even">
<td><strong>Declaring a Client Column for Client-independent Data Sources</strong></td>
<td>The addition <a href="abapselect_declare_client.html"><code class="ph codeph">DECLARE CLIENT</code></a> in the <a href="abapfrom_clause.html"><code class="ph codeph">FROM</code> clause</a> of an ABAP SQL query declares a column of a <a href="abenclient_independent_glosry.html">client-independent</a> data source as a client column and the data source as client-dependent during the current access. Implicit client handling takes place.</td>
</tr>
<tr class="odd">
<td><strong>Addition <code class="ph codeph">OPTIONS</code> for DML Statements</strong></td>
<td><p>The addition <code class="ph codeph">OPTIONS</code> can now also be used for DML statements to introduce ABAP-specific additions.</p>
<ul>
<li>It can be used as <a href="abapiumd_options.html"><code class="ph codeph">OPTIONS</code></a> for the DML statement itself.</li>
<li>It can be used for <a href="abapinsert_from_select.html">subqueries</a> of DML statements.</li>
</ul></td>
</tr>
</tbody>
</table>

## AMDP

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Client Safety of AMDP Methods</strong></td>
<td><p>In <a href="abenamdp_client_safety.html">client-safe</a> AMDP methods, also client-dependent or client-independent <a href="abenddic_db_table_glosry.html">DDIC database tables</a> can be accessed. Client isolation is achieved by filtering a generated intermediate database view for the client that is contained in the HANA session variable <code class="ph codeph">CDS_CLIENT</code>.</p>
<p>In <a href="abenamdp_client_safety.html">client-safe</a> AMDP methods, only objects of the <a href="abenabap_db_schema_glosry.html">ABAP database schema</a> can be accessed that can be controlled by the <code class="ph codeph">USING</code> list.</p></td>
</tr>
<tr class="even">
<td><strong><code class="ph codeph">FOR SQL SERVICE</code></strong></td>
<td>The new addition <a href="abapclass-methods_for_sql_service.html"><code class="ph codeph">FOR SQL SERVICE</code></a> to the statement <code class="ph codeph">CLASS-METHODS</code> specifies that an <a href="abenamdp_procedure_method_glosry.html">AMDP procedure implementation</a> is intended to be exposed for external SQL access using an <a href="abenabap_sql_services_glosry.html">SQL service</a>.</td>
</tr>
</tbody>
</table>

## sXML Library

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Header Options for sXML Library</strong></td>
<td><p><a href="abenabap_sxml_lib_render.html">Header options</a> for the XML declaration are now available in the sXML Library:</p>
<ul>
<li><code class="ph codeph">CO_OPT_VAL_NO</code> (no XML header) This is the default option.</li>
<li><code class="ph codeph">CO_OPT_VAL_WITHOUT_ENCODING</code> (version)</li>
<li><code class="ph codeph">CO_OPT_VAL_FULL</code> (version and encoding)</li>
</ul></td>
</tr>
</tbody>
</table>

## Transformations

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>New Domain for Mapping from ABAP to XML</strong></td>
<td><p>The following new <a href="abenabap_xslt_asxml_schema.html">special domain</a> has been introduced, which overrides the default mapping of elementary ABAP types to asXML.</p>
<ul>
<li><code class="ph codeph">XSDGEO</code> for spatial data</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>New Format for <code class="ph codeph">format</code> in the Attribute <code class="ph codeph">option</code> of <code class="ph codeph">tt:value</code></strong></td>
<td><p>The following new format can be specified in parentheses after <a href="abenst_option_format.html"><code class="ph codeph">format</code></a> in the <a href="abenst_option.html"><code class="ph codeph">option</code></a> attribute of the ST statement <a href="abenst_tt_value_elementary.html"><code class="ph codeph">tt:value</code></a>:</p>
<ul>
<li><code class="ph codeph">geometry</code>, <code class="ph codeph">geography</code>, and <code class="ph codeph">geo=SRID</code> to define a spatial reference system for the conversion of the EWKB representation to GeoJSON and vice versa.</li>
</ul></td>
</tr>
</tbody>
</table>

## ABAP RESTful Application Programming Model

In release 9.14, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

| Modification                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Event-Driven Side Effects**                | You can define a business event to trigger a side effect in your RAP business object using the syntax [`for side effects`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_event.md). Whenever a defined event is raised by the application server, the [event-driven side effect](../../abap-glossary/abenrap_event_sideef_glosry.md) is triggered and the defined targets are reloaded.                                                                                             |
| **Non-Standard Operations for Associations** | You can now define [non-standard operations for associations](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_assoc_nonstand_ops.md). These are [link action, unlink action](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_link_unlink_action.md), and [inverse function](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_inverse_funct.md).                                                                                                                                                                                                  |
| **Editable Treeview**                        | The editable treeview scenario is now available. You can use the syntax [`instance hierarchy`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_instance_hierarchy.md) to make a treeview editable. The [RAP reorder action](../../abap-glossary/abenrap_reorder_action_glosry.md) can optionally be specified to move a hierarchy node to a dedicated position among its siblings. It is defined using the syntax addition [`[managed] reorder action`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_reorder_action.md). |

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
<td><strong>Runtime Type Service Method for BDEF Derived Types</strong></td>
<td><a href="abenrun_time_type_services_glosry.html">Runtime Type Services</a> now offer a method to dynamically and type-safely create BDEF derived types. See the topic <a href="abapderived_types_dynamic.html">here</a>.</td>
</tr>
<tr class="even">
<td><strong>Using Custom Secondary Table Keys in BDEF Derived Types</strong></td>
<td>It is possible to create your own secondary table keys for BDEF derived types, and use them in ABAP statements. Find more information <a href="abapderived_types_secondary_keys.html">here</a>.</td>
</tr>
<tr class="odd">
<td><strong>New Contract Checks</strong></td>
<td><p>The following <a href="abaprap_impl_rules.html">contract checks</a> have been added:</p>
<ul>
<li>Disallowed entries in the <code class="ph codeph">failed</code> response parameter</li>
<li>Entries with wrong fail causes in the <code class="ph codeph">failed</code> response parameter</li>
<li>Entries with non-initial <code class="ph codeph">%state_area</code> components in the <code class="ph codeph">reported</code> response in various contexts</li>
</ul>
<p>Violations result in the runtime error <code class="ph codeph">BEHAVIOR_BAD_HANDLER_RESPONSE</code>.</p></td>
</tr>
</tbody>
</table>
