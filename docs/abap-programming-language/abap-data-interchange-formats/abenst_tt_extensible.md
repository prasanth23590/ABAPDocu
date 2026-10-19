---
title: "ST - tt:extensible, Extensibility of Literal XML Elements"
source_file: abenst_tt_extensible.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Literal Template Content > ST - Literal XML Elements and Attributes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:extensible, Extensibility of Literal XML Elements

## Syntax

``` abap
... tt:extensible="on"|"deep-static"|"deep-dynamic"|"off"|"deep-off"  ...  
```

## Description

In deserializations, XML elements in the input stream that are not specified in the ST program normally produce an error. If the processed XML format is to be extensible, elements that are not specified explicitly can be skipped without further processing through specification of the optional attribute `tt:extensible`. The attribute can have the following values:

- The value `on` states that the current element may have direct subelements that are not explicitly specified. This is the standard setting.

- Values `deep-static` and `deep-dynamic` state that the current element and its subelements can be enhanced. The value `off` deactivates extensibility for the current element but not its subelements. In other words, direct subelements cannot be added to the element but its (specified) subelements can be.

- The value *deep-off* deactivates extensibility for the current element and its subelements. These settings can be overwritten locally in individual subelements.

The values *deep-static* and *deep-dynamic* have different areas of validity:

- *deep-static* only has an effect within the part of the program in which it is set.

- *deep-dynamic* is effective across template calls using [`tt:apply`](abenst_tt_apply.md) and [`tt:call`](abenst_tt_call.md).

The deep extensibility that is configured using `deep-static` and `deep-dynamic` also takes effect in case distinctions with [`tt:switch`](abenst_tt_switch.md) and groupings with [`tt:group`](abenst_tt_group.md) by skipping unexpected elements that are not covered by a case.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The transformation `DEMO_ST_EXTENSIBLE_1` shows that extensibility together with optional elements (such as elements that are only deserialized when a condition occurs) causes problems, since extensibility generally means that such optional elements are not found.

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="A"/> 
  <tt:root name="B"/> 
  <tt:template> 
    <r tt:extensible="on"> 
      <tt:cond> 
        <a tt:value-ref="A"/> 
      </tt:cond> 
      <b tt:value-ref="B"/> 
    </r> 
  </tt:template> 
</tt:transform>
```

Passing an input stream

`<r><x/><a>1</a><b>2</b></r>`

does not produce the deserialization `A=1` since the unexpected element `x` sets the condition for `a` to false. Both `x` and `a` are skipped as *extension elements* and only the mandatory element `b` is deserialized as `B=2`. The problem can be solved by using [`tt:group`](abenst_tt_group.md), although this also resolves the order of `a` and `b`:

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="A"/> 
  <tt:root name="B"/> 
  <tt:template> 
    <r tt:extensible="on"> 
      <tt:group> 
        <tt:cond frq="?"> 
          <a tt:value-ref="A"/> 
        </tt:cond> 
        <tt:cond> 
          <b tt:value-ref="B"/> 
        </tt:cond> 
      </tt:group> 
    </r> 
  </tt:template> 
</tt:transform>
```

The class `CL_DEMO_ST_EXTENSIBLE` calls both transformations with the XML data shown above and displays the results.
