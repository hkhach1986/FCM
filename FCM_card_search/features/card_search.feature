Feature: Card Search in FCM
    
    Scenario Outline: Login to INTFCM
    Given I launch Mozilla browser
    When I open FCM Homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    And User must successfully login to the Dashboard page
    Examples:
    | username   | password |
    | A764789    | test1234 |
    And Go to Issuer Fraud Management page
    Then Select from Detection Cards section
    


