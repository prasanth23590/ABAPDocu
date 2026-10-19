---
title: "Conversions, Performance Notes"
source_file: abenconversion_perfo.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Conversions, Performance Notes

Conversions in assignments between data objects with different data types or a data object specified in an operand position where a different data type is expected, cause runtime costs. To avoid these costs, conversions should be avoided if possible and only data objects of the same type should be assigned to one another.

## Executable Example

[Conversion Costs](abenconversion_costs_abexa.md)
