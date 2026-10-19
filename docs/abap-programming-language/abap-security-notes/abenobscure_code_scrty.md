---
title: "Obscuring ABAP Source Code"
source_file: abenobscure_code_scrty.html
section: "ABAP Programming Language > ABAP Security Notes > Further Security Risks"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Obscuring ABAP Source Code

[ABAP source code](../../abap-glossary/abenabap_source_code_glosry.md) is obscured if tasks that can be performed directly are instead performed across diversions that disguise the real purpose. One common form of obscured code is found when information that could be specified statically is specified using dynamic programming techniques instead. Code can be obscured for one of the following reasons:

- One form of obscured code (which is not directly malicious) is often used to bypass static checks, for example to disguise false positives.

- Code is obscured for malicious purposes to disguise back doors and other forms of attacks using injections.

In general, any type of obscured code presents a security risk. Instead of bypassing static checks by using obscured code, false positives should be handled using other methods, such as exemptions. Obscured code can often only be detected using a two-man rule (code inspections).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Maliciously obscured code in a [user-dependent program flow](abenuser_dependent_scrty.md), which can generally only be detected using code inspections.

``` abap
DATA(field)  = `SY-UNAME`. 
ASSIGN (field) TO FIELD-SYMBOL(<field>). 
... 
IF <field> = `...`. 
  ... 
ENDIF.
```
