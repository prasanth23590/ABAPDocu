---
title: "ABAP SQL - SQL Parameter Passing sql_para"
source_file: abenabap_sql_parameters.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - SQL Parameter Passing sql_para

## Syntax

``` abap
... ( pname1 = act1, pname2 = act2, ... ) ...  
```

## Description

Specifies actual parameters `act1`, `act2`, ... for input parameters [`pname1`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_param.md), [`pname2`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_param.md), ... of a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) in a parenthesized comma-separated list. Parameters can be passed to [CDS persistent entities](../../abap-glossary/abencds_sql_entity_glosry.md) in the following positions in ABAP SQL statements:

- After a CDS entity as the [data source](abapselect_data_source.md) of the [`FROM` clause](abapfrom_clause.md) of a [query](../../abap-glossary/abenasql_query_glosry.md).

- After the CDS associations of a [path expression](abenabap_sql_path.md) in the [data source](abapselect_data_source.md) of the [`FROM` clause](abapfrom_clause.md) and in the [column specifications](abenabap_sql_columns.md) of a [query](../../abap-glossary/abenasql_query_glosry.md).

If a CDS entity has [input parameters](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_param.md) as the data source [`data_source`](abapselect_data_source.md) of a [query](../../abap-glossary/abenasql_query_glosry.md) or `target` of a CDS association specified in a [path expression](abenabap_sql_path.md), a matching actual parameter must be passed to each input parameter as follows:

- If an input parameter does not have an annotation [`@Environment.systemField`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_parameter_annotations.md), an explicit actual parameter must be specified.

- If an input parameter has an annotation [`@Environment.systemField`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_parameter_annotations.md) with one of the predefined values [`#SYSTEM_...`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_parameter_annotations.md), an explicit actual parameter does not need to be specified. If no actual parameter is specified, ABAP SQL passes the nominal value of the system field assigned using the annotation implicitly. Here, only the date and time are taken from the system fields `sy-datum` and `sy-uzeit` and the language and user name are taken from secure sources.

- If an input parameter has an annotation [`@Environment.systemField`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_parameter_annotations.md) with the predefined value [`#CLIENT`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_parameter_annotations.md), an explicit actual parameter must not be specified. Instead, ABAP SQL passes the ID of the current [client](../../abap-glossary/abenclient_glosry.md) or a client specified using `USING CLIENT` implicitly.

[Literals](abenabap_sql_literals.md), [host variables](abenabap_sql_host_variables.md), or [host expressions](abenabap_sql_host_expressions.md), can be specified as actual parameters. The name of a host variable must be prefixed with the escape character `@`. The data type of the parameter must be convertible to the [built-in data type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) in the ABAP Dictionary. The built-in data type is specified by the [typing](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_typing.md) of the parameter. The content of the actual parameter must match the data type of the input parameter in accordance with the rules for a [lossless assignment](../../abap-glossary/abenlossless_assignment_glosry.md). Only typed literals are passed directly without conversion.

In the following cases, the parentheses `( )` after the name of a CDS entity can be empty or omitted:

- The function is a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md) without input parameters.

- The view is a [CDS view](../../abap-glossary/abencds_view_glosry.md) with input parameters that are all filled implicitly using the annotation [`@Environment.systemField`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_parameter_annotations.md).

Parentheses cannot be specified in CDS views without input parameters or in any dictionary objects.

## Hints

- There are currently no optional input parameters for CDS entities and no real replacement values for input parameters. The annotation [`@Environment.systemField`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_parameter_annotations.md) bypasses this gap for some environment values by providing the caller with the non-optional parameters implicitly.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Passing of a time zone to the input parameter `tz` of the CDS view entity `demo_cds_assoc_sairport_tz`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA timezone TYPE s_tzone VALUE 'UTC+1'. 
cl_demo_input=>request( CHANGING field = timezone ). 
 
SELECT id 
       FROM demo_cds_assoc_sairport_tz( tz = @timezone ) 
       INTO TABLE @FINAL(result). 
 
out->write( result ). 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A CDS [enumerated constant](../../abap-glossary/abenenumerated_constant_glosry.md) is specified as a column in the `SELECT` list, in the `WHERE` clause, in the `ORDER BY` clause and passed as actual parameter.

``` abap
SELECT @demo_cds_enum_weekday-tue AS EnumConstant 
       FROM demo_cds_enum_type_usage_2( 
              p1 = @demo_cds_enum_char-first_value ) 
       WHERE friday = @demo_cds_enum_weekday-fri 
       ORDER BY @demo_cds_enum_char-initial_value 
       INTO TABLE @FINAL(itab).
```

## Executable Example

[`SELECT`, CDS View Entity with Input Parameters](abenselect_cds_para_abexa.md)
