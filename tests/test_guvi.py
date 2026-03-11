"""
GUVI Web Application Automation Test Suite

This test module contains automated UI test cases for validating
core functionality of the GUVI website.

Automation Stack
----------------
Test Framework : Pytest
Automation Tool: Selenium WebDriver
Design Pattern : Page Object Model (POM)

Test Coverage
-------------
1. URL validation
2. Page title verification
3. Login button visibility
4. Signup button visibility
5. Signup page navigation
6. Valid login authentication
7. Invalid login error validation
8. Navigation menu verification
9. Dobby AI assistant widget verification
10. Login and Logout workflow

Each test case interacts with the application using Page Object
classes to maintain clean and reusable automation code.
"""

import pytest
from utils.driver_factory import get_driver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from testdata.credentials import *
from selenium.webdriver.support.ui import WebDriverWait


# =========================================
# Application Base URL
# =========================================
URL = "https://www.guvi.in"


# =========================================
# Pytest Fixture for Browser Setup
# =========================================
@pytest.fixture
def setup():
    """
    Pytest fixture responsible for browser setup and teardown.

    Steps
    -----
    1. Initialize browser using driver factory
    2. Navigate to GUVI homepage
    3. Provide driver instance to test cases
    4. Close browser after test execution

    Returns
    -------
    WebDriver instance
    """

    driver = get_driver("chrome")

    # Open the application URL
    driver.get(URL)

    # Provide driver to the test case
    yield driver

    # Close browser after test execution
    driver.quit()


# =========================================
# Test Case 1 : Validate Website URL
# =========================================
def test_url_valid(setup):
    """
    Verify that the application URL loads correctly.

    Expected Result:
    URL should start with https://www.guvi.in
    """

    driver = setup
    assert driver.current_url.startswith("https://www.guvi.in")


# =========================================
# Test Case 2 : Validate Page Title
# =========================================
def test_title(setup):
    """
    Verify that the homepage title contains 'GUVI'.

    Expected Result:
    Page title should contain the keyword 'GUVI'.
    """

    driver = setup
    home = HomePage(driver)

    assert "GUVI" in home.get_title()


# =========================================
# Test Case 3 : Validate Login Button
# =========================================
def test_login_button(setup):
    """
    Verify that the Login button is visible on the homepage.
    """

    home = HomePage(setup)

    assert home.is_visible(home.login_button)


# =========================================
# Test Case 4 : Validate Signup Button
# =========================================
def test_signup_button(setup):
    """
    Verify that the Sign Up button is visible on the homepage.
    """

    home = HomePage(setup)

    assert home.is_visible(home.signup_button)


# =========================================
# Test Case 5 : Verify Signup Navigation
# =========================================
def test_signup_navigation(setup):
    """
    Verify that clicking the Sign Up button redirects
    the user to the registration page.

    Expected Result:
    URL should contain the word 'register'.
    """

    home = HomePage(setup)

    # Click the Sign Up button
    home.click_signup()

    # Wait until navigation happens
    WebDriverWait(setup, 10).until(
        lambda driver: "register" in driver.current_url
    )

    assert "register" in setup.current_url


# =========================================
# Test Case 6 : Valid Login Test
# =========================================
def test_valid_login(setup):
    """
    Verify that a user can login with valid credentials.

    Expected Result:
    User should be successfully logged in and redirected
    away from the login page.
    """

    home = HomePage(setup)

    # Navigate to login page
    home.click_login()

    login = LoginPage(setup)

    # Perform login with valid credentials
    login.login(valid_email, valid_password)

    # Wait for successful login redirection
    WebDriverWait(setup, 15).until(
        lambda d: "guvi.in" in d.current_url
    )

    assert setup.current_url != "https://www.guvi.in/sign-in/"


# =========================================
# Test Case 7 : Invalid Login Test
# =========================================
def test_invalid_login(setup):
    """
    Verify that login fails with invalid credentials.

    Expected Result:
    Error message should be displayed.
    """

    home = HomePage(setup)
    home.click_login()

    login = LoginPage(setup)

    # Attempt login with incorrect credentials
    login.login(invalid_email, invalid_password)

    # Validate login failure
    assert login.login_failed()


# =========================================
# Test Case 8 : Verify Navigation Menu Items
# =========================================
def test_menu_items(setup):
    """
    Verify that important navigation menu items are visible.

    Menu Items Checked:
    - Courses
    - LIVE Classes
    - Practice
    """

    home = HomePage(setup)

    assert home.verify_menu_items()


# =========================================
# Test Case 9 : Verify Dobby Assistant
# =========================================
def test_dobby_assistant(setup):
    """
    Verify that the Dobby AI assistant widget
    is visible on the homepage.
    """

    home = HomePage(setup)

    assert home.verify_dobby()


# =========================================
# Test Case 10 : Login and Logout Workflow
# =========================================
def test_login_logout(setup):
    """
    Verify that a user can successfully login
    and logout from the application.

    Test Flow
    ---------
    1. Navigate to login page
    2. Login using valid credentials
    3. Wait for dashboard/homepage
    4. Logout from profile menu
    5. Verify redirection to login or homepage
    """

    home = HomePage(setup)

    # Navigate to login page
    home.click_login()

    login = LoginPage(setup)

    # Perform login
    login.login(valid_email, valid_password)

    # Wait for dashboard/homepage after login
    WebDriverWait(setup, 10).until(
        lambda driver: "dashboard" in driver.current_url
        or "guvi.in" in driver.current_url
    )

    # Perform logout
    home.logout()

    # Wait for redirect after logout
    WebDriverWait(setup, 10).until(
        lambda driver: "sign-in" in driver.current_url
        or "guvi.in" in driver.current_url
    )

    # Validate logout redirection
    assert "sign-in" in setup.current_url or "guvi.in" in setup.current_url