import unittest
from uk_land_property_client.land_registry import UKLandClient

class TestUKLandClient(unittest.TestCase):
    """Test the UKLandClient class."""

    @unittest.skip("Skipping Selenium-related test")
    def test_download_data_valid_postcode(self):
        pass

if __name__ == '__main__':
    unittest.main()
