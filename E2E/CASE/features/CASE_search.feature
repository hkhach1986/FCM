Feature: Case search in CASE section.
    
    Scenario: CASE Search with Case ID
    Given launch Mozilla browser
    When open E2EFCM Homepage
    And Enter username "A764789" and password "test1234"
    And Click on login button
    And User must successfully login to the Dashboard page
    And Go to Issuer Fraud Management page
    And Select CASE section
    And search Case by Case_ID "36010" positive check
    Then press filter to see searching results
    Then reset buttons for clearing all filleds
    When search Case by Case_ID "qqqq" negative check
    Then press filter to see searching results, but it will return error message 
    #The Case id can only contain digits
    Then reset buttons for clearing all filleds     
    When search Case by Card_Number "4871780046815325" positive check
    Then press filter to see searching result Card_Number
    When search Case by Card_Number "vvv" negative check
    Then press filter to see searching results, but it will return error message pan
    When search Case by Case_ID "36010" press Update_id
    When open case Details
    When Case Status = Closed and Closure Reason = Investigation Completed
    Then press save button for closing case
    #When Show Alert Details
    Then reopen the case



