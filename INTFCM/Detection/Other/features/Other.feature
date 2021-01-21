Feature: Card Payments Search in INTFCM Detection->Other section.
    
    Scenario Outline: Card Payments Search
    Given launch Mozilla browser
    When open INTFCM Homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    And User must successfully login to the Dashboard page
    And Go to Issuer Fraud Management page
    And Select Detection Other section
    And search payment in other section by transaction amounts "<convertedTransactionAmountFrom>", "<convertedTransactionAmountTo>"
    And search payment in other section by external ID "<externalId>", "<panReference>" 
    And search payment in other section by Issuer Country "<sourceCountryDropDown>"
    And search payment in other section by filters Issuer Id "<sourceProviderId>", POS Entry Mode "<filter0>"
#    And search payment in other section by filters Card Entry Mode "<filter1>", Security Type "<filter2>", ISO Result Code "<filter3>", WLP FO Result Code "<filter4>"
########All parameters doesn't work properly return "Internal server error"
    And search payment in other section by filter Transaction SubType "<filterTransactionSubType>" 
#    And search payment in other section by filter Fall Back Flag "<filter5>"    
###All parameters doesn't work properly as it return same result whatever you give
###for example Fall Back Flag should take 2 values 0 and 1 but if select 1 it will bring the results with 0
###Fall Back Flag shouldn't take string value, but when we give string "aa" it will not get the column red color and return Internal server error
###Transaction SubType doesn't pay attention the selected value, it will get same result whatever we give

    And search payment in other section by filters Company Id "<businessId>", Acceptor Id "<targetId>" 
    And search payment in other section by filter Acceptor Country "<targetCountryDropDown>"
    And search payment in other section by filters MCC "<mccIDDropDown>", Acquirer BIN "<targetProviderId>" 
    And search payment in other section by filters Terminal Id "<targetTechnicalId>"
#    And search payment in other section by filters Acq Cntry Code "<filter7>", Alt PAN "<filter8>", Auth Id "<filter6>"
######Acq_Cntry_Code and Alt_PAN  return Internal Server error message
    Then press filter button
    Examples:
    | username   | password | convertedTransactionAmountFrom | convertedTransactionAmountTo | externalId | panReference                                                    | sourceCountryDropDown | sourceProviderId | filter0 | filter1 | filter2 | filter3 | filter4     | filter5 | filterTransactionSubType | businessId | targetId   | targetCountryDropDown | mccIDDropDown | targetProviderId | targetTechnicalId | filter6 | filter7 | filter8 |
    | A764789    | test1234 | 0                              | 50                           |  8         | FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF9871781239657714| DEU                   | 6601             | 01      |         |         |         |             |         | 100                      | 6601       | 1095822540 | DEU                   | 5311          | 462764           | 1888325           |         |         |         |



    


