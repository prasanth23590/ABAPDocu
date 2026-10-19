---
title: "ST - Addressing ABAP Data"
source_file: abenst_addressing.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Addressing ABAP Data

Simple transformations are used to serialize ABAP data or deserialize XML documents to ABAP data objects. Accordingly, it must be possible to address the bound ABAP data in the ST programs. Serializations only allow reads on ABAP data, while deserializations allow only writes.

In an ST program, all data bound to ABAP data objects is considered as data nodes, that is, nodes in tree structures, spread from the data roots. To address the ABAP data, either the data roots are accessed or the current node. At any position of an ST program, exactly one node of the tree structure spreading from the data root can be defined as the current node. The data roots or the current node can be accessed directly and, from that position, the subnodes.

- [Tree Structure of the Data Nodes](abenst_trees.md)

- [Current Node](abenst_tt_ref.md)

- [Addressing Data Nodes](abenst_addressing_nodes.md)

## Hint

No reference variables can currently be serialized and deserialized in ST programs. ABAP reference variables can, however, be bound to data roots. This means that these data roots cannot be specified in ST serialization and deserialization statements. Object reference variables can, however, be used to call instance methods and all reference variables can be passed to appropriate interface parameters of called ABAP methods.
