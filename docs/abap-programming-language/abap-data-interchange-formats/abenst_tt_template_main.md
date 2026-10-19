---
title: "ST - tt:template, Main Template"
source_file: abenst_tt_template_main.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Structure of ST Programs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:template, Main Template

## Syntax

``` abap
<tt:template [name="tmpl"]> 
  ... 
</tt:template>  
```

## Description

The statement `tt:template` defines a template. An ST program must contain at least one definition of a template: Each template of the transformation must be uniquely addressable. To achieve this, each template can be given a unique name, `tmpl`, using the `name` attribute and exactly one template without a name can be specified. The latter is implicitly the main template of the transformation if no template is specified in the root element, [`tt:transform`](abenst_tt_transform.md). Template names are not case-sensitive.

The content of the main template (which can call subtemplates) represents the structure of the XML data to which the ABAP data is serialized or from which the data is deserialized.

The content of a template can consist of literal XML elements and ST statements.
