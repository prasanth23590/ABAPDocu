---
title: "CDS DDL - DDIC-Based View, session_variable"
source_file: abencds_session_variable_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Elementary CDS Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, session_variable

## Syntax

``` abap
... $session.vname ...  
```

## Description

Specifies a [session variable](../../abap-glossary/abensession_variable_glosry.md) `vname` in an operand position in a [`SELECT` statement](abencds_select_statement_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). The variable must be prefixed by `$session.`. The prefix and the variable are case-sensitive. `$session.vname`, `$Session.Vname`, and `$SESSION.VNAME` can all be used. No other spellings are allowed.

Session variables have a predefined name and are set to a predefined value when the CDS view is used in ABAP SQL. This also applies to CDS views that are used as data sources in other CDS views. The following session variables exist:

| **vname**         | **Value when accessed using ABAP SQL**                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `user`            | Current [user name](../../abap-glossary/abenuser_name_glosry.md), nominal value of the ABAP system field [`sy-uname`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md). The returned value has the data type `CHAR`.                                                                                                                                                                                                                                                                                                                                  |
| `client`          | Current [client](../../abap-glossary/abenclient_glosry.md). The default value is the nominal value of the ABAP system field [`sy-mandt`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md). In reads with an ABAP SQL statement (with the addition `USING CLIENT`) and in calls of an [AMDP method](../../abap-glossary/abenamdp_method_glosry.md) from ABAP (in whose declaration the addition [`AMDP OPTIONS CDS SESSION CLIENT`](../../abap-programming-language/abap-database-access/abapmethods_amdp_options_client.md) is specified, the value specified here. The returned value has the data type `CLNT`, length 3. |
| `system_language` | [Text environment language](../../abap-glossary/abentext_env_langu_glosry.md) of the current [internal session](../../abap-glossary/abeninternal_session_glosry.md), nominal value of the ABAP system field [`sy-langu`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md). The returned value has the data type `LANG`, length 1.                                                                                                                                                                                                                                       |
| `system_date`     | Current [system date](../../abap-glossary/abensystem_date_glosry.md) of the AS ABAP, nominal value of the ABAP system field [`sy-datum`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md). The returned value has the data type `DATS`, length 8.                                                                                                                                                                                                                                                                                                     |
| `user_timezone`   | [User time zone](../../abap-glossary/abenuser_time_zone_glosry.md), nominal value of the ABAP system field [`sy-zonlo`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md). The returned value has the data type `CHAR`, length 6.                                                                                                                                                                                                                                                                                                                      |
| `user_date`       | Current [user date](../../abap-glossary/abenuser_date_glosry.md), nominal value of the ABAP system field [`sy-datlo`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md). The returned value is of data type `DATS`, length 8.                                                                                                                                                                                                                                                                                                                          |

## Hints

- From a technical perspective, session variables indicate global variables of the current database that are set to their value when the CDS view is used in ABAP SQL. If ABAP SQL is not used to access a CDS view with session variables, the content of the variables is undefined (with the exception of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md)).

- For [input parameters](abencds_parameter_list_v1.md) of CDS views annotated with the special annotation [`environment.systemField`](../abap-cds-data-definitions/abencds_f1_parameter_annotations.md), ABAP SQL can pass the values of the session variables specified here automatically too. It is generally preferable to use this type of local input parameter.

- In existing CDS views without corresponding input parameters, session variables can be passed to the input parameters of CDS views or CDS table functions used there.

- In the [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) whose [client handling](abencds_view_client_handling_v1.md) is set by the annotation [`@ClientHandling.algorithm: #SESSION_VARIABLE`](abencds_view_client_handling_v1.md), the value of the session variable `client` is used in `WHERE` conditions for the [client column](../../abap-glossary/abenclient_column_glosry.md).

- A CDS view that accesses a session variable directly or using a view cannot usually be [buffered](abencds_v1_buffering.md). Only [client-dependent](abencds_view_client_handling_v1.md) views that access the session variable `client` directly can be buffered.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view contains the possible session variables in the `SELECT` list.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_SESSVAR'
@AccessControl.authorizationCheck: #NOT_ALLOWED
define view demo_cds_session_variables
  as select from demo_expressions
{
  key id,
      $session.user            as system_user,
      $session.client          as system_client,
      $session.system_language as system_language,
      $session.system_date     as system_date,
      $session.user_timezone   as user_timezone,
      $session.user_date       as user_date
}
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view `DEMO_CDS_SELECT_T100` accesses a further CDS view `DEMO_CDS_SELECT_T100_LANGU` with a language input parameter to which the annotation [`environment.systemField`](../abap-cds-data-definitions/abencds_f1_parameter_annotations.md) with the value `system_language` is assigned. Unlike in ABAP SQL, there is no implicit pass of the actual parameter to the input parameter here and the corresponding session variable `$session.system_language` is passed instead. The class `CL_DEMO_CDS_T100` uses ABAP SQL to access both views and the result is identical. When `DEMO_CDS_SELECT_T100_LANGU` is accessed, the value of the system field `sy-langu` is passed implicitly to the input parameter. When `DEMO_CDS_SELECT_T100` is accessed, the session variable `$session.system_language` is filled with this value.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_T100'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_select_t100
  as select from
    demo_cds_select_t100_langu( p_langu: $session.system_language )
    {
      *
    }

```abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_T100_LG'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_select_t100_langu
  with parameters
    @Environment.systemField:#SYSTEM_LANGUAGE
    p_langu : lang
  as select from
    t100
    {
      *
    }
    where
          sprsl = :p_langu
      and arbgb = 'SABAPDEMOS'
```
