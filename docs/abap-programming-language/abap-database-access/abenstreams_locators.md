---
title: "ABAP SQL - Streaming and Locators"
source_file: abenstreams_locators.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Streaming and Locators

In ABAP SQL, [data streams](../../abap-glossary/abendata_stream_glosry.md) and [locators](../../abap-glossary/abenlocator_glosry.md) can be used to access [LOBs](../../abap-glossary/abenlob_glosry.md). LOBs are fields in data sources of type [`STRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`RAWSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or SQL expressions that return one of these data types, for example, [type conversion functions](abenabap_sql_conversion_functions.md). The associated objects are grouped together under the term [LOB handles](../../abap-glossary/abenlob_handle_glosry.md). While a locator is always an LOB handle, there can also be data streams for other resources (see [Streaming](../abap-processing-internal-data/abenstreaming.md)).

For regular access to LOBs, ABAP data objects of the types `string` and `xstring` are used, to which the entire LOB is passed in the case of reads and from which the entire LOB is taken in the case of writes. Data streams and locators, however, work as follows:

- For reads, [reader streams](../../abap-glossary/abenreader_stream_glosry.md) can be linked with LOBs using the assignment of corresponding reference variables. The same applies to writes and [writer streams](../../abap-glossary/abenwriter_stream_glosry.md). LOB data can be processed in portions using the methods of the streams. This has the benefit that LOBs do not have to be completely realized in the ABAP program.

- In the case of reads and writes, locators can be linked with LOBs by assigning corresponding reference variables. Using the methods of the locators, the substrings of LOBs or the properties of LOBs can be accessed without requiring a complete realization in the ABAP program. Furthermore, locators enable the copying of LOBs within the database without having to transport the data between the database and the AS ABAP.

The use of data streams and locators for LOBs in DDIC database tables can improve performance with respect to the program runtime, by omitting unnecessary data transports. There are, however, also some disadvantages:

- The use of locators leads to higher resource consumption in the database system. Locators are not yet supported by all databases. In this case, they must be emulated from the database interface on AS ABAP.

- The use of data streams does not lead to increased resource consumption in the database system, but data streams are somewhat more limited in their use. In particular, data streams cannot be used if internal tables are used in the ABAP SQL statements.

The following sections introduce the classes for data streams and locators as well as the interfaces they include for general LOB handles.

- [Streaming](abenabap_sql_streaming.md)

- [Locators](abenlocators.md)

- [LOB Interfaces](abenlob_interfaces.md)

## Hint

A maximum of 1000 LOB handles can be open in a [database LUW](../../abap-glossary/abendatabase_luw_glosry.md).
