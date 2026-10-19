---
title: "RAP Implementation Rules"
source_file: abaprap_impl_rules.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > Other RAP-Related ABAP Language Elements and Topics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP Implementation Rules

The [ABAP contract checks](../../abap-glossary/abencontract_checks_glosry.md) include [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md) checks. The RAP BO contract defines a set of rules and guidelines for the [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) and [consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) implementation to ensure consistency and reliability.

The checks also include transactional contract checks that are implemented in the [controlled SAP LUW](../../abap-glossary/abencontrolled_sap_luw_glosry.md) concept. This concept is implicitly used by RAP.

The following table contains RAP BO contract check violations:

<table>
<thead>
<tr class="header">
<th><strong>RAP BO Contract Check Violation</strong></th>
<th><strong>Details</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Missing <code class="ph codeph">%cid</code></td>
<td><a href="abapderived_types_cid.html"><code class="ph codeph">%cid</code></a> should always be filled in <a href="abenrap_create_operation_glosry.html">RAP create operations</a>, <a href="abenrap_cba_operation_glosry.html">RAP create-by-association operations</a> (here, <code class="ph codeph">%cid</code> should also be filled in the <a href="abapderived_types_target.html">%target</a> structure) and <a href="abenrap_factory_action_glosry.html">RAP factory actions</a>. If <a href="abapderived_types_cid.html"><code class="ph codeph">%cid</code></a> is of no relevance, you can make use of the addition <a href="abapmodify_entity_entities_fields.html"><code class="ph codeph">AUTO FILL CID</code></a> to automatically fill <code class="ph codeph">%cid</code> with a unique dummy value to make sure that it is filled.</td>
</tr>
<tr class="even">
<td>ABAP EML modify operations in RAP save sequence</td>
<td>The RAP BO provider may only perform ABAP EML modify operations in the RAP interaction phase or in the <code class="ph codeph">finalize</code> saver method.</td>
</tr>
<tr class="odd">
<td>Improper provider implementations of <a href="abenrap_bo_draft_action_glosry.html">draft actions</a> that are specified with <a href="abenbdl_draft_action.html"><code class="ph codeph">with additional implementation</code></a></td>
<td><p>Provider implementations of the <a href="abenbdl_draft_action2_abexa.html"><code class="ph codeph">edit</code></a>, <a href="abenbdl_draft_action2_abexa.html"><code class="ph codeph">discard</code></a>, and <a href="abenbdl_draft_action1_abexa.html"><code class="ph codeph">activate</code></a> methods should not return failed entries.</p>
<p>Provider implementations of the <code class="ph codeph">edit</code>, <code class="ph codeph">discard</code>, and <code class="ph codeph">activate</code>, and <a href="abenbdl_draft_action2_abexa.html"><code class="ph codeph">resume</code></a> methods should not return <a href="abenrap_state_mes_glosry.html">state messages</a>. <a href="abapderived_types_state_area.html"><code class="ph codeph">%state_area</code></a> should not be filled.</p></td>
</tr>
<tr class="even">
<td>Improper authorization check</td>
<td>If a BDEF defines authorization checks (<a href="abenbdl_authorization_context.html"><code class="ph codeph">authorization context</code></a>), then no authorization check should be performed that deviates from the definition, i.e. the authorization object used must either be listed in the <code class="ph codeph">own authorization context</code>, or must be suppressed by another context. In such a case, the <code class="ph codeph">BEHAVIOR_UNEXPECTED_AUTH_CHECK</code> runtime error is usually raised.</td>
</tr>
<tr class="odd">
<td>Mapping of invalid preliminary keys</td>
<td><a href="abenrap_bo_consumer_glosry.html">RAP BO consumers</a> must not request the mapping of preliminary keys for which no final keys exist. Therefore, <a href="abenrap_bo_provider_glosry.html">RAP BO providers</a> should map all preliminary keys unless the operation failed. RAP BO consumers should also avoid requesting the mapping for preliminary keys if the corresponding instances have been deleted in the course of the session.</td>
</tr>
<tr class="even">
<td>Not respecting static <a href="abenrap_feature_control_glosry.html">feature control</a></td>
<td>RAP BO consumers must respect the static feature control. For example, fields that are specified as read-only in the BDEF must not be updated, or fields that are specified as mandatory must be provided in a create operation.</td>
</tr>
<tr class="odd">
<td>Unnecessary or ambiguous requests by RAP BO consumers</td>
<td>RAP BO consumers must not request unnecessary or ambiguous operations, that is, an update operation is unnecessary if no fields are changed. Examples of ambiguous operations are duplicate update operations on the same instance, duplicate delete operations, or action or function executions.</td>
</tr>
<tr class="even">
<td>Improper use of <a href="abenrap_bo_augmentation_glosry.html">augmentation</a></td>
<td>An ABAP EML <code class="ph codeph">MODIFY</code> statement using the addition <code class="ph codeph">AUGMENTING</code> must not overwrite fields of the original request, i. e. there must not be a flag in <code class="ph codeph">%control</code> which is set for the same instance and field both in the original and in the augmenting operation. An ABAP EML <code class="ph codeph">MODIFY</code> statement using the addition <code class="ph codeph">AUGMENTING</code> containing operations on instances which are not contained in the original request should relate these instances to instances of the original request by use of the <code class="ph codeph">RELATING</code> clause so that responses can be associated.</td>
</tr>
<tr class="odd">
<td>Non-privileged access</td>
<td>The contract check detects access to CDS views if they are specified with <a href="abencds_access_control_glosry.html">access control</a>, for example, a <code class="ph codeph">SELECT</code> statement without the <code class="ph codeph"> OPTIONS PRIVILEGED ACCESS</code> addition. The check is performed as with an <code class="ph codeph">AUTHORITY-CHECK OBJECT</code> statement. Therefore, in RAP handler and saver methods, as well as in <a href="abenclassified_api_glosry.html">classified APIs</a>, a contract violation occurs where an authorization check is generally not allowed, or access without the <code class="ph codeph">OPTIONS PRIVILEGED ACCESS</code> addition is detected.</td>
</tr>
<tr class="even">
<td>Disallowed entries in the <code class="ph codeph">failed</code> response parameter</td>
<td><p>RAP handler method implementations of actions defined with <code class="ph codeph">with additional implementation</code>, such as the draft actions <code class="ph codeph">edit</code>, <code class="ph codeph">activate</code> and <code class="ph codeph">discard</code> (except <code class="ph codeph">resume</code>), must not add entries to the <code class="ph codeph">failed</code> response parameter as they cannot be considered for the current processing phase. Otherwise, the runtime error <code class="ph codeph">BEHAVIOR_BAD_HANDLER_RESPONSE</code> is raised.</p>
<p>RAP handler methods of ABAP EML modify operations must not add entries to <code class="ph codeph">failed</code> that do not correspond to instances that are input for the operation.</p></td>
</tr>
<tr class="odd">
<td>Entries with wrong fail causes in the <code class="ph codeph">failed</code> response parameter</td>
<td><p>RAP handler method implementations are allowed to add entries the following fail causes:</p>
<p>Precheck, augmentation: Any fail cause, except <code class="ph codeph">if_abap_behv=&gt;cause-locked</code></p>
<p>RAP saver methods <code class="ph codeph">adjust_numbers</code>, <code class="ph codeph">save</code>, <code class="ph codeph">save_modified</code>, <code class="ph codeph">finalize</code>, <code class="ph codeph">check_before_save</code>, and RAP handler methods with <code class="ph codeph">FOR NUMBERING</code> for early numbering: <code class="ph codeph">if_abap_behv=&gt;cause-unspecific</code></p>
<p>Locks: <code class="ph codeph">if_abap_behv=&gt;cause-locked</code>, <code class="ph codeph">if_abap_behv=&gt;cause-not_found</code></p>
<p>Read and read-by-association operations: <code class="ph codeph">if_abap_behv=&gt;cause-not_found</code>, <code class="ph codeph">if_abap_behv=&gt;cause-unauthorized</code></p>
<p>Functions: any fail cause, except <code class="ph codeph">if_abap_behv=&gt;cause-locked</code></p>
<p>Feature control and authorization: <code class="ph codeph">if_abap_behv=&gt;cause-not_found</code>; not applicable to global feature control and global authorization</p>
<p>Create, create-by-association, update, delete operations and actions: Any fail cause, except <code class="ph codeph">if_abap_behv=&gt;cause-locked</code></p>
<p>Draft action <code class="ph codeph">resume</code>: Any fail cause, except <code class="ph codeph">if_abap_behv=&gt;cause-locked</code></p>
<p>Validations on save: <code class="ph codeph">if_abap_behv=&gt;cause-unspecific</code></p>
<p>The following contexts are not applicable: Global feature control, global authorization, determination on save and on modify, <code class="ph codeph">cleanup</code> and <code class="ph codeph">map_messages</code> methods.</p>
<p>Otherwise, the runtime error <code class="ph codeph">BEHAVIOR_BAD_HANDLER_RESPONSE</code> is raised.</p></td>
</tr>
<tr class="even">
<td>Entries with non-initial <code class="ph codeph">%state_area</code> components in the <code class="ph codeph">reported</code> response parameter</td>
<td><p><code class="ph codeph">%state_area</code> components must be initial in <code class="ph codeph">reported</code> response parameter entries added in the following handler methods: Read, draft methods defined with <code class="ph codeph">with additional implementation</code>, precheck, augmentation, <code class="ph codeph">adjust_numbers</code>, handler methods with <code class="ph codeph">FOR NUMBERING</code> for early numbering, <code class="ph codeph">save</code>, <code class="ph codeph">save_modified</code>, locks, (global) authorization, (global) feature control; not applicable in <code class="ph codeph">cleanup</code></p>
<p>If the <code class="ph codeph">%state_area</code> component is non-initial, the following components must be initial: <code class="ph codeph">%create</code>, <code class="ph codeph">%update</code>, <code class="ph codeph">%delete</code>, <code class="ph codeph">%action</code>, <code class="ph codeph">%cid</code>, <code class="ph codeph">%global</code>; only <code class="ph codeph">%element</code> (as part of <code class="ph codeph">%op</code>) can be specified in that case.</p>
<p>Otherwise, the runtime error <code class="ph codeph">BEHAVIOR_BAD_HANDLER_RESPONSE</code> is raised.</p></td>
</tr>
<tr class="odd">
<td>Empty update</td>
<td>ABAP EML update requests must include at least one non-key field for each updated data set. <code class="ph codeph">%control</code> must be flagged accordingly, and at least one non-key field must be flagged.</td>
</tr>
<tr class="even">
<td>Duplicates in ABAP EML request</td>
<td>ABAP EML update and delete requests and requests using the <code class="ph codeph">EXECUTE</code> addition must not contain duplicate data sets.</td>
</tr>
<tr class="odd">
<td>RAP save action outside of the corresponding RAP saver method</td>
<td>A <a href="abenrap_save_action_glosry.html">RAP save action</a> can only be executed during the <a href="abenrap_save_seq_glosry.html">RAP save sequence</a> in the corresponding <a href="abenabp_saver_method_glosry.html">RAP saver method</a> implementation. Find more information more info <a href="abenbdl_action_onsave.html">here</a>.</td>
</tr>
<tr class="even">
<td>Using wrong BDEF derived types</td>
<td>ABAP EML operations require specific <a href="abenrap_derived_type_glosry.html">BDEF derived types</a> as operands. For example, update operations expect operands of type <code class="ph codeph">TABLE FOR UPDATE</code>. When using dynamic type specifications, the ABAP compiler cannot validate these types, potentially leading to errors in ABAP EML operation processing.</td>
</tr>
<tr class="odd">
<td>Incomplete key mapping in late numbering scenarios</td>
<td>In <a href="abenrap_late_numbering_glosry.html">RAP late numbering</a> scenarios, the <code class="ph codeph">adjust_numbers</code> <a href="abenabp_saver_method_glosry.html">RAP saver method</a> requires a RAP BO to return the mapping of all temporary keys to their final keys. This allows retrieving the final keys using the <a href="abencommit_entities_beginend_abexa.html"><code class="ph codeph">CONVERT KEY</code></a> statement.</td>
</tr>
</tbody>
</table>

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section [RAP Business Object Contract](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap)

- [Restrictions in Transactional Phases](../../abap-programming-language/abap-database-access/abapinvalid_stmts_in_tx.md)

- ABAP Concepts, topic [Controlled SAP LUW](https://help.sap.com/docs/ABAP_Cloud/f2961be2bd3d403585563277e65d108f/80fe04141e30456c80cc90c5cc838e94?version=sap_cross_product_abap)
