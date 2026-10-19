---
title: "News for ABAP Release 7.73"
source_file: abennews-773.html
section: "ABAP Release News > News for ABAP Release 7.7x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.73

The kernel release for ABAP release 7.73 is 7.73.

## Standard Database

| Modification                                    | Description                                                                                                                                                                                                                                                                                                        |
|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Only SAP HANA Database as Standard Database** | As of this release, only an [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) is supported as the [standard database](../../abap-glossary/abenstandard_db_glosry.md) of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). For this reason, Open SQL was renamed to ABAP SQL (see [ABAP SQL in ABAP Release 7.73](abennews-773.md#abap-sql)). |

## Assignments

<table>
<thead>
<tr class="header">
<th>Modification</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Convertibility of Structures</strong></td>
<td><p>The <a href="abenconversion_flat_flat.html">conversion rules for flat structures</a> are based on their <a href="abenunicode_fragment_view_glosry.html">fragment views</a>, where each <a href="abenalignment_gap_glosry.html">alignment gap</a> is considered as a fragment. Alignment gaps arise from the <a href="abenalignment_glosry.html">alignment</a> requirements of the component's data types. For character-like components, the alignment requirement depends on the character representation:</p>
<ul>
<li>For character representation <a href="abenucs2_glosry.html">UCS-2</a> used by the ABAP programming language, the memory address of character-like data objects must be divisible by 2.</li>
<li>For other character representations there are other alignment requirements. For example, the non-Unicode character representation <a href="abenascii_glosry.html">ASCII</a> has no alignment requirement while the Unicode character representation <a href="abenutf32_glosry.html">UTF-32</a> requires a divisibility by 4.</li>
</ul>
<p>Meanwhile, only <a href="abenunicode_system_glosry.html">Unicode systems</a> are supported. The system code page is <a href="abenutf16_glosry.html">UTF-16</a> and its subset <a href="abenucs2_glosry.html">UCS-2</a> is supported in the ABAP language. Any character is represented by 2 bytes and the alignment requirement is always a divisibility by 2.</p>
<p>Because of this, the conversion rules for flat structures can be less strict than before and the new determination of possible alignment gaps was introduced in ABAP release 7.73.</p>
<p><strong>Example:</strong> See below.</p></td>
</tr>
</tbody>
</table>

**Convertibility of Structures**

For example, the following assignment between two flat structures was not possible before ABAP release 7.73 but is possible now.

``` abap
TYPES: 
  BEGIN OF incl1, 
    num TYPE i, 
    c2  TYPE c LENGTH 2, 
  END OF incl1. 
 
DATA: 
  BEGIN OF struc1, 
    c1 TYPE c LENGTH 2. 
    INCLUDE TYPE incl1. 
DATA: 
    c3 TYPE c LENGTH 2, 
  END OF struc1. 
 
DATA: 
  BEGIN OF struc2, 
    c1  TYPE c LENGTH 2, 
    num TYPE i, 
    c2  TYPE c LENGTH 2, 
    c3  TYPE c LENGTH 2, 
  END OF struc2. 
 
struc1 = struc2.
```

In the included substructure `incl1`, the character component has the same alignment as the integer component and there is no alignment gap. As long as non-Unicode Systems were supported, however, an alignment gap had to be assumed behind the included structure in order to make the program executable in Unicode systems as well as in non-Unicode Systems.

## Internal Tables

| Modification                           | Description                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Stricter Syntax Check in `COLLECT`** | Before the statement [`COLLECT`](../../abap-programming-language/abap-processing-internal-data/abapcollect.md) can be executed for an internal table, all components that are not part of the primary table key must have a numeric data type. Until now, if certain structured components broke this rule, a syntax check warning and a program runtime error occurred. Now a syntax error occurs here too. |

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
<td><strong>Access to Hierarchy Data</strong></td>
<td><p>In queries, both</p>
<ul>
<li><a href="abenselect_hierarchy.html">hierarchies</a> and</li>
<li><p><a href="abenselect_hierarchy_node_navis.html">hierarchy node navigators</a></p>
<p>can be specified as <a href="abapselect_data_source.html">data sources</a>.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Subquery as Data Source of <code class="ph codeph">MODIFY</code></strong></td>
<td>In the ABAP SQL write statement <a href="abapmodify_dbtab.html"><code class="ph codeph">MODIFY</code></a>, a parenthesized subquery <a href="abapinsert_source.html"><code class="ph codeph">SELECT subquery_clauses</code></a> can now be specified as a data source after <code class="ph codeph">FROM</code>. The rows of the result set of the subquery are modified or inserted in the target table directly on the database. No data transport is required between the database and AS ABAP.</td>
</tr>
<tr class="odd">
<td><strong><code class="ph codeph">GROUP BY</code> Addition <code class="ph codeph">GROUPING SETS</code></strong></td>
<td>In a <a href="abapselect.html"><code class="ph codeph">SELECT</code></a> statement, the <a href="abapgroupby_clause.html"><code class="ph codeph">GROUP BY</code></a> addition <a href="abapgrouping_sets_clause.html"><code class="ph codeph">GROUPING SETS</code></a> can now be used. The addition <code class="ph codeph">GROUPING SETS</code> makes it possible to group multiple grouping sets under one <code class="ph codeph">GROUP BY</code> clause. This is the same as specifying <a href="abapunion.html"><code class="ph codeph">UNION ALL</code></a> with different <code class="ph codeph">GROUP BY</code> clauses. The addition <code class="ph codeph">GROUPING SETS</code> has an advantage over a <code class="ph codeph">UNION</code> clause grouping because the <code class="ph codeph">SELECT</code> clause only needs to be specified once.</td>
</tr>
<tr class="even">
<td><strong>Aggregate Function <code class="ph codeph">GROUPING</code></strong></td>
<td>The aggregate function <a href="abengrouping_function.html"><code class="ph codeph">GROUPING</code></a> can now be used in a <a href="abapselect.html"><code class="ph codeph">SELECT</code></a> statement. The grouping function <code class="ph codeph">GROUPING</code> can be used to verify whether a specific column is part of the <a href="abenaggregate_expression_glosry.html">aggregation</a>. The grouping function can be used only if the <a href="abapgroupby_clause.html"><code class="ph codeph">GROUP BY</code></a> clause contains the addition <a href="abapgrouping_sets_clause.html"><code class="ph codeph">GROUPING SETS</code></a>.</td>
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
<td><strong>CDS Hierarchies</strong></td>
<td>The new statement <a href="abencds_f1_define_hierarchy.html"><code class="ph codeph">DEFINE HIERARCHY</code></a> can be used to create <a href="abencds_hierarchy_glosry.html">CDS hierarchies</a> that are accessed as <a href="abensql_hierarchy_glosry.html">ABAP SQL hierarchies</a> in <a href="abenabap_sql_glosry.html">ABAP SQL</a> read statements.</td>
</tr>
<tr class="even">
<td><strong>New Condition <code class="ph codeph">IS INITIAL</code></strong></td>
<td>The new condition <a href="abencds_cond_expr_initial_v1.html"><code class="ph codeph">IS INITIAL</code></a> can be used to check the initial value of operands.</td>
</tr>
<tr class="odd">
<td><strong>Access Control</strong></td>
<td><p>The following enhancements have been implemented in <a href="abencds_access_control_glosry.html">CDS access control</a>:</p>
<ul>
<li>New Boolean predicates <a href="abencds_dcl_role_conditions.html"><code class="ph codeph">TRUE</code></a> and <a href="abencds_dcl_role_conditions.html"><code class="ph codeph">FALSE</code></a> can now be used as part of an <a href="abenaccess_condition_glosry.html">access condition</a>.</li>
<li><p>The following is now possible in an <a href="abeninherit_condition_glosry.html">inheritance condition</a> defined using <a href="abencds_f1_cond_inherit.html"><code class="ph codeph">INHERITING</code></a>:</p>
<ul>
<li>The new additions <code class="ph codeph">DEFAULT TRUE</code> and <code class="ph codeph">DEFAULT FALSE</code> can be specified.</li>
<li><code class="ph codeph">ROOT WITH</code> can be used to insert CDS elements in front of SQL path expressions.</li>
</ul></li>
<li>The syntax of <a href="abencds_f1_define_pfcg_mapping.html"><code class="ph codeph">DEFINE PFCG_MAPPING</code></a> was modified to make it possible to define the PFCG mapping using a freely selectable CDS entity <code class="ph codeph">mapping_entity</code>.</li>
</ul></td>
</tr>
</tbody>
</table>

## AMDP

| Modification                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **AMDP Scalar Functions**                 | In the implementation of [AMDP scalar functions](../../abap-glossary/abenamdp_scalar_function_glosry.md), it is now possible to specify the database-specific option [`DETERMINISTIC`](../../abap-programming-language/abap-database-access/abapmethod_by_db_proc.md) after `OPTIONS`. This buffers the result of the function for the duration of a query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Option `CDS SESSION CLIENT` Mandatory** | The option [`CDS SESSION CLIENT`](../../abap-programming-language/abap-database-access/abapmethods_amdp_options_client.md) is now mandatory when an AMDP method accesses the [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md) of a [CDS view](../../abap-glossary/abencds_view_glosry.md) whose [client handling](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_view_client_handling_v1.md) is determined by the annotation [`@ClientHandling.algorithm: #SESSION_VARIABLE`](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_view_client_handling_v1.md). If this option is not specified in this case, a syntax error occurs. The option sets the [session variable](../../abap-glossary/abensession_variable_glosry.md) of the database that can be addressed under the name [`$session.client`](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_session_variable_v1.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) of the [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) to a particular value when the method is called from ABAP. An exception of the class `CX_AMDP_CDS_CLIENT_MISMATCH` can now no longer be raised. |

## Type Checks

| Modification                                | Description                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Checks on `STRUCTURE` Typing**            | In obsolete `STRUCTURE` typing of formal parameters and field symbols, one assigned data object must be at least as long as the structure in question. Typing checks now respect the [alignment gaps](../../abap-glossary/abenalignment_gap_glosry.md) at the end of the data object and the structure.                                                                        |
| **Checks on Literals as Actual Parameters** | The value of a literal passed to a procedure must not be modified in the procedure. In certain cases this was, however, possible, namely when [literals as actual parameters](../../abap-programming-language/abap-declarations/abentyping_literals.md) were passed to differently typed `CHANGING` parameters of subroutines. This is now prevented by stricter checks and always produces a runtime error. |

## ABAP RESTful Application Programming Model

From release 7.73 on, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) is introduced.

This mainly involves:

- [RAP Business Services (BS)](../../abap-rap-business-objects/abencds_business_services.md)

- [RAP Business Objects (RAP BO)](../../abap-rap-business-objects/abenabap_rap.md)

  - [BDL for Behavior Definitions](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl.md)

  - [ABAP Behavior Pools (ABP)](../../abap-rap-business-objects/abap-for-rap-business-objects/abenabap_behavior_pools.md)

- [ABAP EML](../../abap-rap-business-objects/abap-for-rap-business-objects/abeneml.md)

- [BDEF Derived Types](../../abap-rap-business-objects/abap-for-rap-business-objects/abenrpm_derived_types.md) in the ABAP type concept.

In the beginning, so-called [unmanaged RAP BOs](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) can be created with the addition [`unmanaged`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_impl_type.md) of the [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) when defining a [RAP BO](../../abap-glossary/abenrap_bo_glosry.md). This scenario is intended for brownfield developments with existing application code. All operations and services must be implemented by the application developer.
