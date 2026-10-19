---
title: "CDS DDL - DDIC-Based View, field"
source_file: abencds_field_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Elementary CDS Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, field

## Syntax

``` abap
... [entity.]field|[alias.]field ...  
```

## Description

Field of a [data source](abencds_data_source_v1.md) `entity` of the current [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). `field` expects the actual name of the element. Any alternative element names defined using [`AS`](abencds_select_list_entry_v1.md) cannot be used, with the exception of the `ON` condition of a [CDS association](../../abap-glossary/abencds_association_glosry.md).

If the view entity makes use of multiple [data sources](abencds_data_source_v1.md) by using join expressions, then you must ensure that all field names are unique. If a field name `field` is not unique, then `field` must be prefixed with the name `entity` of the data source or with the alias name `alias` of the data source separated by a period (.). If the field name is unique, it may but does not need to be prefixed.
