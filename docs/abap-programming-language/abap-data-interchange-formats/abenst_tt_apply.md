---
title: "ST - tt:apply, Call Subtemplate"
source_file: abenst_tt_apply.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Modularization with Subtemplates"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:apply, Call Subtemplate

## Syntax

``` abap
<tt:apply name="tmpl" [ref="node"]> 
  [<tt:with-root name="root1" [ref="node1"] /> 
   <tt:with-root name="root2" [ref="node2"] /> 
   ...] 
  [<tt:with-parameter name="para1" 
                      [ref="node1"|val="val1"|var="var1"] /> 
   <tt:with-parameter name="para2" 
                      [ref="node2"|val="val2"|var="var2"] /> 
   ...] 
</tt:apply>  
```

## Description

A subtemplate `tmpl` (defined with [`tt:template`](abenst_tt_template_sub.md)) can be called in any other template using the ST statement `tt:apply`. The subtemplate is processed at this point when the including template is executed.

- If custom data roots are declared using [`tt:root`](abenst_tt_template_sub.md) in the called subtemplate, they can be set with the ST statement `tt:with-root`. The optional attribute `ref` can then not be specified in the statement `tt:apply`. `tt:with-root` sets the data root of the name specified in `name` to the node specified in `ref` or binds the data root to the ABAP data object currently bound to the specified node. If `ref` is not specified, the current node of the calling template is used. Local data roots to which no node is bound remain undefined, that is, they do not refer to an ABAP data object. At the beginning of a subtemplate of this type, the current node is undefined.

- If no custom data roots are declared using [`tt:root`](abenst_tt_template_sub.md) in a subtemplate `tmpl`, the root node of the tree structure of the called subtemplate is set either explicitly with the optional attribute `ref` or implicitly to the current node of the calling template at the call position.

- If formal parameters are declared using [`tt:parameter`](abenst_tt_parameter.md) in the called subtemplate, the statement `tt:with-parameter` can be used to associate them with actual parameters. As actual parameters, `ref` can be used to specify data roots, `var` to specify variables, and `val` to specify [values](abenst_abap_representation.md). Depending on the type of formal parameter, the values of the specified actual parameters are either passed in the call or copied when the subtemplate ends (see example below).

  In this case, pass by parameter can be seen as a special case of assignment, which means that the same principle applies as for [`tt:assign`](abenst_tt_assign.md):

  - An assignment with data nodes as the target is possible only in deserializations.

  - An assignment with data nodes as the source is possible only in serializations.
