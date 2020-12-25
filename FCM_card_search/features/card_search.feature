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
    | A764782    | test1234 |
    And Go to Issuer Fraud Management page
    And Select cards from Detection Cards section
    Then search cards by Cardholder Name
    And search cards by Card Number
    And search cards by Case Reference
    And search cards by Card Id
    And search cards by Bank Account Number
    And search cards by Additional Criteria (to be used in combination with CardHolder Name)
    


