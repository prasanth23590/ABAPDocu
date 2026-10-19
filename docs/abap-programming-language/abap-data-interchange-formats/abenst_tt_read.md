---
title: "ST - tt:read, Read Variables"
source_file: abenst_tt_read.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Reading and Writing Variables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:read, Read Variables

## Syntax

``` abap
<tt:read var="variable" [type="type" [length="len"] 
                                     [decimals="dec"]] 
                        [map="..."] 
                        [minLength|maxLength="len"] 
                        [xsd-type...] />  
```

## Description

The `tt:read` statement makes it possible to read the value of the inbound XML stream into a [variable](abenst_tt_variable.md) or a [parameter](abenst_tt_parameter.md):

The attribute value `variable` is used to specify the variable or a parameter into which the value is read. The same applies to the attributes `map`, `minLength`, `maxLength`, and `xsd-type...` as to the statement [`tt:value`](abenst_tt_value_elementary.md) (however `tt:read` always ignores `minLength`).

The other attributes are used to specify the expected type. In the `tt:read` statement, only elementary ABAP types can be specified, which can be partly generic. The syntax of this is the same as for the [`tt:type`](abenst_tt_type.md) statement. The value read must match the specified type and the value must be in the corresponding ABAP value range. Otherwise an exception is raised.

**Serialization**

The statement `tt:read` is ignored in serializations.

**Deserialization**

If no type conflict occurs, the variable or parameter is set to the value of the current position in the input stream, optionally according to the mapping list behind `map`. Depending on the type of the variable or parameter, a mapping takes place according to the [asXML format](abenabap_xslt_asxml.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Deserialization of a value into a variable is shown in the following transformation `DEMO_ST_READ`.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:variable name="VARI"/> 
  <tt:template> 
    <X> 
      <tt:read var="VARI" type="I" /> 
    </X> 
    <tt:assign to-ref="ROOT" var="VARI"/> 
  </tt:template> 
</tt:transform>
```

If the read XML fragment is `<X>333</X>`, the data object bound to the data root `ROOT` has the value 333 after deserialization due to the assignment using [`tt:assign`](abenst_tt_assign.md).
