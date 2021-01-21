from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

@given('launch Mozilla browser')
def step_impl1(context):
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
    context.driver.get("https://int-fcm-gui.service.svc.meshcore.net/product-delivery-fcm/en/login/login")
    context.driver.maximize_window()


@when('open INTFCM Homepage')
def step_impl2(context):
    title = context.driver.title
    print(title)


@when('Enter username "{user}" and password "{pwd}"')
def step_impl3(context, user, pwd):
    context.driver.find_element_by_id("login").send_keys(user)
    time.sleep(1)
    context.driver.find_element_by_id("password").send_keys(pwd)
    time.sleep(1)

@when('Click on login button')
def step_impl4(context):
    context.driver.find_element_by_id("bthp").click()


@when('User must successfully login to the Dashboard page')
def step_impl5(context):
    try:
        dash = context.driver.find_element_by_xpath("//h2[contains(text(),'Home')]").text
    #fail = context.driver.find_element_by_xpath("//p[@id='ferrorlg']").text
    except:
        context.driver.close()
        assert False, "fail"
    if (dash == "HOME"):
        assert True, "login successfully"

@when('Go to Issuer Fraud Management page')
def step_impl(context):
    ###Press Issuer Fraud Management page
    context.driver.find_element_by_xpath("//div[@class='dvList']//ul//li//a[contains(text(),'Issuer Fraud Management')]").click()
   
    
@when('Select Detection Card Payments section')
def step_impl(context):
    ###select Detection
    context.driver.find_element_by_xpath("//a[contains(text(),'Detection')]").click()
    ###select Card Payments section
    context.driver.find_element_by_xpath("//a[contains(text(),'Card Payments')]").click()

    #context.driver.close()


@when('search card payment by "{ACC_ID}", "{ACC_Country}", "{MCC}", "{Pan_Reference}", "{Terminal_ID}"')
def step_impl(context, ACC_ID, ACC_Country, MCC, Pan_Reference, Terminal_ID):
    ###Enter correct ACC_ID 
    context.driver.find_element_by_id("acceptorId").send_keys(ACC_ID)
    context.driver.find_element_by_id("acceptorCountryDropDown").send_keys(ACC_Country)
    context.driver.find_element_by_id("mccIDDropDown").send_keys(MCC)
    context.driver.find_element_by_id("panReference").send_keys(Pan_Reference)
    context.driver.find_element_by_id("cardPymtTerminalId").send_keys(Terminal_ID)


@Then('press filter button')
def step_impl(context):
    ###Press filter button
    time.sleep(1)
    context.driver.find_element_by_id("btfilter").click()
    time.sleep(5)
    Card_payments_search_result = context.driver.find_element_by_xpath("//tr[@class='(blank) t-first']//td[@class='acceptorId'][contains(text(),'1095822540')]").text
    with open(r"C:\Users\haykkh\Desktop\Card_search_results\Card_payments_search_result.txt", "w+") as file:
        file.write(Card_payments_search_result)
    ###Reset all filled fields
    context.driver.find_element_by_id("btreset").click()
    context.driver.close()