---
title: "READ ENTITIES OPERATIONS, Dynamic Form"
source_file: abapread_entities_operations.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > READ ENTITY, ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# READ ENTITIES OPERATIONS, Dynamic Form

## Syntax

``` abap
READ ENTITIES [IN LOCAL MODE|[FORWARDING  ] PRIVILEGED  ] OPERATIONS op_tab [response_param  ].  
```

[`IN LOCAL MODE`](abapin_local_mode.md) · [`FORWARDING `](abapeml_privileged.md) · [`PRIVILEGED `](abapeml_privileged.md) · [`response_param `](abapeml_response.md)

### Addition

[1. `... IN LOCAL MODE ...`](abapread_entities_operations.md#addition-1)

[2. `... [FORWARDING] PRIVILEGED ...`](abapread_entities_operations.md#addition-2)

[3. `... response_param.`](abapread_entities_operations.md#addition-3)

## Overview

### Description

The dynamic form of the `READ` statement enables the collecting of read operations for multiple RAP BOs in one `READ ENTITIES OPERATIONS ...` statement. There is no short form available for the dynamic version.

`op_tab` must be a table of type `ABP_BEHV_RETRIEVALS_TAB`. This table has specific components:

<table>
<thead>
<tr class="header">
<th><strong>Component</strong></th>
<th><strong>Details</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">OP</code></td>
<td>It is a mandatory component and specifies the operation to be executed. It can be set with the defined constants, for example, <code class="ph codeph">OP-R-READ</code> etc., of interface <code class="ph codeph">IF_ABAP_BEHV</code> or just the predefined value for the operation in the interface, for example <code class="ph codeph">'R'</code> for a read operation (<code class="ph codeph">OP = 'R'</code>) or <code class="ph codeph">'N'</code> for a read-by-association operation (<code class="ph codeph">OP = 'N'</code>).</td>
</tr>
<tr class="even">
<td><code class="ph codeph">ENTITY_NAME</code></td>
<td>It is a mandatory component and specifies the name of the RAP BO entity for which the operation is executed. The name must be provided using capital letters.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">SUB_NAME</code></td>
<td>Only relevant for specifying association names in case of read-by-association operations or for functions. In these contexts, the specification is mandatory.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">INSTANCES</code></td>
<td>Mandatory component. It specifies a reference to an internal table holding the input keys. The table must be typed with the required BDEF derived type for the operation.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">FULL</code></td>
<td><p>An optional flag specifying whether all target instances (and not just links) are retrieved in the context of read-by-association operations. It is of type <code class="ph codeph">c</code> with length 1, i. e. <code class="ph codeph">full</code> specified with <code class="ph codeph">abap_true</code> or <code class="ph codeph">'X'</code> respects all target instances.</p>
<p><strong>Note:</strong> Currently, the behavior is as follows: If <code class="ph codeph">full</code> is specified with <code class="ph codeph">abap_true</code> or <code class="ph codeph">'X'</code>, all target instances are retrieved in any case. When specified otherwise, the instances might be retrieved or not.</p>
<p>Setting <code class="ph codeph">full</code> to <code class="ph codeph">if_abap_behv=&gt;typekind-result_chg</code> enables the <a href="abapeml_read_with_changes.html"><code class="ph codeph">WITH CHANGES</code></a> functionality.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">RESULTS</code></td>
<td>It specifies a reference to an internal table with the required BDEF derived type for the read results.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">LINKS</code></td>
<td>It specifies a reference to an internal table with the required BDEF derived type holding the key pairs of the source and target.</td>
</tr>
</tbody>
</table>

### Hints

- If the names of `ENTITY_NAME` and `SUB_NAME` are not provided in uppercase, an error occurs.

- In dynamic ABAP EML `READ` statements, the [`WITH CHANGES`](abapeml_read_with_changes.md) functionality is achieved by setting the `full` component of the statement's operand to `if_abap_behv=>typekind-result_chg`. `IN LOCAL MODE` must then be specified, and the reference to the read result must be typed with `TYPE TABLE FOR READ CHANGES`.

## Addition 1

`... IN LOCAL MODE ...`

### Description

The addition [`IN LOCAL MODE`](abapin_local_mode.md) is used to exclude [feature controls](../rap-behavior-definitions/abenbdl_actions_fc.md) and [authorization checks](../rap-behavior-definitions/abenbdl_authorization.md). It can only be used within the RAP BO runtime implementation.

## Addition 2

`... [FORWARDING] PRIVILEGED ...`

### Description

The addition [`PRIVILEGED`](abapeml_privileged.md) is used for a privileged access to a RAP BO, i. e. the RAP BO runtime does not perform certain authorization checks. As a prerequisite, `privileged` must be specified in the BDEF.

## Addition 3

`... response_param.`

### Description

The addition [`response_param`](abapeml_response.md) represents the response parameters that can be specified. The specification is optional. When used in the context of the dynamic form of the ABAP EML statement, the parameters must be internal tables typed with `ABP_BEHV_RESPONSE_TAB`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_READ` demonstrates an EML `READ ENTITIES OPERATIONS` statement.

``` abap
DATA: 
 op_tab TYPE ABP_BEHV_RETRIEVALS_TAB, 
 read_dyn  TYPE TABLE FOR READ IMPORT DEMO_SPFLI_FLIGHTS, 
 read_dyn_result TYPE TABLE FOR READ RESULT DEMO_SPFLI_FLIGHTS, 
 rba_dyn TYPE TABLE FOR READ IMPORT DEMO_SPFLI_FLIGHTS\_Flights, 
 rba_dyn_result TYPE TABLE FOR READ RESULT DEMO_SPFLI_FLIGHTS\_Flights, 
 rba_dyn_link TYPE TABLE FOR READ LINK DEMO_SPFLI_FLIGHTS\_Flights. 
 
    read_dyn = value #( 
      ( %key-Carrid = 'DL' 
        %key-connid = 106 
        %control = value #( 
           Airpfrom  = if_abap_behv=>mk-on 
           Airpto    = if_abap_behv=>mk-on 
           Arrtime   = if_abap_behv=>mk-on 
           Cityfrom  = if_abap_behv=>mk-on 
           Cityto    = if_abap_behv=>mk-on 
           Countryfr = if_abap_behv=>mk-on 
           Countryto = if_abap_behv=>mk-on 
           Deptime   = if_abap_behv=>mk-on 
           Fltime    = if_abap_behv=>mk-on 
           Distance  = if_abap_behv=>mk-on 
           Distid    = if_abap_behv=>mk-on 
           Fltype    = if_abap_behv=>mk-on 
           Period    = if_abap_behv=>mk-on 
                          ) 
                          ) ). 
 
    rba_dyn = value #( 
     ( %key-Carrid = 'UA' 
       %key-connid = 3516 
       %control = value #( Fldate     = if_abap_behv=>mk-on 
                           Price      = if_abap_behv=>mk-on 
                           Currency   = if_abap_behv=>mk-on 
                           Planetype  = if_abap_behv=>mk-on 
                           Seatsmax   = if_abap_behv=>mk-on 
                           Seatsocc   = if_abap_behv=>mk-on 
                          ) ) ). 
 
    op_tab = value #( 
       ( op = if_abap_behv=>op-r-read 
         entity_name = 'DEMO_SPFLI_FLIGHTS' 
         instances   = ref #( read_dyn ) 
         results     = ref #( read_dyn_result ) ) 
       ( op = if_abap_behv=>op-r-read_ba 
         entity_name = 'DEMO_SPFLI_FLIGHTS' 
         sub_name    = '_FLIGHTS' 
         full        = 'X' 
         instances   = ref #( rba_dyn ) 
         results     = ref #( rba_dyn_result ) 
         links       = ref #( rba_dyn_link ) ) 
                  ). 
 
    READ ENTITIES OPERATIONS op_tab FAILED FINAL(failed_dyn).
```

### Executable Example

- The example [ABAP EML - `READ`, Variants](abeneml_read_alternatives_abexa.md) demonstrates this `READ` variant with a simple managed RAP BO.

- For more examples on `READ` operations in general, see [Examples for ABAP EML `READ`](abapeml_read_examples_abexas.md).
