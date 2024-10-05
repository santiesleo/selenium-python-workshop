from behave import given, when, then
from selenium import webdriver
from pages.login_intu_page import LoginIntuPage
from pages.dashboard_intu_page import DashboardIntuPage

@given('the user is in the intu login page')
def step_user_is_in_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.icesi.edu.co/moodle/login/index.php")
    context.login_page = LoginIntuPage(context.driver)

@when('the user logs int with valid intu credentials')
def step_user_logs_in_valid(context):
    context.login_page.login("1112388184", "Sistemas1714")

@then('the user should be redirected to the dashboard')
def step_user_redirected_to_dashboard(context):
    dashboard_page = DashboardIntuPage(context.driver)
    assert dashboard_page.is_search_displayed()
