---
title: "Creating Exception Classes"
source_file: abenexception_class_create.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Class-Based Exceptions > Exception Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Creating Exception Classes

Exception classes can be defined globally in the [Class Library](../../abap-glossary/abenclass_library_glosry.md) or locally in a program. The naming conventions for global exception classes prescribe the prefix `CX_` or, in the case of exception classes created in customer systems, `YCX_` or `ZCX_`. There is a set of predefined global exception classes, such as those prefixed with `CX_SY_`, whose exceptions are raised in exception situations in the runtime framework.

All exception classes inherit the following instance methods from `CX_ROOT`:

- `GET_TEXT` and `GET_LONGTEXT` return the [exception text](abenexception_texts.md) (short text and long text) as return values of type `string`. These methods are defined in the interface `IF_MESSAGE` implemented in `CX_ROOT` and can be addressed using the identically named alias name for the class.

- `GET_SOURCE_POSITION` returns the program name, the name of a possible [include program](../../abap-glossary/abeninclude_program_glosry.md), and the line number of the statement that raised the exception.

All exception classes inherit the following instance attributes from `CX_ROOT`:

- `TEXTID` of type `SCX_T100KEY` for a key for the database table `T100` or of the type `SOTR_CONC` for a key for OTR (Online Text Repository) that defines the [exception text](abenexception_texts.md). This is usually set by the constructor and evaluated using `GET_TEXT`.

- `PREVIOUS` of reference type `CX_ROOT`, which can contain a reference to a previous exception. This is usually set by the constructor.

- `IS_RESUMABLE` of type `abap_bool`. For exceptions that are raised with the statement [`RAISE RESUMABLE EXCEPTION`](abapraise_exception_class.md), the attribute is set to the value "*X*" in a [`CATCH`](abapcatch_try.md) block with the addition `BEFORE UNWIND`. Here, it indicates whether the exception can be [resumed](../../abap-glossary/abenresumable_exception_glosry.md), that is, whether it is possible to leave a `CATCH` block with [`RESUME`](abapresume.md). The attribute is not set for a `CATCH` block without the addition `BEFORE UNWIND`. In other `CATCH` blocks, in `CLEANUP` blocks, or after `TRY`, the value of `IS_RESUMABLE` is undefined.

## Hints

- Instances of exception classes are usually created when exceptions are raised but can also be instantiated using [`CREATE OBJECT`](../abap-creating-objects-and-values/abapcreate_object.md).

- The instance constructor of an exception class should not raise any exceptions. However, if an exception is raised in the instance constructor after an exception was raised during instantiation of the exception class, and this exception cannot be handled there, it, or, if propagation was unsuccessful, the exception `CX_SY_NO_HANDLER` replaces the originally raised exception.

- Additional methods and attributes can be defined in exception classes, for example to transport additional information about an error situation to the handler. The custom attributes should be read-only (`READ-ONLY`).
