---
title: "Byte Order"
source_file: abenbyteorder.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Byte Order

The byte order determines the order in which bytes of specific data objects are stored in the memory.

## Binary Representation of Numbers

The binary representation of numbers with the ABAP type `i`, `int8`, `decfloat16`, `decfloat34`, `f`, and `s` is hardware-dependent. An important part of this is the **byte order**, which is predefined by the processor of the [host computer](../../abap-glossary/abenhost_computer_glosry.md) on the current [AS instance](../../abap-glossary/abenas_instance_glosry.md), is important: It determines whether the highest-value byte or lowest-value byte is stored first in the memory. In the case of the highest-value byte, the binary representation is referred to as [big endian](../../abap-glossary/abenbig_endian_glosry.md) and in the latter case, the representation is known as [little endian](../../abap-glossary/abenlittle_endian_glosry.md).

### Hint

The byte order of the [host computer](../../abap-glossary/abenhost_computer_glosry.md) of the current [AS instance](../../abap-glossary/abenas_instance_glosry.md) can be taken from the static attribute `ENDIAN` in the [system class](../../abap-glossary/abensystem_class_glosry.md) [`CL_ABAP_CHAR_UTILITIES`](../abap-processing-internal-data/abencl_abap_char_utilities.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The number 16909060 in hexadecimal notation can be represented by the following byte strings:

| **Endian** | **Byte 1** | **Byte 2** | **Byte 3** | **Byte 4** |
|------------|------------|------------|------------|------------|
| Big        | *0x01*     | *0x02*     | *0x03*     | *0x04*     |
| Little     | *0x04*     | *0x03*     | *0x02*     | *0x01*     |

The most common processors that use little endian representations are Intel and `DEC` Alpha. Most other processors use big endian.

## Binary Representation of Characters

Characters are represented by unsigned 2-byte integer values in the [Unicode](../../abap-glossary/abenunicode_glosry.md) format [UCS-2](../../abap-glossary/abenucs2_glosry.md), which is supported by the ABAP programming language. This means that this format depends on the number representation used by the hardware. A distinction is therefore made between UCS-2BE (big endian) and UCS-2LE (little endian).

## Container Problems

Character-like or byte-like data objects of the type `c` or `string`, or `x` or `xstring`, are often used as anonymous containers for data objects, in particular structures, and stored persistently.

If such a container is stored and imported from an [AS instance](../../abap-glossary/abenas_instance_glosry.md) whose [host computer](../../abap-glossary/abenhost_computer_glosry.md) has a different byte order, problems can occur if the container is used for content for which the byte order is critical. This is always the case when numeric content of the type `i`, `int8`, `decfloat16`, `decfloat34`, `f`, or `s` is stored in character-like or byte-like containers. Problems can also arise when byte-like content is stored in character-like containers.

Usually, in order to be able to work with the content of an imported container, a [casting](../../abap-glossary/abencast_casting_glosry.md) is performed on the data type whose data is stored in the container. However, because no type information is stored in the container, any necessary conversion of the byte order cannot take place.

The only way to prevent these problems is to avoid having numeric components in anonymous containers and never store byte-like content in character-like fields.

### Hint

The statement [`EXPORT`](../abap-data-cluster/abapexport_data_cluster.md) ... TO [`DATA BUFFER`](../abap-data-cluster/abapexport_data_cluster_medium.md) can be used to store ABAP data in byte strings. When the statement [`IMPORT`](../abap-data-cluster/abapimport_data_cluster.md) is used, the byte order is handled automatically.
