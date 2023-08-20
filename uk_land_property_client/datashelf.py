"""Static Data Module"""

import platform
import re

from typing import Union

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.safari.webdriver import WebDriver as SafariWebDriver


class Datashelf:
    """Static Data Module"""

    def __init__(self) -> None:
        """
        Datashelf class constructor
        :param str postcode: Postcode to search property transactions for
        :return: an intialized instance of the Datashelf class
        """
        self._selenium_driver = self._initialize_driver()
        self._main_url = 'https://landregistry.data.gov.uk/app/ppd'

    @staticmethod
    def _initialize_driver() -> Union[SafariWebDriver, ChromeWebDriver, FirefoxWebDriver]:
        """Initialize the Selenium browser by choosing the browser according to the OS"""
        if platform.system() == "Darwin":
            return webdriver.Safari()
        elif platform.system() == "Windows":
            return webdriver.Chrome()
        elif platform.system() == "Linux":
            return webdriver.Firefox()

    @property
    def selenium_driver(self) -> Union[SafariWebDriver, ChromeWebDriver, FirefoxWebDriver]:
        """Returns the Selenium driver"""
        return self._selenium_driver

    @staticmethod
    def validate_postcode(postcode: str) -> bool:
        """
        Validates a postcode
        :param str postcode: postcode to validate
        :return: a boolean indicating if the postcode is valid
        """
        if re.match(r'^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) '
                    r'?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} '
                    r'?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$', postcode):
            return True
        return False

    @property
    def main_url(self) -> str:
        """Returns the main URL"""
        return self._main_url
