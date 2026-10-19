---
title: "ABAP CDS - CDS Scalar Function Implementation Reference"
source_file: abencds_scalar_func_impl_ref.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Function Definitions > ABAP CDS - Scalar Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - CDS Scalar Function Implementation Reference

A [CDS scalar function implementation reference](../../abap-glossary/abencds_dsfi_glosry.md) is a [CDS object](../../abap-glossary/abencds_object_glosry.md) defined in a form-based tool in [ABAP Development Tool (ADT)](../../abap-glossary/abenadt_glosry.md) that binds a [CDS scalar function](../../abap-glossary/abencds_scalar_function_glosry.md) to an implementation in a specific runtime environment. A scalar function can have multiple scalar function implementation references, but not more than one per runtime environment.

The name of a scalar function implementation reference must be identical to the name of the scalar function definition and have a suffix that matches its implementation type. The suffix `_SQL` is mandatory for the implementation type *SQL* and the suffix `_ANA` is mandatory for the implementation type *Analytical*.

The following types of scalar function implementation references are currently available:

- Analytical

  - Binds the CDS scalar function in question to an analytical runtime environment, such as the [ABAP Analytical Engine](../../abap-glossary/abenabap_ae_glosry.md).

  - The name of the scalar function implementation reference must have the suffix `_ANA`.

  - [Analytical scalar functions](../../abap-glossary/abencds_ana_scalar_glosry.md) can only be defined internally at SAP. Customers can use the SAP-delivered [analytical scalar functions](../../abap-glossary/abencds_ana_scalar_glosry.md). For a complete list of SAP-delivered analytical scalar functions, see [ABAP CDS - Analytical Scalar Functions](abencds_ana_scalar_function.md).

- SQL

  - Binds the CDS scalar function in question to an SQL environment.

  - The name of the scalar function implementation must have the suffix `_SQL`.

  - [SQL-based scalar functions](../../abap-glossary/abencds_sql_scalar_glosry.md) require an [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md). This AMDP function implementation is also specified in the scalar function implementation reference in the following format: `ClassName`=\>`MethodName`.

## More Information

For details on how to create scalar function implementation references, see [*Creating a CDS Scalar Function Implementation Reference*](https://help.sap.com/docs/ABAP_Cloud/c22b59d4c9314104b4a448f3d30ee2e3/aa72593b4a3a4f5386c70e07ec26674b?version=sap_cross_product_abap) in the ABAP CDS Development Tools user guide on SAP Help Portal.
