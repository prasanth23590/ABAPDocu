---
title: "News for ABAP Release 7.88"
source_file: abennews-788.html
section: "ABAP Release News > News for ABAP Release 7.8x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.88

The kernel release for ABAP release 7.88 is 7.88.

## ABAP CDS

| Modification                              | Description                                                                                                                                                                                                                                                                                     |
|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CDS View Entity, `SUBSTRING` Function** | In [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), the [`SUBSTRING`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_sql_functions_character_v2.md) function has been enhanced. It now accepts not only literals, but also fields, parameters, expressions, and built-in functions as arguments for the parameters `pos` and `len`. |

## ABAP CDS Access Control

| Modification                                                                    | Description                                                                                                                                                                                           |
|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`IF ... THEN ... ELSE ...` Control Structure Available in Access Conditions** | Control structures [`IF ... THEN ... ELSE ...`](../../abap-core-data-services-abap-cds/abap-cds-access-control/abencds_f1_dcl_ifthenelse.md) can now be used as part of an [access condition](../../abap-glossary/abenaccess_condition_glosry.md) after the `DEFINE ROLE` statement. |

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
<td><strong>String Functions Processed by the ABAP SQL In-Memory Engine</strong></td>
<td>The <a href="abensql_string_func.html">string functions</a> <code class="ph codeph">LEFT</code>, <code class="ph codeph">LOWER</code>, <code class="ph codeph">RIGHT</code>, <code class="ph codeph">UPPER</code>, and <code class="ph codeph">SUBSTRING</code> can be processed by the <a href="abenabap_sql_inmemeng.html">ABAP SQL in-memory engine</a> now. They no longer bypass <a href="abentable_buffering_glosry.html">table buffering</a> and do not cause the transport of an internal table accessed by <a href="abapselect_itab.html"><code class="ph codeph">FROM @itab</code></a> to the database. While <code class="ph codeph">LEFT</code>, <code class="ph codeph">LOWER</code>, <code class="ph codeph">RIGHT</code>, and <code class="ph codeph">UPPER</code> were not supported at all, <code class="ph codeph">SUBSTRING</code> was supported under certain conditions.</td>
</tr>
<tr class="even">
<td><strong>Table Buffering for Decimal Floating Point Calculations</strong></td>
<td><p>Calculations for the built-in types <a href="abenddic_builtin_types.html"><code class="ph codeph">DECFLOAT16</code></a> and <a href="abenddic_builtin_types.html"><code class="ph codeph">DF16_DEC</code></a> no longer bypass table buffering. The calculation in the table buffer is done with the respective decimal floating point arithmetic. The following differences to ABAP and to the database must be considered:</p>
<ul>
<li>In ABAP, the <a href="abencalculation_type_glosry.html">calculation type</a> for <code class="ph codeph">decfloat16</code> is <code class="ph codeph">decfloat34</code>.</li>
<li>On the database, the built-in type <code class="ph codeph">DF16_DEC</code> is handled as a packed number.</li>
</ul>
<p>Both can lead to different results.</p></td>
</tr>
</tbody>
</table>

## Data Clusters

| Modification                         | Description                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Import of Type `n` into Type `c`** | The statement [`IMPORT`](../../abap-programming-language/abap-data-cluster/abapimport_data_cluster.md) now allows assignments of data of type [`n` to data objects of type `c`](../../abap-programming-language/abap-data-cluster/abapimport_parameterlist.md) if they have the same length. This change might lead to incompatible behavior if handling of the former exception leads to different results than the new behavior. |

## ABAP RESTful Application Programming Model

In release 7.88, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

| Modification                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CDS Interface Behavior Definitions**       | A new [implementation type](../../abap-glossary/abencds_bdef_impl_type_glosry.md) is available: the [RAP interface behavior definition](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_rap_bo_interface.md). Such interface BDEFs are based on [CDS transactional interfaces](../../abap-glossary/abencds_trans_interface_glosry.md) and define the behavior of a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md). The overall purpose of a RAP BO interface is to project a business object for stable consumption. |
| **Managed RAP BO, New Field Characteristic** | In [managed RAP business objects](../../abap-glossary/abenmanaged_rap_bo_glosry.md), a new field characteristic is available: [`field(suppress)`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_field_char.md). It removes the field in question from the [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) and from all RAP APIs.                                                                                                                                                                |
| **Managed RAP BO, `with full data`**         | In [managed RAP business objects](../../abap-glossary/abenmanaged_rap_bo_glosry.md), the optional addition [`with full data`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_saving.md) can be used in combination with one of the [RAP saving options](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_saving.md) to ensure that full instance data is handed over to the `save_modified` method of the RAP saver class in the ABAP behavior pool.                                                                                           |
| **Abstract BDEF, New Field Characteristic**  | In [RAP abstract behavior definitions](../../abap-glossary/abencds_abstract_bdef_glosry.md), a new [RAP field characteristic](../../abap-glossary/abenrap_field_char_glosry.md) is available: [`mandatory:execute`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_field_abstract.md). It declares the field in question as mandatory. Whenever the hierarchical type is used as input parameter for a RAP action or a RAP function, a value must be supplied.                                                            |
