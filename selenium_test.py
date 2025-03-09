from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Set up WebDriver with automatic driver management
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode for CI
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def test_operation(num1, num2, button, expected_result):
    """Helper function to test calculator operations."""
    try:
        num1_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "num1")))
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
        print(f"Clicking button: {button.text}")
        button.click()

        # Wait for the result to update
        WebDriverWait(driver, 10).until(lambda d: result_span.text.strip() != "")

        # Get the result
        result = result_span.text.strip()
        print(f"Result: {num1} {button.text} {num2} = {result}")

        # Ensure test correctness
        assert result == str(expected_result), f"Test Failed for {button.text}: Expected {expected_result}, got {result}"
    
    except TimeoutException:
        print("Timeout: Element not found or result not updated.")
        print("Page Source:\n", driver.page_source)

try:
    # Open the calculator page
    frontend_path = "file:///C:/Users/cpaji/OneDrive/Desktop/mtech/Software%20testing_seminar/Software%20testing_seminar/Code/calculator.html"
    driver.get(frontend_path)

    # Wait for input fields
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "num1")))

    # Find buttons
    add_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add')]")
    subtract_button = driver.find_element(By.XPATH, "//button[contains(text(),'Subtract')]")
    multiply_button = driver.find_element(By.XPATH, "//button[contains(text(),'Multiply')]")
    divide_button = driver.find_element(By.XPATH, "//button[contains(text(),'Divide')]")

    # Test cases
    test_operation(10, 0, add_button, 10)       # Addition Test
    test_operation(10, 5, subtract_button, 5)   # Subtraction Test
    test_operation(10, 5, multiply_button, 50)  # Multiplication Test
    test_operation(10, 5, divide_button, 2)     # Division Test

except TimeoutException:
    print("Timeout: Element not found or result not updated.")
    print("Page Source:\n", driver.page_source)

finally:
    driver.quit()
