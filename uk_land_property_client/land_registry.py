"""Main module to run the client"""

import time

from io import StringIO
from typing import Any

import pandas as pd
import requests

from .datashelf import Datashelf


class UKLandClient(Datashelf):
    """Class to query the data"""

    def __init__(self, postcode: str) -> None:
        """
        Initialize the client
        :param str postcode: postcode used to query the data
        :return: an instance of the UKLandClient class
        """
        super().__init__()
        self._postcode = postcode
        self._gather_target_url = self._gather_url()
        self.downloaded_data = self.download_data()

    def _gather_url(self) -> str:
        """Download the data from the HM Land Registry Website"""
        self.selenium_driver.get(self.main_url)
        postcode = self.selenium_driver.find_element(
            'id',
            'postcode'
        )
        postcode.send_keys(self.postcode)
        show_all_button = self.selenium_driver.find_element(
                "css selector",
                'input[name="limit"][value="all"]'
            )
        show_all_button.click()
        submit_button = self.selenium_driver.find_element(
            "css selector",
            'button.button[type="submit"]'
        )
        submit_button.click()
        time.sleep(2)
        download_button = self.selenium_driver.find_element(
                "css selector",
                'a.button.button--secondary[href^="/app/ppd/ppd_data"]'
            )
        download_button.click()
        time.sleep(2)
        download_buttons = self.selenium_driver.find_elements(
                'xpath',
                "//a[contains(@class, 'button') and contains(@href, '.csv')]"
            )
        get_all_records_on_csv = download_buttons[-1]
        get_all_records_on_csv.click()
        return self.selenium_driver.current_url

    def download_data(self) -> pd.DataFrame or dict[Any]:
        """Download the data from the url specified"""
        self.selenium_driver.quit()
        csv_data = requests.get(self.target_url)
        return pd.read_csv(StringIO(csv_data.text))

    @property
    def postcode(self) -> str:
        """Postcode property function to search postcode property"""
        return self._postcode

    @postcode.setter
    def postcode(self, postcode: str) -> None:
        """
        Postcode setter function to set postcode property
        :param str postcode: postcode function to validate
        :return: the postcode variable fully validated
        """
        if not isinstance(postcode, str):
            raise TypeError(f'Postcode needs to be string! {str(postcode)} is {type(postcode)}')
        if not postcode:
            raise ValueError('Postcode cannot be blank')
        if self.validate_postcode(postcode):
            raise ValueError(f'Postcode {postcode} is not valid')
        self._postcode = postcode

    @property
    def target_url(self) -> str:
        """Postcode property function to return the gathered URL with the data to be downloaded"""
        return self._gather_target_url
