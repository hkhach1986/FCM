class Constants:
####Login page contains 3 buttons
    LOGIN = "login"
    PSW = "password"
    ENTER = "bthp"
    
###Issuer Fraud Management

    Issuer_fraud_management = "//div[@class='dvList']//ul//li//a[contains(text(),'Issuer Fraud Management')]"
#####Case section contains
    Case_section = "//a[contains(text(),'Case')]"
    Case_subgroup = "//a[contains(text(),'Case')]"
    CaseId = "caseId"
    CardNumber = "caseCardNumber"
    PanReference = "cardNumberRef"
    Issuer = "issuer"
    Brand = "caseBrand"
    CaseStatus = "caseStatus"
    CasePriority = "casePriorityForFilter"
    DetectionSrc = "detectionSrc"
    WorkflowStatus = "workflowStatus"
    CaseFraudStatus = "caseFraudStatus"
    CaseFraudType = "caseFraudReason"
    CaseFraudSubType = "caseFraudSubReason"
    CaseDateOpenedFrom = "caseDateOpenedFrom"
    CaseDateOpenedTo = "caseDateOpenedTo"
    CaseDateClosedFrom = "caseDateClosedFrom"
    CaseDateClosedTo = "caseDateClosedTo"
    DateWorkFlowSetFrom = "dateWorkFlowSetFrom"
    DateWorkFlowSetTo = "dateWorkFlowSetTo"
    LastUpdatedFrom = "lastUpdatedFrom"
    LastUpdatedTo = "lastUpdatedTo"
    CaseToCheck = "caseToCheck"
    CaseTransferred = "caseTransferred"
    CaseCardHolderName = "cardHolderName"
    CaseReference = "caseReference"
    ConfimedFraudReport = "btconfirmedfraudreport"
    WriteoffReport = "btwriteoffreport"
    NextCase = "btnextcase"
    Filter = "btfilter"
    Reset = "btreset"
    Print = "pagelink"
    CaseDisplay = "rppSelect"
    CaseBack = "//a[contains(text(),'BACK')]"
    CaseTop = "//a[contains(text(),'TOP')]"
    BulkClearPan = "bulkClearPanBt"
    
####Case manipulation #####
    ConsultId = "//a[@class='btimgconsult']"
    UpdateId = "//a[@class='btimgupdate']"
    ReopenCase = "//a[@class='btimgreopen']"
    Transfer = "//a[@class='btimgtransfer']"
    AssignId = "//a[@class='btimgAssign']"
    
#####Case detail page on Update mode
    ####Case detail
    UShowHideCaseDetails = "showHide"
    UWorkflowStatusUpdate = "workflowStatusUpdate"
    UCaseStatus = "caseStatusUpdate"
    UClosureReason = "closureReason"
    UPriority = "casePriorityUpdate"
    UAssignTo = "caseAssignedToUpdate"
    ###Alert detail
    UShowHideAlertDetails = "showHide_0"
    UDetectionSource = "detectionSourceUpdate"
    UFraudStatusComment = "fraudStatusCommentAssign"
    UFraudStatus = "fraudStatusUpdate"
    UFraudInfo = "fraudInformationUpdate1"
    UValidUntil = "validUntilUpdate"
    ###Card Holder Details
    UShowHideCardHolderDetails = "showHide_1"
    UCopy = "submit_1"
    ###Contanct
    UShowHideContact = "showHide_2"
    UWait = "contactDataWaitForUpdate"
    UWaitHourMin = "contactDataWaitForUpdateMinHour"
    UContactCustomer = "contactDataContactCustomerUpdate"
    UComment = "contactDataCommentUpdate"
    UViewCardDestails = "pagelink_0"
    UBlockCard = "pagelink_1"
    ULetterSent = "submit_2"
    UCallOutgoing = "submit_3"
    UCallIncoming = "submit_4"
    
    
    ####Authorization 
    URecentAuthorization = "//span[contains(text(),'RECENT AUTHORIZATIONS')]"
    UOperation = "//a[contains(text(),'OPERATION')]"
    UEvent = "//a[contains(text(),'EVENT')]"
    URecentCard = "//a[contains(text(),'RECENT CARD')]"
    UCardList = "//a[contains(text(),'CARD LIST')]"
    
    UAllFields = "select_2"
    UAuthorisationReceivedfrom = "authorisationReceivedfrom"
    UDetectionTimeFrom = "detectionTimeFrom"
    UAuthorisationUntil = "authorisationUntil"
    UDetectionTimeTo = "detectionTimeTo"
    UAuthFilter = "submit_6"
    Umastercheckbox = "mastercheckbox"
    UDeclareGenuine = "bulkDeclareGenuine"
    UDeclareSuspisous = "bulkDeclare"
    UDeclareFraud = "bulkDeclareFrd"
    UCaseDetailsSave = "//input[@type='button']"
    
    UExportType = "exporTypeModel"
    UExport = "exportBt"
    UExportAll = "massExportBt"
    UPrepareManualAlert = "submit_10"
    UCreateLetter = "pagelink_4"
    UCancel = "submit_11"
    
#####Case List #####
    CLCardNumber = "//td[@class='cardNumber t-sort-column-descending']"
    CLCardReferenceNumber = "//td[@class='cardNumberReference']"
    CLPSNExpaieryDate = "//td[@class='sequenceNumber']"
    CLPriority = "//td[@class='priority']"
    CLBrandID = "//td[@class='brandId']"
    CLCardHolderName = "//td[@class='cardHolderName']"
    CLCaseStatus = "//td[@class='status']"
    CLCaseFraudStatus = "//td[@class='fraudStatus']"
    CLCaseFraudType = "//td[@class='fraudTypeLabel']"
    CLCaseFraudSubtype = "//td[@class='fraudSubTypeLabel']"
    CLWorkFlowStatus = "//td[@class='workflowStatus']"
    CLCaseCreationDate = "//td[@class='creationDate']"
    CLIssuer = "//td[@class='issuer']"

    
####Case List Rows
    RCardNumber = "//a[@class='t-sort-column-descending'][contains(text(),'Card Number')]"
    RCardReferenceNumber = "//a[contains(text(),'Card Number Reference:')]"
    RPSNExpaieryDate = "//a[contains(text(),'psn expiry date')]"
    RPriority = "//a[contains(text(),'Priority :')]"
    RBrandID = "//a[contains(text(),'BRAND ID')]"
    RCardHolderName = "//a[contains(text(),'Cardholder Name:')]"
    RCaseStatus = "//a[contains(text(),'CASE STATUS')]"
    RCaseFraudType = "//a[contains(text(),'CASE FRAUD TYPE')]"
    RCaseFraudSubtype = "//a[contains(text(),'CASE FRAUD SUB TYPE')]"
    RWorkFlowStatus = "//a[contains(text(),'Workflow Status:')]"
    RCaseCreationDate = "//a[contains(text(),'CASE CREATION DATE')]"
    RIssuer = "//a[@rel='nofollow'][contains(text(),'issuer')]"
    RCheckbox = "//input[@id='mastercheckbox']"
    
    
