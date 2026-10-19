---
title: "asJSON - General Format"
source_file: abenabap_asjson_general.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Transformations > asJSON - Canonical JSON Representation"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asJSON - General Format

The following lines show the general format of the [canonical JSON representation](../../abap-glossary/abencanonical_json_represen_glosry.md). Any line breaks and indents are included for clarification purposes only.

``` abap
{ 
  "bn1":... 
  "bn2":... 
   ... 
  "%heap":{...} 
}
```

The top level contains the object `{ }`. The object components with the names `bn1`, `bn2` ... represent the ABAP data objects specified in the addition `source` of the statement [`CALL TRANSFORMATION`](abapcall_transformation.md) as `e1` `e2` ... or in the addition `result` as `f1` `f2` ... The names of the object components `bn1`, `bn2`, ... are the names specified there in uppercase.

The values of the object components represent the content of named data object in accordance with the type-dependent mapping described in the following sections. Here, reference variables are always represented as object components whose content is objects that reference the content of referenced anonymous data objects and instances of classes in an optional object component `%heap` of the top object.

The same rules apply to the names of the object components `bn1`, `bn2` ... as in [asXML](abenabap_xslt_asxml_general.md) and replacements can be made as defined the table specified there.

## Executable Example

[asJSON, General Format](abenabap_hello_json_abexa.md)
