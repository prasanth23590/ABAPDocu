---
title: "ST - option, Mapping Rules for Elementary Types"
source_file: abenst_option_format.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Transformation of ABAP Values > ST - tt:value, Elementary Data Objects > ST - option, Mapping Rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - option, Mapping Rules for Elementary Types

## Syntax

``` abap
... option="[format(fmt)][,decimals(dec)][,regime(num|char|bin)][,noError]"  
```

### Addition

[1. `... format(fmt) ...`](abenst_option_format.md#addition-1)

[2. `... decimals(dec) ...`](abenst_option_format.md#addition-2)

[3. `... regime(num|char|bin) ...`](abenst_option_format.md#addition-3)

[4. `... noError ...`](abenst_option_format.md#addition-4)

## Overview

### Description

Specifies mapping rules for elementary types.

- `format` can be used to specify different formats `fmt`.

- `decimals` can be used to affect the decimal places of numeric values and of UTC time stamps.

- `regime` can be used to force numeric, character-like, or byte-like handling.

- `noError` can be used to prevent exceptions for invalid values for some ABAP types and for some of the formats.

## Addition 1

`... format(fmt) ...`

### Description

The `format` option can be used to do the following:

- Specify formats `fmt` based on XML schema data types to create the corresponding XML representation or JSON representation from ABAP-specific representations of specific elementary values and vice versa.

- Specify other formats `fmt` to convert ABAP data to framework-specific representations that do not comply with the standard [asXML](abenabap_xslt_asxml.md) representation and vice versa.

The following table shows the possible formats `fmt`, the ABAP types and representations where they can be used, and the associated XML representations and [JSON](abenabap_json.md) representations.

<table>
<thead>
<tr class="header">
<th><strong><code class="ph codeph">fmt</code></strong></th>
<th><strong>ABAP Type</strong></th>
<th><strong>ABAP Representation</strong></th>
<th><strong>XML Representation</strong></th>
<th><strong>JSON Representation</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">boolean</code></td>
<td><code class="ph codeph">c</code>, length 1</td>
<td><code class="ph codeph">X</code>, blank</td>
<td><code class="ph codeph">true</code>, <code class="ph codeph">false</code></td>
<td><code class="ph codeph">true</code>, <code class="ph codeph">false</code></td>
</tr>
<tr class="even">
<td><code class="ph codeph">hex</code></td>
<td><code class="ph codeph">x</code>, <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">0123456789ABCDEF</code></td>
<td><code class="ph codeph">0123456789ABCDEF</code></td>
<td><code class="ph codeph">0123456789ABCDEF</code></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">duration</code></td>
<td><code class="ph codeph">t</code></td>
<td><code class="ph codeph">125814</code></td>
<td><code class="ph codeph">PT12H58M14S</code></td>
<td><code class="ph codeph">PT11H24M22S</code></td>
</tr>
<tr class="even">
<td><code class="ph codeph">dateTime</code></td>
<td><p><code class="ph codeph">utclong</code>,</p>
<p><code class="ph codeph">TIMESTAMP</code>,</p>
<p><code class="ph codeph">TIMESTAMPL</code></p></td>
<td><p><code class="ph codeph">2014-12-12 11:24:22.7717230</code>,</p>
<p><code class="ph codeph">20141212112422</code>,</p>
<p><code class="ph codeph">20141212112422.7717230</code></p></td>
<td><p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:27:22.7717230Z</code>,</p>
<p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:27:22Z</code>,</p>
<p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:27:22.771723Z</code></p></td>
<td><p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:27:22.7717230Z</code>,</p>
<p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:27:22Z</code>,</p>
<p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:27:22.771723Z</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">dateTimeOffset</code></td>
<td><code class="ph codeph">c</code>, length 18</td>
<td><code class="ph codeph">20141212113855+180</code></td>
<td><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:38:55+03:00</code></td>
<td><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:38:55+03:00</code></td>
</tr>
<tr class="even">
<td><code class="ph codeph">dateTimeOffset</code></td>
<td><p><code class="ph codeph">utclong</code>,</p>
<p><code class="ph codeph">TIMESTAMP</code>,</p>
<p><code class="ph codeph">TIMESTAMPL</code></p></td>
<td><p><code class="ph codeph">2014-12-12 11:24:22.7717230</code>,</p>
<p><code class="ph codeph">20141212112422</code>,</p>
<p><code class="ph codeph">20141212112422.7717230</code></p></td>
<td><p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:27:22.7717230+00:00</code>,</p>
<p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:27:22+00:00</code>,</p>
<p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:27:22.771723+00:00</code></p></td>
<td><p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:27:22.7717230+00:00</code>,</p>
<p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:27:22+00:00</code>,</p>
<p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:27:22.771723+00:00</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">dateTimeLocal</code></td>
<td><code class="ph codeph">c</code>, length 14</td>
<td><code class="ph codeph">20141212114245</code></td>
<td><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:42:45</code></td>
<td><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:42:45</code>,</td>
</tr>
<tr class="even">
<td><code class="ph codeph">dateTimeLocal</code></td>
<td><p><code class="ph codeph">utclong</code>,</p>
<p><code class="ph codeph">TIMESTAMP</code>,</p>
<p><code class="ph codeph">TIMESTAMPL</code></p></td>
<td><p><code class="ph codeph">2014-12-12 11:24:22.7717230</code>,</p>
<p><code class="ph codeph">20141212112422</code>,</p>
<p><code class="ph codeph">20141212112422.7717230</code></p></td>
<td><p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:42:45.7717230</code>,</p>
<p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:42:45</code></p>
<p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:42:45.771723</code></p></td>
<td><p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:42:45.7717230</code>,</p>
<p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:42:45</code>,</p>
<p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:42:45.771723</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ticks</code></td>
<td><code class="ph codeph">d</code></td>
<td><code class="ph codeph">20141212</code></td>
<td><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12</code></td>
<td><code class="ph codeph">/Date(1418342400000)/</code></td>
</tr>
<tr class="even">
<td><code class="ph codeph">ticks</code></td>
<td><p><code class="ph codeph">utclong</code>,</p>
<p><code class="ph codeph">TIMESTAMP</code>,</p>
<p><code class="ph codeph">TIMESTAMPL</code></p></td>
<td><p><code class="ph codeph">2014-12-12 11:50:38.9922080</code>,</p>
<p><code class="ph codeph">20141212115038</code>,</p>
<p><code class="ph codeph">20141212115038.9922080</code></p></td>
<td><p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:50:38.9922080Z</code>,</p>
<p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:50:38Z</code>,</p>
<p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:50:38.992208Z</code></p></td>
<td><p><code class="ph codeph">/Date(1418383462771)/</code>,</p>
<p><code class="ph codeph">/Date(1418383462000)/</code>,</p>
<p><code class="ph codeph">/Date(1418383462771)/</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ticksOffset</code></td>
<td><code class="ph codeph">c</code>, length 18</td>
<td><code class="ph codeph">20141212115254+180</code></td>
<td><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:52:54+03:00</code></td>
<td><code class="ph codeph">/Date(1418383462000+0180)/</code></td>
</tr>
<tr class="even">
<td><code class="ph codeph">ticksOffset</code></td>
<td><p><code class="ph codeph">utclong</code>,</p>
<p><code class="ph codeph">TIMESTAMP</code>,</p>
<p><code class="ph codeph">TIMESTAMPL</code></p></td>
<td><p><code class="ph codeph">2014-12-12 11:24:22.7717230</code>,</p>
<p><code class="ph codeph">20141212112422</code>,</p>
<p><code class="ph codeph">20141212112422.7717230</code></p></td>
<td><p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:27:22.7717230+00:00</code>,</p>
<p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:27:22+00:00</code>,</p>
<p><code class="ph codeph">2014&amp;#x2011;12&amp;#x2011;12T11:27:22.771723+00:00</code></p></td>
<td><p><code class="ph codeph">/Date(1418383462771+0000)/</code>,</p>
<p><code class="ph codeph">/Date(1418383462000+0000)/</code>,</p>
<p><code class="ph codeph">/Date(1418383462771+0000)/</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">guid</code></td>
<td><p><code class="ph codeph">x</code>, length 16; <code class="ph codeph">c</code>, length 32,</p>
<p><code class="ph codeph">c</code>, length 22</p></td>
<td><p><code class="ph codeph">0050569181751ED4A0BED3E86422E104</code>,</p>
<p><code class="ph codeph">051MaO5r7jIWljFeP2BX10</code></p></td>
<td><code class="ph codeph">00505691&amp;#x2011;8175&amp;#x2011;1ed4&amp;#x2011;a0be&amp;#x2011;d3e86422e104</code></td>
<td><code class="ph codeph">00505691&amp;#x2011;8175&amp;#x2011;1ed4&amp;#x2011;a0be&amp;#x2011;d3e86422e104</code></td>
</tr>
<tr class="even">
<td><code class="ph codeph">qName</code></td>
<td><code class="ph codeph">string</code></td>
<td><code class="ph codeph">{uri}name</code></td>
<td><code class="ph codeph">&lt;... xmlns:...="uri"&gt;...:name&lt;/...&gt;</code></td>
<td><code class="ph codeph">{uri}name</code></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">uri</code></td>
<td><code class="ph codeph">c</code>, <code class="ph codeph">string</code></td>
<td><code class="ph codeph">:;&lt;=&gt;?[\]^_``{\|}~</code></td>
<td><code class="ph codeph">:;%3C=%3E?[%5C]%5E_%60%7B%7C%7D~</code></td>
<td><code class="ph codeph">:;%3C=%3E?[%5C]%5E_%60%7B%7C%7D~</code></td>
</tr>
<tr class="even">
<td><code class="ph codeph">uriFull</code></td>
<td><code class="ph codeph">c</code>, <code class="ph codeph">string</code></td>
<td><code class="ph codeph">:;&lt;=&gt;?[\]^_``{\|}~</code></td>
<td><code class="ph codeph">%3A%3B%3C%3D%3E%3F%5B%5C%5D%5E_%60%7B%7C%7D~</code></td>
<td><code class="ph codeph">%3A%3B%3C%3D%3E%3F%5B%5C%5D%5E_%60%7B%7C%7D~</code></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">uri1</code></td>
<td><code class="ph codeph">c</code>, <code class="ph codeph">string</code></td>
<td><code class="ph codeph">Rock'n'Roll &amp; Blues</code></td>
<td><code class="ph codeph">'Rock''n''Roll%20%26%20Blues'</code></td>
<td><code class="ph codeph">'Rock''n''Roll%20%26%20Blues'</code></td>
</tr>
<tr class="even">
<td><code class="ph codeph">uri1</code></td>
<td><code class="ph codeph">x</code>, <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">0123456789ABCDEF</code></td>
<td><code class="ph codeph">binary'0123456789ABCDEF'</code></td>
<td><code class="ph codeph">binary'0123456789ABCDEF'</code></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">uri1</code></td>
<td><code class="ph codeph">t</code></td>
<td><code class="ph codeph">125814</code></td>
<td><code class="ph codeph">time'PT12H58M14S'</code></td>
<td><code class="ph codeph">time'PT12H58M14S'</code></td>
</tr>
<tr class="even">
<td><code class="ph codeph">uri1</code></td>
<td><p><code class="ph codeph">utclong</code>,</p>
<p><code class="ph codeph">TIMESTAMP</code>,</p>
<p><code class="ph codeph">TIMESTAMPL</code></p></td>
<td><p><code class="ph codeph">2014-12-12 11:24:22.7717230</code>,</p>
<p><code class="ph codeph">20141212112422</code>,</p>
<p><code class="ph codeph">20141212112422.7717230</code></p></td>
<td><p><code class="ph codeph">datetimeoffset'2014&amp;#x2011;12&amp;#x2011;12T11%3A27%3A22.7717230Z'</code>,</p>
<p><code class="ph codeph">datetimeoffset'2014&amp;#x2011;12&amp;#x2011;12T11%3A27%3A22Z'</code>,</p>
<p><code class="ph codeph">datetimeoffset'2014&amp;#x2011;12&amp;#x2011;12T11%3A27%3A22.771723Z'</code></p></td>
<td><p><code class="ph codeph">datetimeoffset'2014&amp;#x2011;12&amp;#x2011;12T11%3A27%3A22.7717230Z'</code>,</p>
<p><code class="ph codeph">datetimeoffset'2014&amp;#x2011;12&amp;#x2011;12T11%3A27%3A22Z'</code>,</p>
<p><code class="ph codeph">datetimeoffset'2014&amp;#x2011;12&amp;#x2011;12T11%3A27%3A22.771723Z'</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">uri2</code></td>
<td><code class="ph codeph">x</code>, length 16; <code class="ph codeph">c</code>, length 32</td>
<td><code class="ph codeph">0050569181751ED4A0BED3E86422E104</code></td>
<td><code class="ph codeph">guid'00505691&amp;#x2011;8175&amp;#x2011;1ed4&amp;#x2011;a0be&amp;#x2011;d3e86422e104'</code></td>
<td><code class="ph codeph">guid'00505691&amp;#x2011;8175&amp;#x2011;1ed4&amp;#x2011;a0be&amp;#x2011;d3e86422e104'</code></td>
</tr>
<tr class="even">
<td><code class="ph codeph">uri2</code></td>
<td><code class="ph codeph">d</code></td>
<td><code class="ph codeph">20141212</code></td>
<td><code class="ph codeph">datetime'2014&amp;#x2011;12&amp;#x2011;12T00%3A00%3A00'</code></td>
<td><code class="ph codeph">datetime'2014&amp;#x2011;12&amp;#x2011;12T00%3A00%3A00'</code></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">uri2</code></td>
<td><p><code class="ph codeph">utclong</code>,</p>
<p><code class="ph codeph">TIMESTAMP</code>,</p>
<p><code class="ph codeph">TIMESTAMPL</code></p></td>
<td><p><code class="ph codeph">2014-12-12 11:24:22.7717230</code>,</p>
<p><code class="ph codeph">20141212112422</code>,</p>
<p><code class="ph codeph">20141212112422.7717230</code></p></td>
<td><p><code class="ph codeph">datetime'2014&amp;#x2011;12&amp;#x2011;12T11%3A27%3A22.7717230'</code>,</p>
<p><code class="ph codeph">datetime'2014&amp;#x2011;12&amp;#x2011;12T11%3A27%3A22'</code>,</p>
<p><code class="ph codeph">datetime'2014&amp;#x2011;12&amp;#x2011;12T11%3A27%3A22.771723'</code></p></td>
<td><p><code class="ph codeph">datetime'2014&amp;#x2011;12&amp;#x2011;12T11%3A27%3A22.7717230'</code>,</p>
<p><code class="ph codeph">datetime'2014&amp;#x2011;12&amp;#x2011;12T11%3A27%3A22'</code>,</p>
<p><code class="ph codeph">datetime'2014&amp;#x2011;12&amp;#x2011;12T11%3A27%3A22.771723'</code></p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">language</code></td>
<td><code class="ph codeph">c</code>, length 1</td>
<td><code class="ph codeph">E</code>, <code class="ph codeph">D</code>, ...</td>
<td><code class="ph codeph">EN</code>, <code class="ph codeph">DE</code>, ...</td>
<td><code class="ph codeph">EN</code>, <code class="ph codeph">DE</code>, ...</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">currCode</code></td>
<td><code class="ph codeph">c</code>, length 5</td>
<td><code class="ph codeph">EUR</code>, <code class="ph codeph">USD</code>, ...</td>
<td><code class="ph codeph">EUR</code>, <code class="ph codeph">USD</code>, ...</td>
<td><code class="ph codeph">EUR</code>, <code class="ph codeph">USD</code>, ...</td>
</tr>
<tr class="even">
<td><code class="ph codeph">unitCode</code></td>
<td><code class="ph codeph">c</code>, length 3</td>
<td><code class="ph codeph">KM</code>, <code class="ph codeph">MI</code>, ...</td>
<td><code class="ph codeph">KMT</code>, <code class="ph codeph">SMI</code>, ...</td>
<td><code class="ph codeph">KMT</code>, <code class="ph codeph">SMI</code>, ...</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">currency=CURRCODE</code></td>
<td><a href="abenbuiltin_types_numeric.html">Numeric types</a></td>
<td><p><code class="ph codeph">123456</code>,</p>
<p><code class="ph codeph">123,456</code></p></td>
<td><p><code class="ph codeph">123456</code>,</p>
<p><code class="ph codeph">123,456</code></p></td>
<td><p><code class="ph codeph">123456</code>,</p>
<p><code class="ph codeph">123,456</code></p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">unit=UNITCODE</code></td>
<td><code class="ph codeph">p</code>, <code class="ph codeph">decfloat16</code>, <code class="ph codeph">decfloat34</code></td>
<td><p><code class="ph codeph">123,000</code>,</p>
<p><code class="ph codeph">123,456</code></p></td>
<td><p><code class="ph codeph">123</code>,</p>
<p><code class="ph codeph">123,456</code></p></td>
<td><p><code class="ph codeph">123</code>,</p>
<p><code class="ph codeph">123,456</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">alpha</code></td>
<td><code class="ph codeph">c</code>, <code class="ph codeph">string</code>, <code class="ph codeph">n</code></td>
<td><code class="ph codeph">0000123456</code></td>
<td><code class="ph codeph">123456</code></td>
<td><code class="ph codeph">123456</code></td>
</tr>
<tr class="even">
<td><p><code class="ph codeph">geometry</code>,</p>
<p><code class="ph codeph">geography</code>,</p>
<p><code class="ph codeph">geo=SRID</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td><p><code class="ph codeph">010100002000000000E561A1D634A748400D71AC8BDB482140</code>,</p>
<p><code class="ph codeph">0101000020E6100000E561A1D634A748400D71AC8BDB482140</code>,</p>
<p>...</p></td>
<td><p><code class="ph codeph">AQEAACAAAAAA5WGh1jSnSEANcayL20ghQA==</code>,</p>
<p><code class="ph codeph">AQEAACDmEAAA5WGh1jSnSEANcayL20ghQA==</code>,</p>
<p>...</p></td>
<td><code class="ph codeph">{"type":"Point","coordinates":[49.3063,8.6423]}</code></td>
</tr>
</tbody>
</table>

The following formats match the XML schema data types listed under [Mapping Additional XML Schema Data Types](abenabap_xslt_asxml_schema.md) or other data types. For more details, see

- `boolean` for truth values

- `dateTime`, `dateTimeOffset`, `dateTimeLocal` for date/time values

- `guid` for UUIDs

- `qName` for qualified names

- `language` for ISO language codes

- `currCode` for ISO currency codes

- `unitCode` for ISO unit codes

- `geometry`, `geography`, and `geo=SRID` for spatial data

In addition to the time stamp type `utclong`, packed numbers corresponding to the ABAP Dictionary data types `TIMESTAMP` or `TIMESTAMPL` can also be used as ABAP types for `dateTimeOffset` and `dateTimeLocal`. For `dateTimeOffset`, the value 0 is then used for the offset in the XML or JSON representation of time stamps. For `boolean`, `language`, `currCode`, and `unitCode`, `noError` can be specified to prevent an exception being raised in the event of invalid values.

The other formats have the following meaning:

- The format `hex` means that byte-like content is mapped to a hexadecimal format and not to [base64](../../abap-glossary/abenbase64_glosry.md).

- The format `duration` is based on the XML schema data type with the same name.

- The formats `ticks` and `ticksOffset` are used for JSON representations of UNIX time stamps (or ticks), which are based on the number of milliseconds since 01.01.1970,00:00:00, for OData. These formats only have special support in JSON. In XML, the regular date format or the associated time stamp formats are used. If `ticksOffset` is used for the UTC time stamp type `utclong` or for packed numbers that correspond to the data types `TIMESTAMP` or `TIMESTAMPL`, the value 0 is used for the offset in the XML or JSON representation.

- The formats `uri` and `uriFull` mask special characters like the built-in function [`escape`](../abap-processing-internal-data/abenescape_functions.md) in serializations with the format `E_URI` or `E_URI_FULL`. In deserializations, the escape symbols are transformed to the respective characters.

- The format `uri1` is used to represent literal values in URIs for OData.

  - Content of the ABAP types `c` and `string` is enclosed in quotation marks. Special characters are handled with the format `E_URI_1`, like the built-in function [`escape`](../abap-processing-internal-data/abenescape_functions.md).

  - Content of the ABAP types `x` and `xstring` is mapped as with the format `hex`. The XML and JSON representations are enclosed in quotation marks and prefixed with `binary`.

  - Content of the ABAP type `t` is mapped as with the format `duration`. The XML and JSON representations are enclosed in quotation marks and prefixed with `time`.

  - Content of time stamp fields of type `utclong` or of packed numbers that have the dictionary types `TIMESTAMP` and `TIMESTAMPL` is mapped in the same way as with the format `datetime`. The XML and JSON representations are enclosed in quotation marks and prefixed with `datetimeoffset`. Colons `:` are replaced by the escape symbols `%3A`. The prefix `datetimeoffset` identifies a UTC time stamp in OData.

- The format `uri2` is used to represent additional literal values in URIs for OData.

  - Content of the ABAP types `x` with length 16 and `c` with length 32 is mapped as with the format `guid`. The XML and JSON representations are enclosed in quotation marks and prefixed with `guid`.

  - Content of the ABAP type `d` is handled like a corresponding time stamp of dictionary type `TIMESTAMP`, in which the time part has the value *00:00:00*.

  - Content of time stamp fields of type `utclong` or of packed numbers that have the dictionary types `TIMESTAMP` and `TIMESTAMPL` is mapped in the same way as with the format `uri1`. Here, however, the format of a local time stamp with the prefix `datetime` is used.

- The format `currency=CURRCODE` formats the values of numeric ABAP types in serializations in accordance with a currency code specified in `CURRCODE`. For `CURRCODE`, visible character-like data roots of the ST program with a length no greater than 5 can be specified at this position. If the content of `CURRCODE` is initial, and in deserializations, the format is ignored. The formatting corresponds essentially to the way the function module `CURRENCY_AMOUNT_SAP_TO_IDOC` works.

- The format `unit=UNITCODE` formats the values of decimal numbers in serializations in accordance with a unit code specified in `UNITCODE`. For `UNITCODE`, visible character-like data roots of the ST program with a length no greater than 3 can be specified at this position. The format is ignored in deserializations.

- The format `alpha` formats strings like the formatting option [`ALPHA`](../abap-processing-internal-data/abapcompute_string_format_options.md) for [embedded expressions](../abap-processing-internal-data/abenstring_templates_expressions.md) in [string templates](../abap-processing-internal-data/abenstring_templates.md):

  - In serializations, leading zeros are removed as with `alpha = out`.

  - In deserializations, leading zeros are inserted as with `alpha = in`.

In JSON, the values are produced in accordance with the XML representation, except for `qName`, which is not supported in JSON. In JSON, the format `boolean` creates real [Boolean JSON values](abenjson_oview.md).

If the data type or the content do not match of if the current node is typed using [`tt:type`](abenst_tt_type.md), the option `format` is ignored or an exception is raised.

### Hint

The option `format` can also be used to map ABAP data objects to XML schema data types that are not typed using a dedicated [domain](abenabap_xslt_asxml_schema.md).

### Executable Example

[Formatting Options](abenst_format_option_abexa.md)

## Addition 2

`... decimals(dec) ...`

### Description

The `decimals` option sets the decimal places of numeric values and of time stamps in serializations. It can be applied to all [numeric ABAP types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) and to the [time stamp type](../../abap-glossary/abentimestamp_type_glosry.md) [`utclong`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md) and works in mainly the same way as the formatting option [`DECIMALS`](../abap-processing-internal-data/abapcompute_string_format_options.md) for [embedded expressions](../abap-processing-internal-data/abenstring_templates_expressions.md) in [string templates](../abap-processing-internal-data/abenstring_templates.md). The `decimals` option is ignored in deserializations.

Suitable literal integer values can be specified for `dec`. These values can also be negative for numeric types. Only the values 0 to 7 are allowed for the time stamp type `utclong`. If `dec` is not specified (empty parentheses), the option is ignored.

If `decimals` is used for time stamps of the type `utclong`, surplus decimal places are cut off in serializations instead of being rounded and are padded to seven decimal places using zeros. The following applies to [time stamps in packed numbers](../abap-processing-internal-data/abentime_stamps_packed.md) of the types `TIMESTAMP` and `TIMESTAMPL`:

- `decimals` can be combined with the `format` option for these numbers. In this case, the `decimals` option is applied first, then `format` with a `fmt` format provided for time stamps.

- Packed numbers that are typed with one of the [special domains](abenabap_xslt_asxml_schema.md) `XSDDATETIME_...` are first handled with `decimals` and then formatted as time stamps.

In these cases, the result of `decimals` must be a valid time stamp.

### Executable Example

[Option for Decimal Places](abenst_decimals_option_abexa.md)

## Addition 3

`... regime(num|char|bin) ...`

### Description

The addition `regime` specifies that the ABAP source type in serializations or the ABAP target type in deserializations is overridden by one of the regimes `num`, `char`, or `bin`. `num` specifies numeric handling, `char` specifies character-like handling, and `bin` specifies binary handling of the data by the transformation. The `regime` option deactivates the effect of all [special domains](abenabap_xslt_asxml_schema.md), but can be combined with the `format` options, where a `fmt` format specified with `format` must be suitable for handling with `regime` for handling. The `num` regime can also be combined with `decimals`.

The `num`, `char`, and `bin` regimes have the following effect on the possible ABAP types:

- `num` regime

  Forces a numeric handling of the current node.

  - Apart from deactivating the effect of [special domains](abenabap_xslt_asxml_schema.md), the `num` regime is ignored by [numeric types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md).

  - All other data types are [converted](../abap-processing-internal-data/abenconversion_elementary.md) to the [`decfloat34`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) type before the actual transformation in serializations, and then further processed as such. Source values of types `n`, `d`, and `t` must be valid. In deserializations, a value is created for `decfloat34` and assigned [without loss](../abap-processing-internal-data/abapmove_exact.md) to the target type.

- `char` regime

  Forces a character-like handling of the current node.

  - Apart from deactivating the effect of [special domains](abenabap_xslt_asxml_schema.md), the `char` regime is ignored by [numeric types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), which means that the standard XSD representation of [asXML](abenabap_xslt_asxml_elementary.md) is used.

  - Apart from deactivating the effect of [special domains](abenabap_xslt_asxml_schema.md), the `char` regime is ignored by [character-like data types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md).

  - [Byte-like data types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md) are handled as with the formatting option `format(hex)`, that is, representation is in hexadecimal format.

  - [Date and time types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md) are handled like the `c` type of corresponding length, with invalid values accepted.

- `bin` regime

  Forces a byte-like handling of the current node.

  - [Numeric types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) are [converted](../abap-processing-internal-data/abennumeric_source_fields.md) to the `xstring` type before the actual transformation in serializations, and further processed as such. In deserializations, a value is created for `xstring` and [converted](../abap-processing-internal-data/abenbyte_source_fields.md) to the target type.

  - Source fields of the [character-like data types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) `c` and `string` are [converted](../abap-processing-internal-data/abencharacter_source_fields.md) [without loss](../abap-processing-internal-data/abapmove_exact.md) to `xstring` in serializations and then processed further. A source field of type `n` is checked for valid content and also [converted](../abap-processing-internal-data/abenconversion_type_n.md) to `xstring`. In deserializations, a value is created for `xstring` and [converted](../abap-processing-internal-data/abenbyte_source_fields.md) to the target type. There must be no overflow for type `n`.

  - Apart from deactivating the effect of [special domains](abenabap_xslt_asxml_schema.md), the `bin` regime is ignored by [byte-like data types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md).

  - Source fields of the [date and time types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md) are checked for valid values in serializations, [converted](../abap-processing-internal-data/abendate_time_source_fields.md) to `xstring` and then processed further. The source fields are checked for valid content. In deserializations, a value is created for `xstring` and [converted](../abap-processing-internal-data/abenbyte_source_fields.md) to the target type. There must be no overflow.

### Executable Example

[Option for Regime](abenst_regime_option_abexa.md)

## Addition 4

`... noError ...`

### Description

Prevents exceptions that would be raised in the event of invalid values occurring in serializations of certain ABAP types and with certain formats specified using `format`. The following table shows to which ABAP types and formats `noError` is applied:

| **Type**                                         | **Format** | **Effect**                                                                    |
|--------------------------------------------------|------------|-------------------------------------------------------------------------------|
| [`n`](abenabap_xslt_asxml_elementary.md)       | \-         | Leading and trailing blanks are ignored.                                      |
| [`p`](abenabap_xslt_asxml_elementary.md)       | \-         | An invalid value in the final byte is ignored and interpreted as a plus sign. |
| [`XSDBOOLEAN`](abenabap_xslt_asxml_schema.md)  | `boolean`  | Other values apart from *X* and blank are accepted and return `true`.         |
| [`XSDDATE_D`](abenabap_xslt_asxml_schema.md)   | \-         | Invalid dates are accepted and formatted as a date.                           |
| [`XSDTIME_T`](abenabap_xslt_asxml_schema.md)   | \-         | Invalid times are accepted and formatted as a time.                           |
| [`XSDLANGUAGE`](abenabap_xslt_asxml_schema.md) | `language` | An invalid language is accepted with no conversion taking place.              |
| [`XSDCURRCODE`](abenabap_xslt_asxml_schema.md) | `currCode` | An invalid currency code is ignored with no conversion taking place.          |
| [`XSDUNITCODE`](abenabap_xslt_asxml_schema.md) | `unitCode` | An invalid unit key is ignored with no transformation taking place.           |

### Executable Example

[Option for Invalid Values](abenst_noerror_option_abexa.md)
