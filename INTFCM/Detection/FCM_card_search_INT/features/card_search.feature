Feature: Card Search in FCM
    
    Scenario Outline: Login to INTFCM
    Given I launch Mozilla browser
    When I open FCM Homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    And User must successfully login to the Dashboard page

    And Go to Issuer Fraud Management page
    And Select cards from Detection Cards section
    And search cards by CardholderName "<CardholderName>"
    #And search cards by CardNumber "<CardNumber>"
    And search cards by Case Reference "<CaseReference>"
    And search cards by Card Id "<CardId>"
    And search cards by Bank Account Number "<BankAccountNumber>"
    Examples:
    | username   | password | BankAccountNumber      | CardId                                                           | CaseReference  | CardholderName   |
    | A764789    | test1234 | DE95200411552019155519 | FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF4971780401205595 | P001           | Poghos Simonyan  |
    
    Then search cards by Additional Criteria (to be used in combination with CardHolder Name)
    


