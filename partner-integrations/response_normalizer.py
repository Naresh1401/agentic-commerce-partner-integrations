from __future__ import annotations

def normalize_request(payload):
    if "itemCode" in payload:
        return {"sku": payload["itemCode"], "store_id": payload["location"], "quantity": payload["qty"]}
    return {"sku": payload["product_sku"], "store_id": payload["store"], "quantity": payload["quantity_requested"]}


def to_partner_response(partner, internal):
    if partner == "A":
        return {"itemCode": internal["sku"], "location": internal["store_id"], "available": internal["quantity_available"] > 0}
    return {"product_sku": internal["sku"], "store": internal["store_id"], "can_fulfill": internal["quantity_available"] > 0}
