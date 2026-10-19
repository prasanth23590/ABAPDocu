---
title: "sql_func - Spatial Constructors"
source_file: abensql_spatial_func_c.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - SQL Functions > sql_func - Spatial Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Spatial Constructors

## Description

The following table shows the spatial functions that can be specified as SQL expressions and the requirements on the arguments.

<table>
<thead>
<tr class="header">
<th><strong>Syntax</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>Valid Argument Types</strong></th>
<th><strong>Result Type</strong></th>
<th><strong>HANA Release</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">ST_NEW_CIRCULARSTRING( )</code></td>
<td>Constructs a circularstring representing the empty set</td>
<td>-</td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_NEW_CIRCULARSTRING( text[, srid] )</code></td>
<td>Constructs a circularstring from Well Known Text (WKT).</td>
<td><p><code class="ph codeph">text</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_NEW_GEOMETRYCOLLECTION( )</code></td>
<td>Constructs a geometry collection representing the empty set.</td>
<td>-</td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_NEW_GEOMETRYCOLLECTION( text[, srid] )</code></td>
<td>Constructs a geometry collection from a text representation.</td>
<td><p><code class="ph codeph">text</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_NEW_LINESTRING( )</code></td>
<td>Constructs a linestring representing the empty set.</td>
<td>-</td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_NEW_LINESTRING( text[, srid] )</code></td>
<td>Constructs a linestring from a text representation.</td>
<td><p><code class="ph codeph">text</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_NEW_MULTILINESTRING( )</code></td>
<td>Constructs a multilinestring representing the empty set.</td>
<td>-</td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_NEW_MULTILINESTRING( text[, srid] )</code></td>
<td>Constructs a multilinestring from a text representation.</td>
<td><p><code class="ph codeph">text</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_NEW_MULTIPOINT( )</code></td>
<td>Constructs a multipoint representing the empty set.</td>
<td>-</td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_NEW_MULTIPOINT( text[, srid] )</code></td>
<td>Constructs a multipoint from a text representation.</td>
<td><p><code class="ph codeph">text</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_NEW_MULTIPOLYGON( )</code></td>
<td>Constructs a multi polygon representing the empty set.</td>
<td>-</td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_NEW_MULTIPOLYGON( text[, srid] )</code></td>
<td>Constructs a multi polygon from a text representation.</td>
<td><p><code class="ph codeph">text</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_NEW_POINT( )</code></td>
<td>Constructs a point representing the empty set.</td>
<td>-</td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_NEW_POINT( text[, srid] )</code></td>
<td>Constructs a point from a text representation.</td>
<td><p><code class="ph codeph">text</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_NEW_POINT( x, y[, srid] )</code></td>
<td>Constructs a 2D point from X, Y coordinates.</td>
<td><p><code class="ph codeph">x</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">y</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_NEW_POINTM( x, y, m[, srid])</code></td>
<td>Constructs a 2D point from X, Y coordinates and a measure value.</td>
<td><p><code class="ph codeph">x</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">y</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">m</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_NEW_POINTZ( x, y, z[, srid] )</code></td>
<td>Constructs a 3D point from X, Y, Z coordinates.</td>
<td><p><code class="ph codeph">x</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">y</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">z</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_NEW_POINTZM( x, y, z, m[, srid] )</code></td>
<td>Constructs a 3D point from X, Y, Z coordinates and a measure value.</td>
<td><p><code class="ph codeph">x</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">y</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">z</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">m</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_NEW_POLYGON( )</code></td>
<td>Constructs a polygon representing the empty set.</td>
<td>-</td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_NEW_POLYGON( text[, srid] )</code></td>
<td>Constructs a polygon from a text representation.</td>
<td><p><code class="ph codeph">text</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
</tbody>
</table>
