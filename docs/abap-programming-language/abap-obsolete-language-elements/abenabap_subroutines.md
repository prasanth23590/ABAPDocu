---
title: "Subroutines"
source_file: abenabap_subroutines.html
section: "ABAP Programming Language > ABAP - Obsolete Language Elements > Obsolete Modularization"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Subroutines

***This concept is only supported temporarily in the current ABAP language version and must be replaced with a valid concept for that version.***

Before the introduction of ABAP Objects, subroutines were mainly used for the local modularization of an ABAP program, however, they can also be called externally. Their functions are implemented between the statements [`FORM`](abapform.md) and [`ENDFORM`](abapendform.md). A subroutine is declared immediately when implemented.

Subroutines should no longer be created in new programs for the following reasons:

- The parameter interface has clear weaknesses when compared with the parameter interface of methods, such as:

  - [Positional parameters](../../abap-glossary/abenpositional_parameter_glosry.md) instead of [keyword parameters](../../abap-glossary/abenkeyword_parameter_glosry.md)

  - No real input parameters in pass by reference

  - Typing is only optional

  - No optional parameters

- Every subroutine belongs implicitly to the public interface of its program, which is generally not desired.

- Calling subroutines externally is critical with respect to the assignment of the compilation unit to a [program group](../../abap-glossary/abenprogram_group_glosry.md) in the [internal session](../../abap-glossary/abeninternal_session_glosry.md). This assignment cannot generally be defined statically.

In those places where subroutines cannot yet be replaced by methods (`PERFORM ON COMMIT|ROLLBACK`, `GENERATE SUBROUTINE POOL`), they should be used purely as wrappers for method calls and must not contain any other functional code.
