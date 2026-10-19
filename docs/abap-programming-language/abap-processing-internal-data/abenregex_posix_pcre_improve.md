---
title: "regex - New Features in PCRE Compared to POSIX"
source_file: abenregex_posix_pcre_improve.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Regular Expressions (regex) > regex - Migrating from POSIX to PCRE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# regex - New Features in PCRE Compared to POSIX

While topic [Incompatibilities between POSIX and PCRE](abenregex_posix_pcre_incompat.md) deals with incompatibilities and missing features when migrating from POSIX to PCRE, it is also worth taking a look at the vast array of new features PCRE has to offer.

An introduction to some of these features is provided in the following, the list is however far from complete.

- [Making Use of New Features for Patterns](abenregex_posix_pcre_improve.md#making-use-of-new-features-for-patterns)

  - [Lazy Quantifiers](abenregex_posix_pcre_improve.md#lazy-quantifiers)

  - [Look-behind Assertions](abenregex_posix_pcre_improve.md#look-behind-assertions)

  - [Multiline Mode](abenregex_posix_pcre_improve.md#multiline-mode)

  - [Named Capture Groups](abenregex_posix_pcre_improve.md#named-capture-groups)

  - [Subroutine Calls and Recursion](abenregex_posix_pcre_improve.md#subroutine-calls-and-recursion)

  - [Callouts](abenregex_posix_pcre_improve.md#callouts)

- [Making Use of New Features for Replacements](abenregex_posix_pcre_improve.md#making-use-of-new-features-for-replacements)

  - [Conditional Substitution](abenregex_posix_pcre_improve.md#conditional-substitution)

  - [Case Conversion](abenregex_posix_pcre_improve.md#case-conversion)

## Making Use of New Features for Patterns

### Lazy Quantifiers

The most obvious downside of POSIX regular expressions in ABAP is the lack of lazy (also known as non-greedy or reluctant) quantifiers.

In PCRE a quantifier can be made lazy by adding a trailing [`?:`](abenregex_pcre_syntax_specials.md):

| **Description**                                | **PCRE Syntax** |
|------------------------------------------------|-----------------|
| 0 or 1, preferred 0                            | `??`            |
| 0 or more, as few as possible                  | `*?`            |
| 1 or more, as few as possible                  | `+?`            |
| at least n, no more than m, as few as possible | `{n,m}?`        |
| at least n, as few as possible                 | `{n,}?`         |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Difference between greedy and non-greedy behavior,

``` abap
FINAL(greedy_result) = 
  match( val = `<body><div></div></body>` pcre = `<(.+)>` ). 
  " --> '<body><div></div></body>' 
FINAL(lazy_result) = 
  match( val = `<body><div></div></body>` pcre = `<(.+?)>` ). 
  " --> '<body>'
```

### Look-behind Assertions

| **Description**                                                                                             | **PCRE Syntax** |
|-------------------------------------------------------------------------------------------------------------|-----------------|
| positive look-behind assertion; succeeds if the current match position is preceded by the given pattern     | `(?<=...)`      |
| negative look-behind assertion; succeeds if the current match position is not preceded by the given pattern | `(?<!...)`      |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Leading and trailing look-behind assertions, like look-ahead assertions, are not part of the actual match.

``` abap
FINAL(result1) = find( val = `meter`      pcre = `(?<!centi)meter` ). 
                " --> found; matches whole string 
FINAL(result2) = find( val = `millimeter` pcre = `(?<!centi)meter` ). 
                " --> found; match starts at offset 5 
FINAL(result3) = find( val = `centimeter` pcre = `(?<!centi)meter` ). 
               " --> not found
```

### Multiline Mode

In some scenarios it is necessary to respect line feeds during matching, e.g. matching something only if it is located at the beginning of a line. PCRE makes this very convenient by providing a large amount of control over the handling of multiple lines in the matching process.

When creating a regular expression using method `CREATE_PCRE` of system class [`CL_ABAP_REGEX`](abenregex_system_classes.md) multi line handling can be controlled by the following parameters:

| **Parameter**      | **Description**                                                                                                                                                                                                           |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DOT_ALL`          | single line mode; if enabled, special character `.` also matches line feed characters                                                                                                                                     |
| `ENABLE_MULTILINE` | multi line mode; if enabled, special characters `^` and `$` not only match the start and the end of the character string, but also the start and the end of a line respectively; a line is ended by a line feed character |
| `NEWLINE_MODE`     | controls what gets recognized as a line feed character                                                                                                                                                                    |

Despite their names, single line and multi line mode are not mutually exclusive and can be combined.

It is also possible to set these options directly in the pattern, which is especially useful for regular expressions used in statements [`FIND`](abapfind.md) and [`REPLACE`](abapreplace.md) behind [`PCRE`](abapfind_pattern.md) or in built-in functions behind [`pcre`](abenstring_functions_regex.md):

- Single line mode can be enabled using the option setting syntax [`(?s)`](abenregex_pcre_syntax_specials.md), valid for the following part of the group in which it is specified.

- Multi line mode can be enabled using the option setting syntax [`(?m)`](abenregex_pcre_syntax_specials.md), valid for the following part of the group in which it is specified.

- What gets recognized as a line feed character can be controlled by the following syntax that can only appear at the start of the pattern:

  - [`(*CR)`](abenregex_pcre_syntax_specials.md) carriage return only

  - [`(*LF)`](abenregex_pcre_syntax_specials.md) linefeed only

  - [`(*CRLF)`](abenregex_pcre_syntax_specials.md) carriage return followed by linefeed

  - [`(*ANYCRLF)`](abenregex_pcre_syntax_specials.md) all three of the above

  - [`(*ANY)`](abenregex_pcre_syntax_specials.md) any Unicode line feed sequence

  - [`(*NUL)`](abenregex_pcre_syntax_specials.md) the `NUL` character (binary zero)

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

While the first regular expression matches only the beginning of the character string, the second one also matches the beginning of new lines that are defined by the syntax [`\n`](abenstring_templates_separators.md) for line feeds in a string template.

``` abap
FINAL(result1) = replace( val  = |xxx\nyyy\nzzz| 
                         pcre = `^` 
                         with = `_` 
                         occ = 0 ). 
                " --> _xxx\nyyy\nzzz 
 
FINAL(result2) = replace( val  = |xxx\nyyy\nzzz| 
                         pcre = `(*LF)(?m)^` 
                         with = `_` 
                         occ = 0 ). 
                " --> _xxx\n_yyy\n_zzz
```

### Named Capture Groups

PCRE supports the naming of capture groups, meaning you can assign a name to a capture group, e.g. using the [`(?<name>...)`](abenregex_pcre_syntax_specials.md) syntax. You can refer to a named capture group by its name, e.g. in a backreference using the [`\k<name>`](abenregex_pcre_syntax_specials.md) syntax.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The regular expression matches the character string. The capture group is used by its name to match further occurrences of the pattern defined for the group.

``` abap
ASSERT matches( val  = `foobarfoo` 
                pcre = `(?<my_group>foo)bar\k<my_group>` ).
```

### Subroutine Calls and Recursion

Apart from referring to the content of a group via backreferences, PCRE supports calling groups as subroutines using the [`(?n)`](abenregex_pcre_syntax_specials.md) syntax. It is also possible to call a named group as a subroutine, e.g. using the [`(?&name)`](abenregex_pcre_syntax_specials.md) syntax.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows the calling of groups as subroutines in three blocks:

- In the first block, the backreference [`\1`](abenregex_pcre_syntax_specials.md) simply matches whatever the first capture group actually matched most recently, instead of matching all the things the capture group could match.

- The second block shows, how this behavior can be achieved by calling the group as a subroutine using the [`(?n)`](abenregex_pcre_syntax_specials.md) syntax.

- The third block shows, how by recursing over the whole pattern using the [`(?R)`](abenregex_pcre_syntax_specials.md) syntax in one branch of the alternation, it is ensured that there is a balanced but arbitrary number of opening (`\(`) and closing (`\)`) parentheses to either side of the digits. Note that the pattern makes use of the possessive quantifier `++` that acts the same as `+` but prevents backtracking into what was matched by the quantifier.

``` abap
ASSERT matches( 
  val  = `sense and sensibility` 
  pcre = `(sens|respons)e\ and\ \1ibility` ). 
ASSERT matches( 
  val  = `response and responsibility` 
  pcre = `(sens|respons)e\ and\ \1ibility` ). 
ASSERT NOT matches( 
  val = `sense and responsibility` 
  pcre = `(sens|respons)e\ and\ \1ibility` ). 
ASSERT NOT matches( 
  val = `response and sensibility` 
  pcre = `(sens|respons)e\ and\ \1ibility` ). 
 
ASSERT matches( 
  val  = `sense and sensibility` 
  pcre = `(sens|respons)e\ and\ (?1)ibility` ). 
ASSERT matches( 
  val  = `response and responsibility` 
  pcre = `(sens|respons)e\ and\ (?1)ibility` ). 
ASSERT matches( 
  val  = `sense and responsibility` 
  pcre = `(sens|respons)e\ and\ (?1)ibility` ). 
ASSERT matches( 
  val = `response and sensibility` 
  pcre = `(sens|respons)e\ and\ (?1)ibility` ). 
 
ASSERT matches( 
  val  = `(((123456)))` 
  pcre = `\( ( \d++ | (?R) ) \)` ). 
ASSERT matches( 
  val  = `((((((123456))))))` 
  pcre = `\( ( \d++ | (?R) ) \)` ). 
ASSERT NOT matches( 
  val  = `((((((123456)))` 
  pcre = `\( ( \d++ | (?R) ) \)` ).
```

### Callouts

Callouts are another powerful feature. It invokes ABAP code from within the pattern during the matching process, passing data from the pattern to the callout routine.

Callouts are achieved with the [`(?C...)`](abenregex_pcre_syntax_specials.md). A callout routine cannot only access the numeric data `n` provided by the callout `(?Cn)` or the string data `str` provided by the callout `(?C"str")`, but also a lot of other properties and information about the current matcher state.

### Executable Example

[PCRE Regular Expression with Callouts](abenpcre_callout_abexa.md)

## Making Use of New Features for Replacements

### Conditional Substitution

PCRE's conditional substitution syntax allows you to check if a certain capture group did participate in the match, specifying different replacement strings for when it did and did not participate.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conditional substitutions with [`{id...}`](abenregex_pcre_syntax_specials.md).

``` abap
FINAL(result1) = replace( val  =  `male` 
                         pcre = `(fe)?male` 
                         with = `${1:+her:his} majesty` ). 
                         " --> 'his majesty' 
FINAL(result2) = replace( val  = `female` 
                         pcre = `(fe)?male` 
                         with = `${1:+her:his} majesty` ). 
                         " --> 'her majesty'
```

### Case Conversion

Using the [`\u`](abenregex_pcre_syntax_specials.md), [`\U`](abenregex_pcre_syntax_specials.md), [`\l`](abenregex_pcre_syntax_specials.md) and [`\L`](abenregex_pcre_syntax_specials.md) modifiers in the PCRE replacement string, the case of the inserted text can be converted to uppercase or lowercase. While `\u` and `\l` only affect the first character following them, `\U` and `\L` affect all following characters, until a different case conversion modifier or the termination operator `\E` is reached.

The case conversion syntax can also be combined with conditional substitution.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Replacements with case conversions. The latter two use conditional substitutions.

``` abap
FINAL(result) = replace( 
  val  = `thEsE aRe noT THe dROiDs YoU arE loOKInG FOr` 
  pcre = `(\w)(\w*)` with = `\u$1\L$2` occ = 0 ). 
         " --> 'These Are Not The Droids You Are Looking For' 
 
FINAL(result1) = replace( 
  val  = `body` 
  pcre = `(some)?(body)` with = `${1:+\U:\L}HeLLo` ). 
  " --> 'hello' 
FINAL(result2) = replace( 
  val  = `somebody` 
  pcre = `(some)?(body)` with = `${1:+\U:\L}HeLLo` ). 
  " --> 'HELLO'
```
