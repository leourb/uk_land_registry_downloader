import unittest
from unittest.mock import Mock, patch
from uk_land_property_client.land_registry import UKLandClient


class TestUKLandClient(unittest.TestCase):
    """Test the UKLandClient class."""

    @patch('requests.get')
    def test_download_data_valid_postcode(self, mock_requests_get: Mock) -> None:
        """
        Test the `download_data` method for a valid postcode.
        This test case simulates the behavior of the `download_data` method in the `UKLandClient` class for a valid
        postcode. It uses mocking to simulate the behavior of the `requests.get` method, allowing the `download_data`
        method to be tested without actual network interactions.
        :param Mock mock_requests_get: Mocked requests.get method to control HTTP response.
        :return: None
        """
        # Mock the response from requests.get
        mock_response = Mock()
        mock_response.text = 'your,csv,data,here'
        mock_requests_get.return_value = mock_response

        # Create an instance of UKLandClient and call the method
        client = UKLandClient("SW1A 1AA")
        downloaded_data = client.download_data()

        # Perform assertions
        self.assertEqual(downloaded_data, 'your,csv,data,here')
        mock_requests_get.assert_called_once_with('https://example.com/api/endpoint?postcode=SW1A+1AA')


if __name__ == '__main__':
    unittest.main()
