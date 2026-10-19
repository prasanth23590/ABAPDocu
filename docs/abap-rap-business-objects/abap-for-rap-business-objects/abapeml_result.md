---
title: "ABAP EML - RESULT result_tab"
source_file: abapeml_result.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > ABAP EML - Common EML Statements and Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - RESULT result_tab

## Syntax

``` abap
... RESULT result_tab ...  
```

## Description

Used to store results of the following operations in an internal table `result_tab`:

- All [`READ`](abapread_entity_entities_op.md) operations.

- A [`MODIFY`](abapmodify_entity_entities.md) operation executing an [action](../../abap-glossary/abenrap_action_glosry.md).

The internal table `result_tab` must be typed with a specific [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) depending on the operation performed. The use of `RESULT` is mandatory for all operations except for the modify operation executing an action.

The internal tables comprise nested structures that contain special components. See the details on the components in the documentation for [Components of Derived Types](abapderived_types_comp.md).

The following table provides an overview on those operations that offer a result, their BDEF derived type, and the relevant components for the internal tables:

<table>
<thead>
<tr class="header">
<th><strong>Context</strong></th>
<th><strong>Types</strong></th>
<th><strong>Possible <a href="abapderived_types_comp.html">Components</a> of Structures in Internal Table <code class="ph codeph">result_tab</code></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abapread_entity_entities.html"><code class="ph codeph">READ</code></a> operations (excluding <a href="abenbdl_function.html">functions</a>)</td>
<td><code class="ph codeph">TABLE FOR READ RESULT bdef[\_assoc]</code></td>
<td><p><code class="ph codeph">%data</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
<tr class="even">
<td><a href="abapread_entity_entities.html"><code class="ph codeph">READ</code></a> operations executing functions (<code class="ph codeph">READ ... EXECUTE</code>)</td>
<td><code class="ph codeph">TABLE FOR FUNCTION RESULT bdef~function</code></td>
<td><p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%param</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
<tr class="odd">
<td><a href="abapmodify_entity_entities.html"><code class="ph codeph">MODIFY</code></a> operations executing an action (<code class="ph codeph">MODIFY ... EXECUTE</code>)</td>
<td><code class="ph codeph">TABLE FOR ACTION RESULT bdef~action</code></td>
<td><p><code class="ph codeph">%cid_ref</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%param</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
</tbody>
</table>

## Hint

Additional components are possible for all contexts: If [late numbering](../../abap-glossary/abenrap_late_numbering_glosry.md) is defined for a BO, the component `%pid` is available. In case of a draft-enabled BO, the component `%is_draft` is available.
