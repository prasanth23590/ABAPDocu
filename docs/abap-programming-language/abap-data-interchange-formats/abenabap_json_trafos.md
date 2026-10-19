---
title: "JSON - Transformations"
source_file: abenabap_json_trafos.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON - Transformations

The [transformations for XML](abenabap_xml_trafos.md) that can be called from ABAP, namely [XSL transformations](../../abap-glossary/abenxsl_transformation_glosry.md) and [simple transformations](../../abap-glossary/abensimple_transformation_glosry.md), can also be used for [JSON](../../abap-glossary/abenjson_glosry.md).

- To call a transformation for JSON data as a source, the following JSON sources can be specified in the statement [`CALL TRANSFORMATION`](abapcall_transformation.md):

  - A string or internal table with [JSON data](abenjson_oview.md) in character-like or byte-like representation.

  - A [JSON Reader](abenabap_json_lib_reader.md).

- To call a transformation for JSON data as a source, the following XML sources can be specified in the statement [`CALL TRANSFORMATION`](abapcall_transformation.md):

  - A string or internal table with [JSON data](abenjson_oview.md) in character-like or byte-like representation.

  - A [JSON Reader](../../abap-glossary/abenjson_reader_glosry.md).

    A JSON reader returns data in the [JSON XML](../../abap-glossary/abenjson_xml_glosry.md) format. The JSON data specified as a string or in an internal table is also handled like XML representing JSON data [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) format.

- To call a transformation for JSON data as a target, a [JSON writer](abenabap_json_lib_writer.md) can be specified as a JSON target in the statement [`CALL TRANSFORMATION`](abapcall_transformation.md).

- To call a transformation for JSON data as a target, a [JSON writer](../../abap-glossary/abenjson_writer_glosry.md) can be specified as an XML target in the statement [`CALL TRANSFORMATION`](abapcall_transformation.md): A JSON writer expects data in [JSON-XML](../../abap-glossary/abenjson_xml_glosry.md) format.

Any XSLT programs and ST programs can be called that can handle JSON-XML:

- If the source is JSON data, the transformation must process JSON-XML as its input.

- If the target is JSON data, the transformation must create JSON-XML.

User-defined transformations must be programmed accordingly. The [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID` is handled appropriately internally.

- [Self-Written Transformations](abenabap_json_trafos_self.md)

- [Identity Transformation](abenabap_json_trafo_id.md)
