---
title: "CDS DDL - CDS View Entity, Built-In Session Variables"
source_file: abencds_session_var_builtin_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Elementary CDS Operands > CDS DDL - CDS View Entity, session_variable"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, Built-In Session Variables

## Syntax

``` abap
... $session.vname ...  
```

## Description

Specifies a built-in [session variable](../../abap-glossary/abensession_variable_glosry.md) `vname` in an operand position in a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). The variable must be prefixed by `$session.`.

Session variables have a predefined name and provide context-dependent information. The following built-in session variables exist:

| **vname**         | **Value when accessed**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `user`            | Current [user name](../../abap-glossary/abenuser_name_glosry.md), nominal value of the ABAP system field [`sy-uname`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md). The returned value has the data type `CHAR`.                                                                                                                                                                                                                                                                                                                                                                              |
| `client`          | Current [client](../../abap-glossary/abenclient_glosry.md). The default value is the current client (nominal value of the ABAP system field [`sy-mandt`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md)). In reads of certain CDS entities with an ABAP SQL statement with the addition `USING CLIENT` and in calls of an [AMDP method](../../abap-glossary/abenamdp_method_glosry.md) from ABAP in whose declaration the addition [`AMDP OPTIONS CDS SESSION CLIENT`](../../abap-programming-language/abap-database-access/abapmethods_amdp_options_client.md) is specified, it is the value specified here. The returned value has the data type `CLNT`, length 3. |
| `system_language` | [Text environment language](../../abap-glossary/abentext_env_langu_glosry.md) of the current [internal session](../../abap-glossary/abeninternal_session_glosry.md), nominal value of the ABAP system field [`sy-langu`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md). The returned value has the data type `LANG`, length 1.                                                                                                                                                                                                                                                                                   |
| `system_date`     | Current [system date](../../abap-glossary/abensystem_date_glosry.md) of the AS ABAP, nominal value of the ABAP system field [`sy-datum`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md). The returned value is of data type `DATS`, length 8.                                                                                                                                                                                                                                                                                                                                                   |
| `user_timezone`   | [User time zone](../../abap-glossary/abenuser_time_zone_glosry.md), nominal value of the ABAP system field [`sy-zonlo`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md). The returned value has the data type `CHAR`, length 6.                                                                                                                                                                                                                                                                                                                                                                  |
| `user_date`       | Current [user date](../../abap-glossary/abenuser_date_glosry.md), nominal value of the ABAP system field [`sy-datlo`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md). The returned value is of data type `DATS`, length 8.                                                                                                                                                                                                                                                                                                                                                                      |

## Hints

- From a technical perspective, session variables indicate global variables of the current database that are set to their value when the CDS view entity is used in ABAP SQL. If ABAP SQL is not used to access a CDS view entity with session variables, the content of the variables is undefined (with the exception of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md)).

- For [input parameters](abencds_parameter_list_v2.md) of CDS view entities annotated with the annotation [`environment.systemField`](abencds_f1_parameter_annotations.md), ABAP SQL automatically passes the values of the session variables. It is generally preferable to use this type of local input parameter.

- In existing CDS view entities without corresponding input parameters, session variables can be passed to the input parameters of CDS view entities or CDS table functions used there.

- In CDS view entities, [client handling](abencds_v2_view_client_handling.md) takes place implicitly by using the session variable `client`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity contains all possible session variables in the `SELECT` list.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity `DEMO_CDS_SELECT_T100_VE` accesses the CDS view entity `DEMO_CDS_SELECT_T100_LANGU_VE`, which contains a language input parameter to which the annotation [`environment.systemField`](abencds_f1_parameter_annotations.md) with the value `system_language` is assigned. Unlike in ABAP SQL, there is no implicit pass of the actual parameter to the input parameter here and the corresponding session variable `$session.system_language` is passed instead. The class `CL_DEMO_CDS_T100_VE` uses ABAP SQL to access both view entities and the result is identical. When `DEMO_CDS_SELECT_T100_LANGU_VE` is accessed, the value of the system field `sy-langu` is passed implicitly to the input parameter. When `DEMO_CDS_SELECT_T100` is accessed, the session variable `$session.system_language` is filled with this value.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_SELECT_T100_VE
  as select from DEMO_CDS_SELECT_T100_LANGU_VE(
                 p_langu: $session.system_language )
  {
    key sprsl,
    key arbgb,
    key msgnr,
        text
  }

```abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_SELECT_T100_LANGU_VE
  with parameters
    @Environment.systemField:#SYSTEM_LANGUAGE
    p_langu : lang
  as select from t100
  {
    key sprsl,
    key arbgb,
    key msgnr,
        text
  }
  where
        sprsl = $parameters.p_langu
    and arbgb = 'SABAPDEMOS'
```
