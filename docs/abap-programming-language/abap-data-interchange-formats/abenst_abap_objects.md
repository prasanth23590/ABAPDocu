---
title: "ST - Access to ABAP Objects from ST"
source_file: abenst_abap_objects.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Access to ABAP Objects from ST

Classes and objects in ABAP Objects can be accessed as follows in ST programs:

- [`tt:call-method`, call static methods](abenst_tt_call-method_static.md)

- [`tt:call-method`, call instance methods](abenst_tt_call-method_instance.md)

- [`tt:create-object`, create objects](abenst_tt_create.md)

Data roots, parameters, and variables can all be bound to the interface parameters at the same time.

The call of methods also allows access to the current XML stream.

- [`tt:call-method`, `writer`, `reader`](abenst_tt_call-method_writerreader.md)

## Hint

When binding data nodes, it must be noted that the content of a data root cannot be modified in serializations and only writes can be performed on a data root in deserializations. This places a strong restriction on the use of data nodes as actual parameters. Since parameters and attributes for general use cannot be serialized or deserialized, unless they contain an elementary value, methods called from ST programs are mainly suited for processing elementary values, such as conversions. This restriction can be bypassed by accessing an ABAP data object bound to a data root in the called method.
