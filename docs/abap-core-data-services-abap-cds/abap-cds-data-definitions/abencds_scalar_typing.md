---
title: "CDS DDL - typing"
source_file: abencds_scalar_typing.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Function Definitions > ABAP CDS - Scalar Functions > ABAP CDS - SQL-Based Scalar Functions > CDS DDL - DEFINE SCALAR FUNCTION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - typing

## Syntax

``` abap
 
  dtype                       [WITH REFERENCE TYPE] 
| simple_type                 [WITH REFERENCE TYPE] 
| data_element                [WITH REFERENCE TYPE] 
| generic_type                [WITH REFERENCE TYPE] 
| TYPE OF ParameterReference  [WITH REFERENCE TYPE]  
```

[`dtype`](abencds_typing.md) · [`WITH REFERENCE TYPE`](abencds_with_reference_type.md) · [`simple_type`](abencds_define_simple_type.md) · [`WITH REFERENCE TYPE`](abencds_with_reference_type.md) · [`data_element`](../../abap-dictionary-ddic/ddic-data-types/abenddic_data_elements.md) · [`WITH REFERENCE TYPE`](abencds_with_reference_type.md) · [`generic_type`](../abap-cds-data-types/abenddic_generic_types.md) · [`WITH REFERENCE TYPE`](abencds_with_reference_type.md) · [`WITH REFERENCE TYPE`](abencds_with_reference_type.md)

### Addition

[`... WITH REFERENCE TYPE`](abencds_scalar_typing.md#addition)

## Overview

### Description

The input parameters of [SQL-based scalar functions](../../abap-glossary/abencds_sql_scalar_glosry.md) can be typed as follows:

- Using a [built-in ABAP Dictionary data type](abencds_typing.md).

- Using a [CDS simple type](../../abap-glossary/abencds_simple_type_glosry.md) defined using [`DEFINE TYPE`](abencds_define_simple_type.md).

- Using a [DDIC data element](../../abap-glossary/abendata_element_glosry.md).

- Using the [generic data type](../abap-cds-data-types/abenddic_generic_types.md) `numeric`.

  **Note:** The generic type `any` is only available for analytical scalar functions.

- Referencing another input parameter using the syntax statement `TYPE OF ParameterReference`. `ParameterReference` can be any input parameter from the parameter list of the current scalar function that is typed with a built-in data type, a simple type, a data element, or a generic type.

  **Note:** You cannot reference the return parameter. **Note:** You cannot reference an input parameter that itself references an input parameter.

The return parameter of an SQL-based scalar function can be typed as follows:

- Using a [built-in ABAP Dictionary data type](abencds_typing.md).

- Using a [CDS simple type](../../abap-glossary/abencds_simple_type_glosry.md) defined using [`DEFINE TYPE`](abencds_define_simple_type.md).

- Using a [DDIC data element](../../abap-glossary/abendata_element_glosry.md).

- Referencing another input parameter using the syntax statement `TYPE OF ParameterReference`. `ParameterReference` can be any of the input parameters from the parameter list of the current scalar function that is typed with a built-in data type, a simple type, a data element, or a generic type.

  **Note:** You cannot reference an input parameter that itself references an input parameter.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates the definition, implementation, and use of an SQL-based scalar function with input parameters.

**CDS scalar function definition**

The following CDS scalar function `DEMO_CDS_SCALAR_RATIO` defines two input parameters:

- `portion`: Typed with the generic type `numeric`. Accepts all available reference types.

- `total`: Typed with reference to the input parameter `portion`.

The return parameter is typed with a built-in data type.

``` abap
define scalar function DEMO_CDS_SCALAR_RATIO 
  with parameters 
    portion: numeric 
      with reference type [ #CUKY, #UNIT, #CALC, #NONE ], 
    total  : type of portion 
      with reference type of portion 
  returns abap.decfloat34 
    with reference type #NONE;
```

**CDS scalar function implementation reference**

The scalar function implementation reference ` DEMO_CDS_SCALAR_RATIO_SQL` binds the scalar function to the SQL Engine and defines the method `EXECUTE` of the class `CL_DEMO_CDS_SCALAR_RATIO` as AMDP function implementation.

**AMDP function implementation**

The following listing shows the AMDP function implementation. The input parameter `portion` is divided by the input parameter `total` and multiplied by 100 to get the percentage of `portion` in relation to `total`.

``` abap
METHOD execute BY DATABASE FUNCTION 
               FOR HDB 
               LANGUAGE SQLSCRIPT 
               OPTIONS READ-ONLY. 
  result = portion / total * 100; 
ENDMETHOD.
```

**Use in a CDS view entity**

The following CDS view entity uses the scalar function `DEMO_CDS_SCALAR_RATIO` as an element in the `SELECT` list to calculate the occupancy of a flight.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, scalar func'

define view entity DEMO_CDS_SCALAR_USE_RATIO
  as select from sflight
{
  key carrid                  as Carrid,
  key connid                  as Connid,
  key fldate                  as Fldate,
      seatsocc                as BookedSeats,
      seatsmax                as TotalSeats,
      DEMO_CDS_SCALAR_RATIO( 
        portion => seatsocc, 
        total   => seatsmax ) as OccupationRatio
}
```

**Access Using ABAP SQL**

The following code snippet demonstrates how the CDS view entity can be accessed. The value of the column `OccupationRatio` is calculated by the AMDP function implementation.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
  FROM demo_cds_scalar_use_ratio 
  INTO TABLE @DATA(result). 
 
out->write( result ). 
 
out->display( ).
```

## Addition

`... WITH REFERENCE TYPE`

### Description

Specifies a reference type. Reference types allow the handling of [CDS amount fields](../../abap-glossary/abencds_amount_field_glosry.md) and [CDS quantity fields](../../abap-glossary/abencds_quantity_glosry.md). The addition is described in topic [CDS DDL - `WITH REFERENCE TYPE`](abencds_with_reference_type.md).
