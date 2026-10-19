---
title: "ABAP Managed Database Procedures (AMDP)"
source_file: abenamdp.html
section: "ABAP Programming Language > ABAP - Database Access"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Managed Database Procedures (AMDP)

ABAP Managed Database Procedures are a framework for managing and calling

- [stored procedures](../../abap-glossary/abenstored_procedure_glosry.md) or [database procedures](../../abap-glossary/abendatabase_procedure_glosry.md) and

- [database functions](../../abap-glossary/abendatabase_function_glosry.md)

in [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). Accordingly, the ABAP Managed Database Procedures manage

- [AMDP procedures](../../abap-glossary/abenamdp_procedure_glosry.md) and

- [AMDP functions](../../abap-glossary/abenamdp_function_glosry.md)

A procedure or function of this type is implemented in a database-specific language ([SQLScript](../../abap-glossary/abensql_script_glosry.md) ) in an

- [AMDP procedure implementation](../../abap-glossary/abenamdp_procedure_method_glosry.md) or

- [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md)

as an [AMDP method](../../abap-glossary/abenamdp_method_glosry.md) in an [AMDP class](../../abap-glossary/abenamdp_class_glosry.md).

The following sections describe the components of AMDP:

- [AMDP - Classes](abenamdp_classes.md)

- [AMDP - Methods](abenamdp_methods.md)

- [AMDP - Inheritance](abenamdp_inheritance.md)

- [AMDP - Use](abenamdp_calls.md)

- [AMDP - Client Handling](abenamdp_client_handling.md)

- [AMDP - Macros](abenamdp_macros.md)

- [AMDP - Exception Classes](abenamdp_exceptions.md)

- [AMDP - Glossary](abenamdp_glossary.md)

- [AMDP - Examples](abenamdp_examples.md)

Currently, AMDP only supports database procedures and functions from the SAP HANA database. In principle, however, AMDP is designed so that stored procedures and functions from other database systems can also be supported.

Besides the [C1 contract](../../abap-glossary/abenc1_contract_glosry.md), there is a special [release contract](../../abap-glossary/abenrelease_contract_glosry.md) available to classify repository objects as stable public interface for use in AMDP, the [C4 contract](../../abap-glossary/abenc4_contract_glosry.md);

- AMDP methods that are released as APIs using a [C1 contract](../../abap-glossary/abenc1_contract_glosry.md) can be used in ABAP programs.

- AMDP methods that are released as APIs using a [C4 contract](../../abap-glossary/abenc4_contract_glosry.md) can be used in other AMDP methods.

AMDP methods release with a C4 contract must also be released with a C1 contract.

## Hints

- ABAP developers or consumers do not need separate users for the database system to manage and call database procedures and database functions using AMDP. Instead, the AS ABAP logged on to the database system using its work processes requires the correct authorizations to manage database procedures and functions using AMDP. Missing authorizations can be detected using transaction `SICK`.

- [Table buffering](../../abap-glossary/abentable_buffering_glosry.md) is bypassed when using AMDP.
