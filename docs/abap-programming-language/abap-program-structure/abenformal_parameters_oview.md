---
title: "Parameter Interface of Procedures"
source_file: abenformal_parameters_oview.html
section: "ABAP Programming Language > ABAP - Program Structure > Modularization Statements > Procedures"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Parameter Interface of Procedures

The parameter interface of a procedure consists of [formal parameters](../../abap-glossary/abenformal_parameter_glosry.md) and specifies the possible [exceptions](../../abap-glossary/abenexception_glosry.md) in the procedure.

- [Formal Parameters](abenformal_parameters_oview.md#formal-parameters)

  - [Pass by Reference or Pass by Value](abenformal_parameters_oview.md#pass-by-reference-or-pass-by-value)

- [Exceptions](abenformal_parameters_oview.md#exceptions)

## Formal Parameters

Formal parameters are;

- [Input parameters](../../abap-glossary/abeninput_parameter_glosry.md)

  An input parameter is a formal parameter to which the value of an actual parameter s passed at the time of a call and which is evaluated in the procedure. Input parameters for which [pass by reference](../../abap-glossary/abenpass_by_reference_glosry.md) is defined must not be accessed with write access in the procedure. Input parameters are defined for [methods](../../abap-glossary/abenmethod_glosry.md) and [function modules](../../abap-glossary/abenfunction_module_glosry.md) using `IMPORTING`, which is why they are also called [importing parameters](../../abap-glossary/abenimporting_parameter_glosry.md).

- [Output parameters](../../abap-glossary/abenoutput_parameter_glosry.md)

  An output parameter is a formal parameter whose value is set in the procedure and is made available in the actual parameter after the procedure is completed. Output parameters are defined in [methods](../../abap-glossary/abenmethod_glosry.md) and [function modules](../../abap-glossary/abenfunction_module_glosry.md) using `EXPORTING` and are therefore also referred to as [exporting parameters](../../abap-glossary/abenexporting_parameter_glosry.md).

- [Input/output parameters](../../abap-glossary/abeninput_output_parameter_glosry.md)

  An input/output parameter is a formal parameter to which the value of an actual parameter s passed at the time of a call, whose value can be set in the procedure and is available in the actual parameter at the end of the procedure. In all procedures, input/output parameters are defined using the addition `CHANGING` and are therefore also referred to as [changing parameters](../../abap-glossary/abenchanging_parameter_glosry.md).

- [Return values](../../abap-glossary/abenreturn_value_glosry.md)

  Return values contain the result of [functional methods](../../abap-glossary/abenfunctional_method_glosry.md) at the end of the procedure. They are defined using the addition [`RETURNING`](../abap-declarations/abapmethods_functional.md) and are therefore also referred to as [returning parameters](../../abap-glossary/abenreturning_parameter_glosry.md).

In addition, there are several obsolete [table parameters](../../abap-glossary/abentable_parameter_glosry.md). Formal parameters are either generic or completely [typed](../../abap-glossary/abentyping_glosry.md). [Pass by reference](../../abap-glossary/abenpass_by_reference_glosry.md) or [pass by value](../../abap-glossary/abenpass_by_value_glosry.md) can be specified for most formal parameters. Pass by value is mandatory for some formal parameters.

Formal parameters have names and are either [generic](../../abap-glossary/abengeneric_data_type_glosry.md) or completely typed. Depending on their [typing](../../abap-glossary/abentyping_glosry.md), they can be used in the same way as [data objects](../../abap-glossary/abendata_object_glosry.md) in the procedure. The formal parameters make up a substantial part of the [signature](../../abap-glossary/abensignature_glosry.md) of a procedure. Formal parameters are [keyword parameters](../../abap-glossary/abenkeyword_parameter_glosry.md) (for [methods](../../abap-glossary/abenmethod_glosry.md) and [function modules](../../abap-glossary/abenfunction_module_glosry.md)).

When a procedure is called, formal parameters are bound to [actual parameters](../../abap-glossary/abenactual_parameter_glosry.md). The required data type of an actual parameter and the kind of parameter passing ([pass by reference](../../abap-glossary/abenpass_by_reference_glosry.md) or [pass by value](../../abap-glossary/abenpass_by_value_glosry.md)) are specified by the definition of the formal parameter. To [input parameters](../../abap-glossary/abeninput_parameter_glosry.md) of the of [methods](../../abap-glossary/abenmethod_glosry.md), [functional methods](../../abap-glossary/abenfunctional_method_glosry.md) [calculation expressions](../../abap-glossary/abencalculation_expression_glosry.md) can be passed besides data objects.

### Pass by Reference or Pass by Value

Parameters can be passed to procedures either by reference or by value.

- **Pass by reference**

  In the case of pass by reference, a reference to the actual parameter is passed to the procedure when it is called. The procedure then works with the actual parameter itself. No local data object is created for the actual parameter. Input parameters that are passed by reference cannot be changed in the procedure

- **Pass by value**

  In the case of pass by value, a type-compliant local data object is created as a copy of the actual parameter for the formal parameter. Output parameters and return values are initialized when the procedure is started and input parameters, as well as input/output parameters, are given the value of the actual parameter. A changed formal parameter is only passed to the actual parameter if the procedure is completed without errors.

When deciding whether to use pass by reference or pass by value for a formal parameter, the performance and robustness of each pass-by type must be compared.

In ABAP, pass by reference always has better performance since no local data object is created and no data transport is necessary when the procedure is called. Therefore, for performance reasons, pass by reference is usually preferable, unless explicit or implicit writes to an input parameter take place in the procedure or if it needs to be ensured that an input/output parameter or an output parameter is returned only if the procedure ends without any errors. In such a case, pass by value is mandatory, to make sure that the assigned [actual parameter](../../abap-glossary/abenactual_parameter_glosry.md) is not modified simultaneously in the caller when writes are made to a formal parameter. For performance reasons, only parameters of 100 bytes or less should be passed in these cases, whenever possible.

Also note the following when using pass by reference:

- An output parameter that is passed by reference acts like an input/ output parameter; that is, if read access to an output parameter is carried out in the procedure before the value of that parameter is changed, this value is not initial, unlike with pass by value, but corresponds to the current value of the actual parameter in the caller.

- If a procedure is terminated because of an error, that is, if it is terminated for a reason other than reaching its last statement or `RETURN`, `EXIT`, or `CHECK`, all actual parameters that are passed by reference are set to the value of the assigned formal parameter that the parameter was at when the program was terminated. In pass by value, no values are passed to actual parameters when a procedure is terminated.

Procedures and their calls must be programmed in such a way that these kinds of errors do not occur.

To summarize, pass by reference is always preferable when performance is important, whereas pass by value is more secure in situations where the emphasis is on robustness and data consistency. These factors must be considered when deciding which pass-by type to use with which type of parameter.

### Hints

- When strings or internal tables of the same type are passed by value, [table sharing](../../abap-glossary/abensharing_glosry.md) takes effect between the data object created locally and the passed data object, such as in [assignments](../../abap-glossary/abenassignment_glosry.md). However, [table sharing](../../abap-glossary/abentable_sharing_glosry.md) only occurs if the line type of the internal table allows it. When passing strings and internal tables, the performance drawbacks of pass by value can, under certain circumstances, be lifted by sharing.

- Only pass by reference can be specified for the obsolete [table parameters](../../abap-glossary/abentable_parameter_glosry.md).

- A local data object is generated for formal parameters that are passed by reference and are not bound to an actual parameter during the call as for pass by value.

- There are special rules for defining [literals](../abap-declarations/abentyping_literals.md) and [expressions as actual parameters](../abap-declarations/abentyping_arith_expr.md):

  - When a literal is bound, its typing is not checked as strictly.

  - When a function, a calculation expression, a constructor expression, or a table expression is bound, passing is always [pass by value](../../abap-glossary/abenpass_by_value_glosry.md), even if the formal parameter is defined as [pass by reference](../../abap-glossary/abenpass_by_reference_glosry.md).

- The result of the [typing check](../abap-declarations/abentyping_check.md) when passing actual parameters to formal parameters is independent of the pass type. In a [pass by value](../../abap-glossary/abenpass_by_value_glosry.md), the check for [pass by reference](../../abap-glossary/abenpass_by_reference_glosry.md) is always performed, even though this is stricter than necessary in individual cases. For example, a special reference variable cannot be passed to a general typed `CHANGING` parameter, even if pass by value is defined for this parameter.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

For a method `meth`, `CHANGING` parameter `p1` is defined for pass by reference and `p2` for pass by value. The value of both parameters is changed before an exception is raised. The actual parameter `a1` bound to the parameter using pass by reference contains the changed value when the exception is handled. The actual parameter `a2` bound to the parameter using pass by value, on the other hand, keeps its value.

``` abap
CLASS cx_exception DEFINITION 
                   INHERITING FROM cx_static_check. 
ENDCLASS. 
 
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS meth CHANGING p1        TYPE i 
                                VALUE(p2) TYPE i 
                       RAISING  cx_exception. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD meth. 
    p1 = 333. 
    p2 = 444. 
    RAISE EXCEPTION TYPE cx_exception. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA(a1) = 111. 
    DATA(a2) = 222. 
    TRY. 
        cls=>meth( CHANGING p1 = a1 
                           p2 = a2 ). 
      CATCH cx_exception. 
        cl_demo_output=>display( |{ a1 }, { a2 }| ). 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```

## Exceptions

[Class-based exceptions](../../abap-glossary/abenclass_based_exception_glosry.md) can be declared using `RAISING` in all procedures ([methods](../../abap-glossary/abenmethod_glosry.md), [function modules](../../abap-glossary/abenfunction_module_glosry.md)), and can then be [propagated from the procedure](../abap-program-flow-logic/abenexceptions_procedures.md). `EXCEPTIONS` can also be used in methods and function modules to define non-class-based exceptions, which can then be raised in the procedure using [`RAISE`](../abap-program-flow-logic/abapraise_exception.md) or [`MESSAGE ... RAISING`](../abap-program-flow-logic/abapmessage_raising.md).
