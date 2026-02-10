import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    yield driver
    driver.quit()

def test_explicit_wait(driver):
    wait = WebDriverWait(driver, 20)

    # Click the ACTUAL button
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='start']/button"))
    ).click()

    # Wait until loading spinner disappears
    wait.until(
        EC.invisibility_of_element_located((By.ID, "loading"))
    )

    # Now safely read the result
    result = driver.find_element(By.ID, "finish") 
    assert "Hello World!" in result.text





















# =============================================================================

# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()
# def test_signup_form(driver):
#     driver.get("https://demoqa.com/automation-practice-form")

#     wait = WebDriverWait(driver, 10)

#     # First name
#     wait.until(
#         EC.visibility_of_element_located((By.ID, "firstName"))
#     ).send_keys("Akshara")

#     # Last name
#     driver.find_element(By.ID, "lastName").send_keys("Ranjith")

#     # Email
#     driver.find_element(By.ID, "userEmail").send_keys("akshara@test.com")

#     # Gender (radio button)
#     driver.find_element(By.XPATH, "//label[text()='Female']").click()

#     # Mobile number
#     driver.find_element(By.ID, "userNumber").send_keys("9876543210")

#     # Submit button – scroll + wait + click
#     submit_btn = wait.until(
#         EC.element_to_be_clickable((By.ID, "submit"))
#     )
#     driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
#     submit_btn.click()
 

# =======================================================================================
# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.get("https://the-internet.herokuapp.com/iframe")
#     yield driver
#     driver.quit()

# def test_iframe(driver):
#     wait = WebDriverWait(driver , 10)

#     frame = driver.find_element(By.ID,"mce_0_ifr")
#     driver.switch_to.frame(frame)

#     close_btn = wait.until((EC.element_to_be_clickable(By.XPATH,"//button[@aria-label = 'Close']")))
#     close_btn.click()

#     editor = wait.until((EC.visibility_of_element_located(By.ID,"tinymce")))
#     editor.clear()
#     editor.send_keys("Iframe automation completed")

#     driver.switch_to.default_content()

#     driver.find_element(By.XPATH,"//button[@aria-label = 'Bold']").click()

#     assert "iFrame" in driver.title

# ==================================================================================================

# # //test

# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome()
#     driver.get("https://the-internet.herokuapp.com/iframe")
#     yield driver
#     driver.quit()

# def test_frame(driver):
#     wait = WebDriverWait(driver,10)

#     frame = driver.find_element(By.ID,"mce_0_ifr")
#     driver.switch_to.frame(frame)

#     close_btn = wait.until(EC.element_to_be_clickable(By.XPATH,"//div[@aria-label = 'Close']"))
#     close_btn.click()

#     editor = driver.find_element(By.ID,"tinymce")
#     editor.clear()
#     editor.send_keys("Frame test successful")

#     driver.switch_to.default_content()
    
#     assert "An iFrame containing the TinyMCE WYSIWYG Editor" in driver.title

# ==================================================================================================


# @pytest.fixture()
# def driver():
#     driver=webdriver.Chrome()
#     driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#     yield driver
#     driver.quit()

# def test_alert_handling(driver):
#     driver.find_element(By.XPATH,"//button[contains(text()='JS Confirm')]").click()

#     alert = driver.switch_to.alert
#     alert_text = alert.text
#     alert.dismiss()

#     result_text = driver.find_element(By.ID,"result").click()
#     assert "Cancel" in result_text


# def test_alert_handling(driver):
#     driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
    
#     alert = driver.switch_to.alert

#     alert_text = alert.text
#     alert.accept()

#     assert "I am a JS Alert" in alert_text

# ==================================================================================================

# @pytest.fixture
# def driver():
#     driver=webdriver.Chrome()
#     driver.get("https://the-internet.herokuapp.com/login")
#     yield driver
#     driver.quit()

# def test_login(driver):
#     wait=WebDriverWait(driver,10)

#     wait.until(EC.visibility_of_element_located((By.ID,"username"))).send_keys("tomsmith")
#     driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
#     driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    
#     msg = wait.until(EC.visibility_of_element_located((By.ID,"flash"))).text
#     assert "You logged into a secure area!" in msg

# ==================================================================================================


# @pytest.fixture
# def driver():
#     driver=webdriver.Chrome()
#     driver.get("https://the-internet.herokuapp.com/login")
#     wait=webdriver.Wait
#     yield driver
#     driver.quit()

# def test_login_page(driver):
#     driver.find_element(By.ID,"username").send_keys("tomsmith")
#     driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
#     driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
#     assert "You logged into a secure area!" in driver.page_source

# def test_login_negative(driver):
#     driver.find_element(By.ID,"username").send_keys("tomsmith")
#     driver.find_element(By.ID,"password").send_keys("super")
#     driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
#     assert "Your password is invalid!" in driver.page_source

# @pytest.mark.sanity
# def test_sanity(driver):
#     assert "internet.herokuapp" in driver.current_url
#     assert "Login Page" in driver.title
