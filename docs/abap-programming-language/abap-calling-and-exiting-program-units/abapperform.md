---
title: "PERFORM"
source_file: abapperform.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# PERFORM

## Deprecated Syntax

**[General Subroutine Call](abapperform_general.md)**

1\. PERFORM [`subr_identifier`](abapperform_form.md) \[[`parameter_list`](abapperform_parameters.md)\].

**Registration of Subroutines**

2\. PERFORM subr ON { {COMMIT \[LEVEL idx\]} \| {ROLLBACK} }.

**Caution**

***This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.***

### Description

Calls [subroutines](../../abap-glossary/abensubroutine_glosry.md).

Subroutines can be called statically and dynamically, internally and externally. Parameters can only be passed if they are called statically.

### Hint

Subroutines are obsolete. No new subroutines should be created in new programs. Methods should be used instead. Subroutines that have been created in existing programs for internal modularization can continue to be called. Whenever possible, however, external subroutine calls from other programs should be avoided.
