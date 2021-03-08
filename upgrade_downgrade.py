import os
import time
from locators import WebElements
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime

output_file_name = input("Enter log file name: ")
output_file_path = "/Users/mark.fomin/Documents/Wattbox/{}.txt".format(output_file_name)
outputFile = open(output_file_path, "a+")


def get_timestamp():
    dt = datetime.datetime.now()
    print_timestamp = dt.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    return print_timestamp


# counter variables
upgrade_counter = 0
sleep_counter = 0
upgrade_fw_version = input("Enter upgrade/downgrade firmware version expected: ")
dummy_fw_version = input("Enter dummy firmware version expected: ")

print(get_timestamp(), "Script started!")
print(get_timestamp(), "Script started!", file=outputFile)

options = Options()
capa = DesiredCapabilities.FIREFOX
capa["pageLoadStrategy"] = "none"
driver = webdriver.Firefox()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

# Navigate to web interface
driver.get(WebElements.url)
time.sleep(2)
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(WebElements.cur_fw_version))
# Variables that read current current firmware version, mac address and service tag.
fw = driver.find_element(*WebElements.cur_fw_version).text
mac_address = driver.find_element(*WebElements.mac).text
service_tag = driver.find_element(*WebElements.st).text
wb_model = driver.find_element(*WebElements.model).text

# Logging to terminal, then text file.
print(get_timestamp(),
      "Current Device Info is: " + fw + ' | ' + wb_model + ' | ' + mac_address + ' | ' + service_tag)
print(get_timestamp(),
      "Current Device Info is: " + fw + ' | ' + wb_model + ' | ' + mac_address + ' | ' + service_tag,
      file=outputFile)
time.sleep(2)

# Selecting Update button
driver.find_element(*WebElements.update).click()
time.sleep(2)
print(get_timestamp(), "Clicked Update button...")
print(get_timestamp(), "Clicked Update button...", file=outputFile)

# Choose file button clicked and firmware file attached
driver.find_element(*WebElements.choose_file).send_keys(os.getcwd() + WebElements.wifi_fw)
time.sleep(2)

print(get_timestamp(), "Firmware file attached...")
print(get_timestamp(), "Firmware file attached...", file=outputFile)

# Enter instead click() to bypass element load strategy for fault insertion.
driver.find_element(*WebElements.upload).click()
print(get_timestamp(), "Upload Button clicked...")
print(get_timestamp(), "Upload button clicked...", file=outputFile)

# Waiting couple minutes for device to boot up and recover
print(get_timestamp(), "Firmware uploaded! Please wait for firmware to load.")
print(get_timestamp(), "Firmware uploaded! Please wait for firmware to load.", file=outputFile)
time.sleep(180)

driver.close()
print(get_timestamp(), "Re-launching browser!")
print(get_timestamp(), "Re-launching browser!", file=outputFile)
time.sleep(2)

driver.start_session(capabilities=capa)
driver.get(WebElements.url)
time.sleep(2)

# Device Information variables
fw = driver.find_element(*WebElements.cur_fw_version).text
mac_address = driver.find_element(*WebElements.mac).text
service_tag = driver.find_element(*WebElements.st).text
wb_model = driver.find_element(*WebElements.model).text

# Checking and logging/printing device information
print(get_timestamp(),
      "Current Device Info is: " + fw + ' | ' + wb_model + ' | ' + mac_address + ' | ' + service_tag)
print(get_timestamp(),
      "Current Device Info is: " + fw + ' | ' + wb_model + ' | ' + mac_address + ' | ' + service_tag,
      file=outputFile)
time.sleep(2)

# Firmware version check logic
if fw == upgrade_fw_version:
    print(get_timestamp(), "Firmware Upgrade Successful!")
    print(get_timestamp(), "Firmware Upgrade Successful!", file=outputFile)
else:
    print("Firmware Upgrade failed! Current firmware is: " + fw)
    driver.quit()
    exit()

print(get_timestamp(), " Upgrade process Finished! Starting dummy firmware load.")
print(get_timestamp(), "Upgrade process Finished! Starting dummy firmware load.", file=outputFile)

driver.get(WebElements.url)
time.sleep(2)

fw = driver.find_element(*WebElements.cur_fw_version).text
mac_address = driver.find_element(*WebElements.mac).text
service_tag = driver.find_element(*WebElements.st).text
wb_model = driver.find_element(*WebElements.model).text

# Logging to terminal, then text file.
print(get_timestamp(),
      "Current Device Info is: " + fw + ' | ' + wb_model + ' | ' + mac_address + ' | ' + service_tag)
print(get_timestamp(),
      "Current Device Info is: " + fw + ' | ' + wb_model + ' | ' + mac_address + ' | ' + service_tag,
      file=outputFile)
time.sleep(2)
driver.find_element(*WebElements.update).click()
time.sleep(2)
print(get_timestamp(), "Clicked Update button...")
print(get_timestamp(), "Clicked Update button...", file=outputFile)

# Choose file button clicked and firmware file attached
driver.find_element(*WebElements.choose_file).send_keys(os.getcwd() + WebElements.wifi_dummy)
time.sleep(2)

print(get_timestamp(), "Dummy firmware file attached...")
print(get_timestamp(), "Dummy firmware file attached...", file=outputFile)

# Enter instead click() to bypass element load strategy for fault insertion.
driver.find_element(*WebElements.upload).click()
print(get_timestamp(), "Upload Button clicked...")
print(get_timestamp(), "Upload button clicked...", file=outputFile)
time.sleep(1)

# Waiting couple minutes for device to load firmware
print(get_timestamp(), "Firmware uploaded! Please wait for firmware to load.")
print(get_timestamp(), "Firmware uploaded! Please wait for firmware to load.", file=outputFile)
time.sleep(180)

driver.close()
print(get_timestamp(), "Re-launching browser!")
print(get_timestamp(), "Re-launching browser!", file=outputFile)
time.sleep(2)

driver.start_session(capabilities=capa)
driver.get(WebElements.url)
time.sleep(2)
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(WebElements.cur_fw_version))
# Variables that read current current firmware version, mac address and service tag.
fw = driver.find_element(*WebElements.cur_fw_version).text
mac_address = driver.find_element(*WebElements.mac).text
service_tag = driver.find_element(*WebElements.st).text
wb_model = driver.find_element(*WebElements.model).text

# Logging to terminal, then text file.
print(get_timestamp(),
      "Current Device Info is: " + fw + ' | ' + wb_model + ' | ' + mac_address + ' | ' + service_tag)
print(get_timestamp(),
      "Current Device Info is: " + fw + ' | ' + wb_model + ' | ' + mac_address + ' | ' + service_tag,
      file=outputFile)
time.sleep(2)
if fw == dummy_fw_version:
    print(get_timestamp(), "Dummy Upgrade Successful! Starting downgrade.")
    print(get_timestamp(), "Dummy Upgrade Successful! Starting downgrade.", file=outputFile)
else:
    print("Firmware Upgrade failed! Current firmware is: " + fw)
    driver.quit()
    exit()


# Selecting Update button
driver.find_element(*WebElements.update).click()
time.sleep(2)
print(get_timestamp(), "Clicked Update button...")
print(get_timestamp(), "Clicked Update button...", file=outputFile)

# Choose file button clicked and firmware file attached
driver.find_element(*WebElements.choose_file).send_keys(os.getcwd() + WebElements.wifi_fw)
time.sleep(2)

print(get_timestamp(), "Firmware file attached...")
print(get_timestamp(), "Firmware file attached...", file=outputFile)

# Enter instead click() to bypass element load strategy for fault insertion.
driver.find_element(*WebElements.upload).click()
print(get_timestamp(), "Upload Button clicked...")
print(get_timestamp(), "Upload button clicked...", file=outputFile)
time.sleep(10)

# Waiting couple minutes for device to boot up and recover
print(get_timestamp(), "Firmware uploaded! Please wait for firmware to load.")
print(get_timestamp(), "Firmware uploaded! Please wait for firmware to load.", file=outputFile)
time.sleep(180)

driver.close()
print(get_timestamp(), "Re-launching browser!")
print(get_timestamp(), "Re-launching browser!", file=outputFile)
time.sleep(2)

driver.start_session(capabilities=capa)
driver.get(WebElements.url)
time.sleep(2)

# Device Information variables
fw = driver.find_element(*WebElements.cur_fw_version).text
mac_address = driver.find_element(*WebElements.mac).text
service_tag = driver.find_element(*WebElements.st).text
wb_model = driver.find_element(*WebElements.model).text

# Checking and logging/printing device information
print(get_timestamp(),
      "Current Device Info is: " + fw + ' | ' + wb_model + ' | ' + mac_address + ' | ' + service_tag)
print(get_timestamp(),
      "Current Device Info is: " + fw + ' | ' + wb_model + ' | ' + mac_address + ' | ' + service_tag,
      file=outputFile)
time.sleep(2)

if fw == upgrade_fw_version:
    print(get_timestamp(), "Firmware Downgrade Successful!")
    print(get_timestamp(), "Firmware Downgrade Successful!", file=outputFile)
else:
    print("Firmware Upgrade failed! Current firmware is: " + fw)
    driver.quit()
    exit()

print(get_timestamp(), "Script finished!")
print(get_timestamp(), "Script finished!", file=outputFile)

driver.quit()
