import pytest
from selenium import  webdriver
from selenium.webdriver.support.wait import  WebDriverWait
import logging

# setup logging
logging.basicConfig(
    filename="logs/TC_ALL_logs.log",
    level= logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


@pytest.fixture(scope="function")
def browser_config ():
    logging.info("Starting Browser Session...")
    driver = webdriver.Chrome()
    logging.info("Browser Launch Successfully.")

    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 20)

    driver.get("https://muntasir101.github.io/Movie-Ticket-Booking/")
    logging.info("URL Open Successfully.")

    yield driver, wait
    logging.info("Script Complete.")
    driver.quit()
    logging.info("End Browser Session...")
    logging.info("................")
    logging.info("................")


