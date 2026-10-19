---
title: "Exception Categories"
source_file: abenexception_categories.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Class-Based Exceptions > Exception Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Exception Categories

Exception classes are subclasses of the following abstract classes:

- `CX_ROOT`

  - `CX_STATIC_CHECK`

  - `CX_DYNAMIC_CHECK`

  - `CX_NO_CHECK`

The assignment to one of the three abstract subclasses of `CX_ROOT` determines the exception category, that is, whether an exception must be declared explicitly in the procedure interface when [propagating from a procedure](abenexceptions_procedures.md), and how the declaration is checked:

- `CX_STATIC_CHECK`

  If exceptions defined using subclasses of `CX_STATIC_CHECK` are propagated from a procedure, they must be explicitly declared in the interface of the procedure. The syntax check statically checks whether all exceptions raised in the procedure using [`RAISE EXCEPTION`](abapraise_exception_class.md) or the addition [`THROW`](abenconditional_expression_result.md) in a [conditional expression](abenconditional_expressions.md), or declared in the interfaces of called procedures are either handled using [`CATCH`](abaptry.md) or declared explicitly in the interface, and produces a warning if this is not the case.

- `CX_DYNAMIC_CHECK`

  If exceptions defined using subclasses of `CX_DYNAMIC_CHECK` are propagated from a procedure, they must be declared explicitly in the interface of the procedure. However, this is not checked statically by the syntax check, but dynamically at that moment when such an exception is propagated from a procedure.

- `CX_NO_CHECK`

  Exceptions that are defined using subclasses of `CX_NO_CHECK` can always be propagated, whereby a possible [resumability](../../abap-glossary/abenresumable_exception_glosry.md) is preserved. It is not necessary to declare exceptions defined using subclasses of `CX_NO_CHECK` in the interface of a procedure. They are declared implicitly, but it is also possible to declare subclasses of `CX_NO_CHECK` explicitly in the interface of a procedure. On the one hand, this can be used to document the possible occurrence of exceptions of this category. On the other hand, this makes it possible to change the category of existing exceptions to `CX_NO_CHECK` without causing errors in interface definitions.

If an exception of category `CX_STATIC_CHECK` or `CX_DYNAMIC_CHECK` is [propagated](abenexceptions_procedures.md) from the procedure but not declared in the interface of the procedure, the interface is violated and an exception of the predefined class `CX_SY_NO_HANDLER` is raised at the call point of the procedure. The exception object of the exception contains a reference to the original exception in the attribute `PREVIOUS`. An exception of category `CX_NO_CHECK` can be propagated independently of its explicit declaration in the procedure interface.

## Hints

- Using Exception Categories

  - Exceptions of the `CX_STATIC_CHECK` category are always justified if the direct caller of a procedure is to be forced to handle the exception or to at least explicitly forward it. However, if an exception can be prevented by prior checks, exceptions of the `CX_DYNAMIC_CHECK` category are preferable. Otherwise untestable dead code can be created because corresponding exception handling is necessary, but it is never processed when the interface is used correctly.

  - If the program logic can eliminate potential error situations, the corresponding exceptions do not have to be handled or declared in the interface. This is the case, for example, if, prior to a division, there is an explicit requirement for the denominator not to equal zero (precondition). In this case, exceptions of the `CX_DYNAMIC_CHECK` category can be used. These exceptions only need to be handled and declared if their occurrence cannot be otherwise prevented.

  - For exception situations that can occur practically at any time or that cannot be handled directly, the `CX_NO_CHECK` category can be used. Otherwise, these exceptions would have to be declared in almost every interface, which would result in more complex programs lacking in clarity.

- Interface violations normally only occur for exceptions of the category `CX_DYNAMIC_CHECK`, since exceptions of the category `CX_STATIC_CHECK` are checked first by the syntax check and exceptions of the category `CX_NO_CHECK` can pass each interface.

- The [resumability](../../abap-glossary/abenresumable_exception_glosry.md) of an exception is not specified as a property of the exception class and is instead defined by the addition `RESUMABLE` of the statement [`RAISE EXCEPTION`](abapraise_exception_class.md) or the addition `THROW` in a [conditional expression](abenconditional_expressions.md) when the exception is raised. This property can be lost for exceptions of type `CX_STATIC_CHECK` and `CX_DYNAMIC_CHECK` during propagation of parameter interfaces of procedures, if they are not also declared there with `RESUMABLE`.
