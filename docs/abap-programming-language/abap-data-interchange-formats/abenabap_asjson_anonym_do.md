---
title: "asJSON - Anonymous Data Objects"
source_file: abenabap_asjson_anonym_do.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Transformations > asJSON - Canonical JSON Representation > asJSON - Mapping of ABAP Data Types > asJSON - Mapping of Reference Variables and Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asJSON - Anonymous Data Objects

An anonymous data object, that is, a data object created using `CREATE DATA` or the instance operator `NEW`, is represented as an object component of `%heap` in the form:

``` abap
"key":{ "%type":"...", 
        "%maxLength":..., 
        "%totalDigits":..., 
        "%fractionDigits":..., 
        "%val":... 
      }
```

The name `key` is the key used to reference the anonymous data object. The value of `key` is itself an object whose object components represent the type and the value of the anonymous data object.

The value of the anonymous data object is specified as content of the component `%val` in its canonical representation. If the anonymous data object itself is a non-initial reference variable, it references another component of `%heap`.

The remaining components specify the data type of the anonymous data object.

- The same rules apply to the content of `%type` as to the element name `type` in [asXML](abenasxml_anonymous_data_object.md).

- The components `%maxLength`, `%totalDigits`, and `%fractionDigits` specify the technical properties of the type, if required. The same rules apply to their content as to the corresponding attributes in [asXML](abenasxml_anonymous_data_object.md).

## Executable Example

[asJSON for Anonymous Data Objects](abenabap_json_asjson_dref_abexa.md).
