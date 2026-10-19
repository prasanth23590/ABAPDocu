---
title: "ST - tt:template, tt:context, Create Subtemplate"
source_file: abenst_tt_template_sub.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Modularization with Subtemplates"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:template, tt:context, Create Subtemplate

## Syntax

``` abap
<tt:template name="tmpl"> 
  [<tt:context> 
    [<tt:root name="root1" [[line-]type=...] /> 
     <tt:root name="root2" [[line-]type=...] /> 
     ...] 
    [<tt:parameter name="para1" [[s-|d-]val="def1"] 
                                [kind="knd1"] /> 
     <tt:parameter name="para2" [[s-|d-]val="def2"] 
                                [kind="knd2"] /> 
     ...] 
    [<tt:variable name="vari1" [[s-|d-]val="val1"] /> 
     <tt:variable name="vari2" [[s-|d-]val="val2"] /> 
     ...] 
   </tt:context>] 
  ... 
</tt:template>  
```

## Description

Like the [main template](abenst_tt_template_main.md), subtemplates are defined with `tt:template`. The attribute `name` must be used to define a unique name `tmpl` for the subtemplate.

### Data in Subtemplates

## Description

In a subtemplate, custom data can be declared: `tt:context` can be used to define a context for the statements [`tt:root`](abenst_tt_root.md), [`tt:variable`](abenst_tt_variable.md), and [`tt:parameter`](abenst_tt_parameter.md). The statement `tt:context` is only allowed in subtemplates and the statements `tt:root`, `tt:variable`, and `tt:parameter` are only allowed in a template within the `tt:context` element.

As in the main template, there are three categories of data, all in a single namespace:

- Data roots

  The data roots declared with `tt:root` have exactly the same meaning for the subtemplate as the data roots declared at the highest hierarchy level of the transformation for the main template. This means that they also spread independent tree structures. In contrast to the data roots of the main template, the local data roots of subtemplates do not form a Simple Transformation interface to the ABAP program, but instead an interface to the including template, to which an ABAP data object can be bound with [`tt:with-root`](abenst_tt_apply.md). The data roots of the subtemplates can be typed just like those of the main templates using attribute `[line-]type`.

- Parameters

  The parameters declared using `tt:parameter` are formal parameters of the subtemplate, to which a value can be passed using [`tt:with-parameter`](abenst_tt_apply.md). Otherwise, the same applies as to the parameters of the main template.

- Variables

  The variables declared with `tt:variable` are local variables of the subtemplate and are only visible there. Otherwise, the same applies as to the variables of the main template.

## Hint

Local types cannot be defined in subtemplates using [`tt:type`](abenst_tt_type.md).

### Addressing Data in Subtemplates

## Description

A subtemplate without its own data roots creates a separate tree structure of data nodes whose root node is the [current node](abenst_tt_ref.md) from the calling position in the calling template. As a prerequisite for calling a template like this, the current node must be defined at the call position. At the start of the subtemplate, this root node is also the current node of the subtemplate. In a subtemplate like this, the current node can be [set](abenst_tt_ref.md) as described for main templates, but in contrast to main templates, it is never undefined. Data nodes outside of the tree structure of the subtemplate cannot be addressed. In particular, the data roots of the main template cannot be addressed with `.name`.

Addressing the data nodes of a subtemplate with its own data roots happens exactly as described for the main template. As long as no current node is defined, the data roots of the subtemplate can be addressed using `name`. After they are hidden by a current node, they can only be addressed with `.name`.

## Hint

Figuratively speaking, a subtemplate without its own data roots works exclusively with the substructure of the main template tree structure whose root nodes it was bound to.
