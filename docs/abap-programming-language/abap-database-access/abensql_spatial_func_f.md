---
title: "sql_func - Spatial Functions"
source_file: abensql_spatial_func_f.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - SQL Functions > sql_func - Spatial Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Spatial Functions

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
<td><code class="ph codeph">ST_GEOMFROMESRIJSON( esrijson )</code></td>
<td>Constructs a geometry from an EsriJSON geometry object.</td>
<td><code class="ph codeph">esrijson</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_GEOMFROMEWKB( ewkb )</code></td>
<td>Constructs a geometry from a string representation.</td>
<td><code class="ph codeph">ewkb</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">x</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_GEOMFROMEWKT( ewkt )</code></td>
<td>Constructs a geometry from a string representation.</td>
<td><code class="ph codeph">ewkt</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_GEOMFROMGEOHASH( geohash[, srid] )</code></td>
<td>Constructs a geometry from a Geohash string. The default value for <code class="ph codeph">srid</code> is 0.</td>
<td><p><code class="ph codeph">geohash</code>: <code class="ph codeph">CHAR</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">i</code> or <code class="ph codeph">int4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_GEOMFROMTEXT( wkt[, srid] )</code></td>
<td>Constructs a geometry from a character string representation. The default value for <code class="ph codeph">srid</code> is 0.</td>
<td><p><code class="ph codeph">wkt</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">i</code> or <code class="ph codeph">int4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_GEOMFROMWKB( wkb[, srid] )</code></td>
<td>Constructs a geometry from a string representation. The default value for <code class="ph codeph">srid</code> is 0.</td>
<td><p><code class="ph codeph">wkb</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">x</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">i</code> or <code class="ph codeph">int4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_GEOMFROMWKT( wkt[, srid] )</code></td>
<td>Constructs a geometry from a string representation. The default value for <code class="ph codeph">srid</code> is 0.</td>
<td><p><code class="ph codeph">wkt</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">i</code> or <code class="ph codeph">int4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_MAKELINE( value, secondpoint )</code></td>
<td>Creates a linestring from two given points.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">secondpoint</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_MAKEPOLYGON( exterionring[, interiorring] )</code></td>
<td>Creates a polygon from a given exterior ring (shell) and an optional collection of interior rings (holes).</td>
<td><p><code class="ph codeph">exterionring</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">interiorring</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_POINTFROMGEOHASH( geohash[, srid] )</code></td>
<td>Constructs a point from a Geohash string. The default value for <code class="ph codeph">srid</code> is 0.</td>
<td><p><code class="ph codeph">geohash</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">i</code> or <code class="ph codeph">int4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
</tbody>
</table>
