---
title: "News for ABAP Release 7.72"
source_file: abennews-772.html
section: "ABAP Release News > News for ABAP Release 7.7x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.72

The kernel release for ABAP release 7.72 is 7.72.

## Internal Tables

| Modification                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Predicates in `WHERE` Conditions** | In `WHERE` conditions of the statements [`LOOP AT itab`](../../abap-programming-language/abap-processing-internal-data/abaploop_at_itab_variants.md), [`DELETE itab`](../../abap-programming-language/abap-processing-internal-data/abapdelete_itab.md), and [`MODIFY itab`](../../abap-programming-language/abap-processing-internal-data/abapmodify_itab.md), and in table iterations with [`FOR`](../../abap-programming-language/abap-processing-internal-data/abenfor_itab.md), [`IS [NOT] INSTANCE OF`](../../abap-programming-language/abap-program-flow-logic/abenlogexp_instance_of.md) can now be specified alongside the predicate expressions [`IS [NOT] INITIAL`](../../abap-programming-language/abap-program-flow-logic/abenlogexp_initial.md) and [`IS [NOT] BOUND`](../../abap-programming-language/abap-program-flow-logic/abenlogexp_bound.md). |

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
<td><strong>Date/Time Functions</strong></td>
<td><p>ABAP SQL now supports the following new time zone functions:</p>
<ul>
<li><a href="abensql_timezone_func.html"><code class="ph codeph">ABAP_SYSTEM_TIMEZONE</code></a></li>
<li><a href="abensql_timezone_func.html"><code class="ph codeph">ABAP_USER_TIMEZONE</code></a></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Relational Expression <code class="ph codeph">IS INITIAL</code></strong></td>
<td>The relational expression <a href="abenwhere_logexp_initial.html"><code class="ph codeph">IS [NOT] INITIAL</code></a> can now be used in a condition <a href="abenasql_cond.html"><code class="ph codeph">sql_cond</code></a> to compare operands with their type-dependent initial value.</td>
</tr>
<tr class="odd">
<td><strong>Exposing CDS Associations of Common Table Expressions</strong></td>
<td>When <a href="abencds_view_glosry.html">CDS views</a> are accessed within a <a href="abencommon_table_expression_glosry.html">common table expression</a>, the addition <a href="abapwith_associations.html"><code class="ph codeph">WITH ASSOCIATIONS</code></a> of the statement <a href="abapwith.html"><code class="ph codeph">WITH</code></a> can now be used to expose <a href="abencds_association_glosry.html">CDS associations</a> of these views for use in <a href="abenabap_sql_path.html">path expressions</a> of the current <code class="ph codeph">WITH</code> statement. The addition <code class="ph codeph">REDIRECTED TO</code> can also be used to replace the <a href="abenassociation_target_glosry.html">association target</a> of the exposed CDS association with a previous CTE or the current CTE.</td>
</tr>
<tr class="even">
<td><strong>Numeric Literals in the <code class="ph codeph">SELECT</code> List</strong></td>
<td>Until now, only those <a href="abennumeric_literal_glosry.html">numeric literals</a> whose value matched the value range of the type <a href="abenddic_builtin_types.html"><code class="ph codeph">INT4</code></a> could be specified as <a href="abensql_elem.html">elementary SQL expressions</a> in the <a href="abapselect_list.html"><code class="ph codeph">SELECT</code> list</a> of a query. Now numeric literals of up to 31 digits can be specified, which are interpreted as numbers of the type <a href="abenddic_builtin_types.html"><code class="ph codeph">DEC</code></a> if the value range of <code class="ph codeph">INT4</code> is exceeded.</td>
</tr>
<tr class="odd">
<td><strong>Enhanced Cast Matrix</strong></td>
<td>A <a href="abensql_cast.html">cast expression</a> can now be used to convert the data types <code class="ph codeph">INT1</code>, <code class="ph codeph">INT2</code>, <code class="ph codeph">INT4</code>, and <code class="ph codeph">INT8</code> to <code class="ph codeph">DEC</code>.</td>
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
<td><strong>Literals</strong></td>
<td>A <a href="abencds_literal_v1.html">numeric literal</a> whose value is outside the value range of <code class="ph codeph">INT4</code> but within the value range of <code class="ph codeph">INT8</code> is now handled like a field of type <code class="ph codeph">INT8</code> everywhere, including the definition of CDS associations.</td>
</tr>
<tr class="even">
<td><strong>Access Control</strong></td>
<td><p>The following enhancements have been implemented in <a href="abencds_access_control_glosry.html">CDS access control</a>:</p>
<ul>
<li>New <a href="abencds_f1_cond_inherit.html">inheritance conditions</a> can be used as <a href="abencds_dcl_role_conditions.html">access conditions</a> in <a href="abencds_role_glosry.html">CDS roles</a>. Some inheritance conditions apply conditions from existing CDS roles and some inheritance conditions apply access rules defined for other CDS entities.</li>
<li>In a <a href="abencds_f1_cond_pfcg.html">PFCG condition</a>, a <a href="abencds_pfcg_mapping_glosry.html">PFCG mapping</a> can be <a href="abencds_f1_cond_pfcg_mapping.html">mapped</a> to an element list. This mapping assigns the CDS elements to the authorization fields of an authorization object. A PFCG mapping is defined in a <a href="abencds_access_policy_glosry.html">CDS access policy</a> using <a href="abencds_f1_define_pfcg_mapping.html"><code class="ph codeph">DEFINE PFCG_MAPPING</code></a>.</li>
</ul></td>
</tr>
</tbody>
</table>

## AMDP

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>AMDP Scalar Functions</strong></td>
<td><a href="abenamdp_scalar_function_glosry.html">AMDP</a> scalar functions are now supported alongside <a href="abenamdp_table_function_glosry.html">AMDP table functions</a>. The <a href="abenamdp_function_methods.html">AMDP function implementation</a> of an AMDP scalar function has an elementary return value and can be used in ABAP like a regular function method.</td>
</tr>
<tr class="even">
<td><strong>Restrictions Removed</strong></td>
<td><p>When a replacement parameter declared using <a href="abapmethods_general.html"><code class="ph codeph">DEFAULT</code></a> is specified for an elementary input parameter of an <a href="abenamdp_methods.html">AMDP method</a>, the following (previously undocumented) restrictions were lifted:</p>
<ul>
<li>Constants declared using the addition <a href="abapdata_options.html"><code class="ph codeph">VALUE IS INITIAL</code></a> can now be specified for the data types <code class="ph codeph">d</code>, <code class="ph codeph">t</code>, and <code class="ph codeph">x</code>. This previously produced a syntax error.</li>
<li>Constants declared using the addition <a href="abapdata_options.html"><code class="ph codeph">VALUE '00010101'</code></a> can now be specified for the data type <code class="ph codeph">d</code>, or the literal <code class="ph codeph">'00010101'</code> can be specified directly. Both previously produced a syntax error.</li>
<li><p>Constants declared by specifying numeric literals after <a href="abapdata_options.html"><code class="ph codeph">VALUE</code></a> and whose lengths are not precisely 8 or 6 can now be specified for the data types <code class="ph codeph">d</code> and <code class="ph codeph">t</code>. This previously produced a syntax error. Until now, values of literals with lengths of precisely 8 or 6 were handled like a string. This incorrect behavior was also modified and the numeric value is handled as the number of days since 01.01.001 or as the number of seconds since 00:00:00. This modification is incompatible if an <a href="abenamdp_procedure_glosry.html">AMDP procedure</a> or <a href="abenamdp_function_glosry.html">function</a> with an input parameter of this type is called from other <a href="abendatabase_procedure_glosry.html">database procedures</a> or <a href="abendatabase_function_glosry.html">functions</a> without an actual parameter being assigned to the parameter in question.</p>
<p>In AMDP methods, the addition <code class="ph codeph">DEFAULT</code> now behaves in the same way as in regular methods. It still cannot be specified for the data types <code class="ph codeph">string</code>, <code class="ph codeph">xstring</code>, <code class="ph codeph">decfloat16</code>, and <code class="ph codeph">decfloat34</code>, however, and no literals can be specified that cannot be converted into the data type of the input parameter.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Exception Handling

| Modification                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Raising Runtime Errors**                       | The new statement [`RAISE SHORTDUMP`](../../abap-programming-language/abap-program-flow-logic/abapraise_shortdump.md) raises [runtime errors](../../abap-glossary/abenruntime_error_glosry.md) linked with an [exception object](../../abap-glossary/abenexception_object_glosry.md). This means more information can now be passed to the [short dump](../../abap-glossary/abenshort_dump_glosry.md) than was previously possible in an [exit message](../../abap-glossary/abenexit_message_glosry.md).                                                                                                                                       |
| **Last Message in a Chain of Exception Objects** | The new method `GET_LATEST_T100_EXCEPTION` in the class `CL_MESSAGE_HELPER` is used to return the last object in a chain of exception objects that has an [exception text](../../abap-programming-language/abap-program-flow-logic/abenexception_texts.md) defined by a message. Here, the chain is created using the attribute `PREVIOUS`.                                                                                                                                                                                                                            |
| **Setting the Attribute `IS_RESUMABLE`**         | After an exception is raised using the statement [`RAISE RESUMABLE EXCEPTION`](../../abap-programming-language/abap-program-flow-logic/abapraise_exception_class.md) and caught using the statement [`CATCH BEFORE UNWIND`](../../abap-programming-language/abap-program-flow-logic/abapcatch_try.md), the attribute `IS_RESUMABLE` is set for all previous exception objects referenced in the attribute `PREVIOUS` and not just for the current exception object. Up until the first resumable exception in the chain `IS_RESUMABLE` is set to the value of `abap_true` and is set to the value of `abap_false` otherwise. |

## iXML Library

| Modification                    | Description                                                                                                                                                                                             |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **iXML Library for ABAP Cloud** | The [iXML Library](../../abap-programming-language/abap-data-interchange-formats/abenabap_ixml_lib_cloud.md) now provides a wrapper API to handle XML documents in ABAP for Cloud Development. To access the iXML Library, use the syntax `cl_ixml_core()=>create`. |

## Transformations for ABAP Release 7.72

| Modification                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Resumable Exceptions in Deserializations with ST** | The new transformation option [`OPTIONS exceptions = 'resumable'`](../../abap-programming-language/abap-data-interchange-formats/abapcall_transformation_options.md) can be used to make exceptions of the class `CX_ST_DESERIALIZATION_ERROR` into resumable exceptions. In handling with [`CATCH BEFORE UNWIND`](../../abap-programming-language/abap-program-flow-logic/abapcatch_try.md), the new attribute `RESULT_REF_FOR_RESUME` of the exception object of the class `CX_ST_DESERIALIZATION_ERROR` points to the target field where the exception was raised. The canceled transformation can be resumed using [`RESUME`](../../abap-programming-language/abap-program-flow-logic/abapresume.md). |
