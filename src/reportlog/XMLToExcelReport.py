'''
Created on Sep 26, 2012

@author: luong.mai
'''

from config.DataReader import DataReader
from reportlog.Log import Log
from xlrd import open_workbook
from xlutils.copy import copy
import os
import sys


class XMLToExcelReport():
    sheetRB = None
    env = None
    pathXMLReport = None
    dateReport = None
    rb = None
    platform = None
    browser = None
    fileNameTC = None
    pathFileTC = None
    testCasesPass = []
    testCasesFail = []
    testCasesError = []
    def __init__(self):
        try:
            os.environ["PYTHONPATH_KLOUT"]="D:\QuangTinh\Script\workspace\Training\src"
            XMLToExcelReport.env = os.getenv("PYTHONPATH_KLOUT")
            dataReader = DataReader(str(self.env) + "/config/config.xml").DataSet
            
            XMLToExcelReport.browser = dataReader.report["browser"]
            XMLToExcelReport.platform = dataReader.report["platform"]
            XMLToExcelReport.dateReport = dataReader.report["dateReport"]
            XMLToExcelReport.pathFileTC = dataReader.report.pathFileTC
            XMLToExcelReport.fileNameTC = dataReader.report.fileNameTC
            XMLToExcelReport.pathXMLReport = dataReader.report.pathXMLReport
            XMLToExcelReport.fileNameReport = dataReader.report.fileNameRP
            
            XMLToExcelReport.rb = open_workbook(str(self.env) + XMLToExcelReport.pathFileTC + "/" + XMLToExcelReport.fileNameTC +'.xls',formatting_info=True)
            XMLToExcelReport.sheetRB = self.rb.sheet_by_index(0)           
            
        except Exception, e:
            print str(e)
        
    
    @staticmethod
    def getModules():
        testModules = []
        data = ""
        for row in range(XMLToExcelReport.sheetRB.nrows):
            if(data!=XMLToExcelReport.sheetRB.cell(row,0).value):
                testModules.append(XMLToExcelReport.sheetRB.cell(row,0).value)
                data = XMLToExcelReport.sheetRB.cell(row,0).value
        return testModules
     
    @staticmethod
    def getTestCases(testModule):
        testCases = []
        for r0 in range(XMLToExcelReport.sheetRB.nrows):
            if XMLToExcelReport.sheetRB.cell(r0,0).value == testModule:
                start = r0 
                break
        end = 0
        for r0 in range(start,XMLToExcelReport.sheetRB.nrows):
            if XMLToExcelReport.sheetRB.cell(r0,0).value == testModule:
                end = end + 1
        
        for r1 in range(start,start+end):
            testCases.append(XMLToExcelReport.sheetRB.cell(r1,1).value)  
        return testCases 
     
    @staticmethod
    def XMLReader(): 
        try:    
       
            # Looping all XML file to found test cases are failed, error, passed
            for testmodule in testModules:  
                dataReader = DataReader(str(XMLToExcelReport.env) + XMLToExcelReport.pathXMLReport + "/" + XMLToExcelReport.dateReport + "/" + testmodule + "-" + XMLToExcelReport.browser + ".xml").DataSet
                errors = int(dataReader["errors"])
                fails = int(dataReader['failures'])
                if errors==0 and fails==0:
                    XMLToExcelReport.testCasesPass.append(testmodule)
                elif errors>0 and fails==0:
                    XMLToExcelReport.testCasesFail.append(testmodule)
                elif errors==0 and fails>0:
                    XMLToExcelReport.testCasesError.append(testmodule)    
        except Exception, e:
            Log.logError(str(e))
      
    @staticmethod           
    def CovertToExcel():
              
        rb = open_workbook(str(XMLToExcelReport.env) + XMLToExcelReport.pathFileTC + "/" + XMLToExcelReport.fileNameReport +'.xls',formatting_info=True)
        sheetRB = rb.sheet_by_index(0)  
        
        w = copy(rb)
        sheet = w.get_sheet(0)

        for colDate in range(6,sheetRB.ncols):
            # Find column date report
            if sheetRB.cell(0,colDate).value == XMLToExcelReport.dateReport:
                for colPlatform in range(colDate,colDate+3):
                    # Find column platform 
                    if sheetRB.cell(1,colPlatform).value==XMLToExcelReport.platform + " & " + XMLToExcelReport.browser:                      
                        # Write test result
                        for row in range(2,sheetRB.nrows):
                            for tcPass in XMLToExcelReport.testCasesPass:
                                if sheetRB.cell(row,0).value == tcPass:
                                    sheet.write(row,colPlatform,"Pass")
                            for tcFail in XMLToExcelReport.testCasesFail:
                                if sheetRB.cell(row,0).value == tcFail:
                                    sheet.write(row,colPlatform,"Fail")
                            for tcError in XMLToExcelReport.testCasesError:
                                if sheetRB.cell(row,0).value == tcError:
                                    sheet.write(row,colPlatform,"Error")
                    
        # Save file
        w.save(str(XMLToExcelReport.fileNameReport) + '.xls')
        
if __name__ == '__main__':
    testModules = []
    report = XMLToExcelReport()
    testModules = report.getModules()
    report.XMLReader()
    report.CovertToExcel()

    

            