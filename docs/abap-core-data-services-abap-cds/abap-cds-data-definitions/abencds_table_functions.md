---
title: "ABAP CDS - Table Functions"
source_file: abencds_table_functions.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Table Functions

A CDS table function is defined in the [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) of a [CDS data definition](../../abap-glossary/abencds_data_definition_glosry.md) in the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md) using the statement [`DEFINE TABLE FUNCTION`](abencds_f1_define_table_function.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) of the [ABAP Core Data Services (CDS)](../abencds.md). A CDS table function includes the following:

- The [CDS entity](../../abap-glossary/abencds_entity_glosry.md)

  A CDS table function is declared as a CDS entity `table_function` using the statement [`DEFINE TABLE FUNCTION`](abencds_f1_define_table_function.md). As a global data type, the CDS entity represents a structured type with the [elements of the CDS table function](abencds_f1_return_list.md) as components and can be used like any [CDS entity](../../abap-glossary/abencds_entity_glosry.md).

  - In ABAP CDS, the CDS entity can be used as a data source of other CDS entities.

  - In ABAP, the CDS entity can be used as a data type and in ABAP SQL read statements.

  - The CDS entity cannot be used as a data type for definitions of [dictionary objects](../../abap-glossary/abendictionary_object_glosry.md).

    A CDS table function is located in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

- An [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md)

  CDS table functions are implemented in platform-dependent SQL in a special [AMDP method](../../abap-glossary/abenamdp_method_glosry.md) and the implementation is managed as an [AMDP table function](../../abap-glossary/abenamdp_table_function_glosry.md) by the [AMDP](../../abap-glossary/abenamdp_glosry.md) in the database system. The AMDP method is specified after the addition `IMPLEMENTED BY` in the definition of the CDS table function using [`DEFINE TABLE_FUNCTION`](abencds_f1_define_table_function.md). It must be declared as a special [AMDP function implementation](../../abap-programming-language/abap-database-access/abenamdp_function_methods.md) for exactly one CDS table function using the addition [`FOR TABLE FUNCTION`](../../abap-programming-language/abap-database-access/abapclass-methods_for_tabfunc.md). The parameter interface of the AMDP table function is defined using the [input parameters](abencds_f1_func_parameter_list.md) and the [element list](abencds_f1_return_list.md) of the CDS table function.

A CDS table function is client-dependent by default and [implicit client handling](../../abap-programming-language/abap-database-access/abenabap_sql_client_handling.md) is applied in ABAP SQL reads.

CDS table functions are [CDS SQL entities](../../abap-glossary/abencds_sql_entity_glosry.md).

## Hints

- CDS table functions can only be used in a database system that supports [AMDP](../../abap-glossary/abenamdp_glosry.md).

- When a CDS table function is created, the CDS entity must be activated first, before the associated [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md) is created.

- When a CDS table function is transported, the CDS entity is first transported at the same time as the dictionary transport objects and then the AMDP function implementation as part of the ABAP transport objects. Depending on the size of the transport, there can be a considerable delay between these two phases where the CDS table function is not in a usable state.

- CDS table functions and [CDS scalar functions](../../abap-glossary/abencds_scalar_function_glosry.md) are both implemented in an [AMDP method](../../abap-glossary/abenamdp_method_glosry.md) as an [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md). The differences between CDS table functions and CDS scalar functions are as follows:

  - CDS scalar functions return an elementary value, while CDS table functions return a tabular result type.

  - Different use cases:

    \- CDS table functions are used as a data source in other CDS entities or in ABAP SQL read statements. - CDS scalar functions can be used in the same way as built-in functions, i.e. in operand positions that expect scalar values. Before the introduction of CDS scalar functions, users could define [AMDP scalar functions](../../abap-glossary/abenamdp_scalar_function_glosry.md), but they were not available in CDS entities. CDS scalar functions make scalar functions defined in AMDP known to [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md) and available in ABAP CDS.

- CDS table functions cannot be processed by the [ABAP SQL in-memory engine](../../abap-programming-language/abap-database-access/abenabap_sql_inmemeng.md). An ABAP SQL statement that accesses a CDS table function bypasses the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table accessed by [`FROM @itab`](../../abap-programming-language/abap-database-access/abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

## More Information

For more information about CDS table functions, see [*CDS Table Functions*](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/ed4c5fc6d3fd43ebb355f12aa1e73757?version=sap_cross_product_abap) in the ABAP Data Models guide on SAP Help Portal.
