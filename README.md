# UK Property Transaction Data Downloader Package

The **UK Property Transaction Data Downloader** is a Python package that allows you to automate the process of downloading property transaction data from the HM Land Registry website for a specified UK postcode. This package utilizes the Selenium library for web automation and Pandas for data handling.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [License](#license)

## Installation

You can install the **UK Property Transaction Data Downloader** package using `pip`. Open your terminal and run the following command:

```bash
pip install uk-property-downloader
```

## Usage

Once you've installed the package, you can use it in your Python scripts as follows:

```python
from uk_property_downloader import UKLandClient

# Specify the UK postcode for which you want to download property transaction data
postcode = "XXX YYY"  # Replace with your desired postcode

# Initialize the UKLandClient with the specified postcode
client = UKLandClient(postcode)

# Download property transaction data and store it in a pandas DataFrame
data_frame = client.downloaded_data

# Now you can work with the downloaded data
print(data_frame.head())  # Print the first few rows of the DataFrame
```

The `UKLandClient` class provides a simple and convenient way to interact with the HM Land Registry website and download property transaction data for a given postcode.

## Requirements

- Python 3.x
- Selenium: A Python library for browser automation.
- Pandas: A data manipulation library.

Make sure to have the necessary web drivers installed for Selenium to work properly. The script uses different web drivers based on the operating system:
- Safari for macOS
- Chrome for Windows
- Firefox for Linux

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
