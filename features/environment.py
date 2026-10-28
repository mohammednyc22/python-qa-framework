from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--remote-allow-origins=*")

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        print(f"WebDriverManager initialization failed: {e}. Falling back to default system Chrome...")
        driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(10)
    
    # Assign to both context.driver and context.browser to prevent AttributeError
    context.driver = driver
    context.browser = driver

def after_all(context):
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()
    elif hasattr(context, 'browser') and context.browser:
        context.browser.quit()