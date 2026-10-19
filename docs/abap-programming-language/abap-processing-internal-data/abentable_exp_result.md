---
title: "table_exp - Result"
source_file: abentable_exp_result.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > itab - Table Expressions (table_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# table_exp - Result

## Syntax

``` abap
... {             itab[ itab_line ][...] }   
  | { VALUE type( itab[ itab_line ][...] [default] ) }   
  | { REF   type( itab[ itab_line ][...] [default]  ) } ...  
```

[`itab_line`](abentable_exp_itab_line.md) · [`[...]`](abentable_exp_chaining.md) · [`itab_line`](abentable_exp_itab_line.md) · [`[...]`](abentable_exp_chaining.md) · [`default`](abentable_exp_optional_default.md) · [`itab_line`](abentable_exp_itab_line.md) · [`[...]`](abentable_exp_chaining.md) · [`default`](abentable_exp_optional_default.md)

### Alternative

[1. `... itab[ ... ][...]`](abentable_exp_result.md#alternative-1)

[2. `... VALUE type( itab[ ... ][...] [default] )`](abentable_exp_result.md#alternative-2)

[3. `... REF type( itab[ ... ][...] [default] )`](abentable_exp_result.md#alternative-3)

## Overview

### Description

If a [table expression](abentable_expressions.md) is specified in a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md) or in a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md), the read line can be passed to this position in three different ways:

- As a [field symbol](../../abap-glossary/abenfield_symbol_glosry.md) to which the table line is assigned.

- As a [work area](../../abap-glossary/abenwork_area_glosry.md) that contains the content of the table line.

- As a [data reference variable](../../abap-glossary/abendata_reference_variable_glosry.md) that points to the table line.

The result of a table expression is only available temporarily. It is used as an operand of a statement and then deleted again. It is deleted when the current statement is closed or after the evaluation of a relational expression once the truth value is determined.

The ways of how a table expression is specified shown here determine how the table line is returned. A default value [`default`](abentable_exp_optional_default.md) can be specified for the result in two alternatives.

## Alternative 1

`... itab[ ... ]`

## Alternative 2

`... VALUE type( itab[ ... ] [default] )`

### Description

Both alternatives can be specified in all read positions for table expressions in which the line type matches the operand type (see also [Chainings](abentable_exp_chaining.md)). The result is either a temporary field symbol, a temporary work area, or the value is assigned directly to a target variable. If the value operator `VALUE` is used, an optional default value [`default`](abentable_exp_optional_default.md) can be specified for cases where no table line is found.

- If the table expression is not specified as an operand of the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) or of the reference operator [`REF`](abenconstructor_expression_ref.md), the result is usually a temporary field symbol typed with the line type of the internal table and to which the table line found is assigned. For performance reasons, there are exceptions to this rule in the following cases:

  - If the table expression is specified as the right side of an [assignment](abenequals_operator.md), the content of the table line or a [component](abentable_exp_chaining.md) is assigned directly to the target variable instead of a temporary result being produced.

  - If the line type of the internal table is flat and narrow and used directly in the operand position, for example as an operand of an arithmetic expression or as a formal parameter for an actual parameter where pass by value is declared, the result is a temporary work area.

- If the table expression is specified as an operand of the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md), the result is always a temporary work area, unless the expression is specified as the right side of an [assignment](abenequals_operator.md). The data type of the work area is determined by specifying [`type`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) for the constructor expression:

  - If the `#` character is specified for `type` and the data type required in an operand position is known uniquely and completely, the operand type is used. Otherwise the line type of the internal table or of a [chaining](abentable_exp_chaining.md) specified here is applied.

  - If a non-generic data type `dtype` is specified for `type`, the line type of the internal table must be compatible with this data type or be convertible to this data type. In this case, the temporary work area has the data type `dtype` and the data of the line found is converted to this data type, if necessary, in accordance with the [conversion rules](../../abap-glossary/abenconversion_rule_glosry.md).

    If the expression is specified as the right side of an [assignment](abenequals_operator.md), the content of the table line or [component](abentable_exp_chaining.md) is also assigned directly when using `VALUE`.

In most cases, it is transparent and irrelevant, whether the result exists as a field symbol or as a work area. In some cases, however, performance reasons or to avoid side effects, it may be beneficial if the standard behavior is suspended and data is written explicitly to a temporary work area instead.

- Side effects can occur if the line of the internal table to which the temporary field symbol points is modified while the binding to the field symbol persists.

### Hints

- A table expression whose result is a temporary field symbol can be viewed as a short form of the statement [`READ TABLE`](abapread_table.md) with the addition [`ASSIGNING`](abapread_table_outdesc.md) and a table expression whose result is a temporary work area can be viewed as a short form of this statement with the addition [`INTO`](abapread_table_outdesc.md). The corresponding rules and notes apply.

- More specifically, [restrictions](abapread_table_outdesc.md) regarding the modification of key fields must be respected in write positions in the case of table expressions whose result is a temporary field symbol.

- In variant 1, the compilation decides whether the result is a field symbol or a work area, not the table content at runtime.

- [Chainings](abentable_exp_chaining.md) of table expressions can also be specified as an operand of the value operator `VALUE`. This operand then controls the final result of the chaining.

- Unlike when using the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) for constructing values, elementary types or reference types can also be specified for table expressions for `type`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following program excerpt shows table expression with field symbols and work areas as a result.

``` abap
CLASS class DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS meth IMPORTING p1 TYPE i      OPTIONAL 
                                 p2 TYPE string OPTIONAL 
                                 p3 TYPE c      OPTIONAL. 
ENDCLASS. 
 
CLASS class IMPLEMENTATION. 
  METHOD meth. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(abcde) = 'abcdefghijklmnopqrstuvwxyz'. 
    TYPES text TYPE c LENGTH 1000. 
    DATA  itab TYPE TABLE OF i. 
    DATA  jtab TYPE TABLE OF string. 
    DATA  ktab TYPE TABLE OF text. 
 
    FIELD-SYMBOLS <itab> TYPE INDEX TABLE. 
 
    itab = VALUE #( ( 1 ) ). 
    jtab = VALUE #( ( CONV string( abcde ) ) ). 
    ktab = VALUE #( ( abcde ) ). 
 
    FINAL(number) = itab[ 1 ]. 
    FINAL(text)   = VALUE #( jtab[ 1 ] ). 
 
    class=>meth( p1 = itab[ 1 ] )            ##operator. 
    class=>meth( p2 = VALUE #( jtab[ 1 ] ) ) ##operator. 
    class=>meth( p3 = VALUE #( ktab[ 1 ] ) ) ##operator. 
 
    ASSIGN itab TO <itab>. 
    class=>meth( p1 = <itab>[ 1 ] ). 
  ENDMETHOD. 
ENDCLASS.
```

- Temporary work areas are passed in the assignments to `number` and `text`. The `VALUE` operator of the second assignment expresses this explicitly, but is not necessary.

- In the passes to the formal parameter of the method `meth`, the results are temporary field symbols by default. In two cases, the `VALUE` operator forces a work area explicitly. In the extended program checks, all passes produces syntax check warnings that can be hidden here using the pragma `##operator`.

  - In the pass to the formal parameter `p1`, using a field symbol by default is bad for performance, since the line is a flat narrow table line. The `VALUE` operator is recommended instead.

  - In the pass to the formal parameter `p2`, specifying a work area explicitly is bad for performance, since the line is a deep table line. The `VALUE` operator is not recommended here.

  - In the pass to the formal parameter `p3`, specifying a work area explicitly is bad for performance, since the line is a deep table line. The `VALUE` operator is not recommended here.

- When specifying the internal table using a generically typed field symbol `itab`, using the temporary field symbol by default does not produce a syntax check warning, since no fixed work area can be derived here.

### Executable Example

[Table Expressions, Side Effects](abentable_exp_side_effect_abexa.md)

## Alternative 3

`... REF type( itab[ ... ] [default] )`

### Description

This alternative can be specified in all read positions for table expressions in which a data reference variable with a suitable type is expected. If a table expression is used as an operand of a constructor expression with the reference operator [`REF`](abenconstructor_expression_ref.md), the result is a temporary data reference variable that points to the found table line. If no table line is found, an optional default value [`default`](abentable_exp_optional_default.md) can be specified.

The [static type](../../abap-glossary/abenstatic_type_glosry.md) of the reference variable is determined by specifying [`type`](abenconstructor_expression_ref.md) for the constructor expression:

- If the `#` character is specified for `type`, the line type of the internal table is used as the static type.

- If a non-generic data type `dtype` or the generic data type [`data`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) is specified for `type`, they determine the static type of the result. A non-generic data type, `dtype`, must be compatible with the line type of the internal table.

If the reference operator [`REF`](abenconstructor_expression_ref.md) is specified in front of a [chaining](abentable_exp_chaining.md) whose result is a component of a structured table line, it creates a reference to this component. In this case, no substring accesses [`+off(len)`](../abap-operands/abenoffset_length.md) can be specified after the component.

### Hints

- A table expression whose result is a temporary data reference variable can be viewed as a short form of the statement [`READ TABLE`](abapread_table.md) with the addition [`REFERENCE INTO`](abapread_table_outdesc.md). The corresponding rules and notes apply.

- More specifically, in the case of a table expression whose result is a temporary data reference variable, the [restrictions](abapread_table_outdesc.md) on the modification of key fields are respected when dereferencing write positions.

- The static type of the temporary data reference variable can only be the line type of the internal table or be completely generic.

- [Chainings](abentable_exp_chaining.md) of table expressions can also be specified as an operand of the reference operator `REF`, which then controls the final result of the chaining.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following program corresponds to the example for [`READ TABLE REFERENCE INTO`](abapread_table_outdesc.md), but the statement `READ` has been replaced by a table expression in the constructor expression `REF`.

``` abap
DATA: carrid TYPE sflight-carrid, 
      connid TYPE sflight-connid, 
      fldate TYPE sflight-fldate. 
 
... 
 
DATA sflight_tab TYPE SORTED TABLE OF sflight 
                 WITH UNIQUE KEY carrid connid fldate. 
 
SELECT * 
       FROM sflight 
       WHERE carrid = @carrid AND 
             connid = @connid 
       INTO TABLE @sflight_tab. 
 
IF sy-subrc = 0. 
  TRY. 
      FINAL(sflight_ref) = 
        REF #( sflight_tab[ KEY primary_key 
                            COMPONENTS carrid = carrid 
                                       connid = connid 
                                       fldate = fldate ] ). 
      sflight_ref->price *= '0.9'. 
    CATCH cx_sy_itab_line_not_found. 
      ... 
  ENDTRY. 
ENDIF.
```
