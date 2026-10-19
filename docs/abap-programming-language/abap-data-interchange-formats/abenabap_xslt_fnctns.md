---
title: "XSL - XSLT Functions"
source_file: abenabap_xslt_fnctns.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > XSL Transformations > XSL - User-Defined Transformations > XSL - Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# XSL - XSLT Functions

In the following, supported and not supported XSLT functions of the [SAP XSLT processor](abenabap_xslt_processor.md) are listed. The URI for the XSLT namespace is `http://www.w3.org/1999/XSL/Transform`.

## Supported Functions

<table>
<thead>
<tr class="header">
<th><strong>Function</strong></th>
<th><strong>XSLT Version</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">document(object[, node-set])</code></td>
<td>1.0</td>
<td><p>Allows access to external XML documents.</p>
<p><strong>Note:</strong> The function is only supported for arguments other than node set. Relative URLs are not expanded. It is possible to reference the root of the style sheet document using <code class="ph codeph">document("")</code>.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">key(string, object)</code></td>
<td>1.0</td>
<td>Selects elements by their key.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">current()</code></td>
<td>1.0</td>
<td>Returns the current node.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">generate-id([node-set])</code></td>
<td>1.0</td>
<td>Returns a string that uniquely identifies a node in the node set.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">system-property(string)</code></td>
<td>1.0</td>
<td>Returns an object with the value of the system properties. Otherwise, it returns an empty string.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">element-available(string)</code></td>
<td>1.0</td>
<td>Returns true if the expanded name is the name of an instruction. Returns false if the expanded name has a null namespace URI.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">function-available(string)</code></td>
<td>1.0</td>
<td>Returns true if the expanded name is the name of a function.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">format-number(number, string[, string])</code></td>
<td>1.0</td>
<td>Converts the number to a string using the format pattern in the first string and the decimal-format in the second string.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">current-group()</code></td>
<td>2.0</td>
<td>Returns the current group while evaluating a <code class="ph codeph">for-each-group</code> instruction.</td>
</tr>
</tbody>
</table>

## Not Supported Functions

- `unparsed-entity-uri()`
