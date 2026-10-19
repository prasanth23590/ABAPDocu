---
title: "Restrictions in Transactional Phases"
source_file: abapinvalid_stmts_in_tx.html
section: "ABAP Programming Language > ABAP - Database Access > Data Consistency > SAP LUW > Controlled SAP LUW"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Restrictions in Transactional Phases

The following restrictions apply to operations and/or statements in the modify and save [transactional phases](../../abap-glossary/abentr_phase_glosry.md). *X* means it is allowed.

<table>
<thead>
<tr class="header">
<th><strong>Operations/Statements</strong></th>
<th><strong>modify phase</strong></th>
<th><strong>save phase</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Database modifications</td>
<td>-</td>
<td>X</td>
<td>Only allowed in the late save phase because the data being processed is always potentially inconsistent. Database changes in other phases would result in multiple database transactions instead of one transaction, which would disrupt the SAP LUW.</td>
</tr>
<tr class="even">
<td><p>Transaction control</p>
<p><code class="ph codeph">COMMIT WORK</code>, <code class="ph codeph">ROLLBACK WORK</code></p></td>
<td>X/-</td>
<td>X/-</td>
<td>When a <a href="abentr_phase_glosry.html">transactional phase</a> has been explicitly set by methods of the <code class="ph codeph">CL_ABAP_TX</code> class, the <a href="abentransaction_owner_glosry.html">transaction owner</a> is allowed to execute a commit or rollback statement. In the contexts of <a href="abenarap_glosry.html">RAP</a> (that is, where RAP is the transaction owner, for example, in <a href="abenabp_handler_method_glosry.html">handler</a> and <a href="abenabp_saver_method_glosry.html">saver methods</a>), local consumption of <a href="abenrap_entity_event_glosry.html">RAP business events</a>, <a href="abenbgpf_glosry.html">bgPF</a>, and <a href="abenclassified_api_glosry.html">classified APIs</a>, commit or rollback statements are not allowed.</td>
</tr>
<tr class="odd">
<td>Raising an exception using <code class="ph codeph">RAISE EXCEPTION</code></td>
<td>-</td>
<td>-</td>
<td>It is not allowed to leave a transaction this way.</td>
</tr>
<tr class="even">
<td>Raising a <a href="abenrap_entity_event_glosry.html">RAP business event</a> using <code class="ph codeph">RAISE ENTITY EVENT</code></td>
<td>-</td>
<td>X</td>
<td>The statements are recommended in the <code class="ph codeph">save</code> and <code class="ph codeph">save_modified</code> <a href="abenabp_saver_method_glosry.html">RAP saver methods</a>.</td>
</tr>
</tbody>
</table>

## Hints

- In a RAP transaction, the modify transactional phase includes the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md) and [RAP early save phase](../../abap-glossary/abenearly_rap_save_phase_glosry.md). The save transactional phase includes the [RAP late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md). In these [RAP transactional phases](../../abap-glossary/abentransactional_phase_glosry.md), the restrictions apply. Find a more detailed overview regarding restrictions applying to operations and/or statements in the [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) and [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md) [here](../../abap-rap-business-objects/abap-for-rap-business-objects/abapinvalid_stmts_in_rap_methods.md).

- [ABAP contract checks](../../abap-glossary/abencontract_checks_glosry.md) violations are made visible in [unit tests](../../abap-glossary/abenunit_test_glosry.md), i.e. the unit tests will fail if a contract check violation occurs.

- Violations of [transactional contracts](../../abap-glossary/abentransactional_contract_glosry.md) detected by the [controlled SAP LUW](../../abap-glossary/abencontrolled_sap_luw_glosry.md) are viewable in the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md) on the *Feed Reader* tab for each system. You can add the *ABAP Contract Check Violations* feed query. Configuration options are available for the feed, including filtering for objects you are responsible for

## More Information

- For general information about data consistency and the SAP LUW, see [here](abendata_consistency.md).

- An integral part of RAP transactions is [database locking](../../abap-glossary/abendatabase_lock_glosry.md). Each RAP BO instance that is processed during a SAP LUW in RAP must be locked to avoid conflicts. See more information in the Development Guide for the ABAP RESTful Application Programming Model, section [Pessimistic Concurrency Control (Locking)](https://help.sap.com/docs/ABAP_PLATFORM_NEW/fc4c71aa50014fd1b43721701471913d/99d8162b8d7d4a83ae65320d2a03b8ab).

- [RAP Save Sequence](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/ab7459048c7e4ecda98d0b6f51b01e7b?version=sap_cross_product_abap) in the Development Guide for the ABAP RESTful Application Programming Model.

- [Restrictions in RAP Handler and Saver Methods](../../abap-rap-business-objects/abap-for-rap-business-objects/abapinvalid_stmts_in_rap_methods.md)

- ABAP Concepts, topic [Controlled SAP LUW](https://help.sap.com/docs/ABAP_Cloud/f2961be2bd3d403585563277e65d108f/80fe04141e30456c80cc90c5cc838e94?version=sap_cross_product_abap)
