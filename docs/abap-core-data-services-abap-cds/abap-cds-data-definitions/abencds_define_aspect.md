---
title: "CDS DDL - DEFINE ASPECT"
source_file: abencds_define_aspect.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Aspects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE ASPECT

## Syntax

``` abap
 
[@aspect_annot1] 
[@aspect_annot2] 
... 
DEFINE ASPECT aspect 
       element_list   
```

[`@aspect_annot1`](abencds_ddl_aspect_anno.md) · [`@aspect_annot2`](abencds_ddl_aspect_anno.md) · [`element_list`](abencds_ddl_aspect_element_list.md)

## Description

Defines a [CDS aspect](../../abap-glossary/abencds_aspect_glosry.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md).

The name of the aspect is defined after the `DEFINE ASPECT` statement. The usual rules for ABAP Dictionary views apply to this name and it is not case-sensitive (it is transformed internally into uppercase letters). It can have a maximum of 30 characters and is in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP. The name of the DDL source and of the CDS object must be identical.

- [`aspect annotations`](abencds_ddl_aspect_anno.md) can be used to define optional header annotations for the CDS aspect.

- [`element_list`](abencds_ddl_aspect_element_list.md) is used to declare elements of the CDS aspect.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following aspect contains various different data types that can then be reused in numerous CDS entities.

``` abap
@EndUserText.label: 'Demo Aspect' 
define aspect DEMO_CDS_ASPECT_ALL_TYPES {   
 
  key id     : abap.char(1); 
  int1       : abap.int1; 
  int2       : abap.int2; 
  int4       : abap.int4; 
  int8       : abap.int8;   
  dec10_2    : abap.dec(10,2);   
  d16n       : abap.decfloat16; 
  d34n       : abap.decfloat34; 
  fltp       : abap.fltp; 
  char10     : abap.char(10); 
  sstring512 : abap.sstring(512); 
  string     : abap.string(0); 
  raw10      : abap.raw(10); 
  dats       : abap.dats; 
  tims       : abap.tims; 
  datn       : abap.datn; 
  timn       : abap.timn; 
  utcl       : abap.utclong;   
  numc1      : abap.numc(1); 
  numc10     : abap.numc(10); 
  clnt       : abap.clnt; 
  lang       : abap.lang; 
  unit2      : abap.unit(2); 
     
  geom_ewkb  : abap.geom_ewkb; 
  lchr_int   : abap.int4; 
  @Semantics.amount.currencyCode : 'cuky' 
  curr10_2   : abap.curr( 10, 2 ); 
  cuky       : abap.cuky; 
  @Semantics.quantity.unitOfMeasure : 'unit2' 
  quan10_2   : abap.quan(10,2);  
 
}
```
