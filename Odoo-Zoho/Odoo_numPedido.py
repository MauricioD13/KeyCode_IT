from xmlrpc import client
from env_vars_Odoo import *

# Authenticate and get the UID
# info = xmlrpc.client.ServerProxy(f"{odoo_url}/start").start()
common = client.ServerProxy(f"{odoo_url}xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})
if uid:
    # Create a connection to the model
    models = client.ServerProxy(f"{odoo_url}xmlrpc/2/object")
    # Search for the quotation number in Odoo
    access_rights = models.execute_kw(
        db,
        uid,
        password,
        "res.partner",
        "check_access_rights",
        ["read"],
        {"raise_exception": False},
    )
    if access_rights == True:
        records = models.execute_kw(
            db,
            uid,
            password,
            "res.partner",
            "search_read",
            [[["is_company", "=", True]]],
            {
                "fields": [
                    "name",
                    "child_ids",
                    "email",
                    "email_formatted",
                    "contact_person",
                ],
                "limit": 5,
            },
        )
        for record in records:
            print(f"{record}")
            print("-----------------")
        """atributtes = models.execute_kw(
            db,
            uid,
            password,
            "res.partner",
            "fields_get",
            [],
            {"attributes": ["string", "help", "type"]},
        )"""
    # Extract and print the quotation numbers
    # for quotation in quotation_ids:
    #    print("Quotation Number: {}".format(quotation["name"]))
