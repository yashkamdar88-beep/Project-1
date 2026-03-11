"""
Base Page Module

This module contains the BasePage class which acts as the parent class
for all page objects in the automation framework.

Purpose:
--------
The BasePage class provides reusable methods for common browser
interactions such as clicking elements, typing text, checking element
visibility, and retrieving page information.

Benefits:
---------
- Avoids code duplication across multiple page objects
- Improves maintainability of the automation framework
- Centralizes common Selenium WebDriver actions

All page classes (HomePage, LoginPage, etc.) should inherit from this class.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    BasePage serves as the foundation for all page object classes.

    It stores the WebDriver instance and provides common methods
    that can be reused across different pages of the application.
    """

    def __init__(self, driver):
        """
        Constructor for BasePage.

        Parameters
        ----------
        driver : WebDriver
            The Selenium WebDriver instance used to control the browser.
        """
        self.driver = driver


    def click(self, locator):
        """
        Clicks a web element identified by the given XPath locator.

        Parameters
        ----------
        locator : str
            XPath locator of the element to be clicked.

        Example
        -------
        click("//button[@id='login']")
        """
        self.driver.find_element(By.XPATH, locator).click()


    def type(self, locator, text):
        """
        Enters text into an input field.

        Parameters
        ----------
        locator : str
            XPath locator of the input field.

        text : str
            Text value that will be entered into the field.

        Example
        -------
        type("//input[@name='email']", "test@example.com")
        """
        self.driver.find_element(By.XPATH, locator).send_keys(text)


    def is_visible(self, locator):
        """
        Checks whether an element is visible on the page.

        This method uses an explicit wait to ensure the element
        becomes visible before interacting with it.

        Parameters
        ----------
        locator : str
            XPath locator of the element.

        Returns
        -------
        bool
            True if the element is visible, otherwise raises a timeout error.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(("xpath", locator))
        )
        return element.is_displayed()


    def get_title(self):
        """
        Retrieves the title of the current webpage.

        Returns
        -------
        str
            Title of the webpage.
        """
        return self.driver.title


    def get_url(self):
        """
        Retrieves the current URL of the webpage.

        Returns
        -------
        str
            Current page URL.
        """
        return self.driver.current_url