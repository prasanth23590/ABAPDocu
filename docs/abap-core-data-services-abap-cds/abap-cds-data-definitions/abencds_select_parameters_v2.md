---
title: "CDS DDL - CDS View Entity, CDS Parameter Passing"
source_file: abencds_select_parameters_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, CDS Parameter Passing

## Syntax

``` abap
... ( pname1 : act1, pname2 : act2, ... ) ...  
```

## Description

Passes actual parameters `act1`, `act2`, ... to the [input parameters](abencds_f1_param.md) `pname1`, `pname2`, ... of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md).

The following can be specified for actual parameters:

- [Literals](abencds_literal_v2.md)

- [Parameters](abencds_parameter_v2.md)

- [Session variables](abencds_session_variable_v2.md)

- [CDS enumerated constants](abencds_enum_field_v2.md)

The data types of the actual parameters should match the [typing](abencds_typing.md) of the input parameters exactly. However the following options are also possible:

- bind character-like actual parameters to character-like input parameters with a different length.

- bind numeric actual parameters to numeric input parameters with a greater value range.

## Hints

- Currently, actual parameters can be passed to the input parameters of [CDS views](../../abap-glossary/abencds_view_glosry.md), [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md), and [CDS hierarchies](../../abap-glossary/abencds_hierarchy_glosry.md) used as data sources of the `SELECT` statement.

- If a CDS table function is used as [data source](abencds_data_source_v2.md) after `FROM`, the input parameters and the corresponding actual parameters can also have data type `abap.string`. This has been enabled to avoid length restrictions in spatial scenarios, such as the SAP Geo Framework.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity uses the CDS view entity `demo_cds_parameters_ve` in a join. The input parameters of this view are supplied with the input parameters of the current view as actual parameters. The class `CL_DEMO_CDS_PARAMETERS_JOIN_VE` uses `SELECT` to access the view. Here the input parameters are supplied with actual parameters.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_PARAMETERS_JOIN_VE
  with parameters
    in_distance_l :s_distance,
    in_distance_u :s_distance,
    in_unit       :s_distid
  as select from demo_cds_parameters
                 ( p_distance_l : $parameters.in_distance_l,
                 p_distance_u : $parameters.in_distance_u,
                 p_unit       : $parameters.in_unit ) as flights
    join         scarr on scarr.carrid = flights.carrid
{
  key scarr.carrname,
  key flights.connid,
      flights.cityfrom,
      flights.cityto,
      flights.distance,
      flights.distid
}
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity demonstrates parameter passing in a [path expression](abencds_path_expression_v2.md).

``` abap
@AbapCatalog.viewEnhancementCategory: [#NONE]
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity'

define view entity DEMO_CDS_PARAMETER_PASSING
  as select from demo_ddic_types

  association of many to many Demo_Cds_Param_View_Entity as _assoc 
    on 1 = 1
{
  key id   as Id,
      int1 as Int1,
      int2 as Int2,
      int4 as Int4,
      int8 as Int8,
      _assoc(p_distance_l: 15, p_distance_u:16, p_unit:'KM').carrid 
           as MyField
}
```
