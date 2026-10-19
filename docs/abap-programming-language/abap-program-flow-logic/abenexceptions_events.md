---
title: "Class-Based Exceptions in Event Handlers"
source_file: abenexceptions_events.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Class-Based Exceptions > System Response After a Class-Based Exception"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Class-Based Exceptions in Event Handlers

Class-based exceptions in [event handlers](../../abap-glossary/abenevent_handler_glosry.md) are a special case of [class-based exceptions in procedures](abenexceptions_procedures.md).

Since event handlers and triggers are completely decoupled from each other, the trigger of an event does not know the handler and therefore cannot handle its exceptions. For this reason, no class-based exceptions can be declared using `RAISING` in the [declaration](../abap-declarations/abapmethods_event_handler.md) of event handlers.

This has the following consequences:

- If exceptions of the classes `CX_STATIC_CHECK` or `CX_DYNAMIC_CHECK` occur during event handling, they must be handled in the event handler or they lead to a violation of the interface, whereby the exception `CX_SY_NO_HANDLER` is raised, as in regular [procedures](abenexceptions_procedures.md).

- If a violation of the interface occurs during event handling, event handling is terminated, and the control is given back to the trigger of the event. Further event handlers which are still registered for the event are not executed.

- The trigger of the event can handle the `CX_SY_NO_HANDLER` exception.

## Hints

- An event handler should handle exceptions of the classes `CX_STATIC_CHECK` and `CX_DYNAMIC_CHECK` that are raised during processing. If they are not handled and this leads to a violation of the interface, it is seen as a programming error in the event handling.

- The trigger of an event does not usually have to handle exceptions, unless an exception to the class `CX_NO_CHECK` is expected. The handling of `CX_SY_NO_HANDLER` is only considered when trying to prevent a possible programming error in an event handler from producing a runtime error.

- The trigger of an event should not attempt, any more than the caller of a procedure, to handle the original exception after detecting `CX_SY_NO_HANDLER`. Unlike in direct method calls, it is not yet determined here which method the event has handled.
