---
title: "News for ABAP Release 7.68"
source_file: abennews-768.html
section: "ABAP Release News > News for ABAP Release 7.6x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.68

The kernel release for ABAP release 7.68 is 7.52.

## Assignments

| Modification                         | Description                                                                                                                                                                                                                                                                             |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **System Class for Dynamic Mapping** | The system class [`CL_ABAP_CORRESPONDING`](../../abap-programming-language/abap-processing-internal-data/abencl_abap_corresponding.md) now has a new method [`CREATE_WITH_VALUE`](../../abap-programming-language/abap-processing-internal-data/abencl_abap_corresponding_3.md), which allows the values of any suitable data objects to be assigned to the components of the target structure or target table. |

## ABAP SQL

| Modification             | Description                                                                                                                                                                                                                                                                                                                     |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Conversion Functions** | The new type conversion functions [`BINTOHEX`](../../abap-programming-language/abap-database-access/abensql_type_conv_func.md) and [`HEXTOBIN`](../../abap-programming-language/abap-database-access/abensql_type_conv_func.md) make it possible to convert byte strings to character strings (and the other way round) in [SQL expressions](../../abap-programming-language/abap-database-access/abapsql_expr.md), which is not possible with a [`CAST`](../../abap-programming-language/abap-database-access/abensql_cast.md) expression. |

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
<td><strong>AMDP Options</strong></td>
<td><p>The new addition <a href="abapmethods_amdp_options.html"><code class="ph codeph">AMDP OPTIONS</code></a> for <a href="abapmethods.html"><code class="ph codeph">METHODS</code></a> and <a href="abapclass-methods.html"><code class="ph codeph">CLASS-METHODS</code></a> statements can be used to define attributes of <a href="abenamdp_method_glosry.html">AMDP methods</a> in their declaration:</p>
<ul>
<li>The <a href="abapmethods_amdp_options.html"><code class="ph codeph">READ-ONLY</code></a> option only allows reads in the implementation of the AMDP methods.</li>
<li>The <a href="abapmethods_amdp_options_client.html"><code class="ph codeph">CDS SESSION CLIENT</code></a> option sets the <a href="abensession_variable_glosry.html">session variable</a> <code class="ph codeph">CDS_CLIENT</code> of the database that can be addressed under the name <a href="abencds_session_variable_v1.html"><code class="ph codeph">$session.client</code></a> in the <a href="abencds_ddl_glosry.html">CDS DDL</a> of the <a href="abenabap_cds_glosry.html">ABAP CDS</a> to a particular value when the method is called from ABAP. It avoids the warning from the syntax check and the exception <code class="ph codeph">CX_AMDP_CDS_CLIENT_MISMATCH</code> when an AMDP method accesses the <a href="abencds_mngdddic_view_glosry.html">CDS-managed DDIC view (obsolete)</a> of a <a href="abencds_view_glosry.html">CDS view</a> whose <a href="abencds_view_client_handling_v1.html">client handling</a> is determined by the annotation <a href="abencds_view_client_handling_v1.html"><code class="ph codeph">@ClientHandling.algorithm: #SESSION_VARIABLE</code></a>.</li>
</ul></td>
</tr>
</tbody>
</table>
