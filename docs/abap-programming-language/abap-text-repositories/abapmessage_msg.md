---
title: "MESSAGE, msg"
source_file: abapmessage_msg.html
section: "ABAP Programming Language > ABAP - Text Repositories > Messages > MESSAGE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MESSAGE, msg

## Syntax

``` abap
... { tn }   
  | { tn(id) }   
  | { ID mid TYPE mtype NUMBER num }    ...  
```

### Alternative

[1. `... tn ...`](abapmessage_msg.md#alternative-1)

[2. `... tn(id) ...`](abapmessage_msg.md#alternative-2)

[3. `... ID mid TYPE mtype NUMBER num ...`](abapmessage_msg.md#alternative-3)

## Overview

### Description

`msg` specifies a [message](../../abap-glossary/abenmessage_glosry.md) from the database table `T100` either by specifying the message key consisting of `id` and `n` directly or by using the content of the data objects `mid` and `num` for the message class and the message number. Alternatively, an object reference variable `oref` is specified whose [dynamic type](../../abap-glossary/abendynamic_type_glosry.md) implements the interface [`IF_T100_MESSAGE`](abenif_t100_message.md).

The [message type](../../abap-glossary/abenmessage_type_glosry.md) that controls the behavior of the message must be specified directly in `t` or as content of the data object `mtype`. The following message types are possible: *A*, *E*, *I*, *S*, *W*, or *X*. An invalid type produces a syntax error or runtime error.

If the specified message is not found for the [logon language](../../abap-glossary/abenlogon_language_glosry.md) of the current user, a search is made in the [secondary language](../../abap-glossary/abensecondary_language_glosry.md) in AS ABAP and then in English. If it is still not found, the specified message type, message class, and message number are used as short text in uppercase letters and separated by a colon *:*.

The system fields of the statement `MESSAGE` are always supplied with the specified values.

## Alternative 1

`... tn ...`

### Description

`t` and `n` are used to specify the single-character message type and the three-digit message number directly one after another (static short form). The message class must be specified with the addition `MESSAGE-ID` in the statement that introduces the program.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Display of the short text of the message with the number 014 from the message class `SABAPDOCU` as an [information message](../../abap-glossary/abeninformation_message_glosry.md).

``` abap
REPORT rep MESSAGE-ID sabapdemos. 
... 
MESSAGE i014.
```

## Alternative 2

`... tn(id) ...`

### Description

The same applies to `t` and `n` as to the static short form. In the static long form, the message class is specified directly in parentheses using `id`.

### Hint

Specifying the message class explicitly overrides the addition `MESSAGE-ID` of the statement that introduces the program. Specifying the message class in parentheses does not mean here that the content of `id` is used. Instead, the message class is used that has the name that was specified directly with `id`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

As in the example for alternative 1, with the message class specified explicitly.

``` abap
MESSAGE i014(sabapdemos) INTO FINAL(msg).
```

## Alternative 3

`... ID mid TYPE mtype NUMBER num ...`

### Description

The message class, the message type, and the message number are specified as content of the data objects `mid`, `mtype`, and `num` (dynamic form). `mid` and `mtype` expect character-like data objects that must contain the message class or the message type in uppercase letters. Invalid message types raise an uncatchable exception. `num` expects a data object of the type `n` and length 3.

### Hint

Specifying the message class explicitly overrides the addition `MESSAGE-ID` of the statement that introduces the program.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

As in the example for alternative 2, with the message and the message type specified dynamically.

``` abap
DATA: mid   TYPE sy-msgid VALUE 'SABAPDEMOS', 
      mtype TYPE sy-msgty VALUE 'I', 
      num   TYPE sy-msgno VALUE '014'. 
 
MESSAGE ID mid TYPE mtype NUMBER num INTO FINAL(msg).
```

## Alternative 4

`... oref [TYPE mtype] ...`

\*\* This syntax is not available in the current ABAP language version.\*\*
