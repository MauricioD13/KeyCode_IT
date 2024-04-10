from xmlrpc import client
from env_vars_Odoo import *

# Authenticate and get the UID
# info = xmlrpc.client.ServerProxy(f"{odoo_url}/start").start()

common = client.ServerProxy(f"{odoo_url}/xmlrpc/2/common")
print(common.version())
uid = common.authenticate(db, username, password, {})
print(f"UID: {uid}")

if uid is True:
    # Create a connection to the model
    models = client.ServerProxy(f"{odoo_url}/xmlrpc/2/object")

    # Search for the quotation number in Odoo
    quotation_ids = models.execute_kw(
        db,
        uid,
        password,
        "res.partner",
        "check_access_rights",
        ["read"],
        {"raise_exception": False},
    )
    print(quotation_ids)
    # Extract and print the quotation numbers
    # for quotation in quotation_ids:
    #    print("Quotation Number: {}".format(quotation["name"]))
