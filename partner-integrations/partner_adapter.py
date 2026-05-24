from __future__ import annotations

from response_normalizer import normalize_request, to_partner_response


class PartnerAdapter:
    def __init__(self):
        self.dead_letter_queue = []

    def handle(self, partner: str, payload: dict):
        normalized = normalize_request(payload)
        internal = {"sku": normalized["sku"], "store_id": normalized["store_id"], "quantity_available": 8, "stock_status": "in_stock"}
        return {"partner": partner, "normalized_request": normalized, "internal_response": internal, "partner_response": to_partner_response(partner, internal)}
