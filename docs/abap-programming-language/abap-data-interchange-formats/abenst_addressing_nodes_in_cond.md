---
title: "ST - Data Nodes in Conditions"
source_file: abenst_addressing_nodes_in_cond.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Addressing ABAP Data > ST - Addressing Data Nodes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Data Nodes in Conditions

For addressing data nodes in [logical expressions](abenst_tt_cond.md), a special rule applies. Data nodes as `dnode` operands of [preconditions](abenst_using.md), [assertions](abenst_data.md), or [conditions](abenst_check.md) can be specified as follows:

- If the name `node`, specified in accordance with the preceding addressing rules, contains a letter or an underscore in its first place and only letters, digits, hyphens, or underscores in the remaining positions, it can be specified directly.

- The special names `$ref` and `$alias` can also be specified directly.

- All other names must be specified in the form `ref('node')`. This particularly applies to the specification of a data root using `.root`.
