---
title: "CDS DCL - DEFINE ROLE, if_then_else"
source_file: abencds_f1_dcl_ifthenelse.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE > CDS DCL - DEFINE ROLE, condition"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, if_then_else

## Syntax

``` abap
... IF ( condition ) THEN { condition } ELSE { condition } ...  
```

## Description

The condition `condition` in the `IF` branch is evaluated in the application server. If the result is *true*, the `if_then_else` is replaced by the condition in the `THEN` branch, otherwise by the condition in the `ELSE` branch.

## Hints

- The condition in the `IF` branch must contain only [left-side host expressions](abencds_dcl_cond_left_side.md) (that is, it must not contain a reference to any elements of the CDS entity). Parentheses and logical operators are allowed.

- The conditions in the `THEN` and `ELSE` branches can be any condition, including a nested `if_then_else`.

- The separation between the `THEN` and the `ELSE` branches occurs at runtime. At compile time, both branches must be syntactically valid.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This condition tests whether the actual value of the view parameter `P1` is either `NEW` or `MODERN` and in addition whether the current user has any authorization for the authorization object `S_DEMO`. If this condition is true, the access condition using the fields `A_NEW` and `B_NEW` applies, otherwise the one using `A_OLD` and `B_OLD` applies.

``` abap
GRANT SELECT ON cds_entity 
  WHERE 
    IF 
      ( 
        ( $PARAMETERS.P1 = 'NEW' OR $PARAMETERS.P1 = 'MODERN' ) 
          AND 
        ( ) = ASPECT PFCG_AUTH( S_DEMO ) 
      ) 
    THEN 
      { 
        A_NEW = 1 AND ( B_NEW ) = ASPECT PFCG_AUTH( S_DEMO, F1 ) 
      } 
    ELSE 
      { 
        A_OLD = 1 AND ( B_OLD ) = ASPECT PFCG_AUTH( S_OLD, F1 ) 
      };
```
