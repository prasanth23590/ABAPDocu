---
title: "BAdI interface"
source_file: abenbadi_interface_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# BAdI interface

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md)

## Definition

A BAdI interface is a global [interface](abenoo_intf_glosry.md) that includes the [tag interface](abentag_interface_glosry.md) `IF_BADI_INTERFACE`. A BAdI interface can be used as part of the definition of one or more [BAdIs](abenbadi_glosry.md) and may only contain [methods](abenmethod_glosry.md) ([BAdI methods](abenbadi_method_glosry.md)) and [events](abenevent_glosry.md) but not variable [attributes](abenattribute_glosry.md). Furthermore, a BAdI interface cannot contain any [component interfaces](abencomponent_interface_glosry.md) other than other BAdI interfaces. An interface that includes a BAdI interface is also a BAdI interface.
