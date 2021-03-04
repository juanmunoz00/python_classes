class Constants():
	##1 = Prod/2 = Dev
	##Properties
	#<editor-fold desc="Description">
	App_Name = "ConflictMineralsRptTool"
	DEPLOY_MODE = 1 ##1 = Dev 2 = Prod
	ERR_PREFIX = "Ohhh my! "

	fileName = ''
	fileType = ''

	Plex_Manufacturer_Name = ''


	#</editor-fold>

	##Constants
	#region
	METAL_ID_DB_COL = 0
	METAL_NAME_DB_COL = 1
	#endregion
	##Manufacturer Name	Manufacturer Part Number	Description	 EAU 	 Target 	MFG QUOTED	MPN QUOTED	Quote (USD)	NCNR (Y/N)	LT (weeks)	COO	MIN	MULT	QOH	Comments/Notes
	CS_ANNUAL_QUOTE_MANUFACTURER_NAME_COL = 0
	CS_ANNUAL_QUOTE_MANUFACTURER_PART_NUMBER_COL = 1
	CS_ANNUAL_QUOTE_MANUFACTURER_DESCRIPTION_COL = 2
	CS_ANNUAL_QUOTE_MANUFACTURER_EAU_COL = 3
	CS_ANNUAL_QUOTE_MANUFACTURER_TARGET_COL = 4


	CS_QUOTE_ANALYZER_MANUFACTURER_NAME_COL = 1
	CS_QUOTE_ANALYZER_MANUFACTURER_PART_NUMBER_COL = 2
	CS_QUOTE_ANALYZER_MANUFACTURER_DESCRIPTION_COL = 3
	CS_QUOTE_ANALYZER_MANUFACTURER_EAU_COL = 4
	CS_QUOTE_ANALYZER_MANUFACTURER_TARGET_COL = 5
	CS_QUOTE_ANALYZER_MANUFACTURER_MFG_QUOTED_COL = 6
	CS_QUOTE_ANALYZER_MANUFACTURER_MPN_QUOTED_COL = 7
	CS_QUOTE_ANALYZER_MANUFACTURER_QUOTE_USD_COL = 8
	CS_QUOTE_ANALYZER_MANUFACTURER_NCNR_Y_N_COL = 9
	CS_QUOTE_ANALYZER_MANUFACTURER_LT_WEEKS_COL = 10
	CS_QUOTE_ANALYZER_MANUFACTURER_COO_COL = 11
	CS_QUOTE_ANALYZER_MANUFACTURER_MIN_COL = 12
	CS_QUOTE_ANALYZER_MANUFACTURER_MULT_COL = 13
	CS_QUOTE_ANALYZER_MANUFACTURER_QOH_COL = 14
	CS_QUOTE_ANALYZER_MANUFACTURER_COMMENTS_NOTES_COL = 15

	CS_QUOTE_ANALYZER_DETAILS_LOCATION_COL = 0
	CS_QUOTE_ANALYZER_MANUFACTURER_PART_NUMBER_COL = 1
	CS_QUOTE_ANALYZER_MANUFACTURER_NAME_COL = 2
	CS_QUOTE_ANALYZER_NAME_COL = 3
	CS_QUOTE_ANALYZER_PART_NUMBER_COL = 4
	CS_QUOTE_ANALYZER_EAU_COL = 5
	CS_QUOTE_ANALYZER_CUSTOMER_COL = 6
	##CS_QUOTE_ANALYZER_CUSTOMER_COL = 8


	##Page
	Common_SmelterList_AdditionalInfo_Declaration_Page = 3
	##SupplierManufacturerId
	Common_SmelterList_AdditionalInfo_Declaration_Page_TemplateRevision_Row=2
	Common_SmelterList_AdditionalInfo_Declaration_Page_TemplateRevision_Col=9

	##Company Name
	Common_SmelterList_AdditionalInfo_Declaration_Page_Company_Name_Row = 7
	Common_SmelterList_AdditionalInfo_Declaration_Page_Company_Name_Col = 3

	##Declaration of scope
	Common_SmelterList_AdditionalInfo_Declaration_Page_Declaration_Of_Scope_Row = 8
	Common_SmelterList_AdditionalInfo_Declaration_Page_Declaration_Of_Scope_Col = 3

	##Contact Name
	Common_SmelterList_AdditionalInfo_Declaration_Page_Contact_Name_Row = 14
	Common_SmelterList_AdditionalInfo_Declaration_Page_Contact_Name_Col = 3

	##Contact Email
	Common_SmelterList_AdditionalInfo_Declaration_Page_Contact_Email_Row = 15
	Common_SmelterList_AdditionalInfo_Declaration_Page_Contact_Email_Col = 3

	##Contact Phone
	Common_SmelterList_AdditionalInfo_Declaration_Page_Contact_Phone_Row = 16
	Common_SmelterList_AdditionalInfo_Declaration_Page_Contact_Phone_Col = 3

	##----------------------------------
	##Common_SmelterList_Requiring_DD
	Common_SmelterList_Requiring_DD = 0
	Common_SmelterList_Requiring_DD_Row = 2

	Common_SmelterList_Requiring_DD_Metal_Col = 0
	Common_SmelterList_Requiring_DD_Smelter_Name_Col = 1
	Common_SmelterList_Requiring_DD_Smelter_ID_Col = 2
	Common_SmelterList_Requiring_DD_Country_Location_Col = 3
	Common_SmelterList_Requiring_DD_Eligible_Smelter_Col = 4
	Common_SmelterList_Requiring_DD_Smelter_Operational_Status_Col = 5
	Common_SmelterList_Requiring_DD_Audit_Status_Col = 6
	Common_SmelterList_Requiring_DD_Supplier_Feedback_Col = 7

	Common_SmelterList_Requiring_DD_Watch_List_Metal_Cell_Col = 0
	Common_SmelterList_Requiring_DD_Watch_List_Smelter_ID_Cell_Col = 1
	Common_SmelterList_Requiring_DD_Watch_List_Smelter_Name_Cell_Col = 2
	Common_SmelterList_Requiring_DD_Watch_List_Smelter_Operational_Status_Cell_Col = 3
	Common_SmelterList_Requiring_DD_Watch_List_Audit_Status_Cell_Col = 4
	Common_SmelterList_Requiring_DD_Watch_List_Supplier_Feedback_Cell_Col = 5
	Common_SmelterList_Requiring_DD_Watch_List_Supplier_Contact_Name_Col = 6
	Common_SmelterList_Requiring_DD_Watch_List_Supplier_Contact_Email_Col = 7

	##Comon_Smelter_Mandatory_List
	Common_SmelterList_Mandatory_List_SupplierManufacturerName_Col = 2
	Common_SmelterList_Mandatory_List_Mandatory_Flag_Col = 7

	Common_SmelterList_SmelterList_Page = 4
	##Metal
	Common_SmelterList_SmelterList_Metal_Row = 4
	Common_SmelterList_SmelterList_Metal_Col = 1

	##Smelter Name (StdSmelterId)
	Common_SmelterList_SmelterList_SmelterName_Col = 2
	Common_SmelterList_SmelterList_SmelterCountry_Col = 4
	Common_SmelterList_SmelterList_SmelterId_Col = 5
	Common_SmelterList_SmelterList_SourceOfIdentificationNumber_Col = 6
	Common_SmelterList_SmelterList_SmelterStreetCol = 7
	Common_SmelterList_SmelterList_SmelterCityCol = 8
	Common_SmelterList_SmelterList_SmelterStateProvinceCol = 9

	Common_SmelterList_SmelterList_Page = 4
	##Metal
	Common_SmelterList_SmelterList_Metal_Row = 4
	Common_SmelterList_SmelterList_Metal_Col = 1
	##Smelter Name (StdSmelterId)
	Common_SmelterList_SmelterList_SmelterName_Col = 2
	Common_SmelterList_SmelterList_SmelterCountry_Col = 4
	Common_SmelterList_SmelterList_SmelterId_Col = 5
	Common_SmelterList_SmelterList_SourceOfIdentificationNumber_Col = 6
	Common_SmelterList_SmelterList_SmelterStreetCol = 7
	Common_SmelterList_SmelterList_SmelterCityCol = 8
	Common_SmelterList_SmelterList_SmelterStateProvinceCol = 9
	Common_SmelterList_SmelterList_SmelterContactName = 10
	Common_SmelterList_SmelterList_SmelterContactEmail = 11
	##12 - 16
	SMELTERS_LIST_PROPOSED_NEXT_STEPS = 12
	SMELTERS_LIST_NAME_OF_MINES_OR_IF_RECYCLED = 13
	SMELTERS_LIST_LOCATION_OF_COUNTRY_OF_MINES_OR_RECYLED = 14
	SMELTERS_LIST_DOES_100PCT_ORIGINATED_FROM_RECYCLED = 15
	SMELTERS_LIST_COMMENTS = 16

	##Master list
	XLS_EXTENSION = ".xls"
	XLSX_EXTENSION = ".xlsx"

	CMRT_MASTER_LIST_SUMMARY_ROW = 1
	CMRT_MASTER_LIST_INITIAL_ROW = 3
	CMRT_MASTER_LIST_INITIAL_COL = 0
	CMRT_MASTER_LIST_LIST = 0

	CMRT_MASTER_LIST_PLEX_MANUFACTURER_NAME_COL = 0
	CMRT_MASTER_LIST_SUPPLIER_FILE_COL = 1
	CMRT_MASTER_LIST_SUPPLIER_NAME_COL = 2
	CMRT_MASTER_LIST_SUPPLIER_CMRT_REV_COL = 3
	CMRT_MASTER_LIST_SUPPLIER_SCOPE_COL = 4

	CMRT_MASTER_LIST_PLEX_MANUFACTURER_NAME_CELL_COL = "A"
	CMRT_MASTER_LIST_SUMMARY_CELL_COL = "B"
	CMRT_MASTER_LIST_SUPPLIER_FILE_CELL_COL = "B"
	CMRT_MASTER_LIST_SUPPLIER_NAME_CELL_COL = "C"
	CMRT_MASTER_LIST_SUPPLIER_CMRT_REV_CELL_COL = "D"
	CMRT_MASTER_LIST_SUPPLIER_SCOPE_CELL_COL = "E"
	CMRT_MASTER_LIST_SUPPLIER_MANDATORY_CELL_COL = "H"
	CMRT_MASTER_LIST_SUPPLIER_CONTACT_EMAIL_CELL_COL = "I"

	NCOL_A = 0
	NCOL_B = 1
	NCOL_C = 2
	NCOL_D = 3
	NCOL_E = 4
	NCOL_F = 5
	NCOL_G = 6
	NCOL_H = 7
	NCOL_I = 8
	NCOL_J = 9
	NCOL_K = 10
	NCOL_L = 11
	NCOL_M = 12
	NCOL_N = 13
	NCOL_O = 14
	NCOL_P = 15
	NCOL_Q = 16
	NCOL_R = 17
	NCOL_S = 18
	NCOL_T = 19
	NCOL_U = 20
	NCOL_V = 21
	NCOL_W = 22
	NCOL_X = 23
	NCOL_Y = 24
	NCOL_Z = 25

	COL_A = "A"
	COL_B = "B"
	COL_C = "C"
	COL_D = "D"
	COL_E = "E"
	COL_F = "F"
	COL_G = "G"
	COL_H = "H"
	COL_I = "I"
	COL_J = "J"
	COL_K = "K"
	COL_L = "L"
	COL_M = "M"
	COL_N = "N"
	COL_O = "O"
	COL_P = "P"
	COL_Q = "Q"
	COL_R = "R"
	COL_S = "S"
	COL_T = "T"
	COL_U = "U"
	COL_V = "V"
	COL_W = "W"
	COL_X = "X"
	COL_Y = "Y"
	COL_Z = "Z"

	##Dictionary name
	Common_SmelterList_SmelterList_dictMetals = 1
	Common_SmelterList_SmelterList_dictSmelters = 2
	Common_SmelterList_SmelterList_dict_countries = 3
	Common_SmelterList_SmelterList_dict_cities = 4
	Common_SmelterList_SmelterList_dict_states = 5

	##Tables
	Common_SmelterList_SmelterList_Common_Smelters_Metals = "Common_Smelters_Metals"
	Common_SmelterList_SmelterList_Common_Smelters_CountriesTbl = "Common_Smelters_Countries"
	Common_SmelterList_SmelterList_Common_Smelters_StatedTbl = "Common_Smelters_States"
	Common_SmelterList_SmelterList_Common_Smelters_CitiesTbl = "Common_Smelters_Cities"



class DBConnectionString():
	DEPLOY_MODE_DEV = 1
	DEPLOY_MODE_DEV_TXT = "DEV"

	DEPLOY_MODE_PROD = 2
	DEPLOY_MODE_PROD_TXT = "PROD"

	APP_NAME = "Quote_Analyzer"

	QRY_GET_APP_SETTINGS = "SELECT TOP 1 a.App_Name as 'App Name' ,d.Deploy_Mode_ID as 'Deploy_Mode_ID',d.Deploy_Mode as 'Deploy_Mode', a.Version, a.Current_Commit, c.Datasource as 'Datasource',c.Ds_Database as 'Database',c.Ds_User_Name as 'User_Name',c.Ds_Password as 'Password' FROM AppSettings_Applications a join AppSettings_Deploy_Mode d on a.Deploy_Mode = d.Deploy_Mode_ID join AppSettings_ConnStrings c on a.App_ID = c.App_ID WHERE a.App_Name = 'ConflictMineralsRptTool'	AND c.Deploy_Mode = a.Deploy_Mode"
	##QRY_GET_APP_SETTINGS_CS_QUOTE_ANALYZER_AZ = "SELECT TOP 1 a.App_Name as 'App Name' ,d.Deploy_Mode_ID as 'Deploy_Mode_ID',d.Deploy_Mode as 'Deploy_Mode', a.Version, a.Current_Commit, c.Datasource as 'Datasource',c.ds_Database as 'Database',c.ds_username as 'User_Name',c.ds_Password as 'Password' FROM tblAppSettings_Applications a join tblAppSettings_Deploy_Mode d on a.Deploy_Mode = d.Deploy_Mode_ID join tblAppSettings_ConnStrings c on a.App_ID = c.App_ID WHERE a.App_Name = 'Quote_Analyzer'	AND c.Deploy_Mode = a.Deploy_Mode"
	QRY_GET_APP_SETTINGS_CS_QUOTE_ANALYZER_AZ = "SELECT TOP 1 a.App_Name as 'App Name' ,d.Deploy_Mode_ID as 'Deploy_Mode_ID',d.Deploy_Mode as 'Deploy_Mode', a.Version, a.Current_Commit "
	QRY_GET_APP_SETTINGS_CS_QUOTE_ANALYZER_AZ = QRY_GET_APP_SETTINGS_CS_QUOTE_ANALYZER_AZ + " , c.Datasource as 'Datasource',c.ds_Database as 'Database',c.ds_username as 'User_Name',c.ds_Password as 'Password' "
	QRY_GET_APP_SETTINGS_CS_QUOTE_ANALYZER_AZ = QRY_GET_APP_SETTINGS_CS_QUOTE_ANALYZER_AZ + " FROM tblAppSettings_Applications a join tblAppSettings_Deploy_Mode d on a.Deploy_Mode = d.Deploy_Mode_ID "
	QRY_GET_APP_SETTINGS_CS_QUOTE_ANALYZER_AZ = QRY_GET_APP_SETTINGS_CS_QUOTE_ANALYZER_AZ + " join tblAppSettings_ConnStrings c on a.App_ID = c.App_ID  "
	QRY_GET_APP_SETTINGS_CS_QUOTE_ANALYZER_AZ = QRY_GET_APP_SETTINGS_CS_QUOTE_ANALYZER_AZ + " WHERE a.App_Name = '" + APP_NAME +"'   AND c.Deploy_Mode = a.Deploy_Mode  "

	"""
	Deploy modes:
	1 - Dev
	2 - Prod
	"""

	driver= '{SQL Server}'
	App_Settings_Deploy_Mode_Id = 2
	App_Settings_Server = ''
	App_Settings_Database = ''
	App_Settings_User_Name = ''
	App_Settings_Password = ''

	App_Settings_App_Name = ''
	App_Settings_Version = ''
	App_Settings_Current_Commit = ''

	##def __init__(self, App_Settings_Deploy_Mode, App_Settings_Server,App_Settings_Database,App_Settings_User_Name,App_Settings_Password):
	##Connection settings
	##Azure
	server = 'tcp:s5s4ajlw7v.database.windows.net,1433'##'s5s4ajlw7v.database.windows.net'
	database = 'AZ_Dev_Test'##'Collaborations'
	username = 'jbrubaker'
	password = 'j88975First'
	##'{ODBC Driver 13 for SQL Server}'

	##Local
	"""
	serverLcl = 'tcp:10.120.10.15,1433'##'s5s4ajlw7v.database.windows.net'
	databaseLcl = 'DEV_TEST_DB'
	usernameLcl = ''
	passwordLcl = 'j88975First'
	driverLcl= '{SQL Server}'##'{ODBC Driver 13 for SQL Server}'
	##yes = "yes"
	"""

	##10.15
	serverLcl = 'tcp:10.120.10.15,1433'##'s5s4ajlw7v.database.windows.net'
	databaseLcl = 'DEV_TEST_DB'
	usernameLcl = 'PVSUser2'
	passwordLcl = 'U$3rPVS'
	driverLcl= '{SQL Server}'##'{ODBC Driver 13 for SQL Server}'


	##10.4
	##Local
	server10_4 = 'tcp:10.120.10.4,1433'##'s5s4ajlw7v.database.windows.net'
	database10_4 = 'BeFirst'
	username10_4 = 'DBuser'
	password10_4 = 'DBuser2018*'
	driver10_4= '{SQL Server}'##'{ODBC Driver 13 for SQL Server}'


	##App_Settings_Driver10_4= '{SQL Server}'##'{ODBC Driver 13 for SQL Server}'

	yes = "yes"

	##DB Tables
	COMMON_SMELTERS_METALS = "Common_Smelters_Metals"

	COMMON_SMELTERS_DECLARATION = "Common_Smelters_Declaration"
	COMMON_SMELTERS_DECLARATION_DEV = "Common_Smelters_Declaration_Dev"

	COMMON_SMELTERSLIST = "Common_SmeltersList"
	COMMON_SMELTERSLIST_DEV = "Common_SmeltersList_Dev"

	COMMON_SMELTERS_REQ_DD = "Common_Smelters_Requiring_DD"
	COMMON_SMELTERS_REQ_DD_DEV = "Common_Smelters_Requiring_DD_Dev"

	COMMON_SMELTERS_MANDATORY = "Common_Smelters_Mandatory_List"
	COMMON_SMELTERS_MANDATORY_DEV = "Common_Smelters_Mandatory_List_Dev"

	CS_QUOTE_ANALYZER_QUOTE_RESPONSES_TBL = "Commodity_Strategy_Quote_Responses_Dev1"##"Commodity_Strategy_Quote_Responses"
	CS_QUOTE_ANALYZER_QUOTE_RESPONSES_TBL_DEV = "Commodity_Strategy_Quote_Responses_Dev1"
	CS_NEW_FUTURE_PPV_TBL = "CS_New_Future_PPV"

class Functions():

	LOAD_ORIGINAL_QUOTE = 0
	LOAD_ORIGINAL_QUOTE_DETAILS = 0
	LOAD_COMMODITY_STRATEGY_EXECUTION_MASTER = 0

	LOAD_ORIGINAL_QUOTE_CLEAN_START_PER_SUPPLIER = 0
	LOAD_ORIGINAL_QUOTE_CLEAN_START = 0
	LOAD_QUOTES = 0
	LOAD_PARTS_WITH_NO_QUOTES = 0
	CS_CONSOLIDATED_INSERT_RECORDS = 0

	RUN_POST_CONSOLITATION_VERIFICATION = 0
	INSERT_RE_CONSOLIDATION_RECORD = 0
	GET_LOWEST_QUOTE_PRICE_BY_PN = 0

	LOAD_NEW_FUTURE_PPV = 0
	STD_COST_TO_NEW_FUTURE_PPV = 1
	OVERRIDE_FLAG_UPDATE_CS_LOWEST_QUOTES_TABLE = 1
	UPDATE_STD_COST_TO_NEW_FUTURE_PPV = 1
	UPDATE_PCN_OR_SUPPLIERCODE_DISCREPANCY = 0 ## Can it be deleted?

	DEBUG_ON_PN = 0
	DEBUG_ON_PN_PN = '35-11397'

	DISPLAY_QUOTE_DATA = 0
	DISPLAY_PO_DATA = 0
	DISPLAY_PO_DATA_NOT_FOUND_FOR_MFG_MPN = 0

	DISPLAY_CONSOLIDATED_RECORD = False
	DISPLAY_RE_CONSOLIDATED_PN_WITH_NO_PO = False
	DISPLAY_RE_CONSOLIDATED_MFG_MPN_NOT_FOUND_IN_QUOTES = True

	LOWST_QTE_DISPLAY_INSERT = False
	LOWST_QTE_DISPLAY_NOT_INSERTED = False



	##COMPARE_QUOTES = 1
