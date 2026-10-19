---
title: "GET PERMISSIONS OPERATIONS, Dynamic Form"
source_file: abapget_permissions_dyn.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > GET PERMISSIONS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# GET PERMISSIONS OPERATIONS, Dynamic Form

## Syntax

``` abap
GET PERMISSIONS [[FORWARDING  ]PRIVILEGED  ] [only_clause] OPERATIONS perm_tab [response_param  ].  
```

[`FORWARDING `](abapeml_privileged.md) · [`PRIVILEGED `](abapeml_privileged.md) · [`only_clause`](abapget_permissions_only_clause.md) · [`response_param `](abapeml_response.md)

### Addition

[1. `... [FORWARDING] PRIVILEGED ...`](abapget_permissions_dyn.md#addition-1)

[2. `... only_clause ...`](abapget_permissions_dyn.md#addition-2)

[3. `... response_param.`](abapget_permissions_dyn.md#addition-3)

## Overview

### Description

The dynamic version of the `GET PERMISSIONS` statement collects permission queries for multiple RAP BO entities in one `GET PERMISSIONS` statement.

`perm_tab` must be an internal table of type `ABP_BEHV_PERMISSIONS_TAB`. This table has specific components:

<table>
<thead>
<tr class="header">
<th><strong>Component</strong></th>
<th><strong>Details</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">entity_name</code></td>
<td>Specifies the name of the BO entity for which the permissions are requested. The entry for <code class="ph codeph">entity_name</code> must be of type <code class="ph codeph">ABP_ENTITY_NAME</code>. If the name is specified directly using a character literal, it must be provided using capital letters. It is a mandatory component.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">instances</code></td>
<td>The specification is optional. It is only relevant for getting the permission information on an instance level. The name must be provided using capital letters. The entry for <code class="ph codeph">instances</code> must be a reference variable <a href="abenstatic_type_glosry.html">static type</a> <code class="ph codeph">DATA</code>.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">request</code></td>
<td>Specifies the <code class="ph codeph">REQUEST</code> parameter. It is a mandatory component that must be a reference variable with the <a href="abenstatic_type_glosry.html">static type</a> <code class="ph codeph">DATA</code>.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">results</code></td>
<td><p>Specifies the <code class="ph codeph">RESULT</code> parameter. It is a mandatory component that must be a reference variable with the <a href="abenstatic_type_glosry.html">static type</a> <code class="ph codeph">DATA</code>.</p>
<p><strong><strong>Note:</strong></strong> See the <a href="abapget_permissions_rules.html">Guidelines</a> for information on how the components of the permissions result are handled.</p></td>
</tr>
</tbody>
</table>

## Addition 1

`... [FORWARDING] PRIVILEGED`

### Description

The addition [`PRIVILEGED`](abapeml_privileged.md) is used for a privileged access to a RAP BO, i. e. the RAP BO runtime does not perform certain authorization checks. As a prerequisite, `privileged` must be specified in the BDEF.

## Addition 2

`... only_clause ...`

### Description

The addition [`only_clause`](abapget_permissions_only_clause.md) allows the control characteristics to be specified that are to be included in the result.

## Addition 3

`... response_param.`

### Description

The addition `response_param` represents the response parameters that can be specified. When used in the context of the dynamic form of the ABAP EML statement, the parameters must be internal tables typed with `ABP_BEHV_RESPONSE_TAB`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_GET_PERMISSION` demonstrates the dynamic form of the `GET PERMISSIONS` statement in the context of checking access restrictions for certain data fields.

``` abap
"Root entity components for perm_tab. 
DATA: lt_perm_key_root TYPE TABLE FOR 
        PERMISSIONS KEY demo_managed_root_3, 
      ls_perm_req_root TYPE STRUCTURE FOR 
        PERMISSIONS REQUEST demo_managed_root_3, 
      ls_perm_res_root TYPE STRUCTURE FOR 
        PERMISSIONS RESULT demo_managed_root_3. 
 
lt_perm_key_root = VALUE #( ( %key-key_field = 5 ) 
                            ( %key-key_field = 6 ) ). 
 
ls_perm_req_root = VALUE #( 
                    %field-data_field1_root = if_abap_behv=>mk-on 
                    %field-data_field2_root = if_abap_behv=>mk-on 
                          ). 
ls_perm_res_root = VALUE #( ). 
 
"Child entity components for perm_tab. 
DATA: lt_perm_key_child TYPE TABLE 
        FOR PERMISSIONS KEY demo_managed_child_3, 
      ls_perm_req_child TYPE STRUCTURE 
        FOR PERMISSIONS REQUEST demo_managed_child_3, 
      ls_perm_res_child TYPE STRUCTURE 
        FOR PERMISSIONS RESULT demo_managed_child_3. 
 
lt_perm_key_child = VALUE #( ( %key-key_field = 5 ) 
                             ( %key-key_field = 6 ) ). 
ls_perm_req_child = VALUE #( 
                     %field-data_field1_child = if_abap_behv=>mk-on 
                     %field-data_field2_child = if_abap_behv=>mk-on 
                           ). 
ls_perm_res_child = VALUE #( ). 
 
DATA: 
perm_tab TYPE abp_behv_permissions_tab. 
perm_tab = VALUE #( ( entity_name = 'DEMO_MANAGED_ROOT_3' 
                      instances   = REF data( lt_perm_key_root ) 
                      request     = REF data( ls_perm_req_root ) 
                      results     = REF data( ls_perm_res_root ) ) 
                    ( entity_name = 'DEMO_MANAGED_CHILD_3' 
                      instances   = REF data( lt_perm_key_child ) 
                      request     = REF data( ls_perm_req_child ) 
                      results     = REF data( ls_perm_res_child ) ) 
                    ). 
 
GET PERMISSIONS ONLY INSTANCE FEATURES OPERATIONS perm_tab 
    FAILED FINAL(failed) 
    REPORTED FINAL(reported).
```

### Executable Example

- The example [ABAP EML - `GET PERMISSIONS`, Variants](abenget_perm_forms_abexa.md) demonstrates the dynamic form of the `GET PERMISSIONS` statement with a simple managed RAP BO. It also includes the short and long form.
