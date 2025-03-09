from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver (Headless mode for GitHub Actions)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # Open calculator page hosted on localhost
    frontend_url = "http://localhost:8000/calculator.html"
    driver.get(frontend_url)

    # Wait for the input fields and button to be present
    wait = WebDriverWait(driver, 15)
    num1 = wait.until(EC.presence_of_element_located((By.ID, "num1")))
    num2 = wait.until(EC.presence_of_element_located((By.ID, "num2")))
    add_button = wait.until(EC.element_to_be_clickable((By.ID, "add")))
    result_field = wait.until(EC.presence_of_element_located((By.ID, "result")))

    # Perform addition test
    num1.send_keys("5")
    num2.send_keys("3")
    add_button.click()

    # Wait for the result field to update
    wait.until(lambda driver: result_field.get_attribute("value") != "")

    # Validate result
    result = result_field.get_attribute("value")
    assert result == "8", f"Test Failed! Expected 8 but got {result}"

    print("✅ Selenium Test Passed!")

except Exception as e:
    print("❌ Test Failed:", e)
    print("Page Source:", driver.page_source)  # Debugging info
finally:
    driver.quit()
