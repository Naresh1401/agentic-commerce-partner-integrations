from __future__ import annotations

import json
from partner_adapter import PartnerAdapter

if __name__ == "__main__":
    adapter = PartnerAdapter()
    print(json.dumps(adapter.handle("A", {"itemCode": "SKU-PASTA-001", "location": "store_1001", "qty": 2}), indent=2))
