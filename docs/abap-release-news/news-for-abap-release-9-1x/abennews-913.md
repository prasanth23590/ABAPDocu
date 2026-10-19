---
title: "News for ABAP Release 9.13"
source_file: abennews-913.html
section: "ABAP Release News > News for ABAP Release 9.1x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 9.13

The kernel release for ABAP release 9.13 is 9.13.

## ABAP CDS

| Modification                             | Description                                                                                                                                                                                                 |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Client Safety of CDS Table Functions** | The annotation [`ClientHandling.clientSafe`](../../abap-core-data-services-abap-cds/abap-cds-annotations/abencds_1549616294_anno.md) declares a CDS table function explicitly as [client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md) and ensures the corresponding checks. |

## Internal Tables

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><code class="ph codeph">READ TABLE ... WHERE ...</code></strong></td>
<td><p>The addition <a href="abapread_table_where.html"><code class="ph codeph">WHERE</code></a> can now be used with the <a href="abapread_table.html"><code class="ph codeph">READ TABLE</code></a> statement. It reads the first line of an internal table that fulfills the <code class="ph codeph">WHERE</code> condition. In contrast to the addition <a href="abapread_table_free.html"><code class="ph codeph">WITH KEY</code></a>, arbitrary logical expressions can be specified instead of equality conditions only. The syntax offers an easier to use alternative to the following frequently used pattern but does not offer any performance gain.</p>
<pre class="abap"><code>LOOP AT itab ... [USING KEY ...] WHERE log_exp|(cond_syntax).
EXIT.
ENDLOOP.</code></pre>
<p>The same rules are valid as for using a <code class="ph codeph">WHERE</code> condition in other internal table statements ( <a href="abaploop_at_itab.html"><code class="ph codeph">LOOP AT</code></a>, <a href="abapmodify_itab.html"><code class="ph codeph">MODIFY</code></a>, <a href="abapdelete_itab.html"><code class="ph codeph">DELETE</code></a>) and must be taken into account. In particular, it is also possible to specify a dynamic <code class="ph codeph">WHERE</code> condition.</p></td>
</tr>
<tr class="even">
<td><strong><code class="ph codeph">IS [NOT] INITIAL</code> in <code class="ph codeph">WHERE</code> Condition of <code class="ph codeph">FILTER</code></strong></td>
<td>In the <a href="abenconstructor_expr_filter_basic.html">basic form</a> of the <a href="abenconstructor_expression_filter.html"><code class="ph codeph">FILTER</code></a> operator, the predicate <code class="ph codeph">IS [NOT] INITIAL</code> is now possible.</td>
</tr>
</tbody>
</table>

## ABAP SQL

| Modification                                              | Description                                                                                                                                                                                      |
|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Binary Floating Point Types in Arithmetic Expressions** | Operands of type `FLTP` or `f` can now be used in a [decimal floating point expression](../../abap-programming-language/abap-database-access/abensql_arith.md) and integer types can be used in a [binary floating expression](../../abap-programming-language/abap-database-access/abensql_arith.md). |

## Transformations

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Regular Expressions for XSLT</strong></td>
<td><p>Regular expression functions can now be used in XSLT. The following functions are available:</p>
<ul>
<li><a href="abenabap_xpath_fnctns.html"><code class="ph codeph">matches()</code></a></li>
<li><a href="abenabap_xpath_fnctns.html"><code class="ph codeph">replace()</code></a></li>
<li><a href="abenabap_sap_fnctns.html"><code class="ph codeph">tokenize()</code></a></li>
</ul></td>
</tr>
</tbody>
</table>

## ABAP RESTful Application Programming Model

In release 9.13, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

| Modification                        | Description                                                                                                                                                                    |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`authorization master ( none )`** | The authorization control type `none` can be specified for `authorization master` to implicitly mark operations in authorization-dependent entities with `authorization:none`. |

## Remote Function Call

| Modification            | Description                                                                                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **New Synchronous RFC** | A synchronous RFC call specifying a [remote session](../../abap-programming-language/abap-calling-and-exiting-program-units/abapcall_function_remote_session.md) is now possible using the syntax `CALL FUNCTION ... IN REMOTE SESSION ...`. |
