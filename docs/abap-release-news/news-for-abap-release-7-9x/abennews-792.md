---
title: "News for ABAP Release 7.92"
source_file: abennews-792.html
section: "ABAP Release News > News for ABAP Release 7.9x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.92

The kernel release for ABAP release 7.92 is 7.92.

## ABAP Keyword Documentation

| Modification                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **External Mailbox for Documentation** | From release 7.92 on, the ABAP Keyword Documentation display offers a function to send a feedback mail to *<f1_help@sap.com>* in non-SAP development systems and in the [SAP Help Portal](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/index.htm). Up to now, the possibility for a feedback mail existed only in SAP's own development systems. The function can be switched on or off in the configuration of the ABAP Keyword Documentation, see SAP Note [3051036](https://launchpad.support.sap.com/#/notes/3051036). |

## ABAP CDS

| Modification                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Annotation `Environment.sql.passValue`, Scope Enhancement** | The ABAP annotation [`Environment.sql.passValue`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_parameter_annotations.md) is now also available for [CDS parameters](../../abap-glossary/abencds_parameter_glosry.md) in CDS view entities, CDS projection views, and CDS hierarchies. The annotation scope has been enhanced.                                                                                                                                                                          |
| **New Annotation `Environment.sql.passValueForClient`**       | A new ABAP annotation is available in CDS view entities, CDS projection views, and CDS hierarchies: [`Environment.sql.passValueForClient`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_entity_annotations.md). It works in a similar way to the annotation `Environment.sql.passValue`, but for client fields. It specifies whether a placeholder *?* or a literal value is passed to the database in an ABAP SQL condition when the client field is compared with a host variable. |
| **Further Operand Positions for Typed Literals**              | [Typed literals](../../abap-glossary/abentyped_literal_glosry.md) can now be used in more operand positions in ABAP CDS. They can now be used in the `WHERE` condition of [CDS projection views](../../abap-glossary/abencds_projection_view_glosry.md) and in the `ON` condition of [CDS associations](../../abap-glossary/abencds_association_glosry.md).                                                                                                                                                |

## ABAP SQL

| Modification                           | Description                                                                                                                                                                                                                                                                                                |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Access to Multiple Internal Tables** | It is now possible to process multiple internal tables accessed with [`FROM @itab`](../../abap-programming-language/abap-database-access/abapselect_itab.md) within one ABAP SQL statement with the [ABAP SQL in-memory engine](../../abap-programming-language/abap-database-access/abenabap_sql_inmemeng.md). Currently, this is restricted to joins of internal tables where no database tables are involved. |

## ABAP RESTful Application Programming Model

In release 7.92, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

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
<td><strong>Authorization Control on Action Level</strong></td>
<td><p>Two new <a href="abenbdl_operations_additions.html">RAP BO operation additions</a> are available for <a href="abenrap_action_glosry.html">actions</a> and <a href="abenrap_bo_det_action_glosry.html">determine actions</a>:</p>
<ul>
<li><a href="abenbdl_actions_auth_global.html"><code class="ph codeph">authorization:global</code></a></li>
<li><p><a href="abenbdl_actions_auth_instance.html"><code class="ph codeph">authorization:instance</code></a></p>
<p>Both of these additions are specified on action-level and they replace the <a href="abenbdl_authorization.html">authorization control</a> that is specified in the <a href="abenrap_auth_ma_ent_glosry.html">authorization master entity</a>.</p>
<p>In managed, unmanaged, and projection BDEFs, these additions are optional. In <a href="abenrap_base_bdef_ext_glosry.html">base BDEF extensions</a>, authorization control on action-level is mandatory.</p></li>
</ul></td>
</tr>
</tbody>
</table>

### ABAP EML

| Modification                         | Description                                                                                                                                                                                                                                       |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`RAISE ENTITY EVENT`**             | You can use [`RAISE ENTITY EVENT`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapraise_entity_event.md) statements to raise a [RAP business event](../../abap-glossary/abenrap_entity_event_glosry.md).                                                                                                     |
| **`METHODS, FOR ENTITY EVENT`**      | The [`METHODS, FOR ENTITY EVENT`](../../abap-rap-business-objects/abap-for-rap-business-objects/abenmethod_for_entity_event.md) addition supports [RAP event handler method](../../abap-glossary/abenrap_event_handler_meth_glosry.md) definitions.                                                                             |
| **`CLASS, FOR EVENTS OF`**           | The [`FOR EVENTS OF`](../../abap-rap-business-objects/abap-for-rap-business-objects/abenclass_for_events.md) addition supports the creation of [RAP event handler classes](../../abap-glossary/abenrap_event_handler_class_glosry.md).                                                                                          |
| **`CL_ABAP_BEHAVIOR_EVENT_HANDLER`** | Local classes that inherit from [`CL_ABAP_BEHAVIOR_EVENT_HANDLER`](../../abap-rap-business-objects/abap-for-rap-business-objects/abencl_abap_behavior_event_handler.md) can be implemented in the [CCIMP include](../../abap-glossary/abenccimp_glosry.md) of a RAP event handler class to locally consume RAP business events. |
| **`CL_ABAP_TX`**                     | The class [`CL_ABAP_TX`](../../abap-programming-language/abap-database-access/abaprap_cl_abap_tx.md) is used to explicitly set RAP transactional phases.                                                                                                                                             |
