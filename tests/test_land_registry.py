import unittest
from unittest.mock import Mock, patch
from uk_land_property_client.land_registry import UKLandClient
from selenium.webdriver.chrome.options import Options


class TestUKLandClient(unittest.TestCase):
    """Test the UKLandClient class."""

    @patch('uk_land_property_client.land_registry.Datashelf')
    @patch('selenium.webdriver.chrome.webdriver.WebDriver')
    def test_download_data_valid_postcode(self, mock_webdriver, mock_datashelf: Mock) -> None:
        """
        Test the `download_data` method for a valid postcode.
        This test case simulates the behavior of the `download_data` method in the `UKLandClient` class for a valid
        postcode. It uses mocking to simulate the behavior of the `selenium_driver` and `requests.get` methods, allowing
        the `download_data` method to be tested without actual network or Selenium interactions.
        :param Mock mock_datashelf: Mocked Datashelf class to control Selenium behavior.
        :return: None
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

            # Set Chrome options for headless mode and specify binary
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.binary_location = '/path/to/chrome/binary'  # Update with actual path

            # Use the context manager to temporarily patch the WebDriver behavior
            with mock_webdriver as mock_webdriver_instance:
                mock_webdriver_instance.return_value = mock_driver_instance
                client = UKLandClient("SW1A 1AA")
                downloaded_data = client.downloaded_data

                self.assertIsNotNone(downloaded_data)  # You can add more assertions here


if __name__ == '__main__':
    unittest.main()
