from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_valid_login(driver):
    login = LoginPage(driver)

    login.login("Admin","admin123")

    # assert "dashboard" in driver.current_url.lower()

#def test_invalid_login(driver):
    # login = LoginPage(driver)

    # login.login("Admin","wrongpassword")

    # assert "invalid credentials" in login.get_error_message().lower()
    

    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_displayed