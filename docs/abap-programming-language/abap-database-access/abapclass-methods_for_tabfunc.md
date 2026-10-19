---
title: "CLASS-METHODS, FOR TABLE FUNCTION"
source_file: abapclass-methods_for_tabfunc.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS-METHODS, FOR TABLE FUNCTION

## Syntax

``` abap
CLASS-METHODS meth FOR TABLE FUNCTION cds_tabfunc.  
```

## Description

This statement declares the [static method](../../abap-glossary/abenstatic_method_glosry.md) `meth` as an [AMDP function implementation](../../abap-glossary/abencds_table_function_glosry.md) that implements a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md) `cds_tabfunc` as an [AMDP table function](../../abap-glossary/abenamdp_table_function_glosry.md). This statement can only be specified in the [public](../../abap-glossary/abenpublic_glosry.md) [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) of an [AMDP class](abenamdp_classes.md) and not in an interface. The method must be implemented using the addition [`BY DATABASE FUNCTION`](abapmethod_by_db_proc.md) of the statement `METHOD`.

`cds_tabfunc` expects a CDS table function defined using the statement [`DEFINE TABLE FUNCTION`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_define_table_function.md) in the [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). This CDS entity must refer to the current class and the method `meth` after the addition `IMPLEMENTED BY METHOD`.

No other additions are possible. The interface parameters in the AMDP function implementation are added to the CDS table function as follows:

- Mandatory input parameters of the AMDP function implementation are generated from the [input parameters](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_func_parameter_list.md) of the CDS table function. The names are copied, and the ABAP types are derived from the dictionary types.

- A return value of the type of a standard table with an empty table key with the name `result` with a structured row type is generated from the [elements](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_return_list.md) of the CDS table function. The names of the components of the row type correspond to the names of the elements and the data types are derived from their dictionary types.

## Hint

The client handling of an AMDP method that implements a CDS table function is governed by the [client handling](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_handling.md) of the table function. Refer to [Client Handling/`USING` Matrices](abenamdp_call_matrices.md).
