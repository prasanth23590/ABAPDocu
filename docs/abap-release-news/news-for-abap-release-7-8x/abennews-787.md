---
title: "News for ABAP Release 7.87"
source_file: abennews-787.html
section: "ABAP Release News > News for ABAP Release 7.8x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.87

The kernel release for ABAP release 7.87 is 7.87.

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
<td><strong>Comparisons with CDS Amount Fields and CDS Quantity Fields</strong></td>
<td>Special handling for <a href="abencds_amount_field.html">CDS amount fields</a> and <a href="abencds_quantity_field.html">CDS quantity fields</a> for <a href="abencds_cond_expr_types_v2.html">comparisons</a> in <a href="abencds_v2_view_glosry.html">CDS view entities</a> has been implemented.</td>
</tr>
<tr class="even">
<td><strong>CDS View Entity, Extended Cast Matrix</strong></td>
<td><p>New <a href="abencds_cast_expression_v2.html">casting options</a> have been added in <a href="abencds_v2_view_glosry.html">CDS view entities</a>.</p>
<ul>
<li>Casting from data type <code class="ph codeph">SSTRING</code> into data types <code class="ph codeph">DEC</code>, <code class="ph codeph">CURR</code>, <code class="ph codeph">QUAN</code>, <code class="ph codeph">INT1</code>, <code class="ph codeph">INT2</code>, <code class="ph codeph">INT4</code>, <code class="ph codeph">INT8</code>, <code class="ph codeph">DECFLOAT16</code>, and <code class="ph codeph">DECFLOAT34</code> is now possible.</li>
<li>Casting from data type <code class="ph codeph">CHAR</code> into data types <code class="ph codeph">DEC</code>, <code class="ph codeph">CURR</code>, <code class="ph codeph">QUAN</code>, <code class="ph codeph">INT1</code>, <code class="ph codeph">INT2</code>, <code class="ph codeph">INT4</code>, <code class="ph codeph">INT8</code>, <code class="ph codeph">DECFLOAT16</code>, and <code class="ph codeph">DECFLOAT34</code> is now possible.</li>
<li>Casting from data type <code class="ph codeph">DATS</code> into data types <code class="ph codeph">DEC</code>, <code class="ph codeph">CURR</code>, <code class="ph codeph">QUAN</code>, <code class="ph codeph">INT1</code>, <code class="ph codeph">INT2</code>, <code class="ph codeph">INT4</code>, <code class="ph codeph">INT8</code>, <code class="ph codeph">DECFLOAT16</code>, and <code class="ph codeph">DECFLOAT34</code> is now possible.</li>
<li>Casting from data type <code class="ph codeph">TIMS</code> into data types <code class="ph codeph">DEC</code>, <code class="ph codeph">CURR</code>, <code class="ph codeph">QUAN</code>, <code class="ph codeph">INT1</code>, <code class="ph codeph">INT2</code>, <code class="ph codeph">INT4</code>, <code class="ph codeph">INT8</code>, <code class="ph codeph">DECFLOAT16</code>, and <code class="ph codeph">DECFLOAT34</code> is now possible.</li>
<li>Casting from data types <code class="ph codeph">DECFLOAT16</code> and <code class="ph codeph">DECFLOAT34</code> into data type <code class="ph codeph">CHAR</code> is now possible.</li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>CDS View Entity, Table Buffering</strong></td>
<td><p><a href="abentable_buffering_glosry.html">Table buffering</a> can be defined for <a href="abencds_v2_view_glosry.html">CDS view entities</a> now:</p>
<ul>
<li>Table buffering can be enabled and disabled with the annotation <a href="abencds_v2_view_buffering.html"><code class="ph codeph">@AbapCatalog.entityBuffer.definitionAllowed: true\|false</code></a></li>
<li>The <a href="abenbuffer_type.html">buffering type</a> can be specified with a <a href="abencds_view_entity_b_glosry.html">CDS entity buffer</a> defined by <a href="abencds_define_view_entity_buffer.html"><code class="ph codeph">DEFINE VIW ENTITY BUFFER ON cds_view_entity ...</code></a></li>
</ul>
<p>Table buffering can be defined differently for the layers core, localization, industry, partner and customer.</p></td>
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
<td><strong>New Addition <code class="ph codeph">STEP</code> for Defining Step Size and Processing Order</strong></td>
<td>The new addition <code class="ph codeph">STEP</code> defines the step size and the order for processing an internal table. For the statements <a href="abaploop_at_itab_cond.html"><code class="ph codeph">LOOP</code></a> and <a href="abenfor_cond.html"><code class="ph codeph">FOR</code></a>, <code class="ph codeph">STEP</code> can be used to control the step size and the processing order. For the statements <a href="abapappend_linespec.html"><code class="ph codeph">APPEND</code></a>, <a href="abapdelete_itab_lines.html"><code class="ph codeph">DELETE</code></a>, <a href="abapinsert_itab_linespec.html"><code class="ph codeph">INSERT</code></a>, <a href="abenvalue_constructor_params_lspc.html"><code class="ph codeph">VALUE</code></a>, and <a href="abennew_constructor_params_lspc.html"><code class="ph codeph">NEW</code></a>, <code class="ph codeph">STEP</code> can only be used to define the step size. It is not possible to change the processing order with <code class="ph codeph">STEP</code> for these statements.</td>
</tr>
<tr class="even">
<td><strong>Exception when Mixing Index Access with Hash Key Access</strong></td>
<td><p>Access to a <a href="abentable_index_glosry.html">table index</a> when accessing an internal table using a <a href="abenhash_key_glosry.html">hash key</a> (accessing a <a href="abenhashed_table_glosry.html">hashed table</a> using its primary key or accessing any internal table using a hashed <a href="abensecondary_key_glosry.html">secondary key</a>) is not allowed. When a hashed key is specified dynamically behind <code class="ph codeph">USING KEY</code> in statement <a href="abaploop_at_itab.html"><code class="ph codeph">LOOP AT</code></a> or expression <a href="abenfor_itab.html"><code class="ph codeph">FOR ... IN</code></a>, usage of <code class="ph codeph">FROM</code> and <code class="ph codeph">TO</code> must result in an exception. This was not the case before release 7.87.</p>
<p>From release 7.87 on, the runtime error <code class="ph codeph">ITAB_ILLEGAL_INDEX_OP</code> occurs in such a situation. Before release 7.87, the behavior was undefined.</p>
<p>This change is slightly incompatible.</p></td>
</tr>
<tr class="odd">
<td><strong>Correction for <code class="ph codeph">FROM</code> Addition</strong></td>
<td><p>When a negative value is specified for <code class="ph codeph">FROM</code> in statement <a href="abaploop_at_itab.html"><code class="ph codeph">LOOP AT</code></a> or expression <a href="abenfor_itab.html"><code class="ph codeph">FOR ... IN</code></a>, it is set to 1 implicitly. Before release 7.87, this was not the case in the following situation:</p>
<ul>
<li>The internal table is accessed using a sorted key.</li>
<li>The internal table contains more than 10 table lines.</li>
<li>A <code class="ph codeph">WHERE</code> condition is specified that can be <a href="abenitab_where_optimization.html">optimized</a>.</li>
</ul>
<p>The loop was not processed at all. From release 7.87 on, the loop is processed as documented.</p>
<p>This change is slightly incompatible.</p></td>
</tr>
</tbody>
</table>

## ABAP RESTful Application Programming Model

In release 7.87, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

| Modification                                   | Description                                                                                                                                                                                                                                                                           |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Unmanaged RAP BO, New Field Characteristic** | In [unmanaged RAP business objects](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), a new field characteristic is available: [`field(suppress)`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_field_char.md). It removes the field in question from the [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) and from all RAP APIs. |

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
<td><strong>Entity Manipulation Language</strong></td>
<td><ul>
<li><p><a href="abapraise_entity_event.html"><code class="ph codeph">RAISE ENTITY EVENT</code></a></p>
<p>Raises a <a href="abenrap_entity_event_glosry.html">RAP business event</a>.</p></li>
</ul></td>
</tr>
</tbody>
</table>
