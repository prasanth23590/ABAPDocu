---
title: "CDS DDL - INCLUDE ASPECT"
source_file: abencds_include_aspect.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Aspects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - INCLUDE ASPECT

## Syntax

``` abap
 
...INCLUDE aspect.element1[, 
   INCLUDE aspect.element2], 
   ... 
| {INCLUDE aspect.*[excluding 
     element1, 
     element2, 
     ...]}  
```

[`aspect`](abencds_ddl_aspect_glosry.md) · [`element1`](abencds_aspect_element.md) · [`aspect`](abencds_ddl_aspect_glosry.md) · [`element2`](abencds_aspect_element.md) · [`aspect`](abencds_ddl_aspect_glosry.md) · [`element1`](abencds_aspect_element.md) · [`element2`](abencds_aspect_element.md)

## Description

Includes 1 to n elements of a CDS aspect in the data definition of a [CDS view entity](abencds_v2_views.md) or a [CDS projection view](abencds_proj_views.md). The syntax for including elements of an aspect is the aspect and element names, separated by a `.`, such as `include.element`. The same element of an aspect can be included multiple times as long as the alias name of the element is unique.

To include all elements of an aspect, the syntax `include.*` is used. If `include.*` is used, an ` excluding { ... }` clause can be added to exclude certain elements of the CDS aspect.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example showcases how a CDS aspect is bound to a CDS view entity, as well as how some or all of these bound fields can be included in the entity.

``` abap
@AbapCatalog.viewEnhancementCategory: [#NONE]
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Selecting all DDIC Types'
@Metadata.ignorePropagatedAnnotations: true
@ObjectModel.usageType:{
  serviceQuality: #X,
  sizeCategory: #S,
  dataClass: #MIXED
}
define view entity DEMO_CDS_VE_ASPECT_USE
  as select from demo_ddic_types
  bind aspect DEMO_CDS_ASPECT_ALL_TYPES (
              id         => $projection.IdVE,
              int1       => $projection.Int1VE,
              int2       => $projection.Int2VE,
              int4       => $projection.Int4VE,
              int8       => $projection.Int8VE,
              dec10_2    => $projection.Dec102,
              d16n       => $projection.D16nVE,
              d34n       => $projection.D34nVE,
              fltp       => $projection.FltpVE,
              char10     => $projection.Char10VE,
              sstring512 => $projection.Sstring512VE,
              string     => $projection.StringVE,
              raw10      => $projection.Raw10VE,
              dats       => $projection.DatsVE,
              tims       => $projection.TimsVE,
              datn       => $projection.DatnVE,
              timn       => $projection.TimnVE,
              utcl       => $projection.UtclVE,
              numc1      => $projection.Numc1VE,
              numc10     => $projection.Numc10VE,
              clnt       => $projection.ClntVE,
              lang       => $projection.LangVE,
              unit2      => $projection.Unit2VE,
              geom_ewkb  => $projection.GeomEwkbVE,
              lchr_int   => $projection.LchrIntVE,
              curr10_2   => $projection.Curr102,
              cuky       => $projection.CukyVE,
              quan10_2   => $projection.Quan102
              )
{

  key id         as IdVE,
      include DEMO_CDS_ASPECT_ALL_TYPES.d34n,
      include DEMO_CDS_ASPECT_ALL_TYPES.utcl,
      include DEMO_CDS_ASPECT_ALL_TYPES.unit2,
      include DEMO_CDS_ASPECT_ALL_TYPES.cuky,

      int1       as Int1VE,
      int2       as Int2VE,
      int8       as Int8VE,
      d16n       as D16nVE,
      d34n       as D34nVE,
      fltp       as FltpVE,
      char10     as Char10VE,
      sstring512 as Sstring512VE,
      string     as StringVE,
      raw10      as Raw10VE,
      rawstring  as RawstringVE,
      dats       as DatsVE,
      tims       as TimsVE,
      datn       as DatnVE,
      timn       as TimnVE,
      utcl       as UtclVE,
      numc1      as Numc1VE,
      numc10     as Numc10VE,
      clnt       as ClntVE,
      lang       as LangVE,
      unit2      as Unit2VE,
      geom_ewkb  as GeomEwkbVE,
      lchr_int   as LchrIntVE,
      @Semantics.quantity.unitOfMeasure: 'unit2'
      quan10_2   as Quan102,


      dec10      as Dec10,
      dec10_2    as Dec102,
      dec20      as Dec20,
      dec20_4    as Dec204,
      df16_raw   as Df16Raw,
      char1      as Char1,
      sstring256 as Sstring256,
      raw1       as Raw1,
      unit3      as Unit3,

      @Semantics.amount.currencyCode: 'cuky'
      curr10_2   as Curr102,
      @Semantics.amount.currencyCode: 'cuky'
      curr10_4   as Curr104,
      @Semantics.amount.currencyCode: 'cuky'
      curr20_2   as Curr202,
      @Semantics.amount.currencyCode: 'cuky'
      curr20_4   as Curr204,
      cuky       as CukyVE,
      @Semantics.quantity.unitOfMeasure: 'unit2'
      quan10     as Quan10,

      @Semantics.quantity.unitOfMeasure: 'unit2'
      quan10_4   as Quan104,
      @Semantics.quantity.unitOfMeasure: 'unit2'
      quan20     as Quan20,
      @Semantics.quantity.unitOfMeasure: 'unit2'
      quan20_2   as Quan202,
      @Semantics.quantity.unitOfMeasure: 'unit2'
      quan20_4   as Quan204,


      accp       as Accp,
      df16_dec   as Df16Dec,
      df34_dec   as Df34Dec,
      df34_raw   as Df34Raw,
      int4       as Int4VE

}
```
