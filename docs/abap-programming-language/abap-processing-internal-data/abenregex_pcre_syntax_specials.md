---
title: "PCRE regex - Special Characters"
source_file: abenregex_pcre_syntax_specials.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Regular Expressions (regex) > regex - Syntax > regex - PCRE Syntax"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# PCRE regex - Special Characters

The following tables summarize the special characters in [PCRE regular expressions](../../abap-glossary/abenpcre_regex_glosry.md).

- [Pattern Syntax](abenregex_pcre_syntax_specials.md#pattern-syntax)

  - [Quoting](abenregex_pcre_syntax_specials.md#quoting)

  - [Escaped Characters](abenregex_pcre_syntax_specials.md#escaped-characters)

  - [Character Types](abenregex_pcre_syntax_specials.md#character-types)

  - [Character Classes](abenregex_pcre_syntax_specials.md#character-classes)

  - [Quantifiers](abenregex_pcre_syntax_specials.md#quantifiers)

  - [Anchors and Basic Assertions](abenregex_pcre_syntax_specials.md#anchors-and-basic-assertions)

  - [Reported Match Point Setting](abenregex_pcre_syntax_specials.md#reported-match-point-setting)

  - [Alternation](abenregex_pcre_syntax_specials.md#alternation)

  - [Grouping and Capturing](abenregex_pcre_syntax_specials.md#grouping-and-capturing)

  - [Comments](abenregex_pcre_syntax_specials.md#comments)

  - [Option Setting](abenregex_pcre_syntax_specials.md#option-setting)

  - [Special Control Verbs](abenregex_pcre_syntax_specials.md#special-control-verbs)

  - [Look-ahead and Look-behind Assertions](abenregex_pcre_syntax_specials.md#look-ahead-and-look-behind-assertions)

  - [Non-Atomic Look-around Assertions](abenregex_pcre_syntax_specials.md#non-atomic-look-around-assertions)

  - [Backreferences](abenregex_pcre_syntax_specials.md#backreferences)

  - [Subroutine References](abenregex_pcre_syntax_specials.md#subroutine-references)

  - [Conditional Patterns](abenregex_pcre_syntax_specials.md#conditional-patterns)

  - [Backtracking Control](abenregex_pcre_syntax_specials.md#backtracking-control)

  - [Callouts](abenregex_pcre_syntax_specials.md#callouts)

- [Replacement Syntax](abenregex_pcre_syntax_specials.md#replacement-syntax)

  - [Capture Group Substitution](abenregex_pcre_syntax_specials.md#capture-group-substitution)

  - [Conditional Substitution](abenregex_pcre_syntax_specials.md#conditional-substitution)

  - [Case Conversion](abenregex_pcre_syntax_specials.md#case-conversion)

  - [Substituting Special Characters](abenregex_pcre_syntax_specials.md#substituting-special-characters)

  - [Quoting](abenregex_pcre_syntax_specials.md#quoting)

## Hint

See also [PCRE2 documentation **pcre2syntax man page**](https://www.pcre.org/current/doc/html/pcre2syntax.html).

## Pattern Syntax

### Quoting

| **Syntax** | **Description**                                       |
|------------|-------------------------------------------------------|
| `\x`       | handle `x` as a literal if `x` has no special meaning |
| `\Q...\E,` | handle enclosed characters as literal                 |

### Escaped Characters

| **Syntax**   | **Description**                                                     |
|--------------|---------------------------------------------------------------------|
| `\a`         | alarm (`BEL` character, `0x07`)                                     |
| `\cx`        | control-`x`, where `x` is any ASCII printing character              |
| `\e`         | escape (`0x1B`)                                                     |
| `\f`         | form feed (`0x0C`)                                                  |
| `\n`         | line feed (by default `0x0A`; depends on the active line-feed-mode) |
| `\r`         | carriage return (`0x0D`)                                            |
| `\t`         | tab (`0x09`)                                                        |
| `\0dd`       | character with octal code `0dd`                                     |
| `\ddd`       | character with octal code `ddd`, or backreference                   |
| `\o{ddd..}`  | character with octal code `ddd..`                                   |
| `\N{U+hh..}` | character with Unicode code point `hh..`                            |
| `\xhh`       | character with hex code `hh`                                        |
| `\x{hh..}`   | character with hex code `hh..`                                      |

### Character Types

| **Syntax** | **Description**                                                                                                                                                                                                              |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `.`        | any character except line feed (unless in dotall mode, then any character)                                                                                                                                                   |
| `\C`       | one code unit; only allowed in regular expressions created with the class [`CL_ABAP_REGEX`](abenregex_system_classes.md) with `UNICODE_HANDLING` set to `RELAXED`, as it could partially match UTF-16 characters otherwise |
| `\d`       | a digit (respecting Unicode character properties)                                                                                                                                                                            |
| `\D`       | a character that is not a digit                                                                                                                                                                                              |
| `\h`       | a horizontal white space character (respecting Unicode character properties)                                                                                                                                                 |
| `\H`       | a character that is not a horizontal white space character                                                                                                                                                                   |
| `\N`       | a character that is not a line feed (depends on the active line-feed-mode)                                                                                                                                                   |
| `\p{xx}`   | a character with the `xx` Unicode character property (see below)                                                                                                                                                             |
| `\P{xx}`   | a character without the `xx` Unicode character property (see below)                                                                                                                                                          |
| `\R`       | a line feed sequence; by default matches any Unicode line feed sequence                                                                                                                                                      |
| `\s`       | a white space character (respecting Unicode character properties)                                                                                                                                                            |
| `\S`       | a character that is not a white space character                                                                                                                                                                              |
| `\v`       | a vertical white space character (respecting Unicode character properties)                                                                                                                                                   |
| `\V`       | a character that is not a vertical white space character                                                                                                                                                                     |
| `\w`       | a *word* character (respecting Unicode character properties)                                                                                                                                                                 |
| `\W`       | a *non-word* character                                                                                                                                                                                                       |
| `\X`       | a Unicode extended grapheme cluster                                                                                                                                                                                          |

**General Categories for Properties `\p` and `\P`**

Based on the general categories as defined by the Unicode standard.

| **Category Identifier** | **Description**       |
|-------------------------|-----------------------|
| `C`                     | Other                 |
| `Cc`                    | Control               |
| `Cf`                    | Format                |
| `Cn`                    | Unassigned            |
| `Co`                    | Private use           |
| `Cs`                    | Surrogate             |
| `L`                     | Letter                |
| `Ll`                    | Lower case letter     |
| `Lm`                    | Modifier letter       |
| `Lo`                    | Other letter          |
| `Lt`                    | Title case letter     |
| `Lu`                    | Upper case letter     |
| `L&`                    | `Ll`, `Lu`, or `Lt`   |
| `M`                     | Mark                  |
| `Mc`                    | Spacing mark          |
| `Me`                    | Enclosing mark        |
| `Mn`                    | Non-spacing mark      |
| `N`                     | Number                |
| `Nd`                    | Decimal number        |
| `Nl`                    | Letter number         |
| `No`                    | Other number          |
| `P`                     | Punctuation           |
| `Pc`                    | Connector punctuation |
| `Pd`                    | Dash punctuation      |
| `Pe`                    | Close punctuation     |
| `Pf`                    | Final punctuation     |
| `Pi`                    | Initial punctuation   |
| `Po`                    | Other punctuation     |
| `Ps`                    | Open punctuation      |
| `S`                     | Symbol                |
| `Sc`                    | Currency symbol       |
| `Sk`                    | Modifier symbol       |
| `Sm`                    | Mathematical symbol   |
| `So`                    | Other symbol          |
| `Z`                     | Separator             |
| `Zl`                    | Line separator        |
| `Zp`                    | Paragraph separator   |
| `Zs`                    | Space separator       |

**Script Names for `\p` and `\P`**

- `Adlam`

- `Ahom`

- `Anatolian_Hieroglyphs`

- `Arabic`

- `Armenian`

- `Avestan`

- `Balinese`

- `Bamum`

- `Bassa_Vah`

- `Batak`

- `Bengali`

- `Bhaiksuki`

- `Bopomofo`

- `Brahmi`

- `Braille`

- `Buginese`

- `Buhid`

- `Canadian_Aboriginal`

- `Carian`

- `Caucasian_Albanian`

- `Chakma`

- `Cham`

- `Cherokee`

- `Chorasmian`

- `Common`

- `Coptic`

- `Cuneiform`

- `Cypriot`

- `Cyrillic`

- `Deseret`

- `Devanagari`

- `Dives_Akuru`

- `Dogra`

- `Duployan`

- `Egyptian_Hieroglyphs`

- `Elbasan`

- `Elymaic`

- `Ethiopic`

- `Georgian`

- `Glagolitic`

- `Gothic`

- `Grantha`

- `Greek`

- `Gujarati`

- `Gunjala_Gondi`

- `Gurmukhi`

- `Han`

- `Hangul`

- `Hanifi_Rohingya`

- `Hanunoo`

- `Hatran`

- `Hebrew`

- `Hiragana`

- `Imperial_Aramaic`

- `Inherited`

- `Inscriptional_Pahlavi`

- `Inscriptional_Parthian`

- `Javanese`

- `Kaithi`

- `Kannada`

- `Katakana`

- `Kayah_Li`

- `Kharoshthi`

- `Khitan_Small_Script`

- `Khmer`

- `Khojki`

- `Khudawadi`

- `Lao`

- `Latin`

- `Lepcha`

- `Limbu`

- `Linear_A`

- `Linear_B`

- `Lisu`

- `Lycian`

- `Lydian`

- `Mahajani`

- `Makasar`

- `Malayalam`

- `Mandaic`

- `Manichaean`

- `Marchen`

- `Masaram_Gondi`

- `Medefaidrin`

- `Meetei_Mayek`

- `Mende_Kikakui`

- `Meroitic_Cursive`

- `Meroitic_Hieroglyphs`

- `Miao`

- `Modi`

- `Mongolian`

- `Mro`

- `Multani`

- `Myanmar`

- `Nabataean`

- `Nandinagari`

- `New_Tai_Lue`

- `Newa`

- `Nko`

- `Nushu`

- `Nyakeng_Puachue_Hmong`

- `Ogham`

- `Ol_Chiki`

- `Old_Hungarian`

- `Old_Italic`

- `Old_North_Arabian`

- `Old_Permic`

- `Old_Persian`

- `Old_Sogdian`

- `Old_South_Arabian`

- `Old_Turkic`

- `Oriya`

- `Osage`

- `Osmanya`

- `Pahawh_Hmong`

- `Palmyrene`

- `Pau_Cin_Hau`

- `Phags_Pa`

- `Phoenician`

- `Psalter_Pahlavi`

- `Rejang`

- `Runic`

- `Samaritan`

- `Saurashtra`

- `Sharada`

- `Shavian`

- `Siddham`

- `SignWriting`

- `Sinhala`

- `Sogdian`

- `Sora_Sompeng`

- `Soyombo`

- `Sundanese`

- `Syloti_Nagri`

- `Syriac`

- `Tagalog`

- `Tagbanwa`

- `Tai_Le`

- `Tai_Tham`

- `Tai_Viet`

- `Takri`

- `Tamil`

- `Tangut`

- `Telugu`

- `Thaana`

- `Thai`

- `Tibetan`

- `Tifinagh`

- `Tirhuta`

- `Ugaritic`

- `Vai`

- `Wancho`

- `Warang_Citi`

- `Yezidi`

- `Yi`

- `Zanabazar_Square`

### Character Classes

| **Syntax**   | **Description**                      |
|--------------|--------------------------------------|
| `[...]`      | positive character class             |
| `[^...]`     | negative character class             |
| `[x-y]`      | range                                |
| `[[:xxx:]]`  | positive POSIX named set (see below) |
| `[[:^xxx:]]` | negative POSIX named set (see below) |

**Names for POSIX Named Sets**

| **Syntax** | **Description**                  |
|------------|----------------------------------|
| `alnum`    | alphanumeric                     |
| `alpha`    | alphabetic                       |
| `ascii`    | `0-127`                          |
| `blank`    | space or tab                     |
| `cntrl`    | control character                |
| `digit`    | decimal digit                    |
| `graph`    | printing, excluding space        |
| `lower`    | lower case letter                |
| `print`    | printing, including space        |
| `punct`    | printing, excluding alphanumeric |
| `space`    | white space                      |
| `upper`    | upper case letter                |
| `word`     | same as `\w`                     |
| `xdigit`   | hexadecimal digit                |

POSIX named sets also make use of Unicode character properties if applicable.

### Quantifiers

| **Syntax** | **Description**                            |
|------------|--------------------------------------------|
| `?`        | 0 or 1, greedy                             |
| `?+`       | 0 or 1, possessive                         |
| `??`       | 0 or 1, lazy                               |
| `*`        | 0 or more, greedy                          |
| `*+`       | 0 or more, possessive                      |
| `*?`       | 0 or more, lazy                            |
| `+`        | 1 or more, greedy                          |
| `++`       | 1 or more, possessive                      |
| `+?`       | 1 or more, lazy                            |
| `{n}`      | exactly `n`                                |
| `{n,m}`    | at least `n`, no more than `m`, greedy     |
| `{n,m}+`   | at least `n`, no more than `m`, possessive |
| `{n,m}?`   | at least `n`, no more than `m`, lazy       |
| `{n,}`     | `n` or more, greedy                        |
| `{n,}+`    | `n` or more, possessive                    |
| `{n,}?`    | `n` or more, lazy                          |

### Anchors and Basic Assertions

| **Syntax** | **Description**                                                                                                                                                                                                 |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `\b`       | word boundary                                                                                                                                                                                                   |
| `\B`       | not a word boundary                                                                                                                                                                                             |
| `^`        | start of subject (also after an internal line feed, that is a line feed that does not occur at the end of the subject, in multiline mode)                                                                       |
| `\A`       | start of subject (if matching on a subject is done with a starting offset, \A can never match)                                                                                                                  |
| `$`        | end of subject and before a line feed at the end of the subject (also before line feed in multiline mode)                                                                                                       |
| `\Z`       | end of subject and before a line feed at the end of the subject                                                                                                                                                 |
| `\z`       | end of subject                                                                                                                                                                                                  |
| `\G`       | first matching position in subject (true if the current matching position is at the start point of the matching process, which may differ from the start of the subject e.g. if a starting offset is specified) |

### Reported Match Point Setting

| **Syntax** | **Description**                                                                                                    |
|------------|--------------------------------------------------------------------------------------------------------------------|
| `\K`       | set reported start of match; e.g. the regex `foo\Kbar` matches `foobar` but reports that it has matched only `bar` |

`\K` is respected in positive assertions, but ignored in negative ones.

### Alternation

| **Syntax** | **Description**             |
|------------|-----------------------------|
| `\|`       | start of alternative branch |

### Grouping and Capturing

| **Syntax**       | **Description**                                                               |
|------------------|-------------------------------------------------------------------------------|
| `(...)`          | capture group                                                                 |
| `(?<name>...)`   | named capture group (Perl style)                                              |
| `(?'name'...)`   | named capture group (Perl style)                                              |
| `(?P?<name>...)` | named capture group (Python style)                                            |
| `(?:...)`        | non-capture group                                                             |
| `(?\|...)`       | non-capture group; reset group numbers for capture groups in each alternative |
| `(?>...)`        | atomic non-capture group                                                      |
| `(*atomic:...)`  | atomic non-capture group                                                      |

A name must not start with a digit. Unicode names are allowed.

### Comments

| **Syntax** | **Description**            |
|------------|----------------------------|
| `(?#...)`  | comment (cannot be nested) |
| `#...`     | extended mode: comment     |

In extended mode, an unescaped `#` introduces a comment which in this case continues to immediately after the next line feed character or character sequence in the pattern. This has to be a literal line feed character or character sequence, escape sequences that happen to represent a line feed like `\n` do not count.

### Option Setting

| **Syntax** | **Description**                                         |
|------------|---------------------------------------------------------|
| `(?i)`     | caseless / case-insensitive search                      |
| `(?J)`     | allow duplicate named groups                            |
| `(?m)`     | multiline mode                                          |
| `(?n)`     | no auto capture                                         |
| `(?s)`     | single line mode (dotall)                               |
| `(?U)`     | default ungreedy quantifiers (lazy)                     |
| `(?x)`     | extended mode: ignore white space except in classes     |
| `(?xx)`    | same as `(?x)` but also ignore space and tab in classes |
| `(?-...)`  | unset option(`s`)                                       |
| `(?^)`     | unset `i`, `m`, `n`, `s` and `x` options                |

Changes of these options within a group are automatically cancelled at the end of the group.

Several options may be set at once, and a mixture of setting and unsetting such as `(?i-x)` is allowed, but there may be only one hyphen. Setting (but no unsetting) is allowed after `(?^` for example `(?^in)`. An option setting may appear at the start of a non-capture group, for example `(?i:...)`.

### Special Control Verbs

Special control verbs are only recognized at the very start of a pattern.

| **Syntax**             | **Description**                                                                                                                                                                                                          |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `(*LIMIT_DEPTH=d)`     | set the backtracking limit to `d`                                                                                                                                                                                        |
| `(*LIMIT_HEAP=d)`      | set the heap size limit to `d * 1024` bytes                                                                                                                                                                              |
| `(*LIMIT_MATCH=d)`     | set the match limit to `d`                                                                                                                                                                                               |
| `(*NOTEMPTY)`          | lock out matching of empty strings entirely                                                                                                                                                                              |
| `(*NOTEMPTY_ATSTART)`  | lock out matching of empty strings at the start of the subject                                                                                                                                                           |
| `(*NO_AUTO_POSSES)`    | prevents quantifiers from automatically being made possessive when what follows cannot match the repeated item (e.g. by default, `a+b` is handled as `a++b` as an optimization)                                          |
| `(*NO_DOTSTAR_ANCHOR)` | disable optimizations that apply to patterns whose top-level branches start with `.*`                                                                                                                                    |
| `(*NO_JIT)`            | do not JIT-compile this pattern                                                                                                                                                                                          |
| `(*NO_START_OPT)`      | disable several optimizations for quickly reaching a *no match* result; this can be useful if you want callouts or backtracking control verbs to be executed in any case                                                 |
| `(*UTF)`               | enable UTF-mode; this verb cannot be used in regular expressions created with the class [`CL_ABAP_REGEX`](abenregex_system_classes.md) with `UNICODE_HANDLING` set to `RELAXED`, as it would clash with usages of `\C` |
| `(*UCP)`               | enable usage of Unicode character properties; for ABAP regular expressions this option is already enabled by default                                                                                                     |

The following special control verbs control the line break convention, i.e. what gets recognized as a line feed character. They do not affect `\R`:

| **Syntax**   | **Description**                       |
|--------------|---------------------------------------|
| `(*CR)`      | carriage return only                  |
| `(*LF)`      | line feed only                        |
| `(*CRLF)`    | carriage return followed by line feed |
| `(*ANYCRLF)` | all three of the above                |
| `(*ANY)`     | any Unicode line feed sequence        |
| `(*NUL)`     | the `NUL` character (binary zero)     |

The following special control verbs control what `\R` matches:

| **Syntax**       | **Description**                |
|------------------|--------------------------------|
| `(*BSR_ANYCRLF)` | `CR`, `LF` and `CRLF`          |
| `(*BSR_UNICODE)` | any Unicode line feed sequence |

### Look-ahead and Look-behind Assertions

| **Syntax**                    | **Description**      |
|-------------------------------|----------------------|
| `(?=...)`                     | positive look-ahead  |
| `(*pla:...)`                  | positive look-ahead  |
| `(*positive_look-ahead:...)`  | positive look-ahead  |
| `(?!...)`                     | negative look-ahead  |
| `(*nla:...)`                  | negative look-ahead  |
| `(*negative_look-ahead:...)`  | negative look-ahead  |
| `(?<=...)`                    | positive look-behind |
| `(*plb:...)`                  | positive look-behind |
| `(*positive_look-behind:...)` | positive look-behind |
| `(?<!...)`                    | negative look-behind |
| `(*nlb:...)`                  | negative look-behind |
| `(*negative_look-behind:...)` | negative look-behind |

Each top-level branch of a look-behind must be of fixed length.

### Non-Atomic Look-around Assertions

| **Syntax**                               | **Description**                 |
|------------------------------------------|---------------------------------|
| `(?*...)`                                | non-atomic positive look-ahead  |
| `(*napla:...)`                           | non-atomic positive look-ahead  |
| `(*non_atomic_positive_look-ahead:...)`  | non-atomic positive look-ahead  |
| `(?<*...)`                               | non-atomic positive look-behind |
| `(*naplb:...)`                           | non-atomic positive look-behind |
| `(*non_atomic_positive_look-behind:...)` | non-atomic positive look-behind |

### Backreferences

| **Syntax**  | **Description**                                               |
|-------------|---------------------------------------------------------------|
| `\n`        | reference by number `n` (can be ambiguous, see octal escapes) |
| `\gn`       | reference by number `n`                                       |
| `\g{n}`     | reference by number `n`                                       |
| `\g+n`      | relative reference by number `n`                              |
| `\g-n`      | relative reference by number `n`                              |
| `\g{+n}`    | relative reference by number `n`                              |
| `\g{-n}`    | relative reference by number `n`                              |
| `\k?<name>` | reference by name (Perl style)                                |
| `\k'name'`  | reference by name (Perl style)                                |
| `\g{name}`  | reference by name (Perl style)                                |
| `\k{name}`  | reference by name (.NET style)                                |
| `(?P=name)` | reference by name (Perl style)                                |

### Subroutine References

| **Syntax**  | **Description**                                            |
|-------------|------------------------------------------------------------|
| `(?R)`      | recurse whole pattern                                      |
| `(?n)`      | call subroutine by absolute number `n`                     |
| `\g<n>`     | call subroutine by absolute number `n` (`Oniguruma` style) |
| `\g'n'`     | call subroutine by absolute number `n` (`Oniguruma` style) |
| `(?+n)`     | call subroutine by relative number `n`                     |
| `(?-n)`     | call subroutine by relative number `n`                     |
| `\g<+n>`    | call subroutine by relative number `n`                     |
| `\g'+n'`    | call subroutine by relative number `n`                     |
| `\g<-n>`    | call subroutine by relative number `n`                     |
| `\g'-n'`    | call subroutine by relative number `n`                     |
| `(?&name)`  | call subroutine by name (Perl style)                       |
| `(?P>name)` | call subroutine by name (Python style)                     |
| `\g?<name>` | call subroutine by name (`Oniguruma` style)                |
| `\g'name'`  | call subroutine by name (`Oniguruma` style)                |

Subroutine calls can be recursive. Left recursion is not possible however.

### Executable Example

[Parsing with PCRE Regular Expression](abenpcre_parsing_abexa.md)

### Conditional Patterns

| **Syntax**                              | **Description**                                                                 |
|-----------------------------------------|---------------------------------------------------------------------------------|
| `(?(condition)yes-pattern)`             | match the yes-pattern if the condition holds                                    |
| `(?(condition)yes-pattern\|no-pattern)` | match the yes-pattern if the condition holds, otherwise match the false-pattern |

Where condition can be one of the following or any other assertion like a look-ahead or look-behind assertion:

| **Syntax**       | **Description**                                   |
|------------------|---------------------------------------------------|
| `n`              | absolute number `n` reference condition           |
| `+n`             | relative number `n` reference condition           |
| `-n`             | relative number `n` reference condition           |
| `?<name>`        | named reference condition (Perl style)            |
| `'name'`         | named reference condition (Perl style)            |
| `R`              | overall recursion condition                       |
| `Rn`             | specific number `n` group recursion condition     |
| `R&name`         | specific named group recursion condition          |
| `DEFINE`         | define groups for reference (always yields false) |
| `VERSION[>]=n.m` | test PCRE2 version                                |

### Backtracking Control

The following backtracking control verbs are triggered immediately when they are reached:

<table>
<thead>
<tr class="header">
<th><strong>Syntax</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">(*ACCEPT)</code></td>
<td><p>force successful match;</p>
<p>if triggered inside a group that is called as a subroutine, only the group is ended successfully;</p>
<p>if triggered inside a positive assertion, the assertion succeeds;</p>
<p>if triggered inside a negative assertion, the assertion fails</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">(*FAIL)</code></td>
<td>force backtrack</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">(*F)</code></td>
<td>force backtrack</td>
</tr>
<tr class="even">
<td><code class="ph codeph">(?!)</code></td>
<td>force backtrack; actually a negative look-ahead for the empty string, which always matches thus always failing the look-ahead; <code class="ph codeph">(*FAIL)</code> and <code class="ph codeph">(*F)</code> are synonyms for <code class="ph codeph">(?!)</code></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">(*MARK:NAME)</code></td>
<td>mark a position with name <code class="ph codeph">NAME</code>, see <code class="ph codeph">(*SKIP:NAME)</code> below; synonym <code class="ph codeph">(:NAME)</code>; <code class="ph codeph">NAME</code> can contain any sequence of characters that does not include the closing parenthesis; an empty name will cause the mark to have no effect</td>
</tr>
</tbody>
</table>

The following backtracking control verbs are only triggered when a subsequent match failure causes a backtrack to reach them. All of them force a match failure, but differ in what happens afterwards:

| **Syntax**     | **Description**                                                                                             |
|----------------|-------------------------------------------------------------------------------------------------------------|
| `(*COMMIT)`    | overall failure, no advance of starting point                                                               |
| `(*PRUNE)`     | advance to next starting character; only applies if the pattern is not anchored, otherwise behaves the same |
| `(*SKIP)`      | advance to current matching position                                                                        |
| `(*SKIP:NAME)` | advance to position corresponding to an earlier `(*MARK:NAME)`; if not found, the `(*SKIP)` is ignored      |
| `(*THEN)`      | local failure, backtrack to next alternation                                                                |

If one of these verbs is located in a group called as a subroutine, its effects are confined to the subroutine call.

### Callouts

| **Syntax**   | **Description**               |
|--------------|-------------------------------|
| `(?C)`       | callout (assumed number 0)    |
| `(?Cn)`      | callout with numeric data `n` |
| `(?C"text")` | callout with string data text |

### Executable Example

[PCRE Regular Expression with Callouts](abenpcre_callout_abexa.md)

## Replacement Syntax

### Capture Group Substitution

| **Syntax** | **Description**                                                                                                                                                                                                |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$id`      | substitute for the content of the capture group identified by `id`, `$0` being the content of the whole match; id can either be a number referring to a capture group or the name of a named capture group     |
| `${id}`    | substitute for the content of the capture group identified by `id`, `${0}` being the content of the whole match; `id` can either be a number referring to a capture group or the name of a named capture group |

When referring to a capture group that is not set (i.e. was not participating) in the match, the empty string will be substituted.

When referring to a capture group that does not exist, it is assumed unset and thus the empty string is substituted.

### Conditional Substitution

| **Syntax**                | **Description**                                                                                                                                                                                                                                                          |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `{id:+matched:unmatched}` | substitute for matched if the capture group identified by `id` was set in the match, otherwise for unmatched; `id` can either be a number referring to a capture group or the name of a named capture group                                                              |
| `{id:-default}`           | substitute for the content of the capture group identified by `id` if said capture group was set in the match, otherwise for default; shorthand for `{id:+${id}:default}`; `id` can either be a number referring to a capture group or the name of a named capture group |

When referring to a capture group that is not set (i.e. was not participating) in the match, the empty string will be substituted.

When referring to a capture group that does not exist, it is assumed unset and thus the empty string is substituted.

### Case Conversion

| **Syntax** | **Description**                                                                                                              |
|------------|------------------------------------------------------------------------------------------------------------------------------|
| `\u`       | the first character after `\u` that is inserted into the replacement text is converted to uppercase                          |
| `\U`       | all characters after `\U` up to the next `\L` or `\E` that are inserted into the replacement text are converted to uppercase |
| `\l`       | the first character after `\l` that is inserted into the replacement text is converted to lowercase                          |
| `\L`       | all characters after `\L` up to the next `\U` or `\E` that are inserted into the replacement text are converted to lowercase |
| `\E`       | terminates the current upper- or lowercase transformation                                                                    |

### Substituting Special Characters

| **Syntax** | **Description**                           |
|------------|-------------------------------------------|
| `\t`       | insert a tab (`0x09`)                     |
| `\r`       | insert a carriage return (`0x0D`)         |
| `\n`       | insert a line feed                        |
| `\f`       | insert a form feed (`0x0C`)               |
| `\xhh`     | insert the character with hex code `hh`   |
| `\x{hh..}` | insert the character with hex code `hh..` |

### Quoting

| **Syntax** | **Description**                                      |
|------------|------------------------------------------------------|
| `\\`       | insert a literal `\`                                 |
| `\$`       | insert a literal `$`                                 |
| `\x`       | if `\x` has no special meaning, insert a literal `x` |
