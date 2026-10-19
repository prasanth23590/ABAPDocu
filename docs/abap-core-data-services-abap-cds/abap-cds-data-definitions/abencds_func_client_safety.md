---
title: "ABAP CDS - Client Safety of CDS Table Functions"
source_file: abencds_func_client_safety.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Table Functions > ABAP CDS - Client Handling in CDS Table Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Client Safety of CDS Table Functions

The annotation [`ClientHandling.clientSafe`](../abap-cds-annotations/abencds_1549616294_anno.md) makes a client-dependent CDS table function [client-safe](../../abap-glossary/abenclient_safe_glosry.md). If the value `true` (default) is used for that annotation, the following restrictions are checked that ensure client safety:

- All used objects must be client-safe.

- The table function must have the annotations [`ClientHandling.type`](../abap-cds-annotations/abencds_613831553_anno.md) with the value `#CLIENT_DEPENDENT` together with [`ClientHandling.algorithm`](../abap-cds-annotations/abencds_1114072352_anno.md) with the value `#SESSION_VARIABLE`.

  The [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md) that implements a client-dependent table function is then implicitly defined with the AMDP option [`CDS SESSION CLIENT DEPENDENT`](../../abap-programming-language/abap-database-access/abapmethods_amdp_options_client.md) or [`CLIENT INDEPENDENT`](../../abap-programming-language/abap-database-access/abapmethods_amdp_options_client.md) respectively.

- The table function must not have a parameter of type [`CLNT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The annotation [`Environment.systemField`](../abap-cds-annotations/abencds_1937921420_anno.md) with the enumerated value `#CLIENT` cannot be used for a parameter.

Table functions with the annotation [`ClientHandling.type`](../abap-cds-annotations/abencds_613831553_anno.md) with the value `#CLIENT_INDEPENDENT` are client-unsafe. This cannot be changed with the annotation [`ClientHandling.clientSafe`](../abap-cds-annotations/abencds_1549616294_anno.md).

## Hint

If the annotation [`ClientHandling.clientSafe`](../abap-cds-annotations/abencds_1549616294_anno.md) is not used but the table function has the ABAP language version [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md) or is a [released API](../../abap-glossary/abenreleased_api_glosry.md), the checks are done implicitly and client safety is enforced where necessary.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following `SELECT` statement accesses the CDS table function `DEMO_CDS_TABFUNC_SESS_VAR_CS` that is defined with the annotation [`ClientHandling.clientSafe`](../abap-cds-annotations/abencds_1549616294_anno.md). Without the addition `USING CLIENT` that cannot be used in [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md), only data of the current client can be selected.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
       FROM demo_cds_tabfunc_sess_var_cs "USING CLIENT @clnt 
       INTO TABLE @FINAL(result). 
 
out->write( result ). 
 
out->display( ).
```
