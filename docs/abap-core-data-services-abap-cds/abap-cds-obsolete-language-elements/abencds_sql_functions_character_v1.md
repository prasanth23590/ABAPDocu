---
title: "CDS DDL - DDIC-Based View, String Functions"
source_file: abencds_sql_functions_character_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions > CDS DDL - DDIC-Based View, Built-In Functions > CDS DDL - DDIC-Based View, sql_functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, String Functions

The following table shows the possible [SQL functions](abencds_sql_functions_v1.md) for character strings in a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), plus the requirements made on the arguments.

<table>
<thead>
<tr class="header">
<th><strong>Function</strong></th>
<th><strong>Result</strong></th>
<th><strong>Valid Argument Types</strong></th>
<th><strong>Result Type</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">CONCAT(arg1, arg2)</code></a></td>
<td>Concatenates strings in <code class="ph codeph">arg1</code> and <code class="ph codeph">arg2</code>. Trailing blanks in <code class="ph codeph">arg1</code>, <code class="ph codeph">arg2</code>, and in the result are ignored. The maximum length of the result is 1333.</td>
<td>See below</td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a> if an argument has the type <a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a>, else <a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a> with the length of the result.</td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">CONCAT_WITH_SPACE(arg1, arg2, spaces )</code></a></td>
<td>Concatenates strings in <code class="ph codeph">arg1</code> and <code class="ph codeph">arg2</code> as with <code class="ph codeph">CONCAT</code>. The number of blanks specified in spaces is inserted between <code class="ph codeph">arg1</code> and <code class="ph codeph">arg2</code>. The maximum length of the result is 1333.</td>
<td><p><code class="ph codeph">arg1</code>, <code class="ph codeph">arg2</code>: see below</p>
<p><code class="ph codeph">spaces</code>: positive <a href="abencds_literal_v1.html">numeric literal</a> greater than 0 and less than or equal to 1333</p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a> if an argument has the type <a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a>, else <a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a> with the length of the result.</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">INSTR(arg, sub)</code></a></td>
<td>Position of the first occurrence of the string from <code class="ph codeph">sub</code> in <code class="ph codeph">arg</code> (case-sensitive). <code class="ph codeph">arg</code> respects leading blanks and ignores trailing blanks. <code class="ph codeph">sub</code> respects all blanks. <code class="ph codeph">sub</code> must contain at least one character. If no occurrences are found, the result is 0.</td>
<td><p><code class="ph codeph">arg</code>: see below</p>
<p><code class="ph codeph">sub</code>: non-empty <a href="abencds_literal_v1.html">character literal</a></p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">INT4</code></a></td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">LEFT(arg, len)</code></a></td>
<td>String of the length <code class="ph codeph">len</code> with the <code class="ph codeph">len</code> left characters of <code class="ph codeph">arg</code> (ignoring the trailing blanks). The value of <code class="ph codeph">len</code> cannot be greater than the length of <code class="ph codeph">arg</code>.</td>
<td><p><code class="ph codeph">arg</code>: see below</p>
<p><code class="ph codeph">len</code>: positive <a href="abencds_literal_v1.html">numeric literal</a> greater than 0 and less than or equal to 1333</p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a> if <code class="ph codeph">arg</code> has the type <a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a>, else <a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a> with length <code class="ph codeph">len</code></td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">LENGTH(arg)</code></a></td>
<td>Number of characters in <code class="ph codeph">arg</code> ignoring trailing blanks</td>
<td>See below</td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">INT4</code></a></td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">LOWER( arg )</code></a></td>
<td>String with a length of <code class="ph codeph">arg</code>, in which all uppercase letters are transformed to lowercase letters</td>
<td>See below, with the exception of <a href="abenddic_builtin_types.html"><code class="ph codeph">NUMC</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DATS</code></a>, and <a href="abenddic_builtin_types.html"><code class="ph codeph">TIMS</code></a></td>
<td>Data type of <code class="ph codeph">arg</code> in the length of <code class="ph codeph">arg</code></td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">LPAD(arg, len, src)</code></a></td>
<td>String of the length <code class="ph codeph">len</code> with the right-aligned content of <code class="ph codeph">arg</code> without trailing blanks and in which leading blanks produced by the expanded string are replaced by the characters from the argument <code class="ph codeph">src</code> (respecting all blanks). Leading blanks from <code class="ph codeph">arg</code> are preserved. If more characters are required than exist in <code class="ph codeph">src</code>, the content of <code class="ph codeph">src</code> is used repeatedly. If <code class="ph codeph">len</code> is less than the length of <code class="ph codeph">arg</code>, it is truncated on the right. If <code class="ph codeph">src</code> is empty and <code class="ph codeph">len</code> is greater than the length of <code class="ph codeph">arg</code>, <code class="ph codeph">arg</code> remains unchanged.</td>
<td><p><code class="ph codeph">arg</code>: see below</p>
<p><code class="ph codeph">len</code>: positive <a href="abencds_literal_v1.html">numeric literal</a> greater than 0 and less than or equal to 1333</p>
<p><code class="ph codeph">src</code>: <a href="abencds_literal_v1.html">Character literal</a></p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a> if <code class="ph codeph">arg</code> has the type <a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a>, else <a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a> with length <code class="ph codeph">len</code></td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">LTRIM(arg, char)</code></a></td>
<td>String with the content of <code class="ph codeph">arg</code> in which all trailing blanks and leading characters are removed that match the character in <code class="ph codeph">char</code>. A blank in <code class="ph codeph">char</code> is significant.</td>
<td><p><code class="ph codeph">arg</code>: see below</p>
<p><code class="ph codeph">char</code>: <a href="abencds_literal_v1.html">Character literal</a> with length 1</p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a> if <code class="ph codeph">arg</code> has the type <a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a>, else <a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a> with the length of <code class="ph codeph">arg</code>.</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">REPLACE(arg1, arg2, arg3)</code></a></td>
<td>String <code class="ph codeph">arg1</code>, in which all instances of <code class="ph codeph">arg2</code> are replaced by the content from <code class="ph codeph">arg3</code>. The replacement of letters is case-sensitive. Trailing blanks are ignored in all arguments. The maximum length of the result is 1333</td>
<td>See below</td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a> if <code class="ph codeph">arg1</code> or <code class="ph codeph">arg3</code> has the type <a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a>, else <a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a> with the maximum possible length of the result.</td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">RIGHT(arg,len)</code></a></td>
<td>String of the length <code class="ph codeph">len</code> with the <code class="ph codeph"> len</code> right characters of <code class="ph codeph">arg</code> (ignoring the trailing blanks). The value of <code class="ph codeph">len</code> cannot be greater than the length of <code class="ph codeph">arg</code>.</td>
<td><p><code class="ph codeph">arg</code>: see below</p>
<p><code class="ph codeph">len</code>: positive <a href="abencds_literal_v1.html">numeric literal</a> greater than 0 and less than or equal to 1333</p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a> if <code class="ph codeph">arg</code> has the type <a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a>, else <a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a> with length <code class="ph codeph">len</code></td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">RPAD(arg, len, src)</code></a></td>
<td>String of the length <code class="ph codeph">len</code> with the left-aligned content of <code class="ph codeph">arg</code> without trailing blanks and in which trailing blanks produced by the expanded string are replaced by the characters from the argument <code class="ph codeph">src</code> (respecting all blanks). Leading blanks from <code class="ph codeph">arg</code> are preserved. If more characters are required than exist in <code class="ph codeph">src</code>, the content of <code class="ph codeph">src</code> is used repeatedly. If <code class="ph codeph">len</code> is less than the length of <code class="ph codeph">arg</code>, it is truncated on the right. If <code class="ph codeph">src</code> is empty and <code class="ph codeph">len</code> is greater than the length of <code class="ph codeph">arg</code>, <code class="ph codeph">arg</code> remains unchanged.</td>
<td><p><code class="ph codeph">arg</code>: see below</p>
<p><code class="ph codeph">len</code>: positive <a href="abencds_literal_v1.html">numeric literal</a> greater than 0 and less than or equal to 1333</p>
<p><code class="ph codeph">src</code>: <a href="abencds_literal_v1.html">Character literal</a></p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a> if <code class="ph codeph">arg</code> has the type <a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a>, else <a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a> with length <code class="ph codeph">len</code></td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">RTRIM(arg, char)</code></a></td>
<td>String with the content of <code class="ph codeph">arg</code> in which all trailing blanks are removed and all trailing characters that match the character in <code class="ph codeph">char</code>. A blank in <code class="ph codeph">char</code> is significant.</td>
<td><p><code class="ph codeph">arg</code>: see below</p>
<p><code class="ph codeph">char</code>: <a href="abencds_literal_v1.html">Character literal</a> with length 1</p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a> if <code class="ph codeph">arg</code> has the type <a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a>, else <a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a> with the length of <code class="ph codeph">arg</code>.</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">SUBSTRING(arg, pos, len)</code></a></td>
<td>Substring <code class="ph codeph">arg</code> from the position <code class="ph codeph">pos</code> with length <code class="ph codeph">len</code>. <code class="ph codeph">pos</code> and <code class="ph codeph">len</code> must be specified so that the substring is within <code class="ph codeph">arg</code>.</td>
<td><p><code class="ph codeph">arg</code>: see below</p>
<p><code class="ph codeph">pos</code> and <code class="ph codeph">len</code>: positive <a href="abencds_literal_v1.html">numeric literals</a> not equal to zero</p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a> if <code class="ph codeph">arg</code> has the type <a href="abenddic_builtin_types.html"><code class="ph codeph">SSTRING</code></a>, else <a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a> or <a href="abenddic_builtin_types.html"><code class="ph codeph">NUMC</code></a> with length of at lest <code class="ph codeph">len</code></td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">UPPER( arg )</code></a></td>
<td>String with a length of <code class="ph codeph">arg</code>, in which all lowercase letters were transformed to uppercase letters</td>
<td>See below, with the exception of <a href="abenddic_builtin_types.html"><code class="ph codeph">NUMC</code></a>, <a href="abenddic_builtin_types.html"><code class="ph codeph">DATS</code></a>, and <a href="abenddic_builtin_types.html"><code class="ph codeph">TIMS</code></a></td>
<td>Data type of <code class="ph codeph">arg</code> in the length of <code class="ph codeph">arg</code></td>
</tr>
</tbody>
</table>

The following can be specified as the arguments `arg`:

- [Literals](abencds_literal_v1.md) of a suitable type. The literal can be prefixed with the name of a domain.

- Suitable [fields](abencds_field_v1.md) of a data source [`data_source`](abencds_data_source_v1.md) of the current CDS view.

- [Path expressions](abencds_path_expression_v1.md) that identify a suitable field of a data source [`data_source`](abencds_data_source_v1.md).

- [Input parameters](abencds_parameter_v1.md) from the parameter list [`parameter_list`](abencds_parameter_list_v1.md).

- The following built-in functions and expressions (if they return a matching type):

  - Other built-in [SQL functions](abencds_sql_functions_v1.md)

  - [Arithmetic expressions](abencds_arithmetic_expression_v1.md)

  - Type modifications using [`CAST`](abencds_cast_expression_v1.md)

The valid argument types for `arg`, `arg1`, `arg2`, and `arg3` are [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md),[`CLNT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`LANG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`NUMC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CUKY`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`UNIT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and [`SSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

In functions where an explicit length `len` is specified, the actual length of the result is defined when the CDS view is activated and is at least as long as `len`.

In all functions with the exception of `LPAD` and `RPAD`, the trailing blanks of all arguments are removed before the actual processing and the trailing blanks of the result are removed before the return operation. In `LPAD` and `RPAD`, the trailing blanks of the argument `src` are preserved. In the case of `UPPER` and `LOWER`, the handling of trailing blanks makes no difference, as the length of the argument is retained.

## Hints

- The characters in the [surrogate area](../../abap-glossary/abensurrogate_area_glosry.md) of the [system code page](../../abap-glossary/abensystem_codepage_glosry.md) [UTF-16](../../abap-glossary/abenutf16_glosry.md) are handled as two characters by the CDS string functions. This must be respected when the length is determined and these characters must not be split by mistake. Functions `UPPER` and `LOWER` do not change the character of the surrogate area.

- In the case of the function `REPLACE`, it should be noted that the maximum possible length of the result can be slightly greater than the allowed length of 1333. This produces a syntax error. In general, the maximum possible length is calculated by dividing the length of `arg1` by the length of `arg2`, multiplied by the length of `arg3`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view applies built-in SQL functions for strings in the `SELECT` list to columns of the DDIC database table `DEMO_EXPRESSIONS`. The class `CL_DEMO_CDS_SQL_FNCTNS_STRING` uses `SELECT` to access the view.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_STRFUNC'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_sql_functions_string
  as select from
    demo_expressions
    {
      length(            char1               ) as r_length,
      instr(             char1, 'CD'         ) as r_instr,
      concat(            char1, char2        ) as r_concat,
      concat_with_space( char1, char2, 10    ) as r_concat_with_space,
      left(              char1, 3            ) as r_left,
      lower(             char1               ) as r_lower,
      right(             char2, 3            ) as r_right,
      lpad(              char1, 10, 'x'      ) as r_lpad,
      rpad(              char2, 10, 'y'      ) as r_rpad,
      ltrim(             char1, 'A'          ) as r_ltrim,
      rtrim(             char1, 'E'          ) as r_rtrim,
      replace(           char2, 'GHI', 'XXX' ) as r_replace,
      substring(         char2, 2, 3         ) as r_substring,
      upper(             char2               ) as r_upper
    } 
```
