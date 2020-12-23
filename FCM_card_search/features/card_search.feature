Feature: Card Search in FCM
    
    Scenario Outline: Login to INTFCM
    Given I launch Mozilla browser
    When I open FCM Homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to the Dashboard page
    Examples:
    | username   | password |
    | A764789    | test1234 |

