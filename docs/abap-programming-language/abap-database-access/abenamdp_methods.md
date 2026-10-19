---
title: "AMDP - Methods"
source_file: abenamdp_methods.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Methods

There are two types of AMDP methods, methods without a return value that define [AMDP procedures](../../abap-glossary/abenamdp_procedure_glosry.md) and methods with a return value that define [AMDP functions](../../abap-glossary/abenamdp_function_glosry.md).

- [AMDP procedure implementations](abenamdp_procedure_methods.md)

- [AMDP function implementations](abenamdp_function_methods.md)

In AMDP classes, AMDP methods are flagged as follows:

- In AMDP procedure implementations and AMDP function implementations that do not implement any [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md) or [CDS scalar functions](../../abap-glossary/abencds_table_function_glosry.md), flagging is not necessary in the declaration with [`METHODS`](../abap-declarations/abapmethods.md) or [`CLASS-METHODS`](../abap-declarations/abapclass-methods.md). However, an optional addition [`AMDP OPTIONS`](abapmethods_amdp_options.md) can be used to declare properties of the AMDP method.

- An AMDP procedure implementation can be exposed to external SQL access using an [SQL service](../../abap-glossary/abenabap_sql_services_glosry.md) and using the addition [`FOR SQL SERVICE`](abapclass-methods_for_sql_service.md).

- AMDP function implementations that implement [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md) must be declared as static methods using `CLASS-METHODS`, and linked with the associated CDS table function using the addition [`FOR TABLE FUNCTION`](abapclass-methods_for_tabfunc.md).

- AMDP function implementations that implement [CDS scalar functions](../../abap-glossary/abencds_scalar_function_glosry.md) must be declared as static methods using `CLASS-METHODS`, and linked with the associated CDS scalar function using the addition [`FOR SCALAR FUNCTION`](abapclass-methods_for_scalfunc.md).

- When implemented, all AMDP methods must be flagged using the statement `METHOD`.

  - AMDP procedure implementations with the addition [`BY DATABASE PROCEDURE`](abapmethod_by_db_proc.md)

  - AMDP function implementations with the addition [`BY DATABASE FUNCTION`](abapmethod_by_db_proc.md)

The implementation of an AMDP method is stored in the [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md) by the ABAP runtime framework. In an AMDP method, it is possible to access objects in the same database schema directly. The name of the current database schema need not and must not be specified here. If the correct authorization is granted, it is possible to access objects in a different database schema by specifying its name.

## Hint

[Constructors](../../abap-glossary/abenconstructor_glosry.md) cannot be implemented as AMDP methods.
