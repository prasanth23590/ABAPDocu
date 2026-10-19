---
title: "CDS DDL - DEFINE SCALAR FUNCTION"
source_file: abencds_define_scalar_function.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Function Definitions > ABAP CDS - Scalar Functions > ABAP CDS - SQL-Based Scalar Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE SCALAR FUNCTION

## Syntax

``` abap
 
DEFINE SCALAR FUNCTION ScalarFunction 
  [WITH PARAMETERS pname1 : typing [, 
                   pname2 : typing][, 
                  ...]] 
          RETURNS typing[;]  
```

[`typing`](abencds_scalar_typing.md) · [`typing`](abencds_scalar_typing.md) · [`typing`](abencds_scalar_typing.md)

## Description

Defines a CDS scalar function definition `ScalarFunction` as a [CDS scalar function](../../abap-glossary/abencds_scalar_function_glosry.md). The name `ScalarFunction` must follow the naming conventions for [dictionary types](../../abap-dictionary-ddic/ddic-data-types/abenddic_types_names.md). The following additional rules apply:

- The name can be up to 26 characters long. Four characters are reserved for the suffix of the [scalar function implementation reference](abencds_scalar_func_impl_ref.md).

- The name must not start with the prefix `QCM`.

- The first, second, third, and last character of the name must not be an underscore (*\_*).

- A CDS scalar function is located in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

Optionally, a list of [input parameters](../../abap-glossary/abencds_parameter_glosry.md) `pname1`, `pname2`, ... can be declared using the addition `WITH PARAMETERS`. These also define the input parameters of the AMDP scalar function. There is no limit to the number of input parameters. The typing of these input parameters is explained in the topic [CDS DDL - `typing`](abencds_scalar_typing.md).

The name of an input parameter must comply with the naming rules for [names](../abap-cds-syntax/abencds_general_syntax_rules.md). Furthermore, it cannot contain any slash (/) characters and cannot be a reserved name in ABAP Dictionary. All reserved names that cannot be used are specified in the DDIC database table `TRESE`. The evaluation of names is not case-sensitive. Each parameter name must be unique. Blanks in the comma-separated parameter list are ignored and can be omitted.

`RETURNS` defines the data type of the scalar [return value](../../abap-glossary/abenreturn_value_glosry.md). The topic [CDS DDL - `typing`](abencds_scalar_typing.md) explains how the return value can be typed.

## Use

CDS scalar functions are available in [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) in operand positions that expect scalar values, similar to built-in functions. In particular, they can be specified in the following operand positions:

- As the right-hand side of a join ON-condition of a CDS view entity as documented in the topic [CDS DDL - CDS View Entity, `SELECT`, `JOIN`](abencds_joined_data_source_v2.md).

- As an element in the element list of a CDS view entity, as documented in the topic [CDS DDL - CDS View Entity, `SELECT`, `element`](abencds_select_list_entry_v2.md).

- As operands in a [`WHERE`](abencds_where_clause_v2.md) condition of a CDS view entity.

- As operands of an [arithmetic expression](abencds_arithmetic_expression_v2.md) in a CDS view entity.

- As operand of a [case distinction](abencds_case_expression_v2.md) in a CDS view entity.

- As operand of a [cast expression](abencds_cast_expression_v2.md) in a CDS view entity.

- As operands of [built-in functions](abencds_builtin_functions_v2.md) wherever documented.

- As an operand of a [filter condition](abencds_path_expression_filter_v2.md) of a [path expression](../../abap-glossary/abenpath_expression_glosry.md).

SQL-based scalar functions can be used as operands in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md). This is described in the topic [`sql_exp` - `cds_scalar_func`](../../abap-programming-language/abap-database-access/abensql_cds_scalar_func.md).

## Restrictions

- SQL-based scalar functions cannot be used in CDS entities other than CDS view entities.

Once a CDS scalar function has been activated, a [scalar function implementation reference](abencds_scalar_func_impl_ref.md) must be created. This scalar function implementation reference binds the scalar function to a runtime environment and refers to an [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md).

The scalar function is implemented in an AMDP function using the addition [`FOR SCALAR FUNCTION`](../../abap-programming-language/abap-database-access/abapclass-methods_for_scalfunc.md).

## Hints

- After activation, a CDS scalar function cannot be renamed.

- The scalar function definition and the scalar function implementation reference must have the same [ABAP language version](../../abap-glossary/abenabap_version_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates the definition, implementation, and use of an SQL-based scalar function.

**CDS scalar function definition**

The following CDS scalar function `DEMO_CDS_SCALAR_HELLOWORLD` has no input parameters. It only defines the data type of the return parameter.

``` abap
define scalar function DEMO_CDS_SCALAR_HELLOWORLD 
  returns abap.char(12)
```

**CDS scalar function implementation reference**

The scalar function implementation reference ` DEMO_CDS_SCALAR_HELLOWORLD_SQL` binds the scalar function to the SQL Engine and defines the method `EXECUTE` of the class `CL_DEMO_CDS_SCALAR_HELLOWORLD` as AMDP function implementation.

**AMDP function implementation**

The following listing shows the AMDP function implementation. The value of the return parameter is set to *Hello World!*.

``` abap
METHOD execute BY DATABASE FUNCTION 
               FOR HDB 
               LANGUAGE SQLSCRIPT 
               OPTIONS READ-ONLY. 
  result = 'Hello World!'; 
ENDMETHOD.
```

**Use in a CDS view entity**

The following CDS view entity uses the scalar function `DEMO_CDS_SCALAR_HELLOWORLD` as an element in the `SELECT` list.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, scalar func'

define view entity DEMO_CDS_SCALAR_USE
  as select from demo_expressions
{
  key id                           as Id,

      DEMO_CDS_SCALAR_HELLOWORLD() as MyScalarFunc
}
```

The following code snippet selects data from the CDS view entity `DEMO_CDS_SCALAR_USE`. The scalar function is executed and the field `MyScalarFunc` contains the value `Hello World!`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DELETE FROM demo_expressions. 
 
INSERT demo_expressions FROM @( VALUE #( id = 'X' ) ). 
 
SELECT * 
       FROM demo_cds_scalar_use 
       INTO TABLE @FINAL(result). 
 
out->write( result ). 
 
out->display( ).
```
