import logging

import pytest

from utils.screenshot_utils import capture_full_page_screenshot
from pages.booking_page import BookingPage


def test_tc_tb_003(browser_config):
    logging.info("TC_TB_003 Started..")
    driver, wait = browser_config

    # create object for BookingPage class
    booking_page = BookingPage(driver,wait)

    # 2. Enter a valid Number of Tickets
    try:
        booking_page.enter_number_of_tickets(11)
        logging.info("Ticket Number Enter successfully.")
    except Exception as e:
        logging.info("Element 'Number of Tickets' not found with Explicit wait.")
        pytest.fail("Test Failed.Bug found for Ticket Number !!!")

    # 3. Select valid Ticket Class
    try:
        booking_page.select_ticket_class("750")
        logging.info("Ticket Class Silver - $750 selected.")
    except Exception as e:
        logging.info("Element 'Ticket Class' not found with Explicit wait.")
        pytest.fail("Test Failed.Bug found for Ticket Class !!!")

    # 4. Select valid registered user
    try:
        booking_page.select_registered_user("yes")
        logging.info("Registered User - 'Yes' selected.")

    except Exception as e:
        logging.info("Element 'Register User' not found with Explicit wait.")
        pytest.fail("Test Failed.Bug found for Register User !!!")

    # 5. Enter a valid Promo Code
    try:
        booking_page.enter_promo_code("PROMO2025")
        logging.info("Valid Promo Code Enter successfully.")

    except Exception as e:
        logging.info("Element 'Promo Code' not found with Explicit wait.")
        pytest.fail("Test Failed.Bug found for Promo Code !!!")

    # 6. Click on the "Book Now" button.
    try:
        booking_page.click_book_button()
        logging.info("Click on Book Now button successfully.")

    except Exception as e:
        logging.info("Element 'Book now' button not found with Explicit wait.")
        # Screenshot
        capture_full_page_screenshot(driver, "TC_TB_03")
        pytest.fail("Test Failed.Bug found for Book Now Button !!!")


    # Validate Ticket Number error message
    expected_error_message = "Please enter a number between 1 and 10."

    if expected_error_message == booking_page.get_ticket_error_message():
        logging.info("Test Passed. Error Message for Ticket Number found.")

    else:
        logging.info("Test Failed. Expected Error Message not match with Actual Error Message.")
        # Screenshot
        capture_full_page_screenshot(driver, "TC_TB_03")

    logging.info("TC_TB_003 Completed..")