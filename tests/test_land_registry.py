"""Module to run the unit tests"""

import pytest

import pandas as pd

from .uk_land_property_client.land_registry import UKLandClient


class TestUKLandClient:
    """Test cases for UKLandClient class."""

    def test_download_data_valid_postcode(self):
        """Test downloading data with a valid postcode."""
        client = UKLandClient("SW9 0HT")
        pandas_output = client.download_data()
        assert isinstance(pandas_output, pd.DataFrame)

    def test_download_data_invalid_postcode(self):
        """Test downloading data with an invalid postcode."""
        with pytest.raises(ValueError):
            client = UKLandClient("Invalid Postcode")
