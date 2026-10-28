from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    chrome_options = Options()
    # Required flags for headless Chrome in Linux/Jenkins environments
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--remote-allow-origins=*")

    try:
        # Use webdriver-manager to auto-fetch matching driver
        service = Service(ChromeDriverManager().install())
        context.browser = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        # Fallback: attempt direct system ChromeDriver if manager fails
        print(f"WebDriverManager failed with: {e}. Trying direct Chrome init...")
        context.browser = webdriver.Chrome(options=chrome_options)

    context.browser.implicitly_wait(10)

def after_all(context):
    if hasattr(context, 'browser'):
        context.browser.quit()