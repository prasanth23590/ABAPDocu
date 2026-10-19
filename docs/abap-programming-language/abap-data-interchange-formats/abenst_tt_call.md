---
title: "ST - tt:call, Calling Transformations"
source_file: abenst_tt_call.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Reusing ST Programs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:call, Calling Transformations

## Syntax

``` abap
<tt:call transformation="trafo"> 
  [<tt:with-root name="root1" [ref="node1"] /> 
   <tt:with-root name="root2" [ref="node2"] /> 
   ...] 
  [<tt:with-parameter name="para1" 
                      [ref="node1"|val="val1"|var="var1"] /> 
   <tt:with-parameter name="para2" 
                      [ref="node2"|val="val2"|var="var2"] /> 
   ...] 
</tt:call>  
```

## Description

In an ST program, the statement `tt:call` can be used to call a different ST program `trafo`, as follows: The ST program `trafo` must exist in the repository. `trafo` is not case-sensitive.

The ST statement `tt:with-root` binds the [`data roots`](abenst_tt_root.md) `root1`, `root2`, ... of the main template of the called transformation to the nodes `node1`, `node2`, ... of the current transformation, or passes the ABAP data objects that are currently bound to the specified nodes to these data roots. If `ref` is not specified, the current node of the calling transaction is used.

If formal parameters are declared with [`tt:parameter`](abenst_tt_parameter.md) in the called ST program, these can be linked to the actual parameters with the ST statement `tt:with-parameter`. As actual parameters, `ref` can be used to specify data roots, `var` can be used to specify variables, and [`val`](abenst_abap_representation.md) can be used to specify values. Depending on the type of formal parameter, the values of the specified actual parameters are either passed in the call or used when the called ST program ends.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the ST program `DEMO_ST_CALL1` below, another ST program (here: `DEMO_ST_APPLY1`) is called in a [`tt:loop` loop](abenst_tt_loop.md).

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <tab1> 
      <tt:loop ref="ROOT"> 
        <key> 
          <tt:value ref="key" /> 
        </key> 
        <tt:call transformation="demo_st_apply1"> 
          <tt:with-root name="ROOT" ref="values"/> 
        </tt:call> 
      </tt:loop> 
    </tab1> 
  </tt:template> 
</tt:transform>
```

If the called ST program is implemented as shown in `DEMO_ST_CALL2` below, the transformation has the same function as the [example](abenst_tt_loop.md) of transforming internal tables.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <tab2> 
      <tt:loop ref="ROOT"> 
        <value> 
          <tt:value/> 
        </value> 
      </tt:loop> 
    </tab2> 
  </tt:template> 
</tt:transform>
```
