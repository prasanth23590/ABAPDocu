---
title: "Insufficient Authorization Checks"
source_file: abenauthority_scrty.html
section: "ABAP Programming Language > ABAP Security Notes > Further Security Risks"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Insufficient Authorization Checks

Adequate authorization checks are an important part of secure ABAP programming. In many statements, an appropriate authorization check is performed implicitly, for example:

- In `CALL TRANSACTION` (with the addition `WITH AUTHORITY-CHECK`) and in `LEAVE TO TRANSACTION`.

- When an authorization group is created for the called program in `SUBMIT`.

- Using the automatic authorization checks in the ABAP file interface.

There are, however, many critical statements where no implicit authorization checks are performed, for example:

- [SQL](../../abap-glossary/abensql_glosry.md) reads performed on database tables

Any places in a program that a user can reach without sufficient authorizations and where no implicit authorization check takes place must be secured explicitly using the statement [`AUTHORITY-CHECK`](../abap-authorizations/abapauthority-check.md) and the result of the check analyzed carefully.

A prerequisite for both implicit and explicit authorization checks is that all components required for the SAP authorization concept, such as [authorizations](../../abap-glossary/abenauthorization_glosry.md), [authorization objects](../../abap-glossary/abenauthorization_object_glosry.md), [authorization objects](../../abap-glossary/abenauthorization_profile_glosry.md), and so on are defined. Care must also be taken to set the [check indicator](../../abap-glossary/abencheck_indicator_glosry.md) correctly, to enable all required checks to take place.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Checks explicitly whether the current user can create temporary programs. This check could be used to secure the ABAP command injections example.

``` abap
AUTHORITY-CHECK OBJECT 'S_DEVELOP' 
  ID 'DEVCLASS' FIELD '$TMP' 
  ID 'OBJTYPE'  FIELD 'PROG' 
  ID 'OBJNAME'  DUMMY 
  ID 'P_GROUP'  DUMMY 
  ID 'ACTVT'    FIELD '02'. 
IF sy-subrc <> 0. 
  LEAVE PROGRAM. 
ENDIF.
```
