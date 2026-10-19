---
title: "Restrictions in RAP Handler and Saver Methods"
source_file: abapinvalid_stmts_in_rap_methods.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Restrictions in RAP Handler and Saver Methods

The following restrictions apply to operations and/or statements in the [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) and [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md). **X** means it is allowed.

**RAP handler methods for ...**

\|**Operation**\|[Augmentation implementations](../rap-behavior-definitions/abenbdl_augment_projection.md)\| [Feature control](../../abap-glossary/abenrap_feature_control_glosry.md)\|[Precheck](../../abap-glossary/abenrap_bo_precheck_glosry.md)\| [Authorization control](../../abap-glossary/abenrap_auth_control_glosry.md)\| [Locking](../../abap-glossary/abenrap_locking_glosry.md)\| [Reading](../../abap-glossary/abenrap_read_operation_glosry.md)\| Create, update and delete\| Determinations `ON MODIFY`\| Determinations `ON SAVE`\|Validations `ON SAVE`\|Functions\| Actions \| \|:---\| \|ABAP EML requests raising events\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|- \| \|ABAP EML read requests\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X \| \|ABAP EML `GET PERMISSIONS`\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X \| \|ABAP EML modify requests\|X (but only with the addition `AUGMENTING`)\|-\|-\|-\|-\|-\|X\|X\|X\|-\|-\|X \| \|ABAP EML [key conversion](abapconvert_key.md)\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|- \| \|ABAP EML `SET LOCKS`\|-\|-\|-\|-\|X\|-\|X\|X\|X\|-\|-\|X \| \|Enqueue locks\|-\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X \| \|[Authorization checks](../../abap-glossary/abenauthorization_check_glosry.md)\|X\|X\|X\|X\|X\|X\|X\|X\|-\|-\|X\|X \| \|Calling function modules for update task and background processing\|-\|-\|- \|-\|- \|-\|-\|-\|-\|-\|-\|- \| \|Database modifications using the standard connection\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|- \| \|ABAP SQL `SELECT` statements\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X \| \| \| \|`COMMIT [WORK \| ENTITIES]`, `ROLLBACK [WORK \| ENTITIES]`\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|- \| \|Explicit database commits\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|- \| \|Implicit database commits\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X \| \|[classified APIs](../../abap-glossary/abenclassified_api_glosry.md) that are classified with `IF_ABAP_TX_SURFACE`\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|- \| \|APIs classified with `IF_ABAP_TX_FUNCTIONAL`\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X \| \|APIs classified with `IF_ABAP_TX_READ`\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X\|X \| \|APIs classified with `IF_ABAP_TX_MODIFY`\|-\|-\|-\|-\|-\|-\|X\|X\|X\|-\|-\|X \| \|APIs classified with `IF_ABAP_TX_SAVE`\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|-\|

**RAP saver methods**

\|**Operation**\|`FINALIZE`\|`CHECK_BEFORE_SAVE`\| `CLEANUP`\|`CLEANUP_FINALIZE`\|`ADJUST_NUMBERS`\|`SAVE`/`SAVE_MODIFIED`\|`MAP_MESSAGES` \| \|:---\| \|ABAP EML requests raising events\|-\|-\|-\|-\|X\|X\|- \| \|ABAP EML read requests\|X\|X\|X\|X\|-/X (1)\|-/X (1)\|X \| \|ABAP EML `GET PERMISSIONS`\|X\|X\|-\|X\|X\|-\|X \| \|ABAP EML modify requests\|X\|-\|-\|X\|-\|-\|- \| \|ABAP EML [key conversion](abapconvert_key.md)\|-\|-\|-\|-\|X\|X\|- \| \|ABAP EML `SET LOCKS`\|X\|-\|-\|-\|-\|-\|- \| \|Enqueue locks\|X\|X\|-\|-\|X\|X\|- \| \|[Authorization checks](../../abap-glossary/abenauthorization_check_glosry.md)\|X (2)\|X (2)\|-\|X (2)\|-\|-\|- \| \|Calling function modules for update task and background processing\|-\|-\|- \|-\|X \|X\|- \| \|Database modifications using the standard connection\|-\|-\|- \|-\|X \|X\|- \| \|ABAP SQL `SELECT` statements\|X\|X\|X\|X\|X\|X\|X \| \| \| \|`COMMIT [WORK \| ENTITIES]`, `ROLLBACK [WORK \| ENTITIES]`\|-\|-\|-\|-\|-\|-\|- \| \|Explicit database commits\|-\|-\|-\|-\|-\|-\|- \| \|Implicit database commits\|X\|X\|X\|X\|-\|-\|- \| \|APIs classified with `IF_ABAP_TX_SURFACE`\|-\|-\|-\|-\|-\|-\|- \| \|APIs classified with `IF_ABAP_TX_FUNCTIONAL`\|X\|X\|X\|X\|X\|X\|X \| \|APIs classified with `IF_ABAP_TX_READ`\|X\|X\|X\|X\|X\|X\|X \| \|APIs classified with `IF_ABAP_TX_MODIFY`\|X\|-\|-\|X\|-\|-\|- \| \|APIs classified with `IF_ABAP_TX_SAVE`\|-\|-\|-\|-\|X\|X\|-\|

**Footnotes:**

1.  ABAP EML read requests are here only allowed in [managed RAP business objects](../../abap-glossary/abenmanaged_rap_bo_glosry.md), i.e. read requests on the [managed transactional buffer](../../abap-glossary/abenmanaged_trans_buff_glosry.md). [`IN LOCAL MODE`](abapin_local_mode.md) must be specified, and it may not be a read operation by a function, only read and read-by-association operations. In general, operations that cause applications to terminate are not allowed.

2.  If at least one ABAP EML modify operation occurred in an unprivileged context, it does not violate the contract as long as the authorization check takes place during the early save phase (handler methods `finalize`, `check_before_save`, `cleanup_finalize`). If all ABAP EML modify operations were performed in a privileged context, the early save phase is expected to execute in privileged context. Refer to the [`GET_PRIVILEGED_ACCESS_PROFILE` method of the `CL_ABAP_BEHV_AUX` class](abaprap_cl_abap_behv_aux.md).

## More Information

- [`CL_ABAP_TX`](../../abap-programming-language/abap-database-access/abaprap_cl_abap_tx.md)

- [API Classifications](../../abap-programming-language/abap-database-access/abapapi_classification.md)

- [Restrictions in Transactional Phases](../../abap-programming-language/abap-database-access/abapinvalid_stmts_in_tx.md)

- ABAP Concepts, topic [Controlled SAP LUW](https://help.sap.com/docs/ABAP_Cloud/f2961be2bd3d403585563277e65d108f/80fe04141e30456c80cc90c5cc838e94?version=sap_cross_product_abap)
