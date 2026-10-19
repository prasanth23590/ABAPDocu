---
title: "COMMIT ENTITIES"
source_file: abapcommit_entities.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# COMMIT ENTITIES

## Syntax Forms

**[`COMMIT ENTITIES`, Short Form](abapemlcommit_entities_short.md)**

``` abap
1. COMMIT ENTITIES [IN SIMULATION MODE] [RESPONSES response_param]. 
```

**[`COMMIT ENTITIES RESPONSE OF`, Long Form](abapemlcommit_entities_long.md)**

``` abap
2. COMMIT ENTITIES [IN SIMULATION MODE] RESPONSE OF bdef1 response_param 
                                      [RESPONSE OF bdef2 response_param] 
                                      [...].
```

**[`COMMIT ENTITIES RESPONSES`, Dynamic Form](abapemlcommit_entities_dyn.md)**

``` abap
3. COMMIT ENTITIES [IN SIMULATION MODE] RESPONSES OF dyn_tab [response_param]. 
```

**[`COMMIT ENTITIES BEGIN, END`](abapemlcommit_entities_late.md)**

``` abap
4. COMMIT ENTITIES BEGIN [IN SIMULATION MODE] 
                        [{RESPONSE OF ... | RESPONSES OF ... } [response_param]]. 
   [CONVERT KEY OF bdef 
      FROM [TEMPORARY] pre_key 
      TO final_key.] 
 
  COMMIT ENTITIES END.
```

[`response_param`](abapeml_response.md) · [`response_param`](abapeml_response.md) · [`response_param`](abapeml_response.md) · [`response_param`](abapeml_response.md) · [`response_param`](abapeml_response.md)

## Description

Triggers the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) and completes the [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md). All transactional changes in the [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md), that is, [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) created, modified, or deleted within the RAP transaction, are persisted to the database.

At the end of an ABAP session, the saving of changed or created data to the database must be triggered, which is done by `COMMIT ENTITIES` statements. Otherwise, the changes are lost. `COMMIT ENTITIES` terminates RAP transactions. If the RAP transactions include [RAP modify operations](../../abap-glossary/abenrap_modify_operation_glosry.md), i. e. there were ABAP EML `MODIFY` statements before a `COMMIT ENTITIES` statement, an implicit [`COMMIT WORK`](../../abap-programming-language/abap-database-access/abapcommit.md) is triggered after processing the save sequence.

Therefore, all RAP BO instances that are present in the transactional buffer are persisted to the database. However, `COMMIT ENTITIES` follows an all or nothing approach, i. e. either all instances are valid and correct and all can be saved or none can be saved if at least one instance is invalid.

`COMMIT ENTITIES` statements can be used for [RAP modify operations](../../abap-glossary/abenrap_modify_operation_glosry.md) by [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md) to trigger the data persistency but they cannot be used in [ABAP behavior pools](../../abap-glossary/abenbehavior_pool_glosry.md) in ABAP. In case of a natively supported RAP scenario (for example, an SAP Fiori app using [OData](../../abap-glossary/abenodata_glosry.md)), the `COMMIT ENTITIES` call is not to be used since it is performed implicitly and automatically by the [RAP transactional engine](../../abap-glossary/abenrap_transac_engine_glosry.md).

## System Fields

`COMMIT ENTITIES` statements set the system field `sy-subrc`. Note that when using `COMMIT ENTITIES` statements, it is not guaranteed that the implicit `COMMIT WORK` will be carried out successfully. In the event of failures during the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md), the RAP saver method [`cleanup_finalize`](abapsaver_class_cleanup_finalize.md) is called for all involved [RAP business objects](../../abap-glossary/abenrap_bo_glosry.md) to ensure that the transactional buffer is cleared for the current RAP transaction. The RAP save sequence is then terminated without persisting the instances to the database. This is indicated by the value set for the system field `sy-subrc` when executing `COMMIT ENTITIES` statements.

**Note:** The following statements are only valid for `COMMIT ENTITIES` statements terminating RAP transactions that include [RAP modify operations](../../abap-glossary/abenrap_modify_operation_glosry.md).

<table>
<thead>
<tr class="header">
<th><strong><code class="ph codeph">sy-subrc</code></strong></th>
<th><strong>Meaning</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0</td>
<td>The implicit <code class="ph codeph">COMMIT WORK</code> has been carried out successfully if a RAP transaction that is terminated by a <code class="ph codeph">COMMIT ENTITIES</code> statement includes <a href="abenrap_modify_operation_glosry.html">RAP modify operations</a>.</td>
</tr>
<tr class="even">
<td>4</td>
<td>The implicit <code class="ph codeph">COMMIT WORK</code> has not been carried out successfully. An issue occurred in the early phase of the RAP save sequence (involved RAP saver methods: <code class="ph codeph">finalize</code>, <code class="ph codeph">check_before_save</code>). The value 4 for <code class="ph codeph">sy-subrc</code> means that there are responses returned by the <a href="abapeml_response.html"><code class="ph codeph">failed</code></a> parameter because of failures in the RAP save sequence. Transactional changes successfully executed in the <a href="abenrap_int_phase_glosry.html">RAP interaction phase</a> remain in the transactional buffer.</td>
</tr>
<tr class="odd">
<td>8</td>
<td><p>The implicit <code class="ph codeph">COMMIT WORK</code> has not been carried out successfully. An issue occurred in the late phase of the RAP save sequence (involved RAP saver methods: <code class="ph codeph">save</code> or <code class="ph codeph">save_modified</code>).</p>
<p>Such an issue can produce inconsistencies which triggers the clearing of the transactional buffer and a <code class="ph codeph">ROLLBACK WORK</code> internally. A subsequent RAP modify operation can then lead to a runtime error. If the RAP BO consumer is to proceed after an issue in the late phase of the RAP save sequence, an explicit <code class="ph codeph">ROLLBACK ENTITIES</code> is required.</p></td>
</tr>
</tbody>
</table>

The following variants of the `COMMIT ENTITIES` statement are available:

- [`COMMIT ENTITIES`, Short Form](abapemlcommit_entities_short.md)

  The short form of the `COMMIT ENTITIES` statement saves all instances of RAP BOs that are changed within the RAP transaction.

- [`COMMIT ENTITIES`, Long Form](abapemlcommit_entities_long.md)

  The long form of the `COMMIT ENTITIES` statement saves all RAP BO instances that are changed within the RAP transaction and provides responses for individual [RAP BO entities](../../abap-glossary/abenrap_bo_entity_glosry.md).

- [`COMMIT ENTITIES OPERATIONS`, Dynamic Form](abapemlcommit_entities_dyn.md)

  The dynamic form of the `COMMIT ENTITIES` statement allows the root entities for which the commit should be executed to be specified dynamically.

- [`COMMIT ENTITIES BEGIN, END`](abapemlcommit_entities_late.md)

  This form of the `COMMIT ENTITIES` statement is relevant for [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) scenarios.

## Hints

- Using a `COMMIT WORK` statement also triggers the RAP save sequence and saves RAP BO instances from the transactional buffer to the database. However, the use of `COMMIT ENTITIES` statements is preferable in the context of RAP because they offer more features like the retrieval of [responses information](abapeml_response.md) or [key conversion](abapemlcommit_entities_late.md).

- `COMMIT ENTITIES` statements are not allowed in [RAP BO providers](../../abap-glossary/abenrap_bo_provider_glosry.md).

- ABAP EML statements should not be used in loops. Using them can have a performance impact because it can result in multiple single database accesses. There should be only one ABAP EML statement to read the necessary data, and then the data should be modified with an ABAP EML modify request.

- When using `COMMIT ENTITIES` statements, a check of `sy-subrc` should be included to avoid syntax warnings. If responses are retrieved, it is recommended that the response parameter `failed` is checked so as to react accordingly.

- If in the RAP interaction phase only read operations are executed and a `COMMIT ENTITIES` statement is specified, only the [`cleanup`](abensaver_method_cleanup.md) method is called.

- Commits in the context of [RAP projection behavior definitions](../../abap-glossary/abencds_proj_bdef_glosry.md) (or [RAP interface behavior definitions](../../abap-glossary/abencds_interface_bdef_glosry.md)): RAP BO instances that fail to be committed in the RAP save sequence for the [base RAP BO](../../abap-glossary/abenrap_projected_bo_glosry.md) are returned to the [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md). The messages in the `failed` [RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md) are automatically mapped to projections.

## Executable Examples

The following executable examples demonstrate the use of the respective statements.

- [`COMMIT ENTITIES`, Short and Long Form](abencommit_entities_sh_lo_abexa.md)

- [`COMMIT ENTITIES`, Dynamic Form](abeneml_commit_dyn_abexa.md)

- [`COMMIT ENTITIES BEGIN`, `END` with `CONVERT KEY OF`](abencommit_entities_beginend_abexa.md)
