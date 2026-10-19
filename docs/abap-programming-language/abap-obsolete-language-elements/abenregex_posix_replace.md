---
title: "POSIX regex - Replacement Patterns (obsolete)"
source_file: abenregex_posix_replace.html
section: "ABAP Programming Language > ABAP - Obsolete Language Elements > Obsolete Processing of Internal Data > Obsolete Character String and Byte String Processing > Obsolete Regular Expression Syntax > regex - POSIX Syntax (obsolete)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# POSIX regex - Replacement Patterns (obsolete)

In addition to [searching](abenregex_posix_search.md), the replacement of substrings in character strings is the most important application of regular expressions. When replacing, the occurrences of a search, that is, the substrings that match a regular expression, are replaced by one or more different character strings. In ABAP, the replacement is implemented using regular expressions with the addition [`REGEX`](../abap-processing-internal-data/abapfind_pattern.md) of the statement [`REPLACE`](../abap-processing-internal-data/abapreplace.md).

In contrast to regular text replacements, when regular expressions are used, operators can be used in the replacement text that refer to the relevant occurrence.

- [Operators for Replacement Texts](abenregex_posix_replace.md#operators-for-replacement-texts)

  - [Addressing the Full Occurrence](abenregex_posix_replace.md#addressing-the-full-occurrence)

  - [Addressing the Registers of Subgroups](abenregex_posix_replace.md#addressing-the-registers-of-subgroups)

  - [Addressing the Text Before the Occurrence](abenregex_posix_replace.md#addressing-the-text-before-the-occurrence)

  - [Addressing the Text After the Occurrence](abenregex_posix_replace.md#addressing-the-text-after-the-occurrence)

## Operators for Replacement Texts

The following operators can be specified in the replacement text. These operators consist of the special characters `$`, `&`, \`\`\`, and `&#x00B4;`. The special characters can be converted into literal characters by prefixing the escape character `\` or by using the addition [`VERBATIM`](../abap-processing-internal-data/abapreplace_options.md) of the [`REPLACE`](../abap-processing-internal-data/abapreplace.md) statement, where the latter improves the performance.

### Addressing the Full Occurrence

The operators `$0` and `$&` can be specified in the replacement text as placeholders for the entire current occurrence.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After replacement, `text` contains the content *Yeah Yeah Yeah!*.

``` abap
DATA text TYPE string. 
 
text = `Yeah!`. 
 
REPLACE REGEX `\w+` IN text WITH `$0 $0 $&` ##regex_posix.
```

### Addressing the Registers of Subgroups

The operators `$1`, `$2`, `$3`, ... can be used in the replacement text as placeholders for the character strings stored in the registers of [subgroups](abenregex_posix_syntax_operators.md) for the current occurrence. If the n-th subgroup is not available, or it was not supplied with a value in the match, the corresponding operator `$n` is replaced by the empty character string.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After replacement, `text` has the content *Roll'n'Rock*.

``` abap
DATA text TYPE string. 
 
text = `Rock'n'Roll`. 
 
REPLACE REGEX `(\w+)(\W\w\W)(\w+)` IN text WITH `$3$2$1` ##regex_posix.
```

### Addressing the Text Before the Occurrence

The operator ``` $`` can be used in the replacement text as a placeholder in front of the current occurrence\. If multiple occurrences are replaced using  ```REPLACE ALL OCCURRENCES`, `\$\`\` contains the unchanged text from the beginning of the text to the start of the occurrence, for every occurrence.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After replacement, `text` contains the content *again and again*.

``` abap
DATA text TYPE string. 
 
text = `again and`. 
 
REPLACE REGEX 'and' IN text WITH '$0 $`' ##regex_posix.
```

### Addressing the Text After the Occurrence

The operator `$'` can be used in the replacement text as a placeholder for the entire text after the current occurrence.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After replacement, `text` contains the content *and again and*.

``` abap
DATA: text TYPE string. 
 
text = `again and`. 
 
REPLACE REGEX `again ` IN text WITH `$' $0` ##regex_posix.
```
