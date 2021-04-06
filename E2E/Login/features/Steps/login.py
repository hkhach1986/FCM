from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import sys
sys.path.append(r'C:\Users\haykkh\Desktop\personal\FCMProject\FCM\E2E')
import constants

 


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
    context.driver.get("https://e2e-fcm-cop-gui.service1.svc.meshcore.net/product-delivery-fcm/login/Login")
    context.driver.maximize_window()


@when('open E2EFCM Homepage')
def step_impl2(context):
    title = context.driver.title
    print(title)


@when('Enter username "{user}" and password "{pwd}"')
def step_impl3(context, user, pwd):
    context.driver.find_element_by_id(constants.Constants.LOGIN).send_keys(user)
    time.sleep(1)
    context.driver.find_element_by_id(constants.Constants.PSW).send_keys(pwd)
    time.sleep(1)

@when('Click on login button')
def step_impl4(context):
    context.driver.find_element_by_id(constants.Constants.ENTER).click()


@Then('User must successfully login to the Dashboard page')
def step_impl5(context):
    try:
        dash = context.driver.find_element_by_xpath("//h2[contains(text(),'Home')]").text
    #fail = context.driver.find_element_by_xpath("//p[@id='ferrorlg']").text
    except:
        context.driver.close()
        assert False, "fail"
    if (dash == "HOME"):
        assert True, "login successfully"

@Then('Change password')
def step_impl16(context):
    context.driver.find_element_by_xpath("//a[contains(text(),'User Management')]").click()
    context.driver.find_element_by_xpath("//a[contains(text(),'User List')]").click()
    context.driver.find_element_by_id("rppSelect").click()
    context.driver.find_element_by_xpath("//option[@value='100']").click()
    context.driver.find_element_by_xpath("//body/div[@id='wrapcols']/div[@id='maincol']/div[@id='mainct']/form[@id='UserListForm']/div[@class='dvListCasePage']/div[@id='kawwaGrid']/div[@id='rowPerPageZone_kawwaGrid']/div[@class='t-data-grid']/table/tbody/tr[22]/td[7]/a[2]").click()
    #context.driver.find_element_by_id("submit_1").click()
    # note = context.driver.find_element_by_id("ferror").text
    
    # print(note)
    # length = len(note)
    # print(length)
    # password = note[length-49:length-41]
    # print(password)
    
    #context.driver.find_element_by_xpath("//a[@accesskey='Q']").click()
    # context.driver.find_element_by_id("login").send_keys("CCC")
    # time.sleep(1)
    # context.driver.find_element_by_id("password").send_keys(password)
    # time.sleep(1)
    # context.driver.find_element_by_id("bthp").click()
    # context.driver.find_element_by_id("oldpassword").send_keys(password)
    # context.driver.find_element_by_id("newpassword").send_keys("test1234")
    # context.driver.find_element_by_id("confirmpassword").send_keys("test1234")
    # context.driver.find_element_by_id("btSubmit").click()
    # context.driver.find_element_by_id("login").send_keys("AAA")
    # time.sleep(1)
    # context.driver.find_element_by_id("password").send_keys("test1234")
    # time.sleep(1)
    # context.driver.find_element_by_id("bthp").click()
