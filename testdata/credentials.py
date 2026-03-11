"""
Credentials Module

This module stores test credentials used for authentication
test cases in the automation test suite.

Purpose
-------
Separating credentials from test logic improves code maintainability,
reusability, and readability. Test cases can import these credentials
when performing login validation scenarios.

Test Data Covered
-----------------
1. Valid login credentials for successful authentication tests.
2. Invalid login credentials for negative test scenarios.

Note
----
In production automation frameworks, sensitive data like passwords
should be stored securely using environment variables, encrypted
vaults, or configuration management tools instead of hardcoding
them in the codebase.
"""

# ====================================
# Valid Test Credentials
# ====================================

# Registered email used for successful login test cases
valid_email = "yashkamdar88@gmail.com"

# Correct password associated with the valid_email
valid_password = "Yashkamdar@9"


# ====================================
# Invalid Test Credentials
# ====================================

# Incorrect email used to test login failure scenarios
invalid_email = "wrong@gmail.com"

# Incorrect password used to validate error handling
invalid_password = "wrong123"