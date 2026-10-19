---
title: "XSL - SAP Functions"
source_file: abenabap_sap_fnctns.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > XSL Transformations > XSL - User-Defined Transformations > XSL - Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# XSL - SAP Functions

In the following, enhanced SAP-specific functions of the [SAP XSLT processor](abenabap_xslt_processor.md) are listed. The URI for the SAP namespace is `http://www.sap.com/sapxsl`.

## Numeric Functions

| **Function**        | **XPath Function** | **Description**                                     |
|---------------------|--------------------|-----------------------------------------------------|
| `sap:abs(number)`   | `abs()`            | Returns the absolute value of the number.           |
| `sap:exp(number)`   | \-                 | Returns the result of the exponential function.     |
| `sap:log(number)`   | \-                 | Returns the result of the natural logarithm.        |
| `sap:log10(number)` | \-                 | Returns the result of the decimal logarithm.        |
| `sap:sqrt(number)`  | \-                 | Returns the square root of the number.              |
| `sap:sin(number)`   | \-                 | Returns the result of the sine function.            |
| `sap:cos(number)`   | \-                 | Returns the result of the cosine function.          |
| `sap:tan(number)`   | \-                 | Returns the result of the tangent function.         |
| `sap:asin(number)`  | \-                 | Returns the result of the inverse sine function.    |
| `sap:acos(number)`  | \-                 | Returns the result of the inverse cosine function.  |
| `sap:atan(number)`  | \-                 | Returns the result of the inverse tangent function. |

## String Functions

<table>
<thead>
<tr class="header">
<th><strong>Function</strong></th>
<th><strong>XPath Function</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">sap:upper-case(string)</code></td>
<td><code class="ph codeph">upper-case()</code></td>
<td>Converts the string to upper-case letters.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">sap:lower-case(string)</code></td>
<td><code class="ph codeph">lower-case()</code></td>
<td>Converts the string to lower-case letters.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">sap:string-pad(string, number)</code></td>
<td>-</td>
<td>Returns the string as many times as the number represents.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">sap:ends-with(string, string)</code></td>
<td><code class="ph codeph">ends-with()</code></td>
<td><p>Returns true if the first string ends with the second string. Otherwise, it returns false.</p>
<p><strong>Note:</strong> Parameters as part of the collation URI are not supported.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">sap:find-first(string, string[, number])</code></td>
<td>-</td>
<td>Returns the first occurrence of the second string in the first string. If a number is specified, the search only starts at this position.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">sap:find-last(string, string[, number])</code></td>
<td>-</td>
<td>Returns the last occurrence of the second string in the first string. If a number is specified, the search ends at this position.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">sap:find-first-of(string, string[, number])</code></td>
<td>-</td>
<td>Returns the first occurrence of a character in the second string in the first string. If a number is specified, the search only starts at this position.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">sap:find-first-not-of(string, string[, number])</code></td>
<td>-</td>
<td>Returns the first occurrence of a character not in the second string in the first string. If a number is specified, the search only starts at this position.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">sap:find-last-of(string, string[, number])</code></td>
<td>-</td>
<td>Returns the last occurrence of a character in the second string in the first string. If a number is specified, the search ends at this position.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">sap:find-last-not-of(string, string[, number])</code></td>
<td>-</td>
<td>Returns the last occurrence of a character not in the second string in the first string. If a number is specified, the search ends at this position.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">sap:escape-uri(string)</code></td>
<td><code class="ph codeph">escape-uri()</code></td>
<td>Returns the URI unchanged.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">sap:resolve-uri(string, string)</code></td>
<td><code class="ph codeph">resolve-uri()</code></td>
<td>Resolves a relative URI reference against an absolute URI. The first string contains the base URI and the second string contains the relative URI.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">sap:tokenize(string[, string, string])</code></td>
<td><code class="ph codeph">tokenize()</code></td>
<td>Returns a node set by splitting the first string at the separator defined in a regular expression. If no second argument is given, the separator is a single space character. The third argument defines a flag to set options the regular expression interpretation.</td>
</tr>
</tbody>
</table>

## Node Set Functions

<table>
<thead>
<tr class="header">
<th><strong>Function</strong></th>
<th><strong>XSLT Function</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">sap:min(number\|node-set, number\|node-set)</code></td>
<td>-</td>
<td>Returns the minimum of two numbers or the minimum of the numerical values of a node set.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">sap:max(number\|node-set, number\|node-set)</code></td>
<td>-</td>
<td>Returns the maximum of two numbers or the maximum of the numerical values of a node set.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">sap:node-set(fragment)</code></td>
<td>-</td>
<td>Obsolete. Converts a fragment of the result tree into a node set. The resulting node set contains its own node, which is the fragment root.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">sap:intersection(node-set, node-set)</code></td>
<td>-</td>
<td><p>Returns the intersection of two node sets.</p>
<p><strong>Example:</strong> <code class="ph codeph">sap:intersection(node-set1, node-set2)</code> returns the intersection of the two node sets <code class="ph codeph">node-set1</code> and <code class="ph codeph">node-set2</code>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">sap:document()</code></td>
<td><a href="abenabap_xslt_fnctns.html"><code class="ph codeph">document()</code></a></td>
<td>Allows access to external XML documents.</td>
</tr>
</tbody>
</table>

## Functions for the Online Text Repository

XSLT can be used to read texts of the [Online Text Repository (OTR)](../abap-text-repositories/abenabap_texts.md) and make output of XSLT programs multilingual.

<table>
<thead>
<tr class="header">
<th><strong>Function</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">sap:otr-string()</code></td>
<td><p>Returns OTR strings. An alias name is used to identify a string. There are three variants:</p>
<p><code class="ph codeph">sap:otr-string(alias)</code> returns OTR strings for an alias in the current language.</p>
<p><code class="ph codeph">sap:otr-string(alias, language)</code> returns OTR strings for an alias in the specified language.</p>
<p><code class="ph codeph">sap:otr-string(alias, id_1, value_1, ..., id_n, value_n[, language])</code> returns OTR strings for an alias in the current or specified language. The corresponding placeholder <code class="ph codeph">id_i</code> is replaced by the appropriate value <code class="ph codeph">value_i</code>. A placeholder is specified either as a string (reference by name) or as a number (reference by position).</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">sap:otr-text()</code></td>
<td>Returns short texts from the OTR. An alias name is used to identify a short text (<code class="ph codeph">sap:otr-text(alias, ...)</code>). In the case of <code class="ph codeph">sap:otr-string()</code>, the language and placeholder can be specified as further function arguments.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">sap:otr-line()</code></td>
<td><p>Returns the line number of the node from the current context.</p>
<p><strong>Example:</strong> <code class="ph codeph">sap:otr-line(node-set)</code> returns the line number of the first node of the node set in the source document.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">sap:otr-column()</code></td>
<td><p>Returns the column number of the node from the current context.</p>
<p><strong>Example:</strong> <code class="ph codeph">sap:otr-column(node-set)</code> returns the column number of the first node of the node set in the source document.</p></td>
</tr>
</tbody>
</table>

## More Functions

<table>
<thead>
<tr class="header">
<th><strong>Function</strong></th>
<th><strong>XPath Function</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">sap:if(object, object, object)</code></td>
<td><code class="ph codeph">if()</code></td>
<td><p>Returns the second object if the first object is true. Otherwise, it returns the third object.</p>
<p><strong>Example:</strong> The function <code class="ph codeph">sap:if(x, e1, e2)</code> returns <code class="ph codeph">e1</code> if <code class="ph codeph">x=true</code>; else <code class="ph codeph">e2</code>.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">sap:let(object, object, object)</code></td>
<td>-</td>
<td><p>Displays the syntax of an extension function, but it is used as a construct for a variable bind. <code class="ph codeph">sap:let(x, e1, e2)</code> binds <code class="ph codeph">$x</code> to <code class="ph codeph">e1</code> in <code class="ph codeph">e2</code>.</p>
<p><strong>Example:</strong> <code class="ph codeph">sap:let(x, 4, $x + $x)</code> returns <code class="ph codeph">8</code>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">sap:timestamp()</code></td>
<td>-</td>
<td>Returns an <a href="abenutc_timestamp_glosry.html">UTC time stamp</a> according to the <a href="abenposix_timestamp_glosry.html">POSIX standard</a>.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">sap:date()</code></td>
<td>-</td>
<td>Returns the date.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">sap:line([node-set])</code></td>
<td>-</td>
<td>Returns the line.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">sap:last-line([node-set])</code></td>
<td>-</td>
<td>Returns the last line.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">sap:column([node-set])</code></td>
<td>-</td>
<td>Returns the column.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">sap:object-available(string)</code></td>
<td>-</td>
<td>Returns true if the specified object is available. Otherwise, it returns false.</td>
</tr>
</tbody>
</table>
