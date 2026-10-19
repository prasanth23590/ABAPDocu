---
title: "sql_func - String Functions"
source_file: abensql_string_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - SQL Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - String Functions

## Syntax

``` abap
... func( arg1[, arg2] ... ) ...  
```

## Description

Calls a string function `func` as an [SQL expression](abapsql_expr.md) or operand of an expression in ABAP SQL. The arguments `arg1`, `arg2`, ... of the function are specified as a comma-separated list in parentheses. A blank must be placed after the opening parenthesis and in front of the closing parenthesis.

The following table shows the string functions that can be specified as SQL expressions and the requirements on the arguments. The value *x* in the ABAP SQL In-Memory Engine column indicates that the function can be executed in the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) and that the use of [this function](abensql_engine_expr.md) does not bypass [table buffering](../../abap-glossary/abentable_buffering_glosry.md) and does not cause the transport of an internal table accessed with [`FROM @itab`](abapselect_itab.md) to the database.

<table>
<thead>
<tr class="header">
<th><strong>Syntax</strong></th>
<th><strong>Meaning</strong></th>
<th><strong>Valid Argument Types</strong></th>
<th><strong>Result Type</strong></th>
<th><strong>ABAP SQL In-Memory Engine</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">CONCAT( sql_exp1,sql_exp2 )</code></a></td>
<td>Concatenates strings in <code class="ph codeph">sql_exp1</code> and <code class="ph codeph">sql_exp2</code>. Trailing blanks in <code class="ph codeph">sql_exp1</code>, <code class="ph codeph">sql_exp2</code>, and in the result are ignored. The maximum length of the result is 1333.</td>
<td>See below</td>
<td><code class="ph codeph">SSTRING</code> if an argument has the type <code class="ph codeph">SSTRING</code>, otherwise <code class="ph codeph">CHAR</code> with the length of the result.</td>
<td>x</td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">CONCAT_WITH_SPACE( sql_exp1,sql_exp2,spaces )</code></a></td>
<td>Concatenates strings in <code class="ph codeph">sql_exp1</code> and <code class="ph codeph">sql_exp2</code> as with <code class="ph codeph">CONCAT</code>. The number of blanks specified in <code class="ph codeph">spaces</code> is inserted between <code class="ph codeph">sql_exp1</code> and <code class="ph codeph">sql_exp2</code>. The maximum length of the result is 1333.</td>
<td><p><code class="ph codeph">sql_exp2</code>: see below</p>
<p><code class="ph codeph">spaces</code>: <a href="abenabap_sql_literals.html">Literal</a> or <a href="abenabap_sql_host_variables.html">host constant</a> with the <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">b</code>, <code class="ph codeph">s</code>, <code class="ph codeph">i</code>, or <code class="ph codeph">int8</code> greater than 0 and less than or equal to 1333</p></td>
<td><code class="ph codeph">SSTRING</code> if an argument has the type <code class="ph codeph">SSTRING</code>, otherwise <code class="ph codeph">CHAR</code> with the length of the result.</td>
<td>x</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">INITCAP( sql_exp )</code></a></td>
<td>String with a length of <code class="ph codeph">sql_exp</code>, in which the first letter of a word is transformed to uppercase, and all other letters are transformed to lowercase. A word is delimited by the following: beginning of a string, blank space, new line, form feed, carriage return, line feed, and anything after <em>!</em> <em>"</em> <em>#</em> <em>$</em> <em>%</em> <em>&amp;</em> <em>'</em> <em>(</em> <em>)</em> <em>*</em> <em>+</em> <em>,</em> <em>-</em> <em>.</em> <em>/</em> <em>:</em> <em>;</em> <em>&lt;</em> <em>=</em> <em>&gt;</em> <em>?</em> <em>@</em> <em>[</em> <em>\</em> <em>]</em> <em>^</em> <em>_</em> <em>`</em> <em>{</em> *</td>
<td>* <em>}</em> <em>~</em>.</td>
<td>See below</td>
<td><code class="ph codeph">SSTRING</code> if <code class="ph codeph">sql_exp</code> has the type <code class="ph codeph">SSTRING</code>, otherwise <code class="ph codeph">CHAR</code> with the length of <code class="ph codeph">sql_exp</code></td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">INSTR( sql_exp,sub )</code></a></td>
<td>Position of the first occurrence of the string from <code class="ph codeph">sub</code> in <code class="ph codeph">sql_exp</code> (case-sensitive). <code class="ph codeph">sql_exp</code> respects leading blanks and ignores trailing blanks. <code class="ph codeph">sub</code> respects all blanks. <code class="ph codeph">sub</code> must contain at least one character. If no occurrences are found, the result is 0.</td>
<td><p><code class="ph codeph">sql_exp</code>: see below</p>
<p><code class="ph codeph">sub</code>: <a href="abenabap_sql_literals.html">Literal</a> or <a href="abenabap_sql_host_variables.html">host constant</a> with the <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code>, <code class="ph codeph">n</code>, <code class="ph codeph">d</code>, or <code class="ph codeph">t</code></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">LEFT( sql_exp,len )</code></a></td>
<td>String of the length <code class="ph codeph">len</code> with the <code class="ph codeph">len</code> left characters of <code class="ph codeph">sql_exp</code> (ignoring the trailing blanks). The value of <code class="ph codeph">len</code> cannot be greater than the length of <code class="ph codeph">sql_exp</code>.</td>
<td><p><code class="ph codeph">sql_exp</code>: see below</p>
<p><code class="ph codeph">len</code>: <a href="abapsql_expr.html">SQL expression</a> with the <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">b</code>, <code class="ph codeph">s</code>, <code class="ph codeph">i</code>, or <code class="ph codeph">int8</code> greater than 0 and less than or equal to 1333</p></td>
<td><code class="ph codeph">SSTRING</code> if <code class="ph codeph">sql_exp</code> has the type <code class="ph codeph">SSTRING</code>, otherwise <code class="ph codeph">CHAR</code> with the length of the result</td>
<td>x</td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">LENGTH( sql_exp )</code></a></td>
<td>Number of characters in <code class="ph codeph">sql_exp</code> ignoring trailing blanks</td>
<td>See below</td>
<td><code class="ph codeph">INT4</code></td>
<td>x</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">LIKE_REGEXPR( pcre = pcre, \lbr value = sql_exp[, \lbr case_sensitive = case] )</code></a></td>
<td>Checks whether <code class="ph codeph">sql_exp</code> contains any occurrence of a <a href="abenpcre_glosry.html">Perl Compatible Regular Expression</a> (PCRE) <code class="ph codeph">pcre</code> and returns 1 if yes and 0 if no. The search is case-sensitive by default, but this can be overridden using the parameter <code class="ph codeph">case</code>.</td>
<td><p><code class="ph codeph">pcre</code>: see below</p>
<p><code class="ph codeph">sql_exp</code>: see below</p>
<p><code class="ph codeph">case</code>: 'X', ' ', or <a href="abensql_null.html">null expression</a></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">LOCATE( sql_exp, sub[,start[,occ]] )</code></a></td>
<td><p>Returns the position of a substring <code class="ph codeph">sub</code> in <code class="ph codeph">sql_exp</code> (case-sensitive). Both <code class="ph codeph">sql_exp</code> and <code class="ph codeph">sub</code> respect all blanks and must contain at least one character. <code class="ph codeph">start</code> and <code class="ph codeph">occ</code> are optional parameters. <code class="ph codeph">occ</code> can only be specified if <code class="ph codeph">start</code> is specified. <code class="ph codeph">start</code> specifies the offset from which to start the search, and <code class="ph codeph">occ</code> determines the number of occurrences.</p>
<p>Notes on the result:</p>
<p>If no occurrences are found or <code class="ph codeph">occ</code> is less than 1, the result is 0.</p>
<p>If <code class="ph codeph">sql_exp</code>, <code class="ph codeph">sub</code> or <code class="ph codeph">occ</code> are specified as <a href="abennull_value_glosry.html">null value</a>, the result is 0.</p>
<p>If <code class="ph codeph">start</code> is greater than 0, the matching is carried out starting from this position.</p>
<p>If <code class="ph codeph">start</code> is 0, <code class="ph codeph">NULL</code> or not specified, the matching is carried out starting from the first position. A setting of 1 for <code class="ph codeph">start</code> has the same effect.</p>
<p>If <code class="ph codeph">start</code> is less than 0, the starting position is the end of the string, i. e. if <code class="ph codeph">start</code> is -2, the starting position is the second to last character of the string. The matching then goes in the reverse direction from right to left.</p>
<p>If <code class="ph codeph">occ</code> is specified, the matched position is returned. If no match is found with the specified occurrence, the result is 0.</p>
<p>If <code class="ph codeph">occ</code> is not specified, the first matched position is returned. A setting of 1 for <code class="ph codeph">occ</code> is the same as not specifying it.</p></td>
<td><p><code class="ph codeph">sql_exp</code>: see below</p>
<p><code class="ph codeph">sub</code>: <a href="abenabap_sql_literals.html">Literal</a> or <a href="abenabap_sql_host_variables.html">host constant</a> with the <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code>, <code class="ph codeph">n</code>, <code class="ph codeph">d</code>, or <code class="ph codeph">t</code>, or <a href="abensql_null.html">null expression</a></p>
<p><code class="ph codeph">occ</code>: <code class="ph codeph">i</code> or <code class="ph codeph">int8</code></p>
<p><code class="ph codeph">start</code>: <code class="ph codeph">i</code> or <code class="ph codeph">int8</code></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">LOCATE_REGEXPR( pcre = pcre, \lbr value = sql_exp[, \lbr occurrence = occ][, \lbr case_sensitive = case][, \lbr start = start][, \lbr group = group] )</code></a></td>
<td><p>Searches <code class="ph codeph">sql_exp</code> for a <a href="abenpcre_glosry.html">Perl Compatible Regular Expression</a> (PCRE) pattern <code class="ph codeph">pcre</code> and returns the offset of the match. The other parameters are optional. <code class="ph codeph">occ</code> determines the number of occurrences of <code class="ph codeph">pcre</code>. The search is case-sensitive by default, but this can be overridden using the parameter <code class="ph codeph">case</code>. The parameter <code class="ph codeph">start</code> specifies the offset from which to start the search. The parameter <code class="ph codeph">group</code> specifies the number of the group of the matched substring.</p>
<p>If <code class="ph codeph">occ</code> is not greater than 0 or <code class="ph codeph">start</code> or <code class="ph codeph">group</code> are less than 0, the result is a <a href="abennull_value_glosry.html">null value</a>.</p></td>
<td><p><code class="ph codeph">pcre</code>: see below</p>
<p><code class="ph codeph">sql_exp</code>: see below</p>
<p><code class="ph codeph">occ</code>: <a href="abenabap_sql_literals.html">Literal</a> or <a href="abenabap_sql_host_variables.html">host constant</a> with the <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">b</code>, <code class="ph codeph">s</code>, <code class="ph codeph">i</code>, or <code class="ph codeph">int8</code> greater than 0 and less than or equal to 1333; <a href="abenexpression_glosry.html">expressions</a> are also possible if they return an integer of type <code class="ph codeph">INT4</code></p>
<p><code class="ph codeph">case</code>: 'X', ' ', or <a href="abensql_null.html">null expression</a></p>
<p><code class="ph codeph">start</code>: <code class="ph codeph">i</code> or <code class="ph codeph">int8</code></p>
<p><code class="ph codeph">group</code>: <code class="ph codeph">i</code> or <code class="ph codeph">int8</code></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">LOCATE_REGEXPR_AFTER( pcre = pcre, \lbr value = sql_exp[, \lbr occurrence = occ][, \lbr case_sensitive = case][, \lbr start = start][, \lbr group = group] )</code></a></td>
<td><p>Searches <code class="ph codeph">sql_exp</code> for a <a href="abenpcre_glosry.html">Perl Compatible Regular Expression</a> (PCRE) pattern <code class="ph codeph">pcre</code> and returns the offset of the match plus <em>1</em>. The other parameters are optional. <code class="ph codeph">occ</code> determines the number of occurrences of <code class="ph codeph">pcre</code>. The search is case-sensitive by default, but this can be overridden using the parameter <code class="ph codeph">case</code>. The parameter <code class="ph codeph">start</code> specifies the offset from which to start the search. The parameter <code class="ph codeph">group</code> specifies the number of the group of the matched substring.</p>
<p>If <code class="ph codeph">occ</code> is not greater than 0 or <code class="ph codeph">start</code> or <code class="ph codeph">group</code> are less than 0, the result is a <a href="abennull_value_glosry.html">null value</a>.</p></td>
<td><p><code class="ph codeph">pcre</code>: see below</p>
<p><code class="ph codeph">sql_exp</code>: see below</p>
<p><code class="ph codeph">occ</code>: <a href="abenabap_sql_literals.html">Literal</a> or <a href="abenabap_sql_host_variables.html">host constant</a> with the <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">b</code>, <code class="ph codeph">s</code>, <code class="ph codeph">i</code>, or <code class="ph codeph">int8</code> greater than 0 and less than or equal to 1333; <a href="abenexpression_glosry.html">expressions</a> are also possible if they return an integer of type <code class="ph codeph">INT4</code></p>
<p><code class="ph codeph">case</code>: 'X', ' ', or <a href="abensql_null.html">null expression</a></p>
<p><code class="ph codeph">start</code>: <code class="ph codeph">i</code> or <code class="ph codeph">int8</code></p>
<p><code class="ph codeph">group</code>: <code class="ph codeph">i</code> or <code class="ph codeph">int8</code></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">LOWER( sql_exp )</code></a></td>
<td>String with a length of <code class="ph codeph">sql_exp</code>, in which all uppercase letters are transformed to lowercase letters.</td>
<td>See below</td>
<td><code class="ph codeph">SSTRING</code> if <code class="ph codeph">sql_exp</code> has the type <code class="ph codeph">SSTRING</code>, otherwise <code class="ph codeph">CHAR</code> with the length of <code class="ph codeph">sql_exp</code></td>
<td>x</td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">LPAD( sql_exp,len,src )</code></a></td>
<td>String of the length <code class="ph codeph">len</code> with the right-aligned content of <code class="ph codeph">sql_exp</code> without trailing blanks and in which leading blanks produced by the expanded string are replaced by the characters from the argument <code class="ph codeph">src</code> (respecting all blanks). Leading blanks from <code class="ph codeph">sql_exp</code> are preserved. If more characters are required than exist in <code class="ph codeph">src</code>, the content of <code class="ph codeph">src</code> is used repeatedly. If <code class="ph codeph">len</code> is less than the length of <code class="ph codeph">sql_exp</code>, it is truncated on the right. If <code class="ph codeph">src</code> is empty and <code class="ph codeph">len</code> is greater than the length of <code class="ph codeph">sql_exp</code>, <code class="ph codeph">sql_exp</code> remains unchanged.</td>
<td><p><code class="ph codeph">sql_exp</code>: see below</p>
<p><code class="ph codeph">len</code>: <a href="abapsql_expr.html">SQL expression</a> with the <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">b</code>, <code class="ph codeph">s</code>, or <code class="ph codeph">i</code> greater than -2147483648 and less than 67108864. If <code class="ph codeph">len</code> is used as a <a href="abenabap_sql_literals.html">literal</a> or <a href="abenabap_sql_host_variables.html">host constant</a>, the ABAP type <code class="ph codeph">int8</code> is possible too. The result is empty if <code class="ph codeph">len</code> is less than or equal to 0. The length of the result is 1 if <code class="ph codeph">len</code> is used as a constant less than or equal to 1.</p>
<p><code class="ph codeph">src</code>: <a href="abenabap_sql_literals.html">Literal</a> or <a href="abenabap_sql_host_variables.html">host constant</a> with the <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code>, <code class="ph codeph">d</code>, <code class="ph codeph">t</code>, <code class="ph codeph">n</code>, or <code class="ph codeph">string</code> with a maximum of 1333 characters</p></td>
<td><code class="ph codeph">SSTRING</code> if <code class="ph codeph">sql_exp</code> has the type <code class="ph codeph">SSTRING</code>, <code class="ph codeph">SSTRING</code> with undefined length if <code class="ph codeph">len</code> is used as an SQL expression or with a length outside the range of 1 to 1333, otherwise <code class="ph codeph">CHAR</code> with the length of <code class="ph codeph">len</code>.</td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">LTRIM( sql_exp,char )</code></a></td>
<td>String with the content of <code class="ph codeph">sql_exp</code> in which all leading characters that match the characters in <code class="ph codeph">char</code> are removed. Trailing blanks are removed from <code class="ph codeph">sql_exp</code> but are significant in <code class="ph codeph">char</code>.</td>
<td><p><code class="ph codeph">sql_exp</code>: see below</p>
<p><code class="ph codeph">char</code>: <a href="abenabap_sql_literals.html">Literal</a>, <a href="abenabap_sql_host_variables.html">host variable</a>, <a href="abenabap_sql_host_variables.html">host constant</a>, or <a href="abapsql_expr.html">SQL expression</a> with the <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code> or <code class="ph codeph">n</code></p></td>
<td><code class="ph codeph">SSTRING</code> if <code class="ph codeph">sql_exp</code> has the type <code class="ph codeph">SSTRING</code>, otherwise <code class="ph codeph">CHAR</code> with the length of <code class="ph codeph">sql_exp</code></td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">OCCURRENCES_REGEXPR( pcre = pcre, \lbr value = sql_exp[, \lbr case_sensitive = case] )</code></a></td>
<td>Counts all occurrences of a <a href="abenpcre_glosry.html">Perl Compatible Regular Expression</a> (PCRE) <code class="ph codeph">pcre</code> in <code class="ph codeph">sql_exp</code> and returns the number of occurrences. The search is case-sensitive by default, but this can be overridden using the parameter <code class="ph codeph">case</code>.</td>
<td><p><code class="ph codeph">pcre</code>: see below</p>
<p><code class="ph codeph">sql_exp</code>: see below</p>
<p><code class="ph codeph">case</code>: 'X', ' ', or <a href="abensql_null.html">null expression</a></p></td>
<td><code class="ph codeph">INT4</code></td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">REPLACE( sql_exp1,sql_exp2,sql_exp3 )</code></a></td>
<td>String <code class="ph codeph">sql_exp1</code>, in which all instances of <code class="ph codeph">sql_exp2</code> are replaced by the content from <code class="ph codeph">sql_exp3</code>. The replacement of letters is case-sensitive. Trailing blanks are ignored in all arguments. The maximum length of the result is 1333.</td>
<td>See below</td>
<td><code class="ph codeph">SSTRING</code> if an argument has the type <code class="ph codeph">SSTRING</code>, otherwise <code class="ph codeph">CHAR</code> with the maximum possible length of the result.</td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">REPLACE_REGEXPR( pcre = pcre, \lbr value = sql_exp1, \lbr with = sql_exp2[,\lbr occurrence = occ][,\lbr case_sensitive = case][,\lbr start = start] )</code></a></td>
<td>A <a href="abenpcre_glosry.html">Perl Compatible Regular Expression</a> (PCRE) <code class="ph codeph">pcre</code> is replaced in <code class="ph codeph">sql_exp1</code> with the character string specified in <code class="ph codeph">sql_exp2</code>. <code class="ph codeph">occ</code> is optional and determines the number of occurrences of <code class="ph codeph">pcre</code> to be replaced. By default, all occurrences are replaced. The search is case-sensitive by default, but this can be overridden using the parameter <code class="ph codeph">case</code>. The parameter <code class="ph codeph">start</code> specifies the offset from which to start the search.</td>
<td><p><code class="ph codeph">pcre</code>: see below</p>
<p><code class="ph codeph">sql_exp1</code>: see below</p>
<p><code class="ph codeph">sql_exp2</code>: see below</p>
<p><code class="ph codeph">occ</code>: <a href="abenabap_sql_literals.html">Literal</a> or <a href="abenabap_sql_host_variables.html">host constant</a> with the <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">b</code>, <code class="ph codeph">s</code>, <code class="ph codeph">i</code>, or <code class="ph codeph">int8</code> greater than 0 and less than or equal to 1333; <a href="abenexpression_glosry.html">expressions</a> are also possible if they return an integer of type <code class="ph codeph">INT4</code></p>
<p><code class="ph codeph">case</code>: 'X', ' ', or <a href="abensql_null.html">null expression</a></p>
<p><code class="ph codeph">start</code>: <code class="ph codeph">i</code> or <code class="ph codeph">int8</code></p></td>
<td><code class="ph codeph">SSTRING</code></td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">RIGHT( sql_exp,len )</code></a></td>
<td>String of the length <code class="ph codeph">len</code> with the <code class="ph codeph"> len</code> right characters of <code class="ph codeph">arg</code> (ignoring the trailing blanks). The value of <code class="ph codeph">len</code> cannot be greater than the length of <code class="ph codeph">sql_exp</code>.</td>
<td><p><code class="ph codeph">sql_exp</code>: see below</p>
<p><code class="ph codeph">len</code>: <a href="abapsql_expr.html">SQL expression</a> with the <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">b</code>, <code class="ph codeph">s</code>, <code class="ph codeph">i</code>, or <code class="ph codeph">int8</code> greater than 0 and less than or equal to 1333</p></td>
<td><code class="ph codeph">SSTRING</code> if <code class="ph codeph">sql_exp</code> has the type <code class="ph codeph">SSTRING</code>, otherwise <code class="ph codeph">CHAR</code> with the length of the result</td>
<td>x</td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">RPAD( sql_exp,len,src )</code></a></td>
<td>String of the length <code class="ph codeph">len</code> with the left-aligned content of <code class="ph codeph">sql_exp</code> without trailing blanks and in which trailing blanks produced by the expanded string are replaced by the characters from the argument <code class="ph codeph">src</code> (respecting all blanks). Leading blanks from <code class="ph codeph">sql_exp</code> are preserved. If more characters are required than exist in <code class="ph codeph">src</code>, the content of <code class="ph codeph">src</code> is used repeatedly. If <code class="ph codeph">len</code> is less than the length of <code class="ph codeph">sql_exp</code>, it is truncated on the right. If <code class="ph codeph">src</code> is empty and <code class="ph codeph">len</code> is greater than the length of <code class="ph codeph">sql_exp</code>, <code class="ph codeph"> sql_exp</code> remains unchanged.</td>
<td><p><code class="ph codeph">sql_exp</code>: see below</p>
<p><code class="ph codeph">len</code>: <a href="abapsql_expr.html">SQL expression</a> with the <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">b</code>, <code class="ph codeph">s</code>, or <code class="ph codeph">i</code> greater than -2147483648 and less than 67108864. If <code class="ph codeph">len</code> is used as a <a href="abenabap_sql_literals.html">literal</a> or <a href="abenabap_sql_host_variables.html">host constant</a>, the ABAP type <code class="ph codeph">int8</code> is possible too. The result is empty if <code class="ph codeph">len</code> is less than or equal to 0. The length of the result is 1 if <code class="ph codeph">len</code> is used as a constant less than or equal to 1.</p>
<p><code class="ph codeph">src</code>: <a href="abenabap_sql_literals.html">Literal</a> or <a href="abenabap_sql_host_variables.html">host constant</a> with the <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code>, <code class="ph codeph">d</code>, <code class="ph codeph">t</code>, <code class="ph codeph">n</code>, or <code class="ph codeph">string</code> with a maximum of 1333 characters</p></td>
<td><code class="ph codeph">SSTRING</code> if <code class="ph codeph">sql_exp</code> has the type <code class="ph codeph">SSTRING</code>, <code class="ph codeph">SSTRING</code> with undefined length if <code class="ph codeph">len</code> is used as an SQL expression or with a length outside the range of 1 to 1333, otherwise <code class="ph codeph">CHAR</code> with the length of <code class="ph codeph">len</code>.</td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">RTRIM( sql_exp,char )</code></a></td>
<td>String with the content of <code class="ph codeph">sql_exp</code> in which all trailing characters that match the characters in <code class="ph codeph">char</code> are removed. Trailing blanks are removed from <code class="ph codeph">sql_exp</code> but are significant in <code class="ph codeph">char</code>.</td>
<td><p><code class="ph codeph">sql_exp</code>: see below</p>
<p><code class="ph codeph">char</code>: <a href="abenabap_sql_literals.html">Literal</a>, <a href="abenabap_sql_host_variables.html">host variable</a>, <a href="abenabap_sql_host_variables.html">host constant</a>, or <a href="abapsql_expr.html">SQL expression</a> with the <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">c</code> or <code class="ph codeph">n</code></p></td>
<td><code class="ph codeph">SSTRING</code> if <code class="ph codeph">sql_exp</code> has the type <code class="ph codeph">SSTRING</code>, otherwise <code class="ph codeph">CHAR</code> with the length of <code class="ph codeph">sql_exp</code></td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">SUBSTRING( sql_exp,pos,len )</code></a></td>
<td><p>Substring <code class="ph codeph">sql_exp</code> from the position <code class="ph codeph">pos</code> with length <code class="ph codeph">len</code>. <code class="ph codeph">pos</code> and <code class="ph codeph">len</code> must be specified so that the substring is within <code class="ph codeph">sql_exp</code>.</p>
<p>The function is always executed in the table buffer.</p></td>
<td><p><code class="ph codeph">sql_exp</code>: see below</p>
<p><code class="ph codeph">pos</code>: <a href="abapsql_expr.html">SQL expression</a> with the <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">b</code>, <code class="ph codeph">s</code>, <code class="ph codeph">i</code>, <code class="ph codeph">int8</code></p>
<p><code class="ph codeph">len</code>: <a href="abapsql_expr.html">SQL expression</a> with the <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">b</code>, <code class="ph codeph">s</code>, <code class="ph codeph">i</code>, <code class="ph codeph">int8</code></p></td>
<td><p>If <code class="ph codeph">len</code> is a constant:</p>
<p><code class="ph codeph">SSTRING</code> if <code class="ph codeph">sql_exp</code> has the type <code class="ph codeph">SSTRING</code>, otherwise <code class="ph codeph">CHAR</code> with the length of <code class="ph codeph">len</code></p>
<p>If <code class="ph codeph">len</code> is not a constant:</p>
<p>the result has the same data type as the first parameter (<code class="ph codeph">sql_exp</code>)</p></td>
<td>x</td>
</tr>
<tr class="odd">
<td><a href="abensql_functions_string.html"><code class="ph codeph">SUBSTRING_REGEXPR( pcre = pcre, \lbr value = sql_exp[, \lbr occurrence = occ][, \lbr case_sensitive = case][, \lbr start = start][, \lbr group = group] )</code></a></td>
<td><p>Searches <code class="ph codeph">sql_exp</code> for a <a href="abenpcre_glosry.html">Perl Compatible Regular Expression</a> (PCRE) pattern <code class="ph codeph">pcre</code> and returns the matched substring. The other parameters are optional. <code class="ph codeph">occ</code> determines the number of occurrences of <code class="ph codeph">pcre</code>. The search is case-sensitive by default, but this can be overridden using the parameter <code class="ph codeph">case</code>. The parameter <code class="ph codeph">start</code> specifies the offset from which to start the search. The parameter <code class="ph codeph">group</code> specifies the number of the group of the matched substring.</p>
<p>If <code class="ph codeph">occ</code> is not greater than 0 or <code class="ph codeph">start</code> or <code class="ph codeph">group</code> are less than 0, the result is a <a href="abennull_value_glosry.html">null value</a>.</p></td>
<td><p><code class="ph codeph">pcre</code>: see below</p>
<p><code class="ph codeph">sql_exp</code>: see below</p>
<p><code class="ph codeph">occ</code>: <a href="abenabap_sql_literals.html">Literal</a> or <a href="abenabap_sql_host_variables.html">host constant</a> with the <a href="abenbuilt_in_types_complete.html">ABAP type</a> <code class="ph codeph">b</code>, <code class="ph codeph">s</code>, <code class="ph codeph">i</code>, or <code class="ph codeph">int8</code> greater than 0 and less than or equal to 1333; <a href="abenexpression_glosry.html">expressions</a> are also possible if they return an integer of type <code class="ph codeph">INT4</code></p>
<p><code class="ph codeph">case</code>: 'X', ' ', or <a href="abensql_null.html">null expression</a></p>
<p><code class="ph codeph">start</code>: <code class="ph codeph">i</code> or <code class="ph codeph">int8</code></p>
<p><code class="ph codeph">group</code>: <code class="ph codeph">i</code> or <code class="ph codeph">int8</code></p></td>
<td>The same type as <code class="ph codeph">sql_exp</code>.</td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="abensql_functions_string.html"><code class="ph codeph">UPPER( sql_exp )</code></a></td>
<td>String with a length of <code class="ph codeph">sql_exp</code>, in which all lowercase letters were transformed to uppercase letters.</td>
<td>See below</td>
<td><code class="ph codeph">SSTRING</code> if <code class="ph codeph">sql_exp</code> has the type <code class="ph codeph">SSTRING</code>, otherwise <code class="ph codeph">CHAR</code> with the length of <code class="ph codeph">sql_exp</code></td>
<td>x</td>
</tr>
</tbody>
</table>

The arguments `sql_exp`, `sql_exp1`, `sql_exp2`, and `sql_exp3` can be any [SQL expressions](abapsql_expr.md) with the following data types. The possible data types are the [dictionary types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) `CHAR`, `CLNT`, `CUKY`, `DATS`, `LANG`, `NUMC`, `TIMS`, `UNIT`, and `SSTRING` with the following exceptions:

- The type `NUMC` is not allowed for `LIKE_REGEXPR`, `LOCATE_REGEXPR`, `LOCATE_REGEXPR_AFTER`, `OCCURRENCES_REGEXPR`, `REPLACE_REGEXPR` `SUBSTRING_REGEXPR`.

- The types `NUMC`, `DATS` and `TIMS` are not allowed for `INITCAP`, `LOWER`, `UPPER`.

- The types `STRING` and `RAWSTRING` are also allowed for `LENGTH`.

The possible data types for literals, host variables, and host expressions are the ABAP types [assigned](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to the dictionary types above. The result types are also [dictionary types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The argument `pcre` can be any [SQL expression](abapsql_expr.md) or [null expression](abensql_null.md) with an appropriate data type. The possible data types are `CHAR` and `SSTRING`. `pcre` must contain a [Perl Compatible Regular Expression (PCRE)](../../abap-glossary/abenpcre_glosry.md). The operands passed to the argument `pcre` are not interpreted in extended mode. The pattern *?x* can be used to enable extended mode.

If an argument of a string function has the [null value](../../abap-glossary/abennull_value_glosry.md), the result of the full string function is the null value.

## Hints

- In the case of the function `REPLACE`, it should be noted that the maximum possible length of the result can easily reach the allowed length of 1333, which produces a syntax error. In general, the maximum possible length is calculated by dividing the length of `sql_exp1` by the length of `sql_exp2`, multiplied by the length of `sql_exp3`.

- All string functions with the result type `SSTRING` can have a maximum of 1333 characters. This length restriction can be avoided by using the type conversion function [`TO_CLOB`](abensql_type_conv_func.md) on the result, thus converting it to type `STRING`.

- Not all of the parameters that can be specified for the `REPLACE_REGEXPR` function in [ABAP CDS view entities](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_sql_functions_character_v2.md) (`UNGREEDY`, for example) can be specified for ABAP SQL as well. This functionality can be implemented through the [Perl Compatible Regular Expression](../../abap-glossary/abenpcre_glosry.md) syntax itself.

- The functions `LPAD` and `RPAD` can produce the result type `SSTRING` with an undefined length. This result type can be propagated to other expressions and functions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The `SELECT` statement returns the maximum length of a URL in the DDIC database table `SCARR`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT FROM scarr 
       FIELDS MAX( length( url ) ) AS maxlen 
       INTO @FINAL(result). 
 
out->display( result ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Concatenation of multiple columns of a DDIC database table to a character-like column in the class `CL_DEMO_SQL_FUNCTION_CONCAT` using `CONCAT`. An alignment is achieved using `LPAD` and `RPAD`. A concatenation of this type is not possible using the operator [`&&`](abensql_string.md).

``` abap
SELECT CONCAT_WITH_SPACE( CONCAT( carrid, 
                          LPAD( carrname,21,' ' ) ), 
                          RPAD( url,40,' ' ), 3 ) AS line 
       FROM scarr 
       INTO TABLE @FINAL(result).
```

## Executable Examples

- [String functions](abensql_string_func_abexa.md)

- [SQL expressions, concatenations](abensql_expr_string_abexa.md)
