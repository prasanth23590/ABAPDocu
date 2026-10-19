---
title: "ST - tt:cond-var, Condition for Variables"
source_file: abenst_tt_cond-var.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Flow Control > ST - Flow Control with Variables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:cond-var, Condition for Variables

## Syntax

``` abap
<tt:cond-var check="..."> 
   ... 
</tt:cond-var>  
```

## Description

The statement `tt:cond-var` allows conditional transformations for which, unlike `tt:[s-|d-]cond`, only data content can be specified and not conditions for the data flow. The content of `tt:cond-var` is processed depending on a [`check` condition](abenst_check.md). `cond` is the same as general conditions, with the exception that [variables](abenst_tt_variable.md) and [values](abenst_abap_representation.md) can be specified as operands, but not [data nodes](abenst_addressing_nodes.md).

Outside of `tt:switch-var`, a condition [`check`](abenst_tt_switch-var.md) must be specified.

**Serialization and Deserialization**

In serializations and deserializations, the condition is checked and the content of the element `tt:cond-var` is only processed if the condition is met.

## Hint

Unlike general conditional transformations with [`tt:[s-|d-]cond`](abenst_tt_cond.md), the content of the XML input stream for `tt:cond-var` is irrelevant.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following transformation `DEMO_ST_COND_VAR` demonstrates a condition for a parameter:

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
    <tt:cond-var check="PARA&lt;100"> 
      <X val="small">...</X> 
    </tt:cond-var> 
    <tt:cond-var check="PARA&gt;=100"> 
      <X val="big">...</X> 
    </tt:cond-var> 
  </tt:template> 
</tt:transform>
```

In `tt:apply`, the value of the data root `ROOT` is passed to the parameter `PARA` of the [subtemplate](abenst_tt_template_sub.md) `SUB` and checked there. Depending on whether the ABAP data object bound to `ROOT` is smaller, greater than, or equal to 100, the serialization creates either of the following:

- `<X val="small">...</X>` or

- `<X val="big">...</X>`.

`var(PARA)` could be written in the conditions `check` instead of `PARA`.
