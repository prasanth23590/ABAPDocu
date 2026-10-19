---
title: "News for ABAP Release 7.62"
source_file: abennews-762.html
section: "ABAP Release News > News for ABAP Release 7.6x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.62

The kernel releases for ABAP release 7.62 are 7.45 and 7.46.

## News for ABAP Release 7.62 with Kernel 746

### Assignments

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>System Class for Dynamic Mapping</strong></td>
<td><p>The new methods <a href="abencl_abap_corresponding_2.html"><code class="ph codeph">CREATE_USING</code></a> and <a href="abencl_abap_corresponding_2.html"><code class="ph codeph">EXECUTE_USING</code></a> for making assignments between internal tables by component while using lookup tables have been added to the system class <a href="abencl_abap_corresponding.html"><code class="ph codeph">CL_ABAP_CORRESPONDING</code></a>.</p>
<p>If the method <a href="abencl_abap_corresponding_1.html"><code class="ph codeph">EXECUTE</code></a> for simple assignment is used, the restriction that source and target cannot be identical has been lifted. It should be noted, however, that no temporary copy of the source is created as a target object (like in <a href="abapmove-corresponding.html"><code class="ph codeph">MOVE-CORRESPONDING</code></a>), which means that the result in the case of overlapping source and target components is different than when the operator <a href="abencorresponding_constr_arg_type.html"><code class="ph codeph">CORRESPONDING</code></a> is used reflexively.</p></td>
</tr>
</tbody>
</table>

## News for ABAP Release 7.62 with Kernel 745

### Data Types and ABAP Dictionary

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>New Built-In ABAP Type <code class="ph codeph">int8</code></strong></td>
<td><p>The new built-in data type <a href="abenbuiltin_types_numeric.html"><code class="ph codeph">int8</code></a> enables 8-byte integers with signs to be declared.</p>
<ul>
<li>The associated data type in ABAP Dictionary was introduced with the name <a href="abenddic_builtin_types.html"><code class="ph codeph">INT8</code></a>.</li>
<li>The <a href="abenbuiltin_types_numeric.html">value range</a> of the new data type <code class="ph codeph">int8</code> is -9,223,372,036,854,775,808 to +9,223,372,036,854,775,807.</li>
<li><p>Apart from the extended value range, the new data type <code class="ph codeph">int8</code> has the same properties as the existing data type <a href="abenbuiltin_types_numeric.html"><code class="ph codeph">i</code></a> for 4-byte integers, with the following exceptions:</p>
<ul>
<li>The <a href="abenalignment.html">alignment required</a> for data objects of type <code class="ph codeph">int8</code> is an address divisible by 8.</li>
<li>A new <a href="abenarith_type.html">calculation type</a> has been introduced for <code class="ph codeph">int8</code>, situated between <code class="ph codeph">i</code> and <code class="ph codeph">p</code> in the hierarchy.</li>
</ul></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Global Temporary Tables</strong></td>
<td>Database tables in ABAP Dictionary can be defined using the table category <a href="abenddic_database_tables_gtt.html">global temporary table</a>. A global temporary table (GTT) can only be filled with temporary data during a database LUW. When a GTT is filled using ABAP SQL, it must be emptied again explicitly before the next implicit database commit. If not, an uncatchable exception is raised.</td>
</tr>
<tr class="odd">
<td><strong>Value Ranges of Domains</strong></td>
<td>When the <a href="abenddic_domains_sema.html">value range of a domain</a> is defined, the data types <code class="ph codeph">INT1</code>, <code class="ph codeph">INT2</code>, and <code class="ph codeph">INT4</code> are now checked (like <code class="ph codeph">INT8</code>) to determine whether the fixed values and interval boundaries are valid values, that is, that they lie within the <a href="abenddic_builtin_types.html">value range</a> defined by the technical properties. Existing domains with invalid value ranges must be corrected.</td>
</tr>
</tbody>
</table>

### Expressions and Functions in ABAP Release 7.62

| Modification                                 | Description                                                                                                                                                                                                                                                                                                                                     |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Predicate Expression for Type Inspection** | The new predicate expression [`IS INSTANCE OF`](../../abap-programming-language/abap-program-flow-logic/abenlogexp_instance_of.md) can be used to detect the [dynamic type](../../abap-glossary/abendynamic_type_glosry.md) of an [object reference variable](../../abap-glossary/abenobject_refer_variable_glosry.md). This makes it possible to check the feasibility of a [downcast](../../abap-glossary/abendown_cast_glosry.md) before it is executed. |
| **Case Distinction for Type Inspection**     | The special statement [`CASE TYPE OF`](../../abap-programming-language/abap-program-flow-logic/abapcase_type.md) makes it possible to check the [dynamic type](../../abap-glossary/abendynamic_type_glosry.md) of an [object reference variable](../../abap-glossary/abenobject_refer_variable_glosry.md) as a case distinction.                                                                                                          |

### ABAP SQL in ABAP Release 7.62

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Subquery as Data Source of <code class="ph codeph">INSERT</code></strong></td>
<td>In the ABAP SQL write statement <a href="abapinsert_dbtab.html"><code class="ph codeph">INSERT</code></a>, a parenthesized subquery <a href="abapinsert_source.html"><code class="ph codeph">SELECT subquery_clauses</code></a> can now be specified as a data source after <code class="ph codeph">FROM</code>. The rows of the result set of the subquery are inserted into the target table directly on the database. No data transport is required between the database and AS ABAP.</td>
</tr>
<tr class="even">
<td><strong>SQL Functions</strong></td>
<td><p>The following changes have been made:</p>
<ul>
<li><p>New Numeric Function</p>
<p>The new function <a href="abensql_arith_func.html"><code class="ph codeph">ROUND</code></a> rounds numeric values.</p></li>
<li><p>New String Functions</p>
<p>The new functions <a href="abensql_string_func.html"><code class="ph codeph">CONCAT</code></a>, <a href="abensql_string_func.html"><code class="ph codeph">LPAD</code></a>, <a href="abensql_string_func.html"><code class="ph codeph">LENGTH</code></a>, <a href="abensql_string_func.html"><code class="ph codeph">LTRIM</code></a>, <a href="abensql_string_func.html"><code class="ph codeph">REPLACE</code></a>, <a href="abensql_string_func.html"><code class="ph codeph">RIGHT</code></a>, <a href="abensql_string_func.html"><code class="ph codeph">RTRIM</code></a>, and <a href="abensql_string_func.html"><code class="ph codeph">SUBSTRING</code></a> perform operations on strings.</p></li>
<li><p>Coalesce Function Expanded</p>
<p>The <a href="abensql_coalesce.html">coalesce function</a> can now have 255 arguments instead of just two and returns the value of the first argument that does not have the null value.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>SQL Expressions</strong></td>
<td>Columns of the built-in dictionary type <code class="ph codeph">SSTRING</code> can now be used in the <a href="abensql_expression_glosry.html">SQL expressions</a> <a href="abensql_case.html"><code class="ph codeph">CASE</code></a> and the <a href="abensql_coalesce.html">coalesce function</a>.</td>
</tr>
<tr class="even">
<td><strong>Host Expressions</strong></td>
<td>From ABAP release 7.62, <a href="abenabap_sql_host_expressions.html">host expressions</a> can be specified for the work areas <code class="ph codeph">wa</code> or the internal tables <code class="ph codeph">itab</code> (from which the data is taken) in the write statements <a href="abapinsert_dbtab.html"><code class="ph codeph">INSERT</code></a>, <a href="abapupdate.html"><code class="ph codeph">UPDATE</code></a>, <a href="abapmodify_dbtab.html"><code class="ph codeph">MODIFY</code></a>, and <a href="abapdelete_dbtab.html"><code class="ph codeph">DELETE</code></a>.</td>
</tr>
<tr class="odd">
<td><strong>CDS Path Expressions</strong></td>
<td>From ABAP release 7.62, <a href="abenabap_sql_path.html">path expressions</a> can be used as <a href="abapselect_data_source.html">data sources</a> of the <a href="abapfrom_clause.html"><code class="ph codeph">FROM</code> clause</a> of the statement <a href="abapselect.html"><code class="ph codeph">SELECT</code></a>.</td>
</tr>
<tr class="even">
<td><strong>Access to Global Temporary Tables</strong></td>
<td>When the new <a href="abenglobal_temporary_table_glosry.html">global temporary tables</a> in ABAP Dictionary are accessed using ABAP SQL, all temporary data stored here is guaranteed to be deleted before the next implicit <a href="abendatabase_commit_glosry.html">database commit</a>, If not, a runtime error occurs.</td>
</tr>
<tr class="odd">
<td><strong><code class="ph codeph">ON</code> Conditions</strong></td>
<td>From ABAP release 7.62, the full <code class="ph codeph">ON</code> condition or subconditions of <a href="abapselect_join.html">joins</a> can be specified dynamically as <a href="abenwhere_logexp_dynamic.html"><code class="ph codeph">(cond_syntax)</code></a>. This is not possible if the full <a href="abapfrom_clause.html"><code class="ph codeph">FROM</code> clause</a> is specified dynamically as <code class="ph codeph">(cond_syntax)</code>.</td>
</tr>
<tr class="even">
<td><strong>System Classes</strong></td>
<td><p>The new system class <code class="ph codeph">CL_DBI_UTILITIES</code> contains utility methods for the database interface.</p>
<p>The documented method <code class="ph codeph">IS_LOGGING_ON</code> can be used to verify whether <a href="abenddic_database_tables_protocol.html">logging</a> is currently switched on for a database table.</p></td>
</tr>
</tbody>
</table>

### ABAP CDS

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Session Variables</strong></td>
<td>When a <a href="abencds_view_glosry.html">CDS view</a> is accessed using ABAP SQL, three session variables (<a href="abencds_session_variable_v1.html"><code class="ph codeph">$session.user</code></a>, <a href="abencds_session_variable_v1.html"><code class="ph codeph">$session.client</code></a>, and <a href="abencds_session_variable_v1.html"><code class="ph codeph">$session.system_language</code></a>) can be accessed here. In these variables, the values of the system fields <code class="ph codeph">sy-uname</code>, <code class="ph codeph">sy-mandt</code> and <code class="ph codeph">sy-langu</code> are available.</td>
</tr>
<tr class="even">
<td><strong>Expressions and Functions</strong></td>
<td><p>The following changes have been made:</p>
<ul>
<li>A <a href="abencds_cast_expression_v1.html"><code class="ph codeph">CAST</code> expression</a> now contain nested cast expressions and <a href="abencds_case_expression_v1.html">case distinctions</a> as an operand.</li>
<li>The following additional string functions are now supported: <a href="abencds_sql_functions_character_v1.html"><code class="ph codeph">CONCAT_WITH_SPACE</code></a>, <a href="abencds_sql_functions_character_v1.html"><code class="ph codeph">LEFT</code></a>, <a href="abencds_sql_functions_character_v1.html"><code class="ph codeph">INSTR</code></a>, <a href="abencds_sql_functions_character_v1.html"><code class="ph codeph">RIGHT</code></a>, and <a href="abencds_sql_functions_character_v1.html"><code class="ph codeph">RPAD</code></a>.</li>
<li><a href="abencds_parameter_v1.html">Input parameters</a> from the parameter list <a href="abencds_parameter_list_v1.html"><code class="ph codeph">parameter_list</code></a> of a CDS view can be passed to many parameters of <a href="abencds_builtin_functions_v1.html">built-in functions</a>.</li>
<li>A one character literal with the type <code class="ph codeph">NUMC</code> can now be <a href="abencds_cond_expr_types_v1.html">compared</a> with a data source of the type <code class="ph codeph">LANG</code>.</li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Exposing CDS Associations</strong></td>
<td>Path expressions can now be <a href="abencds_select_list_association_v1.html">exposed</a> with more than one CDS association in the <a href="abencds_select_list_v1.html"><code class="ph codeph">SELECT</code> list</a> of a CDS view. The fields of the <a href="abenassociation_source_glosry.html">association source</a> from the <code class="ph codeph">ON</code> condition of the exposed CDS association, which then also need to be specified, must be defined using an appropriately specified path.</td>
</tr>
</tbody>
</table>

### Further Changes

| Modification                | Description                                                                                        |
|-----------------------------|----------------------------------------------------------------------------------------------------|
| **Short Texts in ABAP Doc** | It is now possible to define short texts in [ABAP Doc comments](../../abap-glossary/abenabap_doc_comment_glosry.md). |
