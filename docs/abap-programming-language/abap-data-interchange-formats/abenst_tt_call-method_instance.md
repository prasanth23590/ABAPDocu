---
title: "ST - tt:call-method, Calling Instance Methods"
source_file: abenst_tt_call-method_instance.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Access to ABAP Objects from ST"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:call-method, Calling Instance Methods

## Syntax

``` abap
<tt:call-method var="oref" [s-|d-]name="meth" 
                           [writer = "writer_para"] 
                           [reader = "reader_para"] > 
  [<tt:with-parameter [s-|d-]name="para1" 
                      [ref="node1"|val="val1"|var="var1"] /> 
   <tt:with-parameter [s-|d-]name="para2" 
                      [ref="node2"|val="val2"|var="var2"] /> 
   ...] 
</tt:call-method>  
```

## Description

Using this variant of the statement `tt:call-method`, it is possible to call an instance method of a global ABAP Objects class in an ST program as follows: `var` can be used to specify a [`variable`](abenst_tt_variable.md) or a [`parameter`](abenst_tt_parameter.md) of the ST program. The addition `ref-type` must have been used to create the variable or parameter as a class reference variable or interface reference variable. When called, the variable or parameter must point to the object of a class. Either the object can have been created in the ST program using [`tt:create-object`](abenst_tt_create.md), or it is referred to a corresponding ABAP reference variable.

`meth` can be used to specify a visible method that exists in the static type of the reference variable, that is in the class or interface. The specification of the method is not case-sensitive.

Method execution, parameter passing, and optional attributes are subject to the same conditions as [static method calls](abenst_tt_call-method_static.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The transformation `DEMO_ST_WITH_METHOD_CALL_INST` calls an instance method `CONVERT` in an object referenced by the parameter `OPAR`. This is passed to the input parameter `input` of the method and its return value `RESULT` is assigned to an identically named variable. The variable `result` is then serialized using [`tt:write`](abenst_tt_write.md). Note that no data root can be assigned to the return value of the method in serializations.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:parameter name="OPAR" ref-type="CL_DEMO_CALL_FROM_ST_INST"/> 
  <tt:variable name="result"/> 
  <tt:template> 
    <tt:call-method s-name="convert" var="OPAR"> 
      <tt:with-parameter name="input" ref="ROOT"/> 
      <tt:with-parameter name="result" var="result"/> 
    </tt:call-method> 
    <Result> 
      <tt:write var="result"/> 
    </Result> 
  </tt:template> 
</tt:transform>
```

The transformation is called in class `CL_DEMO_CALL_METH_FROM_ST`. A reference to an object of class `CL_DEMO_CALL_FROM_ST_INST` is passed using the addition `PARAMETERS`. The instance method `CONVERT` of that class is defined as follows:

``` abap
METHOD convert. 
  result  = input. 
  REPLACE ALL OCCURRENCES OF ` ` IN result WITH `-`. 
ENDMETHOD.
```

The result of the transformation is as follows:

`<Result>1-2-3</Result>`
