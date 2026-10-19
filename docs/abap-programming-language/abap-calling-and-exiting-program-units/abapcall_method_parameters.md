---
title: "meth( ... ), Parameter Passing"
source_file: abapcall_method_parameters.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > Method Calls > Static Method Calls"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# meth( ... ), Parameter Passing

## Syntax

``` abap
... [EXPORTING  p1 = a1 p2 = a2 ...]   
    [IMPORTING  p1 = a1 p2 = a2 ...]   
    [CHANGING   p1 = a1 p2 = a2 ...]   
    [RECEIVING  r  = a  ]   
    [EXCEPTIONS [exc1 = n1 exc2 = n2 ...]   
                [OTHERS = n_others] ].  
```

### Addition

[1. `... EXPORTING p1 = a1 p2 = a2 ...`](abapcall_method_parameters.md#addition-1)

[2. `... IMPORTING p1 = a1 p2 = a2 ...`](abapcall_method_parameters.md#addition-2)

[3. `... CHANGING p1 = a1 p2 = a2 ...`](abapcall_method_parameters.md#addition-3)

[4. `... RECEIVING r = a`](abapcall_method_parameters.md#addition-4)

[5. `... EXCEPTIONS exc1 = n1 exc2 = n2 ... [OTHERS = n_others]`](abapcall_method_parameters.md#addition-5)

## Overview

### Description

Apart from the addition `EXCEPTIONS`, these additions assign actual parameters `a1 a2...` to the formal parameters `p1 p2 ...` or `r` of the parameter interface of the called method. Any data objects (and some expressions) can be specified as actual parameters if their data type matches the [typing](../../abap-glossary/abentyping_glosry.md) of the corresponding formal parameter in accordance with the rules of the [typing check](../abap-declarations/abentyping_check.md).

With the exception of the return value `r` for [functional methods](../../abap-glossary/abenfunctional_method_glosry.md) and the specification of arithmetic expressions for input parameters, every formal parameter inherits all properties of the assigned actual parameters when called. Non-class-based exceptions can be handled using the addition `EXCEPTIONS`. The order of the additions is fixed.

### Hints

- The formal parameters and non-class-based exceptions of a method are defined as its [parameter interface](../../abap-glossary/abenparameter_interface_glosry.md) using the additions of the statements [`METHODS`](../abap-declarations/abapmethods_parameters.md) or [`CLASS-METHODS`](../abap-declarations/abapclass-methods_general.md) of global or local classes.

- Unlike [function module calls](abapcall_function_general.md), static parameter passing is checked by the syntax check and not just by the extended program check.

## Addition 1

`... EXPORTING p1 = a1 p2 = a2 ...`

### Description

This addition assigns actual parameters to the [input parameters](../../abap-glossary/abeninput_parameter_glosry.md) of the called method. `EXPORTING` can be used to assign actual parameters to the optional input parameters and it must be used to assign actual parameters to the non-optional input parameters. In [pass by reference](../../abap-glossary/abenpass_by_reference_glosry.md), a reference to an actual parameter is passed when the call is made. In [pass by value](../../abap-glossary/abenpass_by_value_glosry.md), the content of an actual parameter is assigned to the relevant formal parameter.

`a1`, `a2`, ... are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md), which means that, in addition to data objects, expressions can also be passed as actual parameters. [Special rules](../abap-declarations/abentyping_arith_expr.md) apply in this case.

### Hints

- No [substring access](../abap-operands/abenoffset_length.md) is possible after an actual parameter of type `string` or `xstring` specified after `EXPORTING`.

- The addition `EXPORTING` can also be omitted in the [short form](abapcall_method_static_short.md) of the static method call.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Calls of a method with passing of actual parameters to input parameters. The first call is the syntax short form of the second call. Both have the same functionality.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
out->write_data( name  = 'Some text' 
                 value = 'blah, blah ...' ). 
 
out->write_data( EXPORTING name  = 'Some text' 
                           value = 'blah, blah ...' ). 
 
out->display( ).
```

## Addition 2

`... IMPORTING p1 = a1 p2 = a2 ...`

### Description

This addition assigns actual parameters to the [output parameters](../../abap-glossary/abenoutput_parameter_glosry.md) of the called method. `IMPORTING` can be used to assign actual parameters to all output parameters, but this is not mandatory. In [pass by reference](../../abap-glossary/abenpass_by_reference_glosry.md), a reference is passed to an actual parameter when the call is made. In [pass by value](../../abap-glossary/abenpass_by_value_glosry.md), the content of an output parameter is assigned to the relevant actual parameter only if the method is completed without errors.

The actual parameters are [result positions](../../abap-glossary/abenresult_position_glosry.md), which means that variables and [writable expressions](../../abap-glossary/abenwritable_expression_glosry.md) can be specified. [Special rules](../abap-declarations/abentyping_arith_expr.md) apply in this case.

- Existing variables or writable expressions can be specified as actual parameters for [functional method calls](abapcall_method_functional.md). Inline declarations, however, cannot be specified.

- Inline declarations [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md) can also be specified for [standalone method calls](abapcall_method_static_short.md). If an inline declaration is specified and a formal parameter is completely typed, this type is used for the declaration. If the formal parameter is typed generically, the following data types are used:

  - `string` for `csequence` and `clike`

  - `xstring` for `xsequence`

  - `decfloat34` for `numeric` and `decfloat`

  - `p` with the length 8 and no decimal places if `p` is generic

  - The [standard key](../../abap-glossary/abenstandard_key_glosry.md) for a standard table type with a generic primary table key

Other generic data types cannot be specified correctly for inline declarations and produce a syntax error.

### Hints

- If a formal parameter is typed with the generic type `c` or `x`, for example, `string` or `xstring` cannot be used as the type for an inline declaration, since the typing cannot be checked.

- Functional method calls are on the right side of assignments or are part of expressions where no inline declarations are possible.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The method is called [functionally](abapcall_method_functional.md) as an operand of a [comparison expression](../../abap-glossary/abencomparison_expression_glosry.md) in a logical expression. The values in the output are reused in further method calls only if the method completed successfully.

``` abap
DATA: itf  TYPE tline_tab, 
      head TYPE thead. 
 
IF cl_abap_docu_itf=>get_docu( 
     EXPORTING object = 'ABENABAP' 
     IMPORTING itf  = itf 
               head = head ) = 0. 
  cl_abap_docu_itf=>get_docu_includes( 
     EXPORTING head = head 
     CHANGING  itf  = itf ). 
ENDIF.
```

## Addition 3

`... CHANGING p1 = a1 p2 = a2 ...`

### Description

This addition assigns actual parameters to the [input/output parameters](../../abap-glossary/abeninput_output_parameter_glosry.md) of the called method. `CHANGING` can be used to assign actual parameters to the optional input/output parameters and it must be used to assign actual parameters to the non-optional input/output parameters. In [pass by reference](../../abap-glossary/abenpass_by_reference_glosry.md), a reference to an actual parameter is passed when the call is made. In [pass by value](../../abap-glossary/abenpass_by_value_glosry.md), the content of an actual parameter is assigned to the relevant formal parameter. In [pass by value](../../abap-glossary/abenpass_by_value_glosry.md), the modified content of an input/output parameter is assigned to the relevant actual parameter only if the method is completed without errors.

The actual parameters are [result positions](../../abap-glossary/abenresult_position_glosry.md), which means that variables and [writable expressions](../../abap-glossary/abenwritable_expression_glosry.md) can be specified. [Special rules](../abap-declarations/abentyping_arith_expr.md) apply in this case.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of a method with an input/output parameter.

``` abap
DATA(text) = `...`. 
cl_demo_input=>request( CHANGING field = text ).
```

## Addition 4

`... RECEIVING r = a`

### Description

This addition assigns an actual parameter to the [return value](../../abap-glossary/abenreturn_value_glosry.md) of the called method. It is only possible for [standalone method calls](abapcall_method_static_short.md) and not for [functional method calls](abapcall_method_functional.md). An actual parameter can be assigned to the return value of a [functional method](../../abap-glossary/abenfunctional_method_glosry.md) using `RECEIVING`. The data type of the actual parameter does not have to follow the general rules of the [typing check](../abap-declarations/abentyping_check.md) and it is sufficient if the return value can be converted to the actual parameter in accordance with the [conversion rules](../abap-processing-internal-data/abenconversion_rules.md).

If the method is completed without errors, the content of the formal parameter is assigned to the actual parameter. The content is converted if necessary. If an exception is raised here, it cannot be handled and a runtime error always occurs instead.

The actual parameter is a [result position](../../abap-glossary/abenresult_position_glosry.md), which means that variables and [writable expressions](../../abap-glossary/abenwritable_expression_glosry.md) can be specified. [Special rules](../abap-declarations/abentyping_arith_expr.md) apply in this case.

An existing variable or expression or an inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md) can be specified as an actual parameter. An inline declaration is made as soon as the data type of the return value is fully known.

### Hint

The addition `RECEIVING` is not usually used for static method calls. A functional method with a return value is not usually called as a [standalone method call](abapcall_method_static_short.md) but as a [functional method call](abapcall_method_functional.md) in [operand positions](../../abap-glossary/abenoperand_position_glosry.md) instead.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Calls of a functional method with return value. The first call is the usual [functional method call](abapcall_method_functional.md). The second call demonstrates the unusual use of the addition `RECEIVING`. The result is the same in both cases.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA html type string. 
 
html = out->get( 'blah, blah ...' ). 
 
out->get( EXPORTING data   = 'blah, blah ...' 
          RECEIVING output = html ).
```

## Addition 5

`... EXCEPTIONS exc1 = n1 exc2 = n2 ... [OTHERS =n_others]`

### Description

This addition is only possible for [standalone method calls](abapcall_method_static_short.md) and not for [functional method calls](abapcall_method_functional.md).

`EXCEPTIONS` can be used to assign return codes to [non-class-based exceptions](../abap-program-flow-logic/abenexceptions_non_class.md) `exc1 exc2 ...` declared in the parameter interface. Each exception `exc1 exc2 ...` that the caller wants to handle must be assigned to a directly specified number `n1 n2 ...` All numbers between 0 and 65535 can be specified. The behavior outside of this range is undefined.

By specifying `OTHERS` as the last entry after `EXCEPTIONS`, a common return code can be assigned to all exceptions not specified explicitly in `exc1 exc2...`. This is done by assigning a number `n_others`. The same return code can be assigned to different exceptions (including `OTHERS`). The behavior when an exception is raised is as follows:

- If the statement [`RAISE`](../abap-program-flow-logic/abapraise_exception.md) or [`MESSAGE RAISING`](../abap-program-flow-logic/abapmessage_raising.md) is used to raise an exception `exc1 exc2 ...` to which a return code is assigned, the statement is terminated immediately, any procedure parameters passed by value are not filled, and the number `n1 n2 ...` assigned to the exception is available to be evaluated in `sy-subrc`.

- If the call of an exception raised by [`RAISE`](../abap-program-flow-logic/abapraise_exception.md) does not assign a return code, the program is terminated with a runtime error.

- If the call of an exception raised by [`MESSAGE RAISING`](../abap-program-flow-logic/abapmessage_raising.md) does not assign a return code, the [message](../../abap-glossary/abenmessage_glosry.md) is sent, and the system resumes in accordance with the message type.

If no exception is raised, a call sets `sy-subrc` to 0.

The addition `EXCEPTIONS` cannot be specified in the call if `RAISING` is used to declare [class-based exceptions](../../abap-glossary/abenclass_based_exception_glosry.md) in the parameter interface of the called procedure. The specified exceptions must exist in the parameter interface of the method.

### Hints

- If the value 0 is assigned to an exception, this indicates that the caller wants to ignore this exception. If the exception is raised in the method, no runtime error occurs, but the exception cannot be handled.

- For more information about the behavior of class-based exceptions in methods, see [Class-Based Exceptions in Procedures](../abap-program-flow-logic/abenexceptions_procedures.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Handling of non-class-based exceptions in a method call.

``` abap
cl_gui_frontend_services=>directory_exist( 
  EXPORTING 
    directory            =  '...' 
  RECEIVING 
    result               =   FINAL(flag) 
  EXCEPTIONS 
    cntl_error           = 1 
    error_no_gui         = 2 
    wrong_parameter      = 3 
    not_supported_by_gui = 4 
    OTHERS               = 5 ). 
IF sy-subrc <> 0. 
  CASE sy-subrc. 
    WHEN 1. 
      ... 
    ... 
  ENDCASE. 
ENDIF.
```
