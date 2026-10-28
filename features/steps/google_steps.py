from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I open the Google homepage')
def step_impl(context):
    context.driver.get("https://www.google.com")

@when('I search for "{search_term}"')
def step_impl(context, search_term):
    search_box = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.clear()
    search_box.send_keys(search_term + Keys.RETURN)

@then('I should see search results related to "{expected_text}"')
def step_impl(context, expected_text):
    # Wait for the body to be fully loaded
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    # Break down expected text into individual keywords
    keywords = expected_text.lower().split()
    page_source = context.driver.page_source.lower()
    
    # Verify that all keywords appear somewhere in the page source
    found = all(keyword in page_source for keyword in keywords)
    
    assert found, f"Expected keywords from '{expected_text}' not found anywhere in the search results page source!"