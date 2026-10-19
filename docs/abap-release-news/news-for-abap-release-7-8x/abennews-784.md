---
title: "News for ABAP Release 7.84"
source_file: abennews-784.html
section: "ABAP Release News > News for ABAP Release 7.8x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.84

The kernel release for ABAP release 7.84 is 7.84.

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
<td><strong>CDS View Entity, Reusing Expressions</strong></td>
<td>In <a href="abencds_v2_view_glosry.html">CDS view entities</a>, it is now possible to reuse expressions defined in the <code class="ph codeph">SELECT</code> list in other operand positions of the same CDS view entity by using the syntax <a href="abencds_reusable_expression_v2.html"><code class="ph codeph">$projection.reuse_exp</code></a>.</td>
</tr>
<tr class="even">
<td><strong>CDS View Entity, Extended Expression Matrix</strong></td>
<td><p>In <a href="abencds_v2_view_glosry.html">CDS view entities</a>, the expression matrix has been extended:</p>
<ul>
<li>In the <a href="abencds_where_clause_v2.html"><code class="ph codeph">WHERE</code></a> clause, arithmetic expressions and case expressions are supported as operands.</li>
<li>In the <a href="abencds_having_clause_v2.html"><code class="ph codeph">HAVING</code></a> clause, arithmetic expressions and case expressions are supported as operands.</li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>CDS Abstract Entity Extensions</strong></td>
<td>The new statement <a href="abencds_extend_abstract_entity.html"><code class="ph codeph">EXTEND ABSTRACT ENTITY</code></a> of the DDL of ABAP CDS makes it possible to add new elements to existing <a href="abencds_abstract_entity_glosry.html">CDS abstract entities</a> by using <a href="abencds_abs_entity_extend_glosry.html">CDS abstract entity extensions</a>.</td>
</tr>
<tr class="even">
<td><strong>CDS View Entity, Handling of Amounts and Quantities</strong></td>
<td><p>In <a href="abencds_v2_view_glosry.html">CDS view entities</a>, special handling for <a href="abencds_amount_field.html">CDS amount fields</a> and <a href="abencds_quantity_field.html">CDS quantity fields</a> has been implemented. It differs from the handling of amount fields and quantity fields in DDIC, for example, more data types are possible and the currency key/unit key reference is considered in expressions.</p>
<p>Moreover, a new type is available: the <a href="abencds_calculated_quantity.html">CDS calculated quantity</a>. A CDS calculated quantity is the result type of a calculation using amount and/or quantity fields.</p></td>
</tr>
</tbody>
</table>

## Data Types

| Modification                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Condensed Indicator Structures** | The new addition [`AS BITFIELD`](../../abap-programming-language/abap-declarations/abaptypes_indicators.md) behind addition [`INDICATORS`](../../abap-programming-language/abap-declarations/abaptypes_indicators.md) of the statement [`TYPES`](../../abap-programming-language/abap-declarations/abaptypes.md) allows a [condensed indicator structure](../../abap-glossary/abencondensed_ind_structure_glosry.md) to be defined as a [byte field type](../../abap-glossary/abenbyte_field_type_glosry.md) component of a given [structured type](../../abap-glossary/abenstructured_type_glosry.md). An condensed indicator structure can be used as a [null indicator](../../abap-glossary/abennull_indicator_glosry.md) in ABAP SQL statements. |

## Data References

| Modification                      | Description                                                                                                                                                                                                                  |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Dereferencing Data References** | The [dereferencing operator`->*`](../../abap-programming-language/abap-operands/abendereferencing_operator.md) can be used for generically typed data reference variables in almost all operand positions now. Before, that was possible in the `ASSIGN` statement only. |

## Byte String Processing

| Modification                         | Description                                                                                                                                                  |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Writable Expression in `SET BIT`** | For the operand `byte_string` of statement [`SET BIT`](../../abap-programming-language/abap-processing-internal-data/abapset_bit.md), a [writable expression](../../abap-glossary/abenwritable_expression_glosry.md) can be specified now. |

## ABAP SQL

| Modification                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Addition for the String Function `REPLACE_REGEXPR`** | The new parameter `start` can now be used in the function [`REPLACE_REGEXPR`](../../abap-programming-language/abap-database-access/abensql_string_func.md). Additionally, the parameter `occurrence` can now include [expressions](../../abap-glossary/abenexpression_glosry.md).                                                                                                                                                                                                                                                                                                                                                                  |
| **New String Function `SUBSTRING_REGEXPR`**            | ABAP SQL now supports the new string function [`SUBSTRING_REGEXPR`](../../abap-programming-language/abap-database-access/abensql_string_func.md) which supports regular expressions.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Byte Fields as Null Indicators**                     | The new addition [`INDICATORS ... NULL BITFIELD`](../../abap-programming-language/abap-database-access/abapselect_indicators.md) of the `INTO` clause of a `SELECT` statement allows a [byte field type](../../abap-glossary/abenbyte_field_type_glosry.md) component to be specified as a [null indicator](../../abap-glossary/abennull_indicator_glosry.md). The single bits of the byte field serve for indicating null values in the result set of the query. For this purpose, [condensed indicator structures](../../abap-glossary/abencondensed_ind_structure_glosry.md) can be declared with the addition [`AS BITFIELD`](../../abap-programming-language/abap-declarations/abaptypes_indicators.md) of the `TYPES` statement. |
| **Position of Null Indicators**                        | If `CORRESPONDING FIELDS` is used in the [`INTO`](../../abap-programming-language/abap-database-access/abapinto_clause.md) clause of a `SELECT` statement, a [null indicator](../../abap-glossary/abennull_indicator_glosry.md) defined by [`INDICATORS`](../../abap-programming-language/abap-database-access/abapselect_indicators.md) can be positioned anywhere in the target area. Otherwise, it must be the last component.                                                                                                                                                                                                                                                                     |

## ABAP RESTful Application Programming Model

In release 7.84, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

| Modification                                   | Description                                                                                                                                                                                                                                                         |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BDEF Strict Mode**                           | [BDEF strict mode](../../abap-glossary/abenrap_strict_mode_glosry.md) is now available. It can be enabled using the syntax addition [`strict`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_strict_1.md) and it applies additional syntax checks to [RAP behavior definitions](../../abap-glossary/abencds_behavior_definition_glosry.md). |
| **Projection BDEF, New Actions and Functions** | It is now possible to define and implement [new actions and functions](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_nonstandard_projection.md) in a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md).                                                                                                  |
| **Projection BDEF, Authorization Concept**     | It is now possible to define an [authorization concept](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_authorization_projection.md) in a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md) that controls access to the newly defined actions and functions in a projection BDEF.                          |
| **Projection BDEF, Augmented Fields**          | [Field characteristics](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_field_projection.md) can be specified for [augmented fields](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_augment_projection.md) in a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md).                                                                              |
| **Projection BDEF, New Field Characteristic**  | In [projection BDEFs](../../abap-glossary/abencds_proj_bdef_glosry.md), a new field characteristic is available: [`field(suppress)`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_field_projection.md). It removes the field in question from the BDEF derived types and all RAP APIs.                                   |

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
<td><p>ABAP EML keywords are now available as part of the ABAP Keyword Documentation. The following keywords and topics are covered among others:</p>
<ul>
<li><p><a href="abapmodify_entity_entities.html"><code class="ph codeph">MODIFY ...</code></a></p>
<p><code class="ph codeph">MODIFY ENTITY</code></p>
<p><code class="ph codeph">MODIFY ENTITIES</code></p>
<p><code class="ph codeph">MODIFY ENTITIES OPERATIONS</code></p></li>
<li><p><a href="abapread_entity_entities.html"><code class="ph codeph">READ ...</code></a></p>
<p><code class="ph codeph">READ ENTITY</code></p>
<p><code class="ph codeph">READ ENTITIES</code></p>
<p><code class="ph codeph">READ ENTITIES OPERATIONS</code></p></li>
<li><p><a href="abapcommit_entities.html"><code class="ph codeph">COMMIT ENTITIES ...</code></a></p>
<p><code class="ph codeph">COMMIT ENTITIES</code></p>
<p><code class="ph codeph">COMMIT ENTITIES RESPONSE OF</code></p>
<p><code class="ph codeph">COMMIT ENTITIES RESPONSES OF</code></p>
<p><code class="ph codeph">COMMIT ENTITIES BEGIN, END</code> including <code class="ph codeph">CONVERT KEY OF</code></p></li>
<li><a href="abaprollback_entities.html"><code class="ph codeph">ROLLBACK ENTITIES</code></a></li>
<li><p><a href="abapset_locks.html"><code class="ph codeph">GET PERMISSIONS ...</code></a></p>
<p><code class="ph codeph">GET PERMISSIONS</code></p>
<p><code class="ph codeph">GET PERMISSIONS OF</code></p>
<p><code class="ph codeph">GET PERMISSIONS OPERATIONS</code></p></li>
<li><p><a href="abapset_locks.html"><code class="ph codeph">SET LOCKS ...</code></a></p>
<p><code class="ph codeph">SET LOCKS ENTITY</code></p>
<p><code class="ph codeph">SET LOCKS OF</code></p>
<p><code class="ph codeph">SET LOCKS</code> (dynamic form)</p></li>
<li><p><a href="abapeml_type_mapping.html">Type Mapping for RAP</a></p>
<p><code class="ph codeph">SET NAMES</code></p>
<p><code class="ph codeph">SET FLAGS</code></p>
<p>RAP-specific variants of the <code class="ph codeph">CORRESPONDING</code> operator</p></li>
</ul></td>
</tr>
</tbody>
</table>

### BDEF Derived Types

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>BDEF Derived Types</strong></td>
<td><p><a href="abenrap_derived_type_glosry.html">BDEF derived types</a> are now available as part of the ABAP keyword documentation. The following keywords and topics are covered:</p>
<ul>
<li><a href="abaptype_table_for.html"><code class="ph codeph">TYPE TABLE FOR</code></a></li>
<li><a href="abaptype_structure_for.html"><code class="ph codeph">TYPE STRUCTURE FOR</code></a></li>
<li><a href="abaptype_response_for.html"><code class="ph codeph">TYPE RESPONSE FOR</code></a></li>
<li><a href="abaptype_request_for.html"><code class="ph codeph">TYPE REQUEST FOR</code></a></li>
<li><a href="abapderived_types_comp.html">Components of BDEF Derived Types</a></li>
<li><a href="abapderived_types_declaration.html">Declaration of Variables with BDEF Derived Types</a></li>
</ul></td>
</tr>
</tbody>
</table>
