Feature: Case search in CASE section.
    
    Scenario Outline: CASE Search
    Given launch Mozilla browser
    When open E2EFCM Homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    And User must successfully login to the Dashboard page
    And Go to Issuer Fraud Management page
    And Select CASE section
    And search Case by CaseId = "<caseId>"
    And search Case by CardNumber = "<caseCardNumber>"
    And search Case by PanReference = "<cardNumberRef>"
    #And search Case by Issuer = "<issuer>"
    #And search Case by Brand = "<caseBrand>"
    And search Case by CaseStatus = "<caseStatus>"
    And search Case by CasePriority = "<casePriorityForFilter>"
    #And search Case by DetectionSrc = "<detectionSrc>" (will open comment after fixing the ticket https://jira.worldline.com/browse/EWLFRMTEST-8840)
    And search Case by WorkflowStatus = "<workflowStatus>"
    And search Case by CaseFraudStatus = "<caseFraudStatus>"
    #And search Case by CaseFraudType = "<caseFraudReason>" (https://jira.worldline.com/browse/EWLFRMTEST-885)
    And search Case by CaseFraudSubType = "<caseFraudSubReason>"
    And search Case by CaseDateOpenedFrom = "<caseDateOpenedFrom>"
    And search Case by CaseDateOpenedTo = "<caseDateOpenedTo>"
    And search Case by CaseDateClosedFrom = "<caseDateClosedFrom>"
    And search Case by CaseDateClosedTo = "<caseDateClosedTo>"
    And search Case by DateWorkFlowSetFrom = "<dateWorkFlowSetFrom>"
    And search Case by DateWorkFlowSetTo = "<dateWorkFlowSetTo>"
    And search Case by LastUpdatedFrom = "<lastUpdatedFrom>"
    And search Case by LastUpdatedTo = "<lastUpdatedTo>"
    And search Case by CaseCardHolderName = "<cardHolderName>"
    And search Case by CaseReference = "<caseReference>"
    Then press filter to see searching case for all results
    Examples:
    | username   | password | caseId | caseCardNumber  | cardNumberRef                                                     | issuer               | caseBrand | caseStatus  | casePriorityForFilter | detectionSrc | workflowStatus | caseFraudStatus | caseFraudReason | caseFraudSubReason | caseDateOpenedFrom | caseDateOpenedTo | caseDateClosedFrom | caseDateClosedTo | dateWorkFlowSetFrom | dateWorkFlowSetTo | lastUpdatedFrom | lastUpdatedTo | cardHolderName | caseReference|
    | A764789    | test1234 | 36010  | 4871780046815325|  069F6B63F870E2ADA930F3E1BAC5471B51F10278AD6540360D9E557E07BD0614 | Comdirect Visa Debit |           | In Progress | 10                    | MANUAL       |   Write Off    | GENUINE         |  Lost           | ALTERED EMBOSSING  | 08/04/2021         |  08/04/2021      |  08/04/2021        |  08/04/2021      | 02/04/2021          | 03/04/2021        | 10/04/2021      |  14/04/2021   | JOHN KÖNIG     | J011         |






