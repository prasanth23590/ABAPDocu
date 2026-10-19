---
title: "Environment.systemField"
source_file: abencds_1937921420_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > Environment"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Environment.systemField

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)                                         |
|-------------|--------------------------------------------------------------------------------------------|
| **Syntax**  | `Environment.systemField`                                                                  |
| **Scope**   | `#PARAMETER`                                                                               |
| **Type**    | `String(20)`                                                                               |
| **Enums**   | `#CLIENT, #SYSTEM_DATE, #SYSTEM_LANGUAGE, #SYSTEM_TIME, #USER, #USER_DATE, #USER_TIMEZONE` |
| **Default** | `-`                                                                                        |
| **Text**    | `-`                                                                                        |
| **MDE**     | `-`                                                                                        |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`                              |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Environment

Controls value passing to parameters.

## systemField

Assigns an ABAP system field to an input parameter of a CDS object for implicit parameter passing in ABAP SQL.

## Annotation Value

The possible enumeration values denote the system field. Tha annotation cannot be specified without a value. Otherwise, a syntax error (CDS view entity) or an exception during usage (all other CDS entities) occurs.

## Enums

## \#CLIENT

sy-mandt

## \#SYSTEM_LANGUAGE

sy-langu

## \#USER

sy-uname

## \#SYSTEM_DATE

sy-datum

## \#SYSTEM_TIME

sy-uzeit

## \#USER_DATE

sy-datlo

## \#USER_TIMEZONE

sy-zonlo

## Further Information

An input parameter can be annotated exactly once with the annotation `Environment.systemField`. If the CDS entity is used as a [data source](../../abap-programming-language/abap-database-access/abapselect_data_source.md) of a [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) statement in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), this assignment has the following consequences:

- No explicit actual parameter can be assigned in ABAP SQL to an input parameter to which the system field `sy-mandt` was assigned using `#CLIENT`. ABAP SQL always implicitly passes the ID of the [current client](../../abap-glossary/abencurrent_client_glosry.md) in accordance with the nominal value of `sy-mandt` or from the clients specified using `USING CLIENT`. The obsolete addition `CLIENT SPECIFIED` cannot be specified when a CDS entity of this type is accessed.

- No explicit actual parameter needs to be assigned in ABAP SQL to an input parameter to which a system field other than `sy-mandt` is assigned using `#SYSTEM_...`. If no explicit actual parameter is specified, ABAP SQL passes the nominal value of the assigned system field implicitly.

- For ABAP CDS, this annotation has no effect. Each formal parameter requires an actual parameter and also [session variables](../abap-cds-data-definitions/abencds_session_variable_v2.md) must be specified explicitly.

Any other values for `value` are ignored and raise an exception. For CDS view entities, no value or a wrong value lead to a syntax error.

The annotation `Environment.sql.passValue` is available for parameters in [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), [CDS projection views](../../abap-glossary/abencds_projection_view_glosry.md), and [CDS hierarchies](../../abap-glossary/abencds_hierarchy_glosry.md). It is not available for parameters in any other CDS entity.

### Hints

- The annotation `@Environment.systemField` is ignored in parameter passing to the CDS entity in other CDS entities. Explicit actual parameters must be specified here, for example input parameters from the current entity or [session variables](../abap-cds-data-definitions/abencds_session_variable_v2.md).

- The value `#CLIENT` of the annotation `@Environment.systemField` is particularly significant for [client-dependent CDS table functions](../abap-cds-data-definitions/abencds_func_client_handling.md). If an input parameter is annotated like this, it is given the current client ID implicitly by the ABAP SQL statement [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) and can be used to restrict the result set in the platform-dependent implementation of the function. `@Environment.systemField: #CLIENT` cannot be specified in the case of [client-independent CDS table functions](../abap-cds-data-definitions/abencds_func_client_handling.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity connects all input parameters with ABAP system fields and the `SELECT` list consists only of the input parameters. The ABAP class `CL_DEMO_CDS_SYSTEM_FIELDS` accesses the CDS view entity, once with explicit and once with implicit parameter passing, and produces both results.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_SYSTEM_FIELDS_VE
  with parameters
    @Environment.systemField : #CLIENT
    p_mandt : syst_mandt,
    @Environment.systemField : #SYSTEM_DATE
    p_datum : syst_datum,
    @Environment.systemField : #SYSTEM_TIME
    p_uzeit : syst_uzeit,
    @Environment.systemField : #SYSTEM_LANGUAGE
    p_langu : syst_langu,
    @Environment.systemField : #USER
    p_uname : syst_uname
  as select from
    demo_expressions
    {
      $parameters.p_mandt as client_field,
      $parameters.p_datum as datum,
      $parameters.p_uzeit as uzeit,
      $parameters.p_langu as langu,
      $parameters.p_uname as uname
    }
    where
      id = '1';
```
