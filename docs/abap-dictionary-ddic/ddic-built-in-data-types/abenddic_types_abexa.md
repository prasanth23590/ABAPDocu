---
title: "DDIC - Built-In Dictionary Types"
source_file: abenddic_types_abexa.html
section: "ABAP Dictionary (DDIC) > DDIC - Built-In Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Built-In Dictionary Types

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates valid literal values for all [built-in dictionary types](abenddic_builtin_types.md).

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_ddic_types DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_ddic_types IMPLEMENTATION. 
  METHOD main. 
    DELETE FROM demo_ddic_types.                        "#EC CI_NOWHERE 
    INSERT demo_ddic_types FROM @( VALUE #( id = 'X' 
      int1          = 255 
      int2          = 32767 
      int4          = 2147483647 
      int8          = 9223372036854775807 
      dec10         = 1234567890 
      dec10_2       = '12345678.90' 
      dec20         = 12345678901234567890 
      dec20_4       = '1234567890123456.7890' 
      d16n          = '1234567890123456E10' 
      df16_dec      = '1.23456789012345' 
      df16_raw      = '1234567890123456' 
      d34n          = '1234567890123456789012345678901234E10' 
      df34_dec      = '1234567890123456.78901234567890' 
      df34_raw      = '1234567890123456789012345678901234' 
      fltp          = '-.15e-3' 
      char1         = 'a' 
      char10        = 'abcdefghij' 
      sstring256    = 'abcdefghijklmnopqrstuvwxyz' 
      sstring512    = 'abcdefghijklmnopqrstuvwxyz' 
      string        = 'abcdefghijklmnopqrstuvwxyz' 
      raw1          = 'FF' 
      raw10         = '00112233445566778899' 
      rawstring     = '00112233445566778899AABBCCDDEEFF' 
      dats          = '20200720' 
      tims          = '162345' 
      datn          = '20200720' 
      timn          = '162345' 
      utcl          = '2020-07-20 16:23:45' 
      accp          = '202007' 
      numc1         = '1' 
      numc10        = '0123456789' 
      clnt          = '000' 
      lang          = 'E' 
      curr10_2      = '12345678.90' 
      curr10_4      = '123456.7890' 
      curr20_2      = '123456789012345678.90' 
      curr20_4      = '1234567890123456.7890' 
      cuky          = 'EUR' 
      quan10        = '1234567890' 
      quan10_2      = '12345678.90' 
      quan10_4      = '123456.7890' 
      quan20        = '12345678901234567890' 
      quan20_2      = '123456789012345678.90' 
      quan20_4      = '1234567890123456.7890' 
      unit2         = 'KG' 
      unit3         = 'DEG' 
      geom_ewkb     = 
        '01010000200000000000000000000000000000000000000000' 
      lchr_int      = 256 
      lchr          = 'abcdefghijklmnopqrstuvwxyz' ) ). 
 
    SELECT SINGLE * 
           FROM demo_ddic_types 
           WHERE id = char`X` 
           INTO @FINAL(wa). 
 
    out->write( wa ). 
 
    INSERT demo_ddic_types FROM @( VALUE #( id = 'Y' ) ). 
    UPDATE demo_ddic_types SET 
      int1          = int1`255`, 
      int2          = int2`32767`, 
      int4          = int4`2147483647`, 
      int8          = int8`9223372036854775807`, 
      dec10         = dec`1234567890`, 
      dec10_2       = dec`12345678.90`, 
      dec20         = dec`12345678901234567890`, 
      dec20_4       = dec`1234567890123456.7890`, 
      d16n          = d16n`1234567890123456E10`, 
      df16_dec      = df16_dec`1.23456789012345`, 
      df16_raw      = df16_raw`1234567890123456`, 
      d34n          = d34n`1234567890123456789012345678901234E10`, 
      df34_dec      = df34_dec`1234567890123456.78901234567890`, 
      df34_raw      = df34_raw`1234567890123456789012345678901234`, 
      fltp          = fltp`-.15e-3`, 
      char1         = char`a`, 
      char10        = char`abcdefghij`, 
      sstring256    = sstring`abcdefghijklmnopqrstuvwxyz`, 
      sstring512    = sstring`abcdefghijklmnopqrstuvwxyz`, 
      string        = `abcdefghijklmnopqrstuvwxyz`, 
      raw1          = raw`FF`, 
      raw10         = raw`00112233445566778899`, 
      rawstring     = '00112233445566778899AABBCCDDEEFF', 
      dats          = dats`20200720`, 
      tims          = tims`162345`, 
      datn          = datn`20200720`, 
      timn          = timn`162345`, 
      utcl          = utclong`2020-07-20 16:23:45`, 
      accp          = `202007`, 
      numc1         = numc`1`, 
      numc10        = numc`0123456789`, 
      clnt          = clnt`000`, 
      lang          = lang`E`, 
      curr10_2      = curr`12345678.90`, 
      curr10_4      = curr`123456.7890`, 
      curr20_2      = curr`123456789012345678.90`, 
      curr20_4      = curr`1234567890123456.7890`, 
      cuky          = cuky`EUR`, 
      quan10        = quan`1234567890`, 
      quan10_2      = quan`12345678.90`, 
      quan10_4      = quan`123456.7890`, 
      quan20        = quan`12345678901234567890`, 
      quan20_2      = quan`123456789012345678.90`, 
      quan20_4      = quan`1234567890123456.7890`, 
      unit2         = unit`KG`, 
      unit3         = unit`DEG`, 
      geom_ewkb     = 
        '01010000200000000000000000000000000000000000000000', 
      lchr_int      = int4`256`, 
      lchr          = 'abcdefghijklmnopqrstuvwxyz' 
      WHERE id = char`Y`. 
 
    SELECT SINGLE * 
           FROM demo_ddic_types 
           WHERE id = char`Y` 
           INTO @FINAL(wb). 
 
    out->write( wb ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The first part of the example uses the ABAP SQL statement [`INSERT`](../../abap-programming-language/abap-database-access/abapinsert_dbtab.md) to insert a value into each column of a row of the DDIC database table `DEMO_DDIC_TYPES`. The values are [ABAP literals](../../abap-programming-language/abap-database-access/abenabap_sql_literals.md) used in a [host expression](../../abap-programming-language/abap-database-access/abenabap_sql_host_expressions.md). It should be noted that the literals are assigned to the components of a temporary ABAP structure that is constructed with the [`VALUE`](../../abap-programming-language/abap-creating-objects-and-values/abenconstructor_expression_value.md) operator. These components have the ABAP type that is mapped to the DDIC type of the respective database column. If the type of a literal does not match the this ABAP type, its value is [converted according to the rules](../../abap-programming-language/abap-processing-internal-data/abenconversion_elementary.md). When the temporary structure is inserted in the database table via the [database interface](../../abap-glossary/abendatabase_interface_glosry.md), another conversion might take place from the ABAP types to the database specific types, if necessary.

The second part of the example uses the ABAP SQL statement [`UPDATE`](../../abap-programming-language/abap-database-access/abapinsert_dbtab.md) to set the values of the columns of a row that was inserted with empty columns. In the `UPDATE` statement, the values for most of the data types can be passed as [typed literals](../../abap-programming-language/abap-database-access/abenabap_sql_typed_literals.md) that are not possible in general ABAP. In the case of typed literals, no ABAP-specific type conversion takes place and the validity of the values is guaranteed by the syntax check.
