from xmlrpc import client
from env_vars_Odoo import *


def get_all_subscriptions():
    """
    Retrieves all the subscriptions from the subscription module in Odoo.
    """
    # Search for all subscription records in Odoo
    subscription_ids = models.execute_kw(
        db, uid, password, "sale.subscription", "search", [[["stage_id", "=", 2]]]
    )
    print(subscription_ids)
    # Read the subscription data
    subscription_data = models.execute_kw(
        db,
        uid,
        password,
        "sale.subscription",
        "read",
        [subscription_ids],
        {"fields": ["name", "date_start", "date", "stage_id", "uuid"]},
    )

    return subscription_data


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

    # Example usage
    all_subscriptions = get_all_subscriptions()
    for subscription in all_subscriptions:
        print(f"Subscription Name: {subscription['name']}")
        print(f"Start Date: {subscription['date_start']}")
        print(f"End Date: {subscription['date']}")
        print(f"Subscription State: {subscription['stage_id']}")
        print(f"Token: {subscription['uuid']}")
        print("---------------------------------------")

"""
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "<method>",
    "params": {
      "service": "<service>",
      "method": "<inner_method>",
      "args": [<arguments>]
    },
    "id": '"$(($(RANDOM % 1000000001))')"
  }' \
  <url>
"""
