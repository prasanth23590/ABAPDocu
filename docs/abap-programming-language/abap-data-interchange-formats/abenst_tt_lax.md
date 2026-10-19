---
title: "ST - tt:lax, Name Comparisons of Literal XML Elements"
source_file: abenst_tt_lax.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Literal Template Content > ST - Literal XML Elements and Attributes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:lax, Name Comparisons of Literal XML Elements

## Syntax

``` abap
 ... tt:lax="on"|"off"|"deep-on"|"deep-off" ...  
```

## Description

When deserializing literal XML elements, the optional attribute `tt:lax` can be used to control whether the name of an element is respected.

- If `tt:lax` is specified with the value `off`, the inbound XML stream must contain an identically named element with all literal attributes `attr` of the same content.

- If `tt:lax` is specified with the value `on`, the element in the inbound XML stream can have any name, but the expected attributes must still match.

- The values `deep-on` and `deep-off` for `tt:lax` are used to set the setting `on` and `off` for all subelements of the current element; however, they can be overwritten locally there.

If `tt:lax` is not specified, the setting depends on the surrounding context. By default, a template has the setting `deep-off`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following XML fragment is to be assumed:

`<X my_attr="attr">abc</X>`

Due to `tt:lax="on"`, the ST program `DEMO_ST_LAX` below can still deserialize this fragment despite different element names:

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
<tt:root name="ROOT"/> 
  <tt:template> 
     <Y tt:lax="on"> 
       <tt:value ref="ROOT" /> 
     </Y> 
   </tt:template> 
</tt:transform>
```
