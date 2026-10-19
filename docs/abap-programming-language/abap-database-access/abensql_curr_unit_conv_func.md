---
title: "sql_func - Unit and Currency Conversion Functions"
source_file: abensql_curr_unit_conv_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - Special Functions > sql_func - Conversion Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Unit and Currency Conversion Functions

## Syntax

``` abap
... UNIT_CONVERSION( p1 = a1, p2 = a2, ... ) 
|   CURRENCY_CONVERSION( p1 = a1, p2 = a2, ... ) ...  
```

### Variant

[1. `... UNIT_CONVERSION( p1 = a1, p2 = a2, ... )`](abensql_curr_unit_conv_func.md#variant-1)

[2. `... CURRENCY_CONVERSION( p1 = a1, p2 = a2, ... )`](abensql_curr_unit_conv_func.md#variant-2)

## Overview

### Description

Functions for converting between units and between currencies in an ABAP SQL statement. The functions have [keyword parameters](../../abap-glossary/abenkeyword_parameter_glosry.md) `p1`, `p2`, ... (some of which are optional), to which actual parameters `a1`, `a2`, ... must be assigned using `=` when a function is called.

## Variant 1

`... UNIT_CONVERSION( p1 = a1, p2 = a2, ... )`

### Description

The function `UNIT_CONVERSION` performs a unit conversion for the value passed to the formal parameter `quantity`. The result has the same data type as the formal parameter passed to `quantity`.

The table below shows the actual parameters `p1`, `p2`, ... and their meaning.

| **Formal Parameter** | **Optional** | **Meaning**                                                                                                                                                                                                                   | **Data Type**                                                                                                                                                   | **Actual Parameter**                                         |
|----------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| `quantity`           | `-`          | Inbound value                                                                                                                                                                                                                 | [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md); [`DECFLOAT34`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) | [SQL expression](abapsql_expr.md)                          |
| `on_error`           | *X*          | Error handling. If `fail` (default value), an error raises an exception; if `set_to_null`, the result is reset to the [null value](../../abap-glossary/abennull_value_glosry.md); if `keep_unconverted`, the result is reset to the input value | [Enumerated type](../../abap-glossary/abenenumerated_type_glosry.md) `ON_ERROR` of class `SQL_UNIT_CONVERSION`                                                                    | Allowed [enumerated value](../../abap-glossary/abenenumerated_value_glosry.md) |

Another optional parameter `client` must not be used in ABAP for Cloud Development.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The `SELECT` statement calls a unit conversion in its `SELECT` list for the column `DEC3` of the DDIC database table `DEMO_EXPRESSIONS`. In the event of an error, for example when a unit is not available, the result is reset to the null value.

``` abap
DELETE FROM demo_expressions. 
 
DATA wa TYPE demo_expressions. 
wa = VALUE #( dec3 = `2.213` ). 
 
INSERT INTO demo_expressions VALUES @wa. 
 
SELECT FROM demo_expressions 
  FIELDS dec3, 
         unit_conversion( 
          quantity = dec3, 
          source_unit = unit`MI`, 
          target_unit = unit`KM`, 
          on_error = @sql_unit_conversion=>c_on_error-set_to_null ) 
         AS actual_target_quantity 
  INTO TABLE @DATA(actual_target_unit). 
 
cl_demo_output=>display( actual_target_unit ).
```

## Variant 2

`... CURRENCY_CONVERSION( p1 = a1, p2 = a2, ... )`

### Description

The function `CURRENCY_CONVERSION` performs a currency conversion for the value passed to the formal parameter `amount`. The result has the same data type as the formal parameter passed to `amount`.

The table below shows the actual parameters `p1`, `p2`, ... and their meaning.

| **Formal Parameter** | **Optional** | **Meaning**                                                                                                                                                                              | **Data Type**                                                                                                                                                                           | **Actual Parameter**                                                                       |
|----------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| `amount`             | `-`          | Inbound value                                                                                                                                                                            | [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with two decimal places; [`DECFLOAT34`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) | [SQL expression](abapsql_expr.md)                                                        |
| `round`              | *X*          | Not possible for amount type `D34N`; if *X* (default value), the intermediate result of the conversion is rounded to the end result using commercial rounding; otherwise it is truncated | ABAP type `c` of length 1                                                                                                                                                               | [Literal](abenabap_sql_literals.md) or [host constant](abenabap_sql_host_variables.md) |
| `decimal_shift`      | *X*          | Not possible for amount type `D34N`; if *X* (default value), the decimal places of the source value are moved as specified by the decimal places of the source currency (see below).     | ABAP type `c` of length 1                                                                                                                                                               | [Literal](abenabap_sql_literals.md) or [host constant](abenabap_sql_host_variables.md) |
| `decimal_shift_back` | *X*          | Not possible for amount type `D34N`; if *X* (default value), the decimal places of the result are moved as specified by the decimal places of the target currency (see below).           | ABAP type `c` of length 1                                                                                                                                                               | [Literal](abenabap_sql_literals.md) or [host constant](abenabap_sql_host_variables.md) |
| `on_error`           | *X*          | Error handling. If `fail` (default value), an error raises an exception; if `set_to_null`, the result is reset to the [null value](../../abap-glossary/abennull_value_glosry.md)                           | [Enumerated type](../../abap-glossary/abenenumerated_type_glosry.md) `ON_ERROR` of class `SQL_CURRENCY_CONVERSION`                                                                                        | Allowed [enumerated value](../../abap-glossary/abenenumerated_value_glosry.md)                               |

Another optional parameter `client` must not be used in ABAP for Cloud Development.

**Handling the Decimal Places**

- The value passed is rounded to two decimal places before it is converted.

- Before the conversion, the value is multiplied by 10 to the power of the number of decimal places of the source currency.

- If the value *X* is passed to the parameter `decimal_shift`, the value passed is multiplied by 10 to the power of two minus the number of decimal places of the source currency before it is converted.

- If the value *X* is passed to the parameter `decimal_shift_back`, the result is divided by 10 to the power of two minus the number of decimal places of the target currency before it is converted.

- After the conversion, the result is divided by 10 to the power of the number of decimal places of the target currency.

### Hints

- The conversion is performed on the database, which means that part of the calculation takes place using different rounding rules from ABAP. No matter how the conversion is made, the same results cannot be expected as when using standard function modules for currency conversion, since these modules are generally less precise and round the intermediate results accordingly.

- The parameter `decimal_shift` is intended to set the source value to the number of decimal places of the source currency before the conversion. Because of that, its technical type, [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_currency_field.md) must have two decimal places. The parameter `decimal_shift_back` is intended to perform the reverse operation.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following is an excerpt of the class `CL_DEMO_ASQL_CURRENCY_CNVRSN`. The `SELECT` statement calls a currency conversion in its `SELECT` list for the column `AMOUNT` of the DDIC database table `DEMO_PRICES`. The target currency is passed as a host variable. In the event of an error, for example when a currency is not available, an exception is raised. As a comparison, the same conversion is also performed using the function module `CONVERT_TO_LOCAL_CURRENCY`. As a prerequisite for the example, the currencies and conversion rules must be available in the corresponding DDIC database tables.

``` abap
DATA currency TYPE c LENGTH 5 VALUE 'USD'. 
 
... 
 
SELECT FROM demo_prices 
       FIELDS id, 
              currency_conversion( 
                amount = amount, 
                source_currency = currency, 
                target_currency = @currency, 
                exchange_rate_date = @( 
                  cl_demo_date_time=>get_user_date( ) ), 
                round = 'X', 
                on_error = 
                  @sql_currency_conversion=>c_on_error-fail ) 
                    AS amount, 
                @currency AS currency 
        INTO TABLE @FINAL(converted_prices_asql). 
 
cl_demo_output=>display( converted_prices_asql ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the class `CL_DEMO_ASQL_FUNC_CURR_CONV`, the SQL function `CURRENCY_CONVERSION` is used in a subquery of a `MODIFY` statement.

``` abap
DATA currency TYPE c LENGTH 5 VALUE 'USD'. 
 
... 
 
MODIFY demo_prices FROM 
  ( SELECT FROM demo_prices 
           FIELDS id, 
                  currency_conversion( 
                    amount = amount, 
                    source_currency = currency, 
                    target_currency = @currency, 
                    exchange_rate_date = 
                      @( cl_demo_date_time=>get_user_date( ) ), 
                    on_error = 
                    @sql_currency_conversion=>c_on_error-fail ) 
                      AS amount, 
                    @currency  AS currency 
            ORDER BY id ).
```
