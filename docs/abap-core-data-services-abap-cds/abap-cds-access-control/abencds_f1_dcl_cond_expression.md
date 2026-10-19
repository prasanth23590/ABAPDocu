---
title: "CDS DCL - DEFINE ROLE, operator"
source_file: abencds_f1_dcl_cond_expression.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE > CDS DCL - DEFINE ROLE, condition > CDS DCL - DEFINE ROLE, literal_condition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, operator

## Syntax

``` abap
... operator ...  
```

## Description

Operator of a comparison expression in a [literal condition](abencds_f1_cond_literal.md) in an [access rule](../../abap-glossary/abenaccess_rule_glosry.md) in the definition of a role using [`DEFINE ROLE`](abencds_f1_define_role.md) in the [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md). The operator compares a left side and a right side. The left side is an element of the CDS entity to which the rule applies. The right side is represented using a literal value.

<table>
<thead>
<tr class="header">
<th><strong>operator</strong></th>
<th><strong>True if</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">=</code></td>
<td>The value of the left side is equal to the value of the right side.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">&lt;&gt;</code></td>
<td>The value of the left side is not equal to the value of the right side.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">&lt;</code></td>
<td>The value of the left side is less than the value of the right side.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">&gt;</code></td>
<td>The value of the left side is greater than the value of the right side.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">&lt;=</code></td>
<td>The value of the left side is less than or equal to the value of the right side.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">&gt;=</code></td>
<td>The value of the left side is greater than or equal to the value of the right side.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">?=</code></td>
<td><p>Like the operator <code class="ph codeph">=</code>. The condition is also met, however, if the value of the left side is the <a href="abennull_value_glosry.html">null value</a> or a type-dependent initial value.</p>
<p>The usage of this operator is discouraged.</p>
<p>It was introduced when access controls did not support arbitrary logical conditions and summarized two prominent use-cases in a single statement. The disadvantage is that the application of both conditions when not really needed introduces additional burden to the database.</p>
<p>SAP recommends to replace the use of this operator by dedicated statement tailored to the data model. The access control syntax check issues a warning for each use of this operator and the long text of this warning provides help for the replacement.</p></td>
</tr>
</tbody>
</table>
