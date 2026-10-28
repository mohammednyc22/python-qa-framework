from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    options = Options()
    options.add_argument("--headless=new")     # Run in headless mode for CI/CD servers
    options.add_argument("--no-sandbox")       # Bypass OS security model limitations
    options.add_argument("--disable-dev-shm-usage") # Overcome limited resource/memory issues
    options.add_argument("--disable-gpu")      # Applicable for headless environments
    
    context.browser = webdriver.Chrome(options=options)

def after_all(context):
    if hasattr(context, 'browser'):
        context.browser.quit()