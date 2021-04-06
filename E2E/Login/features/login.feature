Feature: Case search in CASE section.
    
    Scenario: CASE Search with Case ID
    Given launch Mozilla browser
    When open E2EFCM Homepage
    And Enter username "A764789" and password "test1234"
    And Click on login button
    Then User must successfully login to the Dashboard page
    Then Change password