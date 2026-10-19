---
title: "CLASS-METHODS, FOR SCALAR FUNCTION"
source_file: abapclass-methods_for_scalfunc.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS-METHODS, FOR SCALAR FUNCTION

## Syntax

``` abap
CLASS-METHODS meth FOR SCALAR FUNCTION cds_scalar_func.  
```

## Description

This statement declares the [static method](../../abap-glossary/abenstatic_method_glosry.md) `meth` as an [AMDP function implementation](../../abap-glossary/abencds_table_function_glosry.md) that implements a CDS scalar function `cds_scalar_func` as an [AMDP scalar function](../../abap-glossary/abenamdp_scalar_function_glosry.md). This statement can only be specified in the [public](../../abap-glossary/abenpublic_glosry.md) [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) of an [AMDP class](abenamdp_classes.md) and not in an interface. The method must be implemented using the addition [`BY DATABASE FUNCTION`](abapmethod_by_db_proc.md) of the statement `METHOD`.

`cds_scalar_func` expects a [CDS scalar function](../../abap-glossary/abencds_scalar_function_glosry.md) defined using the statement [`DEFINE SCALAR FUNCTION`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_scalar_function.md) in the [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). This function must have a [CDS scalar function implementation reference](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_scalar_func_impl_ref.md) of type *SQL* and the current class as well as the method `meth` must be specified in the field `AMDP Reference` of the [CDS scalar function implementation reference](../../abap-glossary/abencds_dsfi_glosry.md).

No other additions are possible. The interface parameters of the AMDP function implementation are derived from the [CDS scalar function definition](../../abap-glossary/abencds_dsfd_glosry.md) as follows:

- The input parameters of the CDS scalar function are generated as mandatory input parameters of the AMDP function implementation. The names are copied, and the ABAP types are derived from the specified types.

- The return value of the CDS scalar function is generated as return value. It has the data type specified in the CDS scalar function definition. The name of this return variable is `result`. This name is not part of the method signature.

Client-handling has not yet been implemented for CDS scalar functions and therefore, only client-independent objects can be accessed in the AMDP method that implements the scalar function.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

For an example for the definition, implementation, and use of a CDS scalar function, see the topic [CDS DDL - `DEFINE SCALAR FUNCTION`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_scalar_function.md).
