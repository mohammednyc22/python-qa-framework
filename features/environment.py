from selenium import webdriver

def before_scenario(context, scenario):
    # Automatically launch Chrome and maximize browser window before each test scenario
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def after_scenario(context, scenario):
    # Automatically close the browser after each test scenario finishes
    if hasattr(context, 'driver'):
        context.driver.quit()