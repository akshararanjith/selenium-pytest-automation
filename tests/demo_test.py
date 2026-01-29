from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option(
    "prefs",
    {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
)

# Launch browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

wait = WebDriverWait(driver, 10)

try:
    # Open site
    driver.get("https://www.saucedemo.com")

    # Login
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Add product to cart
    wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()

    # Open cart
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="shopping-cart-link"]'))
    ).click()

    # Verify product in cart
    product_name = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
        )
    )

    print("Product found in cart:", product_name.text)

    expected_product = "Sauce Labs Backpack"

    if product_name.text.strip() == expected_product:
        print("Product successfully added to cart")
    else:
        print("Product NOT added to cart")

finally:
    driver.quit()
