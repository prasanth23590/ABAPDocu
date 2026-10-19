---
title: "CLASS-METHODS, FOR DDL OBJECT"
source_file: abapclass-methods_for_ddl_object.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS-METHODS, FOR DDL OBJECT

## Syntax

``` abap
CLASS-METHODS meth FOR DDL OBJECT 
                   [OPTIONS {CDS SESSION CLIENT DEPENDENT|REQUIRED} 
                          | {CLIENT INDEPENDENT}].  
```

### Addition

[`... OPTIONS {CDS SESSION CLIENT DEPENDENT|REQUIRED}|{CLIENT INDEPENDENT}`](abapclass-methods_for_ddl_object.md#addition)

## Overview

### Description

Methods defined with `FOR DDL OBJECT` are used to support [DDL objects](../../abap-glossary/abenddl_object_glosry.md) with [AMDP](../../abap-glossary/abenamdp_glosry.md). The following DDL objects can be used with AMDP:

- [Graph workspaces](../../abap-glossary/abengraph_workspace_glosry.md)

**Note:** [Database tables](../../abap-glossary/abendatabase_table_glosry.md) are not considered as DDL objects.

The methods have the following characteristics:

- Must be defined and implemented in an [AMDP class](../../abap-glossary/abenamdp_class_glosry.md).

- Must be [static](../../abap-glossary/abenstatic_method_glosry.md), i. e. only using `CLASS-METHODS` statements.

- Can be public, protected or private.

- Must not have any parameters and exceptions.

- Must not be defined in interfaces.

- Can be based on [DDIC](../../abap-glossary/abenddic_glosry.md) artifacts and are therefore be client-dependent. In this case, the addition using `OPTIONS ...` is required.

- Cannot be called as methods in ABAP.

- Cannot be [redefined](../../abap-glossary/abenredefinition_glosry.md).

The method implementation must be included for the respective DDL object following the syntax outlined in the topic [`METHOD, BY DATABASE ...`](abapmethod_by_db_proc.md).

## Addition

`... {CDS SESSION CLIENT DEPENDENT|REQUIRED}|{CLIENT INDEPENDENT}`

### Description

Defines the client handling of the DDL object and affects the client handling of an AMDP method that calls the method. A DDL object can be based on client-dependent or client-independent [DDIC](../../abap-glossary/abenddic_glosry.md) or [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) artifacts and can therefore be client-dependent or client-independent.

- If `OPTIONS CDS SESSION CLIENT` is used, the DDL object is client-dependent. The client handling is assumed to be done by implicit evaluation of the HANA session variable `CDS_CLIENT`. A calling AMDP method must set this session variable by using the AMDP option [`CDS SESSION CLIENT`](abapmethods_amdp_options_client.md) as follows:

  - If `OPTIONS CDS SESSION CLIENT DEPENDENT` is used here, a calling AMDP method must also use [`CDS SESSION CLIENT DEPENDENT`](abapmethods_amdp_options_client.md). The [`USING`](abapmethod_by_db_proc.md) list must contain [client-safe](../../abap-glossary/abenclient_safe_glosry.md) objects only.

  - If `OPTIONS CDS SESSION CLIENT REQUIRED` is used here, a calling AMDP method must use [`CDS SESSION CLIENT CURRENT|clnt`](abapmethods_amdp_options_client.md).

- If `OPTIONS CLIENT INDEPENDENT` is used, the DDL object is client-independent. A calling method can be client-dependent or client-independent.

### Hints

- Currently, the addition is required, when a [graph workspace](../../abap-glossary/abengraph_workspace_glosry.md) is defined using client-dependent CDS entities that are filtered by the HANA session variable `CDS_CLIENT`.

- The addition `DEPENDENT` makes a DDL object [client-safe](../../abap-glossary/abenclient_safe_glosry.md).

### Executable Example

The example [AMDP - Graph Processing](abenamdp_graph_cs_abexa.md) demonstrates graph processing using a graph workspace and a graph procedure. In this context, a graph workspace is declared using the `CLASS-METHODS` statement with the addition `FOR DDL OBJECT`.
