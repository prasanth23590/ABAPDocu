---
title: "TYPES, CLIENT SPECIFIED"
source_file: abaptypes_client_specified.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, CLIENT SPECIFIED

## Syntax

``` abap
TYPES dtype TYPE cds_entity CLIENT SPECIFIED clnt.  
```

## Description

With the addition `CLIENT SPECIFIED` the statement `TYPES` defines a structured type constructed from all components of a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) `cds_entity` and an additional first component `clnt` with the type of a [client column](../../abap-glossary/abenclient_column_glosry.md).

`cds_entity` expects the name of a [CDS persistent entity](../../abap-glossary/abencds_sql_entity_glosry.md) [CDS entity](../../abap-glossary/abencds_entity_glosry.md), namely:

- [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md)

- [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md)

- The name of a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md)

- The name of a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md)

as defined in the corresponding [`DEFINE`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_ddl_syntax.md) statement of the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md).

Any name for the client column that follows the [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) can be specified for `clnt`.

## Hints

- The name specified for `clnt` is completely independent of the actual name of a client column in a data source of a CDS view.

- Abstract [CDS](../../abap-glossary/abencds_abstract_entity_glosry.md) entities cannot be specified.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Defining a structure with the components of type `DEMO_CDS_SCARR_ENTITY` and an additional column `MANDT`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES 
  demo_cds_scarr_entity_mandt TYPE demo_cds_scarr_entity 
                              CLIENT SPECIFIED mandt. 
 
out->write( 
   CAST cl_abap_structdescr( cl_abap_typedescr=>describe_by_name( 
     'DEMO_CDS_SCARR_ENTITY_MANDT' ) )->get_components( ) ). 
 
 
out->display( ).
```
