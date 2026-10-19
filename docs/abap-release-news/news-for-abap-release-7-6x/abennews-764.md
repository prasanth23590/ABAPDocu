---
title: "News for ABAP Release 7.64"
source_file: abennews-764.html
section: "ABAP Release News > News for ABAP Release 7.6x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.64

The kernel release for ABAP release 7.64 is 7.48.

## ABAP SQL

| Modification             | Description                                                                                                                                                                                                                                                                                      |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SQL Functions**        | In the string functions [`INSTR`](../../abap-programming-language/abap-database-access/abensql_string_func.md), [`LPAD`](../../abap-programming-language/abap-database-access/abensql_string_func.md), [`LTRIM`](../../abap-programming-language/abap-database-access/abensql_string_func.md), [`RPAD`](../../abap-programming-language/abap-database-access/abensql_string_func.md), and [`RTRIM`](../../abap-programming-language/abap-database-access/abensql_string_func.md), arguments passed as constants or literals can now contain special characters. |
| **Restrictions Removed** | The components of a [replacement object](../../abap-glossary/abenreplacement_object_glosry.md) must no longer be in the same order as the associated components of the replaced database table or DDIC view.                                                                                                       |

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
<td><strong>Client Handling</strong></td>
<td>The new annotation <code class="ph codeph">@ClientHandling</code> specifies the client handling of <a href="abencds_view_client_handling_v1.html">CDS views</a> and <a href="abencds_func_client_handling.html">CDS table functions</a>. It replaces the annotation <code class="ph codeph">@ClientDependent</code> and makes it obsolete.</td>
</tr>
<tr class="even">
<td><strong>Expressions and Functions</strong></td>
<td><p>The following enhancements have been implemented:</p>
<ul>
<li>In a <a href="abencds_cast_expression_v1.html"><code class="ph codeph">CAST</code> expression</a>, operands of the types <code class="ph codeph">CLNT</code>, <code class="ph codeph">LANG</code>, <code class="ph codeph">TIMS</code>, and <code class="ph codeph">UNIT</code> can now be cast to the types <code class="ph codeph">CHAR</code> and <code class="ph codeph">SSTRING</code>. Here, the target type must be specified as a data element.</li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Session Variables</strong></td>
<td>When a <a href="abencds_view_glosry.html">CDS view</a> is accessed using ABAP SQL, it is possible to access the new session variable <a href="abencds_session_variable_v1.html"><code class="ph codeph">$session.system_date</code></a> in which the values of the system field <code class="ph codeph">sy-datum</code> are available.</td>
</tr>
</tbody>
</table>

## Messages

| Modification                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Implicit Message Type in `IF_T100_DYN_MSG`** | If the object reference variable `oref` in the variant [`MESSAGE oref`](../../abap-programming-language/abap-text-repositories/abapmessage_msg.md) of the statement [`MESSAGE`](../../abap-programming-language/abap-text-repositories/abapmessage.md) (used to send a message) points to an object that implements the system interface [`IF_T100_DYN_MSG`](../../abap-programming-language/abap-text-repositories/abenif_t100_dyn_msg.md), the addition `TYPE` can be omitted. The message type from the interface attribute `MSGTY` of the object is then used implicitly. |

## Transformations for ABAP Release 7.64

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>New Domains for Mapping from ABAP to XML</strong></td>
<td><p>The following new <a href="abenabap_xslt_asxml_schema.html">special domains</a> have been introduced, which override the default mapping of elementary ABAP types to asXML.</p>
<ul>
<li><code class="ph codeph">XSDUUID_BASE64</code> for 16-byte UUIDs in base64 format</li>
<li><code class="ph codeph">XSDCURRCODE</code> for ISO currency keys</li>
<li><code class="ph codeph">XSDUNITCODE</code> for ISO unit keys</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>New Formats for <code class="ph codeph">format</code> in the Attribute <code class="ph codeph">option</code> of <code class="ph codeph">tt:value</code></strong></td>
<td><p>The following new formats can be specified in parentheses after <a href="abenst_option_format.html"><code class="ph codeph">format</code></a> in the <a href="abenst_option.html"><code class="ph codeph">option</code></a> attribute of the ST statement <a href="abenst_tt_value_elementary.html"><code class="ph codeph">tt:value</code></a>:</p>
<ul>
<li><code class="ph codeph">hex</code> for a hexadecimal display of byte-like values</li>
<li><code class="ph codeph">uri</code> and <code class="ph codeph">uri_full</code> for escaping special characters in URIs</li>
<li><code class="ph codeph">uri1</code> and <code class="ph codeph">uri2</code> for displaying literal values in URIs for OData.</li>
<li><code class="ph codeph">currCode</code>, <code class="ph codeph">unitCode</code> for converting SAP-specific currency and unit keys in ISO units.</li>
<li><code class="ph codeph">currency=CURRCODE</code>, <code class="ph codeph">unit=UNITCODE</code> for formatting numbers in accordance with a currency or unit key</li>
<li><p><code class="ph codeph">alpha</code> for handling leading zeros in strings</p>
<p>Other enhancements:</p></li>
<li><code class="ph codeph">dateTimeLocal</code>, <code class="ph codeph">dateTimeOffset</code>, and <code class="ph codeph">ticksOffset</code> can now be used on the UTC time stamp types <code class="ph codeph">TIMESTAMP</code> and <code class="ph codeph">TIMESTAMPL</code>.</li>
<li><code class="ph codeph">guid</code> can now also be used on the type <code class="ph codeph">c</code> of length 22 for 16-byte UUIDs in base64 format.</li>
</ul></td>
</tr>
<tr class="odd">
<td><strong><code class="ph codeph">decimals</code> New for the Attribute <code class="ph codeph">option</code> of <code class="ph codeph">tt:value</code></strong></td>
<td><a href="abenst_option_format.html"><code class="ph codeph">Decimals</code></a> specified in the attribute <a href="abenst_option.html"><code class="ph codeph">option</code></a> of the ST statement <a href="abenst_tt_value_elementary.html"><code class="ph codeph">tt:value</code></a> specifies the number of decimal places in numeric types.</td>
</tr>
<tr class="even">
<td><strong><code class="ph codeph">regime</code> New for the Attribute <code class="ph codeph">option</code> of <code class="ph codeph">tt:value</code></strong></td>
<td><a href="abenst_option_format.html"><code class="ph codeph">regime(num\|char\|bin)</code></a> can now be specified in the attribute <a href="abenst_option.html"><code class="ph codeph">option</code></a> of the ST statement <a href="abenst_tt_value_elementary.html"><code class="ph codeph">tt:value</code></a>, where it can be used to force numeric, character-like, or byte-like handling.</td>
</tr>
<tr class="odd">
<td><strong><code class="ph codeph">noError</code> New for the Attribute <code class="ph codeph">option</code> of <code class="ph codeph">tt:value</code></strong></td>
<td><a href="abenst_option_format.html"><code class="ph codeph">noError</code></a> specified in the attribute <a href="abenst_option.html"><code class="ph codeph">option</code></a> of the ST statement <a href="abenst_tt_value_elementary.html"><code class="ph codeph">tt:value</code></a> prevents exceptions in <code class="ph codeph">language</code>, <code class="ph codeph">currCode</code>, and <code class="ph codeph">unitCode</code> formattings, which evaluate entries in database tables.</td>
</tr>
</tbody>
</table>
