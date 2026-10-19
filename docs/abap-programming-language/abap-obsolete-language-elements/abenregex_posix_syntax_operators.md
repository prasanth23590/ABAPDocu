---
title: "POSIX regex - Character String Patterns (obsolete)"
source_file: abenregex_posix_syntax_operators.html
section: "ABAP Programming Language > ABAP - Obsolete Language Elements > Obsolete Processing of Internal Data > Obsolete Character String and Byte String Processing > Obsolete Regular Expression Syntax > regex - POSIX Syntax (obsolete)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# POSIX regex - Character String Patterns (obsolete)

Character strings are represented by chainings or operators.

- [Chainings](abenregex_posix_syntax_operators.md#chainings)

- [Operators for Character Strings](abenregex_posix_syntax_operators.md#operators-for-character-strings)

  - [Chaining Operators](abenregex_posix_syntax_operators.md#chaining-operators)

  - [Alternatives](abenregex_posix_syntax_operators.md#alternatives)

  - [Subgroups](abenregex_posix_syntax_operators.md#subgroups)

  - [Subgroups with Registration](abenregex_posix_syntax_operators.md#subgroups-with-registration)

  - [Literal Characters](abenregex_posix_syntax_operators.md#literal-characters)

  - [Reserved Enhancements](abenregex_posix_syntax_operators.md#reserved-enhancements)

## Chainings

Chainings are valid regular expressions that are written after each other. If `r` and `s` are regular expressions, the chaining `rs` matches all character strings that can be formed from the chaining of character strings that match `r` and `s`.

## Operators for Character Strings

These operators consist of the special characters `{`, `}`, `*`, `+`, `?`, `|`, `(`, `)`, and `\`. The special characters can be made into literal characters using the prefix `\` or by enclosing with `\Q ... \E`.

### Chaining Operators

The operators `{n}`, `{n,m}`, `*`, `+`, and `?` (where `n` and `m` are natural numbers, including zero) can be written directly after a regular expression `r`, and thus create chainings `rrr...` of the regular expression:

- The regular expression `r{n}` is equivalent to an n-fold chaining of `r`. The regular expression `r{0}` matches an empty character string, and therefore also the offset before the first character of a character string, the spaces between the characters in character strings, and the offset after the last character in a character string.

- The regular expression `r{n,m}` is equivalent to at least n and a maximum of m chainings of `r`. The value of n must be less than or equal to the value of m. The expression `r{n}` is equivalent to at least an n-fold chaining of `r`.

- The regular expression `r?` is equivalent to `r{0,1}`, which means the expression `r` or the empty character string.

- The regular expression `r*` is equivalent to `r{0,}`, in other words a chaining of `r` of any length, including the empty character string. When using subgroups (see below), and in a [text search](abenregex_posix_search.md), `r*` matches the longest possible substring (greedy behavior).

- The regular expression `r+` is equivalent to `r{1,}`, in other words a chaining of any length of `r` excluding the empty character string. When using subgroups, and in a text search, `r+` matches the longest possible substring (greedy behavior).

- The regular expressions `r{n,m}?`, `r*?` and `r+?` are reserved for future language enhancements (economical behavior) and currently raise the exception `CX_SY_INVALID_REGEX`.

### Hint

For a regular expression with chaining operators, the primary rule is that the entire expression must match if possible. This rule restricts the length of character strings that match the chaining with the operators `*` and `+` and therefore their greedy behavior.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first subexpression `a+` is compared with the first five characters *aaaaa* from `text`, whereas the last character *a* from `text` is reserved for the second subexpression `a`.

``` abap
DATA TEXT type STRING. 
DATA result_tab TYPE match_result_tab. 
 
text = 'aaaaaa'. 
 
FIND ALL OCCURRENCES OF REGEX '(a+)(a)' ##regex_posix 
     IN text RESULTS result_tab.
```

### Alternatives

The operator `|` can be written between two regular expressions `r` and `s`, and thereby create one single regular expression `r|s`, that matches both `r` as well as `s`.

### Hint

Chainings and other operators form a stronger bond than `|`, in other words `r|st` and `r|s+` are equivalent to `r|(?:st)` or `r|(?:s+)` but not to `(?:r|s)t` or `(?:r|s)+`.

### Subgroups

The operators `(` ... `)` and `(?:` ... `)` group chainings of regular expressions into one unit and thus affect the scope of other operators such as `*` or `|`. Here, the regular expressions `(r)` and `(?:r)` match the regular expression `r`. The difference between `(` ... `)` and `(?:` ... `)` is that the operator `(` ... `)` stores the substrings found in registers and `(?:` ... `)` does not.

### Hint

The greedy behavior of chaining operators mentioned above also applies to subgroups from left to right. However, this does not violate the rule that generally requires the entire regular expression to match.

### Subgroups with Registration

In addition to its effect on creating subgroups, the operator `(` ... `)` also stores the substrings when matching the regular expression to a character string in the correct order in subgroup registers. The subgroups `(` ... `)` of the expression match these substrings. In this process, an operator `\1`, `\2`, `\3`, ... is assigned to each subgroup, which can be specified within the expression after its subgroup and acts as a placeholder for the character string stored in the corresponding register. In [text replacements](abenregex_posix_replace.md), the special characters `$1`, `$2`, `$3`, ... can be used to access the last assignment of the register.

The number of subgroups and registers is only limited by the capacity of the platform.

### Hints

- The addition `SUBMATCHES` of the statements [`FIND`](../abap-processing-internal-data/abapfind.md) and [`REPLACE`](../abap-processing-internal-data/abapreplace.md) and the identically named column of the results table filled using the addition `RESULTS` can be used to access the content of all subgroup registers for an occurrence. The class `CL_ABAP_MATCHER` contains the method `GET_SUBMATCH` for this purpose.

- If only grouping is required and no substrings are to be stored in registers, the operator `(?:` ... `)` can be used instead of `(` ... `)`. With respect to the formation of subgroups, both operators have the same effect. However `(?:` ... `)` does not save anything in registers.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the greedy behavior of the operator `+` in subgroups and its relation to the primary rule that the entire regular expression must match if possible. The first subgroup takes up as many *a* characters as possible. It is assigned the first four characters *aaaa*. A character *a* remains for each of the other two subgroups.

``` abap
DATA text TYPE string. 
DATA result_tab TYPE match_result_tab. 
 
text = 'aaaaaa'. 
 
FIND ALL OCCURRENCES OF REGEX '(a+)(a+)(a+)' ##regex_posix 
     IN text RESULTS result_tab.
```

### Literal Characters

The operators `\Q` ... `\E` form a character string of literal characters from all enclosed characters. Special characters are ignored in this character string.

The following table shows some results from a [matching](../abap-processing-internal-data/abenregex_mtch.md).

| **pattern**  | **Text**      | **`match`** |
|--------------|---------------|-------------|
| `.+\w\d`     | Special: \w\d | \-          |
| `.+\\w\\d`   | Special: \w\d | X           |
| `.+\Q\w\d\E` | Special: \w\d | X           |

### Reserved Enhancements

The character string `(?` ... `)` is generally reserved for later language enhancements. Apart from the operators already supported `(?:`...`)`, [`(?=`...`)`](abenregex_posix_search.md), [`(?!`...`)`](abenregex_posix_search.md), and [`(?>` ... `)`](abenregex_posix_search.md), this string raises the exception `CX_SY_INVALID_REGEX`.
