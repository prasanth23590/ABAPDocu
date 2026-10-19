---
title: "News for ABAP Release 7.67"
source_file: abennews-767.html
section: "ABAP Release News > News for ABAP Release 7.6x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.67

The kernel release for ABAP release 7.67 is 7.51.

## ABAP Objects

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Implementing Interfaces</strong></td>
<td><p>When implementing interfaces in classes with the statement <a href="abapinterfaces_class.html"><code class="ph codeph">INTERFACES</code></a>, the following restrictions do not apply:</p>
<ul>
<li>Methods and attributes of component interfaces of the implemented interface can now be specified after the additions <code class="ph codeph">ABSTRACT METHODS</code>, <code class="ph codeph">FINAL METHODS</code>, and <code class="ph codeph">DATA VALUES</code> using the name of the component interface and the <a href="abeninterface_comp_selector_glosry.html">interface component selector</a><code class="ph codeph">~</code>. Until now, this was only possible for methods by using an <a href="abenalias_glosry.html">alias name</a>, for attributes the interface itself had to be included.</li>
<li>Attributes that are declared in component interfaces can now be specified after the addition <code class="ph codeph">DATA VALUES</code> by using <a href="abenalias_glosry.html">alias names</a>.</li>
</ul></td>
</tr>
</tbody>
</table>

## Expressions and Functions

| Modification                                          | Description                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Exception Object After `RAISE EXCEPTION`**          | The operand position for the reference variable `oref` of the statement [`RAISE EXCEPTION oref`](../../abap-programming-language/abap-program-flow-logic/abapraise_exception_class.md) is now a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md).                                                                                                              |
| **Object Component Selector After Table Expressions** | If an [object component selector `->`](../../abap-programming-language/abap-processing-internal-data/abentable_exp_chaining.md) is specified directly after a [table expression](../../abap-programming-language/abap-processing-internal-data/abentable_expressions.md), the restriction that this is not possible for table expressions whose [result](../../abap-programming-language/abap-processing-internal-data/abentable_exp_result.md) is determined with the value operator `VALUE` no longer applies. |

## ABAP SQL

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Path Expressions</strong></td>
<td><p>The following enhancements have been made to <a href="abenabap_sql_path.html">path expressions</a> that are specified as a <a href="abapselect_data_source.html">data source</a> of the <a href="abapfrom_clause.html"><code class="ph codeph">FROM</code> clause</a> of <code class="ph codeph">SELECT</code> statements of a <a href="abenasql_query_glosry.html">query</a>:</p>
<ul>
<li>When using a path expression, <a href="abenabap_sql_parameters.html">actual parameters</a> can now be passed to CDS entities with input parameters. Path expressions can now contain CDS associations for entities with input parameters.</li>
<li><a href="abenabap_sql_path_filter.html">Filter conditions</a> for CDS associations can now be specified in path expressions.</li>
<li>Path expressions can now be split over several source code rows at the blanks in the syntax for parameter passes and filter conditions and also before slashes (<code class="ph codeph">/</code>).</li>
</ul></td>
</tr>
</tbody>
</table>

## Messages

| Modification                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Implicit Message Specification in `RAISE EXCEPTION MESSAGE`** | A new short form [`USING MESSAGE`](../../abap-programming-language/abap-program-flow-logic/abapraise_exception_message.md) of statement [`RAISE_EXCEPTION`](../../abap-programming-language/abap-program-flow-logic/abapraise_exception_class.md) with the addition [`MESSAGE`](../../abap-programming-language/abap-program-flow-logic/abapraise_exception_message.md) makes it possible to pass the content of system fields `sy-msg...` implicitly to the exceptions of exception classes that include the system interface [`IF_T100_DYN_MSG`](../../abap-programming-language/abap-text-repositories/abenif_t100_dyn_msg.md). |
