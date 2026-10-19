---
title: "PERFORM, general"
source_file: abapperform_general.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > PERFORM"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# PERFORM, general

## Deprecated Syntax

``` abap
PERFORM subr_identifier [parameter_list].  
```

[`subr_identifier`](abapperform_form.md) · [`parameter_list`](abapperform_parameters.md)

**Caution**

***This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.***

### Description

This statement calls the subroutine specified with the name [`subr_identifier`](abapperform_form.md) and assigns the actual parameters specified in [`parameter_list`](abapperform_parameters.md) to the formal parameters of the subroutine.

### Hints

- Subroutines are obsolete. No new subroutines should be created in new programs. Subroutines that have been created in existing programs for internal modularization can continue to be called. Whenever possible, however, external subroutine calls from other programs should be avoided.

- For more information about the behavior of class-based exceptions in subroutines, see [Class-Based Exceptions in Procedures](../abap-program-flow-logic/abenexceptions_procedures.md).

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_NO_HANDLER`

- See [Class-Based Exceptions in Procedures](../abap-program-flow-logic/abenexceptions_procedures.md).

  *Runtime error:* `UNCAUGHT_EXCEPTION`

`CX_SY_PROGRAM_NOT_FOUND`

- *Cause:* The specified program was not found.

  *Runtime error:* `LOAD_PROGRAM_NOT_FOUND`

- *Cause:* The specified program cannot exist because the program name is longer than 40 characters.

  *Runtime error:* `PERFORM_PROGRAM_NAME_TOO_LONG`

`CX_SY_DYN_CALL_ILLEGAL_FORM`

- *Cause:* The specified subroutine was not found.

  *Runtime error:* `PERFORM_NOT_FOUND`

- *Cause:* The specified index was too small.

  *Runtime error:* `PERFORM_INDEX_0`

- *Cause:* The specified index was negative.

  *Runtime error:* `PERFORM_INDEX_NEGATIVE`

- *Cause:* The specified index was too large.

  *Runtime error:* `PERFORM_INDEX_TOO_LARGE`

`CX_SY_DYN_CALL_PARAM_MISSING`

- *Cause:* The called `FORM` expects more parameters than were specified.

  *Runtime error:* `PERFORM_PARAMETER_MISSING`

`CX_SY_DYN_CALL_PARAM_NOT_FOUND`

- *Cause:* More parameters were specified than expected by `FORM`.

  *Runtime error:* `PERFORM_TOO_MANY_PARAMETERS`

`CX_SY_DYN_CALL_ILLEGAL_TYPE`

- *Cause:* The addressing offsets do not match in the actual and target structures in parameter passing using the addition `STRUCTURE`.

  *Runtime error:* `PERFORM_BASE_WRONG_ALIGNMENT`

- *Cause:* The deep components contained in the actual and target structures cannot be passed to each other. This error occurs only in parameter passing using `STRUCTURE`.

  *Runtime error:* `PERFORM_CAST_DEEP_MISMATCH`

- *Cause:* A type conflict occurred when passing a generically defined type to the form.

  *Runtime error:* `PERFORM_CONFLICT_GENERIC_TYPE`

- *Cause:* The table type of the actual parameter does not match the table type of the parameter defined in the form.

  *Runtime error:* `PERFORM_CONFLICT_TAB_TYPE`

- *Cause:* The type of the actual parameter does not match the type of parameter defined in the form.

  *Runtime error:* `PERFORM_CONFLICT_TYPE`

- *Cause:* The actual parameter occupies less memory space than the target parameter defined in the form. This error occurs only in parameter passing using `STRUCTURE`.

  *Runtime error:* `PERFORM_PARAMETER_TOO_SHORT`

- *Cause:* The fragment views of the actual and target parameters do not match in parameter passing using the addition `STRUCTURE`.

  *Runtime error:* `PERFORM_CONFLICT_UC_STRUCT`

- *Cause:* When the form is called, an internal table is expected as the actual parameter.

  *Runtime error:* `PERFORM_TABLE_REQUIRED`

- *Cause:* A hashed table was passed to a parameter defined using `TABLES`.

  *Runtime error:* `PERFORM_STD_TAB_REQUIRED`
