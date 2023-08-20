"""Module to run the unit tests"""

from unittest.mock import Mock, patch

import pandas as pd

from uk_land_property_client.land_registry import UKLandClient


class TestUKLandClient:
    """Test cases for UKLandClient class."""

    @patch('selenium.webdriver.Firefox')
    def test_download_data_valid_postcode(self, mock_firefox: Mock) -> None:
        """
        Test downloading data with a valid postcode.
        :param Mock mock_firefox: The mock object that simulates webdriver.Firefox.
        :return: If the mock object is not called as expected, or if the download_data method does not return a DataFrame
        """
        fake_driver = Mock()
        fake_driver.get = Mock()
        mock_firefox.return_value = fake_driver
        client = UKLandClient("WC1B 3DG")
        pandas_output = client.download_data()
        assert isinstance(pandas_output, pd.DataFrame)
        mock_firefox.assert_called_once()
        fake_driver.get.assert_called_with("https://www.gov.uk/search-property-information-land-registry")