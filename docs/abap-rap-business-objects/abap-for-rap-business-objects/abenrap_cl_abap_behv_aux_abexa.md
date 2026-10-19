---
title: "Getting RAP Context Information Using CL_ABAP_BEHV_AUX"
source_file: abenrap_cl_abap_behv_aux_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > Other RAP-Related ABAP Language Elements and Topics > RAP-Related System Classes and Functionality > CL_ABAP_BEHV_AUX"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Getting RAP Context Information Using CL_ABAP_BEHV_AUX

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the use of methods of the class `CL_ABAP_BEHV_AUX` by focusing on the filling of the specific parameters in multiple contexts.

**Note:** This example does not fully meet the requirements of the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). It is intentionally kept short and simple and focuses on specific RAP aspects. For example, some [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) implementations might be empty. See more information on the RAP BO contract in the [Development guide for the ABAP RESTful Application Programming Model](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

**Used artifacts in the example**

<table>
<thead>
<tr class="header">
<th><strong>What</strong></th>
<th><strong>CDS view</strong></th>
<th><strong>BDEF</strong></th>
<th><strong>Behavior Pool (ABP)</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Base <a href="abenrap_bo_glosry.html">RAP business object</a></td>
<td><code class="ph codeph">DEMO_EXT_M</code></td>
<td><code class="ph codeph">DEMO_EXT_M</code></td>
<td><code class="ph codeph">BP_DEMO_EXT_M=================CCIMP</code></td>
<td><p>The CDS data model only consists of one node constituting the root entity.</p>
<p>The BDEF defines a managed RAP BO. It is also defined as <code class="ph codeph">extensible</code>.</p>
<p>Since it is a simple example serving demonstration purposes, the RAP handler methods in the ABP do not contain any meaningful implementations. Each method implementation contains calls for the methods <code class="ph codeph">get_current_context</code> and <code class="ph codeph">get_current_handler_kind</code>. The return values of the method parameters are stored in a <a href="abennested_structure_glosry.html">nested structure</a> in the global class of the ABP and added to an internal table for displaying purposes.</p></td>
</tr>
<tr class="even">
<td><a href="abenrap_bo_interface_glosry.html">RAP BO interface</a></td>
<td><code class="ph codeph">DEMO_INTF_M</code></td>
<td><code class="ph codeph">DEMO_INTF_M</code></td>
<td></td>
<td>The interface BDEF projects the original RAP BO.</td>
</tr>
<tr class="odd">
<td>RAP BO interface extension</td>
<td></td>
<td><code class="ph codeph">DEMO_INTF_EXT_M</code></td>
<td>The BDEF extension extends the RAP BO via its interface. It addresses the root node by its interface name. It adds one extension action to the RAP BO which is implemented in the extension ABP. This action simply updates the value of a specific field with a default value. Additionally, the methods in the extension ABP contains similar code snippets for method calls as mentioned above. <code class="ph codeph">BP_DEMO_INTF_EXT_M============CCIMP</code></td>
<td></td>
</tr>
<tr class="even">
<td><a href="abenrap_projection_bo_glosry.html">RAP projection business object</a></td>
<td><code class="ph codeph">DEMO_PROJ_M</code></td>
<td><code class="ph codeph">DEMO_PROJ_M</code></td>
<td></td>
<td>The CDS projection view is based on the CDS view of the base BO's CDS view (the projected entity) and exposes only a subset of elements.</td>
</tr>
</tbody>
</table>

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_rap_cl_abap_behv_aux DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    METHODS: 
      initialize_dbtabs. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_cl_abap_behv_aux IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( `Demo: cl_abap_behv_aux` 
    )->write_doc( `<b>1) Create operation directly ` && 
                  `on the root entity</b>` ). 
 
    MODIFY ENTITIES OF demo_ext_m 
      ENTITY Root 
      CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
      WITH VALUE #( ( %cid = 'cid1' 
                      key_field = 1 
                      field1 = 'aaa' 
                      field2 = 'bbb' 
                      field3 = 10 
                      field4 = 11 ) 
                    ( %cid = 'cid2' 
                      key_field = 2 
                      field1 = 'ccc' 
                      field2 = 'ddd' 
                      field3 = 20 
                      field4 = 21 ) ) 
      MAPPED FINAL(m1) 
      FAILED FINAL(f1) 
      REPORTED FINAL(r1). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
      FROM  demo_tab_root_5 
      ORDER BY key_field 
      INTO TABLE @FINAL(create_root). 
 
    out->write( create_root 
    )->write( bp_demo_ext_m=>behv_aux_table 
    )->line( ). 
 
    CLEAR bp_demo_ext_m=>behv_aux_table. 
 
    out->write_doc( `<b>2) Create operation on the root ` && 
                  `entity via interface</b>` ). 
 
    "Creating instances of the root entity via the interface 
    MODIFY ENTITIES OF demo_intf_m 
      ENTITY root_interface 
      CREATE FIELDS ( key_field field1 field2 field3 field4 ) 
      WITH VALUE #( ( %cid = 'cid3' 
                      key_field = 3 
                      field1 = 'eee' 
                      field2 = 'fff' 
                      field3 = 30 
                      field4 = 31 ) 
                    ( %cid = 'cid4' 
                      key_field = 4 
                      field1 = 'ggg' 
                      field2 = 'hhh' 
                      field3 = 40 
                      field4 = 41 ) ) 
       MAPPED FINAL(map2) 
       FAILED FINAL(f2) 
       REPORTED FINAL(r2). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
      FROM  demo_tab_root_5 
      ORDER BY key_field 
      INTO TABLE @FINAL(create_via_itf). 
 
    out->write( create_via_itf 
    )->write( bp_demo_ext_m=>behv_aux_table 
    )->line( ). 
 
    CLEAR bp_demo_ext_m=>behv_aux_table. 
 
    out->write_doc( `<b>3) Action execution via RAP BO ` && 
                  `interface extension</b>` ). 
 
    "Executing an action via RAP BO interface extension 
    MODIFY ENTITIES OF demo_intf_m 
       ENTITY root_interface 
       EXECUTE set_value_ext 
       FROM VALUE #( ( key_field = 1 ) 
                     ( key_field = 2 ) 
                     ( key_field = 3 ) 
                     ( key_field = 4 ) ) 
       MAPPED FINAL(m3) 
       FAILED FINAL(f3) 
       REPORTED FINAL(r3). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
      FROM  demo_tab_root_5 
      ORDER BY key_field 
      INTO TABLE @FINAL(action_via_bo_intf). 
 
    out->write( action_via_bo_intf 
    )->write( bp_demo_ext_m=>behv_aux_table 
    )->line( ). 
 
    CLEAR bp_demo_ext_m=>behv_aux_table. 
 
    out->write_doc( `<b>4) Create operation on the root ` && 
                  `entity via a projection</b>` ). 
 
    "Creating instances of the root entity via a projection 
    "Note that the projection view has only a subset of fields. 
    MODIFY ENTITIES OF demo_proj_m 
       ENTITY proj 
       CREATE FIELDS ( key_field field1 field2 ) 
       WITH VALUE #( ( %cid = 'cid5' 
                       key_field = 5 
                       field1 = 'iii' 
                       field2 = 'jjj' ) 
                     ( %cid = 'cid6' 
                       key_field = 6 
                       field1 = 'kkk' 
                       field2 = 'lll' ) ) 
        MAPPED FINAL(m4) 
        FAILED FINAL(f4) 
        REPORTED FINAL(r4). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, field3, field4 
      FROM demo_tab_root_5 
      ORDER BY key_field INTO TABLE @FINAL(create_via_proj). 
 
    out->write( create_via_proj 
    )->write( bp_demo_ext_m=>behv_aux_table ). 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_5. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object, the RAP BO interface and RAP projection BO from an ABAP class and performs the following steps:

1.  Create operation directly on the root entity

    Instances are created directly on the root entity. The instances are saved to the database table whose entries are displayed. Additionally, the outcome of setting the parameters when calling the methods of class `CL_ABAP_BEHV_AUX` is displayed. This is also true for the following steps.

2.  Create operation on the root entity via interface

    More instances are created on the root entity, however, with an ABAP EML `MODIFY` request via the RAP BO interface. Hence, the `from_interface` parameter is filled after calling the `get_current_context` method.

3.  Action execution via RAP BO interface extension

    An action which is implemented in an extension ABP is called via a RAP BO interface extension. This method simply updates the value of a specific field. The output of the method calls demonstrates that also methods of the base BO's ABP are called. The context for `in_local_mode` is true in this case.

4.  Create operation on the root entity via a projection

    More instances are created on the root entity, however, with an ABAP EML `MODIFY` request via the RAP BO projection. Hence, the `from_projection` parameter is filled after calling the `get_current_context` method.
