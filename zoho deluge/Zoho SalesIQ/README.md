# Zobot in Zoho SalesIQ

The chat widget of Zoho SalesIQ that provide Zoho Desk was modified to ingest data from the web page.

- Customer name
- Customer email

This data is send to the Zoho SalesIQ Zobot, a platform for create low-code Bots.

The Zobot was build with complements that extend the functionality to make request to Odoo API.

*First*: Make a request to Zoho Desk API asking if the customer account and contact is already registered. Then evaluate the response with a "if" statement

- getContactIDAccountID

*Second*: Depende on the response,  Zobot create the missing customer account and/or contact using the Zoho Desk API. Also, if it's needed the Zobot make a request to Odoo API to retrieve the customer information.

- CreateAccount

Note: The CreateAccount complement requires as argument the contact ID of Zoho Desk, if that arg is pass as "false" it only creates an account but does not link it with a contact

- CreateContact
- getOdooContact

*Third*: Zobot uses the contact ID to create a ticket in Zoho Desk. It use all the information collected from the flow of the bot (pre-build cards) to fill all the fields of the ticket. The Zoho SalesIQ chat URL is passed to the ticket.

- CreateTicketContactID

*Fourth*: Finally Zobot pass the chat to a operator
