---
title: "CDS DDL - DEFINE TABLE FUNCTION"
source_file: abencds_f1_define_table_function.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Table Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE TABLE FUNCTION

## Syntax

``` abap
[@entity_annot1] 
[@entity_annot2] 
... 
[@function_annot1] 
[@function_annot2] 
... 
[DEFINE] TABLE FUNCTION table_function 
         [parameter_list] 
          element_list 
          IMPLEMENTED BY METHOD amdp_function [;]  
```

[`@entity_annot1`](abencds_f1_entity_annotations.md) · [`@entity_annot2`](abencds_f1_entity_annotations.md) · [`@function_annot1`](abencds_f1_function_annotations.md) · [`@function_annot2`](abencds_f1_function_annotations.md) · [`parameter_list`](abencds_f1_func_parameter_list.md) · [`element_list`](abencds_f1_return_list.md)

## Description

Defines a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) `table_function` as a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). In platform-dependent SQL, the CDS table function is implemented in an [AMDP method](../../abap-glossary/abenamdp_method_glosry.md) `amdp_function`, which is created using the [AMDP framework](../../abap-glossary/abenamdp_glosry.md) in the database system as an [AMDP table function](../../abap-glossary/abenamdp_table_function_glosry.md). The name `table_function` must comply with the naming conventions for [dictionary types](../../abap-dictionary-ddic/ddic-data-types/abenddic_data_types.md) and can have a maximum of 30 characters.

- [`@entity_annot`](abencds_f1_entity_annotations.md) and [`@function_annot`](abencds_f1_function_annotations.md) are used to specify optional [annotations](../../abap-glossary/abencds_annotation_glosry.md) for the CDS table function.

- [`parameter_list`](abencds_f1_func_parameter_list.md) is used to declare a list of optional input parameters for the CDS table function. These also define the input parameters of the AMDP table function.

- [`element_list`](abencds_f1_return_list.md) is used to declare the elements of the CDS table function. These also define the columns of the tabular return value of the AMDP table function.

- When `amdp_function` is used, an [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md) must be specified for an [AMDP table function](../../abap-glossary/abenamdp_table_function_glosry.md) in the form `amdp_class=>amdp_method`. Here `amdp_class` is an [AMDP class](../../abap-glossary/abenamdp_class_glosry.md) and `amdp_method` is an [AMDP function implementation](../../abap-programming-language/abap-database-access/abenamdp_function_methods.md) contained in this class. When this function implementation is declared, the current CDS table function is specified after the addition [`FOR TABLE FUNCTION`](../../abap-programming-language/abap-database-access/abapclass-methods_for_tabfunc.md). The AMDP function implementation must not exist when the CDS table function is created and activated. The name of an AMDP function implementation `amdp_function` can be specified in a single CDS table function only.

A CDS table function returns a tabular result set. Like any [CDS entity](../../abap-glossary/abencds_entity_glosry.md), it can be used as a data source in other CDS entities or ABAP SQL read [statements](../../abap-glossary/abenabap_sql_glosry.md). The prerequisite for use is that the specified AMDP function implementation exists and is active.

The name of a CDS table function is located in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

## Hints

- If a [CDS role](../../abap-glossary/abencds_role_glosry.md) is defined for a CDS entity using the CDS-DCL statement [`DEFINE ROLE`](../abap-cds-access-control/abencds_f1_define_role.md), implicit [access control](../../abap-glossary/abencds_access_control_glosry.md) applies by default when the CDS entity is accessed using ABAP SQL. CDS access control can be switched off using the value `#NOT_ALLOWED` for the annotation [`@AccessControl.authorizationCheck`](abencds_f1_function_annotations.md) and using the addition [`WITH PRIVILEGED ACCESS`](../../abap-programming-language/abap-database-access/abapselect_data_source.md) in the [`FROM`](../../abap-programming-language/abap-database-access/abapfrom_clause.md) clause of an ABAP SQL query.

- The [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) of a CDS table function does not need to have the same name as the CDS table function, but it is advisable to use the name of the CDS table function.

- After DDL source code is transported, the combination of its name and the name of the CDS table function view is defined and can no longer be modified by being renamed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following DDL source code shows a [client-dependent](abencds_func_client_handling.md) CDS table function that is not [client-safe](../../abap-glossary/abenclient_safe_glosry.md). It contains an input parameter with the annotation [`Environment.systemField`](../abap-cds-annotations/abencds_1937921420_anno.md) and the predefined value [`#CLIENT`](abencds_f1_parameter_annotations.md) for the client, which is implicitly supplied with the ID of the [current client](../../abap-glossary/abencurrent_client_glosry.md) when used as a [data source](../../abap-programming-language/abap-database-access/abapselect_data_source.md) of the ABAP SQL statement [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md).

The method `GET_SCARR_SPFLI_FOR_CDS` is an [AMDP function implementation](../../abap-programming-language/abap-database-access/abenamdp_function_methods.md) for the [CDS table function](../../abap-glossary/abencds_table_function_glosry.md) `DEMO_CDS_GET_SCARR_SPFLI_INP_CS`, which is also shown as an example of the DDL statement [`DEFINE TABLE FUNCTION`](abencds_f1_define_table_function.md)[CDS DDL - DEFINE TABLE FUNCTION](abencds_f1_define_table_function.md):

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@ClientHandling.type: #CLIENT_DEPENDENT
@ClientHandling.algorithm: #SESSION_VARIABLE
define table function DEMO_CDS_GET_SCARR_SPFLI_INPCS
  with parameters
     carrid :s_carr_id
  returns
  {   
    client   :s_mandt;
    carrname :s_carrname;
    connid   :s_conn_id;
    cityfrom :s_from_cit;
    cityto   :s_to_city;
  }
  implemented by method
    CL_DEMO_AMDP_FUNCTIONS_INP_CS=>GET_SCARR_SPFLI_FOR_CDS;
```

This method is declared using the addition [`FOR TABLE FUNCTION`](../../abap-programming-language/abap-database-access/abapclass-methods_for_tabfunc.md) and its interface is determined using the CDS table function.

``` abap
METHOD get_scarr_spfli_for_cds 
       BY DATABASE FUNCTION FOR HDB 
       LANGUAGE SQLSCRIPT 
       OPTIONS READ-ONLY 
       USING scarr spfli. 
  RETURN select sc.mandt as client, 
                sc.carrname, sp.connid, sp.cityfrom, sp.cityto 
                from scarr as sc 
                inner join spfli as sp on sc.mandt = sp.mandt and 
                                          sc.carrid = sp.carrid 
                where sp.carrid = :carrid 
                ORDER BY sc.mandt, sc.carrname, sp.connid; 
endmethod.
```
