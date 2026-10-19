---
title: "CALL FUNCTION, IN REMOTE SESSION"
source_file: abapcall_function_remote_session.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > CALL FUNCTION > CALL FUNCTION, RFC"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CALL FUNCTION, IN REMOTE SESSION

## Syntax

``` abap
CALL FUNCTION func IN REMOTE SESSION session parameter_list.  
```

[`parameter_list`](abapcall_function_remote_para.md)

## Description

Synchronous call (sRFC). The addition `IN REMOTE SESSION` is used to specify the remote session in `session`.

`func` expects character-like data objects. The calling program is continued after the `CALL FUNCTION` statement when the remotely called function has finished. A remote session may call the same system or another system.

The remote session object `session` can be created using a communication target object. A communication target object is a development object that can be created using the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md). A class for the communication target is generated with the same name.

Communication targets represent targets of remote function calls. Using communication targets, the following should be considered:

- For different scenarios, different communication targets should be used.

- Only calls belonging to the same logon user should be made using the same communication target.

- If calls have different security requirements, multiple communication targets must be used.

Two different types of remote sessions can be created using the following communication target instance methods:

- `GET_TRANSIENT_SESSION`

  Using `GET_TRANSIENT_SESSION`, a transient session is created for every call. Every call opens a new [ABAP session](../../abap-glossary/abenabap_session_glosry.md), which is closed after executing the function module. There is no relation between two successive calls. Depending on the application destination settings, the sessions may be established on the same server or any other server of the same system defined in the application destination. For performance reasons, connections might be reused, or new connections might be established automatically and transparently for the caller.

- `CREATE_SESSION`

  Using `CREATE_SESSION`, a stateful remote session is created. Every call using the same session object will result in a call with the same remote session. [Session variables](../../abap-glossary/abensession_variable_glosry.md) and objects are shared and stored in [session memory](../../abap-glossary/abenroll_area_glosry.md) between subsequent calls. The remote session lives as long as the session is not closed by an explicit close call, an error, or the end of the client session. The option `AUTO_REOPEN` can be set to reopen a closed session automatically. This option should only be used when a remote session can handle a session restart, for example, by recreating caches and reloading necessary data.

**More Information**

- For more information about sRFC, refer to the documentation [RFC](https://help.sap.com/docs/ABAP_PLATFORM_NEW/753088fc00704d0a80e7fbd6803c8adb/4888068AD9134076E10000000A42189D) in the SAP Help Portal.

- For more information about the technical terms used here, the communication arrangement, communication target, and the application destination, refer to the documentation [Integration and Connectivity](https://help.sap.com/docs/ABAP_Cloud/eede1416d18c436e8810eaaeb20c38ae/7f07b344bc7a4e8b9ca748c00e379e74) in the SAP Help Portal.

## Hints

- Any self-created application-specific communication targets must be configured by an administrator using a [communication arrangement](https://help.sap.com/docs/ABAP_Cloud/eede1416d18c436e8810eaaeb20c38ae/85a7d0a1ba144a8fa1e0729edd749c96?version=sap_cross_product_abap) or an [application destination](https://help.sap.com/docs/ABAP_Cloud/eede1416d18c436e8810eaaeb20c38ae/f122d1e4026d4925b71319fcc514aab3?version=sap_cross_product_abap).

- If a short dump should abort the program, it is recommended not to catch the exception `CX_SY_REMOTE_SESSION_ERROR` and any inherited exceptions. Short dumps written by the RFC runtime provide more details.

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_APPDESTINATION`

- *Cause:* The communication arrangement or the application destination configuration is missing, ambiguous, or has errors.

  *Runtime error:* `UNCAUGHT_EXCEPTION`

`CX_COMMUNICATION_TARGET_ERROR`

- *Cause:* During the communication target instantiation, an error occurred.

  *Runtime error:* `UNCAUGHT_EXCEPTION`

`CX_SY_REMOTE_SESSION_ERROR`

- *Cause:* There is an error or exception on the server side.

`CX_SY_REMOTE_SESSION_APP_FAIL`

- *Cause:* There is an exception in the application.

  *Runtime error:* `REMOTE_SESSION_APP_FAIL`

`CX_SY_REMOTE_SESSION_CLOSED`

- *Cause:* The remote session is already closed.

  *Runtime error:* `REMOTE_SESSION_CLOSED`

`CX_SY_REMOTE_SESSION_COM_FAIL`

- *Cause:* There is an error on the communication layer.

  *Runtime error:* `REMOTE_SESSION_COM_FAIL`

`CX_SY_REMOTE_SESSION_FAILURE`

- *Cause:* There is an error or short dump on the server side.

  *Runtime error:* `REMOTE_SESSION_FAILURE`
