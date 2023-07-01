import pytest
from selenium import webdriver


@pytest.mark.parametrize("invalid_input", ["abc123", "!@#$%", "1234567890"])
def test_login_negative(invalid_input):
    # Set up the WebDriver (e.g., ChromeDriver)
    driver = webdriver.Chrome()

    # Navigate to the login page
    driver.get("https://www.example.com/login")

    # Enter invalid input in the username field
    username_input = driver.find_element_by_id("username")
    username_input.clear()
    username_input.send_keys(invalid_input)

    # Enter valid input in the password field
    password_input = driver.find_element_by_id("password")
    password_input.clear()
    password_input.send_keys("valid_password")

    # Submit the form
    submit_button = driver.find_element_by_id("submit")
    submit_button.click()

    # Assert that the login failed or an appropriate error message is displayed
    assert "Login failed" in driver.page_source or "Invalid username" in driver.page_source

    # Close the browser
    driver.quit()
