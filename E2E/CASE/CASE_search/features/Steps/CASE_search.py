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
    
@when('search Case by CaseId = "{caseId}"')
def step_impl(context, caseId):
    context.driver.find_element_by_id(constants.Constants.CaseId).send_keys(caseId)
    
@when('search Case by CardNumber = "{caseCardNumber}"')
def step_impl(context, caseCardNumber):
    context.driver.find_element_by_id(constants.Constants.CardNumber).send_keys(caseCardNumber)

@when('search Case by PanReference = "{cardNumberRef}"')
def step_impl(context, cardNumberRef):
    context.driver.find_element_by_id(constants.Constants.PanReference).send_keys(cardNumberRef)

    
# @when('search Case by Issuer = {issuer}')
# def step_impl(context, issuer):
#     Issuer = context.driver.find_element_by_id(constants.Constants.Issuer)
#     drp_issuer = Select(Issuer)
#     drp_issuer.select_by_visible_text(issuer)

# @when('search Case by Brand = "{caseBrand}"')
# def step_impl(context, caseBrand):
#     brand = context.driver.find_element_by_id(constants.Constants.Brand)
#     drp_brand = Select(brand)
#     drp_brand.select_by_visible_text(caseBrand)


@when('search Case by CaseStatus = "{caseStatus}"')
def step_impl(context, caseStatus):
    status = context.driver.find_element_by_id(constants.Constants.CaseStatus)
    drp_status = Select(status)
    drp_status.select_by_visible_text(caseStatus)  

@when('search Case by CasePriority = "{casePriorityForFilter}"')
def step_impl(context, casePriorityForFilter):
    priority = context.driver.find_element_by_id(constants.Constants.CasePriority)
    drp_priority = Select(priority)
    drp_priority.select_by_visible_text(casePriorityForFilter) 

# #####will open comment after fixing the ticket https://jira.worldline.com/browse/EWLFRMTEST-8840####
# @when('search Case by DetectionSrc = "{detectionSrc}"')
# def step_impl(context, detectionSrc):
#     detection_src = context.driver.find_element_by_id(constants.Constants.DetectionSrc)
#     drp_detection_src = Select(detection_src)
#     drp_detection_src.select_by_visible_text(detectionSrc)

@when('search Case by WorkflowStatus = "{workflowStatus}"')
def step_impl(context, workflowStatus):
    workFlow_status = context.driver.find_element_by_id(constants.Constants.WorkflowStatus)
    drp_workFlow_status = Select(workFlow_status)
    drp_workFlow_status.select_by_visible_text(workflowStatus) 
    
@when('search Case by CaseFraudStatus = "{caseFraudStatus}"')
def step_impl(context, caseFraudStatus):
    case_fraud_status = context.driver.find_element_by_id(constants.Constants.CaseFraudStatus)
    drp_case_fraud_status = Select(case_fraud_status)
    drp_case_fraud_status.select_by_visible_text(caseFraudStatus)     

######https://jira.worldline.com/browse/EWLFRMTEST-885
# @when('search Case by CaseFraudType = "{caseFraudReason}"')
# def step_impl(context, caseFraudReason):
#     case_fraud_type = context.driver.find_element_by_id(constants.Constants.CaseFraudType)
#     drp_case_fraud_type = Select(case_fraud_type)
#     drp_case_fraud_type.select_by_visible_text(caseFraudReason) 
    
@when('search Case by CaseFraudSubType = "{caseFraudSubReason}"')
def step_impl(context, caseFraudSubReason):
    case_fraud_sub_type = context.driver.find_element_by_id(constants.Constants.CaseFraudSubType)
    drp_case_fraud_sub_type = Select(case_fraud_sub_type)
    drp_case_fraud_sub_type.select_by_visible_text(caseFraudSubReason) 

    
@when('search Case by CaseDateOpenedFrom = "{caseDateOpenedFrom}"')
def step_impl(context, caseDateOpenedFrom):
    context.driver.find_element_by_id(constants.Constants.CaseDateOpenedFrom).send_keys(caseDateOpenedFrom)

@when('search Case by CaseDateOpenedTo = "{caseDateOpenedTo}"')
def step_impl(context, caseDateOpenedTo):
    context.driver.find_element_by_id(constants.Constants.CaseDateOpenedTo).send_keys(caseDateOpenedTo)
    
@when('search Case by CaseDateClosedFrom = "{caseDateClosedFrom}"')
def step_impl(context, caseDateClosedFrom):
    context.driver.find_element_by_id(constants.Constants.CaseDateClosedFrom).send_keys(caseDateClosedFrom)
    
@when('search Case by CaseDateClosedTo = "{caseDateClosedTo}"')
def step_impl(context, caseDateClosedTo):
    context.driver.find_element_by_id(constants.Constants.CaseDateClosedTo).send_keys(caseDateClosedTo)
    
@when('search Case by DateWorkFlowSetFrom = "{dateWorkFlowSetFrom}"')
def step_impl(context, dateWorkFlowSetFrom):
    context.driver.find_element_by_id(constants.Constants.DateWorkFlowSetFrom).send_keys(dateWorkFlowSetFrom)  
    
@when('search Case by DateWorkFlowSetTo = "{dateWorkFlowSetTo}"')
def step_impl(context, dateWorkFlowSetTo):
    context.driver.find_element_by_id(constants.Constants.DateWorkFlowSetTo).send_keys(dateWorkFlowSetTo)  
    
@when('search Case by LastUpdatedFrom = "{lastUpdatedFrom}"')
def step_impl(context, lastUpdatedFrom):
    context.driver.find_element_by_id(constants.Constants.LastUpdatedFrom).send_keys(lastUpdatedFrom) 
        
@when('search Case by LastUpdatedTo = "{lastUpdatedTo}"')
def step_impl(context, lastUpdatedTo):
    context.driver.find_element_by_id(constants.Constants.LastUpdatedTo).send_keys(lastUpdatedTo)    
    
@when('search Case by CaseCardHolderName = "{cardHolderName}"')
def step_impl(context, cardHolderName):
    context.driver.find_element_by_id(constants.Constants.CaseCardHolderName).send_keys(cardHolderName) 

@when('search Case by CaseReference = "{caseReference}"')
def step_impl(context, caseReference):
    context.driver.find_element_by_id(constants.Constants.CaseReference).send_keys(caseReference) 
    
@Then('press filter to see searching case for all results')
def step_impl(context):
    context.driver.find_element_by_id(constants.Constants.Filter).click()
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
    
    with open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\Case_search\Case_search_result.txt", "w+") as file:
        
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
    golden_file = r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\Case_search\Case_search_result.txt"
    first_file = r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\Case_search\Case_search_result.txt"
    first_file_lines = open(first_file).readlines()
    golden_file_lines = open(golden_file).readlines()
    difference = difflib.HtmlDiff().make_file(first_file_lines, golden_file_lines, first_file, golden_file)
    difference_report = open(r'C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\Case_search\Case_search_result.html', 'w')
    difference_report.write(difference)
    difference_report.close()
    
    golden_file1 = open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\Case_search\Case_search_result_gold.txt", 'r').read()
    first_file2 = open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\Case_search\Case_search_result.txt", 'r').read()
    assert golden_file1 == first_file2, "not equal files"