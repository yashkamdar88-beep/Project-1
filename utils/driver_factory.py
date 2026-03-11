"""
Driver Factory Module

This module is responsible for initializing and returning the appropriate
WebDriver instance based on the browser type provided.

Supported Browsers:
- Chrome
- Firefox
- Edge

Used by test setup to launch the browser before executing test cases.
"""

from selenium import webdriver


def get_driver(browser="chrome"):
    """
    Initializes and returns a WebDriver instance.

    Args:
        browser (str): Name of the browser to launch.

    Returns:
        WebDriver: Selenium WebDriver instance
    """

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()

    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()

    elif browser.lower() == "edge":
        driver = webdriver.Edge()

    else:
        raise ValueError("Unsupported browser")

    # Maximize browser window for consistent test execution
    driver.maximize_window()

    return driver