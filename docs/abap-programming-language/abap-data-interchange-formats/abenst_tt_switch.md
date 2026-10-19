---
title: "ST - tt:switch, Case Distinction"
source_file: abenst_tt_switch.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Flow Control"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:switch, Case Distinction

## Syntax

``` abap
<tt:switch> 
  <tt:[s-|d-]cond ... 
  <tt:[s-|d-]cond ... 
  ... 
</tt:switch>  
```

## Description

The statement `tt:switch` can be used to execute a maximum of one conditional transformations from a set of conditional transformations. A list of cases is specified in `tt:switch`, where the syntax of each case is formulated by a conditional transformation, namely a subelement [`tt:[s-|d-]cond`](abenst_tt_cond.md). In this case, `tt:[s-]cond` defines a serialization-relevant case, and `tt:[d-]cond` a deserialization-relevant case. Other direct subelements are not possible in `tt:switch`.

In contrast to conditional transformations positioned outside of `tt:switch`, for a case specifying at least one attribute [`using`](abenst_using.md), [`data`](abenst_data.md), or [`check`](abenst_check.md) is not necessary, provided that the content of `tt:[s-|d-]cond` is not a [pattern](abenst_pattern.md).

In the list of cases, the following must be noted:

- Only one serialization-relevant case may be specified in which no attribute `using`, `data`, or `check` is specified. This case is called standard serialization.

- A maximum of one deserialization-relevant case may be specified that does not contain a pattern. This case is called standard deserialization.

**Serialization**

Serializations follow these rules:

1.  The first serialization-relevant case `tt:[s-]cond` whose explicitly specified prerequisites are met is serialized and the element `tt:switch` is exited.

2.  If the prerequisite is not met for any of the serialization-relevant cases with explicitly specified attributes `using`, `data`, or `check`, the standard serialization is executed (if it exists) and the element `tt:switch` is exited.

3.  If no standard serialization exists, the exception `CX_ST_SWITCH_NO_CASE` is raised.

In successful serializations, exactly one case is executed.

**Deserialization**

Deserializations follow these rules:

1.  The first deserialization-relevant case `tt:[d-]cond` that contains a suitable [pattern](abenst_pattern.md) and whose prerequisites are met is executed (the assertions are deserialized and met) and the element `tt:switch` is exited.

2.  If no deserialization-relevant case that contains a pattern can be executed, the system tries to execute a standard deserialization, if it exists. After the execution, the element `tt:switch` is exited. If the possible prerequisites `using`, `data`, or `check` of the standard deserialization are not met, the exception `CX_ST_REF_ACCESS` is raised.

3.  If no standard deserialization exists, the exception `CX_ST_SWITCH_NO_CASE` is raised.

In successful deserializations, exactly one case is executed.

## Hint

When case distinctions are programmed, serializations and deserializations should be formulated as far as possible in common cases `tt:cond`, while the directional cases `tt:s-cond` and `tt:d-cond` should only be used where no common formulation is possible.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In serializations, the transformation `DEMO_ST_SWITCH1` below sets the attribute `size` of element `Paragraph` depending on the value of the data node `SIZE` to exactly one value of *Small*, *Big*, or *Medium*. *Medium* is created in standard serializations.

If, for example, the input values for `SIZE` are between 10 and 20, the result is as follows:

`<Paragraph size="Medium">Text</Paragraph>`

In deserializations, `data` is used to assign to the data node `SIZE` a value *8*, *16*, or *28* for each of the three valid attribute values *Small*, *Medium*, and *Big*. If a different attribute value is specified, the value *12* is assigned to `SIZE` in standard deserializations and the invalid attribute is skipped with `tt:skip`.

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="SIZE"/> 
  <tt:template> 
    <Paragraph> 
      <tt:attribute name="size"> 
        <tt:switch> 
          <tt:s-cond check="SIZE&lt;10"> 
            <tt:text>Small</tt:text> 
          </tt:s-cond> 
          <tt:s-cond check="SIZE&gt;20"> 
            <tt:text>Big</tt:text> 
          </tt:s-cond> 
          <tt:s-cond> 
            <tt:text>Medium</tt:text> 
          </tt:s-cond> 
          <tt:d-cond data="SIZE=8" using="exist(SIZE)"> 
            <tt:text>Small</tt:text> 
          </tt:d-cond> 
          <tt:d-cond data="SIZE=16" using="exist(SIZE)"> 
            <tt:text>Medium</tt:text> 
          </tt:d-cond> 
          <tt:d-cond data="SIZE=28" using="exist(SIZE)"> 
            <tt:text>Big</tt:text> 
          </tt:d-cond> 
          <tt:d-cond data="SIZE=12" using="exist(SIZE)"> 
            <tt:skip/> 
          </tt:d-cond> 
        </tt:switch> 
      </tt:attribute> 
      <tt:text>Text</tt:text> 
    </Paragraph> 
  </tt:template> 
</tt:transform>
```

In the above transformation, serializations and deserializations are handled completely separately and are divided within a single `tt:switch element`. Since there is no common case for serializations and deserializations, `tt:serialize` and `tt:deserialize` and two `tt:switch` elements can also be used to achieve the same result. In `DEMO_ST_SWITCH2`, the identifiers `s-` and `d-` can be omitted in front of `cond` and the query about whether `SIZE` is bound to an ABAP data object must be queried only once:

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="SIZE"/> 
  <tt:template> 
    <Paragraph> 
      <tt:attribute name="size"> 
        <tt:serialize> 
          <tt:switch> 
            <tt:cond check="SIZE&lt;10"> 
              <tt:text>Small</tt:text> 
            </tt:cond> 
            <tt:cond check="SIZE>20"> 
              <tt:text>Big</tt:text> 
            </tt:cond> 
            <tt:cond> 
              <tt:text>Medium</tt:text> 
            </tt:cond> 
          </tt:switch> 
        </tt:serialize> 
        <tt:deserialize> 
          <tt:cond check="exist(SIZE)"> 
            <tt:switch> 
              <tt:cond data="SIZE=8"> 
                <tt:text>Small</tt:text> 
              </tt:cond> 
              <tt:cond data="SIZE=16"> 
                <tt:text>Medium</tt:text> 
              </tt:cond> 
              <tt:cond data="SIZE=28"> 
                <tt:text>Big</tt:text> 
              </tt:cond> 
              <tt:cond data="SIZE=12"> 
                <tt:skip/> 
              </tt:cond> 
            </tt:switch> 
          </tt:cond> 
        </tt:deserialize> 
      </tt:attribute> 
      <tt:text>Text</tt:text> 
    </Paragraph> 
  </tt:template> 
</tt:transform>
```
