"""
Home Page Module

This module contains the HomePage class which represents the
main landing page of the GUVI website.

Purpose
-------
The HomePage class stores all the web element locators and actions
that can be performed on the homepage.

Functionalities Covered
-----------------------
1. Clicking Login button
2. Clicking Sign Up button
3. Verifying navigation menu items
4. Verifying the Dobby chat assistant widget
5. Logging out a logged-in user

This class inherits common browser actions from the BasePage class.
"""

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    """
    Page Object representing the GUVI homepage.

    Contains locators and methods to interact with homepage elements
    such as navigation menus, login/signup buttons, chatbot widget,
    and user profile actions.
    """

    # ===============================
    # Locators for homepage elements
    # ===============================

    # Login button displayed on homepage
    login_button = "//button[contains(text(),'Login')]"

    # Sign up button for new users
    signup_button = "//button[contains(text(),'Sign up')]"

    # Top navigation menu items
    courses_menu = "//p[text()='Courses']"
    live_classes_menu = "//p[text()='LIVE Classes']"
    practice_menu = "//p[text()='Practice']"

    # Dobby AI assistant chat widget icon
    dobby_widget = "//span[@class='siqico-chat zsiq-chat-icn']"

    # Profile avatar icon visible after successful login
    profile_menu = "//img[contains(@class,'gravatar')]"

    # Logout button inside the user profile dropdown
    logout_button = "//div[@id='signout']"


    # ===============================
    # Page Actions
    # ===============================

    def click_login(self):
        """
        Clicks the Login button on the homepage.

        This action navigates the user to the login page
        where authentication credentials can be entered.
        """
        self.click(self.login_button)


    def click_signup(self):
        """
        Clicks the Sign Up button.

        This navigates the user to the registration page
        where a new account can be created.
        """
        self.click(self.signup_button)


    def verify_menu_items(self):
        """
        Verifies that key navigation menu items are visible.

        Menu items verified:
        - Courses
        - LIVE Classes
        - Practice

        Returns
        -------
        bool
            True if all menu items are visible, otherwise False.
        """

        return (
            self.is_visible(self.courses_menu) and
            self.is_visible(self.live_classes_menu) and
            self.is_visible(self.practice_menu)
        )


    def verify_dobby(self):
        """
        Verifies the visibility of the Dobby chat assistant widget.

        The Dobby widget is an AI chatbot provided on the homepage
        to assist users with queries and navigation.

        Returns
        -------
        bool
            True if the Dobby widget is visible.
        """

        return self.is_visible(self.dobby_widget)

    def logout(self):
        """
        Logs out the currently authenticated user.

        Steps:
        1. Click profile avatar
        2. Wait for dropdown menu
        3. Click logout option
        """

        wait = WebDriverWait(self.driver, 15)

        # Click profile avatar
        profile = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.profile_menu))
        )
        profile.click()

        # Small wait for dropdown animation
        import time
        time.sleep(2)

        # Locate logout button
        logout = wait.until(
            EC.presence_of_element_located((By.XPATH, self.logout_button))
        )

        # Scroll to element
        self.driver.execute_script("arguments[0].scrollIntoView(true);", logout)

        # Click logout using JS
        self.driver.execute_script("arguments[0].click();", logout)