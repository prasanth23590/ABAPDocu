---
title: "XSL - ABAP Calls"
source_file: abenabap_xslt_abap_calls.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > XSL Transformations > XSL - User-Defined Transformations > XSL - Instructions > XSL - SAP Instructions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# XSL - ABAP Calls

ABAP methods can be called by XSLT using the extension elements `sap:call-external` and `sap:external-function`.

## `sap:call-external`

Using the statement `sap:call-external`, ABAP calls with any number of return values can be performed from within an XSLT program. These calls can take place both at the instance level of ABAP classes (instance methods) and at the class level (class methods). When calling interface methods, these must be indicated with the name of the interface followed by the interface component selector (`intf~`).

Instance methods are called using the following syntax.

``` abap
<sap:call-external name="prefix:localname" method="instanceMethod"> 
  <sap:callvalue      param="inParam1" select="expression"/> 
  <sap:callvalue      param="inParam2" select="expression"/>      ... 
  <sap:callvariable   param="exParam1" name="varName1" type="xslType"/> 
  <sap:callvariable   param="exParam2" name="varName2" type="xslType"/> 
      ... 
</sap:call-external>
```

- The statement `sap:call-external` can be at any position in the XSLT source code where `xsl:call-template` is also allowed.

- An object name that identifies an ABAP object and the name of the method to be called need to be specified to call an instance method.

- Both sub-instructions `sap:callvalue` and `sap:callvariable` are required to pass parameter values.

- Using `sap:callvalue`, parameter values are passed to the called method as import parameters. The `param` attribute specifies one parameter name each from the method definition in ABAP; the value assignment takes place with the `select` attribute. Here the XSLT types `string`, `number`, `boolean`, and `node-set` can be passed to the ABAP parameters.

### Examples

The conversion of the types `number` and `node-set` into, for example, the corresponding ABAP values is done according to the following schema:

1.  A value of the type `number` can be compiled in ABAP both into an integer as well as into a floating point type.

2.  A node set is always converted into an iXML node collection. Note that there can be no implicit conversion of node sets into strings. For example, to pass the value of an attribute `attr` to a string parameter in ABAP, the XPath expression `string(@attr)` must be used.

3.  Data of type `C(1)` is converted to an XSLT string by default. However, if `boolean` is explicitly specified in the `type` attribute, the conversion is to XSLT `boolean` accordingly.

### Hints

- In general, ABAP objects can also be specified as parameters.

- Note that ABAP parameters of type `CHANGING` can be passed using both `sap:callvalue` and `sap:callvariable`.

- When a class method is called, the `name` attribute is replaced with the `class` attribute. The value for `class` must be specified accordingly as the name of the ABAP class and the value for the method as the name of the required class method: `sap:call-external class="className" method="classMethod"`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates an access to the database of the SAP system with which additional data is displayed for a selected flight connection. The call takes place using the class method `GET_DETAIL` for the class `CL_FLIGHT_INFO`. The information received is bound to the corresponding XSLT variables (`duration`, `distance`, `unit`, ...) using `sap:callvariable`.

``` abap
<sap:call-external class="CL_FLIGHT_INFO" method="GET_DETAIL"> 
  <sap:callvalue     param="AIRLID"   select="string($carr/@code)"/> 
  <sap:callvalue     param="CONNID"   select="string(@code)"/> 
  <sap:callvalue     param="FLDATE"   select="string(departure/date)"/> 
  <sap:callvariable  param="FLIME"    name="duration"/> 
  <sap:callvariable  param="DIST"     name="distance" type="number"/> 
  <sap:callvariable  param="UNIT"     name="unit"/> 
  <sap:callvariable  param="PLTYPE"   name="planetype"/> 
  <sap:callvariable  param="SEATSM"   name="seatsmax"/> 
</sap:call-external>
```

## `sap:external-function`

Using the instruction `sap:external-function`, a function for ABAP calls from within XPath can be declared. In contrast to `sap:call-external`, only one single return value can be specified for the method call. For this purpose, the method to be called must be declared as an external function at the top level of the XSLT program. Functions declared this way can be used for method calls in the XPath expressions and have their own namespace (not XSLT or SAP XSLT). When calling interface methods, these must be indicated with the name of the interface followed by the interface component selector (`intf~`).

Instance methods are called using the following syntax.

``` abap
<sap:external-function name="prefix:fName" method="instanceMethod" kind="instance"> 
   <sap:argument      param="PARAM_1"/> 
   <sap:argument      param="PARAM_2"/> 
      ... 
   <sap:result        param="RESULT"      type="xslType"/> 
</sap:external-function>
```

Class methods are called using the following syntax.

``` abap
<sap:external-function name="prefix:fName" class="className" method="classMethod" kind="class"> 
   <sap:argument      param="PARAM_1"/> 
   <sap:argument      param="PARAM_2"/> 
      ... 
   <sap:result        param="RESULT"      type="xslType"/> 
</sap:external-function>
```

Constructors are called using the following syntax.

``` abap
<sap:external-function name="prefix:new" class="className" kind="constructor"> 
   <sap:argument      param="PARAM_1"/> 
   <sap:argument      param="PARAM_2"/> 
      ... 
</sap:external-function>
```

- Except for the constructor declaration, the output of the attribute `method` is the name of the ABAP method to be called. The `kind` attribute defines, in addition, whether there is an instance or class method or a constructor. For class methods and constructors, the output of the name of the ABAP class is made using the `class` attribute.

- The list of function arguments is declared using the sub-instruction `sap:argument` (while respecting the order). The names of the corresponding ABAP parameters are specified using the `param` attribute.

- Calls of instance and class methods can define a return value using the sub-instruction `sap:result`. The name of the return parameter is specified by the `param` attribute. Optionally, a particular XSLT type (`string`, `number`, `boolean`, `node-set`, or `external`) can be assigned to the result using the `type` attribute.

### Calls in XPath Expressions

Declared functions can be used in XPath expressions for ABAP calls. For instance methods, the first function argument must be identified using an ABAP object.

Example: `<xsl:value-of select="prefix:f1($x,99,'abc')"/>`

In the example given, the function with the name `prefix:f1` defines an ABAP call using an instance method that passes the two values `99` and `'abc'` as input parameters. The first function argument `$x` identifies the required ABAP object.

Using a suitable declared constructor function, this call can also be written alternatively as follows: `<xsl:value-of select="prefix:f1(prefix:new('xyz'),99,'abc')"/>`
