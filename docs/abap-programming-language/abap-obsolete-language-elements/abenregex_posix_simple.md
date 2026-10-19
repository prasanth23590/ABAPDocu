---
title: "POSIX regex - Simplified Regular Expressions (obsolete)"
source_file: abenregex_posix_simple.html
section: "ABAP Programming Language > ABAP - Obsolete Language Elements > Obsolete Processing of Internal Data > Obsolete Character String and Byte String Processing > Obsolete Regular Expression Syntax > regex - POSIX Syntax (obsolete)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# POSIX regex - Simplified Regular Expressions (obsolete)

In addition to the regular expressions in accordance with the extended [POSIX](https://en.wikipedia.org/wiki/POSIX) standard IEEE 1003.1, the class `CL_ABAP_REGEX` also offers an alternative type of simplified regular expression with restricted functions. These simplified regular expressions (short: simplified expressions) do not support all POSIX operators and use partially different syntax. The semantics of regular expressions and simplified expressions are, however, the same.

## Simplified Syntax

The following table provides an overview of the syntax differences between regular expressions and simplified regular expressions.

| **Regular Syntax** | **Simplified Syntax** |
|--------------------|-----------------------|
| `*`                | `*`                   |
| `+`                | Not supported         |
| `{ }`              | `\{ \}`               |
| `( )`              | `\( \)`               |
| `[ ]`              | `[ ]`                 |
| `\|`               | Not supported         |
| `(?= ) (?! )`      | Not supported         |
| `(?: )`            | Not supported         |

This table shows that many special characters in the regular syntax have no effect in the simplified syntax. Parentheses and curly brackets must be prefixed with the character `\` if they are to keep their function in the regular syntax.

### Hints

- Regular expressions with simplified syntax can only be used within the class `CL_ABAP_REGEX`. If the value `'X'` is passed to the input parameter `simple_regex`, the regular expression is handled in accordance with the simplified syntax. By default, syntax in accordance with the extended POSIX standard is used. If the simplified syntax is to be used in the statements `FIND` or `REPLACE`, an object of the class `CL_ABAP_REGEX` must be passed.

- The simplified syntax corresponds to the syntax of regular expressions in the command `grep` on Unix.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This table shows the differences in parentheses between regular syntax and simplified syntax. The final two columns show examples that match the expressions in the first column, depending on the syntax used.

| **Pattern** | **Regular Syntax** | **Simplified Syntax** |
|-------------|--------------------|-----------------------|
| `(.)`       | a                  | \(a\)                 |
| `\(.\)`     | \(a\)              | a                     |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first search uses regular syntax and finds the first three letters *aaa*. The second search has simplified syntax, where *+* does not have any meaning as a special character and finds the substring *a+* from offset 2.

``` abap
DATA res TYPE match_result_tab. 
 
FIND ALL OCCURRENCES OF REGEX ##regex_posix 
  cl_abap_regex=>create_posix( pattern = 'a+' 
                               simple_regex = abap_false ) 
  IN 'aaa+bbb' RESULTS res. 
 
FIND ALL OCCURRENCES OF REGEX ##regex_posix 
  cl_abap_regex=>create_posix( pattern = 'a+' 
                               simple_regex = abap_true ) 
  IN 'aaa+bbb' RESULTS res.
```
