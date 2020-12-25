from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

@given('I launch Mozilla browser')
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


@when('I open FCM Homepage')
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
    dash = context.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/h2").text
    if (dash == "HOME"):
        print("login successfully")
        #context.driver.close() 
    else:
        print("doesn't login successfully")
        #context.driver.close()   
        
        
@when('Go to Issuer Fraud Management page')
def step_impl(context):
    ###Press Issuer Fraud Management page
    context.driver.find_element_by_xpath("//div[@class='dvList']//ul//li//a[contains(text(),'Issuer Fraud Management')]").click()
   
    
@when('Select cards from Detection Cards section')
def step_impl(context):
    ###select Detection
    context.driver.find_element_by_xpath("//a[contains(text(),'Detection')]").click()
    ###select Cards section
    context.driver.find_element_by_xpath("//a[contains(text(),'Cards')]").click()

    #context.driver.close()


@then('search cards by Cardholder Name')
def step_impl(context):
    ###Enter cardholder=ch name 
    context.driver.find_element_by_id("cardHolderName").send_keys("ANNETE TRITZ")
    ###Press filter button
    context.driver.find_element_by_id("btfilter").click()
    ###Check if found a ch with mentioned name (ANNETE TRITZ), in FCM we have 3 card in the name of ANNETE TRITZ
    ch = context.driver.find_element_by_xpath("//tr[@class='(blank) t-first']//td[@class='cardholderName'][contains(text(),'ANNETE TRITZ')]").text
    with open(r"C:\Users\haykkh\Desktop\Card_search_results\Cardholder.txt", "w+") as file:
        file.write(ch)
    ###Reset all filled fields
    context.driver.find_element_by_id("btreset").click()
    
@then('search cards by Card Number')
def step_impl(context):
    ###cardNumber is mapped with Pan in card details, in Transaction list it is mapped with Masked Pan. Card pan is uniqe
    context.driver.find_element_by_id("cardNumber").send_keys("4871780038303975")
    context.driver.find_element_by_id("btfilter").click()
    cardNumber = context.driver.find_element_by_xpath("//tr[@class='(blank) t-first']//td[@class='maskedPAN'][contains(text(),'487178XXXXXX3975')]").text
    with open(r"C:\Users\haykkh\Desktop\Card_search_results\cardNumber.txt", "w+") as file:
        file.write(cardNumber)
    ###Reset all filled fields
    context.driver.find_element_by_id("btreset").click()
    
@then('search cards by Case Reference')
def step_impl(context):
    ###Case Reference is mapped Case details with the same name in - Home > Fraud > Case Filter > Case Detail > UPDATE path
    context.driver.find_element_by_id("cardHolderRef").send_keys("A013")
    context.driver.find_element_by_id("btfilter").click()
    ch_for_caseRef = context.driver.find_element_by_xpath("//td[contains(text(),'AUSTIN BENTON')]").text
    with open(r"C:\Users\haykkh\Desktop\Card_search_results\ch_for_caseRef.txt", "w+") as file:
        file.write(ch_for_caseRef)
    ###Reset all filled fields
    context.driver.find_element_by_id("btreset").click()


@then('search cards by Card Id')
def step_impl(context):
    ###card Id is mapped with "card reference" in card details, in Transaction list it is mapped with PAN Reference
    context.driver.find_element_by_id("pANReference").send_keys("6574EAA3CE3C13ED51285299D7558E2109984B18C0BC3864044FC27B9E3CCB12")
    context.driver.find_element_by_id("btfilter").click()
    cardId = context.driver.find_element_by_xpath("//tr[@class='(blank) t-first']//td[@class='panReference'][contains(text(),'6574EAA3CE3C13ED51285299D7558E2109984B18C0BC386404')]").text
    with open(r"C:\Users\haykkh\Desktop\Card_search_results\cardId.txt", "w+") as file:
        file.write(cardId)
    ###Reset all filled fields
    context.driver.find_element_by_id("btreset").click()       

@then('search cards by Bank Account Number')
def step_impl(context):
    ###Bank Account Number is mapped with Bank account No.: in card details, in Transaction list it is missed
    context.driver.find_element_by_id("bankAccountNumber").send_keys("DE45200411330897054300")
    context.driver.find_element_by_id("btfilter").click()
    count_of_search = context.driver.find_element_by_xpath("//a[@class='a9']").text
    with open(r"C:\Users\haykkh\Desktop\Card_search_results\count_of_search.txt", "w+") as file:
        file.write(count_of_search)
    ###Reset all filled fields
    context.driver.find_element_by_id("btreset").click()       
    
@then('search cards by Additional Criteria (to be used in combination with CardHolder Name)')
def step_impl(context):
    ##External Bank Code=issuer Id, Zip Code= ZIP Code, BirthDay=Date of birth mapped with card details
       ###Enter cardholder=ch name 
    context.driver.find_element_by_id("cardHolderName").send_keys("AUSTIN BENTON")
    ###Check if found a ch with mentioned name (AUSTIN BENTON)
    context.driver.find_element_by_id("showHide_0").click()
    time.sleep(2)
    context.driver.find_element_by_id("externalBankcode").send_keys("6601")
    context.driver.find_element_by_id("zipCode").send_keys("10405")
    context.driver.find_element_by_id("birthDate").send_keys("14/07/1976")
    ###Press filter button
    context.driver.find_element_by_id("btfilter").click()
    ch_for_add_cr = context.driver.find_element_by_xpath("//tr[@class='(blank) t-first']//td[@class='cardholderName'][contains(text(),'AUSTIN BENTON')]").text
    with open(r"C:\Users\haykkh\Desktop\Card_search_results\ch_for_add_cr.txt", "w+") as file:
        file.write(ch_for_add_cr)
    ###Reset all filled fields
    context.driver.find_element_by_id("btreset").click()
    context.driver.close()