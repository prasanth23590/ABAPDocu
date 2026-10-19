---
title: "News for ABAP Release 7.94"
source_file: abennews-794.html
section: "ABAP Release News > News for ABAP Release 7.9x"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# News for ABAP Release 7.94

The kernel release for ABAP release 7.94 is 7.94.

## ABAP CDS

| Modification             | Description                                                                                                                                                                                                                                                        |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Extended Cast Matrix** | In [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) and in [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), [casting](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_cast_expression_v2.md) from the data type `CURR` into the data types `DECFLOAT16` and `DECFLOAT34` is now possible. |

## Data Clusters

| Modification                                  | Description |
|-----------------------------------------------|-------------|
| **Enhancement to `CL_ABAP_EXPIMP_UTILITIES`** | ...         |

## ABAP RESTful Application Programming Model

In release 7.94, the [ABAP RESTful Application Programming Model (RAP)](../../abap-glossary/abenarap_glosry.md) was enhanced as follows:

### RAP BDL

| Modification                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Abstract BDEF, `mandatory:execute` for Associations** | The optional addition [`mandatory:execute`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_association_abstract.md) is now available for associations in [abstract BDEFs](../../abap-glossary/abencds_abstract_bdef_glosry.md). It declares the association in question as mandatory, that is, whenever the abstract BDEF is used as an [input parameter](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_action_input_param.md) for a [RAP action](../../abap-glossary/abenrap_action_glosry.md) or a [RAP function](../../abap-glossary/abenrap_function_glosry.md), the [`%control`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapderived_types_control.md) flag must be set for this association. |
| **RAP Default Values Function**                         | A [RAP default values function](../../abap-glossary/abenrap_bo_defaulting_glosry.md) can be used to default values for fields or input parameters for RAP BO operations on the user interface. The syntax for defining a default values function is [`default function`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_default_function.md).                                                                                                                                                                                                                                        |

### ABAP EML

| Modification                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **RAP Handler Methods for RAP Default Values Functions** | [RAP default values functions](../../abap-glossary/abenrap_bo_defaulting_glosry.md) require an implementation in an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) in a specific way. See the topic [Handler Methods for RAP Default Values Functions](../../abap-rap-business-objects/abap-for-rap-business-objects/abaprap_handler_default_val_func.md).                                                                                                                                                 |
| **C1 Release of Class `CL_ABAP_BEHAVIOR_SAVER_FAILED`**  | The [RAP saver class](../../abap-glossary/abenabp_saver_class_glosry.md) [`CL_ABAP_BEHAVIOR_SAVER_FAILED`](../../abap-rap-business-objects/abap-for-rap-business-objects/abenabp_cl_abap_beh_saver_failed.md) has been released with the [C1 release contract](../../abap-glossary/abenc1_contract_glosry.md) for the ABAP language version [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md). See the blog post [*Using BAPIs in RAP*](https://blogs.sap.com/2022/11/30/using-bapis-in-rap/) for further details. |
| **Unit Tests and Contract Check Violations**             | [ABAP contract checks](../../abap-glossary/abencontract_checks_glosry.md) violations are made visible in [unit tests](../../abap-glossary/abenunit_test_glosry.md), i.e. the unit tests will fail if a contract check violation occurs.                                                                                                                                                                                                                               |
