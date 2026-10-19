---
title: "News for ABAP Release 7.80"
source_file: abennews-780.html
section: "ABAP Release News > News for ABAP Release 7.8x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.80

The kernel release for ABAP release 7.80 is 7.80.

## ABAP Dictionary

| Modification  | Description                                                                                                                                                                                                                                                                                                          |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Load Unit** | In ABAP Dictionary, a new technical setting for database tables is available: the [load unit](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_load_unit.md). It specifies how the data of the table is loaded into the main memory of the SAP HANA database. It can be used to reduce the memory consumption in the HANA database server. |

## ABAP CDS

| Modification                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Defining Associations in CDS Projection Views** | It is now possible to define new associations with external data sources in [CDS projection views](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_view_as_projection.md).                                                                                                                                                                                                                                                                                                                                                          |
| **CDS View Entities**                             | A new kind of CDS view is available: the [CDS view entity](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_v2_views.md). CDS view entities represent an improved version of [CDS DDIC-based views (obsolete)](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_v1_views.md) (`DEFINE VIEW`). They serve the same purpose and have the same structure as CDS DDIC-based views (obsolete), but offer many advantages. CDS view entities are planned to replace CDS DDIC-based views (obsolete) in the future. A CDS view entity is defined with the statement `DEFINE VIEW ENTITY`. |

## String Processing

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Support of Perl Compatible Regular Expressions</strong></td>
<td><p>Besides the existing support for <a href="abenposix_regex_glosry.html">POSIX regular expressions</a> (now obsolete), ABAP supports now also <a href="abenpcre_regex_glosry.html">PCRE regular expressions</a> that are processed by the <a href="https://www.pcre.org/">PCRE2 Library</a> implemented in the <a href="abenkernel_glosry.html">ABAP Kernel</a>. PCRE regular expressions can be used in the same way as POSIX regular expressions. The following distinctions exist:</p>
<ul>
<li>The new addition <a href="abapfind_pattern.html"><code class="ph codeph">PCRE</code></a> can be used instead of <a href="abapfind_pattern.html"><code class="ph codeph">REGEX</code></a> in the statements <a href="abapfind.html"><code class="ph codeph">FIND</code></a> and <a href="abapreplace.html"><code class="ph codeph">REPLACE</code></a>.</li>
<li>The new parameter <a href="abenstring_functions_regex.html"><code class="ph codeph">pcre</code></a> can be used instead of <a href="abenstring_functions_regex.html"><code class="ph codeph">regex</code></a> in built-in functions.</li>
<li><p>The new (factory) methods of the <a href="abenregex_system_classes.html">system classes</a> <code class="ph codeph">CL_ABAP_REGEX</code> and <code class="ph codeph">CL_ABAP_MATCHER</code>.</p>
<p>PCRE regular expressions are more powerful and have better performance than POSIX regular expressions. For more information, see <a href="abenregular_expressions.html">Regular Expressions</a>.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Verbatim Replacements</strong></td>
<td>The new addition <a href="abapreplace_options.html"><code class="ph codeph">VERBATIM</code></a> of the <a href="abapreplace.html"><code class="ph codeph">REPLACE</code></a> statement causes all characters of the replacement string to be taken literally. If this addition is used, special characters for regular expression replacement patterns have no special meaning.</td>
</tr>
<tr class="odd">
<td><strong>New Catchable Exception <code class="ph codeph">CX_SY_STRING_SIZE_TOO_LARGE</code></strong></td>
<td>The exception that occurs when an operation with a <a href="abenstring_glosry.html">string</a> exceeds its <a href="abenmemory_consumption_2.html">maximum size</a> is now connected to the exception class <code class="ph codeph">CX_SY_STRING_SIZE_TOO_LARGE</code> and can be handled. Previously, it always resulted in runtime error <code class="ph codeph">STRING_SIZE_TOO_LARGE</code>.</td>
</tr>
<tr class="even">
<td><strong>Formatting Option <code class="ph codeph">CURRENCY</code> for Decimal Floating Point Numbers</strong></td>
<td>The formatting option <a href="abapcompute_string_format_options.html"><code class="ph codeph">CURRENCY</code></a> in <a href="abenstring_templates.html">string templates</a> can now also be applied to <a href="abendecfloat_glosry.html">decimal floating point numbers</a>.</td>
</tr>
</tbody>
</table>

## ABAP SQL

| Modification                                                 | Description                                                                                                                                                                                                                              |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Further Data Types Allowed in Elementary SQL Expressions** | [Elementary SQL expressions](../../abap-programming-language/abap-database-access/abensql_elem.md) can now also have the dictionary data types `STRING` and `RAWSTRING`.                                                                                                                    |
| **New Type Conversion Function `to_blob`**                   | ABAP SQL now supports the new [type conversion function](../../abap-programming-language/abap-database-access/abensql_type_conv_func.md) [`to_blob`](../../abap-programming-language/abap-database-access/abensql_type_conv_func.md).                                                                                                          |
| **Hierarchy Load Options**                                   | The [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_generator.md) can now use the new addition `LOAD BULK|INCREMENTAL|load_option` to specify the load policy for a generated hierarchy. |
| **Typed Literals**                                           | [Typed literals](../../abap-programming-language/abap-database-access/abenabap_sql_typed_literals.md) for many ABAP Dictionary types are now available in ABAP SQL.                                                                                                                         |

## ABAP RESTful Application Programming Model

In release 7.80, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

| Modification                          | Description                                                                                                                                                                                                                                                                          |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Unmanaged Lock in Managed RAP BOs** | The new statement [`lock master unmanaged`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_locking.md) can be used if the application developer wants to implement an own locking mechanism in a managed RAP BO. An own locking mechanism can be used instead of the RAP locking mechanism provided by the RAP framework. |
