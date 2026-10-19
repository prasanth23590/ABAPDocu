---
title: "response_param, Nondynamic Forms of ABAP EML Statements"
source_file: abapeml_responses.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > ABAP EML - Common EML Statements and Operands > ABAP EML - response_param"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# response_param, Nondynamic Forms of ABAP EML Statements

## Syntax

``` abap
... [FAILED failed_resp] 
    [MAPPED mapped_resp] 
    [REPORTED reported_resp] ...  
```

## Description

Used for [RAP responses](../../abap-glossary/abenrap_response_glosry.md) in the context of nondynamic (i. e. short or long) forms of ABAP EML statements such as [`MODIFY ENTITY`](abapmodify_entity_short.md) or [`MODIFY ENTITIES`](abapmodify_entities_long.md). All variants can be used together where possible. The operands `failed_resp`, `mapped_resp` and `reported_resp` after the respective ABAP word represent deep structures that must be typed with the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) [`TYPE RESPONSE FOR`](abaptype_response_for.md). These structures can be constructed inline using the declaration operators [`DATA`](../../abap-programming-language/abap-declarations/abendata_inline.md) and [`FINAL`](../../abap-programming-language/abap-declarations/abenfinal_inline.md).

The deep structures contain one internal table as a nested component for each entity of the RAP BO. Therefore, all information on all entities of a RAP BO can be retrieved at once.

The nested internal tables are of type [`TYPE TABLE FOR`](abaptype_table_for.md) (plus `EARLY` or `LATE` depending on the context) and comprise special components. The addition `EARLY` is the default, even if not explicitly specified. For example, if response parameters are explicitly declared with the type `TYPE RESPONSE FOR FAILED`, they automatically have the type `TYPE RESPONSE FOR FAILED EARLY`. The addition `LATE` is only possible if:

- [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) is defined for a RAP BO.

- the statement [`COMMIT ENTITIES RESPONSE OF`](abapemlcommit_entities_long.md) is used. The operands for storing the responses must be typed with the `LATE` addition.

The following overview shows the variants of the structured data type, its purpose as well as the nested internal tables that are themselves typed with a BDEF derived type and their special components. See the details on the components in the documentation for [Components of Derived Types](abapderived_types_comp.md).

<table>
<thead>
<tr class="header">
<th><strong>Types of Response Structures</strong></th>
<th><strong>Purpose</strong></th>
<th><strong>Types of Nested Internal Tables</strong></th>
<th><strong><a href="abapderived_types_comp.html">Components of Nested Internal Tables</a></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code class="ph codeph">TYPE RESPONSE FOR FAILED</code></p>
<p><code class="ph codeph">TYPE RESPONSE FOR FAILED EARLY</code></p>
<p><code class="ph codeph">TYPE RESPONSE FOR FAILED LATE</code></p></td>
<td>Used for logging instances for which an operation has failed during the interaction phase. If the addition <code class="ph codeph">LATE</code> is used, the logs are provided during the save phase.</td>
<td><p>Depending on the structured data type used, the nested internal tables are of the following types:</p>
<p><code class="ph codeph">TYPE TABLE FOR FAILED</code></p>
<p><code class="ph codeph">TYPE TABLE FOR FAILED EARLY</code></p>
<p><code class="ph codeph"> TYPE TABLE FOR FAILED LATE</code></p></td>
<td><p><code class="ph codeph">%action</code></p>
<p><code class="ph codeph">%assoc</code></p>
<p><code class="ph codeph">%cid</code></p>
<p><code class="ph codeph">%create</code></p>
<p><code class="ph codeph">%delete</code></p>
<p><code class="ph codeph">%fail</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%op</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p>
<p><code class="ph codeph">%update</code></p>
<p>In case of a table typed with the addition <code class="ph codeph">LATE</code>, <code class="ph codeph">%cid</code> is not available.</p>
<p>If <code class="ph codeph">late numbering</code> is defined for a BO, the component <code class="ph codeph">%pid</code> is available.</p>
<p>In case of a <a href="abendraft_rap_bo_glosry.html">draft-enabled BO</a>, the component <code class="ph codeph">%is_draft</code> is available.</p></td>
</tr>
<tr class="even">
<td><p><code class="ph codeph">TYPE RESPONSE FOR MAPPED</code></p>
<p><code class="ph codeph">TYPE RESPONSE FOR MAPPED EARLY</code></p>
<p><code class="ph codeph">TYPE RESPONSE FOR MAPPED LATE</code></p></td>
<td><p>For modify operations, internal tables are returned that map the key values of created instances to the provided content IDs (<code class="ph codeph">%cid</code>). All subsequent operations must use the mapped keys.</p>
<p>The mapping information is available in the interaction phase by default. <code class="ph codeph">%cid</code> is then mapped to the real key or to <code class="ph codeph">%pid</code>. The addition <code class="ph codeph">LATE</code> specifies that the mapping information is available only when saving. In the save phase, <code class="ph codeph">%pid</code> is mapped to the real key.</p></td>
<td><p>Depending on the structured data type used, the nested internal tables are of the following types:</p>
<p><code class="ph codeph">TYPE TABLE FOR MAPPED</code></p>
<p><code class="ph codeph">TYPE TABLE FOR MAPPED EARLY</code></p>
<p><code class="ph codeph"> TYPE TABLE FOR MAPPED LATE</code></p></td>
<td><p>Components of a table typed without an addition or with the addition <code class="ph codeph">EARLY</code>:</p>
<p><code class="ph codeph">%cid</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p>
<p>Components of a table typed with the addition <code class="ph codeph">LATE</code>:</p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pre</code></p>
<p><code class="ph codeph">%tmp</code></p>
<p>If <code class="ph codeph">late numbering</code> is defined for a BO, the component <code class="ph codeph">%pid</code> is available for all additions.</p>
<p>In case of a draft-enabled BO, the component <code class="ph codeph">%is_draft</code> is only available for <code class="ph codeph">EARLY</code>.</p></td>
</tr>
<tr class="odd">
<td><p><code class="ph codeph">TYPE RESPONSE FOR REPORTED</code></p>
<p><code class="ph codeph">TYPE RESPONSE FOR REPORTED EARLY</code></p>
<p><code class="ph codeph">TYPE RESPONSE FOR REPORTED LATE</code></p></td>
<td>Used for returning messages on specific instances, for example, for which failures occurred during the interaction phase. If the addition <code class="ph codeph">LATE</code> is used, the messages are provided during the save phase.</td>
<td><p>Depending on the structured data type used, the nested internal tables are of the following types:</p>
<p><code class="ph codeph">TYPE TABLE FOR REPORTED</code></p>
<p><code class="ph codeph">TYPE TABLE FOR REPORTED EARLY</code></p>
<p><code class="ph codeph">TYPE TABLE FOR REPORTED LATE</code></p></td>
<td><p><code class="ph codeph">%cid</code></p>
<p><code class="ph codeph">%element</code></p>
<p><code class="ph codeph">%global</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%msg</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%state_area</code></p>
<p><code class="ph codeph">%tky</code></p>
<p>In case of a table typed with the addition <code class="ph codeph">LATE</code>, <code class="ph codeph">%cid</code> is not available.</p>
<p>If <code class="ph codeph">late numbering</code> is defined for a BO, the component <code class="ph codeph">%pid</code> is available.</p>
<p>In case of a draft-enabled BO, the component <code class="ph codeph">%is_draft</code> is available.</p></td>
</tr>
</tbody>
</table>

See further information and rules on response parameters in implementations of the [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) in the Development Guide for the ABAP RESTful Application Programming Model, section [General RAP BO Implementation Contract](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/1040b81372d44ed38b07a409fa0e1769?version=sap_cross_product_abap).

## Executable Example

- The example [ABAP EML - Responses](abeneml_responses_abexa.md) demonstrates the RAP response parameters using modify operations to change a simple managed RAP BO.
