---
title: "string_exp - Performance Note"
source_file: abenstring_expr_perfo.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > String Expressions (string_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# string_exp - Performance Note

If on the right side of an [assignment](abenequals_string_expr.md) strings in a [string expression](abapcompute_string.md) are appended to a variable `str` with the type `string` specified on the left side of the assignment, the variable is used directly in the following cases without producing an interim result.

- `str &&= dobj1 && dobj2 && ... .`

- `str = |{ str }...{ dobj1 [format_options] }...{ dobj2 [format_options] }...|.`

The appended strings cannot be dependent on `str` for the compiler:

- The target field `str` can occur only once in the string expression, and only at the very beginning.

- No formatting options can be used on `str` in a [string template](abenstring_templates.md).

- Only directly specified data objects `dobj1`, `dobj2`, ... and no other [expressions](../../abap-glossary/abenexpression_glosry.md) or [functions](../../abap-glossary/abenfunction_glosry.md) can be listed, even if they are not dependent on `str`.

Optimization is therefore deactivated in the following cases:

- `str &&= ... && meth( ... ) && ... .`

- `str &&= ... && str && ... .`

- `str = |{ str }...{ expr( ... ) }...|.`

- `str = |{ str format_options }...|.`

- `str = |{ str }...{ str }...|.`

Deactivating optimization for assignments that are not used very often is usually uncritical, it is strongly recommend to only use optimizable forms within loops, because otherwise the runtime would increase quadratically with the number of iterations. Within loops, the results of expressions that can only be determined there should be assigned to helper variables `dobj1`, `dobj2`, and so on, and these should be used.

## Hint

If optimization is deactivated, the runtime is quadratically dependent on the number of iterations, since the length of the string in the interim result increases in proportion with the number of iterations and has to be copied to the result in every loop pass.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following example for generating an HTML file, there is no optimization. The runtime depends quadratically on the number of iterations `n`.

``` abap
FINAL(n) = 10000. 
 
DATA(html) = `<html><body><table border=1>`. 
DO n TIMES. 
  html = |{ html }<tr><td>{ 
            CONV string( ipow( base = sy-index exp = 2 ) ) 
            }</td></tr>|. 
ENDDO. 
html = html && `</table></body></html>`.
```

The following example shows how the runtime can be optimized by using a helper variable. The bigger `n` is, the greater the runtime difference to the previous example.

``` abap
FINAL(n) = 10000. 
 
DATA(html) = `<html><body><table border=1>`. 
DATA square type string. 
DO n TIMES. 
  square = ipow( base = sy-index exp = 2 ). 
  html = |{ html }<tr><td>{ square }</td></tr>|. 
ENDDO. 
html = html && `</table></body></html>`.
```

## Executable Example

[Concatenating Strings](abenstring_concatenation_abexa.md)
