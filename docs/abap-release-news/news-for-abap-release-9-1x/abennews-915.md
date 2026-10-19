---
title: "News for ABAP Release 9.15"
source_file: abennews-915.html
section: "ABAP Release News > News for ABAP Release 9.1x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 9.15

The kernel release for ABAP release 9.15 is 9.15.

## ABAP CDS

| Modification              | Description                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CDS Delegated Buffers** | [CDS delegated buffers](../../abap-glossary/abencds_del_buffer_glosry.md) can now be defined for [CDS view entities](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_v2_views.md) using the syntax DEFINE VIEW ENTITY BUFFER ON ... cds_entity [`TYPE DELEGATED`](../../abap-core-data-services-abap-cds/abap-cds-tuning-objects/abencds_define_delegated_buffer.md). Delegated buffers delegate the buffer usage of a CDS view entity to the buffer of its base object, which can improve performance. |

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
<td><strong>Level-based Hierarchies</strong></td>
<td><p>A new variant of the <a href="abenhierarchy_generator_glosry.html">hierarchy generator</a> <a href="abenselect_hierarchy_generator.html"><code class="ph codeph">HIERARCHY</code></a> uses the addition <a href="abenselect_hierarchy_gen_level.html"><code class="ph codeph">LEVELS</code></a> in order to generate <a href="abenlevel_based_hiera_glosry.html">level-based hierarchies</a>. These allow access to hierarchical data in data sources that are defined by level columns.</p>
<p>In contrast, the former variant of <code class="ph codeph">HIERARCHY</code> uses the addition <a href="abenselect_hierarchy_gen_assoc.html"><code class="ph codeph">CHILD TO PARENT ASSOCIATION</code></a> in order to generate <a href="abenpc_based_hiera_glosry.html">parent-child-based hierarchies</a> from <a href="abenpcr_glosry.html">parent-child relationships</a>.</p></td>
</tr>
<tr class="even">
<td><strong>Enhancement of <code class="ph codeph">STRING_AGG</code> Function</strong></td>
<td>The optional separator <code class="ph codeph">sep</code> of the <a href="abensql_agg_func.html"><code class="ph codeph">STRING_AGG</code> function</a> can now be a host variable.</td>
</tr>
<tr class="odd">
<td><strong>Enhancement of <code class="ph codeph">LTRIM</code> and <code class="ph codeph">RTRIM</code> Functions</strong></td>
<td>The character <code class="ph codeph">char</code> of the <a href="abensql_string_func.html"><code class="ph codeph">LTRIM</code></a> and <a href="abensql_string_func.html"><code class="ph codeph">RTRIM</code></a> functions can now be a host variable or an SQL expression. Additionally, the length of <code class="ph codeph">char</code> can be other than 1.</td>
</tr>
<tr class="even">
<td><strong>Aggregate Functions Processed by the ABAP SQL In-Memory Engine</strong></td>
<td>The <a href="abensql_agg_func.html">aggregate functions</a> <code class="ph codeph">MIN</code>, <code class="ph codeph">MAX</code>, and <code class="ph codeph">SUM</code> can be processed by the <a href="abenabap_sql_inmemeng.html">ABAP SQL in-memory engine</a> in the <a href="abapselect_list.html"><code class="ph codeph">SELECT</code></a> list now. They no longer bypass <a href="abentable_buffering_glosry.html">table buffering</a> and do not cause the transport of an internal table accessed by <a href="abapselect_itab.html"><code class="ph codeph">FROM @itab</code></a> to the database.</td>
</tr>
<tr class="odd">
<td><strong>Spatial Functions</strong></td>
<td>SAP HANA constructors, methods, and functions for accessing and manipulating spatial data are now available as <a href="abensql_spatial_func.html">functions</a> in ABAP SQL.</td>
</tr>
<tr class="even">
<td><strong><code class="ph codeph">HIERARCHY_COMPOSITE_ID</code></strong></td>
<td>The function <a href="abensql_hierarchy_comp_id.html"><code class="ph codeph">HIERARCHY_COMPOSITE_ID</code></a> can be used to generate composite node identifiers free of name clashes.</td>
</tr>
</tbody>
</table>

## Expressions and Functions

| Modification                         | Description                                                                                                                                                                                                    |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Factorial and Binomial Functions** | The built-in function [`factorial`](../../abap-programming-language/abap-processing-internal-data/abenfactorial_functions.md) computes the factorial of positive integer values. The [`binomial`](../../abap-programming-language/abap-processing-internal-data/abenbinomial_functions.md) function computes the binomial coefficient. |

## ABAP RESTful Application Programming Model

In release 9.15, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

| Modification                                                                      | Description                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **RAP Type Mapping, Constants**                                                   | It is now possible to specify a fixed value on the left side of a [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) using the syntax [`constant`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_type_mapping.md). This can be useful, for example, in scenarios where different entities are mapped to the same underlying [RAP persistent table](../../abap-glossary/abenrap_persistent_table_glosry.md). |
| **RAP Feature Control Additions**                                                 | The new RAP feature control additions [`readonly:create`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_field_char.md) and [`mandatory:update`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_field_char.md) were released. The `field (readonly:create)` causes a certain field to be read-only in create requests whereas the `field (mandatory:update)` states that a field must not remain initial when editing.            |
| **RAP Business Objects: Feature Control and Authorization Support for Functions** | Instance-based feature control, global feature control, and authorization control are now supported for functions defined in RAP Business Object definitions (BDEFs), in addition to actions. See [RAP - function](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_function.md).                                                                                                              |
