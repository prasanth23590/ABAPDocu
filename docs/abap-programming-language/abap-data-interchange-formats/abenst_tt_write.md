---
title: "ST - tt:write, Write Variables"
source_file: abenst_tt_write.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Reading and Writing Variables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:write, Write Variables

## Syntax

``` abap
<tt:write var="variable" [map="..."] 
                         [length|minLength="len"] 
                         [xsd-type...] />  
```

## Description

The `tt:write` statement makes it possible to write the value of a [variable](abenst_tt_variable.md) or a [parameter](abenst_tt_parameter.md) to the target XML data.

The attribute value `variable` is used to specify the variable to be written or a parameter. The same applies to the attributes `map`, `length`, `minLength`, and `xsd-type...` as to the statement [`tt:value`](abenst_tt_value_elementary.md). The variable must represent an elementary value.

**Serialization**

The value of the variable or the parameter is inserted into the XML data at the position of the statement, optionally according to the mapping list behind `map`. Depending on the type of the variable or parameter, mapping takes place according to the [asXML format](abenabap_xslt_asxml.md).

**Deserialization**

The `tt:write` statement is ignored in deserializations.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example `DEMO_ST_WRITE` serializes the start value of a variable.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:variable name="VARI" val="333" /> 
  <tt:template> 
    <X> 
      <tt:write var="VARI"/> 
    </X> 
  </tt:template> 
</tt:transform>
```

The result of the serialization is:

`<X>333</X>`
