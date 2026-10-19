---
title: "CL_ABAP_TX"
source_file: abaprap_cl_abap_tx.html
section: "ABAP Programming Language > ABAP - Database Access > Data Consistency > SAP LUW > Controlled SAP LUW"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_TX

The [static methods](../../abap-glossary/abenstatic_method_glosry.md) of the `CL_ABAP_TX` class can be used to explicitly activate [transactional phases](../../abap-glossary/abentr_phase_glosry.md), thereby controlling the status of the runtime environment and enabling transactional consistency checks with the [controlled SAP LUW](../../abap-glossary/abencontrolled_sap_luw_glosry.md).

The following methods are available:

- `MODIFY`:

  - Activates the *modify* transactional phase.

  - Once the *modify* phase is activated, you can switch to the *save* phase by explicitly activating it.

- `SAVE`:

  - Activates the *save* transactional phase.

  - Once the *save* phase is activated, you cannot switch to the *modify* phase by explicitly activating it.

  - When the [transaction owner](../../abap-glossary/abentransaction_owner_glosry.md) calls the method, the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) is triggered, but without a final commit even if changes to a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) have been performed.

## Hints

- The scope of the *save* transactional phase extends to the end of the [internal session](../../abap-glossary/abeninternal_session_glosry.md). Other than ending the internal session, there is no way to reset the transactional phase.

- The controlled SAP LUW is implicitly supported by [RAP](../../abap-glossary/abenarap_glosry.md). [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md) and [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) implicitly have a transactional contract assigned which is checked for violations of transactional consistency. Therefore, the explicit activation of the transactional phases is usually not needed.

- The transactional phases are implicitly set when [RAP business events](../../abap-glossary/abenrap_entity_event_glosry.md) are consumed locally. This means that [RAP event handler methods](../../abap-glossary/abenrap_event_handler_meth_glosry.md) are started in the *modify* phase when called. If you want to implement database modifications in [RAP event handler method](../../abap-glossary/abenrap_event_handler_meth_glosry.md) implementations, you must explicitly activate the *save* phase to avoid causing errors detected by the controlled SAP LUW.

- The methods can be used to check against [classified APIs](../../abap-glossary/abenclassified_api_glosry.md)

- When a [transactional phase](../../abap-glossary/abentr_phase_glosry.md) has been explicitly set by methods of the `CL_ABAP_TX` class, the [transaction owner](../../abap-glossary/abentransaction_owner_glosry.md) is allowed to execute a commit or rollback statement. In the contexts of [RAP](../../abap-glossary/abenarap_glosry.md) (that is, where RAP is the transaction owner, for example, in [handler](../../abap-glossary/abenabp_handler_method_glosry.md) and [saver methods](../../abap-glossary/abenabp_saver_method_glosry.md)), local consumption of [RAP business events](../../abap-glossary/abenrap_entity_event_glosry.md), [bgPF](../../abap-glossary/abenbgpf_glosry.md), and [classified APIs](../../abap-glossary/abenclassified_api_glosry.md), commit or rollback statements are not allowed.

- Since calling `cl_abap_tx=>save( ).` starts the *save* transactional phase, note the following aspects:

  - In a RAP transaction, if the transaction owner, such as an ABAP program, starts the *save* phase without a `COMMIT ENTITIES` statement to initiate the RAP save sequence, it is recommended that you include the `cl_abap_tx=>save( ).` call within a `TRY` block to catch `CX_ABAP_BEHV_SAVE_FAILED`.

  - This exception occurs if saving fails during the early or late save phases. Catching `CX_ABAP_BEHV_SAVE_FAILED` gives access to attributes like `FAILED_ENTITIES` and `REPORTED_ENTITIES`, which list entries added to the RAP response parameters. Errors causing entries in the failed response can result from failed RAP BO instance validations in the early save phase.

  - Generally, exceptions must not leave RAP handler methods, except for RAP event handler methods.

- Calling `cl_abap_tx=>save( ).` in RAP event handler implementations

  - When RAP event handlers are called, they start in the *modify* transactional phase. Database changes in transactional scenarios require starting the *save* transactional phase. If you need to modify and save RAP BO instances in RAP event handlers, calling `cl_abap_tx=>save( ).` is necessary. Explicit `COMMIT ENTITIES` statements are typically not allowed in handler methods.

  - By catching `CX_ABAP_BEHV_SAVE_FAILED`, you can prevent short dumps and take actions in RAP handler method implementations such as:

  - It is not recommended that you perform cleanup tasks on the transactional buffer - such as correcting failed RAP BO instances and restarting the save - especially when raising custom exceptions.

  - Instead, consider logging the errors to an application log.

  - You can raise custom exceptions inheriting from `CX_ABAP_BEHV_EVENT_HDLR_ERROR` in the `CATCH` block. You can also optionally wrap the raised `CX_ABAP_BEHV_SAVE_FAILED` exception in the `previous` attribute. The raised exceptions are reported to the event framework. **Note:** If corrective tasks are performed for another save, no persistence occurs due to an implicit rollback when raising the custom exception.

  - Only exceptions inheriting from `CX_ABAP_BEHV_EVENT_HDLR_ERROR` may leave RAP event handler method implementations.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Calling the `MODIFY` and `SAVE` methods:

``` abap
... 
 
cl_abap_tx=>modify( ). 
    "The modify transactional phase is activated. 
    "For example, database modification operations are not allowed. 
... 
 
cl_abap_tx=>save( ). 
    "The save transactional phase is activated. 
    "Unlike above, database modification operations are allowed here. 
...
```

## More Information

- [Restrictions in Transactional Phases](abapinvalid_stmts_in_tx.md)

- ABAP Concepts, topic [Controlled SAP LUW](https://help.sap.com/docs/ABAP_Cloud/f2961be2bd3d403585563277e65d108f/80fe04141e30456c80cc90c5cc838e94?version=sap_cross_product_abap)

- Violations of [transactional contracts](../../abap-glossary/abentransactional_contract_glosry.md) detected by the [controlled SAP LUW](../../abap-glossary/abencontrolled_sap_luw_glosry.md) are viewable in the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md) on the *Feed Reader* tab for each system. You can add the *ABAP Contract Check Violations* feed query. Configuration options are available for the feed, including filtering for objects you are responsible for

## Executable Example

The example [`CL_ABAP_TX` and API Classifications](abencl_abap_tx_abexa.md) demonstrates the explicit setting of transactional phases.
