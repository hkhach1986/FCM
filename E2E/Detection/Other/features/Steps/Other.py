from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import difflib
import filecmp

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
   
    
@when('Select Detection Other section')
def step_impl(context):
    ###select Detection
    context.driver.find_element_by_xpath("//a[contains(text(),'Detection')]").click()
    ###select Card Payments section
    context.driver.find_element_by_xpath("//a[contains(text(),'Other')]").click()

    #context.driver.close()
@when('search payment in other section by transaction amounts "{convertedTransactionAmountFrom}", "{convertedTransactionAmountTo}"')
def step_impl(context, convertedTransactionAmountFrom, convertedTransactionAmountTo):
   context.driver.find_element_by_id("convertedTransactionAmountFrom").send_keys(convertedTransactionAmountFrom)
   context.driver.find_element_by_id("convertedTransactionAmountTo").send_keys(convertedTransactionAmountTo)
###These 2 fields doesn't work properly as the given authorization doesn't get correct in the results

@when('search payment in other section by external ID "{externalId}", "{panReference}"')
def step_impl(context, externalId, panReference):
    context.driver.find_element_by_id("externalId").send_keys(externalId)
    context.driver.find_element_by_id("panReference").send_keys(panReference)

    
@when('search payment in other section by Issuer Country "{sourceCountryDropDown}"')
def step_impl(context, sourceCountryDropDown):
    context.driver.find_element_by_id("sourceCountryDropDown").send_keys(sourceCountryDropDown)
    


@when('search payment in other section by filters Issuer Id "{sourceProviderId}", POS Entry Mode "{POS_Entry_Mode}"')
def step_impl(context, sourceProviderId, POS_Entry_Mode):
    context.driver.find_element_by_id("sourceProviderId").send_keys(sourceProviderId)
    context.driver.find_element_by_id("filter0").send_keys(POS_Entry_Mode)


@when('search payment in other section by filters Card Entry Mode "{Card_Entry_Mode}", Security Type "{Security_Type}", WLP FO Result Code "{WLP_FO_Result_Code}"')
def step_impl(context, WLP_FO_Result_Code, Card_Entry_Mode, Security_Type):
    context.driver.find_element_by_id("filter1").send_keys(Card_Entry_Mode)
    context.driver.find_element_by_id("filter2").send_keys(Security_Type)
    # context.driver.find_element_by_id("filter3").send_keys(ISO_Result_Code)
    context.driver.find_element_by_id("filter4").send_keys(WLP_FO_Result_Code)    
###ISO Result Code "<filter3>"  parameter doesn't work properly whatever give it will return same result

@when('search payment in other section by filter Transaction SubType "{filterTransactionSubType}"')
def step_impl(context, filterTransactionSubType):
    context.driver.find_element_by_id("filterTransactionSubType").send_keys(filterTransactionSubType)
    
@when('search payment in other section by filter Fall Back Flag "{Fall_Back_Flag}"')
def step_impl(context, Fall_Back_Flag):
    context.driver.find_element_by_id("filter5").send_keys(Fall_Back_Flag)
    
    #context.driver.close()

###for example Fall Back Flag should take 2 values 0 and 1 but if select 1 it will bring the results with 0
###Fall Back Flag shouldn't take string value, but when we give string "aa" it will not get the column red color and return Internal server error
###Transaction SubType doesn't pay attention the selected value, it will get same result whatever we give


@when('search payment in other section by filters Company Id "{businessId}", Acceptor Id "{targetId}"')
def step_impl(context, businessId, targetId):
    context.driver.find_element_by_id("targetId").send_keys(targetId)
    context.driver.find_element_by_id("businessId").send_keys(businessId)


@when('search payment in other section by filter Acceptor Country "{targetCountryDropDown}"')
def step_impl(context, targetCountryDropDown):
    context.driver.find_element_by_id("targetCountryDropDown").send_keys(targetCountryDropDown)

@when('search payment in other section by filters MCC "{mccIDDropDown}"')
def step_impl(context, mccIDDropDown):
    context.driver.find_element_by_id("mccIDDropDown").send_keys(mccIDDropDown)
 

# @when('search payment in other section by filters Acquirer BIN "{targetProviderId}"')
# def step_impl(context, targetProviderId):
#     context.driver.find_element_by_id("targetProviderId").send_keys(targetProviderId)

@when('search payment in other section by filters Terminal Id "{targetTechnicalId}"')
def step_impl(context, targetTechnicalId):
    context.driver.find_element_by_id("targetTechnicalId").send_keys(targetTechnicalId)
 

@when('search payment in other section by filters Acq Cntry Code "{Acq_Cntry_Code}", Alt PAN "{Alt_PAN}", Auth Id "{Auth_Id}"')
def step_impl(context, Acq_Cntry_Code, Alt_PAN, Auth_Id):
    context.driver.find_element_by_id("filter7").send_keys(Acq_Cntry_Code)
    context.driver.find_element_by_id("filter8").send_keys(Alt_PAN) 
    context.driver.find_element_by_id("filter6").send_keys(Auth_Id)      


@Then('press filter button')
def step_impl(context):
    ###Press filter button
    time.sleep(1)
    context.driver.find_element_by_id("btfilter").click()
    time.sleep(2)
    Auth_Code = context.driver.find_element_by_xpath("//td[contains(text(),'190002')]").text
    cardPan = context.driver.find_element_by_xpath("//td[contains(text(),'487178XXXXXX3650')]").text
    with open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Detection\Other\search_result.txt", "w+") as file:
        file.write("Auth_Code = " + Auth_Code + '\n')
        file.write("PAN = " + cardPan + "\n")
        file.close()
        # with open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Detection\Other\search_result_gold.txt", "r") as filegold:
        #     context.assertTrue(filecmp(filegold, file, shallow=False))
    ###Reset all filled fields
    #context.driver.find_element_by_id("btreset").click()
    context.driver.close()
    
    golden_file = r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Detection\Other\search_result_gold.txt"
    first_file = r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Detection\Other\search_result.txt"
    first_file_lines = open(first_file).readlines()
    golden_file_lines = open(golden_file).readlines()
    difference = difflib.HtmlDiff().make_file(first_file_lines, golden_file_lines, first_file, golden_file)
    difference_report = open(r'C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Detection\Other\difference_reprt.html', 'w')
    difference_report.write(difference)
    difference_report.close()
    
    golden_file1 = open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Detection\Other\search_result_gold.txt", 'r').read()
    first_file2 = open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Detection\Other\search_result.txt", 'r').read()
    assert golden_file1 == first_file2, "not equal files"