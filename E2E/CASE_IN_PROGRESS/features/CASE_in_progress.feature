Feature: Change Case status when the Case Status = In Progress

    Scenario: CASE Search with Case ID
    Given launch Mozilla browser
    When open E2EFCM Homepage
    And Enter username "A764789" and password "test1234"
    And Click on login button
    And User must successfully login to the Dashboard page
    And Go to Issuer Fraud Management page
    And Select CASE section
    And search Case by Case_ID "45006" positive check
    And click on ConsultId button
