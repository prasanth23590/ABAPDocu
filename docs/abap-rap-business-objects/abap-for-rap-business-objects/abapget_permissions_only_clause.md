---
title: "GET PERMISSIONS, only_clause"
source_file: abapget_permissions_only_clause.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > GET PERMISSIONS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# GET PERMISSIONS, only_clause

## Syntax

``` abap
... ONLY { GLOBAL 
         | GLOBAL FEATURES 
         | GLOBAL AUTHORIZATION 
         | INSTANCE 
         | INSTANCE FEATURES 
         | INSTANCE AUTHORIZATION 
         | FEATURES 
         | AUTHORIZATION 
         | (dyn_spec) } ...  
```

## Description

The `only_clause` specifies which control characteristics (instance/global and features/authorization aspects) are to be included in the result of a `GET PERMISSIONS` statement.

**Variants**

The following table shows all the variants for only_clause.

**Note:** For consolidating and interpreting the permission results, see the topic [`GET PERMISSIONS`, Guidelines](abapget_permissions_rules.md).

| **Variant**                   | **Details**                                                                                                                                                          |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ONLY GLOBAL`                 | Includes only the global authorization, global and static feature control in the result. In the subsequent syntax, `FROM keys` is not allowed.                       |
| `ONLY GLOBAL FEATURES`        | Includes only global and static feature control in the result. In the subsequent syntax, `FROM keys` is not allowed.                                                 |
| `ONLY GLOBAL AUTHORIZATION`   | Includes only global authorization in the result. In the subsequent syntax, `FROM keys` is not allowed.                                                              |
| `ONLY INSTANCE`               | Includes only instance-based authorization and instance-based feature control in the result. Note that the result also includes static features.                     |
| `ONLY INSTANCE FEATURES`      | Includes only instance-based feature control in the result. Note that the result also includes static features.                                                      |
| `ONLY INSTANCE AUTHORIZATION` | Includes only instance-based authorization in the result.                                                                                                            |
| `ONLY FEATURES`               | Includes only global, static and instance-based feature control in the result.                                                                                       |
| `ONLY AUTHORIZATION`          | Includes only global and instance-based authorization in the result (but neither global nor instance-based feature control).                                         |
| `ONLY dyn_spec`               | Specifies any of above variants dynamically using an [enumeration value](../../abap-glossary/abenenumerated_value_glosry.md) of type `T_PERMISSIONS_ONLY` of interface `IF_ABAP_BEHV`. |

## Hints

- In the subsequent syntax, `FROM keys` must not be specified if any of the `ONLY GLOBAL ...` variants are used. For all other `ONLY` clauses, `FROM keys` is required.

- If no `only_clause` is specified, all aspects, that is, global- and instance-based feature control as well as global- and instance-based authorization, are included.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code sections taken from `CL_DEMO_RAP_EML_GET_PERM_ONLY` demonstrate the variants of the `only_clause`.

``` abap
DATA: request TYPE STRUCTURE FOR 
        PERMISSIONS REQUEST demo_managed_root_3. 
 
request = VALUE #( 
    %create                 = if_abap_behv=>mk-on 
    %update                 = if_abap_behv=>mk-on 
    %delete                 = if_abap_behv=>mk-on 
    %field-key_field        = if_abap_behv=>mk-on 
    %field-data_field1_root = if_abap_behv=>mk-on 
    %field-data_field2_root = if_abap_behv=>mk-on 
    %field-data_field3_root = if_abap_behv=>mk-on 
    %field-data_field4_root = if_abap_behv=>mk-on 
            ). 
 
GET PERMISSIONS ONLY GLOBAL ENTITY demo_managed_root_3 
     REQUEST request 
     RESULT FINAL(result1) 
     FAILED FINAL(failed1) 
     REPORTED FINAL(reported1). 
********************************************************************** 
GET PERMISSIONS ONLY GLOBAL FEATURES ENTITY demo_managed_root_3 
  REQUEST request 
  RESULT FINAL(result2) 
  FAILED FINAL(failed2) 
  REPORTED FINAL(reported2). 
********************************************************************** 
GET PERMISSIONS ONLY GLOBAL AUTHORIZATION 
      ENTITY demo_managed_root_3 
      REQUEST request 
      RESULT FINAL(result3) 
      FAILED FINAL(failed3) 
      REPORTED FINAL(reported3). 
********************************************************************** 
GET PERMISSIONS ONLY INSTANCE ENTITY demo_managed_root_3 
      FROM VALUE #( ( %key-key_field = 1 ) 
                    ( %key-key_field = 2 ) ) 
      REQUEST request 
      RESULT FINAL(result4) 
      FAILED FINAL(failed4) 
      REPORTED FINAL(reported4). 
********************************************************************** 
GET PERMISSIONS ONLY INSTANCE FEATURES ENTITY demo_managed_root_3 
  FROM VALUE #( ( %key-key_field = 1 ) 
                ( %key-key_field = 2 ) ) 
  REQUEST request 
  RESULT FINAL(result5) 
  FAILED FINAL(failed5) 
  REPORTED FINAL(reported5). 
********************************************************************** 
GET PERMISSIONS ONLY INSTANCE AUTHORIZATION 
  ENTITY demo_managed_root_3 
  FROM VALUE #( ( %key-key_field = 1 ) 
                ( %key-key_field = 2 ) ) 
  REQUEST request 
  RESULT FINAL(result6) 
  FAILED FINAL(failed6) 
  REPORTED FINAL(reported6). 
********************************************************************** 
GET PERMISSIONS ONLY FEATURES ENTITY demo_managed_root_3 
  FROM VALUE #( ( %key-key_field = 1 ) 
                ( %key-key_field = 2 ) ) 
  REQUEST request 
  RESULT FINAL(result7) 
  FAILED FINAL(failed7) 
  REPORTED FINAL(reported7). 
*********************************************************************** 
GET PERMISSIONS ONLY AUTHORIZATION ENTITY demo_managed_root_3 
      FROM VALUE #( ( %key-key_field = 1 ) 
                    ( %key-key_field = 2 ) ) 
      REQUEST request 
      RESULT FINAL(result8) 
      FAILED FINAL(failed8) 
      REPORTED FINAL(reported8). 
********************************************************************** 
GET PERMISSIONS ONLY (if_abap_behv=>permissions_only-authorization) 
     ENTITY demo_managed_root_3 
     FROM VALUE #( ( %key-key_field = 1 ) 
                   ( %key-key_field = 2 ) ) 
     REQUEST request 
     RESULT FINAL(result9) 
     FAILED FINAL(failed9) 
     REPORTED FINAL(reported9).
```

## Executable Example

- The example [ABAP EML - `GET PERMISSIONS`, `only_clause`](abenget_perm_only_abexa.md) demonstrates the different variants of the `only_clause` with a simple managed RAP BO.

- The example [ABAP EML - RAP Calculator (Unmanaged)](abeneml_calculator_abexa.md) demonstrates a `GET PERMISSIONS` statement using `only_clause` `ONLY INSTANCE FEATURES` with a simple unmanaged RAP BO. In this case, permissions are requested to determine a calculation based on entries provided is possible or not. For example, it is disallowed if a division by 0 were to be executed.
