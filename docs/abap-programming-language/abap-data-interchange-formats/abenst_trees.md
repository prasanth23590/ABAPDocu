---
title: "ST - Tree Structure of the Data Nodes"
source_file: abenst_trees.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Addressing ABAP Data"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Tree Structure of the Data Nodes

The starting points of any addressing of ABAP data in an ST program are the data roots of the [main template](abenst_tt_root.md) declared with [`tt:root`](abenst_tt_root.md) at transformation level. These data roots are the interfaces from the ST program to the calling ABAP program. When a Simple Transformation is called, any ABAP data object (reference variables or data objects that have reference variables as components are currently excluded) can be bound to any data root.

Each data root has its own tree structure, which can be used to address the components of the bound data object. Addressing subnodes of a data root is equivalent to referring to the components of the data object bound to the data root. The tree structures of the individual data roots are independent of one another.

The addressing of data nodes in the individual tree structures always starts at the data roots.

\*\* Note\*\*

Each template uses its own tree structures. Only the main template uses the data roots declared at transformation level that are bound directly to the ABAP data objects during transformation. When [subtemplates](abenst_tt_template_sub.md) are called, local data roots are bound to current data nodes of the caller.
