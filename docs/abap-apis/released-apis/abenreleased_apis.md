---
title: "Released APIs of the Current System"
source_file: abenreleased_apis.html
section: "ABAP APIs > Released APIs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Released APIs of the Current System

The following tables show all transportable [repository objects](../../abap-glossary/abenrepository_object_glosry.md) of the current system that are [released APIs](../../abap-glossary/abenreleased_api_glosry.md) and can be used in [restricted ABAP language versions](../../abap-glossary/abenrestricted_version_glosry.md).

- The first three columns show the repository objects or parts of repository objects.

- Column `Release Contract` shows the [release contract](../../abap-glossary/abenrelease_contract_glosry.md) that is used for releasing the API.

- The two subsequent columns show, whether the API is released for restricted ABAP language version [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md), [ABAP for Key Users](../../abap-glossary/abenabap_for_key_users_glosry.md) or for both.

- Column `State` shows the release state that can be *Released* or *Deprecated*.

- In case of deprecation, the successor object is shown in column `Successor` if available.

Any repository object that can be used in a restricted ABAP language versions must be classified with an appropriate release contract ([C1 contract](../../abap-glossary/abenc1_contract_glosry.md) in general). But not all repository objects with a release contract can be used in a restricted language version.

## Hints

- For more information about released APIs, refer also to the [SAP Business Accelerator Hub](https://api.sap.com/) and [SAP S/4HANA Cloud - Released objects for ATC Check](https://github.com/SAP/abap-atc-cr-cv-s4hc).

- [AUTH: Authorization Check Fields](abenreleased_apis.md#auth-authorization-check-fields)

- [BDEF: Behavior Definition](abenreleased_apis.md#bdef-behavior-definition)

- [CHAR: Object characteristic](abenreleased_apis.md#char-object-characteristic)

- [CHKC: Check category](abenreleased_apis.md#chkc-check-category)

- [CHKO: Check](abenreleased_apis.md#chko-check)

- [CHKV: Check Variant](abenreleased_apis.md#chkv-check-variant)

- [CLAS: Class (ABAP Objects)](abenreleased_apis.md#clas-class-abap-objects)

- [DDLS: Data Definition Language Source](abenreleased_apis.md#ddls-data-definition-language-source)

- [DOMA: Domain](abenreleased_apis.md#doma-domain)

- [DRTY: DS Type Definitions](abenreleased_apis.md#drty-cds-type-definitions)

- [DSFD: CDS Scalar Function Definition](abenreleased_apis.md#dsfd-cds-scalar-function-definition)

- [DSFI: DS Scalar Function Implementation Reference](abenreleased_apis.md#dsfi-cds-scalar-function-implementation-reference)

- [DTEL: Data Element](abenreleased_apis.md#dtel-data-element)

- [ENHS: Enhancement Spot](abenreleased_apis.md#enhs-enhancement-spot)

- [EVTB: RAP Event Binding](abenreleased_apis.md#evtb-rap-event-binding)

- [FDT0: FDT/BRFplus: System Application](abenreleased_apis.md#fdt0-fdtbrfplus-system-application)

- [FUGR: Function Group](abenreleased_apis.md#fugr-function-group)

- [G4BA: SAP Gateway OData V4 Backend Service Group & Assignments](abenreleased_apis.md#g4ba-sap-gateway-odata-v4-backend-service-group-and-assignments)

- [INTF: Interface (ABAP Objects)](abenreleased_apis.md#intf-interface-abap-objects)

- [IWSV: SAP Gateway Business Suite Enablement - Service](abenreleased_apis.md#iwsv-sap-gateway-business-suite-enablement-service)

- [MSAG: Message Class](abenreleased_apis.md#msag-message-class)

- [NONT: RESTful ABAP Programming Model: Object Node Type](abenreleased_apis.md#nont-restful-abap-programming-model-object-node-type)

- [RONT: RESTful ABAP Programming Model: Object (Node) Type](abenreleased_apis.md#ront-restful-abap-programming-model-object-node-type)

- [SUSO: Authorization Object](abenreleased_apis.md#suso-authorization-object)

- [TABL: Table](abenreleased_apis.md#tabl-table)

- [TTYP: Table Type](abenreleased_apis.md#ttyp-table-type)

- [TYPE: Type Group](abenreleased_apis.md#type-type-group)

- [VIEW: View](abenreleased_apis.md#view-view)

- [WAPA: BSP (Business Server Pages) Application](abenreleased_apis.md#wapa-bsp-business-server-pages-application)

- [WDCA: Web Dynpro Application Configuration](abenreleased_apis.md#wdca-web-dynpro-application-configuration)

- [WDYA: Web Dynpro Application](abenreleased_apis.md#wdya-web-dynpro-application)

- [XSLT: Transformation](abenreleased_apis.md#xslt-transformation)

## AUTH - Authorization Check Fields

| **Object** | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| ACTVT      | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| SCBO2_ILM  | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| TABLE      | \-                 | \-            | C1                   | X                              |                        | Released  |               |

## BDEF - Behavior Definition

| **Object**          | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|---------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| ABP_BEHV_PAR_SHARE  | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| C_BUSINESSUSEREVENT | \-                 | \-            | C0                   | X                              |                        | Released  |               |
| I_BUSINESSUSEREVENT | \-                 | \-            | C0                   | X                              |                        | Released  |               |
| I_BUSINESSUSEREVENT | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| I_CPWF_INST         | \-                 | \-            | C1                   | X                              |                        | Released  |               |

## CHAR - Object characteristic

| **Object**        | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|-------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| TRANSLATION_DEPTH | \-                 | \-            | C1                   | X                              |                        | Released  |               |

## CHKC - Check category

| **Object**                   | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|------------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| API_RELEASE                  | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| ATC_CHK_CAT_CDS_PERFORMANCE  | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| ATC_IDOC_CONS_CAT            | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_BUSINESS_SERVICES         | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_CDS                       | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_CDS_GENERAL               | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_CDS_SECOBJ                | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_CDS_SYNTAX                | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_CONVENTION                | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_DICTIONARY                | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_DYNAMIC                   | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_ESH                       | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_ESH_GENERAL               | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_FLP_UI                    | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_ILM                       | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_PERFORMANCE               | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_RAP                       | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_ROBUSTNESS                | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_SEARCH                    | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_SECURITY                  | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_SYNTAX                    | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_USER_INTERFACE            | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SADL_RUNTIME                 | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SOFTWARE_COMPONENT_RELATIONS | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SYCM_3TIER                   | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SYCM_CLOUD_READINESS         | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SYCM_S4H_READINESS           | \-                 | \-            | C1                   | X                              |                        | Released  |               |

## CHKO - Check

| **Object**                     | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|--------------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| ABAP_CLOUD_PRECHECK_CHANGES    | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| ABAP_UNIT                      | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| API_CATALOG_USAGE              | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| API_COMPATIBILITY              | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| API_CONSISTENCY                | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| API_USAGE                      | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| ATC_CHECK_BC_CDS_PF1           | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| ATC_IDOC_CONS                  | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| BDEF_IMPL_CHECK                | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| BSP_SEC                        | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CDS_ACCESS_CONDITIONS          | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CDS_ANNOTATIONS                | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CDS_COMPLEXITY                 | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CDS_DDLX_SYNTAX_CHECK          | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CDS_REFERENCED_OBJECTS         | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_ABAP_DOC_COMMENT            | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_AMDP_HDB_MIGRATION          | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_ANALYZE_SELECT_HANA         | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_ANALYZE_WHERE               | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_ANALYZE_WHERE_IMUD          | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_APPEND_TO_SORTED            | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_CDS_JOIN_ANALYSIS           | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_CRITICAL_STATEMENTS         | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_DB_OPS_IN_LOOPS             | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_DCLS_DDLS                   | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_DCLS_IRB                    | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_DDIC_TABLES                 | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_FIND_BADI_CALL              | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_FIND_DYN_SQL                | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_FOR_ALL_ENTRIES             | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_FOR_ALL_ENTRIES_HANA        | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_ILM_OBJECT                  | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_IMUD_NESTED                 | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_IMUD_TAW_SEC01              | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_INVALIDATE_BUFFER           | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_ITAB_PERFORMANCE            | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_METRIC_PROC                 | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_MOVE_PERFORMANCE            | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_NAMING_NEW                  | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_NO_ORDER_BY                 | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_OO_SIZE                     | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_SEARCH_ABAP_PATTERN         | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_SEARCH_CUST_MODIFICATIONS   | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_SEARCH_DB_OPS               | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_SEARCH_DB_OPS_IN_PC         | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_SEARCH_STMT_PATTERN         | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_SELECT_EXIT                 | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_SELECT_TAW_BYBUF            | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_SELECT_TAW_SEC01            | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_SELECT_THEN_CHECK           | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_SELECT_WITH_DELETE          | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_SEQ_ACC_ITAB_NESTED         | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_SORT_IN_LOOP                | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_SQL1_CONSISTENCY            | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_SYSUBRC                     | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_UI5_BASE_APP_VERS           | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_UI5_COMP                    | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_UI5_REL_CHECK               | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CI_VALUE_PARAMETER             | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| DD_CI_DDIC_CONSISTENCY_AC      | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| DD_CI_DDIC_CONSISTENCY_PA      | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| ESH_ATC_CDS_VIEW_ENTITY_CHECK  | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| ESH_ATC_CHECK_EZ_ANNOS         | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| ODATA_CONSISTENCY              | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| ODATA_CONSIST_EVTB             | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SADL_RUNTIME                   | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SADL_TEXT_SEARCH               | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SCR_CONSISTENCY                | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SLIN_MAIN                      | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SLIN_SEC                       | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SLIN_VERS                      | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SUI_UIPG                       | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SUI_UIST                       | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SYCM_ALLOWED_ENH_TECHNOLOGY    | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SYCM_CHECK_ABAP_LANGU_VERSION  | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SYCM_CLOUD_ALLOWED_OBJCT_TYPES | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SYCM_CLOUD_RELEASED_OBJECTS    | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SYCM_RELEASED_CLOUDIFIC_REPOS  | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SYCM_S4H_CDS_PRIV_ACC          | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SYCM_S4H_DD_ENHANCEMENTS       | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SYCM_S4H_DD_VIEW_BASE          | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SYCM_S4H_FIELD_EXT             | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SYCM_S4H_SAP_QUERY             | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SYCM_S4H_SEARCH_DB_OPS         | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SYCM_S4H_TRAN_LITERALS         | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SYCM_S4H_WHERE_USED            | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SYCM_USAGE_OF_APIS             | \-                 | \-            | C1                   | X                              |                        | Released  |               |

## CHKV - Check Variant

| **Object**                     | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State**  | **Successor**                       |
|--------------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|------------|-------------------------------------|
| ABAP_CLEAN_CORE_DEVELOPMENT    | \-                 | \-            | C1                   | X                              |                        | Released   |                                     |
| ABAP_CLEAN_CORE_READINESS      | \-                 | \-            | C1                   | X                              |                        | Released   |                                     |
| ABAP_CLOUD_DEVELOPMENT_3TIER   | \-                 | \-            | C1                   | X                              |                        | Deprecated | CHKV ABAP_CLEAN_CORE_DEVELOPMENT    |
| ABAP_CLOUD_DEVELOPMENT_DEFAULT | \-                 | \-            | C1                   | X                              |                        | Released   |                                     |
| ABAP_CLOUD_DEVELOPMENT_PARTNER | \-                 | \-            | C1                   | X                              |                        | Released   |                                     |
| ABAP_CLOUD_READINESS           | \-                 | \-            | C1                   | X                              |                        | Released   |                                     |
| FUNCTIONAL_DB                  | \-                 | \-            | C1                   | X                              |                        | Released   |                                     |
| SAP_CLOUD_PLATFORM_ATC_DEFAULT | \-                 | \-            | C1                   | X                              |                        | Deprecated | CHKV ABAP_CLOUD_DEVELOPMENT_DEFAULT |
| SAP_CP_READINESS               | \-                 | \-            | C1                   | X                              |                        | Deprecated | CHKV ABAP_CLOUD_READINESS           |
| SLIN_SEC                       | \-                 | \-            | C1                   | X                              |                        | Released   |                                     |

## CLAS - Class (ABAP Objects)

| **Object**                     | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State**  | **Successor**                 |
|--------------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|------------|-------------------------------|
| /IWBEP/CL_CP_FACTORY_REMOTE    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| /IWBEP/CL_CP_FACTORY_UNIT_TST  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| /IWBEP/CL_V4_ABS_PM_MODEL_PROV | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| /IWBEP/CX_CP_REMOTE            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| /IWBEP/CX_GATEWAY              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| /IWXBE/CL_ABS_CONSUMER_EVENT   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| /IWXBE/CL_GENERIC_CONS_DESCRIP | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| /IWXBE/CX_EXCEPTION            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| /UI2/CL_JSON                   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| AIC_CHOICES                    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| AIC_FINISH_REASON              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| AIC_FUNCTION_CALL              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| AIC_ISLM_INSTANTIATION_ERROR   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| AIC_ISLM_PRIVILEGED_MODE       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| AIC_ISLM_PROMPT_TEMPLATE_ID    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| AIC_ISLM_SCENARIO_ID           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| AIC_MEDIA_TYPE                 | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| AIC_PROMPT_MESSAGE_TYPE        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_API_STATE              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_BEHAVIOR_EVENT_HANDLER | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_BEHAVIOR_HANDLER       | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_BEHAVIOR_SAVER         | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_BEHAVIOR_SAVER_FAILED  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_BEHV                   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_BEHV_AUX               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_BEHV_IMPLEMENTATN_MSG  | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CL_ABAP_BEHV_TEST_ENVIRONMENT  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_BIGINT                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_CHAR_UTILITIES         | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_CLASSDESCR             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_CODEPAGE               | \-                 | \-            | C1                   |                                | X                      | Deprecated | CLAS CL_ABAP_CONV_CODEPAGE    |
| CL_ABAP_COMPLEXDESCR           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_CONTAINER_UTILITIES    | \-                 | \-            | C1                   |                                | X                      | Deprecated |                               |
| CL_ABAP_CONTEXT_INFO           | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_CONV_CODEPAGE          | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_CONV_IN_CE             | \-                 | \-            | C1                   |                                | X                      | Deprecated | CLAS CL_ABAP_CONV_CODEPAGE    |
| CL_ABAP_CONV_OUT_CE            | \-                 | \-            | C1                   |                                | X                      | Deprecated | CLAS CL_ABAP_CONV_CODEPAGE    |
| CL_ABAP_CONV_X2X_CE            | \-                 | \-            | C1                   |                                | X                      | Deprecated | CLAS CL_ABAP_CONV_CODEPAGE    |
| CL_ABAP_CORRESPONDING          | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_C_READER               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_C_WRITER               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_DATADESCR              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_DATFM                  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_DB_C_LOCATOR           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_DB_C_READER            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_DB_C_WRITER            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_DB_X_LOCATOR           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_DB_X_READER            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_DB_X_WRITER            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_DECFLOAT               | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_DIFF                   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_DYN_PRG                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_ELEMDESCR              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_ENUMDESCR              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_EXCEPTIONAL_VALUES     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_FORMAT                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_GARBAGE_COLLECTOR      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_GZIP                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_GZIP_BINARY_STREAM     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_GZIP_TEXT_STREAM       | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_HMAC                   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_INTFDESCR              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_ITAB_C_READER          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_ITAB_C_WRITER          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_ITAB_X_READER          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_ITAB_X_WRITER          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_LOCK_OBJECT_FACTORY    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_MATCHER                | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_MATH                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_MEMORY_C_READER        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_MEMORY_C_WRITER        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_MEMORY_X_READER        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_MEMORY_X_WRITER        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_MESSAGE_DIGEST         | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_OBJECTDESCR            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_PARALLEL               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_PROB_DISTRIBUTION      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_PROB_DISTRIBUTION_DF34 | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_DECFLOAT16      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_DECFLOAT34      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_FLOAT           | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_INT             | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_INT8            | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_PACKED          | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_PACKED_DEC1     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_PACKED_DEC10    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_PACKED_DEC11    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_PACKED_DEC12    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_PACKED_DEC13    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_PACKED_DEC14    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_PACKED_DEC2     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_PACKED_DEC3     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_PACKED_DEC4     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_PACKED_DEC5     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_PACKED_DEC6     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_PACKED_DEC7     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_PACKED_DEC8     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANDOM_PACKED_DEC9     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RANGE                  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_RATIONAL               | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_REFDESCR               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_REGEX                  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_RUNTIME                | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CL_ABAP_SQL_CHANGING_STMNT     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_SQL_CONNECTION_BUILDER | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_SQL_CONNECTION_DECO    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_SQL_CONNECTION_HANDLE  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_SQL_SELECT_STATEMENT   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_SQL_STATEMENT_HANDLE   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_STRING_C_READER        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_STRING_C_WRITER        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_STRING_UTILITIES       | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_STRING_X_READER        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_STRING_X_WRITER        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_STRUCTDESCR            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_STRUCT_UTILITIES       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_TABLEDESCR             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_TESTDOUBLE             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_TIMEFM                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_TIMESTAMP_UTIL         | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CL_ABAP_TSTMP                  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_TX                     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_TYPEDESCR              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_UNGZIP_BINARY_STREAM   | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_UNGZIP_TEXT_STREAM     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_UNIT_ASSERT            | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_UTCLONG                | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ABAP_VIEW_OFFLEN            | \-                 | \-            | C1                   |                                | X                      | Deprecated | CLAS CL_ABAP_CONV_CODEPAGE    |
| CL_ABAP_WEAK_OBJECT_REFERENCE  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_X_WRITER               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ABAP_ZIP                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_ACO_KRN_SERVICES            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ADDRESS_FORMAT              | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_AIA_PROGRESS_SERVICE        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_AIA_RESULT_FACTORY          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_AIA_SD_CONTEXT              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_AIC_ISLM_COMPL_API_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_AIC_ISLM_ORCH_API_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_AIC_ISLM_PROMPT_TPL_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_AMDP_TEST_ENVIRONMENT       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_APJ_DT_CREATE_CONTENT       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_APJ_JT_CHECK_BASE           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_APJ_JT_CHECK_BASE_20        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_APJ_RT_API                  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_APJ_SCP_TOOLS               | \-                 | \-            | C1                   | X                              |                        | Deprecated |                               |
| CL_ARCH_DELETE_API             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ARCH_READ_API               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ARCH_RELOAD_API             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ARCH_WRITE_API              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ATO_PREFIX_DETERMINATION    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_AUNIT_ASSERT                | \-                 | \-            | C1                   | X                              |                        | Deprecated | CLAS CL_ABAP_UNIT_ASSERT      |
| CL_AUNIT_AUTHORITY_CHECK       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_AUNIT_AUTH_CHECK_TYPES_DEF  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_AUNIT_CONSTRAINTS           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_AUTH_CHECK_FOR_BU           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_AUTH_FACTORY                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BADI_BASE                   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BALI_EXCEPTION_SETTER       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BALI_FREE_TEXT_SETTER       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BALI_HEADER_SETTER          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BALI_ITEM_FILTER            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BALI_LOG                    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BALI_LOG_DB                 | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BALI_LOG_FILTER             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BALI_MESSAGE_SETTER         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BALI_OBJECT_HANDLER         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BAL_LOGGING                 | \-                 | \-            | C1                   | X                              |                        | Deprecated |                               |
| CL_BCFG_CD_REUSE_API_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BCFG_CD_REUSE_API_INJECTOR  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BCS_MAIL_BINARYPART         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BCS_MAIL_BODYPART           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BCS_MAIL_MESSAGE            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BCS_MAIL_SYSTEM_CONFIG      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BCS_MAIL_TEXTPART           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BGMC_PROCESS_FACTORY        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BGMC_TEST_ENVIRONMENT       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BLE_API_MT_TENANT           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BLE_BADI_RUNTIME            | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CL_BLE_TRACE_WRITER            | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CL_BOTD_MOCKEMLAPI_BLDRFACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BOTD_MOCKEMLAPI_BO_TEST_ENV | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_BOTD_TXBUFDBL_BO_TEST_ENV   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CBE_BDEF_RUNTIME            | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_CBO2_KU_RUNTIME             | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CL_CBO_DEVELOPER_ACCESS        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CDS_ENTITY_INSPECTOR        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CDS_TEST_DATA               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CDS_TEST_DATA_FOR_CURR_CONV | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CDS_TEST_DATA_FOR_UNIT_CONV | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CDS_TEST_ENVIRONMENT        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CHANGEDOCU_ARCHIVE          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CHDO_DELETE_TOOLS           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CHDO_OBJECT_TOOLS_REL       | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_CHDO_READ_TOOLS             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CHDO_WRITE_TOOLS            | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_CI_ATC_ASSISTANT_FACTORY    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CI_ATC_DATA_PROVIDER        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CI_ATC_FINDING_DETAILS      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CI_ATC_QUICKFIXES           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CI_ATC_QUICKFIX_CONTEXT     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CI_ATC_UNIT_DRIVER          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CMIS_CLIENT_FACTORY         | \-                 | \-            | C1                   | X                              |                        | Deprecated | CLAS CL_CMIS_CLIENT_FACTORY2  |
| CL_CMIS_CLIENT_FACTORY2        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CMIS_CONSTANTS              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CMIS_OBJECT_FACTORY         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CMIS_PROPERTY_IDS           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_COMMUNICATION_TARGET_LV5    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_COMMUNICATION_TARGET_RFCLV5 | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_COMMUNICATION_TARGET_ROOT   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_COMM_TARGET_HTTP_LV5        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CONVERSION_EXT_INT          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CSV_ENCODING                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CSV_FACTORY                 | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CSV_FACTORY_INJECTOR        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CSV_FIELD_FORMAT            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CSV_INVALID_VALUE_HANDLING  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CSV_LINE_TERMINATOR         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_CSV_QUOTE                   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_DEMO_CLASSRUN               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_DEMO_OUTPUT_CLOUD           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_FDT_BRS_PROCESSOR           | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_FDT_CP_AST_FACTORY          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_FDT_CP_AST_HELPER           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_FDT_CP_AST_SIMPLE_NODE      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_FDT_CP_FACTORY              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_FDT_CP_UTILITY_API          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_FDT_FUNCTION_PROCESS_API    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_FDT_OBJ_SYSTEM_VARIABLES    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_FHC_CALENDAR_ID_MAPPER      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_FHC_CALENDAR_RUNTIME        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_FP_ADS_UTIL                 | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_FP_FDP_MIGRATION            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_FP_FDP_SERVICES             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_FP_FORM_READER              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_FTD_ARGUMENT_MATCHER        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_FUNCTION_TEST_ENVIRONMENT   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_GSM_API_TEST                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_HDLFS_ACCESS_POLICY_BLDR    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_HDLFS_DOWNLOAD              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_HDLFS_ERROR_RESPONSE        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_HDLFS_FILEMANAGER           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_HDLFS_HTTP_CLIENT           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_HDLFS_HTTP_CLIENT_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_HDLFS_IMPERSONATING_CLIENT  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_HDLFS_UPLOAD                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_HDLFS_USER_INFO             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_HTMLTIDY                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_HTTP_SERVICE_UTILITY        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_ICU_TRANSFORMATION          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_IRM_RT_DESTRUCTION_OBJECT   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_IRM_RT_EXEC                 | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_IXML_CORE                   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_IXML_XPATH                  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_JSON_STRING_READER          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_JSON_STRING_WRITER          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_JSON_XSTRING_READER         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_JSON_XSTRING_WRITER         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_MAIL_ADDRESS                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_MESSAGE_HELPER              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_NUMBERRANGE_BUFFER          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_NUMBERRANGE_INTERVALS       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_NUMBERRANGE_OBJECTS         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_NUMBERRANGE_RUNTIME         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_NUMBER_RANGE_INTERVALS      | \-                 | \-            | C1                   | X                              |                        | Deprecated | CLAS CL_NUMBERRANGE_INTERVALS |
| CL_NUMBER_RANGE_OBJECTS        | \-                 | \-            | C1                   | X                              |                        | Deprecated | CLAS CL_NUMBERRANGE_OBJECTS   |
| CL_NUMBER_RANGE_RUNTIME        | \-                 | \-            | C1                   | X                              |                        | Deprecated | CLAS CL_NUMBERRANGE_RUNTIME   |
| CL_OSQL_TEST_DATA              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_OSQL_TEST_ENVIRONMENT       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_PCF_FIELD_VALIDATION        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_PCF_GENERIC_TEXT_PROVIDER   | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_PCF_READ_API_FACTORY        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_PCF_SRVC_ODATA_MODEL_FCTY   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_PRINT_QUEUE_UTILS           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_PROXY_CLIENT                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_RAP_EVENT_TEST_ENVIRONMENT  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_RSPO_PDF_MERGER             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SAL_WRITE_EVENT_C1          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SATC_API                    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SATC_API_CHECK_VARIANT      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SCAL_API                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |                               |
| CL_SCAL_UTILS                  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_SCPR_CD_BCSET_ACTIVATION    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SCPR_CD_BCSET_ACTIV_OPTIONS | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SD_ACTION_PARAMETER_UI_INFO | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SD_ACTION_PROVIDER          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SD_SIDEEFFECT_PROVIDER      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SD_STUBS_FACTORY            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SD_UI_INFO_FACTORY          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SD_VALUE_HELP_PROVIDER      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SHDB_HC                     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SLDAG_BUSINESS_SYSTEM       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SMTG_EMAIL_TEMPL_RENDERER   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SSI_RP_SESSION_MEMORY       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SWF_CPWF_API_FACTORY_A4C    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_SWF_CPWF_API_FACTORY_PCE    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SXML_STRING_READER          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SXML_STRING_WRITER          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SXML_TABLE_READER           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SXML_TABLE_WRITER           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_SYSTEM_UUID                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_UOM_CONTENT_HANDLER         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_UOM_CONVERSION              | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_UOM_DIM_MAINTENANCE         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_UOM_MAINTENANCE             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_UUID_FACTORY                | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_WEB_HTTP_CLIENT_MANAGER     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_WEB_HTTP_CLIENT_PROVIDER    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_WEB_HTTP_SERVER_UTILITY     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_WEB_HTTP_UTILITY            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_WS_PROTOCOL_FACTORY         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ABAP_T_BI_FIXED_LENGTH  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ABAP_T_BI_P             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ABAP_T_BI_VRBLE_LENGTH  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ABAP_T_BUILT_IN         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ABAP_T_BUILT_IN_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ABAP_T_GENERIC_DATA     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ABAP_T_GENERIC_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ABAP_T_G_DATA           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ABAP_T_G_OBJECT         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ABAP_T_R_BUILT_IN       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ABAP_T_R_GENERIC        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ABAP_T_SOURCE           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ABAP_T_SOURCE_F         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AD_BUILT_IN_TYPE        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AD_BUILT_IN_TYPE_F      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AD_OBJECT_READ_STATE    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AD_OBJECT_STATE         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AD_OBJECT_STATE_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AMDP_DB_LANGUAGE        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AMDP_DB_OPTION          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AMDP_DB_TYPE            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AO_CLASS_CATEGORY       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AO_ORIGIN               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AO_O_LOCAL              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AO_O_REMOTE             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AO_PARAMETER_KIND       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AO_PARAMETER_KIND_F     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AO_TYPING_METHOD        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AO_VERSION              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AO_VISIBILITY           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AO_VISIBILITY_F         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_APLO_OBJ_TEXT           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_APLO_OBJ_TEXT_ATTRIBUTE | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_APLO_SUBOBJ_TEXT        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_APLO_SUBOBJ_TEXT_ATTRBT | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ARS_API_STATE           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ARS_RELEASE_CONTRACT    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ARS_RELEASE_STATE       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ARS_VISIBILITY          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AR_SELECTION_BUILDER    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ASQL_CONSTRAINT         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ASQL_CONSTRAINT_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AU_DURATION             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_AU_RISK_LEVEL           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BAL_LEVEL_OF_DETAIL     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BAL_LOG_SELECTION_BLDR  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BCO_TEXT                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BCO_TEXT_ATTRIBUTE      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BCS_ORIGIN              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BCS_O_LOCAL             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BDEF_CHDO_LOGGNG_OPTION | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BDEF_CHDO_LOG_OPTION_F  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BDEF_EVALUATION_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BDEF_EVALUATION_TIME    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BDEF_EVALUATION_TIME_F  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BDEF_EVAL_TRIGGER_OPRTN | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BDEF_EVAL_TRIGGER_OP_F  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BDEF_EXTENSIBLE_OPTION  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BDEF_IMPLEMENTATION_TYP | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BDEF_IMPLEMENTATN_TYP_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BDEF_KIND               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BDEF_ORIGIN             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BDEF_O_LOCAL            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BDEF_STANDARD_OPERATION | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BDEF_STANDARD_OPERATN_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BDEF_VERSION            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BGQC_ORIGIN             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BGQC_O_LOCAL            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_BOOLEAN                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_XCO_CDS_ANN_CLASS           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CDS_ANN_SELECTION_BLDR  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CDS_CARDINALITY         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CDS_CARDINALITY_1       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CDS_CARDINALITY_C       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CDS_CARDINALITY_CN      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CDS_CARDINALITY_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CDS_CARDINALITY_N       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CDS_LEFT_OUTER_JOIN_CAR | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CDS_LEFT_OUTER_JOIN_C_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CDS_PROVIDER_CONTRACT   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_ADT_SIMPLE_CLASSRUN  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_AD_OBJ_READ_STATE_F  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_AMDP_DB_LANGUAGE_F   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_AMDP_DB_OPTION_F     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_AMDP_DB_TYPE_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_AMDP_OPTION_F        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_AO_ORIGIN_FACTORY    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_AO_VERSION_F         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_APLO_OBJ_TEXT_ATTR_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_APLO_SUBOBJ_T_ATTR_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_APLO_TEXT_ATTR_F     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_ARS_API_STATE_FCTRY  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_ARS_RELEASE_CNTRCT_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_ARS_RELEASE_STATE_F  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_ARS_VISIBILITY_F     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_AU_DURATION_F        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_AU_RISK_LEVEL_F      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_BAL_LVL_OF_DTL_F     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_BCO_TEXT_ATTRIBUTE_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_BCS_ORIGIN_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_BDEF_EXTNSLB_OPTN_FC | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_BDEF_ORIGIN_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_BDEF_VERSION_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_BGQC_ORIGIN_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_BOOLEAN_F            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_CDS_PRVDR_CNTRCT_F   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_CS_FMT_ADT           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_CS_LP_METHOD         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_DBT_LOAD_UNIT_F      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_DBT_ORIGIN_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_DBT_STORAGE_TYPE_F   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_DDEF_ENT_TEXT_ATTR_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_DDEF_FLD_TEXT_ATTR_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_DDEF_OBJ_RD_STATE_F  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_DDEF_PRM_TEXT_ATTR_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_DDEF_TEXT_ATTR_F     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_DOMA_ORIGIN_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_DOMA_TEXT_ATTR_F     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_DRTY_ORIGIN_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_DRTY_VERSION_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_DTEL_ORIGIN_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_DTEL_TEXT_ATTR_F     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_EB_ORIGIN_FACTORY    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_EB_VERSION_F         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_FG_ORIGIN_FACTORY    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_FM_ORIGIN_FACTORY    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_FM_PARAMETER_KIND_F  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_FM_PROCESSING_TYPE_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_FM_RFC_INTF_CNTRCT_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_FM_RFC_SCOPE_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_FM_STATE_F           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_FM_UPDATE_TASK_KND_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_GEN_AO_STR_CM_TY_FCY | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_GEN_AO_TYPE_INCL_FCY | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_GEN_BDEF_TEMPLATE_FC | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_GEN_DDLS_TEMPLATE_FC | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_GEN_DDLX_TEMPLATE_FC | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_GEN_DOMA_TEMPLATE    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_GEN_DRTY_TEMPLATE_FC | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_GEN_DTEL_TEMPLATE    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_GEN_D_O_PUT_OPTION   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_GEN_O_PUT_O_SKP_ACTN | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_GEN_TABL_DBT_TMPLT   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_GEN_TABL_STR_TMPLT   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_GEN_TTYP_TEMPLATE    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_LES_ORIGIN_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_LES_VERSION_F        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_MC_TEXT_ATTR_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_MESSAGE_TYPE_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_ME_ENT_TEXT_ATTR_F   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_ME_FLD_TEXT_ATTR_F   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_ME_LAYER_F           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_ME_PRM_TEXT_ATTR_F   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_ME_TEXT_ATTR_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_NONT_ORIGIN_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_NONT_VERSION_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_RONT_ORIGIN_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_RONT_TYPE_CATEGORY_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_RONT_VERSION_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_SRVB_BINDING_TYPE_F  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_SRVB_ORIGIN_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_SRVB_VERSION_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_SRVC_CONSUMPN_TYPE_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_SRVC_ORIGIN_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_SRVC_VERSION_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_SRVD_ORIGIN_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_SRVD_PRVDR_CNTRCT_F  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_SRVD_VERSION_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_TAB_FIELD_PROPERTY_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_TAB_ORIGIN_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_TEN_URL_TYPE_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_TF_CONTENT_ORIGIN_F  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_TF_STATE_F           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_TM_FMT_ABAP          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_TM_FMT_ISO_8601_BSC  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_TM_FMT_ISO_8601_EXT  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_TP_TEXT_ATTR_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_TR_RELEASE_OPTION_FC | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_TR_RESOLUTION_FCTRY  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_XLSX_COLOR_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_XLSX_COORDINATE_FCT  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_XLSX_DAT_VAL_TYPE_F  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_XLSX_FONT_TYPE_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_XLSX_RA_VT_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_XLSX_STYLE_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CP_XLSX_WA_VT_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CS_FORMAT               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CS_LINE_NUMBER_FLAVOR   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CS_LINE_PATTERN         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CTS_CHANGE              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CTS_CHANGE_CONTEXT      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CTS_PROGRAM_ID          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_CTS_PROGRAM_ID_F        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DATE_CALCULATION_FCTRY  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_BUFFERING           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_BUFFERING_F         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_BUFFERING_TYPE      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_BUFFERING_TYPE_F    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_DATA_CLASS          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_DATA_CLASS_F        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_DATA_MAINTENANCE    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_DATA_MAINTENANCE_F  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_DELIVERY_CLASS      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_DELIVERY_CLASS_F    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_INDX_NU             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_INDX_NU_F           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_LOAD_UNIT           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_ORIGIN              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_O_LOCAL             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_SIZE_CATEGORY       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_SIZE_CATEGORY_F     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DBT_STORAGE_TYPE        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DDEF_ENT_TEXT           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DDEF_ENT_TEXT_ATTRIBUTE | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DDEF_FLD_TEXT           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DDEF_FLD_TEXT_ATTRIBUTE | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DDEF_OBJECT_READ_STATE  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DDEF_OBJECT_STATE       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DDEF_OBJECT_STATE_F     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DDEF_PRM_TEXT           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DDEF_PRM_TEXT_ATTRIBUTE | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DDEF_TYPE               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DDEF_TYPE_F             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DDL_EXPR_CAST_BP_DTYPE  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DOMAIN_ORIGIN           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DOMAIN_OUTPUT_STYLE     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DOMAIN_OUTPUT_STYLE_F   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DOMAIN_O_LOCAL          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DOMAIN_TEXT             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DOMAIN_TEXT_ATTRIBUTE   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DRTY_ORIGIN             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DRTY_O_LOCAL            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DRTY_VERSION            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DTEL_ORIGIN             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DTEL_O_LOCAL            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DTEL_TEXT               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_DTEL_TEXT_ATTRIBUTE     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_EB_ORIGIN               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_EB_O_LOCAL              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_EB_VERSION              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_FG_ORIGIN               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_FG_O_LOCAL              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_FM_ORIGIN               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_FM_O_LOCAL              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_FM_PARAMETER_KIND       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_FM_PROCESSING_TYPE      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_FM_RFC_INTF_CONTRACT    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_FM_RFC_SCOPE            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_FM_STATE                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_FM_UPDATE_TASK_KIND     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_AO_BP_PRMTR_TYPE    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_AO_BP_TYPE_SOURCE   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_AO_TYPE_INCLUDE     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_CDS_BP_CARDINALITY  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_CLAS_BP_AMDP_DB_ENT | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_DDLS_BP_DDL_EXPRESS | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_DDLS_BP_FIELD_TYPE  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_DDLS_BP_PARAM_DTYPE | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_DDLS_BP_PRVD_CNTRCT | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_DOMA_BP_FORMAT      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_DTEL_BP_DATA_TYPE   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_TABL_APS_ENH_CAT    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_TABL_BP_FKEY_CARD   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_TABL_BP_FLD_TYP_APS | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_TABL_BP_FLD_TYP_DBT | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_TABL_BP_FLD_TYP_GTT | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_TABL_BP_FLD_TYP_STR | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_TABL_DBT_BP_INDX_NU | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_TABL_DBT_ENH_CAT    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_TABL_STR_ENH_CAT    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_GEN_TTYP_BP_ROW_TYPE    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_KU_BOOLEAN_F            | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CL_XCO_KU_TEN_URL_TYPE_F       | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CL_XCO_KU_TM_FMT_ABAP          | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CL_XCO_KU_TM_FMT_ISO_8601_BSC  | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CL_XCO_KU_TM_FMT_ISO_8601_EXT  | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CL_XCO_LES_ORIGIN              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_LES_O_LOCAL             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_LES_VERSION             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_MC_TEXT                 | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_MC_TEXT_ATTRIBUTE       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_MESSAGE_TYPE            | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_XCO_ME_ENT_TEXT             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ME_ENT_TEXT_ATTRIBUTE   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ME_FLD_TEXT             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ME_FLD_TEXT_ATTRIBUTE   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ME_LAYER                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ME_PRM_TEXT             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_ME_PRM_TEXT_ATTRIBUTE   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_NONT_ORIGIN             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_NONT_O_LOCAL            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_NONT_VERSION            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_PKG_TYPE                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_PKG_TYPE_F              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_PKG_T_RELEVANCE         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_RONT_ORIGIN             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_RONT_O_LOCAL            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_RONT_TYPE_CATEGORY      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_RONT_VERSION            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_SC_CHANGEABILITY        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_SC_CHANGEABILITY_F      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_SC_EXTENDABILITY        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_SC_EXTENDABILITY_F      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_SRVB_BINDING_TYPE       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_SRVB_ORIGIN             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_SRVB_O_LOCAL            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_SRVB_VERSION            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_SRVC_CONSUMPTION_TYPE   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_SRVC_ORIGIN             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_SRVC_O_LOCAL            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_SRVC_VERSION            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_SRVD_ORIGIN             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_SRVD_O_LOCAL            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_SRVD_PROVIDER_CONTRACT  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_SRVD_VERSION            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_EC_0                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_EC_1                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_EC_2                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_EC_3                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_EC_4                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_ENHANCEMENT_CTGRY   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_ENHANCEMENT_CTGRY_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_FKEY_CARDINALITY    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_FKEY_CARDINALITY_1  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_FKEY_CARDINALITY_C  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_FKEY_CARDINALITY_CN | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_FKEY_CARDINALITY_F  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_FKEY_CARDINALITY_N  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_FKEY_FIELD_TYPE     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_FKEY_FIELD_TYPE_F   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_FP_FK_CHECK_TABLE   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_FP_FK_FIELD_TYPE    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_GEO_SPATIALREFSYSTM | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_GEO_SPATLREFSYSTM_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_ORIGIN              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_O_LOCAL             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TAB_PSL_FKFA_SCENARIO   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TEN_URL_TYPE            | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CL_XCO_TF_CONTENT_ORIGIN       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TF_STATE                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TP_TEXT                 | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TP_TEXT_ATTRIBUTE       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TR_ES_BUILDER           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TR_KIND                 | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TR_KIND_F               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TR_RESOLUTION           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TR_SELECTION_BUILDER    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TR_STATUS               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TR_STATUS_F             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TR_TYPE                 | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TR_TYPE_F               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TT_ACCESS               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TT_ACCESS_F             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TT_KEY_ACCESS           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TT_KEY_ACCESS_F         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TT_KEY_CATEGORY         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TT_KEY_CATEGORY_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_TT_KEY_DEFINITION       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_BORDER_STYLE       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_BORDER_STYLE_F     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_COLOR              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_COLOR_FACTORY      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_COLOR_STANDARD_F   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_COORDINATE         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_FONT_FAMILY        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_FONT_FAMILY_F      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_FONT_SCHEME        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_FONT_SCHEME_F      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_FONT_TYPE          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_HORZNTAL_ALGNMNT_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_HORZNTAL_ALIGNMENT | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_SLC_SIMPLE_FROM_TO | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_UNDERLINE_TYPE     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_UNDERLINE_TYPE_F   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_VERTICAL_ALGNMNT_F | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CL_XCO_XLSX_VERTICAL_ALIGNMENT | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CM_APJ_BASE                    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CT_AIC_GROUNDING_TEMPLATE      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_A4C_CP_SVC_PROP_NOT_FOUND   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_A4C_DESTINATION_NOT_FOUND   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_A4C_DEST_SVC_LOOKUP_FAILURE | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_A4C_RAP_QUERY_PROVIDER      | \-                 | \-            | C1                   | X                              |                        | Deprecated | CLAS CX_RAP_QUERY_PROVIDER    |
| CX_ABAP_API_STATE              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ABAP_AUTH_CHECK_EXCEPTION   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ABAP_BEHV_EVENT_HDLR_ERROR  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ABAP_BEHV_SAVE_FAILED       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ABAP_CONTEXT_INFO_ERROR     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_DATFM                  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_DATFM_AMBIGUOUS        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_DATFM_FORMAT_UNKNOWN   | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_DATFM_INVALID_DATE     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_DATFM_NO_DATE          | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_DECFLOAT_INVALID_CHAR  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_DECFLOAT_PARSE_ERR     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_DECFLOAT_PARSE_FATAL   | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_DIFF                   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ABAP_FOREIGN_LOCK           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ABAP_HTTP_TIMESTAMP_INVALID | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_INT_INVALID_CHAR       | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_ABAP_INVALID_NAME           | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_INVALID_PARAM_VALUE    | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_ABAP_INVALID_VALUE          | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_LOCK_FAILURE           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ABAP_MESSAGE_DIGEST         | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_NOT_AN_INTEGER         | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_NOT_A_PROGRAM          | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_NOT_A_TABLE            | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_NOT_IN_ALLOWLIST       | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_NOT_IN_PACKAGE         | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_NOT_IN_WHITELIST       | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_PROB_UNSUPPORTED       | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_RANDOM                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_RANGE_CONV             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ABAP_SQL_ERROR              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ABAP_TIMEFM_INVALID         | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ABAP_UTCLONG_INVALID        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ACO_APPLICATION_EXCEPTION   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ACO_COMMUNICATION_FAILURE   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ACO_SYSTEM_FAILURE          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ADT_CONTEXT_DYNAMIC         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ADT_CONTEXT_UNAUTHORIZED    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_AIA_DYNAMIC                 | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_AIA_STATIC                  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_AIC_API_FACTORY             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_AIC_API_ISLM_INSTANTIATION  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_AIC_COMPLETION_API          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_AIC_ORCHESTRATION_API       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_AIC_PROMPT_TEMPLATE         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_AI_APPLICATION_FAULT        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_AI_SYSTEM_FAULT             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_AMDPTD_PARAMETER_NOT_VALID  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_AMDP_CREATION_ERROR         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_AMDP_DBPROC_CREATE_FAILED   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_AMDP_EXECUTION_ERROR        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_AMDP_EXECUTION_FAILED       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_AMDP_VERSION_ERROR          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_AMDP_VERSION_MISMATCH       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_APJ_DT_CONTENT              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_APJ_RT                      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_APJ_RT_CONTENT              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_APPDESTINATION              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ARCH_API                    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ARCH_STORAGE_MANAGER        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ATD_EXCEPTION_CORE          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ATD_PARAM_NOT_FOUND         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ATO_PREFIX_DETERMINATION    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BADI                        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BADI_CONTEXT_ERROR          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BADI_DEPREC_HANDLE_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BADI_FILTER_ERROR           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BADI_INITIAL_CONTEXT        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BADI_INITIAL_REFERENCE      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BADI_MULTIPLY_IMPLEMENTED   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BADI_NOT_IMPLEMENTED        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BADI_NOT_SINGLE_USE         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BADI_UNKNOWN_ERROR          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BALI_INTERNAL_ERROR         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BALI_INVALID_PARAMETER      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BALI_NOT_FOUND              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BALI_NOT_POSSIBLE           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BALI_OBJECTS                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BALI_RUNTIME                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BAL_EXCEPTION               | \-                 | \-            | C1                   | X                              |                        | Deprecated | CLAS CX_BALI_RUNTIME          |
| CX_BCFG_TRANSPORT_RECORDER     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BCFG_TRANSPORT_REQUEST      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BCS_MAIL                    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BCS_MAIL_CONFIG             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BGMC                        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BGMC_OPERATION              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_BLE_DYNAMIC_TABLE_ERROR     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_BLE_HTTP_EXCEPTION          | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_BLE_RUNTIME_ERROR           | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_BU_AUTHORIZATION            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CALL_ST_ERROR               | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_CBO_RUNTIME_EXCEPTION       | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_CBO_WRITE_LOCKED            | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_CBO_WRITE_NOT_AUTHORIZED    | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_CBO_WRITE_NOT_EXISTING      | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_CHDO_ARCHIVE_ERROR          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CHDO_DELETE_ERROR           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CHDO_GENERATION_ERROR       | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_CHDO_READ_ERROR             | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_CHDO_WRITE_ERROR            | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_CI_ATC_CHECK_INVALID_ATTR   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CI_ATC_DATA_PROVIDER        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CI_ATC_INVALID_COMP_UNIT    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CI_ATC_TOKEN_NO_CALL        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CLOSE_RESOURCE_ERROR        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CMIS_CONSTRAINT             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CMIS_CONTENT_ALREADY_EXISTS | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CMIS_FILTER_NOT_VALID       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CMIS_INVALID_ARGUMENT       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CMIS_NAME_CONSTRAINT        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CMIS_NOT_SUPPORTED          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CMIS_OAUTH                  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CMIS_OBJECT_NOT_FOUND       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CMIS_PERMISSION_DENIED      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CMIS_ROOT                   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CMIS_RUNTIME                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CMIS_STORAGE                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CMIS_STREAM_NOT_SUPPORTED   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CMIS_UNAUTHORIZED           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CMIS_UPDATE_CONFLICT        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CMIS_VERSIONING             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_COMMCONNECTION              | \-                 | \-            | C1                   | X                              |                        | Deprecated | CLAS CX_APPDESTINATION        |
| CX_COMMUNICATION_TARGET_ERROR  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CONVERSION_EXT_INT          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CONVERSION_NO_DURATION      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_CORR_DYN_ERROR              | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_COTA_CONNECTION_NOT_OPENED  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CREATE_MEM_DUMP_ERROR       | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_CRL_RUNTIME_EXCEPTION       | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_CSV_FIELD_CATALOG           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_CSV_WRITER                  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_DYNAMIC_CHECK               | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_FDT_CP_UTILITY_EXCEPTIONS   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_FDT_FUNCTION_PROCESS_API    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_FDT_INPUT                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_FDT_PROCESSING              | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_FDT_SYSTEM                  | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_FHC_RUNTIME                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_FP_ADS_UTIL                 | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_FP_FDP_ERROR                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_FP_FORM_READER              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_FTD_EXCEPTION               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_FTD_INVALID_STATE           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_FTD_PARAMETER_NOT_FOUND     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_GSM_API                     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_HDLFS_CLIENT_ERROR          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_HDLFS_ERROR                 | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_HDLFS_HTTP_ERROR            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ICU_OTHER_ERROR             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ICU_PARSE_ERROR             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_INVALID_TRANSFORMATION      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_IRM_RT_DESTRUCTION_OBJECT   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_IRM_RT_EXEC                 | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_JSON_READER_ERROR           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_JSON_WRITER_ERROR           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_KMETH_ERR                   | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_LIST_ALREADY_ACTIVE         | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_LIST_ERROR                  | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_LIST_ERROR_DOWNLOAD         | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_LIST_ERROR_EMPTY_LIST       | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_LOB_SQL_ERROR               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_LOGOFF_FAILED               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_MBC_API_EXCEPTION           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_NO_CHECK                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_NR_OBJECT_NOT_FOUND         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_NR_SUBOBJECT                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_NUMBER_RANGES               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_PARAMETER_INVALID           | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_PARAMETER_INVALID_RANGE     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_PARAMETER_INVALID_TYPE      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_PROGRAM_NOT_FOUND           | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_RAP_EVENT_HDLR_ERROR        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_RAP_EVENT_HDLR_ERROR_RETRY  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_RAP_QUERY_FILTER_NO_RANGE   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_RAP_QUERY_PROVIDER          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_RAP_QUERY_PROV_NOT_IMPL     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_RAP_QUERY_RESPONSE_SET_TWIC | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_REDUNDANCY_CHECK            | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_REFERENCE_NOT_SERIALIZABLE  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_RESOURCE_ALREADY_CLOSED     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_RFC_DEST_PROVIDER_ERROR     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ROOT                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_RSPO_PDF_MERGER             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SADL_EXIT                   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SATC_API                    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SCAL                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SCPR_OBJECT_NOT_PERMITTED   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SD_CONTEXT_MISSING          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SD_INT_SERVER_ERROR         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SD_INVALID_DATA             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SD_NO_ACCESS                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SD_URI_MAPPING              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SLDAG_SYSTEM_DATA           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SMTG_EMAIL_COMMON           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SOAP_DESTINATION_ERROR      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SSI_EXCEPTION               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_STACKOFWP_INVALID_WP        | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_STACKOFWP_NOSTACK_AVAIL     | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_STACKOFWP_NO_AUTHORITY      | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_STACKOFWP_WP_NOT_RUN        | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| CX_STATIC_CHECK                | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_STREAM_ERROR                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_STREAM_IO_EXCEPTION         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_STREAM_POSITION_ERROR       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_STREAM_STATE_ERROR          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ST_CALL_ERROR               | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_CALL_METHOD_ERROR        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_CONDITION                | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_COND_CHECK_FAIL          | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_CONSTRAINT_ERROR         | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_DESERIALIZATION_ERROR    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_DYNAMIC_CALL_ST_ERROR    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_ST_ERROR                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_FORMAT_ERROR             | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_GROUP_MISSING_CASE       | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_INVALID_XML              | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_MATCH                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_MATCH_ATTRIBUTE          | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_MATCH_ELEMENT            | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_MATCH_NAMED              | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_MATCH_TEXT               | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_MATCH_TYPE               | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_REF_ACCESS               | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_RUNTIME_ERROR            | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_SERIALIZATION_ERROR      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_SWITCH_NO_CASE           | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_ST_VALIDATION_ERROR         | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SWF_CPWF_API                | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SWF_CPWF_CALLBACK           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SXML_ILLEGAL_ARGUMENT_ERROR | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SXML_INTERNAL_ERROR         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SXML_NAME_ERROR             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SXML_PARSE_ERROR            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SXML_STATE_ERROR            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_ARG_OUT_OF_DOMAIN        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_ARITHMETIC_ERROR         | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_ARITHMETIC_OVERFLOW      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_ASSIGN_CAST_ERROR        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_ASSIGN_CAST_ILLEGAL_CAST | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_ASSIGN_CAST_UNKNOWN_TYPE | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_ASSIGN_ERROR             | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_ASSIGN_ILLEGAL_COMPONENT | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_ASSIGN_OUT_OF_RANGE      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_BDEF_DERIVED_TYPE_ERROR  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_BUFFER_OVERFLOW          | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CODEPAGE_CONVERTER_INIT  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_COMPRESSION_ERROR        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_CODEPAGE      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_CODEPAGE_EX   | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_DATA_LOSS     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_ERROR         | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_EXACT_NOT_SUP | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_INEXACT_FLTP  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_LOST_DECIMALS | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_NOT_SUPPORTED | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_NO_BOOLEAN    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_NO_DATE       | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_NO_DATE_TIME  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_NO_ENUM_VALUE | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_NO_NUMBER     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_NO_QNAME      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_NO_RAW        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_NO_TIME       | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_NO_UUID       | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_OVERFLOW      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_ROUNDING      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_SRC_TOO_SHORT | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_UNKNOWN_CURR  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_UNKNOWN_LANGU | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CONVERSION_UNKNOWN_UNIT  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CREATE_DATA_ERROR        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CREATE_ERROR             | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_CREATE_OBJECT_ERROR      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_DATA_ACCESS_ERROR        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_DYNAMIC_OSQL_ERROR       | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_DYNAMIC_OSQL_SEMANTICS   | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_DYNAMIC_OSQL_SYNTAX      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_DYN_CALL_ERROR           | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_DYN_CALL_EXCP_NOT_FOUND  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_DYN_CALL_ILLEGAL_CLASS   | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_DYN_CALL_ILLEGAL_FUNC    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_DYN_CALL_ILLEGAL_METHOD  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_DYN_CALL_ILLEGAL_TYPE    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_DYN_CALL_PARAMETER_CONV  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_DYN_CALL_PARAMETER_ERROR | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_DYN_CALL_PARAM_MISSING   | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_DYN_CALL_PARAM_NOT_FOUND | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_DYN_TABLE_ERROR          | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_DYN_TABLE_ILL_COMP_VAL   | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_DYN_TABLE_ILL_LINE_TYPE  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_ENUM_CREATION            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_FIND_INFINITE_LOOP       | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_ILLEGAL_HANDLER          | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_IMPORT_FORMAT_ERROR      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_IMPORT_MISMATCH_ERROR    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_INVALID_REGEX            | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_INVALID_REGEX_FORMAT     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_INVALID_REGEX_OPERATION  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_INVALID_SUBMATCH         | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_ITAB_DUPLICATE_KEY       | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_ITAB_DYN_LOOP            | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_ITAB_ERROR               | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_ITAB_LINE_NOT_FOUND      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_MATCHER                  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_MESSAGE_ILLEGAL_TEXT     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_MISSING_OUTBUF           | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_MOVE_CAST_ERROR          | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_NO_CURRENT_MATCH         | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_NO_HANDLER               | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_NO_REFERENCE             | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_OFFSET_NOT_ALLOWED       | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_OPEN_SQL_DATA_ERROR      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_OPEN_SQL_DB              | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_OPEN_SQL_ERROR           | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_OPERATION_FAILURE        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_PRECISION_LOSS           | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_RANGE_OUT_OF_BOUNDS      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_REF_CREATION             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_REF_IS_INITIAL           | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_REF_NOT_SUPPORTED        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_REGEX                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_REGEX_LOCALE_MISMATCH    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_REGEX_TOO_COMPLEX        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_REMOTE_SESSION_APP_FAIL  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_REMOTE_SESSION_CLOSED    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_REMOTE_SESSION_COM_FAIL  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_REMOTE_SESSION_ERROR     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_REMOTE_SESSION_FAILURE   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_REPLACE_INFINITE_LOOP    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_RTTI_NO_CHECK            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_RTTI_SYNTAX_ERROR        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_RTTI_TYPE_NOT_RELEASED   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_SERIALIZABLE_OBJECT      | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_SQL_ERROR                | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_SQL_REDIRECT_ERROR       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_SQL_REPLACEMENT_ERROR    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_SQL_SHARING_ERROR        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_SQL_UNSUPPORTED_FEATURE  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_STRG_FORMAT              | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_STRG_PAR_VAL             | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_STRING_SIZE_TOO_LARGE    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_STRUCT_ATTRIBUTES        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_STRUCT_COMP_NAME         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_STRUCT_COMP_TYPE         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_STRUCT_CREATION          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_STRUCT_SUFFIX_NAME       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_TABLE_ATTRIBUTES         | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_TABLE_CREATION           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_TABLE_KEY_SPECIFICATION  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_TABLE_LINE_TYPE          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_TAB_RANGE_OUT_OF_BOUNDS  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_TRANS_OPTION_ERROR       | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_TYPE_CREATION            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_TYPE_NOT_EXACT           | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_TYPE_NOT_RELEASED        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_UNKNOWN_CURRENCY         | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_UNKNOWN_TYPE             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_SY_UNSUPPORTED_FUNCTION     | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_SY_ZERODIVIDE               | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_TRANSFORMATION_ERROR        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_TSTMP_INTERNAL_ERROR        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_UOM_ERROR                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_UUID_ERROR                  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_WEB_HTTP_CLIENT_ERROR       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_WEB_HTTP_CONVERSION_FAILED  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_WEB_MESSAGE_ERROR           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_WS_PROTOCOL_ERROR           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_XCO_AR_EXISTENCE_EXCEPTION  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_XCO_GEN_DELETE_EXCEPTION    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_XCO_GEN_PATCH_EXCEPTION     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_XCO_GEN_POST_EXCEPTION      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_XCO_GEN_PUT_EXCEPTION       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_XCO_LOCK_EXCEPTION          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_XCO_RUNTIME_EXCEPTION       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_XSDANY_ERROR                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_XSDANY_NAMESPACE_ERROR      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_XSDANY_PARSE_ERROR          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_XSDANY_PREFIX_CONFLICT      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_XSLT_ABAP_CALL_ERROR        | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_XSLT_CALL_ERROR             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_XSLT_DESERIALIZATION_ERROR  | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_XSLT_EXCEPTION              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_XSLT_FORMAT_ERROR           | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_XSLT_ID_HREF_ERROR          | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_XSLT_INVALID_XML            | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_XSLT_RUNTIME_ERROR          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| CX_XSLT_SERIALIZATION_ERROR    | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| CX_XSLT_SYSTEM_ERROR           | \-                 | \-            | C1                   | X                              | X                      | Released   |                               |
| MBC_CP_API                     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_ABAP_SYSTEM_TIMEZONE       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_ABAP_USER_TIMEZONE         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_CURRENCY_CONVERSION        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_CURR_TO_DECFLOAT_AMOUNT    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_DATS_FROM_DATN             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_DATS_TIMS_TO_TSTMP         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_DATS_TO_DATN               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_HIERARCHY                  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_TIMS_FROM_TIMN             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_TIMS_TO_TIMN               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_TSTMPL_FROM_UTCL           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_TSTMPL_TO_UTCL             | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_TSTMP_ADD_SECONDS          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_TSTMP_SECONDS_BETWEEN      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_TSTMP_TO_DATS              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_TSTMP_TO_DST               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_TSTMP_TO_TIMS              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| SQL_UNIT_CONVERSION            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP                         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_ABAP                    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_ABAP_DICTIONARY         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_ABAP_OBJECTS            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_ABAP_REPOSITORY         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_ABAP_SQL                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_ABAP_UNIT               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_AMDP                    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_APPLICATION_LOG_OBJECT  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_ARS                     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_BAL                     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_BCKGRND_PRCSSNG_CNTXT   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_BEHAVIOR_DEFINITION     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_BEHAVIOR_IMPLEMENTATION | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_BINARY                  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_BUSINESS_CNFGRTN_OBJECT | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_BUSINESS_CNFGRTN_SET    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_CALL_STACK              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_CDS                     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_CDS_ANNOTATION          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_CDS_TYPE_DEFINITION     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_CHARACTER               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_CTS                     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_DATABASE_TABLE          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_DATA_DEFINITION         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_DATA_ELEMENT            | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_DCL                     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_DDL                     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_DOMAIN                  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_EVENT_BINDING           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_FUNCTION_GROUP          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_FUNCTION_MODULE         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_GENERATION              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_GENERATION_AO           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_GENERATION_BDEF         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_GENERATION_DDLS         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_GENERATION_DDLX         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_GENERATION_DOMA         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_GENERATION_DTEL         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_GENERATION_SCP1         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_GENERATION_TABL         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_GENERATION_TTYP         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_HASH                    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_I18N                    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_JSON                    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_LANGUAGE                | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_LOGICAL_EXTERNAL_SCHEMA | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_MESSAGE                 | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_MESSAGE_CLASS           | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_METADATA_EXTENSION      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_NAME                    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_PACKAGE                 | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_RAP                     | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_REGULAR_EXPRESSION      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_SAP_OBJECT_NODE_TYPE    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_SAP_OBJECT_TYPE         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_SERVICE_BINDING         | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_SERVICE_CONS_MODEL      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_SERVICE_DEFINITION      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_SOFTWARE_COMPONENT      | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_STRING                  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_SYSTEM                  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_TABLE                   | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_TABLE_TYPE              | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_TENANT                  | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_TEXT_POOL               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_TIME                    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_TRANSFORMATION          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_TRANSPORT               | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_UUID                    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_XLSX                    | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_XLSX_READ_ACCESS        | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_XLSX_SELECTION          | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_CP_XLSX_WRITE_ACCESS       | \-                 | \-            | C1                   | X                              |                        | Released   |                               |
| XCO_KU                         | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| XCO_KU_BINARY                  | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| XCO_KU_JSON                    | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| XCO_KU_REGULAR_EXPRESSION      | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| XCO_KU_STRING                  | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| XCO_KU_TENANT                  | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| XCO_KU_TIME                    | \-                 | \-            | C1                   |                                | X                      | Released   |                               |
| XCO_KU_UUID                    | \-                 | \-            | C1                   |                                | X                      | Released   |                               |

## DDLS - Data Definition Language Source

| **Object**                     | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State**  | **Successor**                  |
|--------------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|------------|--------------------------------|
| ABP_BEHV_DRAFT_USER_ACCESS     | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| ABP_BEHV_PAR_SHARE             | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| A_NOTEBASIC                    | \-                 | \-            | C2                   |                                |                        | Released   |                                |
| A_REGION                       | \-                 | \-            | C2                   |                                |                        | Released   |                                |
| A_REGIONS                      | \-                 | \-            | C2                   |                                |                        | Released   |                                |
| A_REGIONTEXT                   | \-                 | \-            | C2                   |                                |                        | Released   |                                |
| A_REGION_TEXT                  | \-                 | \-            | C2                   |                                |                        | Released   |                                |
| CDS_HIER_EMPL_WITHOUT_PARAM2   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| CDS_HIER_EMPL_WITHOUT_PARAM4   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| CDS_WITH_CALCULATIONS          | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| CDS_WITH_CALCULATIONSP         | \-                 | \-            | C1                   | X                              |                        | Deprecated | ,                              |
| C_BUSINESSUSEREVENT            | \-                 | \-            | C0                   | X                              |                        | Released   |                                |
| C_PCF_CODEVALUEHELP            | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| C_SWF_SWD_C1_RELEASED_NFC_UT   | \-                 | \-            | C1                   |                                | X                      | Deprecated | ,                              |
| C_SWF_SWD_C1_RELEASED_UT       | \-                 | \-            | C1                   | X                              |                        | Deprecated | ,                              |
| DDCDS_CUSTOMER_DOMAIN_VALUE    | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_CUSTOMER_DOMAIN_VALUE_T  | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_CHAR1_SCP   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_CHAR1_T_SCP | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_CHAR2_SCP   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_CHAR2_T_SCP | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_CHAR3_SCP   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_CHAR3_T_SCP | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_CHAR4_SCP   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_CHAR4_T_SCP | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_CHAR5_SCP   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_CHAR5_T_SCP | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_CHAR6_SCP   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_CHAR6_T_SCP | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_CHAR7_SCP   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_CHAR7_T_SCP | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_CHAR8_SCP   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_CHAR8_T_SCP | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_INT1_SCP    | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_INT1_T_SCP  | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_INT2_SCP    | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_INT2_T_SCP  | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_INT4_SCP    | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_INT4_T_SCP  | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_NUMC1_SCP   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_NUMC1_T_SCP | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_NUMC2_SCP   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_NUMC2_T_SCP | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_NUMC3_SCP   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_NUMC3_T_SCP | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_NUMC4_SCP   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_NUMC4_T_SCP | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_NUMC5_SCP   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_NUMC5_T_SCP | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_NUMC6_SCP   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_NUMC6_T_SCP | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_NUMC7_SCP   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_NUMC7_T_SCP | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_NUMC8_SCP   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| DDCDS_TYPE_ENUMVAL_NUMC8_T_SCP | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| D_BUSINESSUSERCREATED          | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| D_BUSINESSUSERDELETED          | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| D_CPWF_CONTEXT_PARAMETER       | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| D_CPWF_START_PARAMETER         | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| D_SELECTCUSTOMIZINGTRANSPTREQP | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_ABAPCLOUDCUSTOMOBJECTS       | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ABAPTRANSPORTREQUESTTEXT     | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_ACADEMICTITLE                | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ACADEMICTITLETEXT            | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ACADEMICTITLEVH              | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ACTIVEADDRESSREPRESENTATION  | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRCOMMUNICATIONMETHODTEXT  | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRCURDEFAULTEMAILADDRESS   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRCURDEFAULTFAXNUMBER      | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRCURDFLTLANDLINEPHONENMBR | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRCURDFLTMOBILEPHONENUMBER | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRDELIVERYSERVICETYPETEXT  | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRDELIVERYSERVICETYPEVH    | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSCOMMUNICATIONMETHOD   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSCOMMUNICATIONMETHODVH | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSCOMMUNICATIONREMARK_2 | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSCOMMUNICATIONUSAGE    | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSDEFAULTREPRESENTATION | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSDELIVERYSERVICETYPE   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSEMAILADDRESS_2        | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSFAXNUMBER_2           | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSGROUP                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSGROUPTEXT             | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSGROUPVH               | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSMAINWEBSITEURL        | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSMANAGEMENTURITYPE     | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSMANAGEMENTURITYPETEXT | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSMANAGEMENTURITYPEVH   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSNONDELIVERABLEREASON  | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSNONDELIVERABLEREASONT | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSOBJECTTYPE            | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSOBJECTTYPETEXT        | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSPERSONNAME            | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSPHONENUMBER_2         | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSREMARK_2              | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSREPRESENTATION        | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSREPRESENTATIONCODEVH  | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSREPRESENTATIONTEXT    | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSURI                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESSWORKPLACEDETAILS      | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRESS_2                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRNONDELIVERABLEREASONVH   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRORGNAMEPOSTALADDRESS     | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ADDRPERSNNAMEDFLTRPRSTN      | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_APISFORCLOUDDEVELOPMENT      | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_APISFORSAPCOUDPLATFORM       | \-                 | \-            | C1                   | X                              |                        | Deprecated | DDLS I_APISFORCLOUDDEVELOPMENT |
| I_APISWITHCLOUDDEVSUCCESSOR    | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_APSOMPRINTQUEUEVH            | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_BPDATACONTROLLERUSAGE        | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_BPUSREXTERNALID              | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_BPUSRROLE                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_BUPAIDENTIFICATIONTYPE       | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_BUSINESSUSER                 | \-                 | \-            | C1                   | X                              | X                      | Deprecated | DDLS I_BUSINESSUSERBASIC       |
| I_BUSINESSUSERBASIC            | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_BUSINESSUSEREVENT            | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_BUSINESSUSERVH               | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_CASEATTRIBUTE                | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASEATTRIBUTEPROFILE         | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASEATTRIBUTEPROFILETEXT     | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASEAUTHORIZATIONLEVEL       | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASEAUTHORIZATIONLEVELTEXT   | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASECATEGORY                 | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASECATEGORYTEXT             | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASEENTITY                   | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASEESCALATIONREASON         | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASEESCALATIONREASONTEXT     | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASEFUNCTIONPROFILE          | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASEFUNCTIONPROFILETEXT      | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASEINDIVIDUALSTATUS         | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASEINDIVIDUALSTATUSTEXT     | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASEPRIORITY                 | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASEPRIORITYTEXT             | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASEPROCESS                  | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASEPROCESSTEXT              | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASEREASONS                  | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASEREASONSTEXT              | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASESTATUSPROFILE            | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASESTATUSPROFILETEXT        | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASESYSTEMSTATUS             | \-                 | \-            | C2                   |                                |                        | Released   |                                |
| I_CASESYSTEMSTATUSTEXT         | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASETERMINOLOGYPROFILE       | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASETERMINOLOGYPROFILETEXT   | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASETEXTPROFILE              | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASETEXTPROFILETEXT          | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASETYPES                    | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CASETYPESTEXT                | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_CONFIGNDEPRECATIONCODE       | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_CONFIGNDEPRECATIONCODETEXT   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_COUNTRY                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_COUNTRYTEXT                  | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_COUNTRYVH                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_CPWF_INST                    | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_CSTMBIZCONFIGNLASTCHGD       | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_CURRENCY                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_CURRENCYSTDVH                | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_CURRENCYTEXT                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_CUSTABAPOBJDIRECTORYENTRY    | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_CUSTABAPPACKAGE              | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_CUSTABAPSOFTWARECOMPONENT    | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_CUSTABAPSOFTWARECOMPONENTTXT | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_CUSTOMFIELDCODELISTTEXT      | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_CUSTOMFIELDCODELISTVALUE     | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_CUSTOMFIELDCODELISTVALUEHELP | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_DATAEXTRACTIONENABLEDVIEW    | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_DAYLIGHTSAVINGRULE           | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_DAYLIGHTSAVINGRULETEXT       | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_EXCHANGERATEFACTORSRAWDATA   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_EXCHANGERATERAWDATA          | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_EXCHANGERATESPREADRAWDATA    | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_EXCHANGERATETYPE             | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_EXCHANGERATETYPESTDVH        | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_EXCHANGERATETYPETEXT         | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_EXCHRATEQTANTYPERAWDATA      | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_FACTORYCALENDARBASIC         | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_FACTORYCALENDARBASICTEXT     | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_FACTORYCALENDARVALUEHELP     | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_FAMILYNAMEPREFIX             | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_FAMILYNAMEPREFIXVH           | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_FISCALPERIODRAWDATA          | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_FISCALPERIODTEXTRAWDATA      | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_FISCALYEARVARIANT            | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_FISCALYEARVARIANTTEXT        | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_FORMOFADDRESS                | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_FORMOFADDRESSTEXT            | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_LANGUAGE                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_LANGUAGETEXT                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_LANGUAGEVH                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_NAMESUPPLEMENT               | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_NAMESUPPLEMENTTEXT           | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_NAMESUPPLEMENTVH             | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ORGADDRESSDEFAULTRPRSTN      | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ORGANIZATIONADDRESS          | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_ORGNAMEPOSTLADDRDFLTRPRSTN   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_PCF_CODEVALUEHELP            | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_PCF_CODEVALUEHELPTEXT        | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_PCF_FIELD_TEXT_API           | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_PERSONADDRESS                | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_PERSONADDRESSDEFAULTRPRSTN   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_PERSONWORKPLACEADDRESS       | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_PHONENUMBERTYPE              | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_PHONENUMBERTYPETEXT          | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_POSTALCITY                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_POSTALCITYTEXT               | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_PUBLHOLIDAYCALENDARBASICTEXT | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_PUBLICHOLIDAYCALENDARBASIC   | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_PUBLICHOLIDAYCALENDARVH      | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| I_REGION                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_REGIONALSTRUCCHECKSTATUSTEXT | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_REGIONALSTRUCTURECHECKSTATUS | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_REGIONTEXT                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_REGIONVH                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_SAPGUIICON                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_SAPGUIICONTEXT               | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_SCBO2_CREATEDBYUSER          | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_SCBO2_DUMMY                  | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_SCBO2_LASTCHANGEDBYUSER      | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_SCBO2_MIGRATION_ENTRY        | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_SECONDARYREGION              | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_SECONDARYREGIONTEXT          | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_SHORTENEDFISCALYEAR          | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_STREET                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_STREETTEXT                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_SYSTEMUSER                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_TAXINGCOUNTY                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_TAXINGCOUNTYTEXT             | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_TERTIARYREGION               | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_TERTIARYREGIONTEXT           | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_TIMEZONE                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_TIMEZONEIANACODEMAP          | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_TIMEZONEIANACODESTDVH        | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_TIMEZONERULE                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_TIMEZONERULETEXT             | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_TIMEZONETEXT                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_TRANSPORTATIONZONE           | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_TRANSPORTATIONZONETEXT       | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_TRANSPORTATIONZONEVH         | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_UNITOFMEASURE                | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_UNITOFMEASURECOMMERCIALNAME  | \-                 | \-            | C1                   | X                              | X                      | Deprecated | DDLS I_UNITOFMEASURETEXT       |
| I_UNITOFMEASUREDIMENSION       | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_UNITOFMEASUREDIMENSIONTEXT   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_UNITOFMEASUREISOCODE         | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_UNITOFMEASUREISOCODETEXT     | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_UNITOFMEASURESTDVH           | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_UNITOFMEASURETECHNICALNAME   | \-                 | \-            | C1                   | X                              | X                      | Deprecated | DDLS I_UNITOFMEASURETEXT       |
| I_UNITOFMEASURETEXT            | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_USER                         | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_USERSUBSTITUTE               | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKFLOWAGENTRULE            | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKFLOWAGENTRULETEXT        | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKFLOWEXTERNALSTATUS       | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKFLOWEXTERNALSTATUSTEXT   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKFLOWLEAVEREQUEST         | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| I_WORKFLOWRECIPIENTS           | \-                 | \-            | C1                   |                                | X                      | Deprecated | DDLS I_WORKFLOWRECIPIENTS_V2   |
| I_WORKFLOWRECIPIENTS_V2        | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKFLOWSCENARIODEFINITION   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKFLOWSCENARIODEFTEXT      | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKFLOWSCENARIORESULT       | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKFLOWSCENARIORESULTTEXT   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKFLOWSTATUSDETAILS        | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKFLOWSTATUSOVERVIEW       | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKFLOWSTEPRESULT           | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKFLOWSTEPRESULTTEXT       | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKFLOWSTEPTYPE             | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKFLOWSTEPTYPETEXT         | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKFLOWTASKEXTERNALSTATTEXT | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKFLOWTASKEXTERNALSTATUS   | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| I_WORKPLACEADDRESS             | \-                 | \-            | C1                   | X                              | X                      | Released   |                                |
| RIS_SEARCH_RELEASED_OBJECTS    | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| SATC_API_APPROVER_AREAS        | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| SATC_API_AREAS                 | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| SATC_API_FINDINGS              | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| SATC_API_MESSAGE_GROUP         | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| SATC_API_MGRP_CRITERIA         | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| SATC_API_OBJECT_GROUP          | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| SATC_API_OGRP_CRITERIA         | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| SATC_API_RESULT_HEADERS        | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| SATC_EXEMPTIONS_DDLV_EC1       | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| SATC_EXEMPTIONS_DDLV_EC2       | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| SPAK_CLS_DDL_TEST_VIEW         | \-                 | \-            | C1                   |                                | X                      | Released   |                                |
| SYCM_APS_ATC_FINDINGS          | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| SYCM_APS_PROJECT               | \-                 | \-            | C1                   | X                              |                        | Released   |                                |
| SYCM_APS_SCOPE_BY_EP_ITEM      | \-                 | \-            | C1                   | X                              |                        | Released   |                                |

## DOMA - Domain

| **Object**                | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State**  | **Successor** |
|---------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|------------|---------------|
| /AIF/IFNAME               | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| /AIF/IFVERSION            | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| /AIF/NS                   | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| ABAPVRS                   | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| ABAP_BOOLEAN              | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ABAP_MSIZE                | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| ACO_PROXY_MSG_TYPE        | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| ACTIV_AUTH                | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| AD_NATION                 | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIFLAG                  | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BEGRU                     | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CHAR001                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR01                    | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| CHAR010                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR02                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR03                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR08                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR1                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| CHAR10                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR100                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR11                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR116                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR12                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR120                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR123                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR128                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR13                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR134                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR14                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR140                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR15                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR150                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR16                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR17                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR18                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR180                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR19                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR1_X                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR2                     | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR20                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR200                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR21                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR22                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR24                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR240                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR25                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR251                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR255                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR256                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR26                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR260                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR27                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR28                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR3                     | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR30                    | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| CHAR300                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR32                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR33                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR34                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR35                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR36                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR37                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR38                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR4                     | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR40                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR42                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR45                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR46                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR47                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR48                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR49                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR5                     | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR50                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR55                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR56                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR58                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR6                     | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR60                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR61                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR64                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR65                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR66                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR7                     | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR70                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR72                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR78                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR79                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR8                     | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR80                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR81                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR9                     | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR90                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| CHAR93                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| COUNC                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| DATS                      | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| DATUM                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| DDOPTION                  | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| DDSIGN                    | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| DISPLAY_PROTECTED_STRING  | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| DISPLAY_PROTECTED_XSTRING | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| DUMMY                     | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| ISOCD                     | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| ISOCD_UNIT                | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| MEINS                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| PROGNAME                  | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| REGEX_STANDARD            | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| SAP_BOOL                  | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| SHDM_MIMETYPE             | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| SNAP_INST_ID              | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| SPRAS                     | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| SWF_PBL_ID_FIELD          | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| SWF_PBL_SAP_OBJECT_TYPE   | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| SXSDDURATION_SIGN         | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| SYCHAR12K                 | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| TEXT1                     | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT10                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT100                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT11                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT12                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT120                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT128                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT132                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT140                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT15                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT16                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT17                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT18                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT2                     | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT20                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT200                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT220                   | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| TEXT240                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT25                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT255                   | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT27                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT3                     | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT30                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT31                    | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| TEXT32                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT34                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT35                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT4                     | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT40                    | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| TEXT42                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT45                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT47                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT5                     | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT50                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT55                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT56                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT60                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT64                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT65                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT7                     | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT70                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT72                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT8                     | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT80                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT9                     | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TEXT90                    | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| TZNTSTMPL                 | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| TZNTSTMPS                 | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| USNAM                     | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| UTF8STR_ND                | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| UTF8STR_XD                | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| WAERS                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| XFELD                     | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| XSDANY                    | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDBOOLEAN                | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| XSDCURRCODE               | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDDATETIME_ISO           | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDDATETIME_LOCAL         | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDDATETIME_LOCAL_DT      | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDDATETIME_LONG_Z        | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDDATETIME_OFFSET        | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDDATETIME_Z             | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDDATE_D                 | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDDATE_ISO               | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDDURATION_ISO           | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDGEO                    | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDLANGUAGE               | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDQNAME                  | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDTIME_ISO               | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDTIME_T                 | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDUNITCODE               | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDUUID_BASE32            | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDUUID_BASE64            | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDUUID_CHAR              | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XSDUUID_RAW               | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| XUBNAME                   | \-                 | \-            | C1                   | X                              |                        | Released   |               |

## DRTY - CDS Type Definitions

| **Object**                     | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|--------------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| ABP_BDEF_DERIVED_TYPE          | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| ABP_BEHV_AUTH                  | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| ABP_BEHV_FIELD_CTRL            | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| ABP_BEHV_FIELD_PERM            | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| ABP_BEHV_OP_CTRL               | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| ABP_BEHV_OP_PERM               | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| CALENDAR_DATE_LEVEL            | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CALENDAR_DATE_OPERATION        | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| CALENDAR_FISCAL_LEVEL          | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| CALENDAR_FISCAL_OPERATION      | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| CUSTOM_OBJECT_CATEGORY         | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| CUSTOM_SOFTWARE_COMPONENT_TYPE | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| I_SATC_API_CHECK_SCOPE         | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| I_SATC_API_EXEMPTION_APPR      | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| I_SATC_API_EXEMPTION_GRANU     | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| I_SATC_API_EXEMPTION_KIND      | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| I_SATC_API_EXEMPTION_STATE_C1  | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| I_SATC_API_EXEMPTION_STATE_C2  | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| I_SATC_API_EXEMPTION_VAL       | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| I_SATC_API_FNDQF               | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| I_SATC_API_ITEM_STATE          | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| I_SATC_API_OBJECT_SCOPE        | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| I_SATC_API_PCPH                | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| I_SATC_API_PRIORITY            | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SQL_HIERARCHY_RETAIN_NULLS     | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SQL_ON_ERROR                   | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SQL_ON_ERROR                   | \-                 | \-            | C2                   |                                |                        | Released  |               |

## DSFD - CDS Scalar Function Definition

| **Object**                 | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|----------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| CALENDAR_OPERATION         | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| CALENDAR_SHIFT             | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| COLUMN_TOTAL               | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| CURRENT_TOTAL              | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| DEMO_CDS_DECFLOAT_RATIO    | \-                 | \-            | C2                   |                                |                        | Released  |               |
| DEMO_CDS_SCALAR_HELLOWORLD | \-                 | \-            | C2                   |                                |                        | Released  |               |
| DEVIATION_RATIO            | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| EXPONENTIAL                | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| FISCAL_CALENDAR_OPERATION  | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| FISCAL_CALENDAR_SHIFT      | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| GET_CELL_REFERENCE_VALUE   | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| GRAND_TOTAL                | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| HRY_NODE_SIGN_VALUE        | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| LN                         | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| LOG                        | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| POWER                      | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| RATIO_OF                   | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| ROW_TOTAL                  | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| SQRT                       | \-                 | \-            | C1                   | X                              | X                      | Released  |               |

## DSFI - CDS Scalar Function Implementation Reference

| **Object**                     | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|--------------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| CALENDAR_OPERATION_ANA         | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| CALENDAR_SHIFT_ANA             | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| COLUMN_TOTAL_ANA               | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| CURRENT_TOTAL_ANA              | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| DEMO_CDS_DECFLOAT_RATIO_SQL    | \-                 | \-            | C2                   |                                |                        | Released  |               |
| DEMO_CDS_SCALAR_HELLOWORLD_SQL | \-                 | \-            | C2                   |                                |                        | Released  |               |
| DEVIATION_RATIO_ANA            | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| EXPONENTIAL_ANA                | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| FISCAL_CALENDAR_OPERATION_ANA  | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| FISCAL_CALENDAR_SHIFT_ANA      | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| GET_CELL_REFERENCE_VALUE_ANA   | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| GRAND_TOTAL_ANA                | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| HRY_NODE_SIGN_VALUE_ANA        | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| LN_ANA                         | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| LOG_ANA                        | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| POWER_ANA                      | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| RATIO_OF_ANA                   | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| ROW_TOTAL_ANA                  | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| SQRT_ANA                       | \-                 | \-            | C1                   | X                              | X                      | Released  |               |

## DTEL - Data Element

| **Object**                     | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State**  | **Successor**           |
|--------------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|------------|-------------------------|
| /AIF/IFNAME                    | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| /AIF/IFVERSION                 | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| /AIF/NS                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| /IWBEP/CP_HIDDEN_ELEMENT       | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| /IWBEP/V4_DELTA_STATUS         | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| /IWBEP/V4_FLOAT                | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| /IWBEP/V4_VALUE_CONTROL        | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| ABAPVRS                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| ABAP_BOOLEAN                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABAP_ENCOD                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABAP_MSIZE                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABAP_REPL                      | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| ABP_ACTION_NAME                | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_ASSOCIATION_NAME           | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_BEHV_CID                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_BEHV_DRAFT                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_BEHV_FEATURE               | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_BEHV_FLAG                  | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_BEHV_KIND                  | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_BEHV_MNGD_OP               | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| ABP_BEHV_OP_MODIFY             | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_BEHV_OP_READ               | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_BEHV_PID                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_BEHV_TYPEKIND              | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_CREATION_DATE              | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_CREATION_TIME              | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_CREATION_TSTMPL            | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_CREATION_USER              | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_CREATION_UTCL              | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_ELEMENT_NAME               | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_ENTITY_NAME                | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_EVENT_NAME                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_FIELD_NAME                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_LASTCHANGE_DATE            | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_LASTCHANGE_TIME            | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_LASTCHANGE_TSTMPL          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_LASTCHANGE_USER            | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_LASTCHANGE_UTCL            | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_LOCINST_LASTCHANGE_DATE    | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_LOCINST_LASTCHANGE_TIME    | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_LOCINST_LASTCHANGE_TSTMPL  | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_LOCINST_LASTCHANGE_USER    | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_LOCINST_LASTCHANGE_UTCL    | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_ROOT_ENTITY_NAME           | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ABP_TIMEST                     | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| ABWGA_CURR                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| ABWKT_CURR                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| ACO_PROXY_MSG_TYPE             | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| ACTIV_AUTH                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| ADDKO                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_ADDRNUM                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_ADRTYPE                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_COMCTRY                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_COMMLINENOTFORUNSLCTDCNTCT  | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_CONSNUM                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_CTRY_FR                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_EMAILCURDFLT                | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_FLOOR                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_HANDLE                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_LINE_S                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_NAMEFIR                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_NAMELAS                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_NATION                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_PERSNUM                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_PHNMBRCUROVRLDFLT           | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_PHONENUMBERTYPE             | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_PSTCD1                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_STRPRIO                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_TELNRLG                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_TITLE                       | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| AD_TITLETX                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| AD_TLNMBR                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| AD_TLXTNS                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ANDEC                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ANZEI                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| APJ_JOB_RESTART_MODE           | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| APPL_VAR                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ARCH_DOCID                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| AUTHOR3                        | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| BADI_CONTEXT_MODE              | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| BADI_FILTER_NAME               | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| BADI_NAME                      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| BALLEVEL                       | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| BALLOGHNDL                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| BALMNR                         | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| BALOBJ_D                       | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| BALOGNR                        | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| BALSUBOBJ                      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| BAPIAG                         | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPICUREXT                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPICUREXT31                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPICURR_D                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPILOGSYS                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPIMAXROW                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPINETWRK                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPIOPTION                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPIPARA                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPIRELSTA                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPISIGN                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPIUPDATE                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPIWAIT                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_BACK                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_COMP                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_CONV                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_FLD                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_HIGH                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_INDEX                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_LFRMT                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_LINE                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_LINESIZE                  | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_LISTR                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_LMASK                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_LOW                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_MSG                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_MTYPE                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_NCOMT                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_PARAM                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_RCODE                     | \-                 | \-            | C1                   | X                              | X                      | Deprecated |                         |
| BAPI_SIGN                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_STXT                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_TABL                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_TFRMT                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BAPI_TLINE                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| BDATJ                          | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| BEGRU                          | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| BOOLEAN                        | \-                 | \-            | C1                   | X                              |                        | Deprecated | DTEL ABAP_BOOLEAN       |
| BOOLE_D                        | \-                 | \-            | C1                   | X                              |                        | Deprecated | DTEL ABAP_BOOLEAN       |
| BTCRESTSTAT                    | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| BUMON                          | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| BUTAG                          | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| CALLTRANS2                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| CFD_CUSTOM_CURRENCY_NAME       | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| CFD_CUSTOM_UOM_LONG_NAME       | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| CFD_DUMMY                      | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| CHAR1                          | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR10                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR100                        | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR12                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR120                        | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR128                        | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR134                        | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR14                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR140                        | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR15                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR16                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR17                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR18                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR2                          | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR20                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR200                        | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR22                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR24                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR25                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR251                        | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR255                        | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR26                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR260                        | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR3                          | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR30                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR32                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR35                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR38                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR4                          | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR40                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR45                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR5                          | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR6                          | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR64                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR70                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR79                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR8                          | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR80                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CHAR90                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| CMIS_DECIMAL                   | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| CMIS_ENUM                      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| CMIS_ID                        | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| CMIS_LONG                      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| CMIS_REPOSITORY_ID             | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| CMIS_STRING                    | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| CNAM                           | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| CONFIG_DEPRECATION_CODE        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| CONFIG_DEPRECATION_CODE_NAME   | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| COUNC                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| CPCODEPAGE                     | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| D16N                           | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| D34N                           | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| DATN                           | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| DATS                           | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| DATUM                          | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| DDDBVERSION                    | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| DDLANGUAGE                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| DDOPTION                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| DDSIGN                         | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| DD_CDS_CALCULATED_UNIT         | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| DECAN                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| DEVCLASS                       | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| DHCDC_SUBSCRIBER_ID            | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| DIMID                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| DOMVALUE_H                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| DOMVALUE_L                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| DUMMY                          | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| DZAEHL                         | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| D_DELFUNC                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ECURR                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| EXP10                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| EXPON                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| FAMUNIT                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| FCURR_CURR                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| FDT_CALENDAR_WEEK              | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| FDT_DAY_OF_MONTH               | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| FDT_DAY_OF_WEEK                | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| FDT_MONTH                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| FDT_QUARTER_OF_YEAR            | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| FDT_SYBATCH                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| FDT_SYDATUM                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| FDT_SYUZEIT                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| FFACT_CURR                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FHC_DESCRIPTION                | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FHC_FACTORYDATE                | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FHC_FCALID                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FHC_HCALID                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FHC_LEGACY_FCALID              | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FHC_LEGACY_HCALID              | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FHC_VALID_FROM                 | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FHC_VALID_TO                   | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FHC_WORK_FRIDAY                | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FHC_WORK_HOLIDAY               | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FHC_WORK_MONDAY                | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FHC_WORK_SATURDAY              | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FHC_WORK_SUNDAY                | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FHC_WORK_THURSDAY              | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FHC_WORK_TUESDAY               | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FHC_WORK_WEDNESDAY             | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FIS_GJAHR                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| FIS_PERIV                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| FLAG                           | \-                 | \-            | C1                   | X                              |                        | Deprecated | DTEL ABAP_BOOLEAN       |
| FPDPNAME                       | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FPFNTEMB                       | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FPMIRRORING                    | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FPNAME                         | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| FPOPTIMIZE                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| GEOM_EWKB                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| GJAHR                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| GUID                           | \-                 | \-            | C1                   | X                              |                        | Deprecated | DTEL SYSUUID_X16        |
| HTTPPORT                       | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| ICON_D                         | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| ILEN                           | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| INT1                           | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| INT2                           | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| INT4                           | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| INTCA                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| IOFF                           | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| ISLM2_DE_BAR01                 | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| ISLM2_DE_DOUBLE_PARAM          | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| ISLM2_DE_FIELDNAME             | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| ISLM2_DE_INTEGER_PARAM         | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| ISLM2_DE_NCLOB_PARAM           | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| ISLM2_DE_PROBABILITY01         | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| ISLM2_DE_SCORE01               | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| ISLM3_DE_PERCENTILE            | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| ISLM_DE_REASON_CODE_QUALITY    | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| ISOCD                          | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| ISOCD_MARK                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ISOCD_TEXT                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| ISOCD_UNIT                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| KURST_CURR                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| KZKEH                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| KZWOB                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| LAISO                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| LAND1                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| LANGU                          | \-                 | \-            | C1                   | X                              |                        | Deprecated | DTEL SPRAS              |
| LENG                           | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| LIGHT                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| LOGSYSTEM                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| MANDT                          | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| MASS                           | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| MEINSINT                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| MOLQU                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| MSEH3                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| MSEH6                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| MSEHI                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| MSEHIUNIT                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| MSEHL                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| MSEHT                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| MSSIE                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| NENNR                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| NUM12                          | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| NUMC2                          | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| NUMC3                          | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| NUMC4                          | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| OBJDELFLAG                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| OUTPUTSTYLE                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| PCF_AMOUNT                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| PCF_BOOLEAN                    | \-                 | \-            | C1                   | X                              | X                      | Deprecated | DTEL ABAP_BOOLEAN       |
| PCF_CURRENCY                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| PCF_DATE                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| PCF_DECIMAL_NUMBER             | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| PCF_NUMBER                     | \-                 | \-            | C1                   | X                              | X                      | Deprecated | DTEL PCF_DECIMAL_NUMBER |
| PCF_QUANTITY                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| PCF_TIME                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| PCF_TIMESTAMP                  | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| PCF_UNIT                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| PERIV                          | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| PFADPRE                        | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| PGMID                          | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| POPER                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| PRESS_DEP                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| PRESS_UNIT                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| PRESS_VAL                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| PROGNAME                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| PRX_AUTOMATIC_RETRY            | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| PRX_LOGICAL_PORT_NAME          | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| PRX_NO_RETRY                   | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| PRX_WORKFLOW_TRIGGERED         | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| R3STATE                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| RAP_CP_ODATA_V2_EDM_DATETIME   | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| RAP_CP_ODATA_V2_EDM_TIME       | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| RAP_CP_ODATA_V4_EDM_DATE       | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| RAP_CP_ODATA_V4_EDM_DURATION   | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| RAP_CP_ODATA_V4_EDM_TIMEOFDAY  | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| RAP_CP_ODATA_VALUE_CONTROL     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| RDIR_CDATE                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| RDIR_UDATE                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| REDIRECT_STATUS                | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| REGEX_STANDARD                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| REGIO                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| RESPONSIBL                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| RFCDEST                        | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| RFCHOST_EXT                    | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| RFCLOAD_D                      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| RFCSERVICE                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| RFCSYSID                       | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| RKZ_DBNA                       | \-                 | \-            | C1                   | X                              |                        | Deprecated | DTEL TABNAME            |
| ROLEGROUP                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| RSAUEVENT                      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SAEARCHIVI                     | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SAEARDOID                      | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SAEDOKTYP                      | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SAENOTESH                      | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SAEOBJART                      | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SAPPDESTCATEGORY               | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SAPPDESTCHANGEDBY              | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SAPPDESTNAME                   | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SAPPDESTPROPERTY               | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SAP_BOOL                       | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SAP_OBJECT_NODE_TYPE_RAW       | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SAP_OBJECT_TYPE_RAW            | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SARCH_ARCHIVE_KEY              | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SARCH_OBJECT                   | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SARCH_OFFSET                   | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SARCH_SESSION_NUMBER           | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SCA_DS_OBJECT_PROVIDER_ID      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SCBO_ACTION_ID                 | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SCBO_BUSINESS_OBJECT_ID        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SCBO_NODE_ID                   | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SCOMMTARGET                    | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SCX_ATTRNAME                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SCX_ST_TSTAMP                  | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SDRAFT_CONSISTENCY_STATUS      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SDRAFT_UUID                    | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SHDM_MIMETYPE                  | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SKTELFTO                       | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SOBJ_NAME                      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SPRAS                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SVC_INSTANCE_NAME              | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SWE_EGUID                      | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SWF_ALL_USERS                  | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SWF_CPWF_CONSUMER              | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SWF_CPWF_HANDLE                | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SWF_PBL_ID_FIELD_1             | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SWF_PBL_ID_FIELD_2             | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SWF_PBL_ID_FIELD_3             | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SWF_PBL_ID_FIELD_4             | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SWF_PBL_ID_FIELD_5             | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SWF_PBL_ID_FIELD_6             | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SWF_PBL_SAP_OBJECT_TYPE        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SXCO_AD_FIELD_NAME             | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_AD_OBJECT_NAME            | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_AMDP_DB_ENTITY            | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_AO_COMPONENT_NAME         | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_AO_FULL_COMPONENT_NAME    | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_AO_OBJECT_NAME            | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_AO_SHORT_DESCRIPTION      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_AO_SUBCOMPONENT_NAME      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_APLO_OBJECT_NAME          | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_AR_OBJECT_NAME            | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_AR_OBJECT_TYPE            | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_AR_SHORT_DESCRIPTION      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_BAL_LOG_HANDLE            | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_BCO_NAME                  | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_BDEF_ACTION_NAME          | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_BDEF_ALIAS_NAME           | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_BDEF_EVALUATION_NAME      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_BDEF_EVENT_NAME           | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_BDEF_FUNCTION_NAME        | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_BDEF_GROUP_NAME           | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_CDS_ANN_PROPERTY          | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_CDS_ASSOCIATION_NAME      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_CDS_FIELD_NAME            | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_CDS_OBJECT_NAME           | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_CDS_PARAMETER_NAME        | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_CLAS_METHOD_NAME          | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_CTS_OBJECT_NAME           | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_CTS_OBJECT_TYPE           | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_DBT_INDEX_ID              | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_DBT_OBJECT_NAME           | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_DDEF_ALIAS_NAME           | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_FG_OBJECT_NAME            | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_FM_EXCEPTION_NAME         | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_FM_NAME                   | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_FM_PARAMETER_NAME         | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_GTT_OBJECT_NAME           | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_I18N_TEXT_ATTRIBUTE       | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_MC_OBJECT_NAME            | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_PACKAGE                   | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_SRVB_OBJECT_NAME          | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_SRVB_SERVICE_NAME         | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_SRVB_SERVICE_VERSION      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_SRVD_OBJECT_NAME          | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_TF_OBJECT_NAME            | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_TRANSPORT                 | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SXCO_USER_NAME                 | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| SYABCDE                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYAPPLI                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYBATCH                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYBATZD                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYBATZM                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYBATZO                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYBATZS                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYBATZW                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYBIN1                         | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYBINPT                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYBREP4                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYBSPLD                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCALLD                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCALLR                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCCURS                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCCURT                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCDATE                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCFWAE                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCHAR01                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYCHAR02                       | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCHAR12K                      | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCHAR30                       | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCHWAE                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCOLNO                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCPAGE                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCPROG                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCTABL                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCTYPE                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCUCOL                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCUROW                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYCURR                         | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYDATAR                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYDATE                         | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYDATUM                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYDAYST                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYDBCNT                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYDBNAM                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYDBSYS                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYDCSYS                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYDEBUG                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYDSNAM                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYDYNGR                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYDYNNR                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYENTRY                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYFDAYW                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYFDPOS                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYFFILE                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYFLENG                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYFMKEY                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYFODEC                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYFOLEN                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYFTYPE                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYGROUP                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYHEX02                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYHOST                         | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYINDEX                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYINPUT                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYLANGU                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYLDBPG                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYLILLI                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYLINCT                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYLINNO                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYLINSZ                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYLISEL                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYLISTI                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYLOOPC                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYLPASS                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYLSIND                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYLSTAT                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYMACDB                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYMACOL                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYMANDT                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYMARKY                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYMAROW                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYMODNO                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYMSGID                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYMSGLI                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYMSGNO                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYMSGTY                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYMSGV                         | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYNEWPA                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYNRPAG                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYONCOM                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYOPSYS                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPAART                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPAGCT                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPAGNO                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPAUTH                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPDEST                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPEXPI                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPFKEY                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPLAYO                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPLAYP                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPLIST                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPNWPA                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPRABT                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPRBIG                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPRCOP                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPRDSN                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPREFX                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPRI40                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPRIMM                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPRINI                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPRLOG                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPRNEW                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPRREC                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPRREL                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYPRTXT                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYREPI2                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYREPID                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYRSTRT                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYRTITL                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSCOLS                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSFNAM                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSFOFF                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSLSET                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSPONO                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSPONR                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSROWS                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSTACO                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSTARO                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSTDATLO                      | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSTEPL                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSTLOCDB                      | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSTLOCOP                      | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSTTIMLO                      | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSTZONLO                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYST_LANGU                     | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSUBCS                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSUBRC                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYSUBTY                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYSUUID_C22                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYSUUID_C26                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYSUUID_C32                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYSUUID_C36                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYSUUID_X16                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYSYSID                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYTABID                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYTABIX                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYTCODE                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYTFDSN                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYTFILL                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYTITLE                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYTLENG                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYTLOPC                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYTMAXL                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYTNAME                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYTOCCU                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYTPAGI                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYTSTIS                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYTTABC                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYTTABI                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYTVAR                         | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYTZONE                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYUCOMM                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYULINE                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYUNAME                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYUZEIT                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| SYVLINE                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYWAERS                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYWILLI                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYWINCO                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYWINDI                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYWINRO                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYWINSL                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYWINX1                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYWINX2                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYWINY1                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYWINY2                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYWTITL                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYXCODE                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYXFORM                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| SYXPROG                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| TABNAME                        | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| TCODE                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| TCURR_CURR                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| TEMP                           | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| TEMP_DEP                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| TEMP_UNIT                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| TEMP_VALUE                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| TEXT12                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT128                        | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT132                        | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT15                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT180                        | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT20                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT200                        | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT240                        | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT25                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT255                        | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT256                        | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT30                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT35                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT40                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT50                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT6                          | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT60                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT70                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT8                          | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT80                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT9                          | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TEXT90                         | \-                 | \-            | C1                   | X                              |                        | Deprecated |                         |
| TE_STRUC                       | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| TFACT_CURR                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| TIMESTAMP                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| TIMESTAMPL                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| TIMEX                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| TIMEZONE                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| TIMN                           | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| TRKORR                         | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| TROBJTYPE                      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| TVARV_NUMB                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| TVARV_OPTI                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| TVARV_SIGN                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| TVARV_VAL                      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| TXDIM                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| TZNTSTMPL                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| TZNTSTMPS                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| TZNZONE                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| UCCHECK                        | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| UKURS_CURR                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| UNAM                           | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| UNAME                          | \-                 | \-            | C1                   | X                              |                        | Deprecated | DTEL SYUNAME            |
| USALIAS                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| USNAM                          | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| UTCL                           | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| UTF8STR_FL                     | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| UTF8STR_N                      | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| UTF8STR_X                      | \-                 | \-            | C1                   |                                | X                      | Released   |                         |
| UUID                           | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| UZEIT                          | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| VALUEPART                      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| VAL_TEXT                       | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| VDM_CREATEDBYUSERDESCRIPTION   | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| VDM_CREATEDBYUSERID            | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| VDM_LASTCHANGEDBYUSERDESCRIPTI | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| VDM_LASTCHANGEDBYUSERID        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| VDM_USERDESCRIPTION            | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| VDM_USERID                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| WAERS_CURC                     | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| WF_RESULT                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| XFELD                          | \-                 | \-            | C1                   | X                              |                        | Deprecated | DTEL ABAP_BOOLEAN       |
| XSDANY                         | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDBOOLEAN                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| XSDCURRCODE                    | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDDATETIME_ISO                | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDDATETIME_LOCAL              | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDDATETIME_LOCAL_DT           | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDDATETIME_LONG_Z             | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDDATETIME_OFFSET             | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDDATETIME_Z                  | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDDATE_D                      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDDATE_ISO                    | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDDURATION_ISO                | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDGEO                         | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDLANGUAGE                    | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDQNAME                       | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDTIME_ISO                    | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDTIME_T                      | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDUNITCODE                    | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDUUID_BASE32                 | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDUUID_BASE64                 | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDUUID_CHAR                   | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XSDUUID_RAW                    | \-                 | \-            | C1                   | X                              |                        | Released   |                         |
| XUCLASS                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| XUDATFM                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| XUDCPFM                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| XUGLTGB                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| XUGLTGV                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| XULANGU                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| XUMODDATE                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| XUMODIFIER                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| XUMODTIME                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| XUTIMEFM                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |
| XUUFLAG                        | \-                 | \-            | C1                   | X                              | X                      | Released   |                         |

## ENHS - Enhancement Spot

| **Object**                     | **Subobject Type** | **Subobject**                  | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|--------------------------------|--------------------|--------------------------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| /AIF/CHANGEABLE_FIELDS         | BADI_DEF           | /AIF/CHANGEABLE_FIELDS         | C1                   |                                | X                      | Released  |               |
| ADDRESS_PRINT_FORMAT           | BADI_DEF           | ADDRESS_PRINT_FORMAT           | C1                   | X                              | X                      | Released  |               |
| CFD_CUSTOM_FIELD               | BADI_DEF           | CFD_RUNTIME_SOAP_AMOUNT_CONV   | C1                   |                                | X                      | Released  |               |
| CFD_DPP                        | BADI_DEF           | CFD_DPP_VALUE_MAPPING          | C1                   |                                | X                      | Released  |               |
| RSM_ES_RESPONSIBILITY_RULE     | BADI_DEF           | RSM_BADI_RESPONSIBILITY_RULE   | C1                   | X                              | X                      | Released  |               |
| SLIN_SEC_BADIS                 | BADI_DEF           | SLIN_BADI_DBTAB_ACCESS         | C1                   | X                              |                        | Released  |               |
| SLIN_SEC_BADIS                 | BADI_DEF           | SLIN_BADI_REJECTED_AUTH        | C1                   | X                              |                        | Released  |               |
| SLIN_SEC_BADIS                 | BADI_DEF           | SLIN_BADI_SEC_BACKDOOR         | C1                   | X                              |                        | Released  |               |
| SLIN_SEC_BADIS                 | BADI_DEF           | SLIN_BADI_SEC_PROCEDURES       | C1                   | X                              |                        | Released  |               |
| SLIN_SEC_BADIS                 | BADI_DEF           | SLIN_BADI_TRUSTED_SOURCES      | C1                   | X                              |                        | Released  |               |
| SLIN_SEC_BADIS                 | BADI_DEF           | SLIN_BADI_VULN_PROCEDURES      | C1                   | X                              |                        | Released  |               |
| SWF_INBOX_ACTION_PROCESSING    | BADI_DEF           | SWF_CHECK_ACTION_ALLOWED       | C1                   | X                              | X                      | Released  |               |
| SWF_PROCESS_VISIBILITY_CONTXT  | BADI_DEF           | SWF_PROC_VISIBILITY_CONTXT_RUN | C1                   | X                              | X                      | Released  |               |
| SWF_PROCESS_VISIBILITY_CONTXT  | BADI_DEF           | SWF_PROC_VISIBILITY_CONTXT_DEF | C1                   | X                              | X                      | Released  |               |
| SWF_PROCESS_WORKFLOW_CONDITION | BADI_DEF           | SWF_WORKFLOW_CONDITION_DEF     | C1                   | X                              | X                      | Released  |               |
| SWF_PROCESS_WORKFLOW_CONDITION | BADI_DEF           | SWF_WORKFLOW_CONDITION_EVAL    | C1                   | X                              | X                      | Released  |               |
| SWF_WI_FORWARD_AGENTS_GET      | BADI_DEF           | SWF_FORWARD_AGENTS_GET_CUSTOM  | C1                   | X                              | X                      | Released  |               |

## EVTB - RAP Event Binding

| **Object**           | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|----------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| BUSINESSUSER_CREATED | EVV                | 0001          | C2                   |                                |                        | Released  |               |
| BUSINESSUSER_DELETED | EVV                | 0001          | C2                   |                                |                        | Released  |               |

## FDT0 - FDT/BRFplus: System Application

| **Object**          | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State**  | **Successor**    |
|---------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|------------|------------------|
| ATO_TEST_1          | \-                 | \-            | C1                   |                                | X                      | Released   |                  |
| B1                  | \-                 | \-            | C1                   |                                | X                      | Released   |                  |
| DEMO_BRFP_HO_02     | \-                 | \-            | C1                   |                                | X                      | Deprecated | FDT0 TEST_APP_03 |
| ERR_TEST_01         | \-                 | \-            | C1                   |                                | X                      | Released   |                  |
| FDT_SYSTEM          | \-                 | \-            | C1                   | X                              | X                      | Released   |                  |
| NEW_TESTING_APP     | \-                 | \-            | C1                   | X                              | X                      | Released   |                  |
| SDNVJSA             | \-                 | \-            | C1                   |                                | X                      | Deprecated | FDT0 TEST_APP_03 |
| SYSTEST             | \-                 | \-            | C1                   | X                              | X                      | Released   |                  |
| TESTALLST_01_FECKER | \-                 | \-            | C1                   |                                | X                      | Released   |                  |
| TEST_APP_01         | \-                 | \-            | C1                   |                                | X                      | Released   |                  |
| TEST_APP_02         | \-                 | \-            | C1                   | X                              | X                      | Deprecated | TEST \_APP_03    |
| TEST_APP_03         | \-                 | \-            | C1                   | X                              | X                      | Deprecated | FDT0 TEST_APP_04 |
| TEST_APP_04         | \-                 | \-            | C1                   | X                              | X                      | Released   |                  |
| TEST_APP_06         | \-                 | \-            | C1                   |                                | X                      | Deprecated | TEST \_APP_02    |
| TEST_APP_REL        | \-                 | \-            | C1                   |                                | X                      | Released   |                  |
| TEST_CDS_APPL       | \-                 | \-            | C1                   |                                | X                      | Released   |                  |
| TEST_DBL_EXP        | \-                 | \-            | C1                   | X                              | X                      | Released   |                  |
| TEST_IMPORT         | \-                 | \-            | C1                   |                                | X                      | Released   |                  |
| TRIAL_APP_001       | \-                 | \-            | C1                   |                                | X                      | Released   |                  |

## FUGR - Function Group

| **Object** | **Subobject Type** | **Subobject**                  | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|------------|--------------------|--------------------------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| BACV       | FUNC               | BAPI_CONVERSION_INT2EXT        | C1                   | X                              |                        | Released  |               |
| BACV       | FUNC               | BAPI_CONVERSION_INT2EXT1       | C1                   | X                              |                        | Released  |               |
| BACV       | FUNC               | BAPI_CONVERSION_EXT2INT        | C1                   | X                              |                        | Released  |               |
| BACV       | FUNC               | BAPI_CONVERSION_EXT2INT1       | C1                   | X                              |                        | Released  |               |
| BAPT       | FUNC               | TRANSACTION_STATUS             | C1                   | X                              |                        | Released  |               |
| BAPT       | FUNC               | BUFFER_SUBSCRIBE_FOR_REFRESH   | C1                   | X                              |                        | Released  |               |
| BAPT       | FUNC               | TRANSACTION_ABORT              | C1                   | X                              |                        | Released  |               |
| BAPT       | FUNC               | TRANSACTION_BEGIN              | C1                   | X                              |                        | Released  |               |
| BAPT       | FUNC               | TRANSACTION_END                | C1                   | X                              |                        | Released  |               |
| BAPT       | FUNC               | BAPI_TRANSACTION_COMMIT        | C1                   | X                              |                        | Released  |               |
| BAPT       | FUNC               | BAPI_TRANSACTION_ROLLBACK      | C1                   | X                              |                        | Released  |               |
| BAPT       | FUNC               | BUFFER_REFRESH_ALL             | C1                   | X                              |                        | Released  |               |
| BASR       | FUNC               | BAPI_MONITOR_CHECKDOCU         | C1                   | X                              |                        | Released  |               |
| BATG       | FUNC               | BAPI_MESSAGE_GETDETAIL         | C1                   | X                              |                        | Released  |               |
| BATG       | FUNC               | BALW_CONVERT_DOCU_LINKS        | C1                   | X                              |                        | Released  |               |
| BATG       | FUNC               | BAPI_APPLICATIONLOG_GETDETAIL  | C1                   | X                              |                        | Released  |               |
| BATG       | FUNC               | BAPI_FIELDHELP_GETDOCU         | C1                   | X                              |                        | Released  |               |
| BATG       | FUNC               | BAPI_HYPERLINK_GETTEXT         | C1                   | X                              |                        | Released  |               |
| BATG       | FUNC               | BAPI_INTERFACE_GETDOCU         | C1                   | X                              |                        | Released  |               |
| BFHV       | FUNC               | BF_BAPI_F4_AUTHORITY           | C1                   | X                              |                        | Released  |               |
| BFHV       | FUNC               | BAPI_HELPVALUES_GET_SEARCHHELP | C1                   | X                              |                        | Released  |               |
| BFHV       | FUNC               | BAPI_HELPVALUES_GET            | C1                   | X                              |                        | Released  |               |
| BFRT       | FUNC               | BALW_RETURN_TO_RET2            | C1                   | X                              |                        | Released  |               |
| BFRT       | FUNC               | BALW_RET1_TO_RET2              | C1                   | X                              |                        | Released  |               |
| BFRT       | FUNC               | BALW_RANGES_CHECK              | C1                   | X                              |                        | Released  |               |
| BFRT       | FUNC               | BALW_BAPIRETURN_GET2           | C1                   | X                              |                        | Released  |               |
| BFRT       | FUNC               | BALW_BAPIRETURN_GET1           | C1                   | X                              |                        | Released  |               |
| BFRT       | FUNC               | BALW_BAPIRETURN_GET            | C1                   | X                              |                        | Released  |               |

## G4BA - SAP Gateway OData V4 Backend Service Group and Assignments

| **Object**                  | **Subobject Type** | **Subobject**                      | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State**  | **Successor**                                                |
|-----------------------------|--------------------|------------------------------------|----------------------|--------------------------------|------------------------|------------|--------------------------------------------------------------|
| API_ADDRESS                 | G4S                | SRVD_A2X API_ADDRESS 0001          | C2                   |                                |                        | Released   |                                                              |
| API_CBC_STA_O4              | G4S                | SRVD_A2X API_CBC_STA 0001          | C2                   |                                |                        | Released   |                                                              |
| API_CDR_FILE_PREPARE        | G4S                | SRVD_A2X API_CDR_FILE_PREPARE 0001 | C2                   |                                |                        | Released   |                                                              |
| API_REGION                  | G4S                | SRVD_A2X REGION 0001               | C2                   |                                |                        | Released   |                                                              |
| C_SATC_API_RESULT_R_WAPI_V4 | G4S                | SRVD_A2X SATC_API_RESULT_R 0001    | C2                   |                                |                        | Released   |                                                              |
| RSAU_LOG_API                | G4S                | SRVD_A2X RSAU_LOG_API 0001         | C2                   |                                |                        | Released   |                                                              |
| SATC_CI_CF_API              | G4S                | SRVD_A2X SATC_CI_CF_SV_API 0001    | C2                   |                                |                        | Released   |                                                              |
| SRAL_API_RAW_LOG_04         | G4S                | SRVD_A2X SRAL_API_RAW_LOG 0002     | C2                   |                                |                        | Released   |                                                              |
| SRAL_API_RAW_LOG_04         | G4S                | SRVD_A2X SRAL_API_RAW_LOG 0001     | C2                   |                                |                        | Deprecated | G4BA SRAL_API_RAW_LOG_04, G4S SRVD_A2X SRAL_API_RAW_LOG 0002 |

## INTF - Interface (ABAP Objects)

| **Object**                     | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State**  | **Successor**              |
|--------------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|------------|----------------------------|
| /AIF/IF_CHANGEABLE_FIELDS      | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| /IWBEP/IF_CP_CLIENT_PROXY      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_DATA_DESC_NODE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_DATA_DESC_NODE_L  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_EXPAND_NODE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_FILTER_FACTORY    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_FILTER_NODE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_REQUEST_ACTION    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_REQUEST_BATCH     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_REQUEST_BATCH_OP  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_REQUEST_CHANGESET | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_REQUEST_CREATE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_REQUEST_DELETE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_REQUEST_FUNCTION  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_REQUEST_READ      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_REQUEST_READ_01   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_REQUEST_READ_DLTA | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_REQUEST_READ_LIST | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_REQUEST_UPDATE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_REQUEST_UPDATE_L  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_RESOURCE_ACTION   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_RESOURCE_ENTITY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_RESOURCE_ENTITY01 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_RESOURCE_FUNCTION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_RESOURCE_LIST     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_RESPONSE_ACTION   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_RESPONSE_CREATE   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_RESPONSE_FUNCTION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_RESPONSE_READ     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_RESPONSE_READ_01  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_RESPONSE_READ_LST | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_RESPONSE_UPDATE   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_RESPONSE_UPDATE_L | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_RUNTIME_TYPES     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_CP_SEARCH_NODE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_MP_ADVANCED_PM    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_MP_BASIC_PM       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_ACTION         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_ACTION_IMP     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_ACT_PARAM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_ACT_RETURN     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_AC_ADVANCED    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_CPLX_PROP      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_CPLX_TYPE      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_CT_ADVANCED    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_ENTITY_SET     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_ENTITY_TYPE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_ENTITY_TYPE_V2 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_ET_ADVANCED    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_FUNCTION       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_FUNC_IMP       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_FUNC_IMP_V2    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_FUNC_PARAM     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_FUNC_RETURN    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_FU_ADVANCED    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_MDL_ADVANCED   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_MODEL          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_MODEL_INFO     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_NAV_PROP       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_PPROP_ADVANCED | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_PRIM_PROP      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_PRIM_TYPE      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_PTYPE_ADVANCED | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWBEP/IF_V4_PM_TYPES          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWXBE/IF_CONSUMER             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWXBE/IF_CONSUMER_EVENT       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWXBE/IF_CONSUMER_TOPIC       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| /IWXBE/IF_DESCRIPTION_TYPES    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_A4C_CP_SERVICE              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_A4C_RAP_QUERY_PROVIDER      | \-                 | \-            | C1                   | X                              |                        | Deprecated | INTF IF_RAP_QUERY_PROVIDER |
| IF_A4C_RAP_QUERY_REQUEST       | \-                 | \-            | C1                   | X                              |                        | Deprecated | INTF IF_RAP_QUERY_REQUEST  |
| IF_A4C_RAP_QUERY_RESPONSE      | \-                 | \-            | C1                   | X                              |                        | Deprecated | INTF IF_RAP_QUERY_RESPONSE |
| IF_ABAP_API_STATE              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_BEHAVIOR_TESTDOUBLE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_BEHV                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_BEHV_MESSAGE           | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_BEHV_TEST_ENVIRONMENT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_CLOSE_RESOURCE         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_CODEPAGE               | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_ABAP_CONV_IN                | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_CONV_OUT               | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_C_READER               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_C_WRITER               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_DATA_TYPE_HANDLE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_DB_BLOB_HANDLE         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_DB_CLOB_HANDLE         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_DB_LOB_HANDLE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_DB_READER              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_DB_WRITER              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_GZIP_BINARY_HANDLER    | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_GZIP_TEXT_HANDLER      | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_LOCK_OBJECT            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_MATCHER_CALLOUT        | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_PARALLEL               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_PROB_DISTRIBUTION      | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_PROB_DISTRIBUTION_8D34 | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_PROB_DISTRIBUTION_DF34 | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_PROB_DISTRIBUTION_ID34 | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_PROB_DISTRIBUTION_INT  | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_PROB_DISTRIBUTION_INT8 | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_PROB_TYPES             | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_RANDOM                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_READER                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_RUNTIME                | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_ABAP_RUNTIME_MEASUREMENT    | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_ABAP_RUNTIME_RESULT         | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_ABAP_RUNTIME_RESULT_METRIC  | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_ABAP_RUNTIME_SAMPLE         | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_ABAP_RUNTIME_TEST           | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_ABAP_RUNTIME_TEST_RESULT    | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_ABAP_RUNTIME_TEST_RUNNER    | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_ABAP_SQL_CONNECTION         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_SQL_CONNECTION_BUILDER | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_SQL_CONNECTION_DESCR   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_SQL_STEP_01_CONNECTION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_SQL_STEP_2A_CONNECTION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_SQL_STEP_2B_CONNECTION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_SQL_STEP_2C_CONNECTION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_TESTDOUBLE_ANSWER      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_TESTDOUBLE_ARGUMENTS   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_TESTDOUBLE_CONFIG      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_TESTDOUBLE_CONFIG_DBL  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_TESTDOUBLE_CONSTANTS   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_TESTDOUBLE_HANDLE      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_TESTDOUBLE_MATCHER     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_TESTDOUBLE_RESULT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_TESTDOUBLE_VERIFY      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_TIMESTAMP_UTIL         | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_ABAP_TX_COMPLETE            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_TX_FUNCTIONAL          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_TX_MODIFY              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_TX_READ                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_TX_SAVE                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_TX_SURFACE             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_UNGZIP_BINARY_HANDLER  | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_UNGZIP_TEXT_HANDLER    | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_UNIT_CONSTANT          | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ABAP_WRITER                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_X_READER               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ABAP_X_WRITER               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ACO_PROXY                   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ADDRESS_PRINT_FORMAT        | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_ADT_CONTEXT                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ADT_CONTEXT_DEV_OBJECT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ADT_CONTEXT_FORM_BASED_OBJ  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ADT_CONTEXT_OBJ_PROPERTIES  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ADT_CONTEXT_RESOURCE        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ADT_CONTEXT_SOURCE_POSITION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ADT_CONTEXT_SRC_BASED_OBJ   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIA_ACTION                  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIA_ACTION_CONTEXT          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIA_ACTION_RESULT           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIA_POPUP_RESULT            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIA_SD_ACTION_INPUT         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIA_SOURCE_CHANGE_RESULT    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_API_ERROR               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_COMPLETION_API          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_COMPLETION_API_RESULT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_COMPLETION_PARAMETERS   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_COMPLETION_STREAM       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_COMPLETION_STREAM_PART  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_COMPLETION_STREAM_RES   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_FORMAT_JSON_SCHEMA      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_FUNCTION_SPECIFIER      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_ISLM_COMPL_API_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_ISLM_ORCH_API_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_ISLM_PROMPT_TPL_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_MEDIA_MESSAGE           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_MESSAGE_CONTAINER       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_ORCHESTRATION_API       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_ORCHESTRATION_RESPONSE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_ORCHESTRATION_SETUP     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_ORCH_CFG_GROUNDING      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_ORCH_CFG_LLM            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_ORCH_CFG_TEMPLATING     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_ORCH_MEDIA_MESSAGE      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_ORCH_RESPONSE_FORMAT    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_ORCH_RESULT             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_ORCH_RES_GROUNDING      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_PROMPT_TEMPLATE         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_RESPONSE_FORMAT         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AIC_TOOL_CALL               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AI_APPLICATION_FAULT        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AMDPTD_AMDP_CLASS_CONFIG    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AMDPTD_DEPENDENCY_RULES     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AMDPTD_ENVIRONMENT_CONFIG   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AMDPTD_METH_CONTENT_CONFIG  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AMDPTD_METH_OUTPUT_CONFIG   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AMDPTD_REPLACEMENT_RULES    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AMDPTD_TABLE_CONTENT_CONFIG | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AMDPTD_TESTDOUBLE           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AMDPTD_VIEW_CONTENT_CONFIG  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AMDPTD_VIEW_OUTPUT_CONFIG   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AMDP_MARKER_HDB             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AMDP_TEST_ENVIRONMENT       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_APJ_DT_DEFAULTS             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_APJ_DT_EXEC_OBJECT          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_APJ_JT_CHECK                | \-                 | \-            | C1                   | X                              |                        | Deprecated | INTF IF_APJ_JT_CHECK_20    |
| IF_APJ_JT_CHECK_20             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_APJ_RT_EXEC_OBJECT          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_APJ_RT_JOB_NOTIF_EXIT       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_APJ_RT_RUN                  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_APJ_RT_VALUE_HELP_EXIT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_APJ_TYPES                   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_APPDESTINATION              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_APPDESTINATION_HTTP_LV5     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_APPDESTINATION_RFC_LV5      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ARCH_API_TYPES              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ARCH_DELETE                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ARCH_DELETE_API             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ARCH_READ_API               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ARCH_RELOAD                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ARCH_RELOAD_API             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ARCH_STORAGE_MANAGER        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ARCH_WRITE                  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ARCH_WRITE_API              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_ATO_PREFIX_DETERMINATION    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AUNIT_AUTHORITY_OBJSET      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AUNIT_AUTH_CHECK_CONTROLLER | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AUNIT_AUTH_CHECK_RESULT_LOG | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_AUNIT_CONSTANTS             | \-                 | \-            | C1                   | X                              |                        | Deprecated | INTF IF_ABAP_UNIT_CONSTANT |
| IF_BADI_CONTEXT                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BADI_INTERFACE              | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_BALI_CONSTANTS              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BALI_EXCEPTION_GETTER       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BALI_EXCEPTION_SETTER       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BALI_FREE_TEXT_GETTER       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BALI_FREE_TEXT_SETTER       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BALI_HEADER_GETTER          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BALI_HEADER_SETTER          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BALI_ITEM_FILTER            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BALI_ITEM_GETTER            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BALI_ITEM_SETTER            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BALI_LOG                    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BALI_LOG_DB                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BALI_LOG_FILTER             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BALI_MESSAGE_GETTER         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BALI_MESSAGE_SETTER         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BALI_OBJECT_HANDLER         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BAL_LOGGER                  | \-                 | \-            | C1                   | X                              |                        | Deprecated |                            |
| IF_BCFG_CD_CUST_OBJECT_SERVICE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BCFG_CD_TRANSPORT_MANAGER   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BCFG_CD_TRANSPORT_RECORDER  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BCFG_CD_TRANSPORT_SERVICE   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BCS_MAIL_STATUS_MONITOR     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BGMC_OPERATION              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BGMC_OPERATION_AIF          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BGMC_OPERATION_AIF_CONF     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BGMC_OPERATION_FRAMEWORK    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BGMC_OP_SINGLE              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BGMC_OP_SINGLE_TX_UNCONTR   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BGMC_PROCESS                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BGMC_PROCESS_FACTORY        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BGMC_PROCESS_MONITOR        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BGMC_PROCESS_SINGLE_OP      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BGMC_PROCESS_SPY            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BGMC_TEST_ENVIRONMENT       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BGMC_TEST_ENVIR_SPY         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BLE_API_MT_TENANT           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BLE_BADI_MARKER_INTERFACE   | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_BLE_BADI_RUNTIME            | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_BLE_DT_ROW_ITERATOR         | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_BLE_DYNAMIC_TABLE           | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_BLE_HTTP_CLIENT             | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_BLE_HTTP_REQUEST            | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_BLE_HTTP_RESPONSE           | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_BOTD_BUFDBL_ACTIONS_HANDLER | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_BUFDBL_ADD_BEHV_CONFIG | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_BUFDBL_FIELDS_HANDLER  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_BUFDBL_IN_CFG_MOD      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_BUFDBL_IN_CFG_READ     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_BUFDBL_IN_SET_MOD      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_BUFDBL_IN_SET_READ     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_BUFDBL_OUT_CFG_MOD     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_BUFDBL_OUT_CFG_READ    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_BUFDBL_OUT_SET_MOD     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_BUFDBL_OUT_SET_READ    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_BUFDBL_SET_ACTION_IMPL | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEMLAPI_BO_TEST_ENV | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEMLAPI_TEST_DOUBLE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEMLAPI_TEST_ENVCFG | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_CALL_CONFIG    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_ENTPART_MOD    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_ENTPART_PERM   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_ENTPART_READ   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_INBLDR_LOCKS   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_INBLDR_MOD     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_INBLDR_PERM    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_INBLDR_READ    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_IN_CFGBLDR     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_IN_CFG_LOCKS   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_IN_CFG_MOD     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_IN_CFG_PERM    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_IN_CFG_READ    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_IN_SET_LOCKS   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_IN_SET_MOD     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_IN_SET_PERM    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_IN_SET_READ    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_OUTBLDR_LOCKS  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_OUTBLDR_MOD    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_OUTBLDR_PERM   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_OUTBLDR_READ   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_OUT_CFGBLDR    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_OUT_CFG_LOCKS  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_OUT_CFG_MOD    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_OUT_CFG_PERM   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_OUT_CFG_READ   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_OUT_SET_LOCKS  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_OUT_SET_MOD    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_OUT_SET_PERM   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_OUT_SET_READ   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_REQUEST_LOCKS  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_VERIFICATION   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_VERIFY_LOCKS   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_VERIFY_MODIFY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_VERIFY_PERM    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_MOCKEML_VERIFY_READ    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_TXBUFDBL_BO_TEST_ENV   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_TXBUFDBL_TEST_DOUBLE   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_TXBUFDBL_TEST_ENVCFG   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_BOTD_TYPES_DEF              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CBE_BDEF_RUNTIME            | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_CBO2_KU_RUNTIME_TRACED_OBJ  | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_CBO_DEV_BO_NODE             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CBO_DEV_BUSINESS_OBJECT     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CBO_DEV_DATA_RETRIEVAL      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CBO_WRITE                   | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_CBO_WRITE_NODE              | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_CDS_ACCESS_CONTROL_DATA     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CDS_ACCESS_CONTROL_DOUBLE   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CDS_ENTITY_INSPECTOR        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CDS_NULL_VALUES_CONFIG      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CDS_PARAMETER_VALUES_CONFIG | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CDS_STUB                    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CDS_TEST_DATA               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CDS_TEST_ENVIRONMENT        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CFD_DPP_VALUE_MAPPING       | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_CFD_RUNTIME_SOAP_AMNT_CNV   | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_CHANGEDOCU_ARCHIVE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CHDO_DELETE_TOOLS           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CHDO_ENHANCEMENTS           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CHDO_OBJECT_TOOLS_REL       | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_CI_ATC_CHECK                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CI_ATC_CHECK_META_DATA      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CI_ATC_CHECK_VERS_COMPAT    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CI_ATC_COMMON_METADATA      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CI_ATC_DDIC_PROVIDER        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CI_ATC_DOMA_PROVIDER        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CI_ATC_FINDING_STACK        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CI_ATC_METADATA_PROVIDER    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CI_ATC_PSREM_AVAIL_CHECKER  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CI_ATC_QUICKFIX             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CI_ATC_SOURCE_CODE_PROVIDER | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CI_ATC_TABL_PROVIDER        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CI_ATC_TABVIEW_PROVIDER     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CI_ATC_TTYP_PROVIDER        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CI_ATC_UNIT_ASSERTER        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CI_ATC_UNIT_TEST_CASE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CI_ATC_VIEW_PROVIDER        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CMIS_CLIENT                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CONSTRAINT                  | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_CONVERSION_EXT_INT          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CSV_FIELD_CATALOG           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CSV_INVALID_VALUE_TRACE     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CSV_WRITER                  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_CX_DEV_OBJECT_INFO          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_DEMO_OUTPUT                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_DEMO_OUTPUT_CLOUD           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_ACTIONS              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_ADMIN_DATA           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_AST_FACTORY          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_AST_FUNCTION_NODE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_AST_LITERAL_NODE     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_AST_NODE             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_AST_REFERENCE_NODE   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_DATA_OBJECT          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_DATA_OBJ_ELEMENT     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_DATA_OBJ_STRUCTURE   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_DATA_OBJ_TABLE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_DECISION_TABLE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_EXTERNAL_TYPES       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_FACTORY              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_OPERATION_CHECK      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_OPERATION_DELETE     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_OPERATION_DEPLOY     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_OP_SAVE_ACTIVATE     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_PROJECT              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_PROJECT_SETTINGS     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_RULE                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_RULESERVICE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_RULESERVICE_VERSION  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_RULESET              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_TEXT_RULE            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_VALIDATION_OPERATION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_CP_VERSION_GENERIC      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FDT_FUNCTION_PROCESS_API    | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_FDT_RANGE                   | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_FDT_RULE                    | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_FDT_TYPES                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_FHC_FCAL_RUNTIME            | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_FHC_HCAL_RUNTIME            | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_FHC_HOLIDAY_RUNTIME         | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_FHC_ID_MAPPER               | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_FP_FDP_API                  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FP_FORM_BASE_READER         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FTD_ARGUMENTS_ITERATOR      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FTD_ARGUMENT_MATCHER        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FTD_BEHAVIOR_VERIFICATION   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FTD_INPUT_ARGUMENTS         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FTD_INPUT_CONFIGURATION     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FTD_INPUT_CONFIG_SETTER     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FTD_INVOCATION_ANSWER       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FTD_INVOCATION_RESULT       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FTD_OUTPUT_CONFIGURATION    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FTD_OUTPUT_CONFIG_SETTER    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FTD_TESTDOUBLE_ARGUMENT     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FUNCTION_TESTDOUBLE         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_FUNCTION_TEST_ENVIRONMENT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_GSM_API_CONSTANTS           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_GSM_API_METRIC              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_GSM_API_METRIC_GROUP        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_GSM_API_MODEL               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_GSM_API_PROVIDER            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_GSM_API_TEST                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_GSM_API_TYPES               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_HDLFS_ACCESS_POLICY_BLDR    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_HDLFS_DOWNLOAD              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_HDLFS_ERROR_RESPONSE        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_HDLFS_FILEMANAGER           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_HDLFS_HTTP_CLIENT           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_HDLFS_UPLOAD                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_HDLFS_USER_INFO             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_HTTP_DESTINATION            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_HTTP_SERVICE_EXTENSION      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_HTTP_SERVICE_EXTENSION_SSE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IRM_DESTRUCTION_OBJECT_EXEC | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IRM_RT_DESTRUCTION_OBJECT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IRM_RT_EXEC                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_ATTRIBUTE              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_ATTRIBUTE_DECL         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_ATT_LIST_DECL          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_CDATA_SECTION          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_CHARACTER_DATA         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_COMMENT                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_COND_DTD_SECTION       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_CONTENT_PARTICLE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_CORE                   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_DOCUMENT               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_DOCUMENT_FRAGMENT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_DOCUMENT_TYPE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_ELEMENT                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_ELEMENT_DECL           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_ENCODING               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_ENTITY_DECL            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_ENTITY_REF             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_EVENT                  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_INLINE_ITERATOR        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_ISTREAM_CORE           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_NAMED_NODE_MAP         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_NAMESPACE_CONTEXT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_NAMESPACE_DECL         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_NODE                   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_NODE_COLLECTION        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_NODE_FILTER            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_NODE_ITERATOR          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_NODE_LIST              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_NOTATION_DECL          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_OSTREAM_CORE           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_PARSER_CORE            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_PARSE_ERROR_CORE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_PI                     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_PI_PARSED              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_PI_UNPARSED            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_RENDERER_CORE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_STREAM_CORE            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_STREAM_FACTORY_CORE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_TEXT                   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_UNKNOWN                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_IXML_XPATH                  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_JSON_NODE                   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_JSON_READER                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_JSON_WRITER                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_MAIL_ADDRESS                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_MBC_CP_API_BUSINESS_CONFIG  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_MBC_CP_APP_CONFIGURATION    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_MBC_CP_MESSAGE              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_MBC_CP_RAP_API              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_MBC_CP_RAP_TABLE_CTS        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_MBC_CP_RAP_TDAT_CTS         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_MBC_CP_RECORDING_RESULT     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_MESSAGE                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_NUMBERRANGE_BUFFER          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_OO_ADT_CLASSRUN             | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_OO_ADT_CLASSRUN_OUT         | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_OSQL_DOUBLE                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_OSQL_NULL_VALUES_CONFIG     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_OSQL_PARAM_VALUES_CONFIG    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_OSQL_STUB                   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_OSQL_TEST_DATA              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_OSQL_TEST_ENVIRONMENT       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_PCF_READ_API                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_PCF_SRVC_ODATA_MODEL        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_PROXY_BASIS                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_PROXY_CLIENT                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_PROXY_DESTINATION           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RAP_EVENT_DOUBLE_MASS       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RAP_EVENT_DOUBLE_M_VERIFY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RAP_EVENT_DOUBLE_SINGLE     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RAP_EVENT_DOUBLE_S_VERIFY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RAP_EVENT_TEST_ENVIRONMENT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RAP_QUERY_AGGREGATION       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RAP_QUERY_FILTER            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RAP_QUERY_FILTER_TREE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RAP_QUERY_FILTER_TREE_NODE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RAP_QUERY_FILTER_TREE_TYPES | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RAP_QUERY_PAGING            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RAP_QUERY_PROVIDER          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RAP_QUERY_REQUEST           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RAP_QUERY_RESPONSE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RFC_DEST                    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RFC_REMOTE                  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RFC_REMOTE_INFO             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RFC_REMOTE_SESSION          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RFC_TRANSIENT_SESSION       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_RSM_BADI_RESPONSIBILITY_RUL | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_RSPO_PDF_MERGER             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SADL_EXIT                   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SADL_EXIT_CALC_ELEMENT_READ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SADL_EXIT_SORT_TRANSFORM    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SATC_API_APPR_AREAS         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SATC_API_APPR_AREAS_R       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SATC_API_APPR_CHECK_GROUPS  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SATC_API_APPR_CHECK_GRPS_R  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SATC_API_APPR_CONFIG        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SATC_API_APPR_CONFIG_R      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SATC_API_APPR_OBJECT_GROUPS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SATC_API_APPR_OBJECT_GRPS_R | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SATC_API_APPR_RESP          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SATC_API_APPR_RESP_R        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SATC_API_APPR_SEL_CRITERIA  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SATC_API_FACTORY            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SATC_API_RESULT             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SATC_API_RUN                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SATC_API_RUN_CONFIGURATION  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SATC_EXEMPTION_CONTROLLER   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SATC_OBJECT_SET             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SCPR_CD_BCSET_ACTIVATION    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SCPR_CD_BCSET_ACTIV_ADD_OPT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SCPR_CD_BCSET_ACTIV_HANDLER | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SCPR_CD_BCSET_ACTIV_OPTIONS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SCPR_CD_BCSET_ACTIV_RESULT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SCPR_CD_BCSET_ACTIV_START   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SCPR_CD_BCSET_OPTNS_HANDLER | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_ACTIONS                  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_ACTION_LINK              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_ACTION_MODEL             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_ACTION_PROVIDER          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_ACTION_SIMPLE            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_ACTION_UTIL              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_CONFIGURATION_FACTORY    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_CONFIG_ELEMENT           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_CONFIG_STRUCTURE         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_CONFIG_TABLE_STRUCTURED  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_CONTEXT                  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_DETERMINATION            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_FEATURE_CONTROL          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_FEATURE_CONTROL_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_MODEL                    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_PATH                     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_SIDEEFFECT_PROVIDER      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_UI_INFORMATION           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_UI_INFO_FACTORY          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_VALUE_HELP_DSNI          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_VALUE_HELP_OBJ_REFRENCES | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_VALUE_HELP_PROVIDER      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SD_VALUE_HELP_UTIL          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SECU                        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SERIALIZABLE_OBJECT         | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_SLDAG_BUSINESS_SYSTEM       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SLIN_BADI_DBTAB_ACCESS      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SLIN_BADI_REJECTED_AUTH     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SLIN_BADI_SEC_BACKDOOR      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SLIN_BADI_SEC_PROCEDURES    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SLIN_BADI_TRUSTED_SOURCES   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SLIN_BADI_VULN_PROCEDURES   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SLIN_GOV_DBTAB_ACCESS       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SLIN_REJECTED_AUTH          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SLIN_SEC_PROCEDURES         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SLIN_SEC_SY_BACKDOOR        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SLIN_SEC_TRUSTED_SOURCES    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SLIN_VULN_PROCEDURES        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SMTG_EMAIL_TEMPL_RENDERER   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SSI_RP_SESSION_MEMORY       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SWF_CPWF_API                | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_SWF_CPWF_API_FACTORY        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SWF_CPWF_CALLBACK           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SWF_CPWF_CAPI               | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_SWF_CPWF_CAPI_ENTITY        | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_SWF_CPWF_CAPI_WF_INSTS      | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_SWF_CPWF_CAPI_WF_INST_CTXT  | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_SWF_CP_JSON                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_SWF_FLEX_IFS_CONDITION_DEF  | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_SWF_FLEX_IFS_CONDITION_EVAL | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_SWF_FLEX_IFS_INBOX_ACTION   | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_SWF_FLEX_IFS_WI_FORWARD_CUS | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_SWF_IFS_PROC_VISIBILITY_DEF | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_SWF_IFS_PROC_VISIBILITY_RUN | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_SXML                        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SXML_ATTRIBUTE              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SXML_CLOSE_ELEMENT          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SXML_NAMED                  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SXML_NODE                   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SXML_NSURI_HELPER           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SXML_OPEN_ELEMENT           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SXML_READER                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SXML_VALUE                  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SXML_VALUE_NODE             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SXML_WRITER                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_SYSTEM_UUID                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_SYSTEM_UUID_RFC4122_STATIC  | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_SYSTEM_UUID_STATIC          | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_T100_DYN_MSG                | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_T100_MESSAGE                | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_TEST_DOUBLE_CONSTANTS       | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_UOM_CONTENT_HANDLER         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_WEB_HTTP_CLIENT             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_WEB_HTTP_HEADER             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_WEB_HTTP_REQUEST            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_WEB_HTTP_RESPONSE           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_WEB_HTTP_SSE_HANDLER        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_WEB_HTTP_STATUS             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_WSPROTOCOL                  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_WS_HTTP_HEADER_FACADE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_WS_SEQUENCE_FACADE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_WS_SERVER_CONTEXT           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_WS_SOAP_HEADER_FACADE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_WS_TRANSPORT_BINDING        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_ABAP_REPOSITORY         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_ABAP_TOKEN              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_ACCESS_CONTROL          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_ACCESS_CONTROLS         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_ADT_CLASSRUN_OUT        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AD_BUILT_IN_TYPE_RFRNC  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AD_DATA_ELEMENT         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AD_DATA_ELEMENTS        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AD_DATA_TYPE            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AD_DATA_TYPE_REFERENCE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AD_OBJECT               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AD_REFERENCE_TYPE_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AD_STRUCTURE            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AD_STRUCTURES           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AD_TABLE                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AD_TABLES               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AD_TABLE_TYPE           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AD_TABLE_TYPES          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AMDP_DATABASE_ENTITY    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AMDP_OPTION             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_CACHEABLE_ORIGIN     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_CLASS                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_CLASSES              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_ALIAS              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_ALIASES            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_ALIAS_CONTENT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_ALIAS_FACTORY      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_CLASS_DATA         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_CLASS_DATAS        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_CLASS_DATA_CONTENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_CLASS_DATA_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_CONSTANT           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_CONSTANTS          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_CONSTANT_CONTENT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_CONSTANT_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_DATA               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_DATAS              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_DATA_CONTENT       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_DATA_FACTORY       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_METHOD             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_TYPE               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_TYPES              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_TYPE_CONTENT       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_C_TYPE_FACTORY       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_INTERFACE            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_INTERFACES           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_OBJECT               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_EXCEPTION          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_EXCEPTIONS         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_EXCEPTIONS_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_EXCEPTION_CONTENT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_PARAMETER          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_PARAMETERS         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_PARAMETERS_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_PARAMETER_CONTENT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_P_CHANGING         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_P_CHANGINGS        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_P_CHANGINGS_FCTRY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_P_CHANGING_CONTENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_P_EXPORTING        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_P_EXPORTINGS       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_P_EXPORTINGS_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_P_EXPORTING_CONTNT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_P_IMPORTING        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_P_IMPORTINGS       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_P_IMPORTINGS_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_P_IMPORTING_CONTNT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_P_RETURNING        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_P_RETURNINGS       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_P_RETURNINGS_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_S_P_RETURNING_CONTNT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_TYPE                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_TYPE_REFERENCE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AO_TYPING_DEFINITION    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APLO_CONTENT            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APLO_SUBOBJECT          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APLO_SUBOBJECTS         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APLO_SUBOBJECTS_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APLO_SUBOBJECT_CONTENT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APPEND_STRUCTURE        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APPEND_STRUCTURES       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APPLICATION_COMPONENT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APPLICATION_LOG_OBJECT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APPLICATION_LOG_OBJECTS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APS_COMPONENT           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APS_COMPONENTS          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APS_COMPONENTS_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APS_COMPONENT_CONTENT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APS_COMPONENT_TYPE      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APS_CONTENT             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APS_FOREIGN_KEY         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APS_FOREIGN_KEY_CONTENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APS_SEARCH_HELP         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_APS_SEARCH_HELP_CONTENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_APLO_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_APLO_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_BDEF_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_BDEF_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_BGQC_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_CLAS_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_CLAS_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_DCLS_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_DCLS_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_DDLS_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_DDLS_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_DDLX_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_DDLX_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_DESD_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_DESD_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_DEVC_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_DEVC_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_DOMA_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_DOMA_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_DRTY_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_DRTY_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_DTEL_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_DTEL_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_EVTB_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_EVTB_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_FILTER               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_FUGR_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_FUGR_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_INTF_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_INTF_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_MSAG_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_MSAG_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_NONT_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_NONT_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_NROB_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_NROB_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_OBJECT               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_OBJECTS              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_OBJECT_CLASS         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_OBJECT_NAME          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_OBJECT_SOURCE        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_OBJECT_TYPE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_RONT_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_RONT_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_SCP1_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_SCP1_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_SMBC_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_SMBC_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_SRVB_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_SRVB_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_SRVC_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_SRVC_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_SRVD_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_SRVD_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_STOB_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_TABL_API_OBJECT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_TABL_APS_OBJ_CLASS   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_TABL_APS_OBJ_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_TABL_DBT_OBJ_CLASS   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_TABL_DBT_OBJ_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_TABL_GTT_OBJ_CLASS   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_TABL_GTT_OBJ_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_TABL_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_TABL_STR_OBJ_CLASS   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_TABL_STR_OBJ_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_TTYP_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_TTYP_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_XSLT_OBJECT_CLASS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_AR_XSLT_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BAL_LOG_FILTER          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BCKGRND_PRCSSNG_CNTXT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BCKGRND_PRCSSNG_CNTXTS  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BCS_CONTENT             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BCS_CUSTOMIZING_OBJECT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BCS_ENTITY              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BEHAVIOR_DEFINITION     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BEHAVIOR_DEFINITIONS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BEHAVIOR_DEFINITION_CO  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BGQC_CONTENT            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BIMP_TD_REQUEST         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BIMP_TD_REQUEST_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BIMP_TD_RESPONSE        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BIMP_TD_RESPONSE_F      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BIMP_TD_STRUCTURE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BIMP_TD_STRUCTURE_F     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BIMP_TD_TABLE           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BIMP_TD_TABLE_F         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BIMP_TYPE_DECLARATION_F | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BINARY_TEXT_ENCODING    | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_BUSINESS_CNFGRTN_OBJCT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BUSINESS_CNFGRTN_OBJCTS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BUSINESS_CNFGRTN_SET    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_BUSINESS_CNFGRTN_SETS   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ABSTRACT_ENTITY     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ABSTRACT_ENTITY_CON | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ANNOTATION          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ANNOTATIONS         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ANN_FILTER          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ANN_TARGET          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ANN_VALUE           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ANN_VALUE_BUILDER   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ANN_VALUE_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ANN_VAL_PRIMITIVE   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ANN_VAL_P_BOOLEAN   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ANN_VAL_P_ENUM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ANN_VAL_P_NULL      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ANN_VAL_P_NUMBER    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ANN_VAL_P_SIMPLE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ANN_VAL_P_STRING    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ANN_VT_VISITOR      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ASSOCIATION         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ASSOCIATIONS        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ASSOCIATIONS_FCTRY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ASSOCIATION_CONTENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_COMPOSITION         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_COMPOSITIONS        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_COMPOSITIONS_FCTRY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_COMPOSITION_CONTENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_CUSTOM_ENTITY       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_CUSTOM_ENTITY_CONT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ENTITIES            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_ENTITY              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_FIELD               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_FIELDS              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_FIELDS_FACTORY      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_FIELD_CONTENT       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_FIELD_TYPE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_PARAMETER           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_PARAMETERS          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_PARAMETERS_FCTRY    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_PARAMETER_CONTENT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_PARAMETER_DATA_TYPE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_PROJECTION_VIEW     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_PROJECTION_VIEW_CO  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_TABLE_FUNCTION      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_TABLE_FUNCTION_CONT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_TYPE_DEFINITION     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_TYPE_DEFINITIONS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_UNION               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_UNION_CONTENT       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_VIEW                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_VIEW_CONTENT        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_VIEW_ENTITY         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CDS_VIEW_ENTITY_CONTENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CHAR_CODE_PAGE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CHAR_CP_CONVERSION      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CLAS_CACHEABLE_ORIGIN   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CLAS_CLASS_METHOD       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CLAS_COMPONENTS_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CLAS_COMPONENT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CLAS_CONTENT            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CLAS_C_METHOD           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CLAS_C_METHODS          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CLAS_C_METHODS_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CLAS_C_METHOD_CONTENT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CLAS_DEFINITION         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CLAS_DEFINITION_CONTENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CLAS_DEFINITION_SECTION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CLAS_IMPLEMENTATION     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CLAS_I_METHOD           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CLAS_I_METHOD_CONTENT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CLAS_SUBCLASSES         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CLAS_SUBCLASSES_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_APPLICATION_CPNT_FCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_API_OBJECT        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_API_OBJECTS       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_API_OBJECT_NAME   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_API_OBJECT_TYPE   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_APLO_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_BDEF_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_CLAS_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_DCLS_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_DDLS_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_DDLX_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_DESD_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_DEVC_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_DOMA_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_DRTY_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_DTEL_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_EVTB_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_FILTER_FACTORY    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_FUGR_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_INTF_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_MSAG_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_NONT_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_NROB_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_RONT_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_SCP1_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_SMBC_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_SRVB_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_SRVC_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_SRVD_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_STOB_OBJECT_CLASS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_STOB_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_TABL_APS_OC_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_TABL_DBT_OC_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_TABL_GTT_OC_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_TABL_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_TABL_STR_OC_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_TTYP_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_AR_XSLT_OC_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_EXC_ADDITION     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_EXC_ADDITION_FCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_EXC_DESCENT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_EXC_DESCENT_FCT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_LM_TIMESTAMP     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_LOG              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_LOGS             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_LOGS_FACTORY     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_LOG_EXCEPTION    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_LOG_EXCEPTIONS   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_LOG_EXCEPTIONS_F | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_LOG_FACTORY      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_LOG_FILTER_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_LOG_HEADER       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_LOG_MESSAGE      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_LOG_MESSAGES     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_LOG_MESSAGES_FCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_PERSISTENCE      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_PERSISTENCE_FCT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_PROFILE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_PROFILE_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_SOURCE           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BAL_SOURCE_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_BINARY_TXT_ENC_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_CALL_STACK           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_CDS_API_ANNOTATIONS  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_CHAR_CODE_PAGE_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_CS_EXTR_API_FROM     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_CS_EXTR_API_TO       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_CS_FORMAT_FACTORY    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_CS_LINE_NMBR_FLV_FCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_CS_LINE_PATTERN_FCT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_CTS_ATTRIBUTE        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_CTS_CHANGE_SCNR_FCT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_DATA_OBJECT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_BDEF_D_API       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_BDEF_D_O_DELETE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_BDEF_D_O_PUT_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_BDEF_D_O_PUT_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_BDEF_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_BDEF_TPL_SOURCE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_BGQC_O_DELETE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_BGQC_O_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_BGQC_O_PATCH_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_BGQC_O_PATCH_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_BGQC_O_PUT_OBJCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_BGQC_O_PUT_SCTN  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_BGQC_S_CHANGE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_BGQC_S_CH_UPDATE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_BGQC_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_CLAS_D_API       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_CLAS_D_O_DELETE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_CLAS_D_O_PATCH   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_CLAS_D_O_PAT_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_CLAS_D_O_PUT_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_CLAS_D_O_PUT_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_CLAS_O_PAT_OBJ_D | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_CLAS_O_PAT_O_D_S | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_CLAS_S_DELETE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_CLAS_S_DE_D_SECT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_CLAS_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_CLAS_S_INSERT    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_CLAS_S_IN_D_SECT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_CLAS_S_UPDATE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DCLS_D_API       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DCLS_D_O_DELETE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DCLS_D_O_PUT     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DCLS_D_O_PUT_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DCLS_D_O_PUT_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DCLS_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DDLS_D_API       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DDLS_D_O_DELETE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DDLS_D_O_PUT_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DDLS_D_O_PUT_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DDLS_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DDLS_TPL_SOURCE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DDLX_D_API       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DDLX_D_O_DELETE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DDLX_D_O_PUT_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DDLX_D_O_PUT_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DDLX_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DDLX_TPL_SOURCE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DESD_O_DELETE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DESD_O_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DESD_O_PATCH_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DESD_O_PATCH_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DESD_O_PUT_OBJCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DESD_O_PUT_SCTN  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DESD_S_CHANGE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DESD_S_CH_UPDATE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DESD_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DEVC_D_API       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DEVC_D_O_DELETE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DEVC_D_O_PUT     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DEVC_D_O_PUT_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DEVC_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DEVC_S_FO_PROPER | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DOMA_D_API       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DOMA_D_O_DELETE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DOMA_D_O_PATCH   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DOMA_D_O_PATCH_O | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DOMA_D_O_PUT_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DOMA_D_O_PUT_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DOMA_O_PATCH_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DOMA_S_CHANGE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DOMA_S_CH_DELETE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DOMA_S_CH_INSERT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DOMA_S_CH_UPDATE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DOMA_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DOMA_TEMPLATE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DOMA_TEMPLATE_FY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DRTY_O_DELETE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DRTY_O_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DRTY_O_PUT_OBJCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DRTY_O_PUT_SCTN  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DRTY_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DRTY_TPL_SOURCE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DTEL_D_API       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DTEL_D_O_DELETE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DTEL_D_O_PATCH   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DTEL_D_O_PATCH_O | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DTEL_D_O_PUT_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DTEL_D_O_PUT_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DTEL_O_PATCH_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DTEL_S_CHANGE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DTEL_S_CH_UPDATE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DTEL_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DTEL_TEMPLATE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_DTEL_TEMPLATE_FY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_D_O_PUT          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_D_O_PUT_OPTION   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_ENV_DEV_SYSTEM   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_ENV_FACTORY      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_EVTB_O_DELETE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_EVTB_O_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_EVTB_O_PATCH_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_EVTB_O_PATCH_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_EVTB_O_PUT_OBJCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_EVTB_O_PUT_SCTN  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_EVTB_S_CHANGE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_EVTB_S_CH_DELETE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_EVTB_S_CH_INSERT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_EVTB_S_CH_UPDATE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_EVTB_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_FUGR_D_API       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_FUGR_D_O_DELETE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_FUGR_D_O_PATCH   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_FUGR_D_O_PATCH_O | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_FUGR_D_O_POST    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_FUGR_D_O_POST_O  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_FUGR_S_DELETE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_FUGR_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_FUGR_S_INSERT    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_FUGR_S_UPDATE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_INTF_D_API       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_INTF_D_O_DELETE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_INTF_D_O_PATCH   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_INTF_D_O_PATCH_O | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_INTF_D_O_PUT_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_INTF_D_O_PUT_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_INTF_S_DELETE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_INTF_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_INTF_S_INSERT    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_INTF_S_UPDATE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_MSAG_D_API       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_MSAG_D_O_DELETE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_MSAG_D_O_PATCH   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_MSAG_D_O_PATCH_O | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_MSAG_D_O_PUT     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_MSAG_D_O_PUT_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_MSAG_S_DELETE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_MSAG_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_MSAG_S_FO_MSG    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_MSAG_S_INSERT    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_MSAG_S_IN_MSG    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_MSAG_S_MODIFY    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_MSAG_S_MO_MSG    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_MSAG_S_UPDATE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_MSAG_S_UP_MSG    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_NONT_O_DELETE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_NONT_O_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_NONT_O_PATCH_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_NONT_O_PATCH_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_NONT_O_PUT_OBJCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_NONT_O_PUT_SCTN  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_NONT_S_CHANGE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_NONT_S_CH_UPDATE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_NONT_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_O_DELETE         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_O_PATCH          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_O_PATCH_MASS     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_O_POST           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_O_PUT            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_O_PUT_OPTION_FCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_RONT_O_DELETE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_RONT_O_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_RONT_O_PATCH_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_RONT_O_PATCH_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_RONT_O_PUT_OBJCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_RONT_O_PUT_SCTN  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_RONT_S_CHANGE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_RONT_S_CH_UPDATE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_RONT_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SCP1_O_DELETE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SCP1_O_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SCP1_O_PATCH     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SCP1_O_PATCH_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SCP1_O_POST      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SCP1_O_POST_OBJ  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SCP1_S_CHANGE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SCP1_S_CH_DELETE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SCP1_S_CH_INSERT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SCP1_S_CH_UPDATE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SCP1_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SCP1_TMPLT_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SRVB_D_API       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SRVB_D_O_DELETE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SRVB_D_O_PUT     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SRVB_D_O_PUT_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SRVB_D_O_PUT_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SRVB_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SRVD_D_API       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SRVD_D_O_DELETE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SRVD_D_O_PUT_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SRVD_D_O_PUT_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_SRVD_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_APS_O_DEL   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_APS_O_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_APS_O_PUT_O | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_APS_O_PUT_S | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_APS_S_FORM  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_DBT_API     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_DBT_DOPU_SC | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_DBT_D_API   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_DBT_D_O_DEL | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_DBT_D_O_P_O | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_DBT_O_PAT_O | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_DBT_O_PAT_S | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_DBT_S_CHNG  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_DBT_S_CH_DE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_DBT_S_CH_IN | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_DBT_S_CH_UP | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_DBT_S_CU_TD | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_DBT_S_FORM  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_DBT_S_FO_TD | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_DBT_TMPLT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_DBT_TMPLT_F | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_GTT_DOPU_SC | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_GTT_D_API   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_GTT_D_O_DEL | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_GTT_D_O_P_O | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_GTT_S_FORM  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_STR_API     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_STR_DOPU_SC | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_STR_D_API   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_STR_D_O_DEL | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_STR_D_O_P_O | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_STR_O_PAT_O | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_STR_O_PAT_S | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_STR_S_CHNG  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_STR_S_CH_UP | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_STR_S_FORM  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_STR_TMPLT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TABL_STR_TMPLT_F | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TTYP_D_API       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TTYP_D_O_DELETE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TTYP_D_O_PUT_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TTYP_D_O_PUT_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TTYP_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TTYP_TEMPLATE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_TTYP_TEMPLATE_FY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_XSLT_D_API       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_XSLT_D_O_DELETE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_XSLT_D_O_PUT_OBJ | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_XSLT_D_O_PUT_SCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_GEN_XSLT_S_FORM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_HASH_ALGORITHM_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_I18N_ALO_TARGT_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_I18N_BCO_TARGT_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_I18N_DD_TARGET_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_I18N_DE_TARGET_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_I18N_DM_TARGET_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_I18N_MC_TARGET_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_I18N_ME_TARGET_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_I18N_TARGET_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_I18N_TP_TARGET_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_I18N_TT_TARGET_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_JSON_DATA            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_JSON_DATA_BUILDER    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_JSON_DATA_FACTORY    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_JSON_TRNSFRMTN_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_LANG_FORMAT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_NAMESPACE            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_NAMESPACE_FACTORY    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_NAME_CHOICE_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_PACKAGE_FACTORY      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_PKG_FILTER_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_REGEX_ENGINE_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_SOFTWARE_COMPONENT_F | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_SRVB_API_LCL_SRVC_EP | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_SRVB_API_LSE_ODV2    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_SRVB_API_LSE_ODV2_OP | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_SRVB_API_LSE_ODV4    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_SRVB_API_LSE_ODV4_OP | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_STD_CURRENT          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_STD_CUR_API_CLL_STCK | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_STD_SY               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_STRING_CMP_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_STRING_DCMP_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_SYS_API_LANGUAGES    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TAB_PSL_FACTORY      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TENANT               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TEN_GLOBL_ACCOUNT_ID | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TEN_SUBACCOUNT_ID    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TM_DATE              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TM_DATE_FORMAT       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TM_FORMAT_FACTORY    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TM_MOMENT            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TM_MOMENT_FORMAT     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TM_MOMENT_INTERVAL   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TM_TIME              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TM_TIME_FORMAT       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TM_TIME_ZONE_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TM_UNIX_TIMESTAMP    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TRANSPORT            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TRANSPORTS           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TRANSPORTS_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TRANSPORT_FACTORY    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_API_ENTRIES       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_API_KEY_ENTRIES   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_API_OBJ_ENTRIES   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_ATTRIBUTE         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_ATTRIBUTES        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_ENTRIES           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_ENTRY             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_ENTRY_CLASS       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_ENTRY_FILTER_FCT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_FILTER_FACTORY    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_KEY_ENTRIES       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_KEY_ENTRY         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_KE_CLASS          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_KE_TABLE_KEY      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_KE_TK_COMPONENT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_KE_TK_CPNT_VALUE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_OBJECT_ENTRIES    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_OBJECT_ENTRY      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_OE_CLASS          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_OE_FILTER_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_R3TR_API_OBJ_ENTS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_R3TR_OBJECT_ENTRS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_R3TR_OBJECT_ENTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_R3TR_OE_CLASS     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_R3TR_TABU_API_OES | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_R3TR_TABU_OBJ_ENS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_R3TR_TABU_OBJ_ENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_R3TR_TABU_OE_CLSS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_REQUEST           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_REQUEST_ATTRBTS_F | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_REQUEST_PROPRTIES | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_SELECTION         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_TASK              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_TR_TASK_PROPERTIES   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_URL                  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_USER                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_UUID_FORMAT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_XLSX_DOCUMENT_FCTRY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_XLSX_DOC_EMPTY       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_XLSX_DOC_FILE_CONTNT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CP_XLSX_SLC_PB_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CS_FORMAT               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CS_LINE_NUMBER_FLAVOR   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CS_LINE_PATTERN         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CTS_CHANGEABLE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CTS_CHANGE_CARRIER      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CTS_CHANGE_SCENARIO     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CTS_CHANGE_TARGET       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CTS_OBJECT              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_CTS_OBJECT_LOCK         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DATABASE_TABLE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DATABASE_TABLES         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DATA_DEFINITION         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DATA_DEFINITIONS        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DATA_OBJECT             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DATE_CALCULATION        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DBT_CACHEABLE_ORIGIN    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DBT_CONTENT             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DBT_FIELD               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DBT_FIELDS              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DBT_FIELDS_CONTENT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DBT_FIELDS_FACTORY      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DBT_FIELD_CONTENT       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DBT_FIELD_PROPOSAL_FCT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DBT_FIELD_PRP_FKFA      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DBT_FIELD_PRP_FKFA_RSLT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DBT_FIELD_TYPE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DBT_FOREIGN_KEY         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DBT_FOREIGN_KEY_CONTENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DBT_SEARCH_HELP         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DBT_SEARCH_HELP_CONTENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DBT_TEXT_TABLE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_ASPECT           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_ASPECT_OPERATOR  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_INHERIT          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_INHERIT_ENTITY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_INHERIT_ROLE     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_INHERIT_SUPER    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_INH_DEFAULT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_INH_REPLACING    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_INH_R_CONDS      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_INH_R_ELEMENT    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_INH_R_PARAMETRS  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_INH_R_PFCG_FLR   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_INH_R_PREFIX     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_INH_R_ROOT       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_INH_R_V_CONDS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_PFCG             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_PFCG_LEFT_SIDE   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_PFCG_LS_FIELD    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_PFCG_OPERATOR    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_PFCG_RIGHT_SIDE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_USER             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CB_USER_OPERATOR    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_CONDITION_BUILDER   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_COND_ASPECT_F       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_COND_FACTORY        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_COND_INHERT_ENTTY_F | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_COND_INHERT_ROLE_F  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_COND_INHERT_SUPER_F | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_COND_PFCG_F         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_COND_USER_F         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_EXPRESSION          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_EXPRESSION_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_EXPR_CONDITION      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_EXPR_FIELD          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_LITERAL             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DCL_LITERAL_FACTORY     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DDA_RECORD              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DDA_RECORDS             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DDA_RECORD_FIELD        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DDA_RECORD_FIELD_VALUE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DDA_RECORD_PROCESSOR    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DDL_EB_CASE             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DDL_EB_CAST             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DDL_EXPRESSION          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DDL_EXPR_CASE_F         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DDL_EXPR_CAST_DTYPE     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DDL_EXPR_CAST_F         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DDL_EXPR_CONDITION      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DDL_EXPR_DATA_SOURCE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DDL_EXPR_DATA_SOURCE_F  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DDL_EXPR_FACTORY        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DDL_EXPR_FIELD          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DDL_LITERAL_FACTORY     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DOMAIN                  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DOMAINS                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DOMAIN_CACHEABLE_ORIGIN | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DOMAIN_CONTENT          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DOMAIN_FIXED_VALUE      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DOMAIN_FIXED_VALUES     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DOMAIN_FIXED_VALUES_FCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DOMAIN_FIXED_VALUE_CNT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DOMAIN_FORMAT           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DP_ACTION               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DP_ACTION_DECORATOR     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DP_ACTION_RESULT        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DP_ADDITION             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DP_CHECK                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DP_CHECK_RESULT         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DP_LOCK                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DP_ONGOING_ACTION       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DRTY_CACHEABLE_ORIGIN   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DRTY_CONTENT            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DTEL_CACHEABLE_ORIGIN   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DTEL_CONTENT            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_DTEL_DATA_TYPE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_EB_CACHEABLE_ORIGIN     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_EB_CONTENT              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_EB_EVENT_VERSION        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_EB_EVENT_VERSIONS       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_EB_EVENT_VERSIONS_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_EB_EVENT_VERSION_CNT    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_EVENT_BINDING           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_EVENT_BINDINGS          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FG_CACHEABLE_ORIGIN     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FG_CONTENT              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FG_FUNCTION_MODULES     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FG_FUNCTION_MODULES_FCT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_CACHEABLE_ORIGIN     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_CONTENT              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_EXCEPTION            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_EXCEPTIONS           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_EXCEPTIONS_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_EXCEPTION_CONTENT    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_PARAMETER            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_PARAMETERS           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_PRMS_CHANGING        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_PRMS_CHANGING_FCTRY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_PRMS_EXPORTING       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_PRMS_EXPORTING_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_PRMS_IMPORTING       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_PRMS_IMPORTING_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_PRM_CHANGING         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_PRM_CHA_CONTENT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_PRM_CHA_TYPE         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_PRM_EXPORTING        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_PRM_EXP_CONTENT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_PRM_EXP_TYPE         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_PRM_IMPORTING        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_PRM_IMP_CONTENT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_PRM_IMP_TYPE         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FM_SOURCE_CODE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FUNCTION_GROUP          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FUNCTION_GROUPS         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_FUNCTION_MODULE         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_FO_COMPONENT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_FO_C_ALIAS     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_FO_C_CONSTANT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_FO_C_DATA      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_FO_C_METHOD    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_FO_C_TYPE      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_FO_PRODUCT     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_FO_S_EXCEPTION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_FO_S_P_CHNGNG  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_FO_S_P_EXPRTNG | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_FO_S_P_IMPRTNG | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_FO_S_P_RETRNG  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_UP_COMPONENT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_UP_C_ALIAS     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_UP_C_CONSTANT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_UP_C_DATA      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_UP_C_METHOD    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_UP_METHD_DELET | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_UP_METHD_INSRT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_UP_METHD_UPDAT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_UP_SUBCOMPNT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_UP_S_EXCEPTION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_UP_S_P_CHNGNG  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_UP_S_P_EXPRTNG | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_UP_S_P_IMPRTNG | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_S_UP_S_P_RETRNG  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_TYPE_ATTRIBUTE   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_TYPE_DECLARATION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_TYPE_D_STR_CPNT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_TYPE_D_TAB_ROW   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_TYPE_PARAMETER   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_TYPE_P_CHANGING  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_TYPE_P_EXPORTING | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_TYPE_P_IMPORTING | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_AO_TYPE_P_RETURNING | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_RSLT_CARDNALTY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_BEHAVIOR  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_ACTION  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_ASC_CRT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_ASSOCTN | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_AUTH    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_A_DE_RF | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_A_PARAM | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_A_RSULT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_A_VA_RF | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_CHARA   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_CH_DOC  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_DETRMTN | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_ETAG    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_EVENT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_E_PARAM | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_FIELD   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_LOCK    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_MAPPING | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_STD_OP  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_B_VALIDTN | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_EXTENSN   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_E_ACT_EXT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_E_CHARA   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_E_GROUP   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_PRAGMA_T  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_SCLR_ENTY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_SD_EFFCTS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_SE_ACTION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_SE_AFFCTS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_SE_DT_ACT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_SE_EXE_ON | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_SE_FIELD  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_S_FO_SE_SELF   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_BDEF_TEMPLATE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CDS_CARDINALITY     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CDS_S_FO_ANNOTATION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CDS_S_FO_ANN_TARGET | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CDS_S_FO_ANN_VALUE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CDS_S_FO_ANN_V_BLDR | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_AMDP_DB_ENTITY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_DE_DEFINITN  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_DE_D_SECTION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_FO_DEFNTN    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_FO_D_C_MTHD  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_FO_D_C_M_AMD | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_FO_D_C_M_BI  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_FO_D_INTRFCE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_FO_D_SECTION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_FO_IMPLMTN   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_FO_I_METHOD  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_FO_I_M_AMDP  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_FO_LCL_CLASS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_FO_S_P_IMP   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_FO_S_P_I_BI  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_FO_TST_CLASS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_IN_DEFINITN  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_IN_D_SECTION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_UPDATE_IMP   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_UP_DEFINITN  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_UP_D_SC_C_MD | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_UP_D_SECTION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_CLAS_S_UP_IMPL_MTHD | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DCLS_S_FO_ROLE      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DCLS_S_FO_R_A_RULE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DCLS_S_FO_R_A_R_O_E | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DCLS_TEMPLATE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_DDL_EXPRESSION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_FIELD_TYPE     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_PARAM_DTYPE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_PRVDR_CNTRCT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_ASSOC     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_A_E       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_A_E_E     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_A_E_E_DS  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_COMPOS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_C_E       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_EXT_E     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_EXT_E_DS  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_FIELD     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_HIERARCHY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_H_DRCTRY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_H_SOB_FLD | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_H_SOURCE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_JOIN_T    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_J_INNER   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_J_LEFT_O  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_J_RIGHT_O | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_PARAM     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_P_VIEW    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_P_VIEW_DS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_TABLE_E   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_TABLE_F   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_UNION     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_VIEW      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_VIEW_DS   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_VIEW_E    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_VIEW_EXT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_VIEW_E_DS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_VIEW_E_E  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_V_EXT_DS  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_S_FO_V_E_E_DS  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLS_TEMPLATE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLX_S_FO_FIELD     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLX_S_FO_PARAMETER | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DDLX_TEMPLATE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DOMA_FORMAT         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DOMA_ORIGIN         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DOMA_S_CH_UP_FXD_VL | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DOMA_S_FO_FXD_VALS  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DOMA_S_FO_FXD_VALUE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DOMA_S_FO_OUTPT_CHR | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DRTY_STD_TYPE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DRTY_S_FO_SPL_TP_DF | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DRTY_S_FO_STD_CNSTN | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DRTY_S_FO_STD_ENUM  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DRTY_TEMPLATE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DTEL_DATA_TYPE      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DTEL_ORIGIN         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DTEL_S_CH_UP_FLD_LB | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_DTEL_S_FO_FLD_LBL   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_EVTB_S_CH_UP_EV_VN  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_EVTB_S_FO_EVNT_VRSN | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_FUGR_FM_PT_CHANGNG  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_FUGR_FM_PT_EXPRTNG  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_FUGR_FM_PT_IMPRTNG  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_FUGR_S_FO_FM_EXCPTN | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_FUGR_S_FO_FM_P_CHA  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_FUGR_S_FO_FM_P_EXP  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_FUGR_S_FO_FM_P_IMP  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_FUGR_S_FO_FNCTN_MDL | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_FUGR_S_UP_FNCTN_MDL | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_INTF_S_FO_C_METHOD  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_INTF_S_UP_C_METHOD  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_O_DELETE_RESULT     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_O_FINDING           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_O_FINDINGS          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_O_F_OBJECT          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_O_F_SECTION         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_O_F_SECTION_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_O_PATCH_RESULT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_O_POST_RESULT       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_O_PUT_RESULT        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_SCP1_O_POST_OBJECT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_SCP1_S_CH_I_CO      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_SCP1_S_CH_I_CO_UPDT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_SCP1_S_CH_I_ENT     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_SCP1_S_CH_U_CO      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_SCP1_S_CH_U_CO_DELT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_SCP1_S_CH_U_CO_INRT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_SCP1_S_CH_U_CO_UPDT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_SCP1_S_CH_U_ENT     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_SCP1_S_CH_U_ENT_DLT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_SCP1_S_CH_U_ENT_UPS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_SCP1_TEMPLATE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_SRVB_S_FO_SERVICE   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_SRVB_S_FO_SRV_VERSN | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_SRVD_PRVDR_CNTRCT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_SRVD_S_FO_EXPOSURE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_APS_ENH_CAT    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_APS_S_FO_CMPNT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_DBT_ENH_CAT    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_DBT_S_CH_UP_FL | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_DBT_S_CH_UP_IC | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_DBT_S_CH_U_F_U | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_DBT_S_FO_FIELD | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_DBT_S_FO_INCL  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_DBT_S_FO_INDEX | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_DBT_S_FO_TS_GP | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_FIELD_TYPE_APS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_FIELD_TYPE_DBT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_FIELD_TYPE_GTT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_FIELD_TYPE_STR | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_FKEY_CARDNALTY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_FKEY_CARD_LEFT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_FKEY_CARD_RGHT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_GTT_S_FO_FIELD | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_ORIGIN         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_STR_ENH_CAT    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_STR_S_CH_U_CMP | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_STR_S_CH_U_C_U | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_STR_S_CH_U_INC | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_STR_S_FO_CMPNT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_STR_S_FO_INCL  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_S_CH_U_CUR_QUN | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_S_CH_U_FRG_KEY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_S_CH_U_SCH_HLP | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_S_FO_CURR_QUAN | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_S_FO_FIELD     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_S_FO_FKEY      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_S_FO_GEODATA   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TABL_S_FO_SHELP     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GEN_TTYP_ROW_TYPE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GLOBAL_TEMPORARY_TABLE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GLOBAL_TEMPORARY_TABLES | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GTT_CONTENT             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GTT_FIELD               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GTT_FIELDS              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GTT_FIELDS_FACTORY      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GTT_FIELD_CONTENT       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GTT_FIELD_TYPE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GTT_FOREIGN_KEY         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GTT_FOREIGN_KEY_CONTENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GTT_SEARCH_HELP         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_GTT_SEARCH_HELP_CONTENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_HASH_ALGORITHM          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_I18N_ALO_TARGET_OBJECT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_I18N_ALO_TARGET_SUBOBJ  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_I18N_BCO_TARGET_OBJECT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_I18N_DD_ENT_TARGET      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_I18N_DD_FLD_TARGET      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_I18N_DD_PRM_TARGET      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_I18N_DE_TARGET_OBJECT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_I18N_DM_TARGET_FIXED_VA | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_I18N_MC_TARGET_MESSAGE  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_I18N_ME_ENT_TARGET      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_I18N_ME_FLD_TARGET      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_I18N_ME_PRM_TARGET      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_I18N_TEXT               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_I18N_TEXT_ATTRIBUTE     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_I18N_TP_TARGET_TXT_ELEM | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_I18N_TRANSLATION        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_I18N_TT_TARGET_RECORD   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_INTF_CACHEABLE_ORIGIN   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_INTF_COMPONENTS_FACTORY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_INTF_COMPONENT_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_INTF_CONTENT            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_INTF_C_METHOD           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_INTF_C_METHODS          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_INTF_C_METHODS_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_INTF_C_METHOD_CONTENT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_INTF_IMPLEMENTATIONS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_INTF_IMPLEMENTATIONS_FC | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_ITERATOR                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_JSON_TRANSFORMATION     | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_JSON_TREE_BUILDER       | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_JSON_TREE_VISITOR       | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_KU_BINARY_TXT_ENC_FCTRY | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_JSON_DATA            | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_JSON_DATA_BUILDER    | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_JSON_DATA_FACTORY    | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_JSON_TRNSFRMTN_FCTRY | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_REGEX_ENGINE_FACTORY | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_STD_CURRENT          | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_STD_SY               | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_STRING_COMPOSITION_F | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_STRING_DECOMPOSTN_F  | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_TENANT               | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_TM_DATE              | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_TM_DATE_FORMAT       | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_TM_FORMAT_FACTORY    | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_TM_MOMENT            | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_TM_MOMENT_FORMAT     | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_TM_TIME              | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_TM_TIME_FORMAT       | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_TM_TIME_ZONE_FACTORY | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_TM_UNIX_TIMESTAMP    | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_URL                  | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_KU_UUID_FORMAT_FACTORY  | \-                 | \-            | C1                   |                                | X                      | Released   |                            |
| IF_XCO_LANGUAGE                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_LANGUAGES               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_LANG_FORMAT             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_LES_CONTENT             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_LOGICAL_EXTERNAL_SCHEMA | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_LOGICAL_EXTERNAL_SCHEMS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_MC_CONTENT              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_MC_MESSAGE              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_MC_MESSAGES             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_MC_MESSAGES_FACTORY     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_MC_MESSAGE_CONTENT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_MESSAGE                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_MESSAGES                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_MESSAGE_CLASS           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_MESSAGE_CLASSES         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_MESSAGE_SHORT_TEXT      | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_METADATA_EXTENSION      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_METADATA_EXTENSIONS     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_NAME_CHOICE             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_NEWS                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_NONT_CACHEABLE_ORIGIN   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_NONT_CONTENT            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_NUMBER_RANGE_OBJECT     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_NUMBER_RANGE_OBJECTS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_PACKAGE                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_PACKAGES                | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_PAYLOAD                 | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_PKG_FILTER              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_PRINTABLE               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_RAP_BEHAVIOR_MESSAGE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_REGEX_APPLICATION       | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_REGEX_ENGINE            | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_REGULAR_EXPRESSION      | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_RONT_CACHEABLE_ORIGIN   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_RONT_CONTENT            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SAP_OBJECT_NODE_TYPE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SAP_OBJECT_NODE_TYPES   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SAP_OBJECT_TYPE         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SAP_OBJECT_TYPES        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SERVICE_BINDING         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SERVICE_BINDINGS        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SERVICE_BINDING_CONTENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SERVICE_CONSUMPTION_MDL | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SERVICE_CONSUMPTN_MDLS  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SERVICE_DEFINITION      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SERVICE_DEFINITIONS     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SOFTWARE_COMPONENT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVB_CACHEABLE_ORIGIN   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVB_OPERATION          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVB_SERVICE            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVB_SERVICES           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVB_SERVICES_FACTORY   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVB_SERVICE_VERSION    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVB_SERVICE_VERSIONS   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVB_SERVICE_VERSIONS_F | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVB_SERVICE_VERSION_CO | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVC_CACHEABLE_ORIGIN   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVC_CONTENT            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVC_REMOTE_FUNCTION    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVC_REMOTE_FUNCTIONS   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVC_REMOTE_FUNCTIONS_F | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVC_SERVICE_OPERATION  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVC_SERVICE_OPERATIONS | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVC_SERVICE_OPERATNS_F | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVC_SVC_ENTITY_SET     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVC_SVC_ENTITY_SETS    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVC_SVC_ENTITY_SETS_F  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVC_SVC_ENTITY_SET_CO  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVD_CACHEABLE_ORIGIN   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVD_CONTENT            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVD_EXPOSURE           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVD_EXPOSURES          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVD_EXPOSURES_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_SRVD_EXPOSURE_CONTENT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_STRING                  | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_STRINGS                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_STRING_BUILDER          | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_STRING_COMPOSITION      | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_STRING_DECOMPOSITION    | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_STRING_ITERABLE         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_STRING_ITERATOR         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_STRING_XSTRING_CNVRSN   | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_STR_COMPONENT           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_STR_COMPONENTS          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_STR_COMPONENTS_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_STR_COMPONENT_CONTENT   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_STR_COMPONENT_PR_FCTRY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_STR_COMPONENT_PR_FKFA   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_STR_COMPONENT_PR_FKFA_R | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_STR_COMPONENT_TYPE      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_STR_CONTENT             | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_STR_FOREIGN_KEY         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_STR_FOREIGN_KEY_CONTENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_STR_SEARCH_HELP         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_STR_SEARCH_HELP_CONTENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TAB_CACHEABLE_ORIGIN    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TAB_FIELD               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TAB_FIELD_CONTENT       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TAB_FOREIGN_KEY         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TAB_FOREIGN_KEY_CONTENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TAB_PSL_FKFA            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TAB_PSL_FKFA_RESULT     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TAB_PSL_FKFA_SCENARIO   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TAB_SEARCH_HELP         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TAB_SEARCH_HELP_CONTENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TEXT                    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TF_CONTENT              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TF_SOURCE_CODE          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TM_TIME_ZONE            | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_TRANSFORMATION          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TRANSFORMATIONS         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TRANSPORT_LAYER         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TRANSPORT_TARGET        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TR_ENTRY_FILTER         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TR_ENTRY_SOURCE         | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TR_FILTER               | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TR_RELEASE_OPTION       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TTYP_CONTENT            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TTYP_ROW_TYPE           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TT_PRIMARY_KEY          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TT_PRIMARY_KEY_FACTORY  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TT_SECONDARY_KEY        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_TT_SECONDARY_KEY_FACTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_UUID                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_UUID_FORMAT             | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_XLSX_DATA_VAL_TYPE      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_DAT_VAL_TYPE_F     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_DAT_VAL_TYPE_LIST  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_PATTERN_RECTANGULR | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_CELL            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_CELL_STREAM     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_CELL_VALUE      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_COLUMN          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_CS_OPERATION_FC | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_CS_OP_VISIT     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_CS_VISITOR      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_CURSOR          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_CURSOR_POSITION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_DATA_VALIDATION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_DOCUMENT        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_DVAL_TYPE_LIST  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_HL_LOCATION     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_HL_TARGET       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_HYPERLINK       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_MERGED_RANGE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_MERGED_RANGES   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_OPERATION       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_ROW_STREAM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_RS_OPERATION_FC | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_RS_OP_WRITE_TO  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_SELECTION       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_STYLE           | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_STYLE_ALIGNMENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_STYLE_BORDER    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_STYLE_BRDR_SIDE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_STYLE_FILL      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_STYLE_FONT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_STYL_PROTECTION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_VT_BEST_EFFORT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_VT_CELL_VALUE   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_VT_IDENTITY     | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_VT_ROW_VALUE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_VT_STRING_VALUE | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_WORKBOOK        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_WORKSHEET       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_WORKSHEETS      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_RA_WORKSHEET_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_SLC_PATTERN        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_SLC_PATTERN_BLDR   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_SLC_PB_SPL_FROM_TO | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_STYLE              | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_STYLE_FACTORY      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_CELL            | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_CELL_VALUE      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_COLUMN          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_CURSOR          | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_CURSOR_POSITION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_CURSOR_WIRING   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_DATA_VALIDATION | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_DOCUMENT        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_OPERATION       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_ROW_STREAM      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_RS_OPERATION_FC | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_RS_OP_WRITE_FRM | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_SELECTION       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_STYLEABLE       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_STYLE_ALIGNMENT | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_STYLE_BORDER    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_STYLE_FILL      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_STYLE_FONT      | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_STYLE_PROTECTN  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_VT_BEST_EFFORT  | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_VT_CELL_VALUE   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_VT_ROW_VALUE    | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_WORKBOOK        | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_WORKSHEET       | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_WORKSHEET_FCTRY | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XLSX_WA_WS_PROTECTION   | \-                 | \-            | C1                   | X                              |                        | Released   |                            |
| IF_XCO_XSTRING                 | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |
| IF_XCO_XSTRING_STRING_CNVRSN   | \-                 | \-            | C1                   | X                              | X                      | Released   |                            |

## IWSV - SAP Gateway Business Suite Enablement (Service)

| **Object**                     | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|--------------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| /UI5/ABAP_REPOSITORY_SRV 0001  | \-                 | \-            | C2                   |                                |                        | Released  |               |
| API_CDR_FILE_DOWNLOAD_SRV 0001 | \-                 | \-            | C2                   |                                |                        | Released  |               |
| API_CLOUD_PRINT_PULL_SRV 0001  | \-                 | \-            | C2                   |                                |                        | Released  |               |
| BC_EXT_APPJOB_MANAGEMENT 0002  | \-                 | \-            | C2                   |                                |                        | Released  |               |

## MSAG - Message Class

| **Object**  | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|-------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| ABAP_TIMEFM | \-                 | \-            | C1                   |                                | X                      | Released  |               |

## NONT - RESTful ABAP Programming Model: Object Node Type

| **Object**                    | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|-------------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| BUSINESSUSER                  | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| SAPGRAPHICALUIICONTEXT        | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| SAPGRAPHICALUSERINTERFACEICON | \-                 | \-            | C1                   | X                              | X                      | Released  |               |

## RONT - RESTful ABAP Programming Model: Object (Node) Type

| **Object**                    | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|-------------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| BUSINESSUSER                  | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| SAPGRAPHICALUSERINTERFACEICON | \-                 | \-            | C1                   | X                              | X                      | Released  |               |

## SUSO - Authorization Object

| **Object** | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| B_BUPA_ADR | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| B_BUPA_BNK | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| B_BUPA_GRP | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| B_BUPA_RLT | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| B_BUPR_BZT | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| B_BUP_DCPA | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| B_BUP_DCPD | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| B_BUP_PCPT | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| PLOG       | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| SDDLVIEW   | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| S_APPL_LOG | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| S_NUMBER   | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| S_SQL_PROC | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| S_SQL_TABL | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| S_SQL_VIEW | \-                 | \-            | C1                   | X                              |                        | Released  |               |
| S_TABU_NAM | \-                 | \-            | C1                   | X                              |                        | Released  |               |

## TABL - Table

| **Object**                   | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State**  | **Successor** |
|------------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|------------|---------------|
| /AIF/CHANGEABLE_FIELD_ST     | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| ABAPOFFLEN                   | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| ABAP_SORTORDER               | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ABP_BEHV_AUTHORIZATION       | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| ABP_BEHV_CHANGES             | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ABP_BEHV_FEATURES            | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| ABP_BEHV_GLOBAL_PERMISSIONS  | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| ABP_BEHV_LOCKS               | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ABP_BEHV_PAR_EDIT            | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ABP_BEHV_PERMISSIONS         | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ABP_BEHV_RESPONSE            | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| ABP_BEHV_RETRIEVALS          | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ACO_PROXY_TEXTID_TYPE        | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| ADDRESSPOST                  | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ADDRESS_1                    | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ADDRESS_2                    | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ADDRESS_3                    | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ADDRESS_DATA_S               | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ADDRESS_KEY_S                | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ADDRESS_ORGANIZATION_NAMES   | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ADDRESS_PERSON_NAMES         | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ADDRESS_PRINTFORM_LINE       | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ADDRESS_WORKPLACE_DETAILS    | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ADDR_DATA_S                  | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| ARCH_STAT                    | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| ARFCTID                      | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| AUTHFIELD_VALS               | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| AUTHORIZATION_FOR_OBJECT     | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| AUTHVALINTERVAL              | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| BADI_FILTER_BINDING          | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| BAL_S_LGNM                   | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| BAPIALA                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIALB                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIALC                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIALD                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIALF                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIALG                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIALT                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPICONVRS                   | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPICURR                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPICURX                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPICURX31                   | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIEXT                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIEXTA                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIEXTC                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIF4A                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIF4B                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIF4C                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIF4D                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIF4E                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIF4F                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIF4M                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIFLAG                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIHTML                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIINFO                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIMONCOM                   | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIMONIT                    | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIMONSTR                   | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIOBJID                    | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIPAREX                    | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIPAREX_HELP               | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIRANGES                   | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIRET1                     | \-                 | \-            | C1                   | X                              | X                      | Deprecated |               |
| BAPIRET2                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIRETC                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIRETI                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIRETS                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPIRETURN                   | \-                 | \-            | C1                   | X                              | X                      | Deprecated |               |
| BAPIRETURN1                  | \-                 | \-            | C1                   | X                              | X                      | Deprecated |               |
| BAPISHLP                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPISRCSYS                   | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPITA                       | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPITGA                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPITGB                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BAPI_STAND                   | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| BDWFAP_PAR                   | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| CDCHANGENR_RANGE             | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CFD_S_CALC_FIELDS_DRAFT_INFO | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| CMIS_S_ACE                   | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_ACL                   | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_ACL_CAPABILITIES      | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_ALLOWABLE_ACTIONS     | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_CAPABILITIES          | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_CHANGE_EVENT          | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_CHOICE                | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_CLIENT_PROPERTY       | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_CNT_DLVRY_NFO         | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_CONTENT_RAW           | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_CONTENT_STREAM        | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_DATE_TIME             | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_EXTENDED_FEATURES     | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_EXTENSION             | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_ID_AND_CHANGE_TOKEN   | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_IMPL_CAP              | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_KEY_VALUE             | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_KEY_VALUES            | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_OBJECT                | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_OBJECT_CONTAINER      | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_OBJECT_IN_FOLDER      | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_OBJECT_IN_FOLDER_LIST | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_OBJECT_LIST           | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_OBJECT_PARENT         | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_PERMISSION_DEFINITION | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_PERMISSION_MAPPING    | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_PRINCIPAL             | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_PROPERTIES            | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_PROPERTY              | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_PROPERTY_DEFINITION   | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_PROPERTY_VALUE        | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_QUERY_RESULT          | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_QUERY_RESULT_LIST     | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_RELATIONSHIP          | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_RENDITION             | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_REPOSITORY_INFO       | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_TYPE_CONTAINER        | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_TYPE_DEFINITION       | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_TYPE_LIST             | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_TYPE_MUTABILITY       | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| CMIS_S_TYPE_SET_ATTR         | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| COUNTRYTEXT_INFO_S           | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| FDT_BRS_S_TRACE_HEADER       | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| FDT_BRS_S_TRACE_RECORD       | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| IHTTPNVP                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| INCL_EEW_BUT000              | \-                 | \-            | C0                   | X                              |                        | Released   |               |
| INCL_EEW_BUT000              | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| LDBCB                        | \-                 | \-            | C1                   | X                              |                        | Deprecated |               |
| MATCH_RESULT                 | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| POSTAL_ADDRESS_DETAIL        | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| PRXCTRL                      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| PRXCTRLD                     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| QNAME                        | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| RCONT                        | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| RECEIVER_COUNTRY_INFO_S      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| REPL_RESULT                  | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| RHEAD                        | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| RSM_S_MESSAGE_CONTAINER      | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| SAPPDESTCLIENTNAME           | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| SCRL_S_AMOUNT                | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| SCRL_S_QUANTITY              | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| SCX_SRCPOS                   | \-                 | \-            | C1                   | X                              | X                      | Deprecated |               |
| SCX_T100KEY                  | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| SENDER_COUNTRY_INFO_S        | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| SFULLAPPDESTNAME             | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| SUBMATCH_RESULT              | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| SWF_PBL_AGENT                | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| SWF_PBL_SAP_OBJECT           | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| SWW_SONT_KEY                 | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| SXCO_S_AR_OBJECT_KEY         | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| SXCO_S_CDS_ANN_VAL_MEMBER    | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| SXCO_S_CDS_DS_PARAMETER      | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| SXCO_S_JSON_NAME_MAPPING     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| SXCO_S_TAB_INCLUDE           | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| SXSDDURATION                 | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| SXSLTEPAR                    | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| SYCH_BDL_DRAFT_ADMIN_INC     | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| SYMSG                        | \-                 | \-            | C1                   | X                              | X                      | Released   |               |
| SYST                         | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| T005N                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| T006                         | \-                 | \-            | C3                   |                                |                        | Released   |               |
| T006A                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| T006B                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| T006C                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| T006D                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| T006I                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| T006J                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| T006T                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| T006_OIB                     | \-                 | \-            | C3                   |                                |                        | Released   |               |
| TB009                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| TB019                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| TB025                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| TB027                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| TB028                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| TB032                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| TB910                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| TB912                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| TB914                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| TB916                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| TOASP                        | \-                 | \-            | C1                   |                                | X                      | Deprecated |               |
| TSA4C_CP_SVC_CONN_DETAILS    | \-                 | \-            | C1                   | X                              |                        | Released   |               |
| TSAD12                       | \-                 | \-            | C3                   |                                |                        | Released   |               |
| TSAD9                        | \-                 | \-            | C3                   |                                |                        | Released   |               |
| UT8STRLIN                    | \-                 | \-            | C1                   |                                | X                      | Released   |               |
| UTF8STR_RC                   | \-                 | \-            | C1                   |                                | X                      | Released   |               |

## TTYP - Table Type

| **Object**                     | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State**  | **Successor**      |
|--------------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|------------|--------------------|
| /AIF/CHANGEABLE_FIELD_TT       | \-                 | \-            | C1                   |                                | X                      | Released   |                    |
| ABAPOFFLENTAB                  | \-                 | \-            | C1                   |                                | X                      | Released   |                    |
| ABAP_SORTORDER_TAB             | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| ABP_BEHV_AUTHORIZATION_TAB     | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| ABP_BEHV_CHANGES_TAB           | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| ABP_BEHV_FEATURES_TAB          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| ABP_BEHV_GLOBAL_PERMISSION_TAB | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| ABP_BEHV_LOCKS_TAB             | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| ABP_BEHV_PERMISSIONS_TAB       | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| ABP_BEHV_RELATING_TAB          | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| ABP_BEHV_RESPONSE_TAB          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| ABP_BEHV_RETRIEVALS_TAB        | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| ABP_ENTITY_NAME_TAB            | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| ABP_FIELD_NAME_TAB             | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| ADDRESS_PRINTFORM_TABLE        | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| ADDR_DATA_TT                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| AUTHORIZATION                  | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| AUTHORIZATION_TAB              | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| AUTHVALINTERVAL_TAB            | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| BADI_FILTER_BINDINGS           | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| BAL_T_LGNM                     | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| BAPIMONLST                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| BAPIPAREXTAB                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| BAPIRETCT                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| BAPIRETM                       | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| BAPIRETTAB                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| CFD_T_CALC_FIELDS_DRAFT_INFO   | \-                 | \-            | C1                   |                                | X                      | Released   |                    |
| CMIS_T_ACE                     | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_BOOLEAN                 | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_CHOICE                  | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_CLIENT_PROPERTY         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_DATE_TIME               | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_DECIMAL                 | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_ENUM                    | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_EXTENDED_FEATURES       | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_EXTENSION               | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_ID                      | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_ID_AND_CHANGE_TOKEN     | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_KEY_VALUES              | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_LONG                    | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_MAP                     | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_OBJECT                  | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_OBJECT_CONTAINER        | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_OBJECT_IN_FOLDER        | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_OBJECT_PARENT           | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_PERMISSION_DEFINITION   | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_PERMISSION_MAPPING      | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_PROPERTY                | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_PROPERTY_DEFINITION     | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_PROPERTY_VALUE          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_QUERY_RESULT            | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_RELATIONSHIP            | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_RENDITION               | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_REPOSITORY_INFO         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_STRING                  | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_TYPE_CONTAINER          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| CMIS_T_TYPE_DEFINITION         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| FDT_BRS_T_TRACE_HEADER         | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| FDT_BRS_T_TRACE_RECORD         | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| HTTP_STATUS_CODES              | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| LDBCB_TT                       | \-                 | \-            | C1                   | X                              |                        | Deprecated |                    |
| MATCH_RESULT_TAB               | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| PRXCTRLDTAB                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| PRXCTRLTAB                     | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| REPL_RESULT_TAB                | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| ROLE_AUTHORIZATIONS            | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| RSM_T_MESSAGE_CONTAINER        | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| STRINGTAB                      | \-                 | \-            | C1                   | X                              |                        | Deprecated | TTYP STRING_TABLE  |
| STRING_HASHED_TABLE            | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| STRING_TABLE                   | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| SUBMATCH_RESULT_TAB            | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| SWF_CPWF_CONSUMER_T            | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_ACCESS_CONTROLS         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AD_DATA_ELEMENTS        | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AD_FIELD_NAMES          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AD_STRUCTURES           | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AD_TABLES               | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AD_TABLE_TYPES          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AMDP_DB_ENTITIES        | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AMDP_DB_OPTIONS         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AO_CLASSES              | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AO_C_ALIASES            | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AO_C_CLASS_DATAS        | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AO_C_CONSTANTS          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AO_C_DATAS              | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AO_C_TYPES              | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AO_INTERFACES           | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AO_OBJECT_NAMES         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AO_SUBCOMPONENT_NAMES   | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AO_S_EXCEPTIONS         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AO_S_PARAMETERS         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AO_S_P_CHANGINGS        | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AO_S_P_EXPORTINGS       | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AO_S_P_IMPORTINGS       | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AO_S_P_RETURNINGS       | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_APLO_OBJ_TEXTS          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_APLO_OBJ_TEXT_ATTRIBTS  | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_APLO_SUBOBJECTS         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_APLO_SUBOBJ_TEXTS       | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_APLO_SUBOBJ_TXT_ATTRBTS | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_APPEND_STRUCTURES       | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_APPLICATION_LOG_OBJECTS | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_APS_COMPONENTS          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_ARS_VISIBILITIES        | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AR_FILTERS              | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AR_OBJECTS              | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_AR_OBJECT_KEY           | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_ASQL_CONSTRAINTS        | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_BAL_LOG_FILTERS         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_BAL_LOG_HANDLES         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_BCO_TEXTS               | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_BCO_TEXT_ATTRIBUTES     | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_BDEF_TRIGGER_OPERATIONS | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_BEHAVIOR_DEFINITIONS    | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_BUSINESS_CNFGRTN_OBJCTS | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CDS_ANNOTATIONS         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CDS_ANN_FILTERS         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CDS_ANN_VALUES          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CDS_ANN_VAL_MEMBER      | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CDS_ASSOCIATIONS        | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CDS_COMPOSITIONS        | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CDS_DS_PARAMETER        | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CDS_ENTITIES            | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CDS_FIELDS              | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CDS_FIELD_NAMES         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CDS_OBJECT_NAMES        | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CDS_PARAMETERS          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CDS_PARAMETER_NAMES     | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CDS_UNIONS              | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CLAS_C_METHODS          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CLAS_METHOD_NAMES       | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CP_BAL_EXC_ADDITIONS    | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CP_BAL_LOGS             | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CP_BAL_LOG_EXCEPTIONS   | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CP_BAL_LOG_MESSAGES     | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CP_GEN_D_O_PUT_OPTIONS  | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CP_TRANSPORTS           | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CP_TR_ENTRIES           | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CP_TR_KEY_ENTRIES       | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CP_TR_KE_TK_COMPONENTS  | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CP_TR_OBJECT_ENTRIES    | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CP_TR_R3TR_OBJECT_ENTRS | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CP_TR_R3TR_TABU_OBJ_ENS | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_CP_TR_TASKS             | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_DATABASE_TABLES         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_DATA_DEFINITIONS        | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_DBT_FIELDS              | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_DCL_EXPRESSIONS         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_DDEF_ENT_TEXTS          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_DDEF_ENT_TEXT_ATTRIBUTS | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_DDEF_FLD_TEXTS          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_DDEF_FLD_TEXT_ATTRIBUTS | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_DDEF_PRM_TEXTS          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_DDEF_PRM_TEXT_ATTRIBUTS | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_DOMAINS                 | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_DOMAIN_FIXED_VALUES     | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_DOMAIN_TEXTS            | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_DOMAIN_TEXT_ATTRIBUTES  | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_DTEL_TEXTS              | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_DTEL_TEXT_ATTRIBUTES    | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_FM_EXCEPTIONS           | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_FM_EXCEPTION_NAMES      | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_FM_NAMES                | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_FM_PARAMETER_NAMES      | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_FM_PRMS_CHANGING        | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_FM_PRMS_EXPORTING       | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_FM_PRMS_IMPORTING       | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_FUNCTION_GROUPS         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_FUNCTION_MODULES        | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_GEN_CLAS_AMDP_DB_ENTS   | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_GEN_DDLS_DDL_EXPRS      | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_GEN_O_FINDINGS          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_GLOBAL_TEMPORARY_TABLES | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_GTT_FIELDS              | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_I18N_TEXTS              | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_I18N_TRANSLATIONS       | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_INTF_C_METHODS          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_JSON_NAME_MAPPING       | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| SXCO_T_JSON_TRANSFORMATIONS    | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| SXCO_T_LANGUAGES               | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_MC_MESSAGES             | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_MC_TEXTS                | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_MC_TEXT_ATTRIBUTES      | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_MESSAGES                | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| SXCO_T_MESSAGE_CLASSES         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_METADATA_EXTENSIONS     | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_ME_ENT_TEXTS            | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_ME_ENT_TEXT_ATTRIBUTES  | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_ME_FLD_TEXTS            | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_ME_FLD_TEXT_ATTRIBUTES  | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_ME_PRM_TEXTS            | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_ME_PRM_TEXT_ATTRIBUTES  | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_PACKAGES                | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_SERVICE_BINDINGS        | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_SERVICE_DEFINITIONS     | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_SRVB_SERVICES           | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_SRVB_SERVICE_VERSIONS   | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_SRVD_EXPOSURES          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_SRVD_OBJECT_NAMES       | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_STR_COMPONENTS          | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_TAB_FIELDS              | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_TAB_INCLUDE             | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_TP_TEXTS                | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_TP_TEXT_ATTRIBUTES      | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_TRANSFORMATIONS         | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_TR_ENTRY_FILTERS        | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_TR_FILTERS              | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_TT_KEY_COMPONENTS       | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXCO_T_TT_SECONDARY_KEYS       | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SXSLTEPARS                     | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| SYMSG_TAB                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| TAPPDESTCLIENTNAME             | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| TAPPDESTPROPERTY               | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| TFULLAPPDESTNAME               | \-                 | \-            | C1                   | X                              |                        | Released   |                    |
| TIHTTPNVP                      | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| TIHTTPURLS2                    | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |
| UTF8STRTAB                     | \-                 | \-            | C1                   |                                | X                      | Released   |                    |
| XSTRINGTAB                     | \-                 | \-            | C1                   | X                              |                        | Deprecated | TTYP XSTRING_TABLE |
| XSTRING_TABLE                  | \-                 | \-            | C1                   | X                              | X                      | Released   |                    |

## TYPE - Type Group

| **Object** | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| ABAP       | \-                 | \-            | C1                   | X                              | X                      | Released  |               |

## VIEW - View

| **Object**       | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| SMAIL_VM_DF_ADDR | \-                 | \-            | C3                   |                                |                        | Released  |               |
| SMAIL_VM_RCV_DOM | \-                 | \-            | C3                   |                                |                        | Released  |               |
| SMAIL_VM_SND_DOM | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_BUT_AUGRP_BLK  | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_T005O          | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_T005S          | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_T005_BAS       | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_T006D          | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_T006I          | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_TB001          | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_TB004          | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_TB005          | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_TB008S         | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_TB008U         | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_TB037          | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_TCURF          | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_TCURN          | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_TCURR          | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_TCURV          | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_TSAD2          | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_TSAD3          | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_TSAD4          | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_TSAD5          | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_TSADVC_CLIDEP  | \-                 | \-            | C3                   |                                |                        | Released  |               |
| V_TZONEBAS       | \-                 | \-            | C3                   |                                |                        | Released  |               |

## WAPA - BSP (Business Server Pages) Application

| **Object**     | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|----------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| NW_APS_APJ_USR | \-                 | \-            | C0                   | X                              |                        | Released  |               |
| NW_APS_APL     | \-                 | \-            | C0                   | X                              |                        | Released  |               |

## WDCA - Web Dynpro Application Configuration

| **Object**                      | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|---------------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| FPM_DEMO_PLAYER_1 02            | \-                 | \-            | C0                   |                                | X                      | Released  |               |
| FPM_DEMO_PLAYER_CBA 02          | \-                 | \-            | C0                   |                                | X                      | Released  |               |
| FPM_TEST_CBA_WIRING_OVP\_ 02    | \-                 | \-            | C0                   |                                | X                      | Released  |               |
| FPM_TEST_SEARCH_E_ATS_RES_AC 02 | \-                 | \-            | C0                   |                                | X                      | Released  |               |
| S_EPM_FPM_PO_ATO 02             | \-                 | \-            | C0                   |                                | X                      | Released  |               |
| S_EPM_FPM_PO_ATO_MOBILE 02      | \-                 | \-            | C0                   |                                | X                      | Released  |               |
| WD_CONFIGURATION_OVERVIEW 02    | \-                 | \-            | C0                   |                                | X                      | Released  |               |

## WDYA - Web Dynpro Application

| **Object**                | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|---------------------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| SALV_WD_TEST_TABLE_SIMPLE | \-                 | \-            | C0                   |                                | X                      | Released  |               |
| WDR_TEST_C_TABLE          | \-                 | \-            | C0                   |                                | X                      | Released  |               |
| WDR_TEST_VALUE_SUGGEST    | \-                 | \-            | C0                   |                                | X                      | Released  |               |

## XSLT - Transformation

| **Object** | **Subobject Type** | **Subobject** | **Release Contract** | **ABAP for Cloud development** | **ABAP for Key Users** | **State** | **Successor** |
|------------|--------------------|---------------|----------------------|--------------------------------|------------------------|-----------|---------------|
| ID         | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
| ID_INDENT  | \-                 | \-            | C1                   | X                              | X                      | Released  |               |
