import sys
from pathlib import Path

sys.path.insert(0, str(Path('partner-integrations').resolve()))
from partner_adapter import PartnerAdapter

def test_partner_a_normalization():
    result = PartnerAdapter().handle('A', {'itemCode': 'SKU-PASTA-001', 'location': 'store_1001', 'qty': 2})
    assert result['normalized_request'] == {'sku': 'SKU-PASTA-001', 'store_id': 'store_1001', 'quantity': 2}
    assert result['partner_response']['available'] is True

