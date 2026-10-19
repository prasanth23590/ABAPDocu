---
title: "sql_func - Spatial Methods"
source_file: abensql_spatial_func_m.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - SQL Functions > sql_func - Spatial Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Spatial Methods

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
<td><code class="ph codeph">ST_3DLENGTH( value[, unit_name] )</code></td>
<td>Returns the length of the linestring or multi-linestring in three-dimensional space.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">unit_name</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP8</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_ADDMEASURE( value, measureend, measurestart )</code></td>
<td>Returns a derived linestring with added or altered M values.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">measureend</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">measurestart</code>: <code class="ph codeph">f</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_ALPHASHAPE( value, radius[, unit_of_measure] )</code></td>
<td>Returns the alpha shape geometry of the input geometry, based on a specified radius value.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">radius</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">unit_of_measure</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_ALPHASHAPEAREA( value, fraction )</code></td>
<td>Returns an alpha shape of the input geometry, based on a specified area fraction.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">fraction</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_ALPHASHAPEEDGE( value, fraction )</code></td>
<td>Returns an alpha shape of the input geometry, based on a specified edge fraction.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">fraction</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_AREA( value[, unit_name] )</code></td>
<td>Computes the area of the multipolygon.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">unit_name</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_ASBINARY( value )</code></td>
<td>Returns the WKB representation of a geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">RAWSTRING</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_ASESRIJSON( value )</code></td>
<td>Returns the EsriJSON representation of a geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">STRING</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_ASEWKB( value )</code></td>
<td>Returns the extended WKB representation of a geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">RAWSTRING</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_ASEWKT( value )</code></td>
<td>Returns the extended WKT representation of a geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">STRING</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_ASGEOJSON( value )</code></td>
<td>Returns a string representing a geometry in GeoJSON format.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">STRING</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_ASMVTGEOM( value, \lbr bounds = x[, \lbr extent = x, \lbr buffer = x, \lbr clipgeom = x] )</code></td>
<td>Constructs a geometry transformed into the coordinate system of a Mapbox Vector Tile.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">bounds</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">extent</code>: <code class="ph codeph">INT4</code></p>
<p><code class="ph codeph">buffer</code>: <code class="ph codeph">INT4</code></p>
<p><code class="ph codeph">clipgeom</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_ASSVG( value[, \lbr approximate = x, \lbr attribute = x, \lbr decimaldigits = x, \lbr pathdataonly = x, \lbr randomfill = x, \lbr relative = x] )</code></td>
<td>Returns an SVG figure representing a geometry.</td>
<td><p><code class="ph codeph">VALUE</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">approximate</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 3</p>
<p><code class="ph codeph">attribute</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code></p>
<p><code class="ph codeph">decimaldigits</code>: <code class="ph codeph">INT4</code></p>
<p><code class="ph codeph">pathdataonly</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 3</p>
<p><code class="ph codeph">randomfill</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 3</p>
<p><code class="ph codeph">relative</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 3</p></td>
<td><code class="ph codeph">STRING</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_ASTEXT( value )</code></td>
<td>Returns the text representation of a geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">STRING</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_ASWKB( value )</code></td>
<td>Returns the WKB representation of a geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">RAWSTRING</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_ASWKT( value )</code></td>
<td>Returns the WKT representation of a geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">STRING</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_BOUNDARY( value )</code></td>
<td>Returns the Open Geospatial Consortium (OGC) boundary of the geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_BUFFER( value, distance[, unit_name_or_nip] )</code></td>
<td>Returns the geometry that represents all points whose distance from any point of a geometry is less than or equal to a specified distance in the given units.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">distance</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">unit_name_or_nip</code>: any data type</p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_CENTROID( value )</code></td>
<td>Returns the <code class="ph codeph">ST_Point</code> value that is the mathematical centroid of the geometry value.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_CLOSESTPOINTOFAPPROACH( value, trajectoryb )</code></td>
<td>Computes the smallest measure (first point in time if measure represents time) at which two trajectories are at closest distance to each other.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">trajectoryb</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_COLLECT( value, geometry2 )</code></td>
<td>Collects geometries into a single geometry collection or multi-geometry.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geometry2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_CONCAVEHULL( value )</code></td>
<td>Returns the concave hull of the geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_CONTAINS( value, geometry2 )</code></td>
<td>Tests if a geometry spatially contains another geometry.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geometry2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_CONVEXHULL( value )</code></td>
<td>Returns the convex hull of the geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_COORDDIM( value )</code></td>
<td>Returns the number of coordinate dimensions stored with each point of the geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_COVEREDBY( value, geometry2 )</code></td>
<td>Tests if a geometry is spatially covered by another geometry.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geometry2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_COVERS( value, geometry2 )</code></td>
<td>Tests if a geometry spatially covers another geometry.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geometry2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_DIFFERENCE( value, geometry2 )</code></td>
<td>Returns the geometry that represents the point set difference of two geometries.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geometry2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_DIMENSION( value )</code></td>
<td>Returns the dimension of the geometry. Points have dimension 0, lines have dimension 1, and polygons have dimension 2. Any empty geometry has dimension -1.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_DISJOINT( value, geometry2 )</code></td>
<td>Tests if a geometry is spatially disjoint from another geometry.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geometry2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_DISTANCE( value, geometry2[, unit_name] )</code></td>
<td>Returns the smallest distance between the <code class="ph codeph">&lt;geometry&gt;</code> and the specified geometry.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geometry2</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">unit_name</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_ENDPOINT( value )</code></td>
<td>Returns an <code class="ph codeph">ST_Point</code> value that is the end point.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_ENVELOPE( value )</code></td>
<td>Returns the bounding rectangle for the geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_EQUALS( value, geom2 )</code></td>
<td>Tests if a geometry is spatially equal to another geometry.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geom2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_EXTERIORRING( value )</code></td>
<td>Returns the exterior ring of the polygon.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_FORCE2D( value )</code></td>
<td>Returns the geometry which results from dropping the Z and M coordinates, from the target geometry, if they exist, retaining only the X and Y components.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_FORCE3DM( value )</code></td>
<td>Returns the geometry which results from dropping the Z coordinate of the target geometry, if it exists, and adding an M coordinate if it does not exist, setting its value to 0.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_FORCE3DZ( value )</code></td>
<td>Returns the geometry which results from dropping the M coordinate of the target geometry, if it exists, and adding a Z coordinate if it does not exist, setting its value to 0.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_FORCE4D( value )</code></td>
<td>Returns the geometry which results from adding Z and M coordinates, and if any of them do not exist, sets their value to 0.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_FRECHETDISTANCE( value, linestring2[, unit_name] )</code></td>
<td>Computes the discrete Fr&amp;#x00E9;chet distance between two linestrings.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">linestring2</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">unit_name</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_GEOHASH( value[, maximum_length] )</code></td>
<td>Returns the Geohash representation of a geometry.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">maximum_length</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">CHAR</code> with the length of 128</td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_GEOMETRYTYPE( value )</code></td>
<td>Returns the name of the type of the geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">CHAR</code> with the length of 128</td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_INTERIORRINGN( value, N )</code></td>
<td>Returns the nth interior ring in the polygon.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">n</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_INTERSECTION( value, geometry2 )</code></td>
<td>Returns the geometry that represents the point set intersection of two geometries.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geometry2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_INTERSECTS( value, geometry2 )</code></td>
<td>Tests if a geometry spatially intersects another value.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geometry2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_INTERSECTSFILTER( value, geometry2 )</code></td>
<td>An inexpensive test if the two geometries might intersect.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geometry2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_INTERSECTSRECT( value, corner1, corner2 )</code></td>
<td>Tests if a geometry intersects a rectangle.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">corner1</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">corner2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_INTERSECTSRECTPLANAR( value, corner1, corner2 )</code></td>
<td>Tests if a geometry intersects a rectangle.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">corner1</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">corner2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_INVALIDREASON( value )</code></td>
<td>Returns the reason why a geometry is invalid.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">CHAR</code> with the length of 10000</td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_IS3D( value )</code></td>
<td>Determines if the geometry has Z coordinate values.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_ISCLOSED( value )</code></td>
<td>Tests if the value is closed. A linestring is closed if the start and end points are coincident. A multilinestring is closed if it is non-empty and has an empty boundary.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_ISEMPTY( value )</code></td>
<td>Determines whether the geometry represents an empty set.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_ISMEASURED( value )</code></td>
<td>Determines if the geometry has associated measure values.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_ISRING( value )</code></td>
<td>Tests if the linestring is a ring. A linestring is a ring if it is closed and simple (no self intersections).</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_ISSIMPLE( value )</code></td>
<td>Determines whether the geometry is simple (containing no self intersections or other irregularities).</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_ISVALID( value )</code></td>
<td>Determines whether the geometry is a valid spatial object.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_ISVALIDTRAJECTORY( value )</code></td>
<td>Determines whether a given geometry is a valid trajectory. A valid trajectory is a <code class="ph codeph">LineString</code> or <code class="ph codeph">CircularString</code> with strictly increasing m-coordinates as measure.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_LENGTH( value[, unit_name] )</code></td>
<td>Returns the length measurement of all the linestrings in the multilinestring.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">unit_name</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_LINEINTERPOLATEPOINT( value, fraction )</code></td>
<td>Returns a point linearly interpolated on a given linestring.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">fraction</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_LINELOCATEPOINT( value, point )</code></td>
<td>Finds the point on a given linestring that is closest to a given point.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">point</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_LINESUBSTRING( value, startfrac, endfrac )</code></td>
<td>Returns a sub-linestring of the given linestring.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">startfrac</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">endfrac</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_LOCATEALONG( value, measure )</code></td>
<td>Returns a derived geometry collection value with elements that match the specified measure.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">measure</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_LOCATEBETWEEN( value, measurestart, measureend )</code></td>
<td>Returns a derived geometry collection value with elements that match the specified range of measures inclusively.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">measurestart</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">measureend</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_M( value )</code></td>
<td>Returns the measure value of a geometry of type <code class="ph codeph">ST_Point</code>.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_MMAX( value )</code></td>
<td>Retrieves the maximum M coordinate value of a geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_MMIN( value )</code></td>
<td>Retrieves the minimum M coordinate value of a geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_NUMGEOMETRIES( value )</code></td>
<td>Returns the number of geometries contained in the geometry collection.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_NUMINTERIORRING( value )</code></td>
<td>Returns the number of interior rings in the polygon.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_NUMINTERIORRINGS( value )</code></td>
<td>Returns the number of interior rings in the polygon.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_NUMPOINTS( value )</code></td>
<td>Returns the number of points defining the linestring.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_ORDERINGEQUALS( value, geom2 )</code></td>
<td>Tests if a geometry is identical to another geometry.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geom2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_OVERLAPS( value, geometry2 )</code></td>
<td>Tests if a geometry overlaps another geometry.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geometry2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_PERIMETER( value[, unit_name] )</code></td>
<td>Computes the perimeter of the polygon in the specified unit.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">unit_name</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_POINTN( value, n )</code></td>
<td>Returns the nth point in the linestring.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">n</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_POINTONSURFACE( value )</code></td>
<td>Returns an <code class="ph codeph">ST_Point</code> value that is guaranteed to spatially intersect the multipolygon.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_REMOVEPOINT( value, position )</code></td>
<td>Removes a point from a given linestring or point.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">position</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP8</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_REVERSE( value )</code></td>
<td>Returns the geometry with the direction of all curves reversed.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_ROTATE( value, angle[, centerx, centery] )</code></td>
<td>Rotates a geometry by a given angle counter-clockwise around the coordinate systems origin or a given center.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">angle</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">centerx</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">centery</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_SCALE( value, factor[, factory] )</code></td>
<td>Scales a geometry by the given factor.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">factor</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">factory</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_SIMPLIFY( value, epsilon )</code></td>
<td>Simplifies a geometry using the Douglas-Peucker algorithm.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">epsilon</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_SNAPTOGRID( value, cell_size )</code></td>
<td>Returns a copy of the geometry with all points snapped to the specified grid.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">cell_size</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_SRID( value[, srid] )</code></td>
<td>Retrieves or modifies the spatial reference system associated with the geometry.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">INT4</code></p></td>
<td><code class="ph codeph">xstring</code> if <code class="ph codeph">srid</code> is specified, else <code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_STARTPOINT( value )</code></td>
<td>Returns an <code class="ph codeph">ST_Point</code> value that is the starting point.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_SYMDIFFERENCE( value, geometry2 )</code></td>
<td>Returns the geometry that represents the point set symmetric difference of two geometries.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geometry2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_TOUCHES( value, geometry2 )</code></td>
<td>Tests if a geometry spatially touches another geometry.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geometry2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP8</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_TRANSFORM( value, srid[, on_error] )</code></td>
<td>Creates a copy of the geometry transformed into the specified spatial reference system.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">srid</code>: <code class="ph codeph">INT4</code></p>
<p><code class="ph codeph">on_error</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 4</p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_TRANSLATE( value, deltax, deltay )</code></td>
<td>Translates a geometry by given offsets.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">deltax</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">deltay</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_TRANSLATE3D( value, deltax, deltay, deltaz )</code></td>
<td>Translates a geometry by given offsets.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">deltax</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">deltay</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">deltaz</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_UNION( value, geometry2 )</code></td>
<td>Returns the geometry that represents the point set union of two geometries.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geometry2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">xstring</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_WITHIN( value, geometry2 )</code></td>
<td>Tests if a geometry is spatially contained within another geometry.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geometry2</code>: <code class="ph codeph">xstring</code></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_WITHINDISTANCE( value, geometry2, distance[, unit_name] )</code></td>
<td>Tests if two geometries are within a specified distance of each other.</td>
<td><p><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">geometry2</code>: <code class="ph codeph">xstring</code></p>
<p><code class="ph codeph">distance</code>: <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">f</code></p>
<p><code class="ph codeph">unit_name</code>: <code class="ph codeph">CHAR</code> greater than 0 and less than or equal to 128</p></td>
<td><code class="ph codeph">INT4</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_X( value )</code></td>
<td>Returns the X coordinate of a geometry of type <code class="ph codeph">ST_Point</code>.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_XMAX( value )</code></td>
<td>Retrieves the maximum X coordinate value of a geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_XMIN( value )</code></td>
<td>Retrieves the minimum X coordinate value of a geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_Y( value )</code></td>
<td>Returns the Y coordinate of a geometry of type <code class="ph codeph">ST_Point</code>.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_YMAX( value )</code></td>
<td>Retrieves the maximum Y coordinate value of a geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_YMIN( value )</code></td>
<td>Retrieves the minimum Y coordinate value of a geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_Z( value )</code></td>
<td>Returns the Z coordinate of a geometry of type <code class="ph codeph">ST_Point</code>.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">ST_ZMAX( value )</code></td>
<td>Retrieves the maximum Z coordinate value of a geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ST_ZMIN( value )</code></td>
<td>Retrieves the minimum Z coordinate value of a geometry.</td>
<td><code class="ph codeph">value</code>: <code class="ph codeph">xstring</code></td>
<td><code class="ph codeph">FLTP</code></td>
<td>SP7</td>
</tr>
</tbody>
</table>
