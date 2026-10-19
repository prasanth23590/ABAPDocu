---
title: "ST - Addressing Subnodes"
source_file: abenst_addressing_subnodes.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Addressing ABAP Data > ST - Addressing Data Nodes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Addressing Subnodes

When addressing subnodes, it is important to distinguish between a defined and undefined [current node](abenst_tt_ref.md).

## Subnodes when the Current Node is Undefined

If the current node is undefined, the subnodes of the data root of the template can be addressed as follows:

`name.node1.node2. ...`

Here, `name` is the symbolic name of a [data root](abenst_tt_root.md) and `node1`, `node2`, ... are the actual names of components of the hierarchy levels 1, 2, ... When the transformation is executed, the ABAP data object bound to the data root must have a structured type with the corresponding components.

### Hint

If the current node is undefined, the first name of a chain is always interpreted as the name of a data root. In particular, `name` is used for the data root itself.

## Subnodes when the Current Node is Defined

- The subnodes of the current node can be addressed as follows:

  `node1.node2. ...` Here, `node1`, `node2`, ... are the actual names of components of the hierarchy levels 1, 2, ... below the current node. If the current node is defined, the first name of a chain is always interpreted as the name of a component of the current node. The chain above therefore has the same meaning as `$ref.node1.node2. ...` where `$ref` is the current node.

- The subnodes of the data root of the template can be addressed as follows:

  `.name.node1.node2. ...` Here, `name` is the symbolic name of a data root and `node1`, `node2`, ... are the actual names of components of the hierarchy levels 1, 3.... The period (`.`) bypasses the hiding of the root by the current node.

When the transformation is executed, the ABAP data object bound to the current node or to the data root must have a structured type with the corresponding components.

### Hint

If the current node is defined, the first name of a chain is always interpreted as the name of a subcomponent of the current node. In particular, `node` does not stand for a data root, but for a direct subcomponent of the current node.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following ST program `DEMO_ST_ADDRESSING_SUBNODES` can be used to serialize a nested ABAP structure:

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <X> 
      <X1> 
        <tt:value ref="ROOT.COL1"/> 
      </X1> 
      <X2> 
        <tt:value ref="ROOT.COL2"/> 
      </X2> 
      <X3> 
        <X1> 
          <tt:value ref="ROOT.STRUC2.COL1"/> 
        </X1> 
        <X2> 
          <tt:value ref="ROOT.STRUC2.COL2"/> 
        </X2> 
      </X3> 
    </X> 
  </tt:template> 
</tt:transform>
```

For each `tt:value statement`, the current node is set individually to a subnode of the data root. Otherwise the current node is undefined, and the data root `ROOT` can be addressed using its name. Also see the example for calling a transformation in the [`tt:value`, Structures](abenst_tt_value_structure.md) section.
