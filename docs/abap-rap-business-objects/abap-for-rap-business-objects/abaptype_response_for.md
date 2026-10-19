---
title: "TYPE RESPONSE FOR"
source_file: abaptype_response_for.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPE RESPONSE FOR

## Syntax

``` abap
... RESPONSE FOR { FAILED 
                 | MAPPED 
                 | REPORTED 
                   { [EARLY | LATE] } 
                   bdef } ...  
```

## Description

[BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) used for [RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md) and operands of [ABAP EML statements](abeneml.md) for the purpose of providing or storing [RAP responses](../../abap-glossary/abenrap_response_glosry.md).

The BDEF derived types with `TYPE RESPONSE FOR ...` are basically [deep structures](../../abap-glossary/abendeep_structure_glosry.md) containing one internal table as nested component for each entity of the RAP BO. Therefore, all information on all entities of a RAP BO can be provided and retrieved at once. `bdef` stands for the source name of a [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md). The addition `EARLY` applies to responses from within the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md); the addition `LATE` applies to responses in the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md).

**Where Used**

- The three predefined [formal parameters](../../abap-glossary/abenformal_parameter_glosry.md) of [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) and [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md) `mapped`, `failed` and `reported` - whose names are also reflected in the syntax here - are typed with these BDEF derived types.

  In [ABAP behavior pools](../../abap-glossary/abenbehavior_pool_glosry.md), the parameters of the said methods typed with this BDEF derived type are implicitly available. The following images show the F2 help information in [ADT](../../abap-glossary/abenadt_glosry.md) for a RAP handler method for which the response parameters have not been explicitly specified: `METHODS create FOR MODIFY`

  `IMPORTING entities FOR CREATE demo_unmanaged_root_2.` F2 help information in ADT: ![figure](images_type_response_for2.png) The parameters can also be explicitly specified. When specified explicitly, for example, for a RAP handler method that creates instances and that includes `... FOR MODIFY ... FOR CREATE ...`, the syntax can be as follows. Note that for the explicit declaration of the changing parameters, the generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) is used. At runtime, the typed parameters implicitly have the type `TYPE RESPONSE FOR ...`. `METHODS create FOR MODIFY`

  `IMPORTING entities FOR CREATE bdef`

  `CHANGING failed TYPE DATA mapped TYPE DATA reported TYPE DATA.`

- The operands following the `MAPPED`, `FAILED` and `REPORTED` additions of nondynamic forms of [ABAP EML statements](abeneml.md) are typed with these BDEF derived types. **Note:** The operands following these additions in dynamic ABAP EML statements are internal tables of type `ABP_BEHV_RESPONSE_TAB`, see [here](abapeml_responses_dyn.md). The operands store the RAP responses when an ABAP EML statement triggers the calling of a method in the behavior pool. One example is the internally created data object `f_resp` in the statement `MODIFY ENTITY ... FROM ... FAILED FINAL(f_resp) ...`.

- In ABAP programs, these BDEF derived types can also be used to declare data objects and types, for example, as follows:

  `DATA f TYPE RESPONSE FOR FAILED demo_managed_root.`

  `TYPES r TYPE RESPONSE FOR REPORTED demo_managed_root.`

  `DATA m TYPE RESPONSE FOR MAPPED demo_managed_root.`

**Details on the Syntax**

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

## Hint

The following image shows the *Variables* tab in the debug mode of [ADT](../../abap-glossary/abenadt_glosry.md). The variables `ls_report`, `ls_map` and `ls_fail` are typed with the structured data type `TYPE RESPONSE FOR`. Once expanded, the nested internal tables for each of the entities contained in the [composition tree](../../abap-glossary/abencds_composition_tree_glosry.md) of `DEMO_MANAGED_ROOT` are displayed. In this case, there are entries for one entity available. See the context of the image in the executable example [ABAP EML - `TYPE RESPONSE FOR`](abeneml_responses_2_abexa.md) that demonstrates the response parameters. ![figure](images_abdoc_eml_responses.png)

## More Information

See further information and rules on response parameters in implementations of the [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) in the Development guide for the ABAP RESTful Application Programming Model, section [General RAP BO Implementation Contract](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/1040b81372d44ed38b07a409fa0e1769?version=sap_cross_product_abap).

## Executable Example

- The example [ABAP EML - `TYPE RESPONSE FOR`](abeneml_responses_2_abexa.md) demonstrates the response parameters with a simple managed RAP BO. To show content for the responses, errors are intentionally produced in the context of an ABAP EML `MODIFY` statement trying to create new instances.

- The example [ABAP EML - Responses](abeneml_responses_abexa.md) demonstrates the response parameters using modify operations to change a simple managed RAP BO.
