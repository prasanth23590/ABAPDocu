---
title: "Example for RAP Handler Methods"
source_file: abenrap_handler_methods_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Handler Classes and Methods > METHODS, FOR, RAP Handler Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Example for RAP Handler Methods

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates various RAP handler methods with an unmanaged and draft-enabled RAP BO.

Note that the simplified example does not represent a real business scenario. The focus is on the technical side by giving an idea on self-implementing the handler methods of an [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) and dealing with the method parameters. The code should not be reused in a production scenario.

**Note:** This example does not fully meet the requirements of the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). It is intentionally kept short and simple and focuses on specific RAP aspects. For example, some [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) implementations might be empty. See more information on the RAP BO contract in the [Development guide for the ABAP RESTful Application Programming Model](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

**Data Model**

The CDS data model consists of the root entity DEMO_UNMANAGED_ROOT_DRAFT and its child entity DEMO_UNMANAGED_CHILD_DRAFT.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, RAP unmanaged, draft'
define root view entity DEMO_UNMANAGED_ROOT_DRAFT
  as select from demo_tab_root_4
  composition [1..*] of DEMO_UNMANAGED_CHILD_DRAFT as _child
  {
    key key_field,
        field1,
        field2,
        field3,
        field4,
        @Semantics.systemDateTime.lastChangedAt: true
        crea_date_time,
        @Semantics.systemDateTime.localInstanceLastChangedAt: true
        lchg_date_time,
        _child
  }
```

Child entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, RAP unmanaged, draft'
define view entity DEMO_UNMANAGED_CHILD_DRAFT
  as select from demo_tab_child_4
  association to parent DEMO_UNMANAGED_ROOT_DRAFT as _parent 
  on $projection.key_field = _parent.key_field
  {
 key key_field,
  key key_field_child,
  field1_child,
  field2_child,
  field3_child,
  field4_child,
      _parent
}
```

**Behavior Definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_UNMANAGED_ROOT_DRAFT` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
unmanaged implementation in class
  bp_demo_unmanaged_root_draft unique;
strict(2);
with draft;

define behavior for DEMO_UNMANAGED_ROOT_DRAFT
draft table demo_tab_dr_ro
lock master
total etag crea_date_time
etag master lchg_date_time
authorization master ( global, instance )
early numbering
{
  create;
  update( features : global );
  delete( features : global );
  association _child { create; with draft; }
  field ( features : instance ) field3;
  action action1;
  action action2 result [1] $self;
  action action3 parameter DEMO_CDS_ABSTRACT_DISCOUNT
      result selective [1] $self;
  factory action( precheck ) action4 [1];
  static function (authorization:none) function1
    result [1] DEMO_CDS_ABSTRACT_SUM;
  function (authorization:none) function2
    parameter DEMO_CDS_DEDUCT_DISCOUNT
    result [1] $self;
  function (authorization:none) function3
    result selective [1] $self;
  validation validation on save { field field3; }
  determination det_on_save on save { create; }
  determination det_on_modify on modify { create; }
  draft action Resume with additional implementation;
  draft action Edit with additional implementation;
  draft action Activate optimized with additional implementation;
  draft action Discard with additional implementation;
  draft determine action Prepare { determination det_on_save;
                                   validation validation; }
  field ( readonly:update ) key_field;
  field ( readonly ) crea_date_time, lchg_date_time;
}

define behavior for DEMO_UNMANAGED_CHILD_DRAFT
draft table demo_tab_dr_ch
lock dependent by _parent
etag dependent by _parent
authorization dependent by _parent
{
  update;
  delete;
  field ( readonly:update ) key_field, key_field_child;
  association _parent { with draft; }
}
```

The behavior definition is the basis of the implementation. It defines what can be implemented in the behavior pool.

**Behavior Implementation**

For the above RAP behavior definition, one ABP is created. The global class of the behavior pool is `BP_DEMO_UNMANAGED_ROOT_DRAFT`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_UNMANAGED_ROOT_DRAFT==CCIMP` of the behavior pool:

- `lcl_buffer` constitutes the transactional buffer. It includes internal tables to handle the data.

- `lhc_demo_unmanaged_root_draft` is the handler class of the behavior pool.

- `lsc_demo_unmanaged_root_draft` is the saver class of the behavior pool.

Handler and saver class for the child entity are not relevant in the example.

**Details of the ABP**

**Transactional buffer**

<table>
<thead>
<tr class="header">
<th><strong>Class / Method</strong></th>
<th><strong>Details</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Local class <code class="ph codeph">lcl_buffer</code></td>
<td><p>In this local class, two internal tables are constructed that serve as transactional buffer: <code class="ph codeph">root_buffer</code> as the transactional buffer for the root entity, and <code class="ph codeph">child_buffer</code> for the child entity to also cover the create- and read-by-association operations.</p>
<p>The underlying structured data types are built in a way that simplifies the handling of the buffers. <code class="ph codeph">gty_buffer</code>, as the structured data type for <code class="ph codeph">root_buffer</code>, contains all the key and data fields of the root entity's underlying CDS view with the same type. Plus, the structure includes the components <code class="ph codeph">cid</code> to hold the content ID that might be provided by an instance and, for a more comfortable processing of saving and deleting instances, it includes two fields (<code class="ph codeph">changed</code> and <code class="ph codeph">deleted</code>) acting as flags. These flags are set in the course of modify operations, i. e. if an instance is created or changed, the <code class="ph codeph">changed</code> receives an <em>X</em>. If an instance gets deleted, <code class="ph codeph">deleted</code> gets the flag <em>X</em>. If no operation takes place for an entity, both fields remain initial. Likewise, the structured data type for the child entity (<code class="ph codeph">gty_buffer_child</code>) is constructed. It also contains all the key and data fields of the child entity's underlying CDS view with the same type (which is in this example very similar to the root entity). This structure contains the components <code class="ph codeph">cid_ref</code> for by-association operations and <code class="ph codeph">cid_target</code> for the content ID of child instances in the <code class="ph codeph">%target</code> structure. The latter is not used in the example. Furthermore, the component <code class="ph codeph">created</code> is included. Its purpose is the same as <code class="ph codeph">changed</code>, however, in this case, it is only relevant to cover create-by-association operations. Only those instances whose <code class="ph codeph">created</code> field is marked with an <em>X</em> should be saved to the database table of the child entity.</p></td>
</tr>
<tr class="even">
<td>Methods <code class="ph codeph">prep_root_buffer</code> and <code class="ph codeph">prep_child_buffer</code></td>
<td><p>These two methods are meant to prepare the transactional buffers for the root and child entity and fill them with data from the underlying database table, especially if the buffer tables are cleared once the save sequence gets triggered by a <code class="ph codeph">COMMIT ENTITIES</code> statement in the ABAP class.</p>
<p>The principle of internal tables as transactional buffer is the following: Once an EML call requests data (to be read or modified) with a specific key, it is checked whether the transactional buffer already holds the requested data, otherwise it is checked if the data is available in the persistent database table. If it exists there, the line with the specified key is read from the database table into the transactional buffer using a <code class="ph codeph">SELECT</code> statement. The following is done in the individual methods for the operations to avoid double entries: If the data does not exist at all (for example, it got deleted), the <code class="ph codeph">FAILED</code> and <code class="ph codeph">REPORTED</code> structures should be filled with information about which data sets could not be read or modified. The <code class="ph codeph">prep_child_buffer</code> method is relevant for the by-association operations. Not only must the availability of the line with the specified key in the root buffer be checked but also the availability of the line in the child buffer. If the line exists in the underlying database table of the child entity, the data gets read into the child buffer using a <code class="ph codeph">SELECT</code> statement as well.</p></td>
</tr>
</tbody>
</table>

**Handler methods**

**Note:**

- In each method, the name of the method is added to an internal table in the global class. This internal table is displayed in the output several times to log and visualize the sequence of the RAP handler method calls.

- The method definitions include the explicit specification of the changing parameters in most cases.

- In most of the method implementations, the `failed` and ` reported` parameters are filled.

<table>
<thead>
<tr class="header">
<th><strong>Method</strong></th>
<th><strong>Details</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">create</code></td>
<td>After preparing the root buffer with the provided input parameters (<code class="ph codeph">entities</code>), a <code class="ph codeph">LOOP AT</code> statement processes the transactional buffer further with the individual instances that come in as input parameters. There are certain conditions to be met before an instance can actually be created. If the conditions are not met for a particular instance, the result is an entry in the <code class="ph codeph">FAILED</code> and <code class="ph codeph">REPORTED</code> structures for the failed instance. The gist is that those instances being present in the transactional buffer and meeting the conditions receive a flag in the <code class="ph codeph">changed</code> field and can finally be created. Consequently, the instances are saved to the database table following a <code class="ph codeph">COMMIT ENTITIES</code> statement in the ABAP class triggering the save sequence. The checks also take the significance of the flags in the <code class="ph codeph">%control</code> structure into consideration, i. e. if a data field is unmarked using the constant <code class="ph codeph">mk-off</code> of interface <code class="ph codeph">ABP_BEHV_FLAG</code>, this particular field should not be created with the provided value.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">update</code></td>
<td>Same as the method above, after preparing the root buffer with the provided input parameters (<code class="ph codeph">entities</code>), a <code class="ph codeph">LOOP AT</code> statement further processes the transactional buffer with the individual instances that come in as input parameters. Also here, there are certain conditions to be met before an instance can be updated. If the conditions are not met for a particular instance, an entry gets created in the <code class="ph codeph">FAILED</code> and <code class="ph codeph">REPORTED</code> structures for the failed instance. The checks are implemented in the way that existing values of a data field should not be overwritten if it is explicitly unmarked in the <code class="ph codeph">%control</code> structure. Same as above, a changed instance receives a flag. Furthermore, the <code class="ph codeph">IF</code> statements are implemented for two scenarios. It might so happen that an EML request includes only the keys or only <code class="ph codeph">%cid_ref</code>. In the latter case, a potentially provided key is ignored since the reference to a particular <code class="ph codeph">%cid</code> is the principal reference.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">delete</code></td>
<td>This method is implemented similarly to the <code class="ph codeph">update</code> method, for example, it considers the two scenarios when only the key or only <code class="ph codeph">%cid_ref</code> are provided. If an instance is to be deleted, it receives a flag for the <code class="ph codeph">deleted</code> field. The <code class="ph codeph">changed</code> field gets initialized. <code class="ph codeph">%control</code> is not applicable here.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">read</code></td>
<td>After preparing the root buffer with the provided input parameters (<code class="ph codeph">keys</code>), a <code class="ph codeph">LOOP AT</code> statement is responsible for a detailed preparation and filling of the read <code class="ph codeph">result</code> table according to the keys that come in as input parameters and considering the flags for the fields in the <code class="ph codeph">%control</code> structure. If a data field is unmarked, this particular field should not be read and included in the read result. The key must always be read and returned.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">rba_child</code></td>
<td>As an initial step in the method for read-by association operations, both root and child buffers must be prepared. Same as in the <code class="ph codeph">read</code> method, the <code class="ph codeph">LOOP AT</code> statement is responsible for a detailed preparation and filling of the read <code class="ph codeph">result</code> table according to the keys that come in as input parameters and considering the flags for the fields in the <code class="ph codeph">%control</code> structure. If a data field is unmarked, this particular field should not be read and included in the read result. The key must always be read and returned.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">cba_child</code></td>
<td>As an initial step in the method for create-by association operations, both root and child buffers must be prepared. The conditions for filling the child buffer within the <code class="ph codeph">LOOP AT</code> statement include checks for two scenarios. It might so happen that an EML request includes only the keys or only <code class="ph codeph">%cid_ref</code>. In the latter case, a potentially provided key is ignored since the reference to a particular <code class="ph codeph">%cid</code> is the principal reference. The flags in the <code class="ph codeph">%control</code> structure for the data fields are considered, too. If the conditions are met for an instance to be created in the child entity, the instance receives a flag for the <code class="ph codeph">created</code> field.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">action1</code></td>
<td><p>Updates the string in field <code class="ph codeph">field2</code> for all requested instances.</p>
<p>RAP BDL information: <a href="abenbdl_action.html">action</a>.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">action2</code></td>
<td><p>Action specified with <code class="ph codeph">result</code> in the BDEF. Updates the string in field <code class="ph codeph">field1</code> for all requested instances. Additionally, the action's result parameter is filled.</p>
<p>RAP BDL information: <a href="abenbdl_action.html">action</a>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">action3</code></td>
<td><p>Action specified with <code class="ph codeph">parameter</code> and <code class="ph codeph">result selective</code> in the BDEF. In this example, the input parameter represents a discount percentage and the action subtracts the discount from the value of the fields <code class="ph codeph">field3</code> and <code class="ph codeph">field4</code> of an entity instance. Additionally, the action's result parameter is filled with the values of requested fields.</p>
<p>RAP BDL information: <a href="abenbdl_action.html">action</a>.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">action4</code></td>
<td><p>Copies instances based on keys specified by the RAP consumer. Since <code class="ph codeph">action4</code> is specified with <code class="ph codeph">precheck</code> in the BDEF, the method <code class="ph codeph">precheck_action4</code> is called beforehand to check whether the action can be executed based on certain field values.</p>
<p>RAP BDL information: <a href="abenbdl_action.html">action</a>, <a href="abenbdl_precheck.html">precheck</a>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">precheck_action4</code></td>
<td><p>Checks whether instances have a certain value for a field. If the field has the specific value, <code class="ph codeph">action4</code> is not executed for this instance. Since <code class="ph codeph">action4</code> is specified with <code class="ph codeph">precheck</code> in the BDEF, the method <code class="ph codeph">precheck_action4</code> is called before <code class="ph codeph">action4</code>. In this example, the uniqueness check is actually implemented in the <code class="ph codeph">create</code> method. Here, it is available for demonstration purposes and so as not to have the precheck interfere with other operations, for example, if the notation <code class="ph codeph">create</code> was specified with <code class="ph codeph">precheck</code> in the BDEF.</p>
<p>RAP BDL information: <a href="abenbdl_precheck.html">precheck</a>.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">function1</code></td>
<td><p>Static function that applies to the complete BO, not to any specific entity instance. The function first filters all entity instances. The value of <code class="ph codeph">field3</code> should be higher than 100. Then, it sums up the values of the field <code class="ph codeph">field3</code>. The value of the sum is returned in the result parameter.</p>
<p>RAP BDL information: <a href="abenbdl_function.html">function</a>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">function2</code></td>
<td><p>Instance function specified with <code class="ph codeph">parameter</code> in the BDEF. To execute the function, it is required to specify an entity instance and also a value for the input parameter. In this example, the input parameter represents a discount percentage and the function subtracts the discount from the value of the field <code class="ph codeph">field3</code> of an entity instance. The reduced value is returned in the result parameter.</p>
<p>RAP BDL information: <a href="abenbdl_function.html">function</a>.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">function3</code></td>
<td><p>Instance function specified with <code class="ph codeph">result selective</code> in the BDEF. The importing parameter <code class="ph codeph">requested_fields</code> is considered. Only those fields that are requested by the RAP consumer are filled.</p>
<p>RAP BDL information: <a href="abenbdl_function.html">function</a>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">get_instance_authorizations</code></td>
<td><p>Checks authorization against the persistent state of the instance. The method returns information on whether update and delete operations as well as the execution of actions are allowed on instances. In this example, they are not allowed if <code class="ph codeph">field2</code> has a particular value.</p>
<p>RAP BDL information: <a href="abenbdl_authorization.html">authorization</a>.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">lock</code></td>
<td><p>A lock object (<code class="ph codeph">ELOCKRAP</code>) is available for the database table. The method locks the active instances based on the keys (<code class="ph codeph">key_field</code>). To visualize the locking, the global lock table (transaction <code class="ph codeph">SM12</code>) can be checked while debugging the program. The locks are removed after the <code class="ph codeph">COMMIT ENTITIES</code> statement has been executed. With regards to editing draft instances, the locks are removed after the draft action <code class="ph codeph">activate</code> has been completed.</p>
<p>RAP BDL information: <a href="abenbdl_locking.html">locking</a>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">get_instance_features</code></td>
<td><p>The method returns information on whether a certain field (<code class="ph codeph">field3</code>) is read-only or can be modified based on a certain condition.</p>
<p>RAP BDL information: <a href="abenbdl_precheck.html">feature control</a>.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">get_global_features</code></td>
<td><p>The method returns information on whether update and delete operations on instances are allowed or not based on a certain condition.</p>
<p>RAP BDL information: <a href="abenbdl_precheck.html">feature control</a>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">get_global_authorizations</code></td>
<td><p>The method is implemented in a way that modify operations are only enabled for users with the appropriate authorizations. In the interest of having a simple demo, the example goes without an authorization object which is, for example, a way to handle the authorization granting in production applications. The variable <code class="ph codeph">auth_flag</code> represents the authorization that is granted or not. In this example, the permission is always granted.</p>
<p>RAP BDL information: <a href="abenbdl_authorization.html">authorization</a>.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">det_on_modify</code></td>
<td><p>Adds a string to the existing string value in field <code class="ph codeph">field1</code>.</p>
<p>RAP BDL information: <a href="abenbdl_determinations.html">determination</a>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">det_on_save</code></td>
<td><p>Performs a simple calculation on the value in field <code class="ph codeph">field4</code>.</p>
<p>RAP BDL information: <a href="abenbdl_determinations.html">determination</a>.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">validation</code></td>
<td><p>Checks if the value of field <code class="ph codeph">field3</code> is higher than 1000.</p>
<p>RAP BDL information: <a href="abenbdl_validations.html">validation</a>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">activate</code></td>
<td><p>Performs a simple calculation on the value in field <code class="ph codeph">field3</code>.</p>
<p>RAP BDL information: <a href="abenbdl_draft_action.html">draft action</a>.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">discard</code></td>
<td><p>Removes underscores from the string in field <code class="ph codeph">field1</code>.</p>
<p>RAP BDL information: <a href="abenbdl_draft_action.html">draft action</a>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">edit</code></td>
<td><p>Converts the string in field <code class="ph codeph">field1</code> to upper case.</p>
<p>RAP BDL information: <a href="abenbdl_draft_action.html">draft action</a>.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">resume</code></td>
<td><p>Does not contain any implementations on draft instances. It is currently not possible to call and debug this method in the demonstration class.</p>
<p>RAP BDL information: <a href="abenbdl_draft_action.html">draft action</a>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">earlynumbering_create</code></td>
<td><p>Early numbering is applied to primary keys. In the example, the key should be a random number between 50 and 100. The keys are mapped to <code class="ph codeph">%cid</code>.</p>
<p>RAP BDL information: <a href="abenbdl_early_numb.html"><code class="ph codeph">early numbering</code></a>.</p></td>
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
CLASS cl_demo_rap_unm_draft DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      failed TYPE RESPONSE FOR FAILED demo_unmanaged_root_draft, 
      reported TYPE RESPONSE FOR REPORTED demo_unmanaged_root_draft, 
      mapped TYPE RESPONSE FOR MAPPED demo_unmanaged_root_draft, 
      links TYPE TABLE FOR READ LINK demo_unmanaged_root_draft\_child, 
      func_result TYPE TABLE FOR FUNCTION RESULT 
        demo_unmanaged_root_draft~function2, 
      func_result_selective TYPE TABLE FOR FUNCTION RESULT 
        demo_unmanaged_root_draft~function3, 
      action_result TYPE TABLE FOR ACTION RESULT 
        demo_unmanaged_root_draft~action2, 
      action_result2 TYPE TABLE FOR ACTION RESULT 
        demo_unmanaged_root_draft~action3, 
      activate_tab TYPE TABLE FOR ACTION IMPORT 
        demo_unmanaged_root_draft~activate. 
    METHODS: 
     initialize_dbtabs, 
     get_handler_meth, 
     extract_from_reported RETURNING VALUE(messages) TYPE string_table, 
     extract_from_failed RETURNING VALUE(errors) TYPE string_table, 
     display_responses. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_unm_draft IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demo: RAP Handler Methods` 
      )->line( 
      )->next_section( `1) First run of standard operations on ` && 
                       ` active instances using EML MODIFY` ). 
 
    MODIFY ENTITY demo_unmanaged_root_draft 
       CREATE FROM VALUE #( 
          ( %cid = 'cid1' 
            %is_draft = if_abap_behv=>mk-off 
            key_field = 1 
            %control-key_field = if_abap_behv=>mk-on 
            field1 = 'aaa_cr' 
            %control-field1 = if_abap_behv=>mk-on 
            field2 = 'bbb_cr' 
            %control-field2 = if_abap_behv=>mk-on 
            field3 = 2 
            %control-field3 = if_abap_behv=>mk-on 
            field4 = 3 
            %control-field4 = if_abap_behv=>mk-on ) 
          ( %cid = 'cid2' 
            %is_draft = if_abap_behv=>mk-off 
            key_field = 2 
            %control-key_field = if_abap_behv=>mk-on 
            field1 = 'ccc_cr' 
            %control-field1 = if_abap_behv=>mk-on 
            field2 = 'ddd_cr' 
            %control-field2 = if_abap_behv=>mk-on 
            field3 = 4 
            %control-field3 = if_abap_behv=>mk-on 
            field4 = 5 
            %control-field4 = if_abap_behv=>mk-on ) 
          ( %cid = 'cid3' 
            %is_draft = if_abap_behv=>mk-off 
            key_field = 3 
            %control-key_field = if_abap_behv=>mk-on 
            field1 = 'eee_cr' 
            %control-field1 = if_abap_behv=>mk-on 
            field2 = 'fff_cr' 
            %control-field2 = if_abap_behv=>mk-on 
            field3 = 6 
            %control-field3 = if_abap_behv=>mk-on 
            field4 = 7 
            %control-field4 = if_abap_behv=>mk-on ) 
          ( %cid = 'cid4'                             "Error 
            %is_draft = if_abap_behv=>mk-off 
            key_field = 3 
            %control-key_field = if_abap_behv=>mk-on 
            field1 = 'ggg_cr' 
            %control-field1 = if_abap_behv=>mk-on 
            field2 = 'hhh_cr' 
            %control-field2 = if_abap_behv=>mk-on 
            field3 = 6 
            %control-field3 = if_abap_behv=>mk-on 
            field4 = 7 
            %control-field4 = if_abap_behv=>mk-on ) 
          ( %cid = 'cid5' 
            %is_draft = if_abap_behv=>mk-off 
            key_field = 4 
            %control-key_field = if_abap_behv=>mk-on 
            field1 = 'iii_cr' 
            %control-field1 = if_abap_behv=>mk-on 
            field2 = 'jjj_cr' 
            %control-field2 = if_abap_behv=>mk-on 
            field3 = 5555 
            %control-field3 = if_abap_behv=>mk-on 
            field4 = 7 
            %control-field4 = if_abap_behv=>mk-on ) 
          ( %cid = 'cid6'                             "Error 
            %is_draft = if_abap_behv=>mk-off 
            key_field = 4 
            %control-key_field = if_abap_behv=>mk-on 
            field1 = 'kkk_cr' 
            %control-field1 = if_abap_behv=>mk-on 
            field2 = 'lll_cr' 
            %control-field2 = if_abap_behv=>mk-on 
            field3 = 6 
            %control-field3 = if_abap_behv=>mk-on 
            field4 = 7 
            %control-field4 = if_abap_behv=>mk-on ) 
          ( %cid = 'cid7' 
            %is_draft = if_abap_behv=>mk-off 
            key_field = 6 
            %control-key_field = if_abap_behv=>mk-on 
            field1 = 'mmm_cr' 
            %control-field1 = if_abap_behv=>mk-on 
            field2 = 'ZZZ' 
            %control-field2 = if_abap_behv=>mk-on 
            field3 = 6 
            %control-field3 = if_abap_behv=>mk-on 
            field4 = 7 
            %control-field4 = if_abap_behv=>mk-on ) 
          ) 
       CREATE BY \_child FROM VALUE #( 
          ( %cid_ref = 'cid1' 
            %is_draft = if_abap_behv=>mk-off 
             %target = VALUE #( 
              ( %cid = 'cid_child1' 
                key_field_child = 1 
                %control-key_field_child = if_abap_behv=>mk-on 
                field1_child = 'nnn_cba' 
                %control-field1_child = if_abap_behv=>mk-on 
                field2_child = 'ooo_cba' 
                %control-field2_child = if_abap_behv=>mk-on 
                field3_child = 2 
                %control-field3_child = if_abap_behv=>mk-on 
                field4_child = 3 
                %control-field4_child = if_abap_behv=>mk-on ) 
              ( %cid = 'cid_child2' 
                key_field_child = 1                    "Error 
                %control-key_field_child = if_abap_behv=>mk-on 
                field1_child = 'ppp_cba' 
                %control-field1_child = if_abap_behv=>mk-on 
                field2_child = 'qqq_cba' 
                %control-field2_child = if_abap_behv=>mk-on 
                field3_child = 2 
                %control-field3_child = if_abap_behv=>mk-on 
                field4_child = 3 
                %control-field4_child = if_abap_behv=>mk-on ) 
          ) ) ) 
        UPDATE FROM VALUE #( 
          ( %cid_ref = 'cid2' 
            %is_draft = if_abap_behv=>mk-off 
            field1 = 'rrr_up' 
            %control-field1 = if_abap_behv=>mk-on 
            field2 = 'sss_up' 
            %control-field2 = if_abap_behv=>mk-on 
            field3 = 4 
            %control-field3 = if_abap_behv=>mk-on 
            field4 = 5 
            %control-field4 = if_abap_behv=>mk-on ) 
          ( %is_draft = if_abap_behv=>mk-off          "Error 
            key_field = 10 
            field1 = 'ttt_up' 
            %control-field1 = if_abap_behv=>mk-on 
            field2 = 'uuu_up' 
            %control-field2 = if_abap_behv=>mk-on 
            field3 = 4 
            %control-field3 = if_abap_behv=>mk-on 
            field4 = 5 
            %control-field4 = if_abap_behv=>mk-on ) 
          ) 
        DELETE FROM VALUE #( 
          ( %cid_ref = 'cid3' 
            %is_draft = if_abap_behv=>mk-off ) 
          ( key_field = 11                       "Error 
            %is_draft = if_abap_behv=>mk-off ) 
          ) 
          FAILED   failed 
          REPORTED reported 
          MAPPED mapped. 
 
    out->write_html( '<b>Responses</b>' 
      )->write_doc( cl_demo_output_helper=>get_infobox_html( 
`The following tables show the information that has been returned ` && 
`by the <code>mapped</code>, <code>failed</code> and ` && 
`<code>reported</code> parameters before triggering the save ` && 
`sequence using a <code>COMMIT</code> statement. <br>Note that ` && 
`only the responses for the root entity are covered. <br>` && 
`In the given example, the global authorization (method ` && 
`<code>get_global_authorization</code>) is always granted. In case ` && 
`the conditions are met for the <code>get_global_features</code> ` && 
`method, deleting and updating is allowed. Other handler methods ` && 
`that are called afterwards (e.g. <code>create</code>), ` && 
`purposely return information on failed instances due to improper ` && 
`values from the RAP BO consumer.` ) ). 
    "Displaying response information 
    display_responses( ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time 
       FROM demo_tab_root_4 
       ORDER BY key_field 
       INTO TABLE @FINAL(itab_root). 
 
    SELECT key_field, key_field_child, field1_child, field2_child, 
           field3_child, field4_child 
       FROM demo_tab_child_4 
       ORDER BY key_field 
       INTO TABLE @FINAL(itab_child). 
 
    get_handler_meth(  ). 
 
    out->write_html( '<b>Database table entries</b>' 
    )->write_doc( cl_demo_output_helper=>get_infobox_html( 
      `<ul><li>The table <code>itab_root</code> shows ` && 
      `database table entries of the root entitiy after ` && 
      `the EML MODIFY operations.</li>` && 
      `<li>The table <code>itab_child</code> shows ` && 
      `database table entries of the child entitiy after ` && 
      `the create-by-association operation.</li></ul>` ) 
    )->write( data = itab_root exclude = `client` 
              name = `itab_root` 
    )->write( data = itab_child exclude = `client` 
              name = `itab_child` ). 
 
********************************************************************** 
 
    out->line( 
        )->next_section( `2) Second run of standard operations ` && 
                         ` on active instances using EML MODIFY` ). 
 
    MODIFY ENTITY demo_unmanaged_root_draft 
      CREATE FROM VALUE #( 
         ( %cid = 'cid7'                          "Error 
           %is_draft = if_abap_behv=>mk-off 
           key_field = 1 
           %control-key_field = if_abap_behv=>mk-on 
           field1 = 'www' 
           %control-field1 = if_abap_behv=>mk-on 
           field2 = 'xxx' 
           %control-field2 = if_abap_behv=>mk-on 
           field3 = 2 
           %control-field3 = if_abap_behv=>mk-on 
           field4 = 3 
           %control-field4 = if_abap_behv=>mk-on ) 
         ( %cid = 'cid8' 
           %is_draft = if_abap_behv=>mk-off 
           key_field = 8 
           %control-key_field = if_abap_behv=>mk-on 
           field1 = 'yyy' 
           %control-field1 = if_abap_behv=>mk-on 
           field2 = 'zzz' 
           %control-field2 = if_abap_behv=>mk-on 
           field3 = 4 
           %control-field3 = if_abap_behv=>mk-on 
           field4 = 5 
           %control-field4 = if_abap_behv=>mk-on ) ) 
      CREATE BY \_child FROM VALUE #( 
         ( key_field = 1 
           %is_draft = if_abap_behv=>mk-off 
            %target = VALUE #( ( 
             %cid = 'cid_child1' 
             key_field_child = 1                            "Error 
             %control-key_field_child = if_abap_behv=>mk-on 
             field1_child = 'aaa_cba' 
             %control-field1_child = if_abap_behv=>mk-on 
             field2_child = 'bbb_cba' 
             %control-field2_child = if_abap_behv=>mk-on 
             field3_child = 2 
             %control-field3_child = if_abap_behv=>mk-on 
             field4_child = 3 
             %control-field4_child = if_abap_behv=>mk-on ) ) ) 
         ( key_field = 2 
           %is_draft = if_abap_behv=>mk-off 
            %target = VALUE #( ( 
             %cid = 'cid_child2' 
             key_field_child = 4 
             %control-key_field_child = if_abap_behv=>mk-on 
             field1_child = 'ccc_cba' 
             %control-field1_child = if_abap_behv=>mk-on 
             field2_child = 'ddd_cba' 
             %control-field2_child = if_abap_behv=>mk-on 
             field3_child = 5 
             %control-field3_child = if_abap_behv=>mk-on 
             field4_child = 6 
             %control-field4_child = if_abap_behv=>mk-on ) ) ) ) 
      UPDATE FROM VALUE #( 
         ( key_field = 4 
           %is_draft = if_abap_behv=>mk-off 
           field3 = 5555 
           %control-field3 = if_abap_behv=>mk-on ) 
         ( key_field = 2 
           %is_draft = if_abap_behv=>mk-off 
           field2 = 'eee_up' 
           %control-field2 = if_abap_behv=>mk-on 
           field3 = 999 
           %control-field3 = if_abap_behv=>mk-on ) 
         ( %is_draft = if_abap_behv=>mk-off 
           key_field = 100                             "Error 
           field2 = 'fff_up' 
           %control-field2 = if_abap_behv=>mk-on ) ) 
      DELETE FROM VALUE #( 
         ( key_field = 6                               "Error 
           %is_draft = if_abap_behv=>mk-off ) 
         ( key_field = 22                              "Error 
           %is_draft = if_abap_behv=>mk-off ) ) 
         FAILED   failed 
         REPORTED reported 
         MAPPED mapped. 
 
    out->write_html( '<b>Responses</b>' 
      )->write_doc( cl_demo_output_helper=>get_infobox_html( 
`The following tables show the information that has been returned ` && 
`by the <code>mapped</code>, <code>failed</code> and ` && 
`<code>reported</code> parameters before triggering the save ` && 
`sequence using a <code>COMMIT</code> statement. <br>Note that ` && 
`only the responses for the root entity are covered. <br>` && 
`In the given example, the global authorization (method ` && 
`<code>get_global_authorization</code>) is always granted. In case ` && 
`the conditions are met for the <code>get_global_features</code> ` && 
`method, deleting and updating is allowed. This run of EML ` && 
`MODIFY operations includes failures that are returned by the ` && 
`<code>get_instance_authorizations</code> and ` && 
`<code>get_instance_features</code> methods among others.` ) ). 
    "Displaying response information 
    display_responses( ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time 
       FROM demo_tab_root_4 
       ORDER BY key_field 
       INTO TABLE @FINAL(itab_root2). 
 
    SELECT key_field, key_field_child, field1_child, field2_child, 
           field3_child, field4_child 
       FROM demo_tab_child_4 
       ORDER BY key_field 
       INTO TABLE @FINAL(itab_child2). 
 
    get_handler_meth(  ). 
 
    out->write_html( '<b>Database table entries</b>' 
    )->write_doc( cl_demo_output_helper=>get_infobox_html( 
      `<ul><li>The table <code>itab_root2</code> shows ` && 
      `database table entries of the root entitiy after ` && 
      `the EML MODIFY operations.</li>` && 
      `<li>The table <code>itab_child2</code> shows ` && 
      `database table entries of the child entitiy after ` && 
      `the create-by-association operation.</li></ul>` ) 
    )->write( data = itab_root2 exclude = `client` name = `itab_root2` 
    )->write( data = itab_child2 exclude = `client` 
              name = `itab_child2` ). 
 
********************************************************************** 
 
    out->line( 
        )->next_section( `3) Executing actions on active instances` ). 
 
    out->write_html( '<b>Executing action1</b>' ). 
 
    MODIFY ENTITY demo_unmanaged_root_draft 
     EXECUTE action1 
     FROM VALUE #( ( key_field = 2 ) 
                   ( key_field = 12 ) "Error 
                 ) 
     FAILED failed 
     REPORTED reported. 
 
    "Displaying response information 
    display_responses( ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time 
     FROM demo_tab_root_4 
     ORDER BY key_field 
     INTO TABLE @FINAL(db_after_action1). 
 
    get_handler_meth(  ). 
 
    out->write_doc( '<b>Database table entries:</b>' 
    )->write_doc( cl_demo_output_helper=>get_infobox_html( 
      `The table <code>db_after_action1</code> shows ` && 
      `database table entries of the root entitiy after ` && 
      `executing <code>action1</code>.<br>` && 
      `In the given example, the value of <code>field2</code> ` && 
      `is changed by the action for instances specified by the ` && 
      `RAP consumer.` ) 
    )->write( data = db_after_action1 exclude = `client` 
              name = `db_after_action1` ). 
 
    out->write_html( '<b>Executing action2</b>' ). 
 
    MODIFY ENTITY demo_unmanaged_root_draft 
     EXECUTE action2 
     FROM VALUE #( ( key_field = 1 ) 
                   ( key_field = 11 ) "Error 
                 ) 
     RESULT action_result 
     FAILED   failed 
     REPORTED reported. 
 
    display_responses( ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time 
     FROM demo_tab_root_4 
     ORDER BY key_field 
     INTO TABLE @FINAL(db_after_action2). 
 
    get_handler_meth(  ). 
 
    out->write_doc( '<b>Database table entries and action result:</b>' 
    )->write_doc( cl_demo_output_helper=>get_infobox_html( 
      `The table <code>db_after_action2</code> shows ` && 
      `database table entries of the root entitiy after ` && 
      `executing <code>action2</code>.<br>` && 
      `In the given example, the value of <code>field1</code>` && 
      ` is changed by the action for instances specified by the ` && 
      `RAP consumer. Additionally, a table is displayed showing ` && 
      `the action result that is returned.` ) ). 
 
    out->write( data = db_after_action2 exclude = `client` 
              name = `db_after_action2` ). 
 
    out->write( action_result ). 
 
    out->write_html( '<b>Executing action3</b>' ). 
 
    MODIFY ENTITY demo_unmanaged_root_draft 
     EXECUTE action3 
     FROM VALUE #( 
        ( key_field = 4 %param-discount_percent = '40' ) 
        ( key_field = 13 %param-discount_percent = '40' ) "Error 
        ( key_field = 1 %param-discount_percent = '200' ) "Error 
                 ) 
     REQUEST VALUE #( key_field = if_abap_behv=>mk-on 
                      field3 = if_abap_behv=>mk-on 
                      field4 = if_abap_behv=>mk-on 
                      lchg_date_time = if_abap_behv=>mk-on ) 
     RESULT action_result2 
     FAILED   failed 
     REPORTED reported. 
 
    display_responses( ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time 
     FROM demo_tab_root_4 
     ORDER BY key_field 
     INTO TABLE @FINAL(db_after_action3). 
 
    get_handler_meth(  ). 
 
    out->write_doc( '<b>Database table entries and action result:</b>' 
    )->write_doc( cl_demo_output_helper=>get_infobox_html( 
    `The table <code>db_after_action3</code> shows ` && 
    `database table entries of the root entitiy after ` && 
    `executing <code>action3</code>.<br>` && 
    `In the given example, the values of the fields ` && 
    `<code>field3</code> and <code>field4</code> are changed ` && 
    `by the action for instances specified by the RAP consumer. ` && 
    `Here, the values of the numbers are reduced by a percentage ` && 
    `that is specified by the RAP consumer, too. Additionally, a ` && 
  `table is displayed showing the action result that is returned.` ) ). 
 
    out->write( data = db_after_action3 exclude = `client` 
              name = `db_after_action3` ). 
 
    out->write( action_result2 ). 
 
    out->write_html( '<b>Executing action4</b>' ). 
 
    MODIFY ENTITY demo_unmanaged_root_draft 
     EXECUTE action4 
     AUTO FILL CID WITH VALUE #( ( key_field = 1 ) 
                                 ( key_field = 123 ) "Error 
                   ) 
 
     FAILED   failed 
     REPORTED reported. 
 
    display_responses( ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time 
     FROM demo_tab_root_4 
     ORDER BY key_field 
     INTO TABLE @FINAL(db_after_action4). 
 
    get_handler_meth(  ). 
 
    out->write_doc( '<b>Database table entries and action result:</b>' 
    )->write_doc( cl_demo_output_helper=>get_infobox_html( 
      `The table <code>db_after_action4</code> shows ` && 
      `database table entries of the root entitiy after ` && 
      `executing <code>action4</code>.<br>` && 
      `In the given example, the action is implemented in ` && 
      `a way that instances are copied. In the BDEF, the ` && 
      `action is defined with a precheck, hence, before calling ` && 
      `the action, the <code>precheck_action4</code> method is ` && 
      `called before. This precheck method checks if a field has ` && 
      `a certain value. If the value is available, the action shall` && 
      ` not be executed.` ) 
         )->write( data = db_after_action4 exclude = `client` 
                   name = `db_after_action4` ). 
 
********************************************************************** 
 
    out->line( 
         )->next_section( `4) READ, READ BY operations + executing` && 
                          ` functions on active instances` ). 
 
    "Read operation 
    READ ENTITY demo_unmanaged_root_draft 
    FROM VALUE #( 
       ( key_field = 1 
         %control-field1 = if_abap_behv=>mk-on 
         %control-field2 = if_abap_behv=>mk-on 
         %control-field3 = if_abap_behv=>mk-on 
         %control-field4 = if_abap_behv=>mk-on 
         %control-crea_date_time = if_abap_behv=>mk-on 
         %control-lchg_date_time = if_abap_behv=>mk-on ) 
       ( key_field = 2 
         %control-field1 = if_abap_behv=>mk-on 
         %control-field2 = if_abap_behv=>mk-on 
         %control-field3 = if_abap_behv=>mk-on 
         %control-field4 = if_abap_behv=>mk-on 
         %control-crea_date_time = if_abap_behv=>mk-on 
         %control-lchg_date_time = if_abap_behv=>mk-on ) 
       ( key_field = 10                                    "Error 
         %control-field1 = if_abap_behv=>mk-on 
         %control-field2 = if_abap_behv=>mk-on 
         %control-field3 = if_abap_behv=>mk-on 
         %control-field4 = if_abap_behv=>mk-on 
         %control-crea_date_time = if_abap_behv=>mk-on 
         %control-lchg_date_time = if_abap_behv=>mk-on ) 
                  ) 
       RESULT FINAL(read_result_root) 
       FAILED failed 
       REPORTED reported. 
 
    out->write_html( '<b>Read operation on root entity</b>' 
      )->write_doc( cl_demo_output_helper=>get_infobox_html( 
  `The tables showing the FAILED and REPORTED responses are ` && 
  `followed by a table showing the read result. The read operation ` && 
  `is executed for the root entity only.` ) ). 
 
    display_responses( ). 
 
    out->write_doc( '<b>Read result:</b>' 
      )->write( data = read_result_root exclude = `client` 
                name = `read_result_root` ). 
 
    "Read-by-association operation 
    READ ENTITY demo_unmanaged_root_draft 
     BY \_child FROM VALUE #( 
     ( key_field = 1 
       %control-key_field_child = if_abap_behv=>mk-on 
       %control-field1_child = if_abap_behv=>mk-on 
       %control-field2_child = if_abap_behv=>mk-on 
       %control-field3_child = if_abap_behv=>mk-on 
       %control-field4_child = if_abap_behv=>mk-on ) 
     ( key_field = 2 
       %control-key_field_child = if_abap_behv=>mk-on 
       %control-field1_child = if_abap_behv=>mk-on 
       %control-field2_child = if_abap_behv=>mk-on 
       %control-field3_child = if_abap_behv=>mk-on 
       %control-field4_child = if_abap_behv=>mk-on ) 
     ( key_field = 7                                     "Error 
       %control-key_field_child = if_abap_behv=>mk-on 
       %control-field1_child = if_abap_behv=>mk-on 
       %control-field2_child = if_abap_behv=>mk-on 
       %control-field3_child = if_abap_behv=>mk-on 
       %control-field4_child = if_abap_behv=>mk-on ) 
      ) 
     RESULT FINAL(read_result_child) 
     LINK links 
     FAILED failed 
     REPORTED reported. 
 
    out->write_html( `<b>Read-by-association operation ` && 
                     `on child entity</b>` 
      )->write_doc( cl_demo_output_helper=>get_infobox_html( 
  `The read operation is only executed for the child entity  ` && 
  `using <code>READ BY</code>. The respective method for ` && 
  `read-by-association operations also returns association ` && 
  `links apart from FAILED and REPORTED responses. <br>` && 
  `These tables are followed by the read result in the output.` ) ). 
 
    display_responses( ). 
 
    out->write( links ). 
 
    out->write_doc( '<b>Read result:</b>' 
      )->write( data = read_result_child exclude = `client` 
                name = `read_result_child` ). 
 
    "Read operation executing a static function 
    READ ENTITY demo_unmanaged_root_draft 
     EXECUTE function1 
     FROM VALUE #( ( %cid = 'cid_stat_func' ) ) 
     RESULT FINAL(stat_func_result) 
     FAILED   failed 
     REPORTED reported. 
 
    out->write_html( `<b>Read operation operation executing ` && 
                     `a static function</b>` 
      )->write_doc( cl_demo_output_helper=>get_infobox_html( 
  `<code>function1</code> applies to the complete RAP BO, ` && 
  `not to any specific entity instance. In the given example, ` && 
  `the respective method for the function is implemented to ` && 
  `do a simple calculation: The sum of all values of ` && 
  `<code>field3</code> that are available in the database ` && 
  `table and have a value higher than 100 is calculated. ` && 
  `The read result table shows the calculated number.` ) ). 
 
    display_responses( ). 
 
    out->write_doc( `<b>Read result for function execution` && 
    ` (function1):</b>` 
      )->write( data = stat_func_result "[ 1 ]-%param 
                name = `Function result` ). 
 
    "Read operation executing an instance function 
    READ ENTITY demo_unmanaged_root_draft 
     EXECUTE function2 
     FROM VALUE #( ( key_field = 1 
                     %param-discount_percent = '50' ) 
                   ( key_field = 4                   "Error 
                     %param-discount_percent = '150' ) 
                   ( key_field = 6 
                     %param-discount_percent = '50' ) ) 
     RESULT func_result 
     FAILED failed 
     REPORTED reported. 
 
    out->write_html( `<b>Read operation operation executing ` && 
                     `an instance function</b>` 
      )->write_doc( cl_demo_output_helper=>get_infobox_html( 
  `<code>function2</code> is an instance function with an ` && 
  ` input parameter. Hence, an input parameter is specified ` && 
  `by the RAP BO consumer for particular instances.<br>` && 
  `In the given example, the respective method for the ` && 
  `function is implemented to do a simple calculation: ` && 
  `The input parameter represents the percentage by which ` && 
  `the value of <code>field3</code> is reduced. The percentage ` && 
  `can only be between 0 and 100.<br>` && 
  `The read result table shows the calculated values.` ) ). 
 
    display_responses( ). 
 
    out->write_doc( `<b>Read result for function execution` && 
    ` (function2):</b>` ). 
    out->write( func_result ). 
 
    "Read operation executing a function with selective result 
    READ ENTITY demo_unmanaged_root_draft 
      EXECUTE function3 
      FROM VALUE #( ( key_field =  1 ) 
                    ( key_field =  2 ) 
                    ( key_field =  22 ) )   "Error 
      REQUEST VALUE #( key_field = if_abap_behv=>mk-on 
                       crea_date_time = if_abap_behv=>mk-on ) 
      RESULT func_result_selective 
      FAILED failed 
      REPORTED reported. 
 
    out->write_html( `<b>Read operation operation executing ` && 
                     `a function with selective result</b>` 
      )->write_doc( cl_demo_output_helper=>get_infobox_html( 
  `<code>function3</code> is a function that is specified with ` && 
  `a selective result in the BDEF. ` && 
  `Hence, the RAP BO consumer specifies request parameters to ` && 
  `only retrieve specific field values. In the given example, ` && 
  `only the keys and the creation date are requested. ` && 
  `Consequently, the read result table only shows those values. ` && 
  `The zeroes displayed for <code>field3</code>, ` && 
  `<code>field4</code> and <code>lchg_date_time</code> ` && 
  `can be ignored.` ) ). 
 
    display_responses( ). 
 
    out->write( 'Read result for function execution (function3):' ). 
    out->write( func_result_selective ). 
 
 
    out->write_html( '<b>Handler methods called</b>' 
      )->write( data = bp_demo_unmanaged_root_draft=>handlers_called 
                name = 'Handler methods log table' ). 
    CLEAR bp_demo_unmanaged_root_draft=>handlers_called. 
 
********************************************************************** 
 
    out->line( 
      )->next_section( `5) Creating draft instances` ). 
 
    MODIFY ENTITY demo_unmanaged_root_draft 
     CREATE FROM VALUE #( 
        ( %cid = 'cid1' 
          %is_draft = if_abap_behv=>mk-on 
          field1 = 'aaa' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'bbb' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 2 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 3 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid2' 
          %is_draft = if_abap_behv=>mk-on 
          field1 = 'ccc' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'ddd' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 4 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 5 
          %control-field4 = if_abap_behv=>mk-on ) 
        ( %cid = 'cid3'               "Instance will not be persisted. 
          %is_draft = if_abap_behv=>mk-on 
          field1 = 'eee' 
          %control-field1 = if_abap_behv=>mk-on 
          field2 = 'fff' 
          %control-field2 = if_abap_behv=>mk-on 
          field3 = 2000 
          %control-field3 = if_abap_behv=>mk-on 
          field4 = 7 
          %control-field4 = if_abap_behv=>mk-on ) ) 
        FAILED failed 
        REPORTED reported 
        MAPPED mapped. 
 
    out->write_html( `<b>Responses before committing the ` && 
                     `created draft instances</b>` 
      )->write_doc( cl_demo_output_helper=>get_infobox_html( 
  `The responses before committing the created draft instances show` && 
  ` the effect of calling the <code>earlynumbering_create</code> ` && 
  `method. The RAP BO consumer does not specify the keys, and the ` && 
  `method assigns the keys to the new instances. The determination ` && 
  `<code>det_on_modify</code> is called, too.` ) ). 
 
    display_responses( ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time, draftentitycreationdatetime, 
           draftentitylastchangedatetime 
     FROM demo_tab_dr_ro 
     ORDER BY key_field 
     INTO TABLE @FINAL(draft_parent_before_act). 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time 
   FROM demo_tab_root_4 
   ORDER BY key_field 
   INTO TABLE @FINAL(db_tab_root_before_act). 
 
    "Get keys for activate action. 
    LOOP AT mapped-demo_unmanaged_root_draft 
      ASSIGNING FIELD-SYMBOL(<key>). 
      APPEND VALUE #( key_field = <key>-%key-key_field ) 
                             TO activate_tab. 
    ENDLOOP. 
 
    MODIFY ENTITY demo_unmanaged_root_draft 
      EXECUTE Activate AUTO FILL CID WITH activate_tab 
      MAPPED mapped 
      FAILED failed 
      REPORTED reported. 
 
    CLEAR activate_tab. 
 
    out->write_html( `<b>Responses of the ACTIVATE action ` && 
                     `before committing</b>` 
      )->write_doc( cl_demo_output_helper=>get_infobox_html( 
  `The responses of the <code>activate</code> action ` && 
  `show the effect of the validation <code>validation</code> whose ` && 
  `method is called in the course of the saving process. While  ` && 
  `the determination <code>det_on_save</code> does not return a ` && 
  `failure, the validation fails for a particular instance. In this` && 
  ` example, the validation fails for instances whose ` && 
  `<code>field3</code> value is higher than 1000. The RAP ` && 
  `framework provides an additional entry in FAILED and REPORTED.` ) ). 
 
    display_responses( ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time, draftentitycreationdatetime, 
           draftentitylastchangedatetime 
      FROM demo_tab_dr_ro 
      ORDER BY key_field 
      INTO TABLE @FINAL(draft_parent_afer_act). 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time 
      FROM demo_tab_root_4 
      ORDER BY key_field 
      INTO TABLE @FINAL(db_tab_root_after_act). 
 
    out->write_html( '<b>Handler methods called</b>' 
      )->write( data = bp_demo_unmanaged_root_draft=>handlers_called 
                name = 'Handler methods log table' ). 
    CLEAR bp_demo_unmanaged_root_draft=>handlers_called. 
 
    out->write_html( `<b>Draft and database tables</b>` 
      )->write_doc( cl_demo_output_helper=>get_infobox_html( 
  `The following tables demonstrate the effect on the draft and ` && 
  `database tables. In this example, only the tables for the ` && 
  `root entity are covered. The first two tables show the state ` && 
  `of the draft and database table before the activation, i. e. ` && 
  `new draft instances are created and, thus, available in the ` && 
  `draft table. To visualize the successful calling of the ` && 
  `determination method <code>det_on_modify</code>, the string ` && 
  `<code>draft_</code> gets added to the string in ` && 
  `<code>field1</code>. At this stage, the database table only ` && 
  `shows those entries that have been created in the operations ` && 
  `beforehand.<br>` && 
  `The next two tables show the state of the draft and database` && 
  ` tables after the activation using the <code>activate</code> ` && 
  `method and a <code>COMMIT ENTITIES</code> statement. Since the ` && 
  `validation returns an error for an instance, the instance ` && 
  `remains in the draft table and is not persisted to the database.` && 
  ` The database table now includes the former draft instances` && 
  ` that have been persisted to the database. Furthermore, the ` && 
  `effects of the methods <code>det_on_save</code> (the value ` && 
  `of <code>field4</code> is divided by 2) and ` && 
  `<code>discard</code> (the underscore in the string of ` && 
  `<code>field1</code> is removeare visible.` ) 
            )->write( data = draft_parent_before_act exclude = `client` 
                      name = 'Draft table before activation' 
            )->write( data = db_tab_root_before_act exclude = `client` 
                      name = 'Database table before activation' 
            )->write( data = draft_parent_afer_act exclude = `client` 
                      name = 'Draft table after activation' 
            )->write( data = db_tab_root_after_act exclude = `client` 
                      name = 'Database table after activation' 
            ). 
 
********************************************************************** 
 
    out->line( 
      )->next_section( `6) Updating draft instances` ). 
 
    MODIFY ENTITY demo_unmanaged_root_draft 
       EXECUTE Edit AUTO FILL CID WITH 
       VALUE #( ( %key-key_field = 1 
                  %param-preserve_changes = abap_false ) 
                ( %key-key_field = 2 
                  %param-preserve_changes = abap_false ) 
              ) 
       REPORTED reported 
       FAILED failed 
       MAPPED mapped. 
 
    out->write_html( `<b>Responses before committing the ` && 
                     `edited draft instances</b>` 
      )->write_doc( cl_demo_output_helper=>get_infobox_html( 
  `The responses before committing the edited draft instances just` && 
  ` show that, among others, the <code>edit</code> method ` && 
  `has been called.` ) ). 
 
    display_responses( ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time, draftentitycreationdatetime, 
           draftentitylastchangedatetime 
     FROM demo_tab_dr_ro 
     ORDER BY key_field 
     INTO TABLE @FINAL(draft_parent_before_act2). 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time 
     FROM demo_tab_root_4 
     ORDER BY key_field 
     INTO TABLE @FINAL(db_tab_root_before_act2). 
 
    "Get keys for the ACTIVATE action. 
    LOOP AT mapped-demo_unmanaged_root_draft 
      ASSIGNING FIELD-SYMBOL(<key2>). 
      APPEND VALUE #( key_field = <key2>-%key-key_field ) 
                             TO activate_tab. 
    ENDLOOP. 
 
    MODIFY ENTITY demo_unmanaged_root_draft 
      EXECUTE Activate AUTO FILL CID WITH activate_tab 
      REPORTED reported 
      FAILED failed 
      MAPPED mapped. 
 
    CLEAR activate_tab. 
 
    out->write_html( `<b>Responses of the ACTIVATE action ` && 
                     `before committing</b>` 
      )->write_doc( cl_demo_output_helper=>get_infobox_html( 
  `The responses of the <code>activate</code> action just show,` && 
  ` that, among others, the <code>update</code> method has` && 
  ` been called.` ) ). 
 
    display_responses( ). 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time, draftentitycreationdatetime, 
           draftentitylastchangedatetime 
         FROM demo_tab_dr_ro 
         ORDER BY key_field 
         INTO TABLE @FINAL(draft_parent_afer_act2). 
 
    SELECT key_field, field1, field2, 
           field3, field4, crea_date_time, 
           lchg_date_time 
   FROM demo_tab_root_4 
   ORDER BY key_field 
   INTO TABLE @FINAL(db_tab_root_after_act2). 
 
    get_handler_meth(  ). 
 
    out->write_html( `<b>Draft and database tables</b>` 
      )->write_doc( cl_demo_output_helper=>get_infobox_html( 
  `The following tables demonstrate the effect on the draft and ` && 
  `database tables. In this example, only the tables for the ` && 
  `root entity are covered. The first two tables show the state ` && 
  `of the draft and database table before the activation, i. e. ` && 
  `persisted instances are inserted in the draft table.` && 
  `In this example, the failed instance of the previous draft` && 
  `instance creation procedure is still available in the table. ` && 
  `It can be ignored. The effect of the <code>edit</code> ` && 
  `method is visible: the strings in <code>field1</code> are ` && 
  `converted to upper case.` && 
  ` At this stage, the database table only ` && 
  `shows those entries that have been created in the operations ` && 
  `beforehand.<br>` && 
  `The next two tables show the state of the draft and database` && 
  ` tables after the activation using the <code>activate</code> ` && 
  `method and a <code>COMMIT ENTITIES</code> statement. Since the ` && 
  `validation has returned an error for an instance in the previous` && 
  ` draft instance creation, the instance is still visible in the ` && 
  `draft table. It can be ignored. The database table shows all ` && 
  `persisted instances including the newly edited instances with ` && 
  `the strings in <code>field2</code> in upper case. ` ) 
          )->write( data = draft_parent_before_act2 exclude = `client` 
                    name = 'Draft table before activation' 
          )->write( data = db_tab_root_before_act2 exclude = `client` 
                    name = 'Database table before activation' 
          )->write( data = draft_parent_afer_act2 exclude = `client` 
                    name = 'Draft table after activation' 
          )->write( data = db_tab_root_after_act2 exclude = `client` 
                    name = 'Database table after activation' 
          ). 
 
********************************************************************** 
 
  ENDMETHOD. 
  METHOD display_responses. 
    IF mapped-demo_unmanaged_root_draft IS NOT INITIAL 
    OR mapped-demo_unmanaged_child_draft IS NOT INITIAL. 
      out->write( data = mapped 
                name = `Entries in MAPPED response parameter ` && 
                       `` ). 
    ENDIF. 
    IF failed IS NOT INITIAL. 
      out->write( data = extract_from_failed( ) 
                name = `Entries in FAILED response parameter` ). 
    ENDIF. 
    IF reported IS NOT INITIAL. 
      out->write( data = extract_from_reported( ) 
                name = `Entries in REPORTED response parameter` ). 
    ENDIF. 
  ENDMETHOD. 
  METHOD extract_from_failed. 
    CLEAR errors. 
 
    LOOP AT failed-demo_unmanaged_root_draft 
    ASSIGNING FIELD-SYMBOL(<err>). 
 
      DATA op TYPE string. 
 
      CASE if_abap_behv=>mk-on. 
        WHEN <err>-%op-%create. 
          op = `create operation`. 
        WHEN <err>-%op-%update. 
          op = `update operation`. 
        WHEN <err>-%op-%delete. 
          op = `delete operation`. 
        WHEN <err>-%op-%assoc-_child. 
          op = `operation involving the child entity`. 
        WHEN OTHERS. op = `operation`. 
      ENDCASE. 
 
      APPEND `Error for instance with ` && 
           COND #( WHEN <err>-%cid IS NOT INITIAL THEN `%cid = ` 
                   && <err>-%cid 
                   ELSE `key = ` && <err>-key_field ) && 
           `: Fail cause ` &&  <err>-%fail-cause && ` for ` &&  op 
            && `.` TO errors. 
 
    ENDLOOP. 
 
    IF failed-demo_unmanaged_child_draft IS NOT INITIAL. 
      LOOP AT failed-demo_unmanaged_child_draft 
      ASSIGNING FIELD-SYMBOL(<err_ch>). 
 
        APPEND `Error for child instance with ` && 
             COND #( WHEN <err_ch>-%cid IS NOT INITIAL THEN `%cid = ` 
                     && <err_ch>-%cid 
                     ELSE `key_field = ` && <err_ch>-key_field && 
             ` and key_field_child = ` && <err_ch>-key_field_child ) && 
             `: Fail cause ` &&  <err_ch>-%fail-cause && ` for ` &&  op 
              && `.` TO errors. 
 
      ENDLOOP. 
    ENDIF. 
 
  ENDMETHOD. 
  METHOD extract_from_reported. 
    CLEAR messages. 
 
    LOOP AT reported-demo_unmanaged_root_draft 
    ASSIGNING FIELD-SYMBOL(<rep>). 
      IF <rep>-%global = if_abap_behv=>mk-on. 
        APPEND <rep>-%msg->m_severity && ` ` && 
                <rep>-%msg->if_t100_dyn_msg~msgv1 TO messages. 
      ELSE. 
        APPEND `Message for instance with ` && 
               COND #( WHEN <rep>-%cid IS NOT INITIAL 
                       THEN `%cid = ` && <rep>-%cid 
                       ELSE `key = ` && <rep>-key_field ) && 
               `: ` &&  <rep>-%msg->m_severity && ` ` && 
               <rep>-%msg->if_t100_dyn_msg~msgv1 TO messages. 
 
      ENDIF. 
    ENDLOOP. 
 
    IF reported-demo_unmanaged_child_draft IS NOT INITIAL. 
      LOOP AT reported-demo_unmanaged_child_draft 
      ASSIGNING FIELD-SYMBOL(<rep_ch>). 
        APPEND `Message for child instance with key_field = ` && 
        <rep_ch>-key_field && ` and key_field_child = ` 
        && <rep_ch>-key_field_child && `: ` 
        && <rep_ch>-%msg->m_severity && 
        ` ` && <rep_ch>-%msg->if_t100_dyn_msg~msgv1 TO messages. 
      ENDLOOP. 
    ENDIF. 
 
  ENDMETHOD. 
  METHOD get_handler_meth. 
    out->write_html( '<b>Handler methods called</b>' 
     )->write( data = bp_demo_unmanaged_root_draft=>handlers_called 
               name = 'Handler methods log table' ). 
    CLEAR bp_demo_unmanaged_root_draft=>handlers_called. 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_tab_root_4. 
    DELETE FROM demo_tab_child_4. 
    DELETE FROM demo_tab_dr_ro.                         "#EC CI_NOWHERE 
    DELETE FROM demo_tab_dr_ch.                         "#EC CI_NOWHERE 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the [unmanaged RAP business object](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) from an ABAP class. The main focus of the class is to demonstrate RAP handler methods with several EML requests.

The output shows several runs of operations on RAP BOs to visualize the effect of implementations in the RAP handler methods as outlined above. For the example to display successful modify operations, it must be executed in a certain time frame (see the `get_global_features` method), otherwise all modify operations are disallowed.

1.  **First run of standard operations on active instances using EML `MODIFY`**

    First, `CREATE` and `CREATE BY` operations create instances for the root and child entity. The same modify request includes `UPDATE` and `DELETE` operations on the newly created instances of the root entity. The `mapped`, `failed` and `reported` parameters are filled by the handler methods. The information that is returned by those parameters is displayed in internal tables. Among them, there are instances that purposely cannot be created, updated and deleted. A `COMMIT ENTITIES` statement triggers the save sequence. The outcome of the saving, i. e. the entries persisted to the database tables are displayed in internal tables, too. Another internal table is displayed - triggered by the `get_handler_meth` method - before the database entries showing handler method names. This internal table is considered as logging and visualizing the sequence of the RAP handler method calls in this run of EML modify operations.

2.  **Second run of standard operations on active instances using EML `MODIFY`**

    The purpose of the second run with the same set of modify operations is to visualize the effect of further handler methods, for example `get_instance_authorizations` and `get_instance_features`. The example demonstrates that certain modify operations are not successful because of not meeting conditions that are set in those method implementations.

3.  **Executing actions on active instances**

    Several actions are covered in the example. All of the actions have a different specification in the BDEF to show the variety of possible parameters for actions in the ABP, for example, some actions include result or request parameters. The pattern for the actions in the output is always the same: the response parameters are displayed in internal tables as well as the effect of the action execution by showing the database table entries in internal tables. Additionally, the handler method log table is displayed for all actions. The action result is displayed for those actions that include a result parameter. Action `action4` is a special case since it is specified with `precheck` in the BDEF. Hence, the effect of the method `precheck_action4` must be considered.

4.  **`READ`, `READ BY` operations and executing functions on active instances**

    First, `READ` and `READ BY` operations are covered. The `rba_child` method includes an additional parameter (`association_links`). The content is displayed in an internal table, too, apart from the response information and read result. Then, several functions are covered in the example. All of the functions have a different specification in the BDEF to show the variety of possible parameters for functions in the ABP, for example, a function includes request parameters. The pattern for the functions in the output is always the same: the response parameters are displayed in internal tables as well as the effect of the functions by showing the read result. Additionally, the handler method log table is displayed for all actions. The action result is displayed for those actions that include a result parameter.

5.  **Creating draft instances**

    First, new draft instances are created by marking the `%is_draft` indicator appropriately. The instances do not include a key. Instead, they include a content ID (`%cid`). The key assignment is done with the `earlynumbering_create` method. The handler method log table shows that the determination `det_on_modify` has been called, too. In the output, the response information is displayed before committing the created draft instances. With the `COMMIT ENTITIES` statement, the saving of the draft instances in the draft table is triggered. The execution of the `activate` method turns the draft instances into active instance, and the following `COMMIT ENTITIES` statement finally triggers the saving of the original draft instances to the database table. In the course of the draft action execution, the `det_on_save` and `validation` methods are called among others. The `discard` method is called last. The output shows four internal tables that log the state of draft and database tables: before and after the activation.

    1.  Draft table before the activation: All created draft instances are available in the draft table. Simple edits, e. g. on field `field1` triggered by the `det_on_modify` method are visible.

    2.  Database table before activation: Does not show any changes to entries.

    3.  Draft table after activation: Since the validation failed for one instance, it is still present in the draft table. It can be ignored in the example. Yet, it shows that the two other instances are no longer present.

    4.  Database table after activation: Two of the three original draft instances have been saved to the database table. Simple edits, e. g. on field `field1` triggered by the `discard` method are visible.

6.  **Updating draft instances**

    With the execution of the draft action `edit`, persisted instances are inserted in the draft table and locked on the database table. The locking effect can be checked while debugging in transaction `SM12`. As above, four internal tables are displayed in the output showing the state of draft and database table. The database table after activation shows the successful saving of instances with the simple edits triggered by the `edit` method.
