---
title: "Class-Based Exceptions in Procedures"
source_file: abenexceptions_procedures.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Class-Based Exceptions > System Response After a Class-Based Exception"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Class-Based Exceptions in Procedures

If a class-based exception is not handled in a [procedure](../../abap-glossary/abenprocedure_glosry.md), the system attempts to [propagate](abenexceptions_system_response.md) it to the caller of the procedure. The exceptions that can be propagated from a procedure must be declared in its interface. The caller then knows which exceptions to expect from the procedure. Class-based exceptions are divided into three [categories](abenexception_categories.md), which determine whether the declaration must be explicit and how it is checked.

In methods, the addition `RAISING` of the statements [`METHODS`](../abap-declarations/abapmethods.md) and [`FORM`](../abap-obsolete-language-elements/abapform.md) is used for the declaration. The declaration of an exception class in an interface is polymorphous. It declares all subclasses simultaneously.

Declarations using `RAISING` can be used to determine whether a [resumable exception](../../abap-glossary/abenresumable_exception_glosry.md) that is propagated from a procedure remains resumable or not. It remains resumable only if the addition `RESUMABLE` is specified for every parameter interface it passes when propagated. The addition `RESUMABLE` in `RAISING` does not make a non-resumable exception resumable when it is propagated by an interface.

Undeclared exceptions cannot exit a procedure but can violate the interface if they are not handled within the procedure. A violation of the interface raises an exception of the predefined class `CX_SY_NO_HANDLER`, whose exception object contains a reference to the original exception in the attribute `PREVIOUS`.

When exceptions are propagated from procedures, the following restrictions apply:

- No exceptions can be declared in the definition of a [static constructor](../abap-declarations/abapclass-methods_constructor.md), that is, exceptions cannot leave a static constructor. It is usually not known whether the user of a class is the first user and whether or not this user must handle exceptions propagated by the static constructor.

- No exceptions can be declared in the definition of an [event handler](../../abap-glossary/abenevent_handler_glosry.md), that is, no exceptions can be propagated from an event handler, except those of category `CX_NO_CHECK`. See [Class-Based Exceptions in Event Handlers](abenexceptions_events.md).

Programs called using `SUBMIT ... AND RETURN` or `CALL TRANSACTION` cannot propagate any exceptions to the caller, since exception objects are bound to the [internal session](../../abap-glossary/abeninternal_session_glosry.md) of a program.

## Hints

- When an exception of type `CX_SY_NO_HANDLER` is raised, this indicates a programming error within a procedure, where the programmer forgot to prevent an exception of category `CX_DYNAMIC_CHECK` or `CX_STATIC_CHECK`, handle it locally, or declare it. When exceptions of type `CX_SY_NO_HANDLER` are handled, it is therefore best not to try to handle the original exception but inform the person responsible for the program instead. In the case of exceptions of type `CX_STATIC_CHECK`, the syntax check also reports this.

- If the exception `CX_SY_NO_HANDLER` is not handled after the interface is violated, the runtime error is raised by the original exception and the associated [short dump](../../abap-glossary/abenshort_dump_glosry.md) describes it. This indicates that primarily the original exception is to be stopped, handled, or declared by the procedure. The short dump should not cause the exception `CX_SY_NO_HANDLER` to be handled instead.
