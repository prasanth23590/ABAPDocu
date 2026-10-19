---
title: "ST - tt:ref, Current Node"
source_file: abenst_tt_ref.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Addressing ABAP Data"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:ref, Current Node

## Syntax

``` abap
... [tt:]ref ...  
```

## Description

Exactly one node of the tree structures of the current template can be set as the current node at any position within a Simple Transformation (statically and when the program is executed). The current node hides the data roots in the sense that a reference `name` does not refer to a root `name`, but to the component `name` of the current node (see [Addressing Subnodes](abenst_addressing_subnodes.md)). If the current node is defined, it is the implicit operand of many [ST statements](abenst_statements.md), but it can also be addressed explicitly using `$ref`.

This section shows how to set the current node explicitly using `[tt:]ref`. In addition, the statement [`tt:loop`](abenst_tt_loop.md) for transforming internal tables also sets the current node.

At positions where the current node is not set explicitly, it is undefined and cannot be addressed using `$ref`. In these positions, the data roots are not hidden, and they can be addressed using `name`.

**Set the Current Node Using a Statement**

``` abap
<tt:ref name="node"> 
  ... 
</tt:ref>
```

The statement `tt:ref` sets the current node to the node specified in `node`. Any addressable data node can be specified for `node`. If no valid node is specified, the current node is undefined.

The `tt:ref` statement can be nested. It builds a context in which the currently set node is valid. Outside the associated XML element, the current outermost node is still valid. At the top level, the current node is always undefined.

The statement `tt:ref` itself has no operational effect; it only affects the impact of the statements nested within it.

## Hint

As a result of the [addressing rules](abenst_addressing_nodes.md), only a subnode of the current node can be set as the new current node, unless a data root is being set.

**Set the Current Node Using an Attribute**

``` abap
<tt:... ref="node"> 
  ... 
</tt:...>
```

Many [ST statements](abenst_statements.md) make it possible to specify the current node as the content of the attribute `ref`. The same rules apply to `node` as when setting using the statement `tt:ref`. If no attribute `ref` is specified, the statement applies to the current node of the context. The currently set node is valid only within the context of the ST statement.

**Set the Current Node in Literal XML Elements**

``` abap
<... tt:ref="node"> 
  ... 
</...>
```

In a [literal XML element](abenst_xml_literals.md), `tt:ref` is a special attribute in the namespace of the ST statement and sets the current node there. The same rules apply to `node` as for setting with the `tt:ref` statement. The currently set node is valid only within the context of the XML element.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following ST program `DEMO_ST_REF` can be used to serialize a nested ABAP structure:

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <X tt:ref="ROOT"> 
      <X1> 
        <tt:value ref="COL1" /> 
      </X1> 
      <X2> 
        <tt:value ref="COL2" /> 
      </X2> 
      <X3 tt:ref="STRUC2"> 
        <X1> 
          <tt:value ref="COL1" /> 
        </X1> 
        <X2> 
          <tt:value ref="COL2" /> 
        </X2> 
      </X3> 
    </X> 
  </tt:template> 
</tt:transform>
```

The current node is changed as follows:

- At the beginning of the (nameless) main template, the current node is undefined. The data root `ROOT` can be addressed directly using *ROOT*.

- The current node is set to the data root for the element `X`. Within the `X` element, only *.ROOT* could be used for addressing the data root directly.

- In the context of the two subsequent `tt:value` statements, the current node is set to the subnodes `COL1` and `COL2` of `ROOT`. The statements serialize or deserialize the ABAP data object that is bound to the current node.

- The current node for literal element `X3`, which is nested in `X`, is set to another subnode `STRUC2` of `ROOT`.

- In the context of the two subsequent `tt:value` statements, the current node is set to the subnodes `COL1` and `COL2` of `STRUC2`. Each time an element is exited, the current node is reset to that of the surrounding element.

See also the example for calling the transformation in the [`tt:value`, Structures](abenst_tt_value_structure.md) section.
