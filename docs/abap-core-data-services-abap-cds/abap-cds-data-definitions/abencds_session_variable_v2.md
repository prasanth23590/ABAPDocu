---
title: "CDS DDL - CDS View Entity, session_variable"
source_file: abencds_session_variable_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Elementary CDS Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, session_variable

## Syntax

``` abap
... $session.vname ...  
```

## Description

Specifies a [session variable](../../abap-glossary/abensession_variable_glosry.md) `vname` in an operand position in a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). The variable must be prefixed by `$session.`. The prefix and the variable are case-sensitive. `$session.vname`, `$Session.Vname`, and `$SESSION.VNAME` can all be used. No other spellings are allowed.

There are two types of session variables available:

- [Built-in session variables](abencds_session_var_builtin_v2.md): Built-in session variables are set to their value when a CDS view entity is used in ABAP SQL. They cannot be set or changed from ABAP programs. The following built-in session variables are currently available: `user`, `client`, `system_language`, `system_date`, `user_timezone`, `user_date`.

- [Application session variables](abencds_session_var_application_v2.md): Application session variables are required for specific applications and they are set by dedicated system programs. The following application session variables are currently available: `bs_instance_id`, `bs_zone_id`.

## Hint

From a technical perspective, session variables indicate global variables of the current database and can be compared to [ABAP system fields](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md). Although application session variables can be changed from ABAP programs, outside of system programs they should only be used for reads.
