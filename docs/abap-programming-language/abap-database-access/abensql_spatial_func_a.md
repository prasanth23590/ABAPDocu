---
title: "sql_func - Aggregate Spatial Functions"
source_file: abensql_spatial_func_a.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - SQL Functions > sql_func - Spatial Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Aggregate Spatial Functions

## Description

The following table shows the aggregate spatial functions that can be specified as SQL expressions and the requirements on the arguments.

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
<td><code class="ph codeph">ST_ALPHASHAPEAGGR( value, radius[, unit_of_measure] )</code></td>
<td>Returns the alpha shape geometry of a set of input geometries, based on a specified radius value.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">radius</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">unit_of_measure</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP8</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_ALPHASHAPEAREAAGGR( value, fraction )</code></td>
<td>Returns the alpha shape geometry of a set of input geometries, based on a specified area fraction.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">fraction</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP8</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_ASESRIJSON_MULTICOLUMN( expression_list[, \lbr geom_name = x, \lbr object_id_name = x, \lbr include_z_values = x, \lbr include_m_values = x, \lbr coordinate_precision = x, \lbr format = x] )</code></td>
<td>Returns a string representing a set of rows in the EsriJSON format.</td>
<td><p><code class="ph codeph">expression_list</code>: any data type</p>
<p><code class="ph codeph">geom_name</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p>
<p><code class="ph codeph">object_id_name</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p>
<p><code class="ph codeph">include_z_values</code>: <code class="ph codeph">INT4</code></p>
<p><code class="ph codeph">include_m_values</code>: <code class="ph codeph">INT4</code></p>
<p><code class="ph codeph">coordinate_precision</code>: <code class="ph codeph">INT4</code></p>
<p><code class="ph codeph">format</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p></td>
<td><code class="ph codeph">CHAR</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_ASGEOJSON_MULTICOLUMN( expression_list[, \lbr geom_name = x, \lbr feature_id_name = x, \lbr include_bbox = x, \lbr include_null_property_values = x, \lbr coordinate_precision = x, \lbr format = x] )</code></td>
<td>Returns a string representing a set of rows in the GeoJSON format.</td>
<td><p><code class="ph codeph">expression_list</code>: any data type</p>
<p><code class="ph codeph">geom_name</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p>
<p><code class="ph codeph">feature_id_name</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p>
<p><code class="ph codeph">include_bbox</code>: <code class="ph codeph">INT4</code></p>
<p><code class="ph codeph">include_null_property_values</code>: <code class="ph codeph">INT4</code></p>
<p><code class="ph codeph">coordinate_precision</code>: <code class="ph codeph">INT4</code></p>
<p><code class="ph codeph">format</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p></td>
<td><code class="ph codeph">CHAR</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_ASMVT( expression_list[, \lbr layer_name = x, \lbr extent = x, \lbr geom_name = x] )</code></td>
<td>Returns a binary representation of a set of rows in the Mapbox Vector Tile format.</td>
<td><p><code class="ph codeph">expression_list</code>: any data type</p>
<p><code class="ph codeph">layer_name</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p>
<p><code class="ph codeph">extent</code>: <code class="ph codeph">INT4</code></p>
<p><code class="ph codeph">geom_name</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p></td>
<td><code class="ph codeph">RAWSTRING</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_ASSVGAGGR( value )</code></td>
<td>Returns a complete or partial SVG document which renders the geometries in a group.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">CHAR</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_COLLECTAGGR( value )</code></td>
<td>Creates a single geometry collection or multi-geometry containing all geometries of the column.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_CONCAVEHULLAGGR( value )</code></td>
<td>Returns the alpha shape geometry of a set of input geometries.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_CONVEXHULLAGGR( value )</code></td>
<td>Returns the convex hull for all of the geometries in a group.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_ENVELOPEAGGR( value )</code></td>
<td>Returns the bounding rectangle for all of the geometries in a group.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_INTERSECTIONAGGR( value )</code></td>
<td>Returns the spatial intersection of all of the geometries in a group.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_UNIONAGGR( value )</code></td>
<td>Returns the spatial union of all of the geometries in a group.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
</tbody>
</table>
