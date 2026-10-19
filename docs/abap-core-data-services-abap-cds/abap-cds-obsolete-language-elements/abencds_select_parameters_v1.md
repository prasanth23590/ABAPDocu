---
title: "CDS DDL - DDIC-Based View, CDS Parameter Passing"
source_file: abencds_select_parameters_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, CDS Parameter Passing

## Syntax

``` abap
... ( pname1 : act1, pname2 : act2, ... ) ...  
```

## Description

Passes actual parameters `act1`, `act2`, ... to the [input parameters](../abap-cds-data-definitions/abencds_f1_param.md) `pname1`, `pname2`, ... of a [CDS entity](../../abap-glossary/abencds_entity_glosry.md).

The following can be specified for actual parameters:

- [Literals](abencds_literal_v1.md)

- [Parameters](abencds_parameter_v1.md)

- [Session variables](abencds_session_variable_v1.md)

The data types of the actual parameters should match the [typing](../abap-cds-data-definitions/abencds_typing.md) of the input parameters exactly. However the following options are also possible:

- bind character-like actual parameters to character-like input parameters with a different length.

- bind numeric actual parameters to numeric input parameters with a greater value range.

## Hint

Currently, actual parameters can be passed to the input parameters of [CDS views](../../abap-glossary/abencds_view_glosry.md), [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md), and [CDS hierarchies](../../abap-glossary/abencds_hierarchy_glosry.md) used as data sources of the `SELECT` statement.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view uses the CDS view `demo_cds_parameters` in a join. The input parameters of this view are supplied with the input parameters of the current view as actual parameters. The class `CL_DEMO_CDS_PARAMETERS_JOIN` uses `SELECT` to access the view. Here the input parameters are supplied with actual parameters.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_PARJOIN'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_parameters_join
  with parameters
    in_distance_l :s_distance,
    in_distance_u :s_distance,
    in_unit       :s_distid
  as select from
           demo_cds_parameters
      ( p_distance_l : $parameters.in_distance_l,
        p_distance_u : $parameters.in_distance_u,
        p_unit       : $parameters.in_unit ) as flights
      join scarr on
        scarr.carrid = flights.carrid
    {
      key scarr.carrname,
      key flights.connid,
          flights.cityfrom,
          flights.cityto,
          flights.distance,
          flights.distid
    }; 
```
