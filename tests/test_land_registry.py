import unittest
from uk_land_property_client.land_registry import UKLandClient


class TestUKLandClient(unittest.TestCase):
    """Test the UKLandClient class."""

    def test_init(self):
        # Create an instance of UKLandClient
        client = UKLandClient("SW1A 1AA")

        # Basic assertion to ensure the client was created
        self.assertIsInstance(client, UKLandClient)


if __name__ == '__main__':
    unittest.main()
