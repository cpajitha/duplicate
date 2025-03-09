from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Configure WebDriver for headless execution
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (important for CI/CD)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

def test_operation(num1, num2, button, expected_result):
    """Helper function to test calculator operations."""
    num1_input = driver.find_element(By.ID, "num1")
    num2_input = driver.find_element(By.ID, "num2")
    result_span = driver.find_element(By.ID, "result")

    # Clear the result field before each operation
    driver.execute_script("arguments[0].innerText = '';", result_span)

    # Enter values
    num1_input.clear()
    num1_input.send_keys(str(num1))

    num2_input.clear()
    num2_input.send_keys(str(num2))

    # Click the button
    print(f"Clicking button: {button.text}")  # Debugging
    button.click()

    # Wait for the result to update
    WebDriverWait(driver, 5).until(lambda d: result_span.text.strip() != "")

    # Get the result
    result = result_span.text.strip()
    print(f"Result: {num1} {button.text} {num2} = {result}")

    # Ensure test correctness
    assert result == str(expected_result), f"Test Failed for {button.text}: Expected {expected_result}, got {result}"

try:
    # Open the calculator page hosted in FastAPI
    frontend_url = "http://0.0.0.0:8000"  # CI/CD runs FastAPI on 0.0.0.0
    driver.get(frontend_url)

    # Wait for input fields to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "num1")))

    # Find buttons
    add_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add')]")
    subtract_button = driver.find_element(By.XPATH, "//button[contains(text(),'Subtract')]")
    multiply_button = driver.find_element(By.XPATH, "//button[contains(text(),'Multiply')]")
    divide_button = driver.find_element(By.XPATH, "//button[contains(text(),'Divide')]")

    # Perform tests
    test_operation(10, 5, add_button, 15)
    test_operation(10, 5, subtract_button, 5)
    test_operation(10, 5, multiply_button, 50)
    test_operation(10, 5, divide_button, 2)

finally:
    # Close the browser after tests
    driver.quit()
