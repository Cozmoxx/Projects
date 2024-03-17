from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def get_silver_price():
    """Scrapes the current price of silver from a website.

    Returns:
        str: The price as a string in £.
    """

    # sets the browser to be headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.royalmint.com/silver-price/")

    # Waits for the silver price element to be visible.
    silver_price_element = WebDriverWait(driver, 3).until(
        ec.visibility_of_element_located(
            (By.XPATH, "//span[@class='cPrice text-LightSilver']"))
    )

    silver_price = silver_price_element.text

    driver.quit()
    return silver_price