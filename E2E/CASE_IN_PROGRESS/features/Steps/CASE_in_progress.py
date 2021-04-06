from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import difflib
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
    context.driver.find_element_by_xpath(constants.Constants.Issuer_fraud_management).click()
   
    
@when('Select CASE section')
def step_impl(context):
    ###select CASE section
    context.driver.find_element_by_xpath(constants.Constants.Case_section).click()
    context.driver.find_element_by_xpath(constants.Constants.Case_subgroup).click()
    
@when('search Case by Case_ID "{Case_ID}" positive check')
def step_impl(context, Case_ID):
    context.driver.find_element_by_id(constants.Constants.CaseId).send_keys(Case_ID)
    context.driver.find_element_by_id(constants.Constants.Filter).click()
    
@when('click on Reopen button and save it')
def step_impl(context):
    context.driver.find_element_by_xpath(constants.Constants.ReopenCase).click()
    context.driver.find_element_by_xpath(constants.Constants.UCaseDetailsSave).click()

@Then ('check if the case status became In progress from Closed')       
def step_impl(context):
    case_status = context.driver.find_element_by_xpath(constants.Constants.CLCaseStatus).text
    cardPan = context.driver.find_element_by_xpath(constants.Constants.CLCardNumber).text
    cardNumberRef = context.driver.find_element_by_xpath(constants.Constants.CLCardReferenceNumber).text
    ExpieryDate = context.driver.find_element_by_xpath(constants.Constants.CLPSNExpaieryDate).text
    priority = context.driver.find_element_by_xpath(constants.Constants.CLPriority).text
    BrandId = context.driver.find_element_by_xpath(constants.Constants.CLBrandID).text
    CardHolderName = context.driver.find_element_by_xpath(constants.Constants.CLCardHolderName).text
    CaseFraudStatus = context.driver.find_element_by_xpath(constants.Constants.CLCaseFraudStatus).text
    CaseFraudtype = context.driver.find_element_by_xpath(constants.Constants.CLCaseFraudType).text
    CaseFraudSubType = context.driver.find_element_by_xpath(constants.Constants.CLCaseFraudSubtype).text
    WorkFlowStatus = context.driver.find_element_by_xpath(constants.Constants.CLWorkFlowStatus).text
    CaseCreationDate = context.driver.find_element_by_xpath(constants.Constants.CLCaseCreationDate).text
    Issuer = context.driver.find_element_by_xpath(constants.Constants.CLIssuer).text
    
    with open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\CaseReopenClose\status_InProgress.txt", "w+") as file:
        
        file.write("Card Number = " + cardPan + "\n")
        file.write("Card Number Reference = " + cardNumberRef + "\n")
        file.write("psn expiry date = " + ExpieryDate + "\n")
        file.write("Priority = " + priority + "\n")
        file.write("BRAND ID = " + BrandId + "\n")
        file.write("Cardholder Name = " + CardHolderName + "\n")
        file.write("CASE STATUS = " + case_status + '\n')
        file.write("Case Fraud Status = " + CaseFraudStatus + "\n")
        file.write("CASE FRAUD TYPE = " + CaseFraudtype + "\n")
        file.write("CASE FRAUD SUB TYPE = " + CaseFraudSubType + "\n")
        file.write("Workflow Status = " + WorkFlowStatus + "\n")
        file.write("CASE CREATION DATE = " + CaseCreationDate + "\n")
        file.write("issuer = " + Issuer + "\n")
        file.close()
    
    golden_file = r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\CaseReopenClose\status_InProgress_gold.txt"
    first_file = r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\CaseReopenClose\status_InProgress.txt"
    first_file_lines = open(first_file).readlines()
    golden_file_lines = open(golden_file).readlines()
    difference = difflib.HtmlDiff().make_file(first_file_lines, golden_file_lines, first_file, golden_file)
    difference_report = open(r'C:\Users\haykkh\Desktop\TestCaseOutput\e2e\CaseReopenClose\difference_In_Progress_report.html', 'w')
    difference_report.write(difference)
    difference_report.close()
    
    golden_file1 = open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\CaseReopenClose\status_InProgress_gold.txt", 'r').read()
    first_file2 = open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\CaseReopenClose\status_InProgress.txt", 'r').read()
    assert golden_file1 == first_file2, "not equal files" 
    
@when('press Update id to close the case again')
def step_impl(context):
    context.driver.find_element_by_xpath(constants.Constants.UpdateId).click()

@when ('select mandatory fields for closing the case')
def step_impl(context):
    context.driver.find_element_by_id(constants.Constants.UShowHideCaseDetails).click()
    time.sleep(2)
    context.driver.find_element_by_id(constants.Constants.UCaseStatus).send_keys("Closed")
    time.sleep(2)
    context.driver.find_element_by_id(constants.Constants.UClosureReason).send_keys("Investigation Completed")
    time.sleep(2)
    
@Then ('check if the case status became closed from In Progress')
def step_impl(context):
    context.driver.find_element_by_xpath(constants.Constants.UCaseDetailsSave).click()
    time.sleep(2)
    case_status = context.driver.find_element_by_xpath(constants.Constants.CLCaseStatus).text
    cardPan = context.driver.find_element_by_xpath(constants.Constants.CLCardNumber).text
    cardNumberRef = context.driver.find_element_by_xpath(constants.Constants.CLCardReferenceNumber).text
    ExpieryDate = context.driver.find_element_by_xpath(constants.Constants.CLPSNExpaieryDate).text
    priority = context.driver.find_element_by_xpath(constants.Constants.CLPriority).text
    BrandId = context.driver.find_element_by_xpath(constants.Constants.CLBrandID).text
    CardHolderName = context.driver.find_element_by_xpath(constants.Constants.CLCardHolderName).text
    CaseFraudStatus = context.driver.find_element_by_xpath(constants.Constants.CLCaseFraudStatus).text
    CaseFraudtype = context.driver.find_element_by_xpath(constants.Constants.CLCaseFraudType).text
    CaseFraudSubType = context.driver.find_element_by_xpath(constants.Constants.CLCaseFraudSubtype).text
    WorkFlowStatus = context.driver.find_element_by_xpath(constants.Constants.CLWorkFlowStatus).text
    CaseCreationDate = context.driver.find_element_by_xpath(constants.Constants.CLCaseCreationDate).text
    Issuer = context.driver.find_element_by_xpath(constants.Constants.CLIssuer).text
    
    with open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\CaseReopenClose\status_closed.txt", "w+") as file:
        
        file.write("Card Number = " + cardPan + "\n")
        file.write("Card Number Reference = " + cardNumberRef + "\n")
        file.write("psn expiry date = " + ExpieryDate + "\n")
        file.write("Priority = " + priority + "\n")
        file.write("BRAND ID = " + BrandId + "\n")
        file.write("Cardholder Name = " + CardHolderName + "\n")
        file.write("CASE STATUS = " + case_status + '\n')
        file.write("Case Fraud Status = " + CaseFraudStatus + "\n")
        file.write("CASE FRAUD TYPE = " + CaseFraudtype + "\n")
        file.write("CASE FRAUD SUB TYPE = " + CaseFraudSubType + "\n")
        file.write("Workflow Status = " + WorkFlowStatus + "\n")
        file.write("CASE CREATION DATE = " + CaseCreationDate + "\n")
        file.write("issuer = " + Issuer + "\n")
        file.close()
    context.driver.close()
    
    
    golden_file = r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\CaseReopenClose\status_closed_gold.txt"
    first_file = r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\CaseReopenClose\status_closed.txt"
    first_file_lines = open(first_file).readlines()
    golden_file_lines = open(golden_file).readlines()
    difference = difflib.HtmlDiff().make_file(first_file_lines, golden_file_lines, first_file, golden_file)
    difference_report = open(r'C:\Users\haykkh\Desktop\TestCaseOutput\e2e\CaseReopenClose\difference_closed_report.html', 'w')
    difference_report.write(difference)
    difference_report.close()
    
    golden_file1 = open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\CaseReopenClose\status_closed_gold.txt", 'r').read()
    first_file2 = open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\CaseReopenClose\status_closed.txt", 'r').read()
    assert golden_file1 == first_file2, "not equal files" 
    
    
                                      

    
