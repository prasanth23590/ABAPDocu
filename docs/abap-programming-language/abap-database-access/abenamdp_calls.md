---
title: "AMDP - Use"
source_file: abenamdp_calls.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Use

AMDP methods can be used in ABAP programs as follows:

- [AMDP procedure implementations](abenamdp_procedure_methods.md)

  An AMDP procedure implementation is called from an ABAP program in the same way as any other ABAP Objects method.

- [AMDP function implementations](abenamdp_function_methods.md)

  - An AMDP function implementation for an [AMDP scalar function](../../abap-glossary/abenamdp_scalar_function_glosry.md) is called in an ABAP program in the same way as any regular [functional method](../../abap-glossary/abenfunctional_method_glosry.md).

  - In an ABAP program, an AMDP function implementation for an [AMDP table function](../../abap-glossary/abenamdp_table_function_glosry.md) is used by accessing an assigned [CDS table function](../../abap-glossary/abencds_table_function_glosry.md) in an ABAP SQL read statement.

    A prerequisite is that the [standard database](../../abap-glossary/abenstandard_db_glosry.md) of the current AS ABAP is managed by the database system for which the AMDP method is implemented. If not, a runtime error is produced.

Before the method is used for the first time, the ABAP runtime framework creates the procedure or function implemented in the AMDP method in the database system of the standard AS ABAP database or, if necessary, updates any existing database procedure or database function. Execution takes place in the database system and the interface parameters are passed to the database system or adopted by the database system itself.

Once a database procedure or database function managed using AMDP has been created on the database, this procedure can be used in other database procedures or database functions using the database syntax if the database allows this type of access. The calls can take place from other AMDP procedures or AMDP functions and also database procedures or database functions not managed by AMDP. If an AMDP procedure or function uses a different AMDP procedure or function, this procedure must be specified after the addition [`USING`](abapmethod_by_db_proc.md) of the calling method.

## Hints

- For the caller of an AMDP procedure implementation from ABAP, it is usually transparent whether the method is an AMDP method and in which database system it is executed. For this reason, the implementation of the method must ensure that the interface parameters are returned in a format expected by the caller. This applies in particular to ABAP types for which there is no equivalent type in the type system of the database system. These types must either not be offered in the interface or an appropriate casting must take place in the procedure.

- Generally, the database procedures and database functions managed using AMDP are called using AMDP methods from ABAP or in ABAP SQL.

- It is recommended that AMDP procedure implementations that are not intended to be called from the AMDP methods of other classes are created as private methods of an AMDP class and that they are called in a regular method depending on the standard AS ABAP database.
