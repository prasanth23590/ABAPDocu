---
title: "ST - tt:transform, Root Element"
source_file: abenst_tt_transform.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Structure of ST Programs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:transform, Root Element

## Syntax

``` abap
<tt:transform [template="tmpl"]> 
  ... 
</tt:transform>  
```

## Description

The keyword for the root element of an ST program is `tt:transform`. The name of a template `tmpl` can optionally be specified for the `template` attribute. The specified template forms the [main template](abenst_tt_template_main.md) of the transformation. When the program is executed, this template is evaluated. If no explicit main template is specified, the template for which no name is specified is set as the main template by default.
