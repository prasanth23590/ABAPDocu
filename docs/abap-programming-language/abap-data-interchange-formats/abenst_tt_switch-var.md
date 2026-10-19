---
title: "ST - tt:switch-var, Case Distinction for Variables"
source_file: abenst_tt_switch-var.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Flow Control > ST - Flow Control with Variables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:switch-var, Case Distinction for Variables

## Syntax

``` abap
<tt:switch-var> 
  <tt:[s-|d-]cond-var ... 
  <tt:[s-|d-]cond-var ... 
  ... 
</tt:switch-var>  
```

## Description

The statement `tt:switch-var` allows case distinctions in which, unlike `tt:switch`, only cases for data content can be specified, not for the data flow. In `tt:switch`, a list of cases can be shown where the syntax of each case is formulated by a condition for variables, namely a [`tt:cond-var`](abenst_tt_cond-var.md) subelement. Other direct subelements are not possible in `tt:switch-var`.

A maximum of one case can be specified that does not contain a [`check`](abenst_check.md) condition.

**Serialization and Deserialization**

Serialization and deserialization follow these rules:

1.  The first case `tt:cond-var`, whose explicitly specified condition `check` is met, is processed and the element `tt:switch-var` is exited.

2.  If no condition is met for any case with explicitly specified conditions, the case without condition is executed by default (if it exists) and the element `tt:switch-var` is exited.

3.  If no case without condition exists, the element `tt:switch-var` is exited without any case being processed.

## Hint

Unlike the general case distinction with [`tt:switch`](abenst_tt_switch.md), the content of the cases is irrelevant.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following transformation `DEMO_ST_SWITCH_VAR` expands the example from [Conditions for Variables](abenst_tt_cond-var.md).

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <tt:apply name="SUB"> 
      <tt:with-parameter name="PARA" ref="ROOT"/> 
    </tt:apply> 
  </tt:template> 
  <tt:template name="SUB"> 
    <tt:context> 
      <tt:parameter name="PARA"/> 
    </tt:context> 
    <tt:switch-var> 
      <tt:cond-var check="PARA&lt;50"> 
        <X val="small">...</X> 
      </tt:cond-var> 
      <tt:cond-var check="PARA&lt;100"> 
        <X val="medium">...</X> 
      </tt:cond-var> 
      <tt:cond-var> 
        <X val="big">...</X> 
      </tt:cond-var> 
    </tt:switch-var> 
  </tt:template> 
</tt:transform>
```

Depending on the value of the ABAP data object bound to `ROOT`, the serialization creates either of the following:

- `<X val="small">...</X>` or

- `<X val="medium">...</X>` or

- `<X val="big">...</X>`.

The position of the element `tt:cond-var` without explicit condition within `tt:switch-var` is irrelevant. However, the order of the elements `tt:cond-var` with explicit conditions is relevant.
