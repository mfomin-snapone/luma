import os
import time
from selenium.webdriver.common.keys import Keys
from locators import Elements
from selenium import webdriver
import resets
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime

# output_file_name = input("Enter log file name: ")
# output_file_path = "/Users/mark.fomin/Documents/Wattbox/{}.txt".format(output_file_name)
# outputFile = open(output_file_path, "a+")


def get_timestamp():
    dt = datetime.datetime.now()
    print_timestamp = dt.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    return print_timestamp


sleep_counter = 0
loop_counter = input("Enter number of loops: ")
start_script_choice = input("Start script? y/n: ")
entered_loops = input("Enter number of loops: ")
screenshot_counter = 0
screenshot_counter = screenshot_counter + 1


options = Options()
capabilities = DesiredCapabilities.CHROME
capabilities["pageLoadStrategy"] = "none"
driver = webdriver.Chrome()
driver.implicitly_wait(10)

if start_script_choice == 'Y' or start_script_choice == 'y':
    for x in range(0, int(loop_counter)):

        driver.get(Elements.url)
        time.sleep(2)

        # Entering username
        driver.find_element(*Elements.login_username).send_keys("admin")

        # Entering password
        driver.find_element(*Elements.login_password).send_keys("Snapav704")
        time.sleep(1)
        # Selecting login button
        driver.find_element(*Elements.login_button).click()
        time.sleep(5)
        driver.find_element(*Elements.settings_button).click()
        time.sleep(2)
        driver.find_element(*Elements.maintenance_menu).click()
        time.sleep(2)
        driver.find_element(*Elements.reboot_button).click()
        time.sleep(2)
        driver.find_element(*Elements.reboot_popup_ok_option).click()
        time.sleep(55)
        resets.poe_port_reset()

        time.sleep(60)
        driver.start_session(capabilities=capabilities)
        driver.get(Elements.url)
        time.sleep(2)

        # Entering username
        driver.find_element(*Elements.login_username).send_keys("admin")

        # Entering password
        driver.find_element(*Elements.login_password).send_keys("Snapav704")
        time.sleep(1)
        # Selecting login button
        driver.find_element(*Elements.login_button).click()
        time.sleep(5)

        driver.get_screenshot_as_file("Loop " + str(screenshot_counter))

driver.quit()
