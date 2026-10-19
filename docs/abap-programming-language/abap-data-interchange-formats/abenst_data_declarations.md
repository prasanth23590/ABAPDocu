---
title: "ST - Data Declarations"
source_file: abenst_data_declarations.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Structure of ST Programs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Data Declarations

In ST programs, data can be declared using the following statements:

- [`tt:root`](abenst_tt_root.md) defines data roots for binding ABAP data interfaces.

- [`tt:parameter`](abenst_tt_parameter.md) defines parameters as formal parameters.

- [`tt:variable`](abenst_tt_variable.md) defines variables as local data.

If these statements are specified outside of a template in the context of the transformation, the data declarations apply to the [main template](abenst_tt_template_main.md).

Within a [subtemplate](abenst_tt_template_sub.md), the statements can be used in the element `tt:context` to declare local data of the subtemplate.
