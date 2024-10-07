from unittest.mock import MagicMock, patch

from unittest.mock import patch

from src.external_api import currency_conversion_in_rub


@patch("requests.get")
def test_currency_conversion_in_rub(mock_get: MagicMock) -> None:
    mock_get.return_value.json.return_value["result"] = 1.0
    assert (
        currency_conversion_in_rub(
            {
                "operationAmount": {
                    "amount": "1.0",
                    "currency": {"name": "USD", "code": "USD"},
                }
            }
        )
        == 1.0
    )
    mock_get.assert_called()

@patch("requests.get")
def test_conversion_2(mock_get: MagicMock, transaction_data_1: dict) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": "8221.37"},
        "info": {"timestamp": 1726849624, "rate": 92.349211},
        "date": "2024-09-20",
        "result": 759222.82,
    }
    assert currency_conversion_in_rub(transaction_data_1) == 759222.82
    mock_get.assert_called()