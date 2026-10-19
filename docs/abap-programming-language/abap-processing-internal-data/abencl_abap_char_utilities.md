---
title: "Class with Utilities for String Processing"
source_file: abencl_abap_char_utilities.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > System Classes for Character String and Byte String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Class with Utilities for String Processing

The class `CL_ABAP_CHAR_UTILITIES` provides attributes and methods as utilities for string processing.

The components of this class are all static and public and the attributes are read-only and are initialized in the class constructor. Details about the attributes and methods of this class are described in the class documentation.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following lines demonstrate that attributes of the class `CL_ABAP_CHAR_UTILITIES` containing [control characters](../../abap-glossary/abencontrol_character_glosry.md) can be replaced by a representation of the [control characters](abenstring_templates_separators.md) in a [string template](../../abap-glossary/abenstring_template_glosry.md).

``` abap
ASSERT cl_abap_char_utilities=>newline        = |\n|. 
ASSERT cl_abap_char_utilities=>horizontal_tab = |\t|. 
ASSERT cl_abap_char_utilities=>cr_lf          = |\r\n|.
```
