---
title: "ABAP CDS - Definition of Client Handling for Table Functions"
source_file: abencds_func_client_hdl_def.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Table Functions > ABAP CDS - Client Handling in CDS Table Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Definition of Client Handling for Table Functions

The [CDS annotation](../../abap-glossary/abencds_annotation_glosry.md) [`ClientHandling.type`](../abap-cds-annotations/abencds_613831553_anno.md) is used to define the [client dependency](../../abap-glossary/abenclient_dependency_glosry.md) for a CDS table function.

- The value `#CLIENT_DEPENDENT` declares a table function as client-dependent.

- The value `#CLIENT_INDEPENDENT` declares a table function as client-independent.

Client dependency is declared by default. The value `#INHERITED` is not permitted for table functions.

The additional annotation [`ClientHandling.algorithm`](../abap-cds-annotations/abencds_1114072352_anno.md) specifies how implicit client handling is performed:

- Together with the value `#CLIENT_DEPENDENT` of annotation `ClientHandling.type`, the values `#NONE` and `#SESSION_VARIABLE` can be specified.

- Together with the value `#CLIENT_INDEPENDENT` of annotation `ClientHandling.type`, only the value `#NONE` can be specified.

The value `#AUTOMATED` cannot be specified for CDS table functions. If the annotation `ClientHandling.algorithm` is not specified, the value `#NONE` is used implicitly.

The following subtopics explain the effect of the different combinations of the annotations for client handling:

- [Client-Dependent CDS Table Function](abencds_func_client_hdl_def.md#client-dependent-cds-table-function)

  - [Client-Dependent Table Function without Using Session Variable](abencds_func_client_hdl_def.md#client-dependent-table-function-without-using-session-variable)

  - [Client-Dependent Table Function Using Session Variable](abencds_func_client_hdl_def.md#client-dependent-table-function-using-session-variable)

- [Client-Independent CDS Table Function](abencds_func_client_hdl_def.md#client-independent-cds-table-function)

## Hints

- CDS table functions for application data should usually be client-dependent.

## Client-Dependent CDS Table Function

Client-dependent CDS table functions are declared with the annotation `ClientHandling.type: #CLIENT_DEPENDENT`. In that case:

- The [element list](abencds_f1_return_list.md) of a client-dependent CDS table function must have an explicit client field with the built-in dictionary type `CLNT` as its first element. The client field is a column of the tabular return value of the associated AMDP function implementation and is not a component of the structured data type represented by the CDS entity.

- If the annotation [`ClientHandling.clientSafe`](../abap-cds-annotations/abencds_1549616294_anno.md) is not used, the table function can have an input parameter of the dictionary type `CLNT`, which must be annotated with the annotation [`Environment.systemField`](../abap-cds-annotations/abencds_1937921420_anno.md) and the enumerated value `#CLIENT`.

- If the annotation [`ClientHandling.clientSafe`](../abap-cds-annotations/abencds_1549616294_anno.md) is used, the table function cannot have an input parameter of the dictionary type `CLNT`.

### Client-Dependent Table Function without Using Session Variable

If the annotation [`ClientHandling.algorithm`](../abap-cds-annotations/abencds_1114072352_anno.md) is not specified or used with the value `#NONE`, the CDS table function is not inherently [client-safe](../../abap-glossary/abenclient_safe_glosry.md) but can access data of multiple clients. Client handling is done as follows:

- When a client-dependent CDS table function is accessed using [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) only those rows are selected implicitly from the result set of the function that contain the ID of the [current client](../../abap-glossary/abencurrent_client_glosry.md) in the client field.

- The platform-dependent SQL in the associated [AMDP method](../../abap-glossary/abenamdp_method_glosry.md) implementation must ensure that all required data is made available. Particularly in the `ON` conditions of joins, client columns must be used correctly.

- For performance and client safety, it is best to restrict the result set of the function to the required client at the implementation stage. This usually involves passing the client ID in question to an input parameter of the function. Here, it is advisable to use an input parameter of the dictionary type `CLNT`, which is annotated with the annotation [`Environment.systemField`](../abap-cds-annotations/abencds_1937921420_anno.md) and the enumerated value `#CLIENT`. In this case, [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) passes the correct client ID implicitly.

- Note that if the ABAP-specific session variables `CLIENT` and `CDS_CLIENT` are accessed in the implementation of a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md), the addition `USING CLIENT` of the ABAP SQL statement [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) only acts on the session variable `CDS_CLIENT`. If the AMDP function is used in an AMDP method called from ABAP, there is no equivalent for `USING CLIENT`.

### Executable Example

Refer to Client-Dependent CDS Table Functions (not Client-safe).

### Client-Dependent Table Function Using Session Variable

If the annotation [`ClientHandling.algorithm`](../abap-cds-annotations/abencds_1114072352_anno.md) is specified with the value `#SESSION_VARIABLE`, the implementing method of the AMDP class is handled as follows:

- If the table function has an input parameter of the dictionary type `CLNT` annotated with the annotation [`Environment.systemField`](../abap-cds-annotations/abencds_1937921420_anno.md) and the enumerated value `#CLIENT`, the implementing method of the AMDP class is handled as with the AMDP option [`CDS SESSION CLIENT clnt`](../../abap-programming-language/abap-database-access/abapmethods_amdp_options_client.md) where `clnt` is the name of the input parameter.

- If the table function has no input parameter of the dictionary type `CLNT`, the implementing method of the AMDP class is handled as with the AMDP option [`CDS SESSION CLIENT DEPENDENT`](../../abap-programming-language/abap-database-access/abapmethods_amdp_options_client.md). In this case the CDS table function is [client-safe](../../abap-glossary/abenclient_safe_glosry.md) and can be annotated with [`ClientHandling.clientSafe`](../abap-cds-annotations/abencds_1549616294_anno.md).

### Hint

Since an AMDP method with the AMDP option [`CDS SESSION CLIENT DEPENDENT`](../../abap-programming-language/abap-database-access/abapmethods_amdp_options_client.md) is client-safe but not an AMDP method with the AMDP option [`CDS SESSION CLIENT clnt`](../../abap-programming-language/abap-database-access/abapmethods_amdp_options_client.md), only client-dependent table functions without input parameter of the dictionary type `CLNT` can be client-safe.

### Executable Example

Refer to [Client-Dependent CDS Table Function (Client-safe)](abencds_func_client_dep_cs_abexa.md).

## Client-Independent CDS Table Function

Client-independent CDS table functions are declared with the annotation `ClientHandling.type: #CLIENT_INDPENDENT`. The annotation `ClientHandling.algorithm` can be specified with the value `#NONE` only.

- The [element list](abencds_f1_return_list.md) of a client-independent CDS table function does not need to have an explicit client field with the built-in dictionary type `CLNT`. If the first element has the type `CLNT`, it does not function as a client field. Instead, it is a column of the tabular return value of the associated AMDP function implementation and also a regular component of the structured data type represented by the CDS entity.

- When a client-independent CDS table function is accessed using [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md), an element of the type `CLNT` does not have a special meaning and is handled like any other element.

- A parameter of a client-independent CDS table function might have the dictionary type `CLNT`, but The annotation [`@Environment.systemField: #CLIENT`](abencds_f1_parameter_annotations.md) cannot be used in the parameter list.

Client-independent CDS table functions can be [client-safe](../../abap-glossary/abenclient_safe_glosry.md) or not.

- Client safety can be enforced with the annotation [`ClientHandling.clientSafe`](../abap-cds-annotations/abencds_1549616294_anno.md). Then, the implementing AMDP method must be client-safe and no cross-client access is possible.

- If the annotation [`ClientHandling.clientSafe`](../abap-cds-annotations/abencds_1549616294_anno.md) is not used, the client safety of the implementing AMDP method is not strictly checked and cross-client access is possible.

As a rule, the implementing AMDP method should be handled as defined with the AMDP option [`CLIENT INDEPENDENT`](../../abap-programming-language/abap-database-access/abapmethods_amdp_options_client.md) and its [`USING`](../../abap-programming-language/abap-database-access/abapmethod_by_db_proc.md) list should contain only client-independent objects, otherwise a syntax warning occurs. If this rule is followed, the CDS table-function is client-safe.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

See the executable example Client-Independent CDS Table Function (Client-safe) for a client-safe table function.
