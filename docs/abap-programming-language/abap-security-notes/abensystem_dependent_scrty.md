---
title: "System-Dependent Program Flow"
source_file: abensystem_dependent_scrty.html
section: "ABAP Programming Language > ABAP Security Notes > Further Security Risks"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# System-Dependent Program Flow

The use of the following [system fields](../../abap-glossary/abensystem_field_glosry.md) in ABAP programs to control program behavior can be a security risk:

- `sy-host`

- `sy-sysid`

- `sy-mandt`

As a [user-specific program flow](abenuser_dependent_scrty.md), it may in the worst case constitute a real back door that can be used by developers to access unauthorized data or functions in systems where they do not have authorization. On the other hand, these can also be code sections used for test purposes during development and then forgotten. Generally speaking, source code that depends on the above system fields should always be avoided and removed. Instead, suitable APIs or fully separate implementations should be used. In cases where the use of the above system fields in logical expressions is absolutely necessary, a special exemption must be granted for the program, so that it can pass the appropriate security tests.

It is possible to define additional system fields, for which this check is performed, by implementing [BAdI](../../abap-glossary/abenbadi_glosry.md) `SLIN_BADI_SEC_BACKDOOR`.
