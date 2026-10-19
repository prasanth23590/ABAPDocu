---
title: "Call Event Handler"
source_file: abencall_event_handler.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Call Event Handler

Event handlers are special methods that are declared using the addition [`FOR EVENT ... OF`](../abap-declarations/abapmethods_event_handler.md) of the statements [`METHODS`](../abap-declarations/abapmethods.md) and [`CLASS-METHODS`](../abap-declarations/abapclass-methods.md). They are not usually called directly using explicit [method calls](abenmethod_calls.md).

- Instead, they are called indirectly using [`RAISE EVENT`](abapraise_event.md).

- They can only be executed if an event handler is registered using [`SET HANDLER`](abapset_handler.md).
