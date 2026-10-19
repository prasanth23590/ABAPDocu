---
title: "CDS DDL - DDIC-Based View, Unit and Currency Conversion Functions"
source_file: abencds_conv_func_unit_curr_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions > CDS DDL - DDIC-Based View, Built-In Functions > CDS DDL - DDIC-Based View, Special Functions > CDS DDL - DDIC-Based View, Conversion Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, Unit and Currency Conversion Functions

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
  | DECIMAL_SHIFT(      amount             => arg1, 
                        currency           => arg2[, 
                        error_handling     => arg3])  
```

### Variant

[1. `... UNIT_CONVERSION( ... )`](abencds_conv_func_unit_curr_v1.md#variant-1)

[2. `... CURRENCY_CONVERSION( ... )`](abencds_conv_func_unit_curr_v1.md#variant-2)

[3. `... DECIMAL_SHIFT( ... )`](abencds_conv_func_unit_curr_v1.md#variant-3)

## Overview

### Description

Functions for converting between units and between currencies [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). The functions have [keyword parameters](../../abap-glossary/abenkeyword_parameter_glosry.md) `quantity`, `amount`, ... (some of which are optional), to which actual parameters `arg1`, `arg2`, ... can or must be assigned when called using `=>`.

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
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">QUAN</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DEC</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT1</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT2</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">INT4</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">FLTP</code></a></td>
<td>Field of a <a href="abencds_data_source_v1.html">data source</a>, <a href="abencds_parameter_v1.html">parameter</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">source_unit</code></td>
<td><code class="ph codeph">-</code></td>
<td>Source currency from column <code class="ph codeph">MSEHI</code> of DDIC database table <code class="ph codeph">T006</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">UNIT</code></a></td>
<td>Field of a <a href="abencds_data_source_v1.html">data source</a>, <a href="abencds_expressions_v1.html">expression</a> that returns a suitable data type, <a href="abencds_parameter_v1.html">parameter</a></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">target_unit</code></td>
<td><code class="ph codeph">-</code></td>
<td>Target unit from column <code class="ph codeph">MSEHI</code> of DDIC database table <code class="ph codeph">T006</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">UNIT</code></a></td>
<td>Field of a <a href="abencds_data_source_v1.html">data source</a>, <a href="abencds_expressions_v1.html">expression</a> that returns a suitable data type, <a href="abencds_parameter_v1.html">parameter</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">client</code></td>
<td>X, <code class="ph codeph">-</code></td>
<td>Client whose rules are used to perform the unit conversion. Optional, if the current data source is client-dependent. Default: Content of the client column of the current row.</td>
<td><p>Field of a <a href="abencds_data_source_v1.html">data source</a>, <a href="abencds_literal_v1.html">literal</a>, <a href="abencds_parameter_v1.html">parameter</a>, <a href="abencds_session_var_builtin_v2.html">session variable</a>.</p>
<p>In <a href="abenabap_for_cloud_dev_glosry.html">ABAP for Cloud Development</a>, only the session variable <a href="abencds_session_variable_v1.html"><code class="ph codeph">$session.client</code></a> can be passed to <code class="ph codeph">client</code>.</p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CLNT</code></a>.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">error_handling</code></td>
<td>X</td>
<td>Error handling. If <em>FAIL_ON_ERROR</em> (default value), an error raises an exception; if <em>SET_TO_NULL</em>, the result is set to the <a href="abennull_value_glosry.html">null value</a>; if <em>KEEP_UNCONVERTED</em>, the source value is not changed.</td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a> with length 20</td>
<td><a href="abencds_literal_v1.html">Literal</a></td>
</tr>
</tbody>
</table>

The data type of the result depends on the data type of the formal parameter `quantity`:

- If `quantity` does not have a decimal floating point type, the result has the data type [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the length 31 and 14 decimal places.

- If `quantity` has data type `DECFLOAT16`, the result has data type `DECFLOAT16`.

- If `quantity` has data type `DECFLOAT34`, the result has data type `DECFLOAT34`.

### Hint

The precision of the result of the unit conversion depends on the database platform. The highest precision is achieved on databases that support [decimal floating point numbers](../../abap-glossary/abendecfloat_glosry.md). Due to rounding, the result can be different from a unit conversion performed using ABAP methods, such as a standard function module.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view calls a unit conversion in the `SELECT` list for the column `DEC3` of the DDIC database table `DEMO_EXPRESSIONS`. The source unit is a literal that is cast to the required type. The target unit must be passed as a parameter. In the event of an error, e.g. if a conversion between the entered units is impossible, the result is reset to null.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_UNTCNV'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_unit_conversion
  with parameters
    to_unit :abap.unit( 3 )
  as select from demo_expressions
{
  key id,
      dec3                                               as original_value,
      cast( 'MI' as abap.unit(3) )                       as original_unit,
      @Semantics.quantity.unitOfMeasure: 'converted_unit'
      unit_conversion( quantity => dec3,
                       source_unit => cast( 'MI' as abap.unit(3) ),
                       target_unit => :to_unit,
                       client      => $session.client,
                       error_handling => 'SET_TO_NULL' ) as converted_value,
      :to_unit                                           as converted_unit
}
```

The class `CL_DEMO_CDS_UNIT_CONVERSION` accesses the view in a `SELECT` statement. Here, the target unit is passed to the parameter in question. As a comparison, the same conversion is also performed using the function module `UNIT_CONVERSION_SIMPLE`. As prerequisite for the example, the units and their conversion rules must be available in the corresponding DDIC database tables.

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
<td>Field of a <a href="abencds_data_source_v1.html">data source</a>, <a href="abencds_parameter_v1.html">parameter</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">source_currency</code></td>
<td><code class="ph codeph">-</code></td>
<td>Source currency from column <code class="ph codeph">WAERS</code> of DDIC database table <code class="ph codeph">TCURC</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CUKY</code></a></td>
<td>Field of a <a href="abencds_data_source_v1.html">data source</a>, <a href="abencds_literal_v1.html">literal</a>, <a href="abencds_parameter_v1.html">parameter</a></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">target_currency</code></td>
<td><code class="ph codeph">-</code></td>
<td>Target currency from column <code class="ph codeph">WAERS</code> of DDIC database table <code class="ph codeph">TCURC</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CUKY</code></a></td>
<td>Field of a <a href="abencds_data_source_v1.html">data source</a>, <a href="abencds_literal_v1.html">literal</a>, <a href="abencds_parameter_v1.html">parameter</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">exchange_rate_date</code></td>
<td><code class="ph codeph">-</code></td>
<td>Exchange rate date for column <code class="ph codeph">GDATU</code> of DDIC database table <code class="ph codeph">TCURR</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">DATS</code></a></td>
<td>Field of a <a href="abencds_data_source_v1.html">data source</a>, <a href="abencds_literal_v1.html">literal</a>, <a href="abencds_parameter_v1.html">parameter</a></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">exchange_rate_type</code></td>
<td>X</td>
<td>Exchange rate type from column <code class="ph codeph">KURST</code> of DDIC database table <code class="ph codeph">TCURR</code>, default value: <em>M</em></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a> with length 4</td>
<td><a href="abencds_literal_v1.html">Literal</a>, <a href="abencds_parameter_v1.html">parameter</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">client</code></td>
<td>X, <code class="ph codeph">-</code></td>
<td>Client whose rules are used to perform the currency conversion. Optional, if the current data source is client-dependent. Default: Content of the client column of the current row. <a href="abenddic_builtin_types.html"><code class="ph codeph">CLNT</code></a></td>
<td><p>Field of a <a href="abencds_data_source_v1.html">data source</a>, <a href="abencds_literal_v1.html">literal</a>, <a href="abencds_parameter_v1.html">parameter</a>, <a href="abencds_session_var_builtin_v2.html">session variable</a>.</p>
<p>In <a href="abenabap_for_cloud_dev_glosry.html">ABAP for Cloud Development</a>, only the session variable <a href="abencds_session_variable_v2.html"><code class="ph codeph">$session.client</code></a> can be passed to <code class="ph codeph">client</code>.,</p></td>
<td></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">round</code></td>
<td>X</td>
<td>If <em>X</em> (default value), the intermediate result of the conversion is rounded to the end result using commercial rounding; else it is truncated</td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a></td>
<td><a href="abencds_literal_v1.html">Literal</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">decimal_shift</code></td>
<td>X</td>
<td><p>This formal parameter can only be used with data type <code class="ph codeph">CURR</code> for <code class="ph codeph">amount</code>.</p>
<p>If <em>X</em> (default value), the decimal places of the source value are moved as specified by the decimal places of the source currency (see below).</p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a></td>
<td><a href="abencds_literal_v1.html">Literal</a></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">decimal_shift_back</code></td>
<td>X</td>
<td><p>This formal parameter can only be used with data type <code class="ph codeph">CURR</code> for <code class="ph codeph">amount</code>.</p>
<p>If <em>X</em> (default value), the decimal places of the result are moved as specified by the decimal places of the target currency (see below).</p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a></td>
<td><a href="abencds_literal_v1.html">Literal</a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">error_handling</code></td>
<td>X</td>
<td>Error handling. If <em>FAIL_ON_ERROR</em> (default value), an error raises an exception; if <em>SET_TO_NULL</em>, the result is reset to the <a href="abennull_value_glosry.html">null value</a>; if <em>KEEP_UNCONVERTED</em>, the source value is not changed.</td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a> with length 20</td>
<td><a href="abencds_literal_v1.html">Literal</a></td>
</tr>
</tbody>
</table>

The input parameters `round`, `decimal_shift`, and `decimal_shift_back` accept the literals `'true'`, `'false'`, `'X'`, or `' '`. `#cdsboolean.true` and `#cdsboolean.false` with the domain prefix `CDSBOOLEAN` are also possible. Internally, these literals are handled like the values *X* or blank.

**Caution**

The literal values `'true'` and `'false'` (with and without domain prefix) are case-sensitive. Uppercase letters, such as `#cdsboolean.TRUE` and `#cdsboolean.FALSE`, are not valid input. No error message occurs, but these values are not considered valid input and unexpected behavior may occur.

**Handling the Decimal Places**

- The value passed is rounded to two decimal places before it is converted.

- Before the conversion, the value passed is multiplied by 10 to the power of the number of decimal places of the source currency.

- If the value *X* or *true* is passed to the parameter `decimal_shift`, the value passed is multiplied by 10 to the power of two minus the number of decimal places of the source currency before it is converted.

- If the value *X* or *true* is passed to the parameter `decimal_shift_back`, the result is divided by 10 to the power of two minus the number of decimal places of the target currency before it is converted.

- After the conversion, the result is divided by 10 to the power of the number of decimal places of the target currency.

### Hints

- The conversion is performed on the database, which means that part of the calculation takes place using different rounding rules from ABAP. No matter how the conversion is made, the same results cannot be expected as when using standard function modules for currency conversion, since these modules are generally less precise and round the intermediate results accordingly.

- The parameter `decimal_shift` is intended to set the source value to the number of decimal places of the source currency before the conversion. This assumes that its technical type, [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_currency_field.md), has two decimal places as usual. The parameter `decimal_shift_back` is intended to perform the reverse operation.

- If the technical type [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_currency_field.md) of the source value does not have two decimal places, the behavior of the `CURRENCY_CONVERSION` function can be unexpected.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view calls a currency conversion in the `SELECT` list for the column `AMOUNT` of the DDIC database table `DEMO_PRICES`. The target currency must be passed as a parameter. In the event of an error, e.g. when a currency is not available, the result is reset to zero.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_CURRCO'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_curr_conv
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
                           target_currency => :to_currency,
                           exchange_rate_date => :exc_date,
                           client => $session.client,
                           error_handling => 'SET_TO_NULL' ) as amount,
      :to_currency                                           as currency
}
```

The class `CL_DEMO_CDS_CURRENCY_CNVRSN` accesses the view in a `SELECT` statement. The target currency is passed here. As a comparison, the same conversion is also performed using the function module `CONVERT_TO_LOCAL_CURRENCY`. As prerequisite for the example, the currencies and conversion rules must be available in the corresponding DDIC database tables.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In class `CL_DEMO_CDS_FUNC_CURR_CONV`, the above CDS view is used in a subquery of an ABAP SQL `MODIFY` statement.

``` abap
DATA currency TYPE c LENGTH 5 VALUE 'USD'. 
 
... 
 
MODIFY demo_prices FROM 
  ( SELECT id, amount, currency 
           FROM demo_cds_curr_conv( 
                  to_currency = @currency, 
                  exc_date = @( cl_demo_date_time=>get_user_date( ) ) ) 
           ORDER BY id )  ##null_values.
```

## Variant 3

`... DECIMAL_SHIFT( ... )`

### Description

The function `DECIMAL_SHIFT` sets the decimal separator of the value that is passed to the keyword parameter `amount` in accordance with a currency. The result has the data type [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the length 31 and 14 decimal places. Its value is produced by multiplying the input parameter rounded to two decimal places by 10 to the power of two minus the decimal places defined by the currency passed.

Possible currencies and their decimal places are based on the database tables `TCUR...` of the package `SFIB`.

| **Formal Parameter** | **Optional** | **Meaning**                                                                                                                                                                                                                      | **Data Type**                                        | **Actual Parameter `arg`**                                                                                                        |
|----------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| `amount`             | `-`          | Inbound value                                                                                                                                                                                                                    | [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                | Field of a [data source](abencds_data_source_v1.md), [parameter](abencds_parameter_v1.md)                                     |
| `currency`           | `-`          | Currency from column `WAERS` of DDIC database table `TCURC`; the associated decimal places determined from the column `CURRDEC` of `TCURX`                                                                                       | [`CUKY`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                | Field of a [data source](abencds_data_source_v1.md), [literal](abencds_literal_v1.md), [parameter](abencds_parameter_v1.md) |
| `error_handling`     | X            | Error handling. If *FAIL_ON_ERROR* (default value), an error raises an exception; if *SET_TO_NULL*, the result is reset to the [null value](../../abap-glossary/abennull_value_glosry.md); if *KEEP_UNCONVERTED*, the source value is not changed. | [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 20 | [Literal](abencds_literal_v1.md)                                                                                                |

### Hint

If the type of the actual parameter passed to `amount` has two decimal places, its value is set to the number of decimal places of the passed currency.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the `SELECT` list, the following CDS view sets the decimal separator for column `AMOUNT` of DDIC database table `DEMO_PRICES` to between 0 and 5, according to the relevant currency. The column `AMOUNT` has two decimal places, which means that the decimal places are determined directly by the passed currencies. In the event of an error, e.g. when a currency is not available, the result is reset to zero.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_DCSHFT'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_decimal_shift
  as select from demo_prices
{
  key id,
      @Semantics.amount.currencyCode:'currency'
      amount                                           as original,
      @Semantics.currencyCode
      currency,
      decimal_shift( amount => amount,
                     currency => cast( '0 ' as abap.cuky(5) ),
                     error_handling => 'SET_TO_NULL' ) as shift_0,
      decimal_shift( amount => amount,
                     currency => cast( '1 ' as abap.cuky(5) ),
                     error_handling => 'SET_TO_NULL' ) as shift_1,
      decimal_shift( amount => amount,
                     currency => cast( '2 ' as abap.cuky(5) ),
                     error_handling => 'SET_TO_NULL' ) as shift_2,
      decimal_shift( amount => amount,
                     currency => cast( '3 ' as abap.cuky(5) ),
                     error_handling => 'SET_TO_NULL' ) as shift_3,
      decimal_shift( amount => amount,
                     currency => cast( '4 ' as abap.cuky(5) ),
                     error_handling => 'SET_TO_NULL' ) as shift_4,
      decimal_shift( amount => amount,
                     currency => cast( '5 ' as abap.cuky(5) ),
                     error_handling => 'SET_TO_NULL' ) as shift_5
}
```

The class `CL_DEMO_CDS_DECIMAL_SHIFT` accesses the view in a `SELECT` statement. As prerequisite for the example, the currencies and their number of decimal places must be available in the corresponding DDIC database tables.
