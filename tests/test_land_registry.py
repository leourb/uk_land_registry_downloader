"""Module to mock the tests"""

import unittest


class TestUKLandClient(unittest.TestCase):
    """Test the UKLandClient class."""

    @unittest.skip("Skipping Selenium-related test")
    def test_download_data_valid_postcode(self):
        """Mock function to skip test"""
        pass


if __name__ == '__main__':
    unittest.main()
