import unittest
from unittest.mock import Mock, patch
from uk_land_property_client.land_registry import UKLandClient


class TestUKLandClient(unittest.TestCase):
    """Test the UKLandClient class."""

    @patch('uk_land_property_client.land_registry.Datashelf')
    def test_download_data_valid_postcode(self, mock_datashelf: Mock) -> None:
        """
        Test the `download_data` method for a valid postcode.
        This test case simulates the behavior of the `download_data` method in the `UKLandClient` class for a valid
        postcode. It uses mocking to simulate the behavior of the `selenium_driver` and `requests.get` methods, allowing
        the `download_data` method to be tested without actual network or Selenium interactions.
        :param Mock mock_datashelf: Mocked Datashelf class to control Selenium behavior.
        :return: a function to test the `download_data` method.
        """
        mock_driver_instance = Mock()
        mock_datashelf_instance = Mock(selenium_driver=mock_driver_instance)
        mock_datashelf.return_value = mock_datashelf_instance

        mock_driver_instance.find_element.return_value = Mock(
            send_keys=Mock(),
            click=Mock()
        )

        # Assuming 'requests.get' also needs to be mocked to return a sample CSV data
        with patch('requests.get') as mock_get:
            mock_get.return_value.text = 'your,csv,data,here'

            client = UKLandClient("SW1A 1AA")
            downloaded_data = client.downloaded_data

            self.assertIsNotNone(downloaded_data)  # You can add more assertions here


if __name__ == '__main__':
    unittest.main()
