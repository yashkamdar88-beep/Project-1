"""
Login Page Module

This module contains the LoginPage class which represents
the login page of the GUVI website.

Purpose
-------
The LoginPage class stores the web element locators and actions
related to user authentication such as entering credentials and
submitting the login form.

Functionalities Covered
-----------------------
1. Entering email and password
2. Clicking the login button
3. Validating login failure error message

This class inherits common browser actions from the BasePage class.
"""

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    """
    Page Object representing the GUVI Login Page.

    This class encapsulates all interactions that can be performed
    on the login screen such as entering credentials and verifying
    login error messages.
    """

    # ===============================
    # Locators for Login Page Elements
    # ===============================

    # Input field where users enter their registered email address
    email_field = "//input[@id='email']"

    # Input field where users enter their account password
    password_field = "//input[@id='password']"

    # Login button used to submit authentication credentials
    login_btn = "//a[@id='login-btn']"

    # Error message displayed when login credentials are incorrect
    error_message = "//div[contains(text(),'Incorrect')]"


    # ===============================
    # Page Actions
    # ===============================

    def login(self, email, password):
        """
        Performs the login action using the provided credentials.

        Steps Performed
        ---------------
        1. Wait for the email input field to become visible.
        2. Enter the user's email address.
        3. Wait for the password input field to become visible.
        4. Enter the user's password.
        5. Wait for the login button to become clickable.
        6. Click the login button to submit the form.

        Parameters
        ----------
        email : str
            Registered user email address.

        password : str
            User account password.
        """

        wait = WebDriverWait(self.driver, 20)

        # Wait until the email input field is visible
        email_box = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.email_field))
        )
        email_box.send_keys(email)

        # Wait until the password input field is visible
        password_box = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.password_field))
        )
        password_box.send_keys(password)

        # Wait until the login button becomes clickable
        login_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.login_btn))
        )
        login_button.click()


    def login_failed(self):
        """
        Verifies whether the login attempt has failed.

        This method waits for an error message to appear when
        invalid credentials are entered.

        Expected Behavior
        -----------------
        If incorrect email or password is provided, the application
        displays an error message indicating login failure.

        Returns
        -------
        bool
            True if the login error message is displayed.
        """

        wait = WebDriverWait(self.driver, 10)

        # Wait for the login error message to appear
        error = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.error_message))
        )

        return error.is_displayed()