---
title: "boolc, boolx, xsdbool, Boolean Functions"
source_file: abenboole_functions.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# boolc, boolx, xsdbool, Boolean Functions

## Variant

[1. `... boolc( log_exp ) ...`](abenboole_functions.md#variant-1)

[2. `... boolx( bool = log_exp bit = bit ) ...`](abenboole_functions.md#variant-2)

[3. `... xsdbool( log_exp ) ...`](abenboole_functions.md#variant-3)

## Overview

### Description

The [built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) Boolean functions determine the [truth value](../../abap-glossary/abentruth_value_glosry.md) of a logical expression [`log_exp`](abenlogexp.md) specified as an argument. For `log_exp`, any logical expression can be specified in accordance with the applicable rules. The return value of a Boolean function has a data type dependent on the function and expresses the truth value of the logical expression with a value of this type.

### Hint

These functions can be considered a partial replacement for the Boolean data type for truth values that is not available in ABAP. In particular, `xsdbool` and, under certain circumstances, `boolc` can be used in many operand positions where values of the type `ABAP_BOOLEAN` (or `abap_bool` of the type pool `ABAP`) are expected.

## Variant 1

`... boolc( log_exp ) ...`

### Description

The function `boolc` returns a single-character character string of the type `string`. If the logical expression is true, *X* is returned. If the logical expression is false, a blank is returned. In principle, `boolc` is one of the [processing functions with character-like results](../abap-processing-internal-data/abenprocess_functions.md) and can be specified in [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md) and in [character-like expression positions](../../abap-glossary/abencharlike_expr_position_glosry.md).

### Hints

- If `boolc` requires return values other than *X* or blank (for example, *Y* and *N* or *1* and *0*), the result of `boolc` can be processed directly using the function [`translate`](../abap-processing-internal-data/abentranslate_functions.md) or another suitable [processing function](../abap-processing-internal-data/abenprocess_functions.md).

- The result of `boolc` should not be compared with the constants `abap_true` and `abap_false` in relational expressions, since the latter converts from `c` to `string` and ignores any blanks. Comparisons of this type are not usually necessary. If a comparison of this type is to be executed anyway, the function `xsdbool` can be used instead of `boolc` whose result has the ABAP type mapped to `ABAP_BOOLEAN`.

- If the logical expression is false, the result of `boolc` does not meet the condition [`IS INITIAL`](abenlogexp_initial.md), since a blank and no empty string is returned. If this is desired, the function `xsdbool` can be used instead of `boolc`.

- If `boolc` is used in inappropriate places as specified in the points above, this leads to a syntax warning, which can be hidden using a pragma.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The value 0, 1, or 2 is assigned to the variable `bool_value`, depending on the result of the logical expressions `log_exp1` and `log_exp2`.

``` abap
DATA bool_value TYPE i. 
 
bool_value = strlen( condense( val = boolc( log_exp1 ) ) ) + 
             strlen( condense( val = boolc( log_exp2 ) ) ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of a method, where the input parameter `no_dialog` is supplied with the character-like representation of the results of a predicate expression.

``` abap
DATA word TYPE c LENGTH 30. 
DATA result_tab TYPE cl_abap_docu=>search_results. 
 
cl_abap_docu=>start( 
  EXPORTING word           = word 
            no_dialog      = boolc( sy-batch IS NOT INITIAL ) 
  IMPORTING search_results = result_tab ).
```

## Variant 2

`... boolx( bool = log_exp bit = bit ) ...`

### Description

The function `boolx` returns a byte chain of the type `xstring`. If the logical expression is true, the byte chain is filled as if the function [`bit-set( bit )`](../abap-processing-internal-data/abenbit_functions.md) were executed. If the logical expression is false, the byte chain is filled as if the function [`bit-set( 0 )`](../abap-processing-internal-data/abenbit_functions.md) were executed. `bit` expects a data object of the type `i`. In principle, `boolx` belongs to the [bit functions](../abap-processing-internal-data/abenbit_functions.md) and can be used in all positions where a [bit expression](../../abap-glossary/abenbit_expression_glosry.md) is also allowed.

### Hint

The function `boolx` can be used for efficient storage of sequences of truth values.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following [bit expression](../../abap-glossary/abenbit_expression_glosry.md) is hexadecimal `55`, which corresponds to the calculated bit string `01010101`.

``` abap
FINAL(result) = boolx( bool = 2 > 1 bit = 8 ) 
        BIT-OR boolx( bool = 2 < 1 bit = 7 ) 
        BIT-OR boolx( bool = 2 > 1 bit = 6 ) 
        BIT-OR boolx( bool = 2 < 1 bit = 5 ) 
        BIT-OR boolx( bool = 2 > 1 bit = 4 ) 
        BIT-OR boolx( bool = 2 < 1 bit = 3 ) 
        BIT-OR boolx( bool = 2 > 1 bit = 2 ) 
        BIT-OR boolx( bool = 2 < 1 bit = 1 ).
```

The bit expression above can be expressed using the following iteration with the operator [`REDUCE`](abenconstructor_expression_reduce.md).

``` abap
FINAL(result) = 
  REDUCE xstring( INIT x TYPE xstring 
                  FOR j = 4 THEN j - 1 UNTIL j < 1 
                  LET b1 = 2 * j b2 = 2 * j - 2 IN 
                  NEXT x = x BIT-OR boolx( bool = 2 > 1  bit = b1 ) 
                             BIT-OR boolx( bool = 2 < 1  bit = b2 ) ).
```

## Variant 3

`... xsdbool( log_exp ) ...`

### Description

Like `boolc`, the function `xsdbool` returns the value *X* for true and a blank for false. The data type of the return value, however, has the type `c` of the length 1 here.

The return value references the type `XSDBOOLEAN` from the ABAP Dictionary. This type, which refers to the identically named domain of type `CHAR` and length 1, is handled like a real Boolean type in serializations and deserializations to or from [asXML](../abap-data-interchange-formats/abenabap_xslt_asxml_schema.md) and [asJSON](../abap-data-interchange-formats/abenabap_asjson_schema.md) using [`CALL TRANSFORMATION`](../abap-data-interchange-formats/abapcall_transformation.md). The XML or JSON values `true` and `false` are assigned to the values *X* and blank of this type.

`xsdbool` can be specified in [general](../../abap-glossary/abengeneral_expr_position_glosry.md) and [character-like expression positions](../../abap-glossary/abencharlike_expr_position_glosry.md).

### Hints

- The result of `xsdbool` can be used like a value of the type `ABAP_BOOLEAN` and can be compared with the constants `abap_true` and `abap_false` without any problems.

- If the logical expression is false, the result of `boolc` fulfills the condition [`IS INITIAL`](abenlogexp_initial.md), since the returned blank is the type-dependent initial value at the same time.

- The result of `xsdbool` cannot usually be converted directly using a [processing function](../abap-processing-internal-data/abenprocess_functions.md) such as [`translate`](../abap-processing-internal-data/abentranslate_functions.md), since the trailing blanks here are ignored in text fields of type `c`. The result of a false logical expression would be ignored. The result of the function `boolc` of type `string` is better suited for conversions of this type.

- The abbreviation `xsd` stands for [XML schema data types](http://www.w3.org/TR/xmlschema-2/).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example sets the type and the value of the variable `gui_flag` declared inline using the Boolean function `xsdbool` for whose argument a [predicative method call](../../abap-glossary/abenpredicative_method_call_glosry.md) is listed. The variable is then serialized to [asXML](../../abap-glossary/abenasxml_glosry.md) and [asJSON](../../abap-glossary/abenasjson_glosry.md) using the predefined [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) [`ID`](../abap-data-interchange-formats/abenabap_xslt_id.md). This produces the value *true* or `false`. After a comparison with the identically typed constant `abap_false`, the formatted result of the serialization is either read or displayed.

The result would be quite different if `boolc` were used instead of `xsdbool`. First, the transformations would have a different result since the values *X* and blank are not transformed to `true` or `false`; second, the logical expression `gui_flag = abap_false` would always be false, since `abap_false` loses its blank when converting to the type `string`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(gui_flag) = xsdbool( cl_demo_sap_gui=>check( ) ). 
 
CALL TRANSFORMATION id SOURCE gui_flag = gui_flag 
                       RESULT XML FINAL(xml). 
 
FINAL(writer) = 
  cl_sxml_string_writer=>create( type = if_sxml=>co_xt_json ). 
CALL TRANSFORMATION id SOURCE gui_flag = gui_flag 
                       RESULT XML writer. 
FINAL(json) = writer->get_output( ). 
 
out->write_xml( xml ). 
out->write_json( json ). 
 
IF gui_flag = abap_false. 
  out->get( ). 
ELSE. 
  out->display( ). 
ENDIF.
```
