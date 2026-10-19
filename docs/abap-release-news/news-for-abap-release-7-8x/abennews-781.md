---
title: "News for ABAP Release 7.81"
source_file: abennews-781.html
section: "ABAP Release News > News for ABAP Release 7.8x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.81

The kernel release for ABAP release 7.81 is 7.81.

## ABAP CDS Access Control

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Quantifier Operators</strong></td>
<td><p>With the new addition <code class="ph codeph">ALL</code>, access conditions can express that access shall only be granted when from a set-valued association all values satisfy the condition.</p>
<p><code class="ph codeph">WHERE ALL toItem.State = 'A'</code></p>
<p>To accompany this use case, the <code class="ph codeph">BYPASS WHEN</code> operator has been extended to literal conditions also.</p>
<p>A dedicated operator <code class="ph codeph">EXISTS</code> can be used when different access conditions using the same set-valued association shall not be coupled in their fields by means of a common join expression.</p>
<p><a href="abencds_dcl_role_conditions.html">More Information</a></p></td>
</tr>
</tbody>
</table>

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
<td><strong>New Session Variables for User Time Zone and User Date</strong></td>
<td><p>Two new <a href="abencds_session_variable_v1.html">session variables</a> are available in ABAP CDS:</p>
<ul>
<li><a href="abencds_session_variable_v1.html"><code class="ph codeph">$session.user_timezone</code></a>, which returns the time zone defined in the user master record for the local user time.</li>
<li><a href="abencds_session_variable_v1.html"><code class="ph codeph">$session.user_date</code></a>, which returns the local date of a user.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>New String Function for Regular Expressions</strong></td>
<td>ABAP CDS now supports the new string function <a href="abencds_sql_functions_character_v2.html"><code class="ph codeph">REPLACE_REGEXPR</code></a> that allows regular expressions to be replaced.</td>
</tr>
</tbody>
</table>

## Data Types

| Modification             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Indicator Structures** | The new addition [`INDICATORS`](../../abap-programming-language/abap-declarations/abaptypes_indicators.md) of the statement [`TYPES`](../../abap-programming-language/abap-declarations/abaptypes.md) allows an [indicator structure](../../abap-glossary/abenindicator_structure_glosry.md) to be defined as a [substructure](../../abap-glossary/abensubstructure_glosry.md) of a given [structured type](../../abap-glossary/abenstructured_type_glosry.md). An indicator structure can be used as a [ABAP SQL indicator](../../abap-glossary/abenabap_sql_indicator_glosry.md) in ABAP SQL read and write statements. |

## Expressions and Functions

| Modification                                                 | Description                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Calculation Assignments in Constructor Operator `REDUCE`** | In the assignments behind the addition `NEXT` of the constructor operator [`REDUCE`](../../abap-programming-language/abap-program-flow-logic/abenconstructor_expression_reduce.md). The [calculation assignment operators](../../abap-glossary/abencalc_assignment_op_glosry.md) `+=`, `+=`, `*=`, `/=` or `&&=` can be used now and the respective rules apply. |

## String Processing

| Modification                                                   | Description                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Exception `CX_SY_STRING_SIZE_TOO_LARGE` in Transformations** | The exception of exception class `CX_SY_STRING_SIZE_TOO_LARGE` that occurs, when an operation with a [string](../../abap-glossary/abenstring_glosry.md) exceeds its [maximum size](../../abap-programming-language/abap-data-types-and-data-objects/abenmemory_consumption_2.md) can now also be handled for the statement [`CALL TRANSFORMATION`](../../abap-programming-language/abap-data-interchange-formats/abapcall_transformation.md) if some conditions are met. |

## ABAP SQL

| Modification                             | Description                                                                                                                                                                                                                         |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **New String Functions**                 | ABAP SQL now supports the new string functions [`REPLACE_REGEXPR`](../../abap-programming-language/abap-database-access/abensql_string_func.md), [`LIKE_REGEXPR`](../../abap-programming-language/abap-database-access/abensql_string_func.md), and [`OCCURRENCES_REGEXPR`](../../abap-programming-language/abap-database-access/abensql_string_func.md), which support regular expressions. |
| **Addition to the `UPDATE FROM` Clause** | [Set indicators](../../abap-programming-language/abap-database-access/abapupdate_set_indicator.md) can now be used as additions after the [`UPDATE FROM`](../../abap-programming-language/abap-database-access/abapupdate_source.md) clause to indicate columns for updating.                                                             |

## ABAP RESTful Application Programming Model

In release 7.81, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Draft Support for RAP BOs</strong></td>
<td>The new statement <a href="abenbdl_with_draft.html"><code class="ph codeph">with draft</code></a> can be used to enable the draft concept for a RAP BO.</td>
</tr>
<tr class="even">
<td><strong>Determine Actions</strong></td>
<td>Determine actions are a new type of action defined using <a href="abenbdl_determine_action.html"><code class="ph codeph">determine action</code></a>. With a determine action, determinations and validations can be executed on request.</td>
</tr>
<tr class="odd">
<td><strong>Precheck for Modify Operations</strong></td>
<td>The new RAP BO operation addition <a href="abenbdl_precheck.html"><code class="ph codeph">precheck</code></a> can be used to prevent illegal changes from reaching the application buffer by prechecking modify operations.</td>
</tr>
<tr class="even">
<td><strong>New Field Characteristics</strong></td>
<td><p>RAP BDL now supports the following new <a href="abenbdl_field_char.html">field characteristics</a>:</p>
<ul>
<li><a href="abenbdl_field_char.html"><code class="ph codeph">mandatory:create</code></a></li>
<li><a href="abenbdl_field_char.html"><code class="ph codeph">readonly:update</code></a></li>
</ul></td>
</tr>
</tbody>
</table>
