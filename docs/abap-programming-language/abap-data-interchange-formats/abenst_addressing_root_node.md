---
title: "ST - Addressing the Data Roots"
source_file: abenst_addressing_root_node.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Addressing ABAP Data > ST - Addressing Data Nodes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Addressing the Data Roots

The [data roots](abenst_tt_root.md) declared at the highest hierarchy level of an ST program are the root nodes of the [tree structures](abenst_trees.md) of the data nodes of the [main template](abenst_tt_template_main.md). Addressing a data root during the execution of an ST program means referring to the bound ABAP data object.

## Addressing when the Current Node is Undefined

If a data root is not hidden by the definition of a [current node](abenst_tt_ref.md), it can be addressed directly using

`root`

where `root` is the symbolic name declared after [`tt:root`](abenst_tt_root.md).

## Addressing when the Current Node is Defined

A data root `root` can be addressed at any position of the main template using

`.root`

where the period (`.`) bypasses cases where the root is hidden by a current node.

### Hint

In [subtemplates](abenst_tt_template_sub.md), the rules for the root nodes of their tree structures apply.
