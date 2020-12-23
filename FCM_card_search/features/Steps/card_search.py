from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

@given('I launch Mozilla browser')
def step_impl(context):
    context.myProxy= "10.26.221.13:3128"
    context.desired_capability = webdriver.DesiredCapabilities.FIREFOX
    context.desired_capability['proxy'] = {
            "proxyType": "manual",
            "httpProxy": context.myProxy,
            "ftpProxy": context.myProxy,
            "sslProxy": context.myProxy
        }
    context.profile = webdriver.FirefoxProfile()
    context.profile.accept_untrusted_certs = True
    context.driver = webdriver.Firefox(firefox_profile=context.profile,
    capabilities=context.desired_capability,
    executable_path="C:\\drivers\\geckodriver.exe")
    context.driver.get("https://e2e-fcm-cop-gui.service1.svc.meshcore.net/product-delivery-fcm/login/Login")
    context.driver.maximize_window()


@when('I open FCM Homepage')
def step_impl(context):
    title = context.driver.title
    print(title)


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element_by_id("login").send_keys(user)
    time.sleep(1)
    context.driver.find_element_by_id("password").send_keys(pwd)
    time.sleep(1)

@when('Click on login button')
def step_impl(context):
    context.driver.find_element_by_id("bthp").click()


@when('User must successfully login to the Dashboard page')
def step_impl(context):
    dash = context.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/h2").text
    print(dash)
    if (dash == "HOME"):
        print("login successfully")
    else:
        print("doesn't login successfully")
        #context.driver.close()   
        
        
@when('Go to Issuer Fraud Management page')
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/ul/li/a").click()
    #context.driver.select_element_by_visible_text("Issuer Fraud Management").click()
    
    
@then('Select from Detection Cards section')
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/div[3]/div[2]/ul/li[3]/a").click()
    context.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/ul/li[1]/a").click()
    context.driver.find_element_by_id("cardHolderName").send_keys("ANNETE TRITZ")
    context.driver.find_element_by_id("btfilter").click()
    #context.driver.select_element_by_visible_text("Detection").click()
    ch = context.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[1]/form/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[6]").text
    print(ch)
    context.driver.close()
   