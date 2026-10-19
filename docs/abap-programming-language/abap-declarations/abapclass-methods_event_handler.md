---
title: "CLASS-METHODS, FOR EVENT"
source_file: abapclass-methods_event_handler.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Methods > CLASS-METHODS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS-METHODS, FOR EVENT

## Syntax

``` abap
CLASS-METHODS meth [DEFAULT IGNORE|FAIL]   
   FOR EVENT evt OF {class|intf}   
   [IMPORTING p1 p2 ...[sender]].  
```

[`DEFAULT IGNORE|FAIL`](abapmethods_default.md)

## Description

This statement declares the [static method](../../abap-glossary/abenstatic_method_glosry.md) `meth` as the [event handler](../../abap-glossary/abenevent_handler_glosry.md) for the event `evt` of the class `class` or the interface `intf`. The syntax and meaning of the additions are identical to the declaration of [instance methods as event handlers](abapmethods_event_handler.md).

Static event handlers can be called by the event `evt` independently of an instance of the class.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The class `dialog_box` defines a static event handler `close_box` for the event that is raised when the user wants to close a Control Frameworks (CFW) dialog box.

``` abap
CLASS dialog_box DEFINITION. 
  PUBLIC SECTION. 
    METHODS constructor. 
    ... 
  PRIVATE SECTION. 
    CLASS-DATA open_boxes TYPE i. 
    CLASS-METHODS close_box 
      FOR EVENT close OF cl_gui_dialogbox_container 
      IMPORTING sender. 
    ... 
ENDCLASS. 
 
CLASS dialog_box IMPLEMENTATION. 
  METHOD constructor. 
    ... " create a dialogbox 
    open_boxes = open_boxes + 1. 
  ENDMETHOD. 
  METHOD close_box 
    ... " close the dialogbox referred by sender 
    open_boxes = open_boxes - 1. 
  ENDMETHOD. 
ENDCLASS.
```
