---
title: "RAP message"
source_file: abenrap_message_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP message

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

A message that is represented by an instance of a class that implements the interface `IF_ABAP_BEHV_MESSAGE` and is used in [RAP BO provider](abenrap_bo_provider_glosry.md) implementations.

Each application can create its own classes. For convenience, each [behavior pool](abenbehavior_pool_glosry.md) contains a predefined local [exception class](abenexception_class_glosry.md) `CL_ABAP_BEHV_MSG` inherited from `CX_NO_CHECK` that implements `IF_ABAP_BEHV_MESSAGE` in a minimalistic way. It can be used for RAP messages as well as for raising [exceptions](abenexception_glosry.md) where appropriate.
