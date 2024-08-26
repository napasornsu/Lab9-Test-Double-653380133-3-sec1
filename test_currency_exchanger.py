import unittest
from unittest.mock import patch, Mock
from currency_exchanger import CurrencyExchanger

class TestCurrencyExchanger(unittest.TestCase):
    def setUp(self):
        self.exchanger = CurrencyExchanger(base_currency="THB", target_currency="KRW")

    @patch("currency_exchanger.requests.get")  # Mock the 'requests.get' method
    def test_get_currency_rate(self, mock_get):
        # Mock response object
        mock_response = Mock()
        expected_json = {'base': 'THB', 'result': {'KRW': 38.69}}
        mock_response.status_code = 200
        mock_response.json.return_value = expected_json

        # Assign mock's return value
        mock_get.return_value = mock_response

        # Act - execute the method under test
        self.exchanger.get_currency_rate()

        # Assert that the API was called correctly
        mock_get.assert_called_once_with("https://coc-kku-bank.com/foreign-exchange", params={'from': 'THB', 'to': 'KRW'})
        
        # Assert that the response was processed correctly
        self.assertIsNotNone(self.exchanger.api_response)
        self.assertEqual(self.exchanger.api_response, expected_json)

    @patch("currency_exchanger.requests.get")
    def test_currency_exchange(self, mock_get):
        # Mock response object
        mock_response = Mock()
        expected_json = {'base': 'THB', 'result': {'KRW': 38.69}}
        mock_response.status_code = 200
        mock_response.json.return_value = expected_json

        # Assign mock's return value
        mock_get.return_value = mock_response

        # Act - test the currency_exchange method
        result = self.exchanger.currency_exchange(100)

        # Assert that the API was called correctly
        mock_get.assert_called_once_with("https://coc-kku-bank.com/foreign-exchange", params={'from': 'THB', 'to': 'KRW'})

        # Assert that the exchange was calculated correctly
        expected_result = 100 * 38.69
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
