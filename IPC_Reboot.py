import os
import time
from selenium.webdriver.common.keys import Keys
from locators import Elements
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime

output_file_name = "Logs"
output_file_path = os.getcwd() + "\\logs\\{}.txt".format(output_file_name)
outputFile = open(output_file_path, "a+")


def get_timestamp():
    dt = datetime.datetime.now()
    print_timestamp = dt.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    return print_timestamp


ip_address = '192.168.7.187'
url = "http://{}/".format(ip_address)
loop_counter = 20
start_script_choice = 'y'
script_loop_count = 0
screenshot_counter = 0

options = Options()
capabilities = DesiredCapabilities.CHROME
capabilities["pageLoadStrategy"] = "normal"
driver = webdriver.Chrome()
driver.implicitly_wait(10)

if start_script_choice == 'Y' or start_script_choice == 'y':
    for x in range(0, int(loop_counter)):
        script_loop_count = script_loop_count + 1
        print(get_timestamp(), "Starting script! Loop Interval: " + str(script_loop_count))
        print(get_timestamp(), "Starting script!", file=outputFile)
        screenshot_counter = screenshot_counter + 1
        driver.get(url)
        time.sleep(2)

        # Entering username
        driver.find_element(*Elements.login_username).send_keys("admin")
        print(get_timestamp(), "Entering username")
        print(get_timestamp(), "Entering username", file=outputFile)
        # Entering password
        driver.find_element(*Elements.login_password).send_keys("Snapav704")
        print(get_timestamp(), "Entering password")
        print(get_timestamp(), "Entering password", file=outputFile)
        time.sleep(1)
        # Selecting login button
        driver.find_element(*Elements.login_button).click()
        print(get_timestamp(), "Logging in")
        print(get_timestamp(), "Logging in", file=outputFile)
        time.sleep(5)
        driver.find_element(*Elements.settings_button).click()
        print(get_timestamp(), "Selecting Settings")
        print(get_timestamp(), "Selecting Settings", file=outputFile)
        time.sleep(2)
        driver.find_element(*Elements.maintenance_menu).click()
        print(get_timestamp(), "Selecting Maintenance menu")
        print(get_timestamp(), "Selecting Maintenance menu", file=outputFile)
        time.sleep(2)
        driver.find_element(*Elements.reboot_button).click()
        print(get_timestamp(), "Selecting Reboot button")
        print(get_timestamp(), "Selecting Reboot button", file=outputFile)
        time.sleep(2)
        driver.find_element(*Elements.reboot_popup_ok_option).send_keys(Keys.ENTER)
        print(get_timestamp(), "Device Rebooting! Please wait...")
        print(get_timestamp(), "Device Rebooting! Please wait...", file=outputFile)
        time.sleep(60)

        print(get_timestamp(), "Re-launching web browser!")
        print(get_timestamp(), "Re-launching web browser!", file=outputFile)
        driver.close()
        driver.start_session(capabilities=capabilities)
        driver.get(url)
        print(get_timestamp(), "Sending DUT address to browser")
        print(get_timestamp(), "Sending DUT address to browser", file=outputFile)
        time.sleep(5)

        # Entering username
        driver.find_element(*Elements.login_username).send_keys("admin")
        print(get_timestamp(), "Entering username")
        print(get_timestamp(), "Entering username", file=outputFile)
        # Entering password
        driver.find_element(*Elements.login_password).send_keys("Snapav704")
        print(get_timestamp(), "Entering password")
        print(get_timestamp(), "Entering password", file=outputFile)
        time.sleep(1)
        # Selecting login button
        driver.find_element(*Elements.login_button).click()
        print(get_timestamp(), "Login button selected")
        print(get_timestamp(), "Login button selected", file=outputFile)
        time.sleep(15)
        screenshot_file = "Loop " + str(screenshot_counter) + ".png"
        driver.get_screenshot_as_file('Screenshots\\' + screenshot_file)
        print(get_timestamp(), "Post-Loop Screenshot taken: " + str(screenshot_counter))
        print(get_timestamp(), "Post-Loop Screenshot taken: " + str(screenshot_counter), file=outputFile)
        time.sleep(2)
        driver.close()
        driver.start_session(capabilities=capabilities)
        print(get_timestamp(), "Loop Finished!")
        print(get_timestamp(), "Loop Finished!", file=outputFile)


print(get_timestamp(), "Script Finished!")
print(get_timestamp(), "Script Finished!", file=outputFile)

driver.quit()
