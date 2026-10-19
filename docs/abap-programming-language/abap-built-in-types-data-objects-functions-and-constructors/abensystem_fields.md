---
title: "ABAP System Fields"
source_file: abensystem_fields.html
section: "ABAP Programming Language > ABAP - Built-In Types, Data Objects, Functions, and Constructors > Built-In Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP System Fields

System fields are filled by the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md) and can be used in an ABAP program to query system states.

Reads can be performed on the following system fields in the current ABAP language version:

| **Name**                                       | **Type** | **Length** | **Content**                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------------------|----------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `sy-batch`                                     | `c`      | 1          | Set to *X* in an ABAP program that runs in the background; otherwise initial.                                                                                                                                                                                                                                                                                                                                                    |
| `sy-dbcnt`                                     | `i`      | \-         | SQL statements set the content of `sy-dbcnt` to the number of processed table lines.                                                                                                                                                                                                                                                                                                                                             |
| `sy-fdpos`                                     | `i`      | \-         | Found position for specific operations on character-like or byte-like data objects (for example [comparisons](../abap-program-flow-logic/abenlogexp_strings.md) or the obsolete statement `SEARCH`).                                                                                                                                                                                                                                                      |
| `sy-index`                                     | `i`      | \-         | Loop index. In `DO` and `WHILE` loops, this contains the number of previous loop passes, including the current pass.                                                                                                                                                                                                                                                                                                             |
| `sy-langu`                                     | `c`      | 1          | Single-character language key (such as *E*, `D`, or `F`) for the [text environment language](../../abap-glossary/abentext_env_langu_glosry.md) of the current [internal session](../../abap-glossary/abeninternal_session_glosry.md). The text environment language is the [logon language](../../abap-glossary/abenlogon_language_glosry.md) by default.                                                                                                                              |
| `sy-mandt`                                     | `c`      | 3          | [Client ID](../../abap-glossary/abenclient_identifier_glosry.md) with which the current user has logged on, for example `401` or `800`.                                                                                                                                                                                                                                                                                                            |
| `sy-msgid`                                     | `c`      | 20         | After the statement `MESSAGE`, contains the message class. After `MESSAGE ... RAISING`, is also set in the calling program if it handles the exception.                                                                                                                                                                                                                                                                          |
| `sy-msgno`                                     | `n`      | 3          | After the statement `MESSAGE`, contains the message number. After `MESSAGE ... RAISING`, is also set in the calling program if it handles the exception.                                                                                                                                                                                                                                                                         |
| `sy-msgty`                                     | `c`      | 1          | After the statement `MESSAGE`, contains the message type. After `MESSAGE ... RAISING`, is also set in the calling program if it handles the exception.                                                                                                                                                                                                                                                                           |
| `sy-msgv1`, `sy-msgv2`, `sy-msgv3`, `sy-msgv4` | `c`      | 50         | After the statement `MESSAGE`, contains the field content used as placeholders of the [message](../../abap-glossary/abenmessage_glosry.md). After `MESSAGE ... RAISING`, is also set in the calling program if it handles the exception. When a database lock is requested using an `ENQUEUE` function module, `sym-sgv1` contains the name of the user holding the lock after the exception `FOREIGN_LOCK`.                                       |
| `sy-subrc`                                     | `i`      | \-         | [Return code](../../abap-glossary/abenreturn_code_glosry.md) that is set by many ABAP statements. In general, the value 0 means that the statement was executed without problems. Depending on which statement was used to set `sy-subrc`, the cause of an error can be derived from this value. The content of `sy-subrc` keeps its previous value or is undefined after statements where the setting of `sy-subrc` is not documented explicitly. |
| `sy-sysid`                                     | `c`      | 8          | [System ID](../../abap-glossary/abensystem_id_glosry.md) of [AS ABAP](../../abap-glossary/abenas_abap_glosry.md), for example `S01` or `K99`.                                                                                                                                                                                                                                                                                                                        |
| `sy-tabix`                                     | `i`      | \-         | Line number in the table index of an [internal table](../../abap-glossary/abeninternal_table_glosry.md). Contains the last line addressed using a [primary](../../abap-glossary/abenprimary_table_index_glosry.md) or [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md). Is set to 0 when accessed using a [hash algorithm](../../abap-glossary/abenhash_algorithm_glosry.md).                                                                                            |
| `sy-uname`                                     | `c`      | 12         | [User name](../../abap-glossary/abenuser_name_glosry.md) of the current [user session](../../abap-glossary/abenuser_session_glosry.md), for example `KELLERH`.                                                                                                                                                                                                                                                                                                       |

## Hints

- Although it is not syntactically forbidden, data objects or types with the names `sy` or `syst` or with the names of the system fields themselves in programs should not be created separately, since they can hide built-in data objects and types.

- The content of system fields is only defined as described in the table above or for individual ABAP statements. In contexts other than those described, the content of system fields is not reliable. In particular statements where no effect on system fields is documented may affect the content of certain system fields, such as `sy-subrc`, in undefined ways. This is especially true for statements that call ABAP code implicitly or explicitly when executed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Typical evaluation of the system field `sy-subrc` after a [`SELECT`](../abap-database-access/abapselect.md) statement.

``` abap
SELECT SINGLE * 
       FROM scarr 
       WHERE carrid = '...' 
       INTO @FINAL(wa). 
 
IF sy-subrc <> 0. 
  RETURN. 
ENDIF.
```

Besides the allowed read access to the system fields in the above table, read access to all other system fields is tolerated in the current ABAP language version for compatibility reasons but leads to a warning of the syntax check. This includes all system fields that are released for usage in ABAP programs as well as internal and obsolete system fields. The documentation of all system fields can be found in the ABAP Keyword Documentation for [classic ABAP](../../abap-glossary/abenclassic_abap_glosry.md):

- [Released system fields](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/index.htm?file=abensystem_fields.htm)

- [Internal system fields](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/index.htm?file=abensystem_fields_internal.htm)

- [Obsolete system fields](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/index.htm?file=abensystem_fields_obsolete.htm)
