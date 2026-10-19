---
title: "Sessions and Memory Areas"
source_file: abenmemory_organization.html
section: "ABAP Programming Language > ABAP - Overview > ABAP Programs on the AS ABAP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Sessions and Memory Areas

This section describes the sessions of an AS ABAP in which ABAP programs are executed and the associated memory areas that can be accessed by an ABAP program. For a more general and technically more detailed description, see the documentation [Memory Management](https://help.sap.com/docs/ABAP_PLATFORM_NEW/f146e75588924fa4987b6c8f1a7a8c7e/49325d4ee93934ffe10000000a421937) in SAP Help Portal.

The following figure shows the general organization of sessions for ABAP programs and their memory areas up to the [internal session](../../abap-glossary/abeninternal_session_glosry.md) level: ![figure](images_abdoc_memory1.gif)

- [AS instance](abenmemory_organization.md#as-instance)

- [User Session](abenmemory_organization.md#user-session)

- [ABAP Session](abenmemory_organization.md#abap-session)

- [Internal Session](abenmemory_organization.md#internal-session)

## AS instance

An [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) can be distributed across multiple [AS instances](../../abap-glossary/abenas_instance_glosry.md). If an AS ABAP is implemented using multiple AS instances, they are usually instantiated on different [host computers](../../abap-glossary/abenhost_computer_glosry.md), which do not have to have the same operating system. However, multiple AS instances of one or more AS ABAP can also be instantiated on the same host computer. AS instances communicate with the [presentation layer](../../abap-glossary/abenpresentation_layer_glosry.md), the [database layer](../../abap-glossary/abendatabase_layer_glosry.md), and with each other using the message server. The most important components of an AS instance are its [work processes](../../abap-glossary/abenwork_process_glosry.md), the number and [type](../../abap-glossary/abentype_glosry.md) of which are determined when the AS ABAP is started. An [ABAP program](../../abap-glossary/abenabap_program_glosry.md) is executed by a suitable AS instance work process.

The transaction `SM51` shows an overview of the AS instances of the current AS ABAP and on which host computers they are instantiated. The name of the current AS instance can be determined in an ABAP Program using the method `GET_INSTANCE_NAME` of the system class `CL_ABAP_SYST`. This name has the form `hostname_sysid_instnr`. Here, `hostname` is the name of the host computer of the AS instance, `sysid` is the name of the AS ABAP, and `instnr` is the instance number of the AS instance. The network name of the host computer on which the current AS instance is instantiated can be found in the [system field](../../abap-glossary/abensystem_field_glosry.md) `sy-host`.

Every AS instance has access to the [standard database](../../abap-glossary/abenstandard_db_glosry.md) of the AS ABAP. Every AS instance has its own [shared memory](../../abap-glossary/abenshared_memory_glosry.md). The ABAP runtime framework uses the shared memory for programs, program data, and buffers (for example, during [table buffering](../../abap-glossary/abentable_buffering_glosry.md)). ABAP programs can store shared objects and [data clusters](../../abap-glossary/abendata_cluster_glosry.md) in the shared memory.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Gets the name of the current AS instance.

``` abap
cl_demo_output=>display( cl_abap_syst=>get_instance_name( ) ).
```

## User Session

Logging on to an AS instance opens a [user session](../../abap-glossary/abenuser_session_glosry.md). Logons take place using SAP GUI, the RFC interface, or ICF (including APC). A user session is assigned a separate memory area, the user memory, which can be used as follows in ABAP programs:

- The user memory stores SPA/GPA parameters that can be accessed using the statements `SET PARAMETER` and `GET PARAMETER`.

- The ABAP Daemon Memory is a subarea of the user memory in which ABAP daemons can store context information in PCP format.

The maximum number of user sessions is determined by the profile parameter `rdisp/tm_max_no`. The profile parameter `rdisp/server_resource/user_sessions` determines which percentage of the sessions can be opened using the RFC interface.

For more information, see User Sessions.

## ABAP Session

An [ABAP session](../../abap-glossary/abenabap_session_glosry.md) is opened for each user session. Each ABAP session is assigned its own memory area ABAP memory, in which [data clusters](../../abap-glossary/abendata_cluster_glosry.md) can be stored. The programs of a call sequence share access to these clusters and the data is retained for as long as the top level transaction of the call sequence remains. The SAP Easy Access program does not work as a top level transaction for the ABAP memory.

Additional ABAP sessions for a user session can be opened as follows:

- Enter a transaction code after */o* in the command field in the toolbar.

- Call the function module `TH_CREATE_MODE`.

- Call a dynpro during the processing of asynchronous RFC. In the RFC client, an additional ABAP session for communication with the SAP GUI is required.

A maximum of 16 ABAP sessions are possible per user session. The number of sessions that is actually possible for a system is determined by the profile parameter `rdisp/max_alt_modes`, whose default value is 16.

## Internal Session

Each call of an ABAP program creates a new internal session, in which the called program is loaded.

An internal session contains a [session memory](../../abap-glossary/abenroll_area_glosry.md) that is divided into the areas [heap](../../abap-glossary/abenheap_glosry.md) and [stack](../../abap-glossary/abenstack_glosry.md) from the perspective of an ABAP program. The modifiable [objects](../../abap-glossary/abenobject_glosry.md) of the program live there. The non-modifiable data of the program is stored in the [PXA](../../abap-glossary/abenpxa_glosry.md). The session memory contains references to the required data in the PXA. From a technical perspective, the session memory and the global PXA are stored in the shared memory of the AS instance where they are managed by the SAP Memory Management.

In an ABAP session, there can be a maximum of nine internal sessions that always belong to a call sequence. Data from the ABAP memory is always assigned to a call sequence.

On 64-bit platforms, an internal session can theoretically require up to 4 TB of memory. The practical upper limit is usually below the theoretical limit, since the actual physically installed main memory is the maximum available and divided up among all users.

Further information about the way ABAP programs are organized in an internal session can be found in Programs in the Internal Session.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Usage of `CL_SESSION_INFO`.

``` abap
TRY. 
    FINAL(session_info) = NEW cl_session_info( )->get_info( ). 
  CATCH cx_ssi_exception. 
    ... 
ENDTRY.
```
