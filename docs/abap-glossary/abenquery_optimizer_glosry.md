---
title: "SAP HANA SQL optimizer"
source_file: abenquery_optimizer_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SAP HANA SQL optimizer

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md)

## Definition

The query optimizer generates the most efficient query execution plan for a given query and passes it to the executor. In [HANA SQL](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f), there are basically two optimization tasks:

- Rule-based optimization (declarative): Rewriting of the entire tree by, for example, removing joins. More efficient queries are produced at best.

- Cost-based optimization (procedural): Discovering the space of access plans of the queries produced during the rule-based optimization and comparing the access plans by cost and size. The cheapest query is used for further processing.

[***-\>* More about**](https://help.sap.com/docs/SAP_HANA_PLATFORM/9de0171a6027400bb3b9bee385222eff/d2948cc2209a407ea2b686c29e72ca50)
