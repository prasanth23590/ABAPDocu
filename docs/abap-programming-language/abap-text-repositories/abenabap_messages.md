---
title: "Messages"
source_file: abenabap_messages.html
section: "ABAP Programming Language > ABAP - Text Repositories"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Messages

Messages are [repository objects](../../abap-glossary/abenrepository_object_glosry.md) that are managed using a message maintenance tool. Fundamentally, a message is a short text that can be expanded using an optional long text. A message is identified with the following key:

- A 20-character message class

- A 3-digit message number

A message is created with an original language and can be translated to other languages.

The statement [`MESSAGE`](abapmessage.md) is the basic statement for working with messages in an ABAP program. When the statement `MESSAGE` is used to send a message, the message key and a [message type](../../abap-glossary/abenmessage_type_glosry.md) must be specified. Optionally, placeholders in the message text can be filled with values.

- The variant [`MESSAGE ... INTO`](abapmessage_into.md) assigns the short text of the message to a field.

Only the variant with the addition [`INTO`](abapmessage_into.md) can be used in the current ABAP language version [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md).

- [`MESSAGE`](abapmessage.md)

- [Messages - System Interfaces](abenmessage_interfaces.md)
