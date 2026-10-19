---
title: "XSL - XSLT Instructions"
source_file: abenabap_xslt_instr.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > XSL Transformations > XSL - User-Defined Transformations > XSL - Instructions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# XSL - XSLT Instructions

In the following, supported and not supported XSLT instructions of the [SAP XSLT processor](abenabap_xslt_processor.md) are listed. The URI for the XSLT namespace is `http://www.w3.org/1999/XSL/Transform`.

## Top-level Elements

<table>
<thead>
<tr class="header">
<th><strong>Element</strong></th>
<th><strong>Attributes</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">xsl:key</code></td>
<td><p><code class="ph codeph">name</code></p>
<p><code class="ph codeph">match</code></p>
<p><code class="ph codeph">use</code></p></td>
<td>Declares keys.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsl:import</code></td>
<td><code class="ph codeph">href</code></td>
<td>See below.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">xsl:include</code></td>
<td><code class="ph codeph">href</code></td>
<td>See below.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsl:output</code></td>
<td><p><code class="ph codeph">method</code></p>
<p><code class="ph codeph">version</code></p>
<p><code class="ph codeph">encoding</code></p>
<p><code class="ph codeph">omit-xml-declaration</code></p>
<p><code class="ph codeph">standalone</code></p>
<p><code class="ph codeph">doctype-public</code></p>
<p><code class="ph codeph">doctype-system</code></p>
<p><code class="ph codeph">cdata-section-elements</code></p>
<p><code class="ph codeph">indent</code></p>
<p><code class="ph codeph">media-type</code></p></td>
<td><p>Specifies how the result tree is output.</p>
<p><strong>Note:</strong> The <code class="ph codeph">cdata-section-elements</code> attribute is not supported.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">xsl:param</code></td>
<td><p><code class="ph codeph">name</code></p>
<p><code class="ph codeph">select</code></p></td>
<td><p>Binds a variable to a default value.</p>
<p><strong>Note:</strong> XSLT types can be assigned to a parameter using the <code class="ph codeph">sap:type</code> attribute. The following values can be used: <code class="ph codeph">string</code>, <code class="ph codeph">number</code>, <code class="ph codeph">boolean</code>, <code class="ph codeph">node-set</code>, <code class="ph codeph">external</code>, and <code class="ph codeph">xstring</code>. A type conversion is triggered in ABAP. Example: In ABAP, a date is passed as string <em>'2001-05-16'</em>. The parameter declaration in XSLT is <code class="ph codeph">xsl:param name="p" sap:type="number"</code>. The date is first converted to a number in ABAP (number of days from <em>0001-01-01</em>). The number is then passed to the XSLT program.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsl:preserve-space</code></td>
<td><code class="ph codeph">elements</code></td>
<td>Adds an element to the set of whitespace-preserving element names.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">xsl:strip-space</code></td>
<td><code class="ph codeph">elements</code></td>
<td>Removes an element from the set of whitespace-preserving element names.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsl:template</code></td>
<td><p><code class="ph codeph">match</code></p>
<p><code class="ph codeph">name</code></p>
<p><code class="ph codeph">priority</code></p>
<p><code class="ph codeph">mode</code></p></td>
<td>See below.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">xsl:variable</code></td>
<td><p><code class="ph codeph">name</code></p>
<p><code class="ph codeph">select</code></p></td>
<td>See below.</td>
</tr>
</tbody>
</table>

## Template Elements

### Creating the Result Tree

<table>
<thead>
<tr class="header">
<th><strong>Element</strong></th>
<th><strong>Attributes</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">xsl:attribute</code></td>
<td><p><code class="ph codeph">name</code></p>
<p><code class="ph codeph">namespace</code></p></td>
<td>Adds an attribute to a result element.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsl:comment</code></td>
<td>-</td>
<td>Creates a comment node in the result tree.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">xsl:copy</code></td>
<td><code class="ph codeph">use-attribute-sets</code></td>
<td><p>Copies the current node without attributes and child nodes.</p>
<p><strong>Note:</strong> The <code class="ph codeph">use-attributes-sets</code> attribute is not supported.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsl:copy-of</code></td>
<td><code class="ph codeph">select</code></td>
<td>Inserts a result tree fragment into the result tree.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">xsl:element</code></td>
<td><p><code class="ph codeph">name</code></p>
<p><code class="ph codeph">namespace</code></p>
<p><code class="ph codeph">use-attribute-sets</code></p></td>
<td><p>Creates an element node in the result tree.</p>
<p><strong>Note:</strong> The <code class="ph codeph">use-attributes-sets</code> attribute is not supported.</p>
<p>The element name <em>QName</em> is not validated.</p>
<p>Namespace declarations are not necessarily copied to the result tree. If a namespace attribute is specified in the element instruction, no namespace node is created in the result tree unless a URI must be declared. If the namespace attribute contains a prefix, it is not necessarily used. If a namespace attribute is not specified in the element instruction, all namespace declarations are copied to the created element in the result tree. A prefix specified in the namespace attribute is also used in the result node.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsl:processing-instruction</code></td>
<td><code class="ph codeph">name</code></td>
<td>Creates a processing instruction node.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">xsl:text</code></td>
<td><code class="ph codeph">disable-output-escaping</code></td>
<td>Writes literal data characters.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsl:value-of</code></td>
<td><p><code class="ph codeph">select</code></p>
<p><code class="ph codeph">disable-output-escaping</code></p></td>
<td>Creates a text node in the result tree.</td>
</tr>
</tbody>
</table>

### Flow Control

<table>
<thead>
<tr class="header">
<th><strong>Element</strong></th>
<th><strong>Attributes</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">xsl:choose</code></td>
<td>-</td>
<td>Selects one alternative. It is used with a sequence of <code class="ph codeph">xsl:when</code> elements and an optional <code class="ph codeph">xsl:otherwise</code> element.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsl:for-each</code></td>
<td><code class="ph codeph">select</code></td>
<td>Specifies a template for each selected node.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">xsl:if</code></td>
<td><code class="ph codeph">test</code></td>
<td>Contains a template that is instantiated if the evaluated expression is true.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsl:otherwise</code></td>
<td>-</td>
<td>Specifies a default content template.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">xsl:sort</code></td>
<td><p><code class="ph codeph">select</code></p>
<p><code class="ph codeph">lang</code></p>
<p><code class="ph codeph">data-type</code></p>
<p><code class="ph codeph">order</code></p>
<p><code class="ph codeph">case-order</code></p></td>
<td><p>Sorts the output structure.</p>
<p><strong>Note:</strong> The <code class="ph codeph">lang</code> attribute is ignored.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsl:variable</code></td>
<td><p><code class="ph codeph">name</code></p>
<p><code class="ph codeph">select</code></p></td>
<td><p>Binds a variable to a value.</p>
<p><strong>Note:</strong> The instruction <code class="ph codeph">xsl:variable name="x"</code> within the scope of another variable declaration of <em>x</em> can cause a syntax error. <em>x</em> can still be referenced after it is bound and if it is outside of its scope. The following is allowed:</p>
<p><code class="ph codeph"> &lt;A&gt;&lt;xsl:variable name="x" select="..."/&gt;&lt;/A&gt;</code></p>
<p><code class="ph codeph">&lt;xsl:value-of select="$x"/&gt;</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">xsl:when</code></td>
<td><code class="ph codeph">test</code></td>
<td>Selects the first content template of a test that is true.</td>
</tr>
</tbody>
</table>

### Defining and Calling Template Rules

<table>
<thead>
<tr class="header">
<th><strong>Element</strong></th>
<th><strong>Attributes</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">xsl:apply-templates</code></td>
<td><p><code class="ph codeph">select</code></p>
<p><code class="ph codeph">mode</code></p></td>
<td>Processes selected nodes.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsl:call-template</code></td>
<td><code class="ph codeph">name</code></td>
<td>Calls a specified template.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">xsl:param</code></td>
<td><p><code class="ph codeph">name</code></p>
<p><code class="ph codeph">select</code></p></td>
<td>Binds a variable to a default value.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsl:template</code></td>
<td><p><code class="ph codeph">match</code></p>
<p><code class="ph codeph">name</code></p>
<p><code class="ph codeph">priority</code></p>
<p><code class="ph codeph">mode</code></p></td>
<td><p>Defines a template rule.</p>
<p><strong>Note:</strong> In addition to patterns in the specification, appropriate match patterns are accepted. Example: <code class="ph codeph">(A\|B)/C</code>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">xsl:with-param</code></td>
<td><p><code class="ph codeph">name</code></p>
<p><code class="ph codeph">select</code></p></td>
<td>Passes a parameter to a template and replaces the value of the variable binding.</td>
</tr>
</tbody>
</table>

### Style Sheets and Structuring

<table>
<thead>
<tr class="header">
<th><strong>Element</strong></th>
<th><strong>Attributes</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">xsl:apply-imports</code></td>
<td>-</td>
<td><p>Processes the current node and applies the template rule of the imported stylesheet.</p>
<p><strong>Note:</strong> Parameters can be passed to the called template in the same way as for <code class="ph codeph">xsl:apply-templates</code> using <code class="ph codeph">xsl:with-param</code>.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsl:import</code></td>
<td><code class="ph codeph">href</code></td>
<td><p>Imports another XSLT stylesheet.</p>
<p><strong>Note:</strong> Import units are defined as nodes in the import tree. The relationship <em>imports to</em> is defined between the import units through the (transitive) relationship in the import tree.</p>
<p>Example: <em>Program Y</em> is imported into <em>program X</em> if the import unit of <em>program Y</em> was imported into the import unit of <em>program X</em>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">xsl:include</code></td>
<td><code class="ph codeph">href</code></td>
<td><p>Includes another XSLT stylesheet.</p>
<p><strong>Note:</strong> The inclusion uses the name of the repository instead of a URL. The name is specified in the <code class="ph codeph">sap:name</code> attribute. The <code class="ph codeph">href</code> attribute no longer applies in this case.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">xsl:stylesheet</code></td>
<td><p><code class="ph codeph">id</code></p>
<p><code class="ph codeph">extension-element-prefixes</code></p>
<p><code class="ph codeph">exclude-result-prefixes</code></p>
<p><code class="ph codeph">version</code></p></td>
<td><p>Represents a stylesheet.</p>
<p><strong>Note:</strong> The <code class="ph codeph">extension-element-prefixes</code> attribute is not supported.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">xsl:transform</code></td>
<td><p><code class="ph codeph">id</code></p>
<p><code class="ph codeph">extension-element-prefixes</code></p>
<p><code class="ph codeph">exclude-result-prefixes</code></p>
<p><code class="ph codeph">version</code></p></td>
<td>Synonym for <code class="ph codeph">xsl:stylesheet</code>.</td>
</tr>
</tbody>
</table>

### Output

| **Element**   | **Attributes** | **Description**                   |
|---------------|----------------|-----------------------------------|
| `xsl:message` | `terminate`    | Sends a message to report errors. |

## Not Supported Elements

| **Element**           | **Alternative**                                               |
|-----------------------|---------------------------------------------------------------|
| `xsl:attribute-set`   | Use the `xsl:attribute` element or literal result attributes. |
| `xsl:decimal-format`  | Use the `position()` function or a parameter as a counter.    |
| `xsl:fallback`        | \-                                                            |
| `xsl:namespace-alias` | Use the `xsl:element` element.                                |
| `xsl:number`          | Use the `position()` function or a parameter as a counter.    |
