---
title: "XSL - SAP Instructions"
source_file: abenabap_xslt_sap_instr.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > XSL Transformations > XSL - User-Defined Transformations > XSL - Instructions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# XSL - SAP Instructions

In the following, enhanced SAP-specific instructions of the [SAP XSLT processor](abenabap_xslt_processor.md) are listed. The URI for the SAP namespace is `http://www.sap.com/sapxsl`.

## ABAP Calls

Transformations should be described using XSLT elements. However, it can be useful to access additional data from within an XSLT program, for example, data in the database, or to execute calculations in procedures. For this purpose, ABAP calls have been integrated as enhancements into the SAP XSLT processor. In this way, constructor calls and class method calls in XSLT programs can be defined, in addition to method calls for ABAP objects that are included as program parameters using `xsl:param`.

### Hint

XSLT is a declarative language, which means that the order in program execution is not fixed. ABAP calls should therefore be limited to read access. Possible state manipulations are the exception and are visible when transformations are executed.

## Additional XPath Functions

Even recursive functions at the level of tree transformations can be defined using named templates. The SAP XSLT processor provides an enhancement to define XPath functions. Functions of this type always have their own namespace (not XSLT or SAP XSLT) and are generally used in connection with the additional [SAP functions](abenabap_sap_fnctns.md) `sap:if()` and `sap:let()`.
