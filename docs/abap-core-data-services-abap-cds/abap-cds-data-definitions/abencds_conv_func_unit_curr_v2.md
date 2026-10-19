---
title: "CDS DDL - CDS View Entity, Unit and Currency Conversion Functions"
source_file: abencds_conv_func_unit_curr_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions > CDS DDL - CDS View Entity, Built-In Functions > CDS DDL - CDS View Entity, Special Functions > CDS DDL - CDS View Entity, Conversion Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, Unit and Currency Conversion Functions

## Syntax

``` abap
... UNIT_CONVERSION(    quantity           => arg1, 
                        source_unit        => arg2, 
                        target_unit        => arg3[, 
                        client             => arg4][, 
                        error_handling     => arg5]) 
  | CURRENCY_CONVERSION(amount             => arg1, 
                        source_currency    => arg2, 
                        target_currency    => arg3, 
                        exchange_rate_date => arg4[, 
                        exchange_rate_type => arg5][, 
                        client             => arg6][, 
                        round              => arg7][, 
                        decimal_shift      => arg8][, 
                        decimal_shift_back => arg9][, 
                        error_handling     => arg10]) 
  | GET_NUMERIC_VALUE( arg ) 
  | CURR_TO_DECFLOAT_AMOUNT( arg ) ...  
```

### Variant

[1. `... UNIT_CONVERSION( ... )`](abencds_conv_func_unit_curr_v2.md#variant-1)

[2. `... CURRENCY_CONVERSION( ... )`](abencds_conv_func_unit_curr_v2.md#variant-2)

[3. `... GET_NUMERIC_VALUE( arg )`](abencds_conv_func_unit_curr_v2.md#variant-3)

[4. `... CURR_TO_DECFLOAT_AMOUNT( arg )`](abencds_conv_func_unit_curr_v2.md#variant-4)

## Overview

### Description

Functions for converting between units and between currencies in a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md).

The functions `UNIT_CONVERSION` and `CURRENCY_CONVERSION` have [keyword parameters](../../abap-glossary/abenkeyword_parameter_glosry.md) `quantity`, `source_unit`, ... (some of which are optional), to which actual parameters `arg1`, `arg2`, ... can or must be assigned when called using `=>`.

The functions `GET_NUMERIC_VALUE` and `CURR_TO_DECFLOAT_AMOUNT` each have one mandatory [positional parameter](../../abap-glossary/abenpositional_parameter_glosry.md) `arg`.

### Hint

The function `DECIMAL_SHIFT` is currently not supported in [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md).

## Variant 1

`... UNIT_CONVERSION( ... )`

### Description

The function `UNIT_CONVERSION` performs a unit conversion for the value passed to the keyword parameter `quantity`.

The unit conversion is performed on the basis of the client-dependent rules saved in the DDIC database tables `T006...` of the package `SZME`.

The table below shows all available keyword parameters and their meaning.

<table>
<thead>
<tr class="header">
<th><strong>Formal Parameter</strong></th>
<th><strong>Optional</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>Data Type</strong></th>
<th><strong>Actual Parameter <code class="ph codeph">arg</code></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">quantity</code></td>
<td><code class="ph codeph">-</code></td>
<td>Inbound value</td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">QUAN</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DEC</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT1</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT2</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT4</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DECFLOAT16</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DECFLOAT34</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">FLTP</code></a></td>
<td><a href="abencds_literal_v2.html">Literal</a>, field of a <a href="abencds_data_source_v2.html">data source</a>, <a href="abencds_parameter_v2.html">parameter</a>, <a href="abencds_expressions_v2.html">expression</a>, <a href="abencds_sql_scalar_function.html">SQL-based scalar function</a>, <a href="abencds_path_expression_v2.html">path expression</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">source_unit</code></td>
<td><code class="ph codeph">-</code></td>
<td>Source currency from column <code class="ph codeph">MSEHI</code> of DDIC database table <code class="ph codeph">T006</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">UNIT</code></a></td>
<td>Field of a <a href="abencds_data_source_v2.html">data source</a>, <a href="abencds_parameter_v2.html">parameter</a>, <a href="abencds_case_expression_v2.html">case distinction</a>, <a href="abencds_cast_expression_v2.html">cast expression</a>, <a href="abencds_path_expression_v2.html">path expression</a>, <a href="abencds_sql_scalar_function.html">SQL-based scalar function</a></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">target_unit</code></td>
<td><code class="ph codeph">-</code></td>
<td>Target unit from column <code class="ph codeph">MSEHI</code> of DDIC database table <code class="ph codeph">T006</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">UNIT</code></a></td>
<td>Field of a <a href="abencds_data_source_v2.html">data source</a>, <a href="abencds_parameter_v2.html">parameter</a>, <a href="abencds_case_expression_v2.html">case distinction</a>, <a href="abencds_cast_expression_v2.html">cast expression</a>, <a href="abencds_path_expression_v2.html">path expression</a>, <a href="abencds_sql_scalar_function.html">SQL-based scalar function</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">client</code></td>
<td><em>X</em>, <code class="ph codeph">-</code></td>
<td><p>Client whose rules are used to perform the unit conversion. Since client handling takes place implicitly for CDS view entities, it is not possible to explicitly specify any client column as actual parameter. For client-dependent sources, there are two options:</p>
<p>- either, the parameter can be left out and the client column is implicitly added, or</p>
<p>- the actual parameter can be specified as expression, literal, or session variable (but not as field of a data source).</p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CLNT</code></a></td>
<td><p><a href="abencds_expressions_v2.html">Expression</a>, <a href="abencds_sql_scalar_function.html">SQL-based scalar function</a>, <a href="abencds_literal_v2.html">literal</a>, <a href="abencds_session_variable_v2.html">session variable</a></p>
<p>In <a href="abenabap_for_cloud_dev_glosry.html">ABAP for Cloud Development</a>, only the session variable <a href="abencds_session_variable_v2.html"><code class="ph codeph">$session.client</code></a> can be passed to <code class="ph codeph">client</code>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">error_handling</code></td>
<td><em>X</em></td>
<td><p>Error handling.</p>
<p><code class="ph codeph">'FAIL_ON_ERROR'</code>: an error raises an exception (default)</p>
<p><code class="ph codeph">'SET_TO_NULL'</code>: the result is set to the <a href="abennull_value_glosry.html">null value</a></p>
<p><code class="ph codeph">'KEEP_UNCONVERTED'</code>: the source value is not changed.</p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a> with length 20</td>
<td><a href="abencds_literal_v2.html">Literal</a></td>
</tr>
</tbody>
</table>

The data type of the result depends on the data type of the formal parameter `quantity`:

- If `quantity` has data type `QUAN`, `DEC`, `INT1`, `INT2`, `INT4`, or `FLTP`, the result has data type `QUAN` with the length 31 and 14 decimal places.

- If `quantity` has data type `DECFLOAT16`, the result has data type `DECFLOAT16`.

- If `quantity` has data type `DECFLOAT34`, the result has data type `DECFLOAT34`.

### Hint

The precision of the result of the unit conversion depends on the database platform. The highest precision is achieved on databases that support [decimal floating point numbers](../../abap-glossary/abendecfloat_glosry.md). Due to rounding, the result can be different from a unit conversion performed using ABAP methods, such as a standard function module.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity calls a unit conversion in the `SELECT` list for the column `DEC3` of the DDIC database table `DEMO_EXPRESSIONS`. The source unit is specified using a typed literal. The target unit must be passed as a parameter. In the event of an error, for example if a conversion between the entered units is impossible, the result is set to null.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_UNIT_CONVERSION_VE
  with parameters
    to_unit :abap.unit( 3 )
  as select from demo_expressions
{
  key id,
      dec3                                              as original_value,
      abap.unit'MI'                                     as original_unit,
      @Semantics.quantity.unitOfMeasure: 'converted_unit'
      unit_conversion( quantity => dec3,
                      source_unit => abap.unit'MI',
                      target_unit => $parameters.to_unit,
                      client      => $session.client,
                      error_handling => 'SET_TO_NULL' ) as converted_value,
      $parameters.to_unit                               as converted_unit
}
```

The class `CL_DEMO_CDS_UNIT_CONVERSION_VE` accesses the view in a `SELECT` statement. The target unit is passed to the respective formal parameter. As a comparison, the same conversion is also performed using the function module `UNIT_CONVERSION_SIMPLE`. As prerequisite for the example, the units and their conversion rules must be available in the corresponding DDIC database tables.

## Variant 2

`... CURRENCY_CONVERSION( ... )`

### Description

The function `CURRENCY_CONVERSION` performs a currency conversion for the value passed to the keyword parameter `amount`. The result has the data type [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`DECFLOAT34`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the same technical properties as the actual parameter passed to `amount`. The currency conversion is performed on the basis of the client-dependent rules saved in the DDIC database tables `TCUR...` of package `SFIB`.

The table below shows all available keyword parameters and their meaning.

<table>
<thead>
<tr class="header">
<th><strong>Formal Parameter</strong></th>
<th><strong>Optional</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>Data Type</strong></th>
<th><strong>Actual Parameter <code class="ph codeph">arg</code></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">amount</code></td>
<td><code class="ph codeph">-</code></td>
<td>Inbound value</td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CURR</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DECFLOAT34</code></a></td>
<td>Field of a <a href="abencds_data_source_v2.html">data source</a>, <a href="abencds_parameter_v2.html">parameter</a>, <a href="abencds_sql_scalar_function.html">SQL-based scalar function</a>, <a href="abencds_expressions_v2.html">expression</a>, <a href="abencds_path_expression_v2.html">path expression</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">source_currency</code></td>
<td><code class="ph codeph">-</code></td>
<td>Source currency from column <code class="ph codeph">WAERS</code> of DDIC database table <code class="ph codeph">TCURC</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CUKY</code></a></td>
<td>Field of a <a href="abencds_data_source_v2.html">data source</a>, <a href="abencds_sql_scalar_function.html">SQL-based scalar function</a>, <a href="abencds_cast_expression_v2.html">cast expression</a>, <a href="abencds_path_expression_v2.html">path expression</a>, <a href="abencds_parameter_v2.html">parameter</a></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">target_currency</code></td>
<td><code class="ph codeph">-</code></td>
<td>Target currency from column <code class="ph codeph">WAERS</code> of DDIC database table <code class="ph codeph">TCURC</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CUKY</code></a></td>
<td>Field of a <a href="abencds_data_source_v2.html">data source</a>, <a href="abencds_sql_scalar_function.html">SQL-based scalar function</a>, <a href="abencds_cast_expression_v2.html">cast expression</a>, <a href="abencds_path_expression_v2.html">path expression</a>, <a href="abencds_parameter_v2.html">parameter</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">exchange_rate_date</code></td>
<td><code class="ph codeph">-</code></td>
<td>Exchange rate date for column <code class="ph codeph">GDATU</code> of DDIC database table <code class="ph codeph">TCURR</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">DATS</code></a></td>
<td>Field of a <a href="abencds_data_source_v2.html">data source</a>, <a href="abencds_literal_v2.html">literal</a>, <a href="abencds_parameter_v2.html">parameter</a>, <a href="abencds_sql_scalar_function.html">SQL-based scalar function</a>, <a href="abencds_path_expression_v2.html">path expression</a>.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">exchange_rate_type</code></td>
<td><em>X</em></td>
<td>Exchange rate type from column <code class="ph codeph">KURST</code> of DDIC database table <code class="ph codeph">TCURR</code>, default value: <code class="ph codeph">'M'</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a> with length 4</td>
<td><a href="abencds_literal_v2.html">Literal</a>, <a href="abencds_parameter_v2.html">parameter</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">client</code></td>
<td><em>X</em>, <code class="ph codeph">-</code></td>
<td><p>Client whose rules are used to perform the currency conversion. Since client handling takes place implicitly for CDS view entities, it is not possible to explicitly specify any client column as actual parameter. For client-dependent sources, there are two options:</p>
<p>- either, the parameter can be left out and the client column is implicitly added, or</p>
<p>- the actual parameter can be specified as expression, literal, or session variable (but not as field of a data source).</p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CLNT</code></a></td>
<td><p><a href="abencds_expressions_v2.html">Expression</a>, <a href="abencds_sql_scalar_function.html">SQL-based scalar function</a>, <a href="abencds_literal_v2.html">literal</a>, <a href="abencds_session_variable_v2.html">session variable</a></p>
<p>In <a href="abenabap_for_cloud_dev_glosry.html">ABAP for Cloud Development</a>, only the session variable <a href="abencds_session_variable_v2.html"><code class="ph codeph">$session.client</code></a> can be passed to <code class="ph codeph">client</code>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">round</code></td>
<td><em>X</em></td>
<td>If <em>X</em> (default value), the intermediate result of the conversion is rounded to the end result using commercial rounding; else it is truncated</td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a></td>
<td><a href="abencds_literal_v2.html">Literal</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">decimal_shift</code></td>
<td><em>X</em></td>
<td><p>This formal parameter can only be used with data type <code class="ph codeph">CURR</code> for <code class="ph codeph">amount</code>.</p>
<p>If <em>X</em> (default value), the decimal places of the source value are moved as specified by the decimal places of the source currency (see below).</p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a></td>
<td><a href="abencds_literal_v2.html">Literal</a></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">decimal_shift_back</code></td>
<td><em>X</em></td>
<td><p>This formal parameter can only be used with data type <code class="ph codeph">CURR</code> for <code class="ph codeph">amount</code>.</p>
<p>If <code class="ph codeph">'X'</code> (default value), the decimal places of the result are moved as specified by the decimal places of the target currency (see below).</p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a></td>
<td><a href="abencds_literal_v2.html">Literal</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">error_handling</code></td>
<td><em>X</em></td>
<td>Error handling. If <code class="ph codeph">'FAIL_ON_ERROR'</code> (default value), an error raises an exception; if <code class="ph codeph">'SET_TO_NULL'</code>, the result is set to the <a href="abennull_value_glosry.html">null value</a>; if <code class="ph codeph">'KEEP_UNCONVERTED'</code>, the source value is not changed.</td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a> with length 20</td>
<td><a href="abencds_literal_v2.html">Literal</a></td>
</tr>
</tbody>
</table>

The input parameters `round`, `decimal_shift`, and `decimal_shift_back` accept the literals `'true'`, `'false'`, `'X'`, or `' '`. `#cdsboolean.true` and `#cdsboolean.false` with the domain prefix `CDSBOOLEAN` are also possible. Internally, these literals are handled like the values *X* or blank.

**Caution**

The literal values `'true'` and `'false'` (with and without domain prefix) are case-sensitive. Uppercase letters, such as `#cdsboolean.TRUE` and `#cdsboolean.FALSE`, are not valid input. No error message occurs, but these values are not considered valid input and unexpected behavior may occur.

**Handling the Decimal Places**

- The inbound value is rounded to two decimal places before it is converted.

- Before the conversion, the value passed is multiplied by 10 to the power of the number of decimal places of the source currency.

- If the value 'X' or `'true'` is passed to the parameter `decimal_shift`, the value passed is multiplied by 10 to the power of two minus the number of decimal places of the source currency before it is converted.

- If the value 'X' or `'true'` is passed to the parameter `decimal_shift_back`, the result is divided by 10 to the power of two minus the number of decimal places of the target currency after the conversion.

- After the conversion, the result is divided by 10 to the power of the number of decimal places of the target currency.

### Hints

- The conversion is performed on the database, which means that part of the calculation takes place using different rounding rules from ABAP. The results might differ from the results returned when using standard function modules for currency conversion, since these modules are generally less precise and round the intermediate results accordingly.

- The parameter `decimal_shift` is intended to set the source value to the number of decimal places of the source currency before the conversion. This assumes that its technical type, [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_currency_field.md), has two decimal places as usual. The parameter `decimal_shift_back` is intended to perform the reverse operation.

- If the technical type [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_currency_field.md) of the source value does not have two decimal places, the behavior of the `CURRENCY_CONVERSION` function can be unexpected.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity performs a currency conversion in the `SELECT` list for the column `AMOUNT` of the DDIC database table `DEMO_PRICES`. The target currency must be passed as a parameter. In the event of an error, for example, when a currency is not available, the result is set to zero.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_CURR_CONV_VE
  with parameters
    to_currency :abap.cuky( 5 ),
    exc_date    :abap.dats
  as select from demo_prices
{
  key id,
      @Semantics.amount.currencyCode: 'currency'
      currency_conversion( amount => amount,
                          source_currency => currency,
                          round =>  'X',
                          target_currency => $parameters.to_currency,
                          exchange_rate_date => $parameters.exc_date,
                          error_handling => 'SET_TO_NULL' ) as amount,
      $parameters.to_currency                               as currency
}
```

The class `CL_DEMO_CDS_CURRENCY_CONV_VE` accesses the view in a `SELECT` statement, passing the target currency. As a comparison, the same conversion is also performed using the function module `CONVERT_TO_LOCAL_CURRENCY`. As prerequisite for the example, the currencies and conversion rules must be available in the corresponding DDIC database tables.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In class `CL_DEMO_CDS_FUNC_CURR_CONV_VE`, the above CDS view entity is used in a subquery of an ABAP SQL `MODIFY` statement.

``` abap
DATA currency TYPE c LENGTH 5 VALUE 'USD'. 
 
... 
 
MODIFY demo_prices FROM 
  ( SELECT id, amount, currency 
           FROM demo_cds_curr_conv_ve( 
                  to_currency = @currency, 
                  exc_date = @( cl_demo_date_time=>get_user_date( ) ) ) 
           ORDER BY id )  ##null_values.
```

## Variant 3

`... GET_NUMERIC_VALUE( arg )`

### Description

`GET_NUMERIC_VALUE` returns the numeric value of a [currency](../../abap-glossary/abencurrency_field_glosry.md) or [quantity](../../abap-glossary/abenquantity_glosry.md) field without its [currency](../../abap-glossary/abencurrency_key_glosry.md) or [unit](../../abap-glossary/abenunit_glosry.md) key. `arg` must be a [field of a data source](abencds_field_v2.md). No other [elementary operand](abencds_operands_v2.md), [expression](abencds_expressions_v2.md), or [function](abencds_builtin_functions_v2.md) is possible. The argument `arg` can have any data type that supports reference annotations, namely: `INT1`, `INT2`, `INT4`, `DEC`, `FLTP`, `DECFLOAT16`, `DECFLOAT34`, `CURR`, or `QUAN`. The result of the function `GET_NUMERIC_VALUE` has data type `DECFLOAT34` and it has no reference information assigned. That means that no currency or unit key is assigned.

### Hint

If `arg` has data type `CURR`, an implicit decimal shift takes place.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity applies the function `GET_NUMERIC_VALUE` to calculate the number of bookings. It divides the total value of current bookings (field `paymentsum`) by the price of a flight (field `price`). This would not be possible without the function `GET_NUMERIC_VALUE`, since elements of data type `CURR` are not allowed in [arithmetic expressions](abencds_arithmetic_expression_v2.md).

Details on the elements:

- `paymentsum` has data type `CURR`, a reference annotation that assigns a currency key, and it contains the total value of current bookings.

- `price` has data type `CURR`, a reference annotation that assigns a currency key, and it contains the price of a flight.

- `number_of_bookings` has data type `DECFLOAT34` and it has no currency key assigned.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, GET_NUMERIC_VALUE'
@Metadata.ignorePropagatedAnnotations: true

define view entity DEMO_CDS_GET_NUMERIC_VALUE
  as select from sflight
{
  key carrid,
  key connid,
  key fldate,
      @Semantics.amount.currencyCode: 'currency'
      price,
      currency,
      @Semantics.amount.currencyCode: 'currency'
      paymentsum,
      get_numeric_value( paymentsum )
        / get_numeric_value( price ) as number_of_bookings
}
```

The class `CL_DEMO_CDS_GET_NUMERIC_VALUE` accesses the view and performs the following steps:

- It displays the element annotations of `price`. One of them is the `Semantics.amount.currencyCode` annotation that assigns a currency key.

- It displays the element annotations of `number_of_bookings`. This field does not have any annotations.

- It displays the structure of the CDS view entity. The element `number_of_bookings` has type *e*, which corresponds to the built-in DDIC type `DECFLOAT34`.

## Variant 4

`... CURR_TO_DECFLOAT_AMOUNT( arg )`

### Description

The function `CURR_TO_DECFLOAT_AMOUNT` converts a [currency field](../../abap-glossary/abencurrency_field_glosry.md) of data type `CURR` into a [currency field](../../abap-glossary/abencurrency_field_glosry.md) of data type `DECFLOAT34`. `arg` must have data type `CURR` and a [currency key](../../abap-glossary/abencurrency_key_glosry.md) must be assigned using the annotation [`Semantics.amount.currencyCode`](abencds_f1_element_annotation.md). The result has the data type [`DECFLOAT34`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and exactly the same currency key that is assigned to `arg` must be assigned.

### Hint

This functions performs an implicit decimal shift.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity demonstrates the `CURR_TO_DECFLOAT_AMOUNT` function. Field `curr10_4` is converted from data type `CURR` to data type `DECFLOAT34`. The source and the target field require a currency key assignment.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, CURR_TO_DEC'

define view entity DEMO_CDS_CURR_TO_DEC
  as select from demo_ddic_types
{
  key id,
      cuky                              as currency,
      @Semantics.amount.currencyCode: 'currency'
      curr10_4                          as amount,
      @Semantics.amount.currencyCode: 'currency'
      curr_to_decfloat_amount(curr10_4) as curr_conv
}
```

The class `CL_DEMO_CDS_CURR_TO_DEC` accesses the view and performs the following steps:

- It displays all element annotations of the view `DEMO_CDS_CURR_TO_DEC`. Both source and target field have a currency key assigned.

- It evaluates the components of the CDS view entity. The element `curr_conv` has type `e`, which corresponds to the built-in DDIC type `DECFLOAT34`.
