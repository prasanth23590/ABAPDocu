---
title: "ST - Addressing the Current Node"
source_file: abenst_addressing_current_node.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Addressing ABAP Data > ST - Addressing Data Nodes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Addressing the Current Node

In all ST statements in which the name of a node can be specified, the [current node](abenst_tt_ref.md) can be addressed explicitly with `$ref`. An alias name can be also be defined for `$ref` in [`tt:loop` loops](abenst_tt_loop.md) where internal tables are transformed. If specifying the node is optional, ST statements use the current node by default.

## Hint

If the current node is undefined, it cannot be addressed using `$ref` and ST statements that work implicitly with the current node cannot be executed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following ST program `DEMO_ST_CURRENT_NODE` can be used to serialize a nested ABAP structure:

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <X tt:ref="ROOT"> 
      <X1 tt:ref="$ref.COL1"> 
        <tt:value ref="$ref"/> 
      </X1> 
      <X2 tt:ref="$ref.COL2"> 
        <tt:value ref="$ref"/> 
      </X2> 
      <X3 tt:ref="STRUC2"> 
        <X1 tt:ref="COL1"> 
          <tt:value/> 
        </X1> 
        <X2 tt:ref="COL2"> 
          <tt:value/> 
        </X2> 
      </X3> 
    </X> 
  </tt:template> 
</tt:transform>
```

In this example, subnodes `COL1` and `COL2` are set as the current node in the surrounding elements of the `tt:value` statements with `ROOT` and `STRUC2`, respectively. In the first two elements, the current node is addressed explicitly using `$ref` for demonstration purposes. The current node is also specified using `$ref` in the first two `tt:value` statements, while specification is implicit in the other two `tt:value` statements.

Also see the example for calling a transformation in the [`tt:value`, Structures](abenst_tt_value_structure.md) section.
