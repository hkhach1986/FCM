Feature: Card Payments Search in E2EFCM Detection->Other section.
    
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
    And search payment in other section by filters Card Entry Mode "<filter1>", Security Type "<filter2>", WLP FO Result Code "<filter4>"
########ISO Result Code "<filter3>"  parameter doesn't work properly whatever give it will return same result
    And search payment in other section by filter Transaction SubType "<filterTransactionSubType>" 
    And search payment in other section by filter Fall Back Flag "<filter5>"    

###for example Fall Back Flag should take 2 values 0 and 1 but if select 1 it will bring the results with 0
###Fall Back Flag shouldn't take string value, but when we give string "aa" it will not get the column red color and return Internal server error
###Transaction SubType doesn't pay attention the selected value, it will get same result whatever we give

    And search payment in other section by filters Company Id "<businessId>", Acceptor Id "<targetId>" 
    And search payment in other section by filter Acceptor Country "<targetCountryDropDown>"
    And search payment in other section by filters MCC "<mccIDDropDown>" 
#    And search payment in other section by filters Acquirer BIN "<targetProviderId>" 
    And search payment in other section by filters Terminal Id "<targetTechnicalId>"
    And search payment in other section by filters Acq Cntry Code "<filter7>", Alt PAN "<filter8>", Auth Id "<filter6>"
######Acq_Cntry_Code and Alt_PAN  return Internal Server error message
    Then press filter button
    Examples:
    | username   | password | convertedTransactionAmountFrom | convertedTransactionAmountTo | externalId | panReference                                                     | sourceCountryDropDown | sourceProviderId | filter0 | filter1 | filter2 | filter3   | filter4     | filter5 | filterTransactionSubType | businessId | targetId   | targetCountryDropDown | mccIDDropDown | targetProviderId | targetTechnicalId | filter6 | filter7 | filter8                                                          |
    | A764789    | test1234 | 49                             | 51                           |  8         | E9C07E171704E9EAB71EF8EBDA9C4130F68514CA657CF3204C32311EE1B884A4 | USA                   | 6601             | 90      |   04    | 14      |  0        | APP_OLW_O   |   0     | 100                      | 6601       | 1234567    | DEU                   | 5969          |                  | 00000001          | 190002  | USA     | 4A05A3B9F40DDD21F73F5749C4AC81CD465013541C857EDD8C155F46BB0CEE09 |



    


