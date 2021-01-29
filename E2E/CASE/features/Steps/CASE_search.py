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
   
    
@when('Select CASE section')
def step_impl(context):
    ###select CASE section
    context.driver.find_element_by_xpath("//a[contains(text(),'Case')]").click()
    context.driver.find_element_by_xpath("//a[contains(text(),'Case')]").click()
    
@when('search Case by Case_ID "{Case_ID}" positive check')
def step_impl(context, Case_ID):
    context.driver.find_element_by_id("caseId").send_keys(Case_ID)
    
    

    
@Then('press filter to see searching results')
def step_impl(context):
    context.driver.find_element_by_id("btfilter").click()
    time.sleep(2)
    Card_Number = context.driver.find_element_by_xpath("//td[contains(text(),'487178XXXXXX5325')]").text
    #CardHolderName = context.driver.find_element_by_xpath("//tr[@class='(blank) t-first']//td[@class='cardHolderName'][contains(text(),'JOHN KÖNIG')]").text
    with open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\CaseID_search_result.txt", "w+") as file:
        file.write("Card_Number = " + Card_Number + '\n')
        #file.write("CardHolderName = " + CardHolderName + "\n")
        file.close()
        # with open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Detection\Other\search_result_gold.txt", "r") as filegold:
        #     context.assertTrue(filecmp(filegold, file, shallow=False))

    golden_file = r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\CaseID_search_result_gold.txt"
    first_file = r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\CaseID_search_result.txt"
    first_file_lines = open(first_file).readlines()
    golden_file_lines = open(golden_file).readlines()
    difference = difflib.HtmlDiff().make_file(first_file_lines, golden_file_lines, first_file, golden_file)
    difference_report = open(r'C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\CaseID_search_result.html', 'w')
    difference_report.write(difference)
    difference_report.close()
    
    golden_file1 = open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\CaseID_search_result_gold.txt", 'r').read()
    first_file2 = open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\CaseID_search_result.txt", 'r').read()
    assert golden_file1 == first_file2, "not equal files"
    
@Then('reset buttons for clearing all filleds')
def step_impl(context):   
    context.driver.find_element_by_id("btreset").click()

@When('search Case by Case_ID "{Case_ID}" negative check')
def step_impl(context, Case_ID):
    context.driver.find_element_by_id("caseId").send_keys(Case_ID)
    
@Then ('press filter to see searching results, but it will return error message')
def step_impl(context):
    context.driver.find_element_by_id("btfilter").click()
    text = context.driver.find_element_by_xpath("//li[contains(text(),'The Case id can only contain digits')]").text
    assert text == "The Case id can only contain digits", "error message is different"
    context.driver.find_element_by_id("btreset").click()



@when('search Case by Card_Number "{Card_Number}" positive check')
def step_impl(context, Card_Number):
    context.driver.find_element_by_id("caseCardNumber").send_keys(Card_Number)
    
    
@Then('press filter to see searching result Card_Number')
def step_impl(context):
    context.driver.find_element_by_id("btfilter").click()
    time.sleep(2)
    Card_Number = context.driver.find_element_by_xpath("//td[contains(text(),'487178XXXXXX5325')]").text
    #CardHolderName = context.driver.find_element_by_xpath("//tr[@class='(blank) t-first']//td[@class='cardHolderName'][contains(text(),'JOHN KÖNIG')]").text
    with open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\CaseID_search_result.txt", "w+") as file:
        file.write("Card_Number = " + Card_Number + '\n')
        #file.write("CardHolderName = " + CardHolderName + "\n")
        file.close()
        # with open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Detection\Other\search_result_gold.txt", "r") as filegold:
        #     context.assertTrue(filecmp(filegold, file, shallow=False))

    golden_file = r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\CaseID_search_result_gold.txt"
    first_file = r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\CaseID_search_result.txt"
    first_file_lines = open(first_file).readlines()
    golden_file_lines = open(golden_file).readlines()
    difference = difflib.HtmlDiff().make_file(first_file_lines, golden_file_lines, first_file, golden_file)
    difference_report = open(r'C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\CaseID_search_result.html', 'w')
    difference_report.write(difference)
    difference_report.close()
    
    golden_file1 = open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\CaseID_search_result_gold.txt", 'r').read()
    first_file2 = open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\CaseID_search_result.txt", 'r').read()
    assert golden_file1 == first_file2, "not equal files"
    context.driver.find_element_by_id("btreset").click()


@When('search Case by Card_Number "{Card_Number}" negative check')
def step_impl(context, Card_Number):
    context.driver.find_element_by_id("caseCardNumber").send_keys(Card_Number)
    
@Then ('press filter to see searching results, but it will return error message pan')
def step_impl(context):
    context.driver.find_element_by_id("btfilter").click()
    text = context.driver.find_element_by_xpath("//li[contains(text(),'The Pan is invalid')]").text
    assert text == "The Pan is invalid", "error message is different"
    context.driver.find_element_by_id("btreset").click()
    
    
@When('search Case by Case_ID "{Case_ID}" press Update_id')
def step_impl(context, Case_ID):    
    context.driver.find_element_by_id("caseId").send_keys(Case_ID)
    context.driver.find_element_by_id("btfilter").click()
    context.driver.find_element_by_xpath("//a[@class='btimgupdate']").click()
    time.sleep(5)

@When ('open case Details')
def step_impl(context):
    context.driver.find_element_by_id("showHide").click()
    
@When ('Case Status = Closed and Closure Reason = Investigation Completed')
def step_impl(context):
    case_status = context.driver.find_element_by_id("caseStatusUpdate")
    drp_case_status = Select(case_status)
    drp_case_status.select_by_visible_text("Closed")
    time.sleep(5)
    Closure_Reason = context.driver.find_element_by_id("closureReason")
    drp_Closure_Reason = Select(Closure_Reason)
    drp_Closure_Reason.select_by_visible_text("Investigation Completed")
    time.sleep(5)
@Then ('press save button for closing case')       
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@type='button']").click()
    case_status = context.driver.find_element_by_xpath("//td[@class='status']").text
    cardPan = context.driver.find_element_by_xpath("//td[@class='cardNumber t-sort-column-descending']").text
    with open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\close_status.txt", "w+") as file:
        file.write("case_status = " + case_status + '\n')
        file.write("Card Number = " + cardPan + "\n")
        file.close()
    
    golden_file = r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\close_status_gold.txt"
    first_file = r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\close_status.txt"
    first_file_lines = open(first_file).readlines()
    golden_file_lines = open(golden_file).readlines()
    difference = difflib.HtmlDiff().make_file(first_file_lines, golden_file_lines, first_file, golden_file)
    difference_report = open(r'C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\difference_close_report.html', 'w')
    difference_report.write(difference)
    difference_report.close()
    
    golden_file1 = open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\close_status_gold.txt", 'r').read()
    first_file2 = open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\close_status.txt", 'r').read()
    assert golden_file1 == first_file2, "not equal files" 

@Then ('reopen the case')  
def step_impl(context):
    context.driver.find_element_by_xpath("//a[@class='btimgreopen']").click()
    context.driver.find_element_by_xpath("//input[@type='button']").click()
    
    case_status = context.driver.find_element_by_xpath("//td[@class='status']").text
    cardPan = context.driver.find_element_by_xpath("//td[@class='cardNumber t-sort-column-descending']").text
    with open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\reopen_status.txt", "w+") as file:
        file.write("case_status = " + case_status + '\n')
        file.write("Card Number = " + cardPan + "\n")
        file.close()

    context.driver.close()
    
    golden_file = r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\reopen_status_gold.txt"
    first_file = r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\reopen_status.txt"
    first_file_lines = open(first_file).readlines()
    golden_file_lines = open(golden_file).readlines()
    difference = difflib.HtmlDiff().make_file(first_file_lines, golden_file_lines, first_file, golden_file)
    difference_report = open(r'C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\difference_reopen_report.html', 'w')
    difference_report.write(difference)
    difference_report.close()
    
    golden_file1 = open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\reopen_status_gold.txt", 'r').read()
    first_file2 = open(r"C:\Users\haykkh\Desktop\TestCaseOutput\e2e\Case\reopen_status.txt", 'r').read()
    assert golden_file1 == first_file2, "not equal files"    