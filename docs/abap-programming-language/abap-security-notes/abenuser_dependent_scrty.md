---
title: "User-Dependent Program Flow"
source_file: abenuser_dependent_scrty.html
section: "ABAP Programming Language > ABAP Security Notes > Further Security Risks"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# User-Dependent Program Flow

Using user names in ABAP programs to control program behavior can be a security risk. In the worst case, a back door can be created and used by developers to access unauthorized data or functions in systems where they do not have authorization. On the other hand, there can also be code sections used for test purposes during development and then be forgotten. Generally speaking, user-dependent source code must be completely avoided and removed. In cases where user-dependent source code is absolutely necessary, a special exemption must be granted for the program so that it can pass the appropriate security tests.

In ABAP, user-dependent program flows can occur in the following instances:

- The [system field](../../abap-glossary/abensystem_field_glosry.md) `sy-uname` is queried in logical expressions. This is a security risk and should never occur (with the exception of a few predefined user names).

- A user name is specified using the addition `USER` of the statement [`AUTHORITY-CHECK`](../abap-authorizations/abapauthority-check.md). This addition can be misused to bypass an authorization check by specifying a user with extensive authorizations.

`sy-uname` is usually redundant when specified explicitly after the addition `USER` and carries the risk of the content being manipulated in advance, for example in the ABAP Debugger.

User names passed to the program from the outside should never be used. If this does become necessary, however, the names must be checked carefully.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following program section demonstrates a back door where an authorization check for a user is ignored intentionally. The program must be repaired by removing the `IF` control block with the `sy-uname` query.

``` abap
AUTHORITY-CHECK OBJECT 'S_DEVELOP' 
   ID 'DEVCLASS' FIELD '...' 
   ID 'OBJTYPE'  DUMMY 
   ID 'OBJNAME'  DUMMY 
   ID 'P_GROUP'  DUMMY 
   ID 'ACTVT'    FIELD '02'. 
IF sy-subrc <> 0. 
  IF sy-uname <> '...'. 
    RETURN. 
  ENDIF. 
ENDIF.
```
