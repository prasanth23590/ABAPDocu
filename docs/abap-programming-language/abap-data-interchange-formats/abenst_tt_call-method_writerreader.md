---
title: "ST - tt:call-method, writer, reader, XML Stream"
source_file: abenst_tt_call-method_writerreader.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Access to ABAP Objects from ST"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:call-method, writer, reader, XML Stream

## Syntax

``` abap
<tt:call-method class="class"|var="oref" 
                [s-|d-]name="meth" 
                ... 
                writer="p_writer" 
                reader="p_reader"> 
  ... 
</tt:call-method>  
```

## Description

In the [static method](abenst_tt_call-method_static.md) or [instance method](abenst_tt_call-method_instance.md) called from an ST program, the attributes `writer` and `reader` can be used to access the current XML stream where the serialization or deserialization is currently taking place.

The called method `meth` must have an optional parameter with the reference type `IF_SXML_WRITER` or `IF_SXML_READER`, depending on the direction of transformation. The name of this parameter can be specified after the `writer` or `reader` attributes. In serialization, the `p_writer` parameter is passed a reference to the current writer stream. In deserialization, the parameter of type `p_reader` is passed a reference to the current reader stream. In the method `meth`, these parameters can be used to work with the XML stream.
