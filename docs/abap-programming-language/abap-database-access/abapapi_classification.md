---
title: "API Classifications"
source_file: abapapi_classification.html
section: "ABAP Programming Language > ABAP - Database Access > Data Consistency > SAP LUW > Controlled SAP LUW"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# API Classifications

[Released APIs](../../abap-glossary/abenreleased_api_glosry.md) can contain classifications to ensure transactional consistency within the [SAP LUW](../../abap-glossary/abensap_luw_glosry.md). In the context of the [controlled SAP LUW](../../abap-glossary/abencontrolled_sap_luw_glosry.md), the classifications are used to control that functionality encapsulated by the APIs is only used in [transactional phases](../../abap-glossary/abentr_phase_glosry.md) where allowed.

This affects both a consumer and a provider of such an API. A consumer is not allowed to use [classified APIs](../../abap-glossary/abenclassified_api_glosry.md) in certain contexts. Likewise, a provider is not allowed to use certain operations in its implementations. Violations of the transactional consistency are either logged or result in a runtime error.

The classifications are typically included as type definitions in interfaces, classes (in a local class include for all public and protected methods) and function modules (in the top include of the function group).

The [structured type](../../abap-glossary/abenstructured_type_glosry.md) `tx_contract` contains components whose names are the names of those methods that are to be classified. `tx_contract` is a predefined name. The individual components are typed with an [enumerated type](../../abap-glossary/abenenumerated_type_glosry.md) (`ty`) available in the `IF_ABAP_TX_*` interfaces. When used as shown below, the ABAP compiler interprets the methods as classified.

``` abap
TYPES: BEGIN OF tx_contract, 
         method_a TYPE if_abap_tx_read=>ty, 
         method_b TYPE if_abap_tx_modify=>ty, 
         ... 
       END OF tx_contract.
```

The following table shows the classifications, what is allowed and what not in those APIs, and if these APIs are allowed to be called in [transactional phases](../../abap-glossary/abentr_phase_glosry.md) or not:

<table>
<thead>
<tr class="header">
<th><strong>Classification</strong></th>
<th><strong>Notes</strong></th>
<th><strong>Allowed</strong></th>
<th><strong>Not Allowed</strong></th>
<th><strong>Transactional Phases</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">IF_ABAP_TX_FUNCTIONAL</code></td>
<td>Since such an API should have the character of a pure function, that is, it should only compute a mapping between its input and output parameters, the implementation scope for a provider of the API is very restricted.</td>
<td><p>ABAP SQL <a href="abapselect.html"><code class="ph codeph">SELECT</code></a>,</p>
<p>calling APIs tagged with <code class="ph codeph">IF_ABAP_TX_FUNCTIONAL</code></p></td>
<td><p>ABAP EML requests,</p>
<p><a href="abenlock_glosry.html">locks</a>,</p>
<p><a href="abenauthorization_check_glosry.html">authorization checks</a>,</p>
<p>database modifying operations (<a href="abenstandard_db_connection_glosry.html">standard connection</a>),</p>
<p><a href="abapcommit.html"><code class="ph codeph">COMMIT WORK</code></a>, <a href="abaprollback.html"><code class="ph codeph">ROLLBACK WORK</code></a>, <a href="abapcommit_entities.html"><code class="ph codeph">COMMIT ENTITIES</code></a>, <a href="abaprollback_entities.html"><code class="ph codeph">ROLLBACK ENTITIES</code></a>,</p>
<p>implicit and explicit <a href="abendatabase_commit_glosry.html">database commits</a>,</p>
<p>calling APIs tagged with <code class="ph codeph">IF_ABAP_TX_SAVE</code>, <code class="ph codeph">IF_ABAP_TX_MODIFY</code>, <code class="ph codeph">IF_ABAP_TX_READ</code> and <code class="ph codeph">IF_ABAP_TX_SURFACE</code></p></td>
<td>Allowed in both the <code class="ph codeph">modify</code> and <code class="ph codeph">save</code> phases.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">IF_ABAP_TX_READ</code></td>
<td>A consumer can call an API with this classification in the modify transactional phase. Permitted operations for a provider of the API include read requests.</td>
<td><p>ABAP EML read and permission requests,</p>
<p>ABAP SQL <a href="abapselect.html"><code class="ph codeph">SELECT</code></a>,</p>
<p>implicit <a href="abendatabase_commit_glosry.html">database commits</a>,</p>
<p><a href="abenauthorization_check_glosry.html">authorization checks</a>,</p>
<p>calling APIs tagged with <code class="ph codeph">IF_ABAP_TX_FUNCTIONAL</code> and <code class="ph codeph">IF_ABAP_TX_READ</code></p></td>
<td><p>ABAP EML modify requests,</p>
<p>ABAP EML requests <a href="abapin_local_mode.html">in local mode</a> (except for ABAP EML read requests with a managed BDEF),</p>
<p>ABAP EML <a href="abapconvert_key.html">key conversion</a>,</p>
<p><a href="abenlock_glosry.html">locks</a>,</p>
<p>database modifying operations (<a href="abenstandard_db_connection_glosry.html">standard connection</a>),</p>
<p><a href="abapcommit.html"><code class="ph codeph">COMMIT WORK</code></a>, <a href="abaprollback.html"><code class="ph codeph">ROLLBACK WORK</code></a>, <a href="abapcommit_entities.html"><code class="ph codeph">COMMIT ENTITIES</code></a>, <a href="abaprollback_entities.html"><code class="ph codeph">ROLLBACK ENTITIES</code></a>,</p>
<p>explicit <a href="abendatabase_commit_glosry.html">database commits</a>,</p>
<p>calling APIs tagged with <code class="ph codeph">IF_ABAP_TX_SAVE</code>, <code class="ph codeph">IF_ABAP_TX_MODIFY</code> and <code class="ph codeph">IF_ABAP_TX_SURFACE</code></p></td>
<td><p>Allowed in the <code class="ph codeph">modify</code> phase, not allowed in the <code class="ph codeph">save</code> phase.</p>
<p>Since an API classified with <code class="ph codeph">IF_ABAP_TX_READ</code> allows operations that can trigger an implicit database commit, calling such an API is incompatible with the <code class="ph codeph">save</code> transactional phase.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">IF_ABAP_TX_MODIFY</code></td>
<td>A consumer can only call an API with this classification in the modify transactional phase. A provider of the API must not perform illegal operations.</td>
<td><p>ABAP EML read, modify, permission and lock requests,</p>
<p>ABAP SQL <a href="abapselect.html"><code class="ph codeph">SELECT</code></a>, <a href="abenlock_glosry.html">locks</a>,</p>
<p><a href="abenauthorization_check_glosry.html">authorization checks</a>,</p>
<p>implicit <a href="abendatabase_commit_glosry.html">database commits</a>,</p>
<p>calling APIs tagged with <code class="ph codeph">IF_ABAP_TX_MODIFY</code>, <code class="ph codeph">IF_ABAP_TX_FUNCTIONAL</code> and <code class="ph codeph">IF_ABAP_TX_READ</code></p></td>
<td><p>ABAP EML requests <a href="abapin_local_mode.html">in local mode</a>,</p>
<p>ABAP EML <a href="abapconvert_key.html">key conversion</a>,</p>
<p>database modifying operations (<a href="abenstandard_db_connection_glosry.html">standard connection</a>),</p>
<p><a href="abapcommit.html"><code class="ph codeph">COMMIT WORK</code></a>, <a href="abaprollback.html"><code class="ph codeph">ROLLBACK WORK</code></a>, <a href="abapcommit_entities.html"><code class="ph codeph">COMMIT ENTITIES</code></a>, <a href="abaprollback_entities.html"><code class="ph codeph">ROLLBACK ENTITIES</code></a>,</p>
<p>explicit <a href="abendatabase_commit_glosry.html">database commits</a>,</p>
<p>calling APIs tagged with <code class="ph codeph">IF_ABAP_TX_SAVE</code> and <code class="ph codeph">IF_ABAP_TX_SURFACE</code></p></td>
<td>Allowed in the <code class="ph codeph">modify</code> phase, not allowed in the <code class="ph codeph">save</code> phase.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">IF_ABAP_TX_SAVE</code></td>
<td>A consumer can only call an API with this classification in the save transactional phase. A provider of the API must not perform illegal operations.</td>
<td><p>ABAP EML <a href="abapraise_entity_event.html"><code class="ph codeph">RAISE ENTITY EVENT</code></a>,</p>
<p>ABAP EML read requests,</p>
<p>ABAP EML <a href="abapconvert_key.html">key conversion</a>,</p>
<p>ABAP SQL <a href="abapselect.html"><code class="ph codeph">SELECT</code></a>,</p>
<p><a href="abenlock_glosry.html">locks</a>,</p>
<p>database modifying operations (<a href="abenstandard_db_connection_glosry.html">standard connection</a>),</p>
<p>calling APIs tagged with <code class="ph codeph">IF_ABAP_TX_FUNCTIONAL</code> and <code class="ph codeph">IF_ABAP_TX_SAVE</code></p></td>
<td><p>ABAP EML modify, permission and lock requests,</p>
<p>ABAP EML requests <a href="abapin_local_mode.html">in local mode</a>,</p>
<p><a href="abenauthorization_check_glosry.html">authorization checks</a>,</p>
<p><a href="abapcommit.html"><code class="ph codeph">COMMIT WORK</code></a>, <a href="abaprollback.html"><code class="ph codeph">ROLLBACK WORK</code></a>, <a href="abapcommit_entities.html"><code class="ph codeph">COMMIT ENTITIES</code></a>, <a href="abaprollback_entities.html"><code class="ph codeph">ROLLBACK ENTITIES</code></a>,</p>
<p>implicit and explicit <a href="abendatabase_commit_glosry.html">database commits</a>,</p>
<p>calling APIs tagged with <code class="ph codeph">IF_ABAP_TX_SURFACE</code>, <code class="ph codeph">IF_ABAP_TX_READ</code> and <code class="ph codeph">IF_ABAP_TX_MODIFY</code></p></td>
<td>Not allowed in the <code class="ph codeph">modify</code> phase, allowed in the <code class="ph codeph">save</code> phase.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">IF_ABAP_TX_SURFACE</code></td>
<td>A consumer cannot call an API with this classification from RAP BO implementations and from APIs with the other classifications. There are no restrictions for an API provider.</td>
<td><p>Each of the following operations is allowed within the API, but not in <a href="abenbehavior_implement_glosry.html">behavior implementations</a></p>
<p>ABAP EML requests,</p>
<p>ABAP SQL <a href="abapselect.html"><code class="ph codeph">SELECT</code></a>,</p>
<p>ABAP EML <a href="abapraise_entity_event.html"><code class="ph codeph">RAISE ENTITY EVENT</code></a>,</p>
<p><a href="abenlock_glosry.html">locks</a>,</p>
<p><a href="abenauthorization_check_glosry.html">authorization checks</a>,</p>
<p>Database modifying operations (<a href="abenstandard_db_connection_glosry.html">standard connection</a>),</p>
<p><a href="abapcommit.html"><code class="ph codeph">COMMIT WORK</code></a>, <a href="abaprollback.html"><code class="ph codeph">ROLLBACK WORK</code></a>, <a href="abapcommit_entities.html"><code class="ph codeph">COMMIT ENTITIES</code></a>, <a href="abaprollback_entities.html"><code class="ph codeph">ROLLBACK ENTITIES</code></a>,</p>
<p>implicit and explicit <a href="abendatabase_commit_glosry.html">database commits</a>,</p>
<p>calling APIs tagged with each of the <code class="ph codeph">IF_ABAP_TX_*</code> tags available</p></td>
<td><p>ABAP EML requests <a href="abapin_local_mode.html">in local mode</a>,</p>
<p><strong>Note:</strong> Not to be called in <a href="abenbehavior_implement_glosry.html">behavior implementations</a>.</p></td>
<td>Not allowed in both the <code class="ph codeph">modify</code> and <code class="ph codeph">save</code> phases.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">IF_ABAP_TX_COMPLETE</code></td>
<td>The call of the classified API is put under transactional control. When called, an API with this classification always starts in the <code class="ph codeph">modify</code> transactional phase, as if the transactional phase had been explicitly set by calling <code class="ph codeph">cl_abap_tx=&gt;modify( )</code>. At any time during its execution, the API can enter the <code class="ph codeph">save</code> transactional phase by calling <code class="ph codeph">cl_abap_tx=&gt;save( )</code>. From this point on, operations that violate the <code class="ph codeph">SAVE</code> transactional contract are not allowed. When the API is exited, transactional control ends. An API with this classification must not be called from within a transactional contract, i.e. <a href="abenbehavior_implement_glosry.html">ABAP behavior implementations</a>, APIs classified with a transactional contract (including <code class="ph codeph">IF_ABAP_TX_COMPLETE</code> itself) and a transactional phase that has been explicitly set (e.g. using <code class="ph codeph">cl_abap_tx=&gt;modify( )</code>).</td>
<td><p><a href="abenlock_glosry.html">Locks</a>,</p>
<p>ABAP SQL <a href="abapselect.html"><code class="ph codeph">SELECT</code></a>,</p>
<p>calling APIs tagged with <code class="ph codeph">IF_ABAP_TX_FUNCTIONAL</code></p>
<p><strong>Allowed in the modify phase in the API implementation:</strong></p>
<p>ABAP EML read, permission, modify and lock requests,</p>
<p><a href="abenauthorization_check_glosry.html">authorization checks</a>,</p>
<p>implicit <a href="abendatabase_commit_glosry.html">database commits</a>,</p>
<p>calling APIs tagged with <code class="ph codeph">IF_ABAP_TX_READ</code> and <code class="ph codeph">IF_ABAP_TX_MODIFY</code></p>
<p><strong>Allowed in the save phase in the API implementation:</strong></p>
<p><a href="abapraise_entity_event.html"><code class="ph codeph">RAISE ENTITY EVENT</code></a>,</p>
<p>ABAP EML <a href="abapconvert_key.html">key conversion</a>,</p>
<p>database modifying operations (<a href="abenstandard_db_connection_glosry.html">standard connection</a>),</p>
<p>calling APIs tagged with <code class="ph codeph">IF_ABAP_TX_SAVE</code></p></td>
<td><p>ABAP EML requests <a href="abapin_local_mode.html">in local mode</a>,</p>
<p><a href="abapcommit.html"><code class="ph codeph">COMMIT WORK</code></a>, <a href="abaprollback.html"><code class="ph codeph">ROLLBACK WORK</code></a>, <a href="abapcommit_entities.html"><code class="ph codeph">COMMIT ENTITIES</code></a>, <a href="abaprollback_entities.html"><code class="ph codeph">ROLLBACK ENTITIES</code></a>,</p>
<p>explicit <a href="abendatabase_commit_glosry.html">database commits</a>,</p>
<p>calling APIs tagged with <code class="ph codeph">IF_ABAP_TX_SURFACE</code></p></td>
<td>Not allowed in both the <code class="ph codeph">modify</code> and <code class="ph codeph">save</code> phases</td>
</tr>
</tbody>
</table>

## Hints

- Violations of [transactional contracts](../../abap-glossary/abentransactional_contract_glosry.md) detected by the [controlled SAP LUW](../../abap-glossary/abencontrolled_sap_luw_glosry.md) are viewable in the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md) on the *Feed Reader* tab for each system. You can add the *ABAP Contract Check Violations* feed query. Configuration options are available for the feed, including filtering for objects you are responsible for

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code snippet demonstrates an interface that contains methods that are typed with classifications.

``` abap
INTERFACE if_some_interface 
  PUBLIC. 
 
  TYPES: BEGIN OF tx_contract, 
           meth_complete   TYPE if_abap_tx_complete=>ty, 
           meth_read       TYPE if_abap_tx_read=>ty, 
           meth_functional TYPE if_abap_tx_functional=>ty, 
           meth_modify     TYPE if_abap_tx_modify=>ty, 
           meth_save       TYPE if_abap_tx_save=>ty, 
           meth_surface    TYPE if_abap_tx_surface=>ty, 
         END OF tx_contract. 
 
  METHODS: 
    meth_complete ..., 
    meth_functional ..., 
    meth_read ..., 
    meth_modify ..., 
    meth_save ..., 
    meth_surface .... 
 
ENDINTERFACE.
```

## More Information

- ABAP Concepts, topic [Controlled SAP LUW](https://help.sap.com/docs/ABAP_Cloud/f2961be2bd3d403585563277e65d108f/80fe04141e30456c80cc90c5cc838e94?version=sap_cross_product_abap)

- [`CL_ABAP_TX`](abaprap_cl_abap_tx.md)

- [RAP Implementation Rules](../../abap-rap-business-objects/abap-for-rap-business-objects/abaprap_impl_rules.md)

- [Restrictions in RAP Handler and Saver Methods](../../abap-rap-business-objects/abap-for-rap-business-objects/abapinvalid_stmts_in_rap_methods.md)

## Executable Example

The example [`CL_ABAP_TX` and API Classifications](abencl_abap_tx_abexa.md) demonstrates classified APIs.
