from selenium.webdriver.common.by import By


class Elements:
    url = "http://192.168.0.142/"
    login_username = (By.ID, "username")
    login_password = (By.ID, "password")
    login_button = (By.XPATH, "/html/body/div[2]/table/tbody/tr[1]/td[2]/div/div[3]/button")
    settings_button = (By.ID, "settings")
    maintenance_menu = (By.XPATH, "//*[@id='menu']/div/div[2]/div[3]")
    browse_fw_button = (By.XPATH, "//*[@id='maintainUpgrade']/div[1]/div[8]/button[1]")
    ipc_fw = "\\fw\\upgrade_wattboxvps_2.0.1.8_20210219.bin"
    reboot_button = (By.XPATH, "//*[@id='maintainUpgrade']/div[1]/div[2]/span[1]/button")
    reboot_popup_ok_option = (By.XPATH, "//*[@id='config']/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[1]")

