---
title: "GET PERMISSIONS, Short Form"
source_file: abapget_permissions_short.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > GET PERMISSIONS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# GET PERMISSIONS, Short Form

## Syntax

``` abap
GET PERMISSIONS [[FORWARDING  ] PRIVILEGED  ] [only_clause] 
     ENTITY entity [FROM keys] REQUEST request RESULT result [response_param  ].  
```

[`FORWARDING `](abapeml_privileged.md) · [`PRIVILEGED `](abapeml_privileged.md) · [`only_clause`](abapget_permissions_only_clause.md) · [`response_param `](abapeml_response.md)

### Addition

[1. `... [FORWARDING] PRIVILEGED ...`](abapget_permissions_short.md#addition-1)

[2. `... only_clause ...`](abapget_permissions_short.md#addition-2)

[3. `... FROM keys ...`](abapget_permissions_short.md#addition-3)

[4. `... response_param.`](abapget_permissions_short.md#addition-4)

## Overview

### Description

The short form of the `GET PERMISSIONS` statement is used to retrieve information on permissions for instances of a single entity.

**Syntax Details**

<table>
<thead>
<tr class="header">
<th><strong>Syntax Part</strong></th>
<th><strong>Details</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">entity</code></td>
<td>Specifies the name of the entity following the keyword <code class="ph codeph">ENTITY</code>. It must be the full entity name, not the defined alias.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">REQUEST request</code></td>
<td><p><code class="ph codeph">request</code> is a structure following the keyword <code class="ph codeph">REQUEST</code> containing request components to specify which operations, fields or actions are to be considered for the information retrieval. The request components can be either marked as enabled or disabled. The structure must be typed with <a href="abaptype_structure_for.html"><code class="ph codeph">TYPE STRUCTURE FOR PERMISSIONS REQUEST</code></a>.</p>
<p>To enable or disable the request components, the constants provided in the interface <code class="ph codeph">IF_ABAP_BEHV</code> can be used: One example is <code class="ph codeph">if_abap_behv=&gt;mk-on</code> for enabling (indicated by <code class="ph codeph">01</code>) and <code class="ph codeph">if_abap_behv=&gt;mk-off</code> for disabling (indicated by <code class="ph codeph">00</code>).</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">RESULT result</code></td>
<td><p><code class="ph codeph">result</code> is a structure of type <a href="abaptype_structure_for.html"><code class="ph codeph">TYPE STRUCTURE FOR PERMISSIONS RESULT</code></a> following the keyword <code class="ph codeph">RESULT</code>. It contains two components that contain the result of the permission information request:</p>
<p><code class="ph codeph">instances</code>: Internal table containing instance keys and components for those elements in the <a href="abenbdl_body.html">entity behavior body</a> of the BDEF for which permissions are defined (excluding static elements).</p>
<p><code class="ph codeph">global</code>: Structure containing components for all elements in the entity behavior body of the BDEF for which permissions are defined.</p>
<p><strong>Note:</strong> See the <a href="abapget_permissions_rules.html">Guidelines</a> for information on how the components of the permissions result are handled.</p></td>
</tr>
</tbody>
</table>

## Addition 1

`... [FORWARDING] PRIVILEGED ...`

### Description

The addition [`PRIVILEGED`](abapeml_privileged.md) is used for a privileged access to a RAP BO, i. e. the RAP BO runtime does not perform certain authorization checks. As a prerequisite, `privileged` must be specified in the BDEF.

## Addition 2

`... only_clause ...`

### Description

The addition [`only_clause`](abapget_permissions_only_clause.md) allows the control characteristics to be specified that are to be included in the result.

## Addition 3

`... FROM keys ...`

### Description

The addition `FROM keys` specifies the keys of the instances for which permissions are to be requested. `keys` is an internal table and must be typed with the BDEF derived type [`TYPE TABLE FOR PERMISSIONS KEY`](abaptype_table_for.md).

The addition must not be specified if any of the [`ONLY GLOBAL ...`](abapget_permissions_only_clause.md) variants are used. For all other `ONLY` clauses, `FROM keys` is required.

## Addition 4

`... response_param.`

### Description

The addition [`response_param`](abapeml_response.md) represents the response parameters that can be specified.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_GET_PERMISSION` demonstrates the short form of the `GET PERMISSIONS` statement in the context of checking access restrictions for certain data fields.

``` abap
DATA: request TYPE STRUCTURE FOR 
        PERMISSIONS REQUEST demo_managed_root_3. 
request-%field-data_field1_root = if_abap_behv=>mk-on. 
request-%field-data_field2_root = if_abap_behv=>mk-on. 
 
GET PERMISSIONS ONLY INSTANCE FEATURES ENTITY demo_managed_root_3 
  FROM VALUE #( ( %key-key_field = 1 ) 
                ( %key-key_field = 2 )  ) 
  REQUEST request 
  RESULT FINAL(result) 
  FAILED FINAL(failed) 
  REPORTED FINAL(reported).
```

### Executable Example

- The example [ABAP EML - `GET PERMISSIONS`, Variants](abenget_perm_forms_abexa.md) demonstrates the short form of the `GET PERMISSIONS` statement with a simple managed RAP BO. It also includes the long and dynamic form.
