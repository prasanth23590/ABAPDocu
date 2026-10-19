---
title: "Secondary Table Keys in BDEF Derived Types"
source_file: abapderived_types_secondary_keys.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Secondary Table Keys in BDEF Derived Types

BDEF derived types can include predefined and custom [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md).

The following topics are covered in this section:

- [Predefined Secondary Table Keys in BDEF Derived Types](abapderived_types_secondary_keys.md#predefined-secondary-table-keys-in-bdef-derived-types)

- [Custom Secondary Table Keys in BDEF Derived Types](abapderived_types_secondary_keys.md#custom-secondary-table-keys-in-bdef-derived-types)

## Predefined Secondary Table Keys in BDEF Derived Types

[Internal tables](../../abap-glossary/abeninternal_table_glosry.md) that are typed with [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md), that is, with [`TYPE TABLE FOR ...`](abaptype_table_for.md), are [standard tables](../../abap-glossary/abenstandard_table_glosry.md) with an empty [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md). However, most of these internal tables have predefined [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md). In this case, the secondary table keys are always non-unique [sorted keys](../../abap-glossary/abensorted_key_glosry.md). The following secondary table keys are currently available:

<table>
<thead>
<tr class="header">
<th><strong>Secondary Table Key</strong></th>
<th><strong>Details</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">entity</code></td>
<td>The table key <code class="ph codeph">entity</code> always includes the component <a href="abapderived_types_key.html"><code class="ph codeph">%key</code></a> and is available in all BDEF derived types that have <code class="ph codeph">%key</code> as a component.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">cid</code></td>
<td>The table key <code class="ph codeph">cid</code> includes the components <a href="abapderived_types_cid.html"><code class="ph codeph">%cid</code></a> or <a href="abapderived_types_cid_ref.html"><code class="ph codeph">%cid_ref</code></a>. Depending on the BDEF derived type, the components can also include <a href="abapderived_types_key.html"><code class="ph codeph">%key</code></a> and <a href="abapderived_types_pid.html"><code class="ph codeph">%pid</code></a>.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">draft</code></td>
<td>The table key <code class="ph codeph">draft</code> includes the component <a href="abapderived_types_is_draft.html"><code class="ph codeph">%is_draft</code></a> and is only available in <a href="abenbdl_with_draft.html">draft</a> scenarios. Depending on the BDEF derived type, the components can also include <a href="abapderived_types_pid.html"><code class="ph codeph">%pid</code></a> and <a href="abapderived_types_key.html"><code class="ph codeph">%key</code></a>.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">pid</code></td>
<td>Only available in the context of <a href="abenrap_late_numbering_glosry.html">late numbering</a> scenarios. The table key <code class="ph codeph">pid</code> includes the component <a href="abapderived_types_pid.html"><code class="ph codeph">%pid</code></a>. Depending on the BDEF derived type, the components can also include <a href="abapderived_types_tmp.html"><code class="ph codeph">%tmp</code></a> and <a href="abapderived_types_key.html"><code class="ph codeph">%key</code></a> <code class="ph codeph">id</code> is available for this secondary table key.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">id</code></td>
<td><p>It is an <a href="abenalias_glosry.html">alias name</a> for either <code class="ph codeph">entity</code>, <code class="ph codeph">draft</code>, or <code class="ph codeph">pid</code> depending on the context. If a BDEF derived type contains <code class="ph codeph">entity</code> as secondary table key, and not <code class="ph codeph">draft</code> or <code class="ph codeph">pid</code>, then <code class="ph codeph">id</code> is an alias for <code class="ph codeph">entity</code>. If a BDEF derived type contains <code class="ph codeph">pid</code> as secondary table key, no matter if <code class="ph codeph">entity</code> is available or the context is a draft-enabled RAP BO, then <code class="ph codeph">id</code> is an alias for <code class="ph codeph">pid</code>. If a BDEF derived type contains <code class="ph codeph">draft</code> as secondary table key, even if <code class="ph codeph">entity</code> is available, then <code class="ph codeph">id</code> is an alias for <code class="ph codeph">draft</code>.</p>
<p><strong>Note:</strong> For <code class="ph codeph">id</code> to be available, the <a href="abenrap_strict_mode_glosry.html">BDEF strict mode</a> <code class="ph codeph">strict(2);</code> must be specified.</p></td>
</tr>
</tbody>
</table>

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code demonstrates the secondary keys of an internal table type with `TYPE TABLE FOR CREATE` and [table expressions](../../abap-glossary/abentable_expression_glosry.md).

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA create_tab TYPE TABLE FOR CREATE demo_managed_root_4. 
 
create_tab = VALUE #( %control-key_field = if_abap_behv=>mk-on 
                      %control-field1 = if_abap_behv=>mk-on 
                      %control-field2 = if_abap_behv=>mk-on 
                      %control-field3 = if_abap_behv=>mk-on 
                      %control-field4 = if_abap_behv=>mk-on 
                    ( %cid           = 'cid1' 
                      %key-key_field = 1 
                      field1         = 'aaa' 
                      field2         = 'bbb' 
                      field3         = 11 
                      field4         = 111 ) 
                    ( %cid           = 'cid2' 
                      %key-key_field = 2 
                      field1         = 'ccc' 
                      field2         = 'ddd' 
                      field3         = 22 
                      field4         = 222  ) ). 
 
FINAL(line1) = create_tab[ KEY cid COMPONENTS %cid           = 'cid1' 
                                              %key-key_field = 1 ]. 
 
FINAL(line2) = create_tab[ KEY entity COMPONENTS %key-key_field = 2 ]. 
 
out->write( line1 ). 
out->write( line2 ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

You can execute the class `CL_DEMO_RAP_DSPLY_DER_TYPE_KS` to explore multiple BDEF derived types ([`TYPE TABLE FOR ...`](abaptype_table_for.md)) and their keys.

The class makes use of three different RAP scenarios:

- [RAP external numbering](../../abap-glossary/abenrap_ext_numbering_glosry.md) (non-draft and non-late numbering)

- [Late numbering](../rap-behavior-definitions/abenbdl_late_numbering.md) (non-draft)

- [Draft](../rap-behavior-definitions/abenbdl_with_draft.md)

The example is based on dummy [BDEFs](../../abap-glossary/abencds_behavior_definition_glosry.md) and [behavior pools (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) that just serve the purpose of including many specifications to display a variety of BDEF derived types:

<table>
<thead>
<tr class="header">
<th><strong>Scenario</strong></th>
<th><strong>Data model</strong></th>
<th><strong>BDEF</strong></th>
<th><strong>ABP</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RAP external numbering</td>
<td><p>Root entity: <code class="ph codeph">DEMO_MANAGED_ROOT_TEST</code></p>
<p>Child entity: <code class="ph codeph">DEMO_MANAGED_CHILD_TEST</code></p></td>
<td><code class="ph codeph">DEMO_MANAGED_ROOT_TEST</code></td>
<td><code class="ph codeph">BP_DEMO_MANAGED_ROOT_TEST</code></td>
</tr>
<tr class="even">
<td>Late numbering</td>
<td><p>Root entity: <code class="ph codeph">DEMO_MANAGED_ROOT_TEST_LN</code></p>
<p>Child entity: <code class="ph codeph">DEMO_MANAGED_CHILD_TEST_LN</code></p></td>
<td><code class="ph codeph">DEMO_MANAGED_ROOT_TEST_LN</code></td>
<td><code class="ph codeph">BP_DEMO_MANAGED_ROOT_TEST_LN</code></td>
</tr>
<tr class="odd">
<td>Draft</td>
<td><p>Root entity: <code class="ph codeph">DEMO_MANAGED_ROOT_TEST_DT</code></p>
<p>Child entity: <code class="ph codeph">DEMO_MANAGED_CHILD_TEST_DT</code></p></td>
<td><code class="ph codeph">DEMO_MANAGED_ROOT_TEST_DT</code></td>
<td><code class="ph codeph">BP_DEMO_MANAGED_ROOT_TEST_DT</code></td>
</tr>
</tbody>
</table>

### Hints

- Since variables cannot be declared with many of the BDEF derived types outside of the implementation class, the global class contains variables that are typed with various BDEF derived types. The methods `get_keys`, `get_keys_ln`, and `get_keys_dt` in the respective classes are responsible for providing the key tables.

- The availability of secondary keys varies depending on the specification in the BDEF, for example, `draft` is only available for draft scenarios. `pid` is only available for late numbering scenarios.

- *E* in the `KEY_KIND` field means empty key. *U* means user-defined key.

## Custom Secondary Table Keys in BDEF Derived Types

You can create your own secondary table keys for BDEF derived types. Such [BDEF secondary keys](../../abap-glossary/abenrap_secondary_key_glosry.md) are declared in [RAP behavior definitions](../../abap-glossary/abencds_behavior_definition_glosry.md) (BDEF) as described [here](../rap-behavior-definitions/abenbdl_define_key.md). They are used to define the signature of a [RAP key function](../../abap-glossary/abenrap_key_function_glosry.md), and can be used in ABAP statements specifying secondary table keys. The keys are relevant for all BDEF derived types that include [`%data`](abapderived_types_data.md). For these, [secondary table indices](../../abap-glossary/abensecondary_table_index_glosry.md) are created. For other BDEF derived types, they are not created. Like the predefined secondary table keys, the custom keys are always non-unique sorted keys.

### Hint

When using the secondary table keys with ABAP statements, for example, a loop across the result of an ABAP EML read request, it makes only sense to use them when the complete secondary table key was requested, i.e. when [`%control`](abapderived_types_control.md) was specified for all key components accordingly.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code demonstrates the use of a BDEF secondary table key.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DELETE FROM demo_dbtab_root. 
INSERT demo_dbtab_root FROM TABLE @( VALUE #( 
( key_field = 1  data_field = `F` char_field = 'X' dec_field = '0.2' ) 
( key_field = 2  data_field = `E` char_field = 'X' dec_field = '0.5' ) 
( key_field = 3  data_field = `D` char_field = 'X' dec_field = '0.1' ) 
( key_field = 4  data_field = `C` char_field = 'X' dec_field = '0.2' ) 
( key_field = 5  data_field = `B` char_field = 'X' dec_field = '0.6' ) 
( key_field = 6  data_field = `A` char_field = 'X' dec_field = '0.4' ) 
) ). 
 
READ ENTITY demo_rap_r_m_define_key 
ALL FIELDS WITH VALUE #( 
  ( key_field = 1 ) ( key_field = 2 ) ( key_field = 3 ) 
  ( key_field = 4 ) ( key_field = 5 ) ( key_field = 6 ) ) 
  RESULT DATA(read_result) 
  FAILED DATA(fr) 
  REPORTED DATA(rr). 
 
"Using the BDEF secondary table key in an ABAP statement 
"In the example, the BDEF secondary table key includes the components 
"char_field and dec_field. key_field which is of type i is added to 
"an internal table to visualize the secondary table index. 
 
DATA key_tab TYPE TABLE OF i WITH EMPTY KEY. 
LOOP AT read_result INTO DATA(sec) USING KEY secondindex. 
  APPEND sec-key_field TO key_tab. 
ENDLOOP. 
 
out->write( key_tab ). 
 
out->display( ).
```
