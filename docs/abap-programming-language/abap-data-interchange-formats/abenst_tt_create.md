---
title: "ST - tt:create-object, Create Objects"
source_file: abenst_tt_create.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Access to ABAP Objects from ST"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:create-object, Create Objects

## Syntax

``` abap
<tt:create-object var="oref" [class="class"]> 
  [<tt:with-parameter name="para1" 
                      [ref="node1"|val="val1"|var="var1"] /> 
   <tt:with-parameter name="para2" 
                      [ref="node2"|val="val2"|var="var2"] /> 
   ...] 
</tt:create-object>  
```

## Description

The statement `tt:create-object` can be used to create an instance of a global ABAP Objects class in an ST program. `var` can be used to specify a [`variable`](abenst_tt_variable.md) or a [`parameter`](abenst_tt_parameter.md) of the ST program. The variable or parameter must have been created as a class reference variable or an interface reference variable with the addition `ref-type`.

The object is created in the [internal session](../../abap-glossary/abeninternal_session_glosry.md) of the ABAP program that called the ST program. If the attribute `class` is not specified, `var` must be a class reference variable and an instance of the corresponding class is created. If the attribute `class` is specified, an instance of the specified class is created. A global class from the ABAP class library can be specified for `class`, either more special or the same as the static type of the reference variable `var`:

- If `var` is a class reference variable, `class` must be the class or subclass of the class of `var`.

- If `var` is an interface reference variable, `class` must implement the interface of `var`.

The interface parameters `para1`, `para2`, ... of the instance constructor of the class of the object can or must be bound to actual parameters using the ST statement `tt:with-parameter`. The same rules apply here as to regular [method calls](abenst_tt_call-method_static.md). Constructor exceptions are also handled in the same way as exceptions for regular method calls.

After the object has been created, the reference variable `var` points to the object and can be used to call instance methods.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The transformation `DEMO_ST_WITH_CREATE_OBJECT` uses the variable `ovar` to create an object of class `CL_DEMO_CREATE_FROM_ST` and passes the data root `PARA` to the parameter `REPL` of its instance constructor. The method `CONVERT` is then called, whose input/output parameter is assigned the variable `result`. Note that a data root cannot be assigned to an input/output parameter, neither in serializations nor in deserializations.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:root name="PARA"/> 
  <tt:variable name="ovar" ref-type="CL_DEMO_CREATE_FROM_ST"/> 
  <tt:variable name="result"/> 
  <tt:template> 
    <tt:create-object var="ovar"> 
      <tt:with-parameter name="repl" ref="PARA"/> 
    </tt:create-object> 
    <tt:assign ref="ROOT" to-var="result"/> 
    <tt:call-method s-name="convert" var="ovar"> 
      <tt:with-parameter name="text" var="result"/> 
    </tt:call-method> 
    <Result> 
      <tt:write var="result"/> 
    </Result> 
  </tt:template> 
</tt:transform>
```

The transformation is called in class `CL_DEMO_CREATE_OBJECT_FROM_ST`. The constructor of class `CL_DEMO_CREATE_FROM_ST` is defined as follows:

``` abap
METHOD constructor. 
me->repl = repl. 
ENDMETHOD.
```

The method `CONVERT` is defined as follows:

``` abap
METHOD convert. 
  REPLACE ALL OCCURRENCES OF ` ` IN text WITH repl. 
ENDMETHOD.
```

The result of the transformation is as follows:

`<Result>1*2*3</Result>`
