---
title: "POSIX regex - Special Characters (obsolete)"
source_file: abenregex_posix_syntax_specials.html
section: "ABAP Programming Language > ABAP - Obsolete Language Elements > Obsolete Processing of Internal Data > Obsolete Character String and Byte String Processing > Obsolete Regular Expression Syntax > regex - POSIX Syntax (obsolete)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# POSIX regex - Special Characters (obsolete)

The following tables summarize the special characters in [POSIX regular expressions](../../abap-glossary/abenposix_regex_glosry.md).

- [Escape Character](abenregex_posix_syntax_specials.md#escape-character)

- [Special Characters for Single Character Strings](abenregex_posix_syntax_specials.md#special-characters-for-single-character-strings)

- [Special Characters for Character String Patterns](abenregex_posix_syntax_specials.md#special-characters-for-character-string-patterns)

- [Special Characters for Search Patterns](abenregex_posix_syntax_specials.md#special-characters-for-search-patterns)

- [Special Characters for Replacement Texts](abenregex_posix_syntax_specials.md#special-characters-for-replacement-texts)

## Escape Character

| **Special Character** | **Meaning**                             |
|-----------------------|-----------------------------------------|
| `\`                   | Escape character for special characters |

### Hint

The string function [`escape`](../abap-processing-internal-data/abenescape_functions.md) can be used to prefix all special characters for regular expressions with their escape character.

## Special Characters for Single Character Strings

| **Special Character** | **Meaning**                                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------------------------|
| `.`                   | Placeholder for any single character                                                                            |
| `\C`                  | Placeholder for any single character                                                                            |
| `\d`                  | Placeholder for any digit                                                                                       |
| `\D`                  | Placeholder for any non-digit character                                                                         |
| `\l`                  | Placeholder for any lowercase letter                                                                            |
| `\L`                  | Placeholder for any non-lowercase letter                                                                        |
| `\s`                  | Placeholder for a blank character                                                                               |
| `\S`                  | Placeholder for a non-blank character                                                                           |
| `\u`                  | Placeholder for any uppercase letter                                                                            |
| `\U`                  | Placeholder for any non-uppercase letter                                                                        |
| `\w`                  | Placeholder for any alphanumeric character including \_                                                         |
| `\W`                  | Placeholder for any non-alphanumeric character except for \_                                                    |
| `[ ]`                 | Definition of a value set for single characters                                                                 |
| `[^ ]`                | Negation of a value set for single characters                                                                   |
| `[ - ]`               | Definition of a range in a value set for single characters                                                      |
| `[[:alnum:]]`         | Designation for all alphanumeric characters in a value set                                                      |
| `[[:alpha:]]`         | Designation for all letters in a value set                                                                      |
| `[[:blank:]]`         | Designation for blank characters and horizontal tabulators in a value set                                       |
| `[[:cntrl:]]`         | Designation for all control characters in a value set                                                           |
| `[[:digit:]]`         | Designation for all digits in a value set                                                                       |
| `[[:graph:]]`         | Designation for all displayable characters apart from blank characters and horizontal tabulators in a value set |
| `[[:lower:]]`         | Designation for all lowercase letters in a value set                                                            |
| `[[:print:]]`         | Designation for all displayable characters in a value set                                                       |
| `[[:punct:]]`         | Designation for all punctuation marks in a value set                                                            |
| `[[:space:]]`         | Designation for all blank characters, tabulators, carriage returns and line feeds in a value set                |
| `[[:unicode:]]`       | Designation for all Unicode characters in a value set with a code greater than 255                              |
| `[[:upper:]]`         | Designation for all uppercase letters in a value set                                                            |
| `[[:word:]]`          | Designation for all alphanumeric characters and \_ in a value set                                               |
| `[[:xdigit:]]`        | Designation for all hexadecimal digits in a value set                                                           |
| `\a \f \n \r \t \v`   | Various platform-dependent control characters                                                                   |
| `[..]`                | Reserved for future enhancements                                                                                |
| `[==]`                | Reserved for future enhancements                                                                                |

[***-\>* More about**](abenregex_posix_syntax_signs.md)

## Special Characters for Character String Patterns

| **Special Character** | **Meaning**                                                           |
|-----------------------|-----------------------------------------------------------------------|
| `{n}`                 | Chaining of `n` single characters                                     |
| `{n,m}`               | Chaining of at least `n` and a maximum of `m` single characters       |
| `{n,m}?`              | Reserved for future enhancements                                      |
| `?`                   | One single character or no single characters                          |
| `*`                   | Chaining of any number of single characters including 'no characters' |
| `*?`                  | Reserved for future enhancements                                      |
| `+`                   | Chaining of any number of single characters excluding 'no characters' |
| `+?`                  | Reserved for future enhancements                                      |
| `\|`                  | Combination of two alternative expressions                            |
| `( )`                 | Definition of subgroups with registration                             |
| `(?: )`               | Definition of subgroups without registration                          |
| `\1`, `\2`, `\3` ...  | Placeholder for the registration of subgroups                         |
| `\Q` ... `\E`         | Definition of a string of literal characters                          |
| `(?` ... `)`          | Reserved for future enhancements                                      |

[***-\>* More about**](abenregex_posix_syntax_operators.md)

## Special Characters for Search Patterns

| **Special Character** | **Meaning**                                                                               |
|-----------------------|-------------------------------------------------------------------------------------------|
| `^`                   | Anchor character for the start of a line                                                  |
| `\A`                  | Anchor character for the start of a character string                                      |
| `$`                   | Anchor character for the end of a line                                                    |
| `\z`                  | Anchor character for the end of a character string                                        |
| `\Z`                  | The same as for `\z`. Line feeds at the end of the character string, however, are ignored |
| `\<`                  | Start of a word                                                                           |
| `\>`                  | End of a word                                                                             |
| `\b`                  | Start or end of a word                                                                    |
| `\B`                  | Space between characters within a word                                                    |
| `(?= )`               | Preview condition                                                                         |
| `(?! )`               | Negated preview condition                                                                 |
| `(?> )`               | Cut operator                                                                              |

[***-\>* More about**](abenregex_posix_search.md)

## Special Characters for Replacement Texts

| **Special Character** | **Meaning**                                         |
|-----------------------|-----------------------------------------------------|
| `$0`, `$&`            | Placeholder for the entire occurrence               |
| `$1`, `$2`, `$3`...   | Placeholder for the registration of subgroups       |
| \`\$\`\`              | Placeholder for the text in front of the occurrence |
| `$'`                  | Placeholder for the text after the occurrence       |

[***-\>* More about**](abenregex_posix_replace.md)
