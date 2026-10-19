---
title: "CDS DDL - DEFINE TYPE"
source_file: abencds_define_type.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Type Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE TYPE

## Syntax Forms

**[CDS Simple Types](abencds_simple_types.md)**

``` abap
1. [@type_annot1] 
   [@type_annot2] 
   ... 
   DEFINE TYPE simple_type : dtype 
                           | data_element 
                           | simple_type
```

**[CDS Enumerated Types](abencds_enumeration_types.md)**

``` abap
2. [@type_annot1] 
   [@type_annot2] 
   ... 
     DEFINE TYPE EnumType : BaseType ENUM 
     { 
       [@enum_annot1] 
        EnumConstant1 = EnumValue1 | initial; 
       [@enum_annot2] 
        EnumConstant2 = EnumValue2 | initial; 
       [...] 
     } 
   | DEFINE TYPE EnumType : EnumType[;]
```

[`@type_annot1`](abencds_simple_type_anno.md) · [`@type_annot2`](abencds_simple_type_anno.md) · [`dtype`](../abap-cds-data-types/abencds_overview_builtin_types.md) · [`data_element`](abencds_dtel.md) · [`simple_type`](abencds_simple_type.md) · [`@type_annot1`](abencds_enum_type_anno.md) · [`@type_annot2`](abencds_enum_type_anno.md)

## Description

The statement `DEFINE TYPE` defines a [CDS user-defined type](../../abap-glossary/abencds_user_defined_type_glosry.md).

- Without the addition `ENUM`, the type is a [CDS simple type](../../abap-glossary/abencds_simple_type_glosry.md) that defines an [elementary data type](../../abap-glossary/abenelementary_data_type_glosry.md).

- With the addition `ENUM`, the type is a [CDS enumerated type](../../abap-glossary/abencds_enum_type_glosry.md) that defines an [enumerated type](../../abap-glossary/abenenum_type_glosry.md).
