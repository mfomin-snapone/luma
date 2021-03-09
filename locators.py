from selenium.webdriver.common.by import By


class Elements:
    url = "http://192.168.0.140/"
    login_username = (By.ID, "username")
    login_password = (By.ID, "password")
    login_button = (By.XPATH, "/html/body/div[2]/table/tbody/tr[1]/td[2]/div/div[3]/button")
    settings_button = (By.ID, "settings")
    maintenance_menu = (By.XPATH, "//*[@id='menu']/div/div[2]/div[3]")
    browse_fw_button = (By.XPATH, "//*[@id='maintainUpgrade']/div[1]/div[8]/button[1]")
    ipc_fw = "\\fw\\upgrade_wattboxvps_2.0.1.8_20210219.bin"
    reboot_button = (By.XPATH, "//*[@id='maintainUpgrade']/div[1]/div[2]/span[1]/button")
    reboot_popup_ok_option = (By.XPATH, "//*[@id='config']/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[1]")


class WebElements:
    url = "http://192.168.7.148/"
    url_dc = "http://wattbox:wattbox@192.168.0.13/main"
    mac = (By.XPATH, "/html/body/div/div[2]/div[2]/div/ul/li[4]/span")
    st = (By.XPATH, "/html/body/div/div[2]/div[2]/div/ul/li[3]/span")
    model = (By.XPATH, "/html/body/div/div[2]/div[2]/div/ul/li[2]/span")
    vps_fw = "\\fw\\upgrade_wattboxvps_2.0.1.8_20210219.bin"
    vps_dummy = "\\fw\\upgrade_wattboxvps_2.0.1.9_20210219.bin"
    wifi_fw = "\\fw\\upgrade_wattboxwifi_2.0.1.6_20210127.bin"
    wifi_dummy = "\\fw\\upgrade_wattboxwifi_2.0.1.7_20210127.bin"
    recovery_fw = "\\fw\\upgrade_wattboxwifi_1.2.0.6_20191108.bin"
    vps_recovery_fw = "\\fw\\upgrade_wattboxwifi_1.2.0.6_20191108.bin"
    upload = (By.ID, "upload")
    main_page_reboot_btn = (By.XPATH, "/html/body/div/div[2]/div/ul/li[2]/a/i")
    yellow_reboot_btn = (By.XPATH, "/html/body/div/div[2]/a[2]/button")
    fw_failed_msg = (By.XPATH, "/html/body/div/div[2]/h4")
    update = (By.XPATH, "/html/body/div/div[2]/div[1]/ul/li[1]/a/i")
    properties = (By.XPATH, "/html/body/div/div[2]/a[2]/div[1]")
    username_field = (By.XPATH, "/html/body/div/div[2]/form/table/tbody/tr[1]/td/input")
    password_field = (By.XPATH, "/html/body/div/div[2]/form/table/tbody/tr[2]/td/input")
    password_confirm_field = (By.XPATH, "/html/body/div/div[2]/form/table/tbody/tr[3]/td/input")
    properties_apply = (By.XPATH, "/html/body/div/div[2]/form/input")
    choose_file = (By.XPATH, "/html/body/div/div[2]/div[2]/form/table/tbody/tr/td[2]/input")
    reset_all = (By.XPATH, "/html/body/div/div[2]/div[4]/button")
    reboot = (By.CLASS_NAME, "icon-cs-reset-icon")
    cur_fw_version = (By.XPATH, "/html/body/div/div[2]/div[2]/div/ul/li[6]/span")
    configure = (By.XPATH, "/html/body/div/div[2]/header/div[2]/ul/li[2]/a")
    maintenance = (By.XPATH, "/html/body/div/div[2]/a[4]/div[1]")
    export_config = (By.XPATH, "/html/body/div/div[2]/div[2]/a/span/span")
    details = (By.XPATH, "/html/body/div/div[2]/header/div[2]/ul/li[1]/a")
    outlet_1_Toggle = (By.XPATH, "/html/body/div/div[2]/div[5]/div[1]/div/ul/li[3]/div/label")
    outlet_1_reset = (By.XPATH, "/html/body/div/div[2]/div[5]/div[1]/div/ul/li[3]/a/i")
    fault_trigger = (By.ID, "blocking-background")
