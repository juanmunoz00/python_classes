import matplotlib.pyplot as plt
import pandas as pd
import scipy
import numpy as np
import seaborn as sns

import sys

import pyodbc

from sklearn import preprocessing
from matplotlib import pyplot

from os import system, name
import os

import xlrd, xlwt
from xlutils.copy import copy
from openpyxl import load_workbook

from datetime import datetime
from time import sleep
import time

from alive_progress import alive_bar
from progress.bar import ShadyBar

import re

# import the smtplib module. It should be included in Python by default
import smtplib

import email.utils
from email.mime.text import MIMEText
import getpass
import numbers
from decimal import Decimal

import Classes

##https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
import sys
sys.path.append('C:/Apps/Common_Classes_and_Functions')
##from scriptName import functionName #scriptName without .py extension
##---------------------------------


def LoadSuppliers():
	try:
		qry = "SELECT [SupplierID], [Supplier_Desc] FROM tblSupplier"
		suppliersList = pd.read_sql_query(qry,cnxn)##From Azure

		print("Retrieving suppliers list... Done!")

		return suppliersList
	except Exception as e:
			print(Classes.Constants.ERR_PREFIX + "LoadSuppliers() -")
			print type(e)
			print(e)

def execQuery(qry):
	try:
		cursor.execute(qry)
		cursor.commit()
	except Exception as e:
		print(Classes.Constants.ERR_PREFIX + "execQuery() -")
		print type(e)
		print(e)

def Load_Original_Quote_Clean_Start(quote_supplier,SupplierID):
	try:
		delay = 0.25  ##Delay for quarter of a second
		if( ObjFunctions.LOAD_ORIGINAL_QUOTE_CLEAN_START == 1 ):
			qry = "TRUNCATE TABLE Commodity_Strategy_Quote_Responses_Dev1"
			execQuery(qry)
			##cursor.execute(qry)
			##cursor.commit()

			time.sleep(delay)

			qry = "TRUNCATE TABLE CS_Quote_Response_Files"
			execQuery(qry)

			time.sleep(delay)

			qry = "TRUNCATE TABLE CS_Consolidated_Data"
			execQuery(qry)

			time.sleep(delay)

			print("Quotes clean start... tables have been initialized")
		else:
			if( ObjFunctions.LOAD_ORIGINAL_QUOTE_CLEAN_START_PER_SUPPLIER == 1 ):
				qry = "DELETE FROM  Commodity_Strategy_Quote_Responses_Dev1 WHERE Supplier_Quote = '" + quote_supplier + "'"
				execQuery(qry)

				time.sleep(delay)

				qry = "DELETE FROM  CS_Quote_Response_Files WHERE SupplierID = " + str(SupplierID)
				execQuery(qry)

				time.sleep(delay)

				qry = "DELETE FROM  CS_Consolidated_Data WHERE Quote_Supplier = " + str(SupplierID)
				execQuery(qry)

				print("Quotes clean start... tables for supplier " + quote_supplier +  " have been initialized")

		qry = "TRUNCATE TABLE CS_Consolidated_Data_Lowest_Quote_Only"
		execQuery(qry)

	except Exception as e:
		print(Classes.Constants.ERR_PREFIX + "Load_Original_Quote_Clean_Start() -")
		print type(e)
		print(e)


def GetPOsByPN(part_no):
	try:
		open_po_releases = 0

		qry="select count(*) as 'open_po_releases' from Open_PO_Data where Part_No = '" + part_no + "' and Blanket_Order = 1 "
		##print(str(qry))
		Po_Data = pd.read_sql_query(qry,tendotCnxn)##Get it from po data table in 10.15

		if(len(Po_Data) > 0):
			open_po_releases = Po_Data["open_po_releases"].iloc[0]
			##print(str(open_po_releases))

		return open_po_releases

	except Exception as e:
			print(Classes.Constants.ERR_PREFIX + "GetPOsByPN() -")
			print type(e)
			print(e)

def InsertConsolidatedDataRow(dB_table, pcn, part_no, part_key, mfg_name, mpn, supplier_code, std_cost, po_price, quote_supplier, quote_price, eau_qty, demand_qty, ppv_eau, ppv_primary_po, ncnr,lt_weeks,coo,_min,_mult,_qoh,comments):
	try:


		SQLCommand = ("INSERT INTO " + dB_table + " ([PCN],[Part_No],[Part_Key],[Manufacturer_Name],[Manufacturer_Part_Number],[Supplier_Code],[Std_Cost],[PO_Price],[Quote_Supplier],[Quote_Price],[EAU_Quantity],[Demand_Quantity],[PPV_at_EAU],[PPV_at_Primary_PO], [NCNR_Y_N],[LT_Weeks],[COO],[_MIN],[_MULT],[_QOH],[Comments_Notes]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);")
		Values = [pcn, part_no, part_key, mfg_name, mpn, supplier_code, std_cost, po_price, quote_supplier, quote_price, eau_qty, demand_qty, ppv_eau, ppv_primary_po, ncnr,lt_weeks,coo,_min,_mult,_qoh,comments]

		##print(SQLCommand)
		##print(Values)

		cursor.execute(SQLCommand,Values)
		cursor.commit()

		if( ObjFunctions.DISPLAY_CONSOLIDATED_RECORD == True ): print("Consolodated data. PCN " + str(pcn) + " Part_No " + str(part_no) + " inserted...")

	except Exception as e:
		print(Classes.Constants.ERR_PREFIX + "InsertConsolidatedDataRow() -")
		print type(e)
		print(e)

def InsertQuoteRow(dB_table,Supplier_Quote, Part_Number,Mfg_Name,MPN,Description,EAU,Target,Mfg_Quoted,Mpn_Quoted,Quote_USD,NCNR,LT,COO,_Min,Mult,QOH,Comments_Notes,fas,ms,discrepnacy,filename):
	try:

		SQLCommand = ("INSERT INTO " + dB_table + " ([Supplier_Quote],[Part_No],[Manufacturer_Name],[Manufacturer_Part_Number],[_Description],[EAU],[_Target],[MFG_QUOTED],[MPN_QUOTED],[Quote_USD],[NCNR_Y_N],[LT_Weeks],[COO],[_MIN],[_MULT],[_QOH],[Comments_Notes],[Firstronics_Annual_Savings],[Montly Savings],[MPNDiscrepancy],[File_Name]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);")
		Values = [Supplier_Quote, Part_Number,Mfg_Name,MPN,Description,EAU,Target,Mfg_Quoted,Mpn_Quoted,Quote_USD,NCNR,LT,COO,_Min,Mult,QOH,Comments_Notes,fas,ms,discrepnacy,filename]

		##print(SQLCommand)
		##print(Values)

		cursor.execute(SQLCommand,Values)
		cursor.commit()

		##print("Quote Data Mfg_Name " + str(Mfg_Name) + " MPN " + str(MPN) + " quote " + str(Quote_USD) + " inserted...")

	except Exception as e:
		print(Classes.Constants.ERR_PREFIX + "InsertQuoteRow() -")
		print type(e)
		print(e)

def GetAllOpen_PO_Data():
	try:
		qry="select * from Open_PO_Data1 where Blanket_Order = 1"
		OpenPO_Data = pd.read_sql_query(qry,tendotCnxn)

		return OpenPO_Data

	except Exception as e:
		print(Classes.Constants.ERR_PREFIX + "GetAllOpen_PO_Data() -")
		print type(e)
		print(e)

def GetSupplierID(suppliersList, Supplier_Desc):
	try:
		Supplier_Desc = Supplier_Desc.upper()
		supplier_id = 0
		for k, ind in suppliersList.iterrows() :
			if( Supplier_Desc == str(suppliersList["Supplier_Desc"].iloc[k]) ):
				supplier_id = suppliersList["SupplierID"].iloc[k]
				break
			##print(str(suppliersList["SupplierID"].iloc[k]))
			##print(str(suppliersList["Supplier_Desc"].iloc[k]))

		##print("Supplier_Desc: " + str(Supplier_Desc) +  " - Supplier ID: " + str(supplier_id))
		return supplier_id

	except Exception as e:
		print(Classes.Constants.ERR_PREFIX + "GetSupplierID() -")
		print type(e)
		print(e)

def Re_consolidate_quoted_parts(Part_Key, Manufacturer_Name, Manufacturer_Part_No, PCN, Part_No, Supplier_Code, Std_Cost, PO_Price, Quantity,suppliersList):
	try:
		consolidated_DataTable = "CS_Consolidated_Data"

		##Get raw quote data for PN
		##select * from Commodity_Strategy_Quote_Responses_Details_Dev1 where Part_Number = Part_No
		qry_Qdata = "select * from Commodity_Strategy_Quote_Responses_Dev1 where Manufacturer_Name = '" + Manufacturer_Name + "' AND Manufacturer_Part_Number = '" + Manufacturer_Part_No +"'"
		##Part_No = '" + Part_No  + "'"

		Q_Data = pd.read_sql_query(qry_Qdata,cnxn)

		mfg_mpn_not_found_in_quotes_list = []

		if( len(Q_Data) > 0 ):
			##If Q data found...
			for j,ind1 in Q_Data.iterrows() :
				##print(str(ind1))
				Supplier_Quote  = Q_Data["Supplier_Quote"].iloc[j]
				##Part_No = Q_Data["Part_No"].iloc[j]
				Quote_USD = Q_Data["Quote_USD"].iloc[j]

				location  = PCN
				Part_Number = Part_No
				Part_Key = Part_Key
				Mfg_Name = Manufacturer_Name
				MPN = Manufacturer_Part_No
				Supplier_Code = Q_Data["Supplier_Quote"].iloc[j]
				##Std_Cost
				##PO_Price,
				##SupplierID
				SupplierID = int(GetSupplierID(suppliersList, Supplier_Code))
				quote =  Q_Data["Quote_USD"].iloc[j]
				##print("quote: " + str(quote))
				eau = int(Q_Data["EAU"].iloc[j])
				##print("eau: " + str(eau))
				##print("PO_Price: " + str(PO_Price))

				##Quantity =
				##PPV @ EAU
				##print("PPV @ EAU")
				ppv_at_eau = 0
				ppv_at_eau = int((float(quote) - float(PO_Price)) * eau)

				##PPV @ PO
				##print("PPV @ PO")
				open_po_releases = 0
				open_po_releases = int(GetPOsByPN(Part_Number))
				##print("open_po_releases: " + str(open_po_releases))
				ppv_at_po = 0
				ppv_at_po = int((float(quote) - float(PO_Price)) * open_po_releases)
				##ppv_at_eau,
				##ppv_at_po,
				NCNR = Q_Data["NCNR_Y_N"].iloc[j]
				lt = Q_Data["LT_Weeks"].iloc[j]
				coo = Q_Data["COO"].iloc[j]
				_min = Q_Data["_MIN"].iloc[j]
				mult = Q_Data["_MULT"].iloc[j]
				qoh = Q_Data["_QOH"].iloc[j]
				comments = Q_Data["Comments_Notes"].iloc[j]

				if( ObjFunctions.INSERT_RE_CONSOLIDATION_RECORD == 1 ): InsertConsolidatedDataRow(consolidated_DataTable, location, Part_Number, Part_Key, Mfg_Name,MPN, Supplier_Code, Std_Cost, PO_Price, SupplierID, quote, eau, int(Quantity), ppv_at_eau, ppv_at_po, NCNR,int(lt),coo,_min,mult,qoh,comments)
				##print(str(Part_Number) + " inserted !")
		else:
			##print(str(Part_No) + "-" + str(Manufacturer_Name) + "-" + str(Manufacturer_Part_No))
			##print(str(Manufacturer_Name) + " | " + str(Manufacturer_Part_No))
			if( ObjFunctions.DISPLAY_RE_CONSOLIDATED_MFG_MPN_NOT_FOUND_IN_QUOTES == True ):
				print("[" + Manufacturer_Name + " | " + Manufacturer_Part_No + "]")
				##mfg_mpn_not_found_in_quotes_list.append(mfg_mpn_not_found_in_quotes)

	except Exception as e:
		print(Classes.Constants.ERR_PREFIX + "Re_consolidate_quoted_parts() -")
		print type(e)
		print(e)

def Post_Consolidation_Verification(suppliersList):
	try:
		##print(suppliersList)
		print("Get execution master list and re-consolidating")
		##Get execution master list
		qry_partList_data = "SELECT Part_No, Manufacturer_Name, Manufacturer_Part_Number from Commodity_Strategy_Execution_Master Cs where Cs.Part_No NOT IN (select Part_No from CS_Consolidated_Data_Lowest_Quote_Only group by Part_No) GROUP BY Part_No, Manufacturer_Name, Manufacturer_Part_Number"

		partList_data = pd.read_sql_query(qry_partList_data,cnxn)

		##print(Po_Data)

		if( len(partList_data) > 0 ):
			##If PO data found...
			pn_with_no_po_data_found = []
			for i,ind in partList_data.iterrows() :
				##print(str(i))
				Part_No = partList_data["Part_No"].iloc[i]
				##print(str(Part_No))
				##PO Data
				qry_po_data = "SELECT Part_Key, Manufacturer_Name, Manufacturer_Part_No, PCN, Part_No, Supplier_Code, Std_Cost, PO_Price, CAST(Quantity AS float) as 'Quantity' FROM Open_PO_Data1 WHERE Part_No = '" + Part_No + "' GROUP BY Part_Key, Manufacturer_Name, Manufacturer_Part_No, PCN, Part_No, Supplier_Code, Std_Cost, PO_Price, Quantity "

				Po_Data = pd.read_sql_query(qry_po_data,cnxn)

				if( len(Po_Data) > 0 ):
					##If PO data found...
					for j,ind1 in Po_Data.iterrows() :
						Part_No = Po_Data["Part_No"].iloc[j]
						Part_Key = Po_Data["Part_Key"].iloc[j]
						Manufacturer_Name = Po_Data["Manufacturer_Name"].iloc[j]
						Manufacturer_Part_No = Po_Data["Manufacturer_Part_No"].iloc[j]
						PCN = Po_Data["PCN"].iloc[j]
						Supplier_Code = Po_Data["Supplier_Code"].iloc[j]
						Std_Cost = Po_Data["Std_Cost"].iloc[j]
						PO_Price = Po_Data["PO_Price"].iloc[j]
						Quantity = Po_Data["Quantity"].iloc[j]

						Re_consolidate_quoted_parts(Part_Key, Manufacturer_Name, Manufacturer_Part_No, PCN, Part_No, Supplier_Code, Std_Cost, PO_Price, Quantity,suppliersList)

						break
				else:
					pn_with_no_po_data_found.append(str(Part_No))

		if( ObjFunctions.DISPLAY_RE_CONSOLIDATED_PN_WITH_NO_PO == True ):
			if( len(pn_with_no_po_data_found) > 0 ):
				print("PNs with no po data found: " + str(len(pn_with_no_po_data_found)))
				print(pn_with_no_po_data_found)

		print("Done!")

	except Exception as e:
		print(Classes.Constants.ERR_PREFIX + "Post_Consolidation_Verification() -")
		print type(e)
		print(e)

def InsertNotQuoted(Part_Key, Part_Number,Mfg_Name,MPN):
	try:
		dB_table = "CS_Parts_Not_Quoted"
		SQLCommand = ("INSERT INTO " + dB_table + " ([Part_Key],[Part_No],[Manufacturer_Name],[Manufacturer_Part_Number]) VALUES (?,?,?,?);")
		Values = [Part_Key, Part_Number,Mfg_Name,MPN]

		##print(SQLCommand)
		##print(Values)

		cursor.execute(SQLCommand,Values)
		cursor.commit()

		##print("Quote Data Mfg_Name " + str(Mfg_Name) + " MPN " + str(MPN) + " quote " + str(Quote_USD) + " inserted...")

	except Exception as e:
		print(Classes.Constants.ERR_PREFIX + "InsertNotQuoted() -")
		print type(e)
		print(e)

def Part_Not_Quoted_Has_Been_Registered(Mfg_Name, MPN):
	try:
		flg_Found = False
		qry_part_key = "SELECT Part_No, Part_Key FROM CS_Parts_Not_Quoted WHERE Manufacturer_Name = '" + str(Mfg_Name) + "' AND Manufacturer_Part_Number = '" + str(MPN) + "'"

		##Pkey_Data = pd.read_sql_query(qry_part_key,tendotCnxn)
		Pkey_Data = pd.read_sql_query(qry_part_key,cnxn)

		if( len(Pkey_Data) > 0 ):
			flg_Found = True

		return flg_Found

	except Exception as e:
		print(Classes.Constants.ERR_PREFIX + "Get_Part_Number_Part_Key() -")
		print type(e)
		print(e)

##Under dev...
def Get_Part_Number_Part_Key(Mfg_Name, MPN):
	try:

		PKey_PN = []
		qry_part_key = "SELECT Part_No, Part_Key FROM Manufacturer_Part WHERE Manufacturer_Name = '" + str(Mfg_Name) + "' AND Manufacturer_Part_No = '" + str(MPN) + "' GROUP BY Part_No, Part_Key"
		##print(str(qry_part_key))
		##Pkey_Data = pd.read_sql_query(qry_part_key,tendotCnxn)
		Pkey_Data = pd.read_sql_query(qry_part_key,cnxn)

		Part_Key = ""
		Part_Number = ""

		if( len(Pkey_Data) > 0 ):
			for ind in Pkey_Data:
				##location = Pkey_Data["PCN"].iloc[0]
				Part_Key = Pkey_Data["Part_Key"].iloc[0]
				Part_Number = Pkey_Data["Part_No"].iloc[0]

				##print("Part_Key: " + str(Part_Key))
				##print("Part_Number: " + str(Part_Number))

				break

			PKey_PN.append(Part_Key)
			PKey_PN.append(Part_Number)

		return PKey_PN

	except Exception as e:
		print(Classes.Constants.ERR_PREFIX + "Get_Part_Number_Part_Key() -")
		print type(e)
		print(e)

def LoadAndProcessQuote(file,filename, suppliersList, Open_PO_Data):
	try:
		if( ObjAppSettings.App_Settings_Deploy_Mode_Id == ObjAppSettings.DEPLOY_MODE_DEV ):
			dB_table = ObjAppSettings.CS_QUOTE_ANALYZER_QUOTE_RESPONSES_TBL_DEV
		else:
			dB_table = ObjAppSettings.CS_QUOTE_ANALYZER_QUOTE_RESPONSES_TBL



		consolidated_DataTable = "CS_Consolidated_Data"
		insertRecords = ObjFunctions.CS_CONSOLIDATED_INSERT_RECORDS

		if( insertRecords == 0 ):
			x = raw_input("Insert records flag is OFF!")

		print(str(file))
		wb = xlrd.open_workbook(file)
		sheet = wb.sheet_by_index(0)
		num_rows = sheet.nrows-1
		curr_row = 1

		filename = filename.upper()
		##print("To upper... " + filename)
		if( filename.find("FUTURE") != -1 ):
			quote_supplier = "FUTURE"
		if( filename.find("AVNET") != -1 ):
			quote_supplier = "AVNET"
		if( filename.find("ARROW") != -1 ):
			quote_supplier = "ARROW"
		if( filename.find("TTI") != -1 ):
			quote_supplier = "TTI"
		if( filename.find("RUTRONIK") != -1 ):
			quote_supplier = "RUTRONIK"

		SupplierID = 0
		SupplierID = RegisterQuoteFile(quote_supplier, filename, suppliersList)

		##Clean db for this quote_supplier and SupplierID
		if( ObjFunctions.LOAD_ORIGINAL_QUOTE_CLEAN_START_PER_SUPPLIER == 1 ): Load_Original_Quote_Clean_Start(quote_supplier,SupplierID)

		consolidated_data_records = 0
		quote_data_records = 0
		discrepancyCount = 0

		retrieved_pns = 0
		proccessed_pns = 0
		no_po_data_found_for_pn_counter = 0
		no_po_data_found_for_pn = []
		complexPN_found = False

		DISPLAY_QUOTE_DATA = ObjFunctions.DISPLAY_QUOTE_DATA
		DISPLAY_PO_DATA = ObjFunctions.DISPLAY_PO_DATA
		DISPLAY_PO_DATA_NOT_FOUND_FOR_MFG_MPN = ObjFunctions.DISPLAY_PO_DATA_NOT_FOUND_FOR_MFG_MPN

		with ShadyBar('Processing file...', max = num_rows) as bar:
			while curr_row < num_rows:
				##sheet.cell_value(curr_row, Classes.Constants.Common_SmelterList_SmelterIdentificationNumberInput_Col)
				##Init
				Mfg_Name = ""
				MPN = ""
				description = ""
				eau = ""
				target = ""

				mfgquoted = ""
				MPNQuoted = ""
				quote = 0
				NCNR = ""
				lt = 0
				coo = ""
				_min = 0
				mult = 0
				qoh = 0
				comments = 0
				fstSavings = 0
				monthlySavings = 0

				##Retrieve
				Mfg_Name = sheet.cell_value(curr_row, ObjConstants.NCOL_A)
				MPN = sheet.cell_value(curr_row, ObjConstants.NCOL_B)
				##print("\nMPN: " + str(MPN))
				description = sheet.cell_value(curr_row, ObjConstants.NCOL_C)
				eau = int(sheet.cell_value(curr_row, ObjConstants.NCOL_D))
				target = sheet.cell_value(curr_row, ObjConstants.NCOL_E)

				mfgquoted = sheet.cell_value(curr_row, ObjConstants.NCOL_F)
				quote = sheet.cell_value(curr_row, ObjConstants.NCOL_H)
				##print("Quote: " + str(quote))
				##Only take into account the quoted mfg name and mpn
				##if( mfgquoted != "" ):
				if( quote != "" ):
					if( quote > 0 ):
						if( ( str(MPN) == str(MPNQuoted) ) == False ):
							markAsDiscrepancy = 1
							discrepancyCount +=1

						NCNR = sheet.cell_value(curr_row, ObjConstants.NCOL_I)
						lt = sheet.cell_value(curr_row, ObjConstants.NCOL_J)
						coo = sheet.cell_value(curr_row, ObjConstants.NCOL_K)
						_min = sheet.cell_value(curr_row, ObjConstants.NCOL_L)
						mult = sheet.cell_value(curr_row, ObjConstants.NCOL_M)
						qoh = sheet.cell_value(curr_row, ObjConstants.NCOL_N)
						comments = sheet.cell_value(curr_row, ObjConstants.NCOL_O)
						fstSavings = 0##sheet.cell_value(curr_row, ObjConstants.NCOL_P)
						monthlySavings = 0##sheet.cell_value(curr_row, ObjConstants.NCOL_Q)

						retrieved_pns += 1

						##print("Mfg_Name: " + str(Mfg_Name))
						##print("MPN: " + str(MPN))
						##Display
						if( DISPLAY_QUOTE_DATA == 1 ):
							print("\n")
							print("\nR: " + str(curr_row))
							print("Mfg_Name: " + str(Mfg_Name))
							print("MPN: " + str(MPN))
							print("description: " + str(description))
							print("eau: " + str(eau))
							print("target: " + str(target))

							print("mfgquoted: " + str(mfgquoted))
							print("MPNQuoted: " + str(MPNQuoted))

							print("quote: " + str(quote))
							print("NCNR: " + str(NCNR))
							print("lt: " + str(lt))
							print("coo: " + str(coo))
							print("_min: " + str(_min))

							print("mult: " + str(mult))
							print("qoh: " + str(qoh))

							print("comments: " + str(comments))
							print("fstSavings: " + str(fstSavings))
							print("monthlySavings: " + str(monthlySavings))

						##print("***********************")
						##Get PO Data
						##print("R: " + str(curr_row))

						##print("\nMfg_Name: " + str(Mfg_Name))
						##print("MPN: " + str(MPN))

						Part_Key = ""
						Part_Number = ""
						qry_part_key = "SELECT PCN, Part_No, Part_Key FROM Manufacturer_Part WHERE Manufacturer_Name = '" + str(Mfg_Name) + "' AND Manufacturer_Part_No = '" + str(MPN) + "'"

						##Pkey_Data = pd.read_sql_query(qry_part_key,tendotCnxn)
						Pkey_Data = pd.read_sql_query(qry_part_key,cnxn)

						if( len(Pkey_Data) > 0 ):
							for ind in Pkey_Data:
								##location = Pkey_Data["PCN"].iloc[0]
								Part_Key = Pkey_Data["Part_Key"].iloc[0]
								Part_Number = Pkey_Data["Part_No"].iloc[0]

							##if( Part_Key != "" ): print("*** Part_Key: " + str(Part_Key))

							##qry_po_data = "SELECT Part_Key, PCN, Part_No, Supplier_Code, Std_Cost, PO_Price, CAST(Quantity AS float) as 'Quantity' FROM Open_PO_Data WHERE Manufacturer_Name = '" + str(Mfg_Name) + "' AND Manufacturer_Part_No = '" + str(MPN) + "'"
							##qry_po_data = "SELECT Part_Key, PCN, Part_No, Supplier_Code, Std_Cost, PO_Price, CAST(Quantity AS float) as 'Quantity' FROM Open_PO_Data WHERE Part_Key = '" + str(Part_Key) + "'"

							qry_part_key_list = "SELECT Part_Key FROM Manufacturer_Part WHERE Manufacturer_Name = '" + str(Mfg_Name) + "' AND Manufacturer_Part_No = '" + str(MPN) + "'"
							qry_po_data = "SELECT Part_Key, PCN, Part_No, Supplier_Code, Std_Cost, PO_Price, CAST(Quantity AS float) 'Qty' FROM Open_PO_Data1 WHERE Part_Key in (" + str(qry_part_key_list) + ")"

							##print(str(qry_po_data))

							##Po_Data = pd.read_sql_query(qry_po_data,tendotCnxn)
							Po_Data = pd.read_sql_query(qry_po_data,cnxn)

							if( len(Po_Data) > 0 ):
								##If PO data found...
								for ind in Po_Data:
									##Part_Key = Po_Data["Part_Key"].iloc[0]
									location = Po_Data["PCN"].iloc[0]
									##Part_Number = Po_Data["Part_No"].iloc[0]


									"""
									print("*** PCN: " + str(location))
									print("*** Part_No: " + str(Part_Number))

									print("Mfg_Name: " + str(Mfg_Name))
									print("MPN: " + str(MPN))
									"""

									Supplier_Code = Po_Data["Supplier_Code"].iloc[0]
									Std_Cost = Po_Data["Std_Cost"].iloc[0]
									PO_Price = Po_Data["PO_Price"].iloc[0]
									Quantity = int(Po_Data["Qty"].iloc[0])

									"""
									print("Supplier_Code: " + str(Supplier_Code))
									print("Std_Cost: " + str(Std_Cost))
									print("PO_Price: " + str(PO_Price))
									print("Quantity: " + str(Quantity))
									"""



								##Calcultions
								##PPV @ EAU
								##print("PPV @ EAU")
								ppv_at_eau = 0
								ppv_at_eau = int((float(quote) - float(PO_Price)) * eau)


								##PPV @ PO
								##print("PPV @ PO")
								open_po_releases = 0
								open_po_releases = int(GetPOsByPN(Part_Number))
								##print("open_po_releases: " + str(open_po_releases))
								ppv_at_po = 0
								ppv_at_po = int((float(quote) - float(PO_Price)) * open_po_releases)

								##x = raw_input("press any key to continue...")

								##Display
								if( DISPLAY_PO_DATA == 1 ):
									print("#########################")
									print("Part_Key: " + str(Part_Key))
									print("PCN: " + str(location))
									print("Part_No: " + str(Part_Number))
									print("Mfg_Name: " + str(Mfg_Name))
									print("MPN: " + str(MPN))
									print("Supplier_Code: " + str(Supplier_Code))
									print("Std_Cost: " + str(Std_Cost))
									print("PO_Price: " + str(PO_Price))
									print("Quantity: " + str(Quantity))
									print("PPV_at_EAU: " + str(ppv_at_eau))
									print("PPV_at_PO: " + str(ppv_at_po))
									print("#########################")

								##Register
								##Consolidated data
								if( insertRecords == 1 ): InsertConsolidatedDataRow(consolidated_DataTable, location, Part_Number, Part_Key, Mfg_Name,MPN, Supplier_Code, Std_Cost, PO_Price, SupplierID, quote, eau, str(Quantity), ppv_at_eau, ppv_at_po, NCNR,lt,coo,_min,mult,qoh,comments)
								consolidated_data_records += 1

								if( Part_Number == '35-11396' ): complexPN_found = True## print("Part 35-11396 aggregated!")

								quote_data_records += 1



							else:
								##print("\nmfg name: " + str(Mfg_Name) + "|mpn: " + str(MPN))
								mpn_not_found =  str(Mfg_Name) + "|" + str(MPN)
								no_po_data_found_for_pn.append(mpn_not_found)

							##Insert quote response
							if( insertRecords == 1 ): InsertQuoteRow(dB_table,quote_supplier, Part_Number,Mfg_Name,MPN,description,str( int(eau) ),target,mfgquoted,MPNQuoted,quote,NCNR,lt,coo,_min,mult,qoh,comments,fstSavings,monthlySavings,markAsDiscrepancy,filename)
							markAsDiscrepancy = 0

							##if( (len(Po_Data) > 0)  & ( Po_Data["Part_Key"].iloc[0] > 0) ):
							##print("***********************")

				else:
					if( ObjFunctions.LOAD_PARTS_WITH_NO_QUOTES == 1 ):
						#Part not quoted already recorded?
						flg_Found = Part_Not_Quoted_Has_Been_Registered(Mfg_Name, MPN)
						##print("\nPart quoted: " + str(flg_Found))
						PKey_PN = []
						Part_Key = ""
						Part_Number = ""
						if( flg_Found == False ) :
							##PKey_PN = Get_Part_Number_Part_Key(Mfg_Name, MPN)
							##print(PKey_PN)
							##Part_Key = PKey_PN[0]
							##Part_Number = PKey_PN[1]
							##print(str(Part_Key))
							##print(str(Part_Number))

							qry_part_key = "SELECT Part_No, Part_Key FROM Manufacturer_Part WHERE Manufacturer_Name = '" + str(Mfg_Name) + "' AND Manufacturer_Part_No = '" + str(MPN) + "' GROUP BY Part_No, Part_Key"
							##print(str(qry_part_key))
							##Pkey_Data = pd.read_sql_query(qry_part_key,tendotCnxn)
							Pkey_Data = pd.read_sql_query(qry_part_key,cnxn)

							if( len(Pkey_Data) > 0 ):
								for ind in Pkey_Data:
									Part_Key = Pkey_Data["Part_Key"].iloc[0]
									Part_Number = Pkey_Data["Part_No"].iloc[0]

									##print("Part_Key: " + str(Part_Key))
									##print("Part_Number: " + str(Part_Number))

									break

							InsertNotQuoted(Part_Key, Part_Number,Mfg_Name,MPN)
							##print("Part not quoted has not been recorded, recording it...")

				curr_row += 1
				bar.next()
			bar.finish()

			print("************** QUOTE LOAD SUMMARY ****************************")
			print("Rows in file: " + str(num_rows))
			print("Quoted pns retrieved: " + str(retrieved_pns))
			print("PNs inserted: " + str(quote_data_records))
			print("PNs NOT inserted: " + str( int(retrieved_pns) - int(quote_data_records) ))
			##if( complexPN_found == True ): print("Part 35-11396 aggregated!")

			if( DISPLAY_PO_DATA_NOT_FOUND_FOR_MFG_MPN == 1 ):
				print("No PO data found for this MPN(s): ")
				for mpn in no_po_data_found_for_pn:
					print(str(mpn))

			##Clean the not found parts
			##no_po_data_found_for_pn.clear()
			print("**************************************************************")
			##print("No PO data found for these P/Ns: \n")
			##print(no_po_data_found_for_pn)
			##consolidated_data_records
	except Exception as e:
		##if( type(e) == 'exceptions.IndexError' ):

		##print("Field " + _field + " on row: " + str(curr_row))
		print(Classes.Constants.ERR_PREFIX + "LoadAndProcessQuote() - R" + str(curr_row) + " - ")
		print type(e)
		print(e)


def RegisterQuoteFile(supplier, filename, suppliersList):
	try:
		dB_table = "CS_Quote_Response_Files"
		##print(suppliersList)

		##print("Supplier: " + str(supplier))
		for index, row in suppliersList.iterrows():
			if( row['Supplier_Desc'] == supplier):
				supplier_id = row['SupplierID']
				##print("supplier_id = " + str(supplier_id))
				break

		SQLCommand = ("INSERT INTO " + dB_table + " ([SupplierID],[File_Name]) VALUES (?,?);")
		Values = [str(supplier_id),str(filename)]

		##print(SQLCommand)
		##print(Values)

		cursor.execute(SQLCommand,Values)
		cursor.commit()

		return supplier_id
	except Exception as e:
			print(Classes.Constants.ERR_PREFIX + "RegisterQuoteFile() -")
			print type(e)
			print(e)

def SanitizeQuoteResponsesParsed():
	try:

		SQLCommand = "UPDATE Commodity_Strategy_Quote_Responses_Dev1 SET "
		SQLCommand = SQLCommand + " Manufacturer_Name = Replace(Manufacturer_Name, '''', '') "
		SQLCommand = SQLCommand + " ,Manufacturer_Part_Number = Replace(Manufacturer_Part_Number, '''', '') "
		SQLCommand = SQLCommand + " ,_Description = Replace(_Description, '''', '') "
		SQLCommand = SQLCommand + " ,MFG_QUOTED = Replace(MFG_QUOTED, '''', '') "
		SQLCommand = SQLCommand + " ,MPN_QUOTED = Replace(MPN_QUOTED, '''', '') "
		SQLCommand = SQLCommand + " ,Quote_USD = Replace(Quote_USD, '''', '') "
		SQLCommand = SQLCommand + " ,COO = Replace(COO, '''', '') "
		SQLCommand = SQLCommand + " ,Comments_Notes = Replace(Comments_Notes, '''', '') "
		SQLCommand = SQLCommand + " ,File_Name = Replace(File_Name, '''', '')"

		##print(SQLCommand)
		##print(Values)

		cursor.execute(SQLCommand)
		cursor.commit()

		time.sleep(0.5) ##Delay for half a second

		SQLCommand = "UPDATE CS_Consolidated_Data SET "
		SQLCommand = SQLCommand + " Manufacturer_Name = Replace(Manufacturer_Name, '''', '') "
		SQLCommand = SQLCommand + " ,Manufacturer_Part_Number = Replace(Manufacturer_Part_Number, '''', '') "

		print("Records sanitized...")

	except Exception as e:
		print(Classes.Constants.ERR_PREFIX + "SanitizeQuoteResponsesParsed() -")
		print type(e)
		print(e)

def FindInConsolidated_And_InsertInLowestQ_IfFound(Part_Number):
	DISPLAY_INSERT = ObjFunctions.LOWST_QTE_DISPLAY_INSERT
	DISPLAY_NOT_INSERTED = ObjFunctions.LOWST_QTE_DISPLAY_NOT_INSERTED
	dB_table = "CS_Consolidated_Data_Lowest_Quote_Only"
	part_inserted = 0

	try:
		SQLCommand = " SELECT DISTINCT TOP 1 "
		SQLCommand = SQLCommand + " Cs.PCN, Cs.Part_Key, Cs.Part_No, Cs.Manufacturer_Name, Cs.Manufacturer_Part_Number, Cs.Supplier_Code, Cs.Std_Cost, Cs.PO_Price, Cs.Quote_Supplier "
		SQLCommand = SQLCommand + " , Cs.Quote_Price, Cs.EAU_Quantity, Cs.Demand_Quantity, Cs.PPV_at_EAU, Cs.PPV_at_Primary_PO "
		SQLCommand = SQLCommand + " FROM CS_Consolidated_Data Cs "
		SQLCommand = SQLCommand + " WHERE Cs.Part_No = '" + Part_Number + "' "
		SQLCommand = SQLCommand + " GROUP BY "
		SQLCommand = SQLCommand + " Cs.PCN, Cs.Part_Key, Cs.Part_No, Cs.Manufacturer_Name, Cs.Manufacturer_Part_Number, Cs.Supplier_Code, Cs.Std_Cost, Cs.PO_Price, Cs.Quote_Supplier "
		SQLCommand = SQLCommand + " , Cs.Quote_Price, Cs.EAU_Quantity, Cs.Demand_Quantity, Cs.PPV_at_EAU, Cs.PPV_at_Primary_PO "
		SQLCommand = SQLCommand + " ORDER BY Quote_Price ASC "

		##print(str(SQLCommand))

		Pn_List = pd.read_sql_query(SQLCommand,cnxn)
		df = Pn_List

		r_count = 0
		if(len(Pn_List) > 0 ):
			##print(Pn_List)
			for ind, row in df.iterrows():
				PCN = row["PCN"]
				Part_Key = row["Part_Key"]
				Part_No  = row["Part_No"]
				Manufacturer_Name  = row["Manufacturer_Name"]
				Manufacturer_Part_Number  = row["Manufacturer_Part_Number"]
				Supplier_Code = row["Supplier_Code"]
				Std_Cost = row["Std_Cost"]
				PO_Price  = row["PO_Price"]
				Quote_Supplier  = row["Quote_Supplier"]
				Quote_Price  = row["Quote_Price"]
				EAU_Quantity  = row["EAU_Quantity"]
				Demand_Quantity  = row["Demand_Quantity"]
				PPV_at_EAU = row["PPV_at_EAU"]
				PPV_at_Primary_PO = row["PPV_at_Primary_PO"]


				SQLCommand = ("INSERT INTO " + dB_table + " (PCN, Part_Key, Part_No, Manufacturer_Name, Manufacturer_Part_Number, Supplier_Code, Std_Cost, PO_Price, Quote_Supplier, Quote_Price, EAU_Quantity, Demand_Quantity, PPV_at_EAU, PPV_at_Primary_PO) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);")
				Values = [PCN, Part_Key, Part_No, Manufacturer_Name, Manufacturer_Part_Number, Supplier_Code, Std_Cost, PO_Price, Quote_Supplier,Quote_Price, EAU_Quantity, Demand_Quantity, PPV_at_EAU, PPV_at_Primary_PO]

				##print(SQLCommand)
				##print(Values)

				cursor.execute(SQLCommand,Values)
				cursor.commit()

				part_inserted += 1

				if( DISPLAY_INSERT == True ): print("Part No " + Part_Number + " inserted in lowest Q !")

				break

		if( DISPLAY_NOT_INSERTED == True ):
			if( part_inserted == 0 ):
				print("PN not inserted: " + str(Part_Number))

		return part_inserted

	except Exception as e:
		print(Classes.Constants.ERR_PREFIX + "FindInConsolidated_And_InsertInLowestQ_IfFound() - ")
		print type(e)
		print(e)

def Get_Lowest_Quote_Price_By_PN():
	try:
		CS_Consolidated_Data_Lowest_Quote_Table = "CS_Consolidated_Data_Lowest_Quote_Only"
		qry = "TRUNCATE TABLE CS_Consolidated_Data_Lowest_Quote_Only"
		cursor.execute(qry)
		cursor.commit()

		print("Loading lowest quoted price by PN...")
		##GetPN list
		qry = "select distinct Cs.Part_No from Commodity_Strategy_Execution_Master Cs group by Cs.Part_No"
		Pn_List = pd.read_sql_query(qry,cnxn)
		df = Pn_List

		r_count = 0
		if(len(Pn_List) > 0 ):
			##print(Pn_List)
			for ind, row in df.iterrows():
				part_inserted = 0
				Part_Number = row["Part_No"]##.iloc[0]

				part_inserted = FindInConsolidated_And_InsertInLowestQ_IfFound(Part_Number)

				if( part_inserted == 1 ): r_count += 1

				"""
				SQLCommand = "INSERT INTO " + CS_Consolidated_Data_Lowest_Quote_Table + " "
				SQLCommand = SQLCommand + " (PCN, Part_Key, Part_No, Manufacturer_Name, Manufacturer_Part_Number, Supplier_Code, Std_Cost, PO_Price, Quote_Supplier "
				SQLCommand = SQLCommand + " , Quote_Price, EAU_Quantity, Demand_Quantity, PPV_at_EAU, PPV_at_Primary_PO) "
				SQLCommand = SQLCommand + " SELECT DISTINCT TOP 1 "
				SQLCommand = SQLCommand + " Cs.PCN, Cs.Part_Key, Cs.Part_No, Cs.Manufacturer_Name, Cs.Manufacturer_Part_Number, Cs.Supplier_Code, Cs.Std_Cost, Cs.PO_Price, Cs.Quote_Supplier "
				SQLCommand = SQLCommand + " , Cs.Quote_Price, Cs.EAU_Quantity, Cs.Demand_Quantity, Cs.PPV_at_EAU, Cs.PPV_at_Primary_PO "
				SQLCommand = SQLCommand + " FROM CS_Consolidated_Data Cs "
				SQLCommand = SQLCommand + " WHERE Cs.Part_No = '" + Part_Number + "' "
				SQLCommand = SQLCommand + " GROUP BY "
				SQLCommand = SQLCommand + " Cs.PCN, Cs.Part_Key, Cs.Part_No, Cs.Manufacturer_Name, Cs.Manufacturer_Part_Number, Cs.Supplier_Code, Cs.Std_Cost, Cs.PO_Price, Cs.Quote_Supplier "
				SQLCommand = SQLCommand + " , Cs.Quote_Price, Cs.EAU_Quantity, Cs.Demand_Quantity, Cs.PPV_at_EAU, Cs.PPV_at_Primary_PO "
				SQLCommand = SQLCommand + " ORDER BY Quote_Price ASC "

				cursor.execute(SQLCommand)
				cursor.commit()
				"""

				##print("PN " + str(Part_Number) + " inserted...")
				##r_count += 1

		print("\nLoading lowest quoted price by PN... Done! Loaded: " + str(r_count))

	except Exception as e:
		##if( type(e) == 'exceptions.IndexError' ):

		##print("Field " + _field + " on row: " + str(curr_row))
		print(Classes.Constants.ERR_PREFIX + "Get_Lowest_Quote_Price_By_PN() - ")
		print type(e)
		print(e)

def ParseQuotesDirectory(suppliersList):
	try:

		"""
		if( ObjAppSettings.App_Settings_Deploy_Mode_Id == ObjAppSettings.DEPLOY_MODE_DEV ):
			directory = r'C:\dataXtractfiles\Quote_Analyzer\Test\Responses'
		else:
			directory = r'C:\dataXtractfiles\Quote_Analyzer\Responses'
		"""

		Open_PO_Data = GetAllOpen_PO_Data()

		if( ObjFunctions.LOAD_ORIGINAL_QUOTE_CLEAN_START == 1 ):
			quote_supplier = ""
			SupplierID = 0
			Load_Original_Quote_Clean_Start(quote_supplier,SupplierID)

		##print(Open_PO_Data)
		##directory = r'C:\dataXtractfiles\Quote_Analyzer\Received\To_Compare'
		directory = r'C:\dataXtractfiles\Quote_Analyzer\Test\Responses'
		start = time.time()
		for filename in os.listdir(directory):
			print(filename)
			fullpath = directory + os.sep + filename
			ObjConstants.fileName = filename
			LoadAndProcessQuote(fullpath,filename, suppliersList, Open_PO_Data)

		##SanitizeQuoteResponsesParsed()
		##if( ObjFunctions.GET_LOWEST_QUOTE_PRICE_BY_PN == 1): Get_Lowest_Quote_Price_By_PN()

		print("\nBoom, all done!!!")
		end = time.time()
		elapsed_time = end - start
		print("Elapsed time (h): " + "%.2f" % ((elapsed_time/60)/60))
		print("Elapsed time (m): " + "%.2f" % (elapsed_time/60))
		print("Elapsed time (s): " + "%.2f" % elapsed_time)

	except Exception as e:
		print(Classes.Constants.ERR_PREFIX + "CompareQuotes() -")
		print type(e)
		print(e)

##Under dev
def Update_Quoted_Values_W_PO_And_Fut_PPV_Data(flgUpdate_Std_Cost,flgUpdate_PO_Price,flgUpdate_DmandQty,flgUpdate_EAU,flgPCN_Discrepancy,flgSupplierCode_Discrepancy,Cs_ConsolidatedData_Id,Part_Number,po_pn_pcn,po_pn_supplierCode,Std_Cost,PO_Price,Quote_Price,use_price,EAU_Quantity,Demand_Qty):
	try:
		update_qry_set = None
		update_qry = "UPDATE CS_Consolidated_Data_Lowest_Quote_Only SET "
		##flgUpdate_Std_Cost,flgUpdate_PO_Price,flgUpdate_DmandQty
		if( flgUpdate_Std_Cost or flgUpdate_EAU ):
			calculate_actual_ppv = False

			update_qry_set = " Std_Cost = " + str(Std_Cost)

			quote = Quote_Price
			eau = EAU_Quantity

			print(">>quoted price: " + str(quote))
			print(">>eau: " + str(eau))

			##Calcultions
			ppv = (float(quote) - float(Std_Cost))
			print(">>ppv: " + str(ppv))
			##( (quted price - 2021std) * eau) )
			ppv_at_eau = ppv * eau

			##PPV @ PO
			##print("PPV @ PO")
			##open_po_releases = 0
			##open_po_releases = int(GetPOsByPN(Part_Number))
			##print(">>open_po_releases: " + str(open_po_releases))

			ppv_at_po = ppv * Demand_Qty

			#print(": " + str()
			print(">>PPV_at_EAU: " + str(ppv_at_eau))
			print(">>PPV_at_Primary_PO: " + str(ppv_at_po))

			##Annualized PPV
			annaulized_ppv = ((Quote_Price - PO_Price) * EAU_Quantity)
			print(">>annaulized_ppv: " + str(annaulized_ppv))
			##Turnover
			turnonver = (PO_Price * EAU_Quantity)
			print(">>turnonver: " + str(turnonver))


			ppv_use_price_at_eau = 0
			ppv_use_price_at_po = 0
			if( use_price > 0 ):
				calculate_actual_ppv = True
				print(">>use_price: " + str(use_price))

				##PPV use proce common factor
				ppv_use_price = (float(use_price) - float(Std_Cost))

				##PPV @ EAU use price
				ppv_use_price_at_eau = ppv_use_price * eau

				##PPV @ PO use price
				ppv_use_price_at_po = ppv_use_price * Demand_Qty

				print(">>PPV_use_price_at_EAU: " + str(ppv_use_price_at_eau))
				print(">>PPV_use_price_at_Primary_PO: " + str(ppv_use_price_at_po))


			update_qry_set = update_qry_set + ", PPV_at_EAU = " + str(ppv_at_eau)
			update_qry_set = update_qry_set + ", PPV_at_Primary_PO = " + str(ppv_at_po)
			##Annaulized_PPV_2020,Turn_Over_2020,PPV_UsePrice_At_EAU,PPV_UsePrice_At_Primary_PO
			update_qry_set = update_qry_set + ", Annaulized_PPV_2020 = " + str(annaulized_ppv)
			update_qry_set = update_qry_set + ", Turn_Over_2020 = " + str(turnonver)

			if( calculate_actual_ppv ):
				update_qry_set = update_qry_set + ", PPV_UsePrice_At_EAU = " + str(ppv_use_price_at_eau)
				update_qry_set = update_qry_set + ", PPV_UsePrice_At_Primary_PO = " + str(ppv_use_price_at_po)
			else:
				update_qry_set = update_qry_set + ", PPV_UsePrice_At_EAU = null"
				update_qry_set = update_qry_set + ", PPV_UsePrice_At_Primary_PO = null"

		if( flgUpdate_PO_Price ):
			if( update_qry_set == None ):
				update_qry_set = " PO_Price = " + str(PO_Price)
			else:
				update_qry_set = update_qry_set + ", PO_Price = " + str(PO_Price)

		if( flgUpdate_DmandQty ):
			if( update_qry_set == None ):
				update_qry_set = " Demand_Quantity = " + str(Demand_Qty)
			else:
				update_qry_set = update_qry_set + ", Demand_Quantity = " + str(Demand_Qty)

		if( flgUpdate_EAU ):
			if( update_qry_set == None ):
				update_qry_set = " EAU_Quantity = " + str(Demand_Qty)
			else:
				update_qry_set = update_qry_set + ", EAU_Quantity = " + str(eau)

		if( flgPCN_Discrepancy ):
			if( update_qry_set == None ):
				update_qry_set = " PCN = '" + str(po_pn_pcn) + "'"
			else:
				update_qry_set = update_qry_set + ", PCN = '" + str(po_pn_pcn) + "'"


		if( flgSupplierCode_Discrepancy ):
			if( update_qry_set == None ):
				update_qry_set = " Supplier_Code = '" + str(po_pn_supplierCode) + "'"
			else:
				update_qry_set = update_qry_set + ", Supplier_Code = '" + str(po_pn_supplierCode) + "'"



		##,Part_Number,Std_Cost,PO_Price,Demand_Qty
		update_qry_condition = " WHERE Cs_ConsolidatedData_Id = " + str(Cs_ConsolidatedData_Id)

		SQLCommand = update_qry + update_qry_set + update_qry_condition

		print(str(SQLCommand))

		if ( ObjFunctions.UPDATE_STD_COST_TO_NEW_FUTURE_PPV == 1):
			cursor.execute(SQLCommand)
			cursor.commit()


	except Exception as e:
		##if( type(e) == 'exceptions.IndexError' ):

		##print("Field " + _field + " on row: " + str(curr_row))
		print(Classes.Constants.ERR_PREFIX + "Update_Quoted_Values_W_PO_And_Fut_PPV_Data() - ")
		print type(e)
		print(e)

def Get_Curr_StdCost_or_PO_Price(part_no, field, pcn):
	try:
		value = 0
		if( field == "StdCost" ):
			##qry = "select distinct part_no, MaterialCost as 'StdCost'  from CS_New_Future_PPV where Part_No = '"+ part_no +"' group by part_no, MaterialCost "
			qry = "select [Cost] as StdCost from Part_Cost_Model where PCN = '"+ pcn +"' AND Part_no = '" + part_no + "'"

		if( field == "PO_Price" ):
			qry = "select distinct Po.PO_Price from Open_PO_Data1 Po where Part_No = '"+ part_no +"' AND Blanket_Order = 1 group by Po.PO_Price "
			##print(str(qry))
		if( field == "PO Demand QTY" ):
			qry = "select COALESCE( SUM(CONVERT(float, [Quantity], 101)), 0) as 'PO_Demand_QTY' from Open_PO_Data1 where Part_No = '"+ part_no +"' AND Blanket_Order = 1 "
			##print(str(qry))
		if( field == "EAU" ):
			##select distinct COALESCE([EAU_Quantity], 0) as 'PO_Demand_QTY' from Open_PO_Data1 where Part_No = @PN AND Blanket_Order = 1 group by EAU_Quantity
			qry = "select distinct COALESCE([EAU_Quantity], 0) as 'EAU_Quantity' from Open_PO_Data1 where Part_No = '"+ part_no +"' AND Blanket_Order = 1 group by EAU_Quantity "
		if( field == "USE PRICE" ):
			##select * from Part_Cost_Model where PCN = '278344' AND Part_No = @PN
			qry = "select distinct Part_No, isnull([Use_Price],0) as 'Use_Price' from CS_Consolidated_Data_Lowest_Quote_Only where Part_No = '"+ part_no +"' group by Part_No, Use_Price "
		##PO_PN_PCN
		if( (field == "PO_PN_PCN") or (field == "PO_PN_SUPPLIER_CODE") ):
			##qry = "select distinct PCN, Part_No,Supplier_Code from Open_PO_Data1 where Part_No = '"+ part_no +"' AND Blanket_Order = 1  group by PCN, Part_No,Supplier_Code"
			qry = "select distinct PCN, Part_No,Supplier_Code from Open_PO_Data1 where Part_No = '"+ part_no +"' AND Blanket_Order = 1  group by PCN, Part_No,Supplier_Code"

		Pn_List = pd.read_sql_query(qry,cnxn)
		df = Pn_List

		r_count = 0
		if(len(Pn_List) > 0 ):
			##print(Pn_List)
			for ind, row in df.iterrows():
				##Yet again the comparison
				if( field == "StdCost" ):  value = row["StdCost"]
				if( field == "PO_Price" ):  value = row["PO_Price"]
				if( field == "PO Demand QTY" ):  value = row["PO_Demand_QTY"]
				if( field == "EAU" ):  value = row["EAU_Quantity"]
				if( field == "USE PRICE" ):  value = row["Use_Price"]
				if( field == "PO_PN_PCN" ):  value = row["PCN"]
				if( field == "PO_PN_SUPPLIER_CODE" ):  value = row["Supplier_Code"]

				break

		if( ObjFunctions.DEBUG_ON_PN == 1 and part_no == ObjFunctions.DEBUG_ON_PN_PN ):
			print("field: " + field)
			print("PN: " + str(part_no) )
			print("value: " + str(value))
			strcontinue = input("Press any key to continue...")

		return value

	except Exception as e:
		##if( type(e) == 'exceptions.IndexError' ):

		##print("Field " + _field + " on row: " + str(curr_row))
		print(Classes.Constants.ERR_PREFIX + "Get_Curr_StdCost_or_PO_Price() - ")
		print type(e)
		print(e)

##Create an audit routine to check the updates.

##Under dev
def Get_StdCost_To_Future_PPV():
	try:
		print("StdCost from Future PPV by PN...")
		##GetPN list
		qry = "select * from CS_Consolidated_Data_Lowest_Quote_Only Cs"
		Pn_List = pd.read_sql_query(qry,cnxn)
		df = Pn_List

		r_count = 1
		if(len(Pn_List) > 0 ):
			##print(Pn_List)
			for ind, row in df.iterrows():
				flgUpdate_Std_Cost = False
				flgUpdate_PO_Price = False
				flgUpdate_DmandQty = False
				flgUpdate_EAU = False
				flgPCN_Discrepancy = False
				flgSupplierCode_Discrepancy = False

				Cs_ConsolidatedData_Id = row["Cs_ConsolidatedData_Id"]
				Part_Number = row["Part_No"]
				Curr_Std_Cost = float(row["Std_Cost"])
				Curr_PO_Price = float(row["PO_Price"])
				EAU_Quantity = int(row["EAU_Quantity"])
				Curr_Demand_Qty = int(row["Demand_Quantity"])
				Quote_Price = float(row["Quote_Price"])
				pcn = row["PCN"]

				supplier_code = row["Supplier_Code"]

				Curr_EAU_Quantity = EAU_Quantity

				##Get std/po and quantities
				_2021_StdCost = float(Get_Curr_StdCost_or_PO_Price(Part_Number, "StdCost",pcn))
				Blanket_PO_Price = float(Get_Curr_StdCost_or_PO_Price(Part_Number, "PO_Price",''))
				Added_Up_Demand_Qty = int(Get_Curr_StdCost_or_PO_Price(Part_Number, "PO Demand QTY",''))
				PO_EAU_Quantity = int(Get_Curr_StdCost_or_PO_Price(Part_Number, "EAU",''))
				use_price = float(Get_Curr_StdCost_or_PO_Price(Part_Number, "USE PRICE",''))

				po_pn_pcn = Get_Curr_StdCost_or_PO_Price(Part_Number, "PO_PN_PCN",'')
				po_pn_supplierCode = Get_Curr_StdCost_or_PO_Price(Part_Number, "PO_PN_SUPPLIER_CODE",'')

				print("/////////////////////////")
				print("r_count: " + str(r_count))
				print("pcn: " + str(pcn))
				print("PO pcn: " + str(po_pn_pcn))
				if( (po_pn_pcn != 0) and (pcn != po_pn_pcn) ):
					flgPCN_Discrepancy = True
					print("*** PCN DISCREPNACY *** ")

				print("PN: " + str(Part_Number))

				print("po_pn_supplierCode: " + str(po_pn_supplierCode))
				print("supplier code: " + str(supplier_code))
				##supplier_code
				if( (po_pn_supplierCode != 0) and (supplier_code.upper() != po_pn_supplierCode.upper()) ):
					po_pn_supplierCode = po_pn_supplierCode.upper()
					flgSupplierCode_Discrepancy = True
					print("$$$ SUPPLIER CODE DISCREPNACY $$$ ")

				print("Curr Std Cost: " +  str(Curr_Std_Cost))
				print("2021_StdCost: " +  str(_2021_StdCost))

				if( _2021_StdCost > 0):
					if ( (_2021_StdCost < Curr_Std_Cost) or (_2021_StdCost > Curr_Std_Cost) ):
						flgUpdate_Std_Cost = True
						print(" *** take the 2021 std cost ***")

				print("Curr PO Price: "  + str(Curr_PO_Price))
				print("Blanket PO Price: "  + str(Blanket_PO_Price))

				if( Blanket_PO_Price > 0):
					if ( (Blanket_PO_Price < Curr_PO_Price) or (Blanket_PO_Price > Curr_PO_Price) ):
						flgUpdate_PO_Price = True
						print(" *** take the blanket PO price ***")

				print("Dmnd Qty: " + str(Curr_Demand_Qty))
				print("Added Up Demmand Qty: " + str(Added_Up_Demand_Qty))

				if( Added_Up_Demand_Qty > 0):
					if ( (Added_Up_Demand_Qty < Curr_Demand_Qty) or (Added_Up_Demand_Qty > Curr_Demand_Qty) ):
						flgUpdate_DmandQty = True
						print(" *** take the added up demand qty ***")

				print("Curr_EAU_Quantity: " +  str(Curr_EAU_Quantity))
				print("PO_EAU_Quantity: " +  str(PO_EAU_Quantity))
				if( PO_EAU_Quantity > 0 ):
					if( Curr_EAU_Quantity != PO_EAU_Quantity ):
						flgUpdate_EAU = True
						EAU_Quantity = PO_EAU_Quantity
						print(" *** take PO EAU Qty ***")

				if( ObjFunctions.OVERRIDE_FLAG_UPDATE_CS_LOWEST_QUOTES_TABLE ==1 ):
					flgUpdate_Std_Cost = True

				if ( flgUpdate_Std_Cost or flgUpdate_PO_Price or flgUpdate_DmandQty or flgUpdate_EAU ):
					Update_Quoted_Values_W_PO_And_Fut_PPV_Data(flgUpdate_Std_Cost,flgUpdate_PO_Price,flgUpdate_DmandQty,flgUpdate_EAU,flgPCN_Discrepancy,flgSupplierCode_Discrepancy,Cs_ConsolidatedData_Id,Part_Number,po_pn_pcn,po_pn_supplierCode,_2021_StdCost,Blanket_PO_Price,Quote_Price,use_price,EAU_Quantity,Added_Up_Demand_Qty)

				print("-------")

				r_count += 1

	except Exception as e:
		##if( type(e) == 'exceptions.IndexError' ):

		##print("Field " + _field + " on row: " + str(curr_row))
		print(Classes.Constants.ERR_PREFIX + "Get_StdCost_To_Future_PPV() - ")
		print type(e)
		print(e)

def InsertIntoCS_New_Future_PPV(dB_table, Part_No,Po_No,POSupplier,Qty,PO_Price,Release_No,DueDate,MaterialCost,Ext,PPV,Location):
	try:

		SQLCommand = ("INSERT INTO " + dB_table + " (Part_No,Po_No,POSupplier,Qty,PO_Price,Release_No,DueDate,MaterialCost,Ext,PPV,Location) VALUES (?,?,?,?,?,?,?,?,?,?,?);")
		Values = [Part_No,Po_No,POSupplier,Qty,PO_Price,Release_No,DueDate,MaterialCost,Ext,PPV,Location]

		##print(SQLCommand)
		##print(Values)

		cursor.execute(SQLCommand,Values)
		cursor.commit()

	except Exception as e:
		print(Classes.Constants.ERR_PREFIX + "InsertIntoCS_New_Future_PPV() -")
		print(e)

def Parse_New_Future_PPV():
	try:
		dB_table = Classes.DBConnectionString.CS_NEW_FUTURE_PPV_TBL
		print("Update std cost from new_future_ppv")
		##fileName = r'new_future_ppv.csv'
		file = r'C:\dataXtractfiles\Quote_Analyzer\plex_data\new_future_ppv.xlsx'

		print(str(file))

		wb = xlrd.open_workbook(file)
		sheet = wb.sheet_by_index(0)
		num_rows = sheet.nrows-1
		curr_row = 1

		##Prepare table
		qry = "TRUNCATE TABLE " + dB_table
		cursor.execute(qry)
		cursor.commit()

		with ShadyBar('Processing file...', max = num_rows) as bar:
			while curr_row < num_rows:
				Part_No = sheet.cell_value(curr_row, ObjConstants.NCOL_A)
				Po_No = sheet.cell_value(curr_row, ObjConstants.NCOL_B)
				POSupplier = sheet.cell_value(curr_row, ObjConstants.NCOL_C)
				Qty = sheet.cell_value(curr_row, ObjConstants.NCOL_D)
				PO_Price = sheet.cell_value(curr_row, ObjConstants.NCOL_E)
				Release_No = sheet.cell_value(curr_row, ObjConstants.NCOL_F)
				DueDate = sheet.cell_value(curr_row, ObjConstants.NCOL_G)
				MaterialCost = sheet.cell_value(curr_row, ObjConstants.NCOL_H)
				Ext = sheet.cell_value(curr_row, ObjConstants.NCOL_I)
				PPV = sheet.cell_value(curr_row, ObjConstants.NCOL_J)
				Location = sheet.cell_value(curr_row, ObjConstants.NCOL_K)

				InsertIntoCS_New_Future_PPV(dB_table, Part_No,Po_No,POSupplier,Qty,float(PO_Price),Release_No,DueDate,float(MaterialCost),Ext,PPV,Location)

				curr_row += 1
				bar.next()
			bar.finish()
	except Exception as e:
		print(Classes.Constants.ERR_PREFIX + "Parse_New_Future_PPV() -")
		print(e)

def Main():
	print("Parsing quote responses to the DB...")
	try:
		##mpn_to_fstpn = Get_Latest_MPN_To_FSTPN()
		##if( ObjFunctions.LOAD_ORIGINAL_QUOTE_CLEAN_START == 1 ): Load_Original_Quote_Clean_Start()

		"""
		fileName = r'2021 Annual Quote.xlsx'
		fullPath = r'C:\dataXtractfiles\Quote_Analyzer\Sent\2021 Annual Quote.xlsx'

		if( ObjFunctions.LOAD_ORIGINAL_QUOTE == 1 ):
			Load_Original_Quote_(fullPath, fileName)
		"""

		suppliersList = LoadSuppliers()
		if( ObjFunctions.LOAD_QUOTES == 1 ):
			fileName = r'Firstronic-2021-RFQ-Detail.xlsx'
			fullPath = r'C:\dataXtractfiles\Quote_Analyzer\Sent\Firstronic-2021-RFQ-Detail.xlsx'

			##Load_Original_Quote_Details1(fullPath, fileName)
			ParseQuotesDirectory(suppliersList)
			SanitizeQuoteResponsesParsed()

			##Load_Files(mpn_to_fstpn)

		if( ObjFunctions.RUN_POST_CONSOLITATION_VERIFICATION == 1): Post_Consolidation_Verification(suppliersList)

		if( ObjFunctions.GET_LOWEST_QUOTE_PRICE_BY_PN == 1): Get_Lowest_Quote_Price_By_PN()

		if( ObjFunctions.LOAD_NEW_FUTURE_PPV == 1 ): Parse_New_Future_PPV()

		if( ObjFunctions.STD_COST_TO_NEW_FUTURE_PPV == 1 ): Get_StdCost_To_Future_PPV()

		print("\nParsing quote responses to the DB... Done!")

	except Exception as e:
		print(Classes.Constants.ERR_PREFIX + "Main() -")
		print(e)



##Program

##Instantiate classes
ObjAppSettings = Classes.DBConnectionString()
ObjConstants = Classes.Constants()
ObjFunctions = Classes.Functions()

dbCollaborations = 'Collaborations'
dbAZ_Dev_Test = 'AZ_Dev_Test'

"""
Swithcing to interact only w/azure due current commodity strategy infrastructure
Connect to Collaborations database to retrieve the app settings
"""

##Azure
driver= '{SQL Server}'
server = 'tcp:s5s4ajlw7v.database.windows.net'
database = dbCollaborations
devDatabase = dbAZ_Dev_Test
username = 'jbrubaker'
password = 'j88975First'
yes = Classes.DBConnectionString.yes##"yes"


system('cls')

try:
	cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	##print("DB connection succesful")

	print("Okey, let's get started. Retrieving app settings...")
	##Get the app settings
	_AppSettings = pd.read_sql_query(ObjAppSettings.QRY_GET_APP_SETTINGS_CS_QUOTE_ANALYZER_AZ,cnxn)
	##print(_AppSettings)


	##Get app settings to handle conection in the application
	##ObjAppSettings.App_Settings_Deploy_Mode_Id = _AppSettings["Deploy_Mode_ID"].iloc[0]
	##ObjAppSettings.App_Settings_Deploy_Mode = _AppSettings["Deploy_Mode"].iloc[0]

	ObjAppSettings.App_Settings_Server = _AppSettings["Datasource"].iloc[0]
	ObjAppSettings.App_Settings_Database = _AppSettings["Database"].iloc[0]
	ObjAppSettings.App_Settings_User_Name = _AppSettings["User_Name"].iloc[0]
	ObjAppSettings.App_Settings_Password = _AppSettings["Password"].iloc[0]

	ObjAppSettings.App_Settings_App_Name = _AppSettings["App Name"].iloc[0]
	ObjAppSettings.App_Settings_Version = _AppSettings["Version"].iloc[0]
	ObjAppSettings.Current_Commit = _AppSettings["Current_Commit"].iloc[0]

	cursor.close()
	cnxn.close()

	server = ObjAppSettings.App_Settings_Server
	database = ObjAppSettings.App_Settings_Database ##databaseLcl
	username = ObjAppSettings.App_Settings_User_Name ##usernameLcl
	password = ObjAppSettings.App_Settings_Password ##passwordLcl

	##Reconnect...
	if( ObjAppSettings.App_Settings_Deploy_Mode_Id == ObjAppSettings.DEPLOY_MODE_DEV ):
		database = devDatabase
		ObjAppSettings.App_Settings_Deploy_Mode = ObjAppSettings.DEPLOY_MODE_DEV_TXT
	else:
		database = database
		ObjAppSettings.App_Settings_Deploy_Mode = ObjAppSettings.DEPLOY_MODE_PROD_TXT

	cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	##print(cnxn)

	##driver = ObjAppSettings.driver## '{SQL Server}'##'{ODBC Driver 13 for SQL Server}'
	server = ObjAppSettings.serverLcl##'tcp:10.120.10.4,1433'##'s5s4ajlw7v.database.windows.net'
	database = ObjAppSettings.databaseLcl ##= 'BeFirst'
	username = ObjAppSettings.usernameLcl ##= 'DBuser'
	password = ObjAppSettings.driverLcl ##= 'DBuser2018*'
	###driver10_4= '{SQL Server}'##'{ODBC Driver 13 for SQL Server}'
	##yes = Classes.DBConnectionString.yes##"yes"

	tendotCnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';trusted_connection='+ yes)
	tendotCursor = tendotCnxn.cursor()

	##Cursor para BeFirst
	driver = ObjAppSettings.driver## '{SQL Server}'##'{ODBC Driver 13 for SQL Server}'
	server = ObjAppSettings.server10_4##'tcp:10.120.10.4,1433'##'s5s4ajlw7v.database.windows.net'
	database = ObjAppSettings.database10_4 ##= 'BeFirst'
	username = ObjAppSettings.username10_4 ##= 'DBuser'
	password = ObjAppSettings.password10_4 ##= 'DBuser2018*'
	###driver10_4= '{SQL Server}'##'{ODBC Driver 13 for SQL Server}'
	yes = Classes.DBConnectionString.yes##"yes"

	beFirstCnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';trusted_connection='+ yes)
	beFirstCursor = beFirstCnxn.cursor()
	##print(beFirstCnxn)

	##Let the user know to where it's connected
	print("\n----------------------")
	print("App Name: " + str(ObjAppSettings.App_Settings_App_Name))
	print("----------------------")
	print("App Version: " + str(ObjAppSettings.App_Settings_Version))
	print("----------------------")
	print("Current Commit: " + str(ObjAppSettings.Current_Commit))
	print("----------------------")
	print("Deply mode: " + str(ObjAppSettings.App_Settings_Deploy_Mode))
	print("----------------------")
	print("dataBase: " + str(ObjAppSettings.App_Settings_Database))
	print("----------------------")

	print("DB connection succesful")
	print("----------------------")

	"""
	##Dictionaries init
	companyName_dict = {}
	fileRevisions_dict = {}
	nonExcelFiles = []
	watchList_Emails = []
	"""
	suppliersList = ""
	Main()

except Exception as e:
	print(Classes.Constants.ERR_PREFIX + "Program() -")
	print type(e)
	print(e)
