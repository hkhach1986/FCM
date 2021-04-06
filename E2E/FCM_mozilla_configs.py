class configsMozilla:
    myProxy= "10.26.221.13:3128"
    desired_capability = webdriver.DesiredCapabilities.FIREFOX
    desired_capability['proxy'] = {
            "proxyType": "manual",
            "httpProxy": myProxy,
            "ftpProxy": myProxy,
            "sslProxy": myProxy
        }
    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True
    driver = webdriver.Firefox(firefox_profile=profile,
    capabilities=desired_capability,
    executable_path="C:\\drivers\\geckodriver.exe")
    driver.get("https://e2e-fcm-cop-gui.service1.svc.meshcore.net/product-delivery-fcm/login/Login")
    driver.maximize_window()