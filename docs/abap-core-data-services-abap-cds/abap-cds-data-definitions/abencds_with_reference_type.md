---
title: "CDS DDL - WITH REFERENCE TYPE"
source_file: abencds_with_reference_type.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Function Definitions > ABAP CDS - Scalar Functions > ABAP CDS - SQL-Based Scalar Functions > CDS DDL - DEFINE SCALAR FUNCTION > CDS DDL - typing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - WITH REFERENCE TYPE

## Syntax Forms

**Static Reference Type Specification**

``` abap
  WITH REFERENCE TYPE [#CUKY | #UNIT | #CALC | #NONE] 
| WITH REFERENCE TYPE OF pname 
```

**Dynamic Reference Type Specification**

``` abap
WITH REFERENCE TYPE 
  CASE 
    WHEN pname1: reference [AND pname2: reference][AND...] 
      THEN reference 
    [WHEN ... [AND ... ] THEN ...] 
    [ELSE reference] 
  END[;]
```

### Variant

[1. `WITH REFERENCE TYPE ref_type | OF ...`](abencds_with_reference_type.md#variant-1)

[2. `WITH REFERENCE TYPE CASE ...`](abencds_with_reference_type.md#variant-2)

## Overview

### Description

[SQL-based scalar functions](../../abap-glossary/abencds_sql_scalar_glosry.md) support the handling of [CDS amount fields](../../abap-glossary/abencds_amount_field_glosry.md) and [CDS quantity fields](../../abap-glossary/abencds_quantity_glosry.md). CDS amount fields and CDS quantity fields are fields with a reference to a [currency key](../../abap-glossary/abencurrency_key_glosry.md), a [unit key](../../abap-glossary/abenunit_glosry.md), or a [calculated unit](../../abap-glossary/abencds_calculated_unit_glosry.md). Scalar functions can handle these references. They can define which reference types are allowed for each [input parameter](../../abap-glossary/abeninput_parameter_glosry.md) and for the return parameter. The [actual parameters](../../abap-glossary/abenactual_parameter_glosry.md) passed to the input parameters must provide the required reference types. If the return parameter requires a reference type, the required annotation must be provided when the scalar function is used. Missing reference types for actual parameters or the return parameter result in a syntax check error.

The following general rules apply:

- If the data type of a parameter is specified as `abap.curr`, then the reference type must be `#CUKY`.

- If the type of a parameter is specified as `abap.quan`, then the reference type must be `#UNIT`.

In all other cases, the syntax checker does not check whether the data type and the reference type match and the developer must ensure logical combinations. The following definition is not logical and no actual parameter can satisfy the conditions. In other words, if a value has data type `CHAR`, it must not have a reference to a currency key and vice versa. The required data type and the required reference type are mutually exclusive. However, no syntax check error occurs.

``` abap
p1: abap.char(10) 
WITH REFERENCE TYPE [ #CUKY ]
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates the definition, implementation, and use of an SQL-based scalar function with parameters with reference types.

**CDS scalar function definition**

The following CDS scalar function `DEMO_CDS_SCALAR_REF_CASE` defines input parameters with reference types. The return parameter dynamically specifies the reference type.

``` abap
define scalar function DEMO_CDS_SCALAR_REF_CASE 
  with parameters 
    p1: numeric 
      with reference type [ #CUKY, #UNIT, #CALC, #NONE ], 
    p2: numeric 
      with reference type [ #CUKY, #UNIT, #CALC, #NONE ], 
    p3: abap.dec(4,2) 
      with reference type [ #CUKY, #UNIT, #CALC, #NONE ] 
  returns abap.dec(4,2) 
    with reference type 
      case 
        when p2: reference type of p1 
          then #NONE 
        else reference type of p1 
      end;
```

**CDS scalar function implementation reference**

The scalar function implementation reference `DEMO_CDS_SCALAR_REF_CASE_SQL` binds the scalar function to the SQL Engine and defines the method `EXECUTE` of the class `CL_DEMO_CDS_SCALAR_REF_CASE` as AMDP function implementation.

**AMDP function implementation**

The following listing shows the AMDP function implementation. The input parameters are summed up.

``` abap
METHOD execute BY DATABASE FUNCTION 
               FOR HDB 
               LANGUAGE SQLSCRIPT 
               OPTIONS READ-ONLY. 
  result = p1 + p2 + p3; 
  ENDMETHOD.
```

**Use in a CDS view entity**

The following CDS view entity uses the scalar function `DEMO_CDS_SCALAR_REF_CASE` as an element in the `SELECT` list. The passed actual parameter for `p1` has a unit key as reference and the result is also linked with a unit key using the annotation `@Semantics.quantity.unitOfMeasure`.

**Note:** The syntax checker checks the reference types of the input parameters and of the return parameter. Wrong reference types lead to a syntax check error.

**Note:** The AMDP function implementation does not check the reference types. It would be technically possible to add 5 kilometers and 3 kilograms. The result might not make sense, but there would be no syntax check error. The developer must ensure logical calculations.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, scalar func'

define view entity DEMO_CDS_SCALAR_USE_REF_CASE
  with parameters
    p1 : abap.dec(4,2)
  as select from DEMO_CDS_SCALAR_HELPER
{
  key Id,
      Unit2,
      @Semantics.quantity.unitOfMeasure: 'Unit2'
      DEMO_CDS_SCALAR_REF_CASE(
      p1 => Int4,
      p2 => abap.int4'22',
      p3 => $parameters.p1) as ScalarResult
}
```

## Variant 1

`WITH REFERENCE TYPE ref_type | OF ...`

### Description

The reference type can be specified statically. The following options are available:

- Specifying a reference type `ref_type`. The following values can be specified for `ref_type`:

  - `#CUKY`: The actual parameters passed must be [CDS amount fields](../../abap-glossary/abencds_amount_field_glosry.md). They must have a valid data type and they must be annotated with [`Semantics.amount.currencyCode`](abencds_f1_element_annotation.md).

  - `#UNIT`: The actual parameters passed must be [CDS quantity fields](../../abap-glossary/abencds_quantity_glosry.md). They must have a valid data type and they must be annotated with [`Semantics.quantity.unitOfMeasure`](abencds_f1_element_annotation.md).

  - `#CALC`: The passed actual parameters must be [CDS calculated quantities](../../abap-glossary/abencds_calculated_quantity_glosry.md). This means that they must be the result of a calculation, they have data type `DECFLOAT34`, and they must have a calculated unit reference using the annotation [`Semantics.quantity.unitOfMeasure`](abencds_f1_element_annotation.md).

  - `#NONE`: The actual parameters passed must not have a reference to a currency key, a unit of measure key, or a calculated unit.

- `WITH REFERENCE TYPE OF pname`: Defines a reference type with reference to another input parameter. A parameter typed with reference to another input parameter automatically inherits the reference type of the referenced parameter. This is useful when two parameters require the same reference type. The following rules apply:

  - The referenced parameter `pname` must be another input parameter. References to the return parameter are not supported.

  - `pname` must be a parameter that is specified statically with a reference value. Referencing parameters with a dynamic specification or with a parameter reference is not allowed.

An input parameter can have one or more reference types. The reference types can be freely combined. Here's an example:

`WITH REFERENCE TYPE [#CUKY, #CALC, #NONE, REFERENCE TYPE OF pname1]`

This means that the parameter in question supports all of the specified reference types, and the actual parameter can have a currency key reference, a calculated unit, no reference at all, or any of the reference types specified for the input parameter `pname1`.

**Note:** This does not apply to return parameters. Return parameters cannot have more than one reference type.

The data type specified for a parameter and the data type required by the reference type must match. This means:

- The reference type `#CUKY` only allows actual parameters of the types `CURR`, `DECFLOAT34`, `DEC`, and `FLTP`.

- The reference type `#UNIT` only allows actual parameters of the types `QUAN`, `DECFLOAT16`, `DECFLOAT34`, `DEC`, `FLTP`, `INT1`, `INT2`, or `INT4`.

- The reference type `#CALC` only allows actual parameters of the type `DECFLOAT34`.

- The reference type `#NONE` accepts all data types except for `CURR` and `QUAN`, because these data types force a reference type.

### Hints

- The [generic data type](../abap-cds-data-types/abenddic_generic_types.md) `numeric` has a different scope of data types than CDS amount fields and CDS quantity fields. When `numeric` is specified together with a reference type, the valid data types for the actual parameter are the intersection of the two requirements.

- Casting and conversions may be required for the actual parameters. For example, the generic data type `numeric` does not support the data type `abap.curr`. The conversion function [`CURR_TO_DECFLOAT_AMOUNT`](abencds_conv_func_unit_curr_v2.md) can be used to convert fields of the data type `abap.curr` to a data type that is allowed for `numeric`, so that they can be used as actual parameter for a parameter typed with `numeric`.

## Variant 2

`WITH REFERENCE TYPE CASE ...`

### Description

The reference type of the input parameter or return parameter can be defined dynamically, depending on the reference types of the input parameters. This is done using case statements. The following rules apply:

- Each parameter can have exactly one `CASE` statement.

- A `CASE` statement can have one or more `WHEN` branches.

- A `WHEN` branch can have one or more conditions. Multiple conditions can be combined with `AND`.

- For input parameters, the `ELSE` branch is optional. For the return parameter, the `ELSE` branch is mandatory.
