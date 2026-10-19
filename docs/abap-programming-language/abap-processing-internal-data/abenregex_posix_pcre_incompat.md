---
title: "regex - Incompatibilities Between POSIX and PCRE"
source_file: abenregex_posix_pcre_incompat.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Regular Expressions (regex) > regex - Migrating from POSIX to PCRE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# regex - Incompatibilities Between POSIX and PCRE

This topics lists all features of POSIX regular expressions that cannot be reused directly in PCRE but require some migration effort by rewriting the regular expressions.

- [Migrating Patterns](abenregex_posix_pcre_incompat.md#migrating-patterns)

  - [Fundamental Differences](abenregex_posix_pcre_incompat.md#fundamental-differences)

  - [Significance of Whitespaces in Patterns](abenregex_posix_pcre_incompat.md#significance-of-whitespaces-in-patterns)

  - [Meaning of the Dot](abenregex_posix_pcre_incompat.md#meaning-of-the-dot)

  - [Comments](abenregex_posix_pcre_incompat.md#comments)

  - [Unicode Handling](abenregex_posix_pcre_incompat.md#unicode-handling)

  - [Matching Uppercase and Lowercase Letters](abenregex_posix_pcre_incompat.md#matching-uppercase-and-lowercase-letters)

  - [Matching All Unicode Characters](abenregex_posix_pcre_incompat.md#matching-all-unicode-characters)

  - [Word Anchors](abenregex_posix_pcre_incompat.md#word-anchors)

- [Migrating Replacement Strings](abenregex_posix_pcre_incompat.md#migrating-replacement-strings)

  - [Substituting the Whole Match](abenregex_posix_pcre_incompat.md#substituting-the-whole-match)

  - [Substituting Parts Around the Match](abenregex_posix_pcre_incompat.md#substituting-parts-around-the-match)

## Migrating Patterns

For the most part the features supported by PCRE form a superset of the features supported by POSIX. There are however some key differences and missing features, which are outlined in the following sections.

### Fundamental Differences

Both PCRE and POSIX use a regex-directed, backtracking algorithm, meaning both implementations will in most cases yield the same result. There is however a crucial difference: PCRE will always return the leftmost match, while POSIX aims to return the leftmost longest match, meaning that if multiple possible matches start at the same offset, the longest of those is returned.

If you are making use of the leftmost longest matching rule in POSIX, you may need to reorder or rewrite parts of your regular expression to achieve the same results in PCRE.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

PCRE stops after finding the first (leftmost) match, while POSIX also tries the other match starting at the same position and, as it is longer, considers it the better match.

``` abap
FINAL(pcre_result) = 
  match( val   = `unfoldable` 
         pcre  = `un(fold|foldable)` ). 
         " --> returns 'unfold' 
FINAL(posix_result) = 
  match( val   = `unfoldable` 
         regex = `un(fold|foldable)` ) ##regex_posix. 
         " --> returns 'unfoldable'
```

To also return the longest match in the PCRE case, the example above can be rewritten as follows, reordering the alternations:

``` abap
FINAL(pcre_result) = 
  match( val   = `unfoldable` 
         pcre  = `un(foldable|fold)` ). 
         " --> returns 'unfoldable'
```

However the different matching strategies do not only affect alternations introduced by `|`, but all cases where multiple matches start at the same location, for example using the `?` quantifier:

``` abap
FINAL(pcre_result) = 
  match( val = `unfoldable` 
         pcre  = `un(fold)?(foldable)?` ). 
         " --> returns 'unfold' 
 
FINAL(posix_result) = 
  match( val   = `unfoldable` 
         regex = `un(fold)?(foldable)?` ) ##regex_posix. 
         " --> returns 'unfoldable'
```

In this case, a look-ahead assertion can be used to also return the longest match in the PCRE case:

``` abap
FINAL(pcre_result) = 
  match( val  = `unfoldable` 
         pcre = `un(fold(?!able))?(foldable)?` ). 
         " --> returns 'unfoldable'
```

### Significance of Whitespaces in Patterns

By default PCRE syntax is compiled in an extended mode on AS ABAP: Most unescaped whitespace (blanks and line breaks) of the pattern are ignored outside character classes. In order to include whitespace into a pattern, they must be escaped. In order to explicitly match whitespaces in PCRE's extended mode, there are the following options:

- Escape the whitespace in the pattern. The pattern `Hello\ World` matches `Hello World`.

- Match all whitespaces using the special character [`\s`](abenregex_pcre_syntax_specials.md). `Hello\sWorld` matches `Hello World`. The same applies to `Hello \s World`, which might be more readable.

While the extended mode allows you to write more readable regular expressions, it can be a bit confusing at first, especially when migrating POSIX regular expressions. The extended mode of PCRE can be switched of as follows:

- By passing `ABAP_FALSE` to the parameter `EXTENDED` when creating a PCRE regular expression with method `CREATE_PCRE` of class [`CL_ABAP_REGEX`](abenregex_system_classes.md).

- By using the special character [`(?-x)`](abenregex_pcre_syntax_specials.md) in the pattern itself. This also works for the addition [`PCRE`](abapfind_pattern.md) in statements and the parameter [`pcre`](abenstring_functions_regex.md) in string functions.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The extended mode for PCRE is enabled when using parameter `pcre` in the following function. This means that whitespace characters are handled as not significant when the pattern is evaluated. The PCRE regular expression does not match the string `Hello World`.

``` abap
ASSERT NOT 
  matches( val = `Hello World` pcre  = `Hello World` ). 
 
ASSERT 
  matches( val = `Hello World` regex = `Hello World` ) ##regex_posix.
```

The string `HelloWorld` however is matched by PCRE but not by POSIX:

``` abap
ASSERT 
  matches( val = `HelloWorld` pcre  = `Hello World` ). 
 
ASSERT NOT 
  matches( val = `HelloWorld` regex = `Hello World` ) ##regex_posix.
```

The following example finally shows, how the extended mode can be switched of in built-in string functions:

``` abap
ASSERT 
  matches( val = `Hello World` pcre  = `(?-x)Hello World` ).
```

### Meaning of the Dot

In contrast to POSIX, where the dot (`.`) matches anything, in PCRE the dot by default matches everything but line breaks. The control characters that are interpreted as a line break in PCRE can be defined with the parameter `NEWLINE_MODE` of method `CREATE_PCRE` of class `CL_ABAP_REGEX` or by prefixing the regular expression with the respective [special control verb](abenregex_pcre_syntax_specials.md).

In order to achieve the same behavior as for a POSIX regular expression, either the parameter `DOT_ALL` of method `CREATE_PCRE` of class `CL_ABAP_REGEX` can be set or `(?s)` can be used in the regular expression.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the first regular expression, the line break is not replaced by the character *x*. In the regular expression with POSIX syntax and in the regular expression with PCRE syntax using `(?s)` it is replaced.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(pcre_result1) = replace( val = |Hello\nWorld| pcre  = `.` 
                              with = `x` occ = 0 ). 
DATA(posix_result) = replace( val = |Hello\nWorld| regex = `.` 
                              with = `x` occ = 0 ) ##regex_posix. 
DATA(pcre_result2) = replace( val = |Hello\nWorld| pcre  = `(?s).` 
                              with = `x` occ = 0 ). 
 
out->write( pcre_result1 
  )->write( posix_result 
  )->write( pcre_result2 
  )->display( ).
```

### Comments

In the extended mode of PCRE, comments can be placed behind an unescaped `#`. In order to include the character `#` into a pattern in PCRE's extended mode, it must be escaped:

The pattern `Hello\#World` matches `Hello#World`.

The extended mode of PCRE can be switched of as explained in the preceding topic.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The extended mode for PCRE is enabled when using parameter `pcre` in the following function. This means that the character `#` introduces a comment. The first PCRE regular expression does not match the string `Hello#World`. A POSIX regular expression and the second and third PCRE regular expression where `#` is escaped or the extended mode is switched off match the string.

``` abap
ASSERT NOT 
  matches( val = `Hello#World` pcre  = `Hello#World` ). 
 
ASSERT 
  matches( val = `Hello#World` regex = `Hello#World` ) ##regex_posix. 
 
ASSERT 
  matches( val = `Hello#World` pcre  = `Hello\#World` ). 
 
ASSERT 
  matches( val = `Hello#World` pcre  = `(?-x)Hello#World` ).
```

### Unicode Handling

For the representation of character strings, the ABAP programming language supports the two byte [Unicode character representation](../../abap-glossary/abenunicode_char_represent_glosry.md) [UCS-2](../../abap-glossary/abenucs2_glosry.md). The [system code page](../../abap-glossary/abensystem_codepage_glosry.md) of an AS ABAP is [UTF-16](../../abap-glossary/abenutf16_glosry.md), that supports all characters of the Unicode standard. UCS-2 is a subset of UTF-16 that supports the so called Basic Multilingual Plane (BMP) of the Unicode standard. In UTF-16, the other Unicode planes are encoded as [surrogates](../../abap-glossary/abensurrogates_glosry.md) ( [surrogate pairs](../../abap-glossary/abensurrogate_pair_glosry.md)) in the [surrogate area](../../abap-glossary/abensurrogate_area_glosry.md).

POSIX regular expressions always assume UCS-2 and handle characters that are represented by surrogate pairs as two separate characters what might lead to unexpected results. Unlike POSIX, PCRE can handle character strings as both UCS-2 or UTF-16. This can be configured in different ways depending on the type of regular expression operation performed:

<table>
<thead>
<tr class="header">
<th><strong>Operation</strong></th>
<th><strong>Description</strong></th>
<th><strong>Default Behavior</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Methods of system classes <a href="abenregex_system_classes.html"><code class="ph codeph">CL_ABAP_REGEX</code></a> and <a href="abenregex_system_classes.html"><code class="ph codeph">CL_ABAP_MATCHER</code></a></td>
<td><p>Unicode handling is controlled by parameter <code class="ph codeph">UNICODE_HANDLING</code> of factory method <code class="ph codeph">CREATE_PCRE</code>. The following values can be passed:</p>
<p><code class="ph codeph">STRICT</code> - handle character string as UTF-16, raise an exception upon encountering invalid UTF-16 (broken surrogate pairs)</p>
<p><code class="ph codeph">IGNORE</code> - handle character string as UTF-16, ignore invalid UTF-16; parts of the input that are not valid UTF-16 cannot be matched in any way</p>
<p><code class="ph codeph">RELAXED</code> - handle character string as UCS-2; special character <code class="ph codeph">\C</code> is enabled in patterns, the matching of surrogate pairs by their Unicode code point is however no longer possible</p></td>
<td><code class="ph codeph">STRICT</code></td>
</tr>
<tr class="even">
<td><p>Addition <a href="abapfind_pattern.html"><code class="ph codeph">PCRE</code></a> of statements <a href="abapfind.html"><code class="ph codeph">FIND</code></a> and <a href="abapreplace.html"><code class="ph codeph">REPLACE</code></a>,</p>
<p>Parameter <a href="abenstring_functions_regex.html"><code class="ph codeph">pcre</code></a> of built-in functions for strings</p></td>
<td>No addition exists to control Unicode handling, instead the syntax <code class="ph codeph">(*UTF)</code> can be specified at the start of the pattern to switch on the strict mode (see above)</td>
<td>Without <code class="ph codeph">(*UTF)</code> the relaxed mode (see above) is used, the special character <code class="ph codeph">\C</code> can however not be used</td>
</tr>
</tbody>
</table>

The following table gives a quick overview of which Unicode mode to use when migrating a pattern from POSIX to PCRE:

| **Operation**                                                                                                                     | **Handle Input as UCS-2 or UTF-16?** | **Accept Invalid UTF-16?** | **Action**                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Methods of system classes [`CL_ABAP_REGEX`](abenregex_system_classes.md) and [`CL_ABAP_MATCHER`](abenregex_system_classes.md) | UTF-16                               | Yes                        | Set `UNICODE_HANDLING` to `IGNORE`                                                                                                            |
| Methods of system classes [`CL_ABAP_REGEX`](abenregex_system_classes.md) and [`CL_ABAP_MATCHER`](abenregex_system_classes.md) | UTF-16                               | No                         | Set `UNICODE_HANDLING` to `STRICT` (default)                                                                                                  |
| Methods of system classes [`CL_ABAP_REGEX`](abenregex_system_classes.md) and [`CL_ABAP_MATCHER`](abenregex_system_classes.md) | UCS-2 (ABAP default)                 | \-                         | Set `UNICODE_HANDLING` to `RELAXED`                                                                                                           |
| Statements and built-in functions                                                                                                 | UTF-16                               | Yes                        | This cannot be achieved with the addition `PCRE` of statements and the parameter `pcre` of built-in functions; use objects of `CL_ABAP_REGEX` |
| Statements and built-in functions                                                                                                 | UTF-16                               | No                         | Add syntax `(*UTF)` to the pattern                                                                                                            |
| Statements and built-in functions                                                                                                 | UCS-2 (ABAP default)                 | \-                         | No action required, relaxed mode is default                                                                                                   |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The special character `.` matches two UCS-2 characters in the first two replacements, even though they form a surrogate pair for a a single UTF-16 character. The third replacement uses `(*UTF)` at the beginning of a PCRE regular expression and only the UTF-16 character is matched and replaced.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(surrogate_pair) = cl_abap_codepage=>convert_from( 
  codepage = 'UTF-8' 
  source    = CONV xstring( 'F09F91BD' ) ). 
                            "U+1F47D, EXTRATERRESTRIAL ALIEN 
 
out->write_text( surrogate_pair 
  )->write_text( replace( val = surrogate_pair 
                          regex = `.` 
                          with = `Alien` occ = 0 ) ##regex_posix 
  )->write_text( replace( val = surrogate_pair 
                          pcre = `.` 
                          with = `Alien` occ = 0 ) 
  )->write_text( replace( val = surrogate_pair 
                          pcre = `(*UTF).` 
                          with = `Alien` occ = 0 ) 
  )->display( ).
```

### Matching Uppercase and Lowercase Letters

PCRE does not directly support the POSIX syntax [`\u`](../abap-obsolete-language-elements/abenregex_posix_syntax_specials.md) and [`\l`](../abap-obsolete-language-elements/abenregex_posix_syntax_specials.md) to match an uppercase and lowercase letter respectively. This includes the corresponding negations [`\U`](../abap-obsolete-language-elements/abenregex_posix_syntax_specials.md) and [`\L`](../abap-obsolete-language-elements/abenregex_posix_syntax_specials.md).

As an alternative PCRE's [`\p{xx}`](abenregex_pcre_syntax_specials.md) and [`\P{xx}`](../abap-obsolete-language-elements/abenregex_posix_syntax_specials.md) syntax can be used to match characters having certain Unicode character properties:

| **Description**         | **POSIX Syntax** | **PCRE Syntax** |
|-------------------------|------------------|-----------------|
| uppercase letter        | `\u`             | `\p{Lu}`        |
| not an uppercase letter | `\U`             | `\P{Lu}`        |
| lowercase letter        | `\l`             | `\p{Ll}`        |
| not a lowercase letter  | `\L`             | `\P{Ll}`        |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following replacements yield the same result.

``` abap
ASSERT replace( val = `uuuUuuu` regex = `\u` with = `X` ) ##regex_posix 
     = replace( val = `uuuUuuu` pcre = ` \p{Lu} ` with = `X` ). 
       " --> uuuXuuu
```

### Matching All Unicode Characters

While PCRE supports most of the named sets available in the POSIX syntax, there is one exception: [`[[:unicode:]]`](abenregex_posix_syntax_specials.html), which matches any character whose code is greater than 255.

Depending on the context there are different ways to achieve the same behavior in PCRE:

| **POSIX Syntax**    | **PCRE Syntax**            | **Description**                                                                                                                                                                                                                                                                                                                     |
|---------------------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `[[:unicode:]]`     | `[^\x{00}-\x{ff}]`         | a standalone `[[:unicode:]]` can be replaced by the negation of the range of characters from `0x00` to `0xff`                                                                                                                                                                                                                       |
| `[^[:unicode:]]`    | `[\x{00}-\x{ff}]`          | similarly, a standalone `[^[:unicode:]]` can be replaced by the range of characters from `0x00` to `0xff`                                                                                                                                                                                                                           |
| `[[:unicode:]...]`  | `[\x{100-\xffff}...]`      | if `[[:unicode:]]` is used in conjunction with other elements in a character class, the range of characters has to be specified explicitly (not by negation); when the regular expression is to be executed in a non-UTF-16 context ( `UNICODE_HANDLING` is set to `RELAXED`), this is the character range from `0x100` to `0xffff` |
| `[[:unicode:]...]`  | `[\x{100}-\x{10ffff}...]`  | in a UTF-16 context (`UNICODE_HANDLING` is set to `STRICT` or `IGNORE`) this range becomes `0x100` to `0x10ffff`                                                                                                                                                                                                                    |
| `[^[:unicode:]...]` | `[^\x{100}-\x{ffff}...]`   | similarly, when the `[[:unicode:]]` is used in conjunction with other elements in a negated character class, the range from `0x100` to `0xffff` for a non-UTF-16 context has to be specified explicitly                                                                                                                             |
| `[^[:unicode:]...]` | `[^\x{100}-\x{10ffff}...]` | in a UTF-16 context this range becomes `0x100` to `0x10ffff`                                                                                                                                                                                                                                                                        |

Alternatively, if you only care about the character range from 0 to 127, or the negation thereof, you can use the POSIX named set `[[:ascii:]]` available in PCRE. Using PCRE's negative POSIX named set syntax `([[:^ascii:]])`, you can match non-ASCII characters. The negative POSIX named set syntax can also be used in negated character classes, allowing for a lot of flexibility.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following searches yield the same result.

``` abap
FINAL(c_circumflex) = cl_abap_codepage=>convert_from( 
  source = CONV xstring( 'C488' ) ). 
 
FINAL(text) = `xxx` && c_circumflex && `xxx`. 
 
ASSERT find( val = text regex = `[[:unicode:]]` ) ##regex_posix 
     = find( val = text pcre  = `[^\x{00}-\x{ff}]` ). 
       " --> 3
```

### Word Anchors

PCRE does not directly support the POSIX syntax [`\<`](../abap-obsolete-language-elements/abenregex_posix_syntax_specials.md) and [`\>`](../abap-obsolete-language-elements/abenregex_posix_syntax_specials.md) to match the start and end of a word respectively. As an alternative the word anchor [`\b`](abenregex_pcre_syntax_specials.md) (which matches the start and the end of a word) can be used in conjunction with a look-ahead or look-behind assertion. Alternatively, a special character set can be used.

\|Description\|**POSIX Syntax**\|**PCRE Syntax** \| \|:---\|:---\| \|start of word\|`\<`\|`\b(?=\w)` or `[[:<:]]` \| \|end of word\|`\>`\|`\b(?<=\w)` or `[[:>:]]`\|

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following replacements yield the same result.

``` abap
FINAL(text) = `xxx yyy zzz`. 
 
ASSERT replace( val  = text regex = `\>` ##regex_posix 
                with = `-`  occ = 0 ) 
    =  replace( val   = text pcre =  `\b(?<=\w)` 
                with  = `-`  occ = 0 ). 
 
ASSERT replace( val  = text regex = `\>` ##regex_posix 
                with = `-`  occ = 0 ) 
    =  replace( val  = text pcre =  `[[:>:]]` 
                with = `-`  occ = 0 ). 
 
       " --> xxx- yyy- zzz-
```

## Migrating Replacement Strings

Apart from referring to the content of a capture group by its number (`$1`, `$2`, `$3`, ...), the replacement string syntax and capabilities of PCRE are quite different to those of POSIX.

### Substituting the Whole Match

POSIX offers both [`$0`](../abap-obsolete-language-elements/abenregex_posix_syntax_specials.md) and [`$&`](../abap-obsolete-language-elements/abenregex_posix_syntax_specials.md) as placeholders for the whole match in the replacement string. PCRE only supports the former syntax [`$0`](abenregex_pcre_syntax_specials.md), with the latter syntax `$&` raising an exception. If you are using `$&` in your POSIX patterns, simply replace it with [`$0`](abenregex_pcre_syntax_specials.md) when migrating to PCRE.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following replacements yield the same result.

``` abap
ASSERT 
  replace( val = `abc` regex = `a(b)c` with = `$0$&` ) ##regex_posix 
= replace( val = `abc` pcre  = `a(b)c` with = `$0$0` ). 
  " --> 'abcabc'
```

### Substituting Parts Around the Match

POSIX supports ``` $`` and [ ```\$'\`](../abap-obsolete-language-elements/abenregex_posix_syntax_specials.md) as placeholders for the text in front of and after the match respectively. PCRE does not offer any directly equivalent functionality. If your pattern makes use of these POSIX features, you can however try to emulate them, e.g. by introducing additional capture groups

There are however limitations to this approach. If your pattern or replacement string is more complex, you may have to either perform the replacement manually (using string operations and the offset and length obtained from the match), or keep your POSIX pattern with the `##regex_posix` pragma.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following replacements yield the same result.

``` abap
ASSERT 
  replace( val   = `again and` 
           regex = `and` 
           with  = '$0 $`' )    ##regex_posix 
= replace( val   = `again and` 
           pcre  = `^(.+?)and` 
           with  = `$0 $1` ). 
  " --> 'again and again'
```
