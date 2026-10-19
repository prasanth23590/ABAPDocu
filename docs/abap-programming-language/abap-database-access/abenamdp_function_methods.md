---
title: "AMDP - Function Implementations"
source_file: abenamdp_function_methods.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Function Implementations

An AMDP function implementation is an AMDP method for implementing an [AMDP function](../../abap-glossary/abenamdp_function_glosry.md) as a [database function](../../abap-glossary/abendatabase_function_glosry.md). An AMDP function implementation is indicated as an AMDP method in the implementation part of the class using the addition [`BY DATABASE FUNCTION`](abapmethod_by_db_proc.md) of the statement `METHOD`. [AMDP table functions](../../abap-glossary/abenamdp_table_function_glosry.md) and [AMDP scalar functions](../../abap-glossary/abenamdp_scalar_function_glosry.md) can be implemented.

- [AMDP Table Functions](abenamdp_function_methods.md#amdp-table-functions)

  - [AMDP Table Functions for AMDP Methods](abenamdp_function_methods.md#amdp-table-functions-for-amdp-methods)

  - [AMDP Table Functions for CDS Table Functions](abenamdp_function_methods.md#amdp-table-functions-for-cds-table-functions)

- [AMDP Scalar Functions](abenamdp_function_methods.md#amdp-scalar-functions)

  - [AMDP Scalar Functions for AMDP Methods](abenamdp_function_methods.md#amdp-scalar-functions-for-amdp-methods)

  - [AMDP Scalar Functions for CDS Scalar Functions](abenamdp_function_methods.md#amdp-scalar-functions-for-cds-scalar-functions)

## AMDP Table Functions

There are the following types of AMDP table functions:

- Functions that can only be accessed in other AMDP methods

- Functions that implement [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md) that can be accessed in ABAP SQL

### AMDP Table Functions for AMDP Methods

An AMDP function implementation for an AMDP table function that can only be accessed in AMDP methods is declared in an [AMDP](abenamdp_classes.md) class like a regular [static method](../../abap-glossary/abenstatic_method_glosry.md) or [instance method](../../abap-glossary/abeninstance_method_glosry.md) in any [visibility section](../../abap-glossary/abenvisibility_section_glosry.md). An AMDP function implementation like this cannot be identified in the declaration part of the class and the same basically applies as to [AMDP procedure implementations](abenamdp_procedure_methods.md) with the following differences:

- The AMDP function implementation must have a [return value](../../abap-glossary/abenreturn_value_glosry.md) defined using [`RETURNING`](../abap-declarations/abapmethods_functional.md). The data type of the return value must be tabular with a structured row type whose components are elementary. Any [table category](../../abap-glossary/abentable_category_glosry.md) and [table key](../../abap-glossary/abentable_key_glosry.md) can be specified for return value.

- In addition to the return value, the AMDP function implementation can have elementary and tabular [input parameters](../../abap-glossary/abeninput_parameter_glosry.md), but no [input/output parameters](../../abap-glossary/abeninput_output_parameter_glosry.md) or [output parameters](../../abap-glossary/abenoutput_parameter_glosry.md). The special input parameter `connection` is not allowed.

- No class-based exceptions can be declared using [`RAISING`](../abap-declarations/abapmethods_general.md) in the interface of the AMDP function implementation.

- The AMDP function implementation cannot be [called](../abap-calling-and-exiting-program-units/abenmethod_calls.md) in ABAP like a regular method and cannot be used as a [functional method](../../abap-glossary/abenfunctional_method_glosry.md) in a [functional method call](../../abap-glossary/abenfunctional_method_call_glosry.md).

The AMDP table function of a [AMDP table function](../../abap-glossary/abenamdp_table_function_glosry.md) can be called from other AMDP methods. It cannot be called in ABAP programs like a regular functional method.

### Hints

- Calls from ABAP programs are not possible since the result set cannot be restricted using a `WHERE` condition.

### Executable Example

AMDP functions

### AMDP Table Functions for CDS Table Functions

The same rules apply to an AMDP function implementation that implements an [CDS table function](../../abap-glossary/abencds_table_function_glosry.md) as to the AMDP table functions for AMDP methods (described above), with the following differences:

- An AMDP function implementation for a CDS table function can only be declared in the public [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) of a [static](../../abap-glossary/abenstatic_class_glosry.md) AMDP class. It is not possible in interfaces.

- A special form of the statement [`CLASS-METHODS`](../abap-declarations/abapclass-methods.md) with the addition [`FOR TABLE FUNCTION`](abapclass-methods_for_tabfunc.md) must be used for the declaration. This addition flags the [AMDP](../../abap-glossary/abencds_table_function_glosry.md) function implementation as an implementation of a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md).

- The parameter interface of the AMDP function implementation is not declared using the statement `CLASS-METHODS`. Instead it is generated in accordance with the associated [CDS table function](../../abap-glossary/abencds_table_function_glosry.md) using the statement [`DEFINE TABLE FUNCTION`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_define_table_function.md) in the [ABAP CDS](../../abap-glossary/abencds_ddl_glosry.md) [CDS DDL](../../abap-glossary/abenabap_cds_glosry.md):

  - The input parameters in the AMDP function implementation are determined by the [input parameters](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_func_parameter_list.md) of the CDS table function. Their names are used, and the ABAP types are derived from their Dictionary types. The input parameters are always elementary and not optional.

  - A return value with the type of a standard table is created with an empty table key named `result` with a structured row type. The components of the row type are determined by the [elements](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_return_list.md) of the CDS table function. Their names are used, and the ABAP types are derived from their dictionary types. The row type corresponds to the structured data type represented by the CDS table function. In the case of a client-dependent CDS table function, the client column is also included.

The [AMDP table function](../../abap-glossary/abenamdp_table_function_glosry.md) defined by an AMDP function implementation like this can be used as follows using the [CDS entity](../../abap-glossary/abencds_entity_glosry.md) represented by the CDS table function:

- as a [data source](abapselect_data_source.md) of ABAP SQL read statements in ABAP.

- as a [data source](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_data_source_v2.md) of [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) of [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md).

- as a [data source](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_data_source_v1.md) of [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) of [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md).

In addition, calls from other AMDP methods are possible. Calls as regular functional methods are not possible in an ABAP program.

### Hints

- The row type of the return value `result` of an AMDP function implementation for a client-dependent CDS table function does not contain a client field, even though this field must be declared in the element list.

- An AMDP function implementation can only be linked with a single CDS table function.

- When an AMDP function implementation is created for a CDS table function, the CDS table function must already exist as an active function. When a new CDS table function is activated, an empty AMDP table function is created in the database. This function raises an exception if a non-AMDP access is performed. When the CDS table function is accessed by the ABAP runtime framework for the first time (for example, using ABAP SQL), the AMDP function implementation implements the empty AMDP table function. Other frameworks that evaluate CDS entities using their [annotations](../../abap-glossary/abencds_annotation_glosry.md), however, can also cause the AMDP table function to be implemented. It is possible to access the table function in a native way only after the implementation.

### Executable Example

AMDP functions

## AMDP Scalar Functions

There are the following types of AMDP scalar functions:

- Functions that can only be accessed in other AMDP methods.

- Functions that implement [CDS scalar functions](../../abap-glossary/abencds_scalar_function_glosry.md) and that can be used in operand positions of CDS entities.

### AMDP Scalar Functions for AMDP Methods

An AMDP function implementation is declared in an [AMDP class](abenamdp_classes.md) like a regular [static method](../../abap-glossary/abenstatic_method_glosry.md) or [instance method](../../abap-glossary/abeninstance_method_glosry.md) in any [visibility section](../../abap-glossary/abenvisibility_section_glosry.md). An AMDP function implementation is not recognizable as such in the declaration part of the class and the same rules apply as to AMDP table functions for AMDP methods (described above) with the following differences:

- The data type of the return value is [elementary](../../abap-glossary/abenelementary_data_type_glosry.md).

- The data types of input parameters must also be elementary.

- No class-based exceptions can be declared using [`RAISING`](../abap-declarations/abapmethods_general.md) in the interface of the AMDP function implementation for AMDP scalar functions.

- An AMDP scalar function can be [called](../abap-calling-and-exiting-program-units/abenmethod_calls.md) in ABAP like a regular method and can be used as a [functional method](../../abap-glossary/abenfunctional_method_glosry.md) in a [functional method call](../../abap-glossary/abenfunctional_method_call_glosry.md).

The [AMDP scalar function](../../abap-glossary/abenamdp_scalar_function_glosry.md) defined using an AMDP function implementation like this can be used in other AMDP methods in accordance with the rules for [scalar functions](../../abap-glossary/abenscalar_function_glosry.md).

### Hints

- It is possible for an [AMD scalar function](../../abap-glossary/abenamdp_scalar_function_glosry.md) to specify the database-specific option `DETERMINISTIC` after `OPTIONS`. This buffers the result of the function for the duration of a query. For further details, see topic [`METHOD`, `BY DATABASE PROCEDURE`, `FUNCTION`, `GRAPH WORKSPACE`](abapmethod_by_db_proc.md).

### Executable Example

AMDP functions

### AMDP Scalar Functions for CDS Scalar Functions

The same rules apply to an AMDP function implementation that implements a [CDS scalar function](../../abap-glossary/abencds_scalar_function_glosry.md) as to the AMDP scalar functions for AMDP methods (described above), with the following differences:

- An AMDP function implementation for a CDS scalar function can only be declared in the public [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) of a [static](../../abap-glossary/abenstatic_class_glosry.md) AMDP class. It is not possible in interfaces.

- A special form of the statement [`CLASS-METHODS`](../abap-declarations/abapclass-methods.md) with the addition [`FOR SCALAR FUNCTION`](abapclass-methods_for_scalfunc.md) must be used for the declaration. This addition flags the [AMDP](../../abap-glossary/abencds_table_function_glosry.md) function implementation as an implementation of a [CDS scalar function](../../abap-glossary/abencds_scalar_function_glosry.md).

- The parameter interface of the AMDP function implementation is not declared using the statement `CLASS-METHODS`. Instead it is generated in accordance with the associated [CDS scalar function](../../abap-glossary/abencds_scalar_function_glosry.md) using the statement [`DEFINE SCALAR FUNCTION`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_scalar_function.md) in the [ABAP CDS](../../abap-glossary/abencds_ddl_glosry.md) [CDS DDL](../../abap-glossary/abenabap_cds_glosry.md):

  - The input parameters in the AMDP function implementation are determined by the input parameters of the CDS scalar function. Their names are used, and the ABAP types are derived from their Dictionary types. The input parameters are always elementary and not optional.

  - A return value with an elementary data type named `result` is created. Its data type is derived from the CDS scalar function definition.

- An AMDP scalar function cannot be [called](../abap-calling-and-exiting-program-units/abenmethod_calls.md) in ABAP like a regular method. It cannot be used as a [functional method](../../abap-glossary/abenfunctional_method_glosry.md) in a [functional method call](../../abap-glossary/abenfunctional_method_call_glosry.md). Calls from other AMDP methods are not possible. AMDP scalar functions for CDS scalar functions can only be accessed using the name of their CDS entity, that is, the name of the CDS scalar function definition.

The [AMDP scalar function](../../abap-glossary/abenamdp_scalar_function_glosry.md) defined by an AMDP function implementation like this can be used in operand positions of a CDS view entity in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) of [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md).

### Hints

- An AMDP function implementation can only be linked with a single CDS scalar function.

- When an AMDP function implementation is created for a CDS scalar function, the CDS scalar function definition must already exist as an active function. When a new CDS scalar function definition is activated, an empty AMDP scalar function is created in the database. This function raises an exception if a non-AMDP access is performed. When the CDS scalar function is accessed by the ABAP runtime framework for the first time, the AMDP function implementation implements the empty AMDP scalar function. It is possible to access the scalar function in a native way only after the implementation.
