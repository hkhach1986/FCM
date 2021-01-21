Feature: Card Payments Search in INTFCM
    
    Scenario Outline: Card Payments Search
    Given launch Mozilla browser
    When open INTFCM Homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    And User must successfully login to the Dashboard page
    And Go to Issuer Fraud Management page
    And Select Detection Card Payments section
    And search card payment by "<ACC_ID>", "<ACC_Country>", "<MCC>", "<Pan_Reference>", "<Terminal_ID>"
    # And search card payment by "<ACC_Country>"
 #   And search card payment by "<Clear_Pan>"
    # And search card payment by "<MCC>"
    # And search card payment by "<Pan_Reference>"
    # And search card payment by "<Terminal_ID>"
    # And search card payment by "<Transaction_Date_From>"
    # And search card payment by "<Transaction_Date_To>"
    Then press filter button
    Examples:
    | username   | password | ACC_ID     | ACC_Country | MCC  | Pan_Reference                                                   | Terminal_ID |
    | A764789    | test1234 | 1095822540 | DEU         | 5311 | FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF9871781239657714| 1888325     |

    


