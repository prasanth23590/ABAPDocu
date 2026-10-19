---
title: "asJSON - Instances of Classes"
source_file: abenabap_asjson_class_instances.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON > JSON - Transformations > asJSON - Canonical JSON Representation > asJSON - Mapping of ABAP Data Types > asJSON - Mapping of Reference Variables and Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asJSON - Instances of Classes

To transform classes to [JSON](../../abap-glossary/abenjson_glosry.md) using the statement [`CALL TRANSFORMATION`](abapcall_transformation.md) or to create classes from JSON data, their classes must implement the interface `IF_SERIALIZABLE_OBJECT`. The instance of a class (object) is represented as an object component of the object `%heap` as follows:

``` abap
"key":{ "%type":"class", 
        "%val":{ "part":{ "%classVersion":"...", 
                          "name":... 
                          ... 
                        } 
                 ... 
               } 
      }
```

The name `key` is the key used to reference the object. The value of `key` is itself an object whose object components represent the class and the attributes of the referenced ABAP object.

- The character-like value *class* of the component `%TYPE` specifies the class of the object. The same applies to `class` as to the element name `class` in [asXML](abenasxml_class_instances.md) representation. In asJSON, the namespace that specifies where the class is defined in asXML is resolved before the class name.

- The component `%VAL` represents the attribute values of the object. The value of `%VAL` is itself an object. The components `part` are objects that contain the values of the instance attributes of individual object parts. The same applies to the object parts and their names `part` as to the subelements `<part>` in [asXML](abenasxml_class_instances.md) representation.

- The components of an object part `part` represent the values of the instance attributes of the objects in their canonical representation under their names. The same applies to the names as to the corresponding elements in [asXML](abenasxml_class_instances.md) representation. Static attributes are ignored.

- An optional component, `%classVersion`, of an object part, `part`, contains the version of the class of the object part in character-like representation. The same applies to the version of the class as to the attribute `classVersion` in [asXML](abenasxml_class_instances.md) representation.

The [tag interface](../../abap-glossary/abentag_interface_glosry.md) `IF_SERIALIZABLE_OBJECT` has the same meaning for JSON as for [asXML](abenasxml_class_instances.md). This means it defines which attributes of a class are serialized. In addition, helper methods can be implemented that adjust behavior (see the [example](abenserializable_object_abexa.md)).

## Executable Example

[asJSON for Object References](abenabap_json_asjson_oref_abexa.md)
