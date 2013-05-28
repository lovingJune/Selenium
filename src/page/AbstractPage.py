'''
Created on Dec 13, 2012

@author: tinh.do
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time, random, os
from selenium.webdriver.support.ui import Select
from browser.Browser import Browser
from reportlog.Log import Log

class AbstractPage():
    browser = None
    flag = True
    
    @classmethod
    def Browser(cls):
        if cls.browser == None:
            # open browser
            try:
                if AbstractPage.browser == None:
                    AbstractPage.browser = Browser.initBrowser()
                Log.logInfo("Open browser successfully")
            except Exception, e:
                Log.logError(str(e))
                Log.logError("Open browser unsuccessfully")
                AbstractPage.flag = False
        return cls.browser
        
    '''
    classdocs
    '''
    def __init__(self):
        '''
        # Following UI element declarations are for the header bar items
        #     like "Dashboard", "Profile", etc.
        '''
        self.btn_homeFacebook_id = "navHome"
        self.link_logoutFacebook_xpath = "//input[@value='Log Out']"
        self.btn_dropMenuFacebook_id = "userNavigationLabel"
        self.txt_user = "email"
        self.btn_home_id = "dashboard-menu-item"
        self.btn_dropdownMenu_id = "dropdown-summary-user"
        self.btn_dropdownMenu_xpath = "//a[@id='dropdown-summary-user']"
        self.link_logout_xpath = "//a[text()='Log out']"      
        self.txt_email_tw = ".//*[@id='front-container']/div[3]/div[2]/form/div[1]/label"
               
    '''
    Build in actions
    '''
    
    # Get element by ID 
    def getElementByID(self, elementId, timeout = 30):
        if AbstractPage.flag:
            try:
                WebDriverWait(AbstractPage.Browser, timeout).until(lambda driver: AbstractPage.Browser().find_element_by_id(elementId))
                return AbstractPage.Browser().find_element_by_id(elementId)
            except Exception, e:
                Log.logError(str(e))
                AbstractPage.flag = False
    
    # Get element by xpath
    def getElementByXPath(self, xPath, timeout = 30):
        if AbstractPage.flag:
            try:
                WebDriverWait(AbstractPage.Browser, timeout).until(lambda driver: AbstractPage.Browser().find_element_by_xpath(xPath))
                return AbstractPage.Browser().find_element_by_xpath(xPath)
            except Exception, e:
                Log.logError(str(e))
                AbstractPage.flag = False
     
    # Check control exist by ID       
    def checkControlExistedById(self,element_id, timeout = 60):
        if AbstractPage.flag:
            try:
                WebDriverWait(AbstractPage.Browser, timeout).until(lambda driver: AbstractPage.Browser().find_element_by_id(element_id))
                return True
            except Exception, e:
                Log.logError(str(e))
                return False
     
    # Check control exist by xpath       
    def checkControlExistedByXpath(self,element_xpath, timeout = 60):
        if AbstractPage.flag:
            try:
                WebDriverWait(AbstractPage.Browser, timeout).until(lambda driver: AbstractPage.Browser().find_element_by_xpath(element_xpath))
                return True
            except Exception, e:
                Log.logError(str(e))
                return False
     
    # move mouse to element by ID   
    def mouseMoveToElementById(self, elementID):
        if AbstractPage.flag:
            try:
                element = self.getElementByID(elementID)
                hov = ActionChains(AbstractPage.Browser()).move_to_element(element)
                hov.perform()
            except Exception, e:
                Log.logError(str(e))
    
    # move mouse element by xpath
    def mouseMoveToElementByXpath(self, elementXpath):
        if AbstractPage.flag:
            try:
                element = self.getElementByXPath(elementXpath)
                hov = ActionChains(AbstractPage.Browser()).move_to_element(element)
                hov.perform()
            except Exception, e:
                Log.logError(str(e))

    # Click on Element by Xpath  
    def clickElementByXPath(self, xpath):
        if AbstractPage.flag:
            try:
                element = self.getElementByXPath(xpath)
                element.click()
            except Exception, e:
                Log.logError(str(e))
     
    # Click on Element by ID   
    def clickElementById(self, id):
        if AbstractPage.flag:
            try:
                element = self.getElementByID(id)
                element.click()
            except Exception, e:
                Log.logError(str(e))
                
                
    # Select element on dropdown list   
    def selectDropdownListItemXpath(self, xpath, xpathItem):
        if AbstractPage.flag:
            try:
                self.getSettingPage.getElementByXPath(xpath).click()
                self.getSettingPage.getElementByXPath(xpathItem).click()
            except Exception, e:
                Log.logError(str(e))
        
    def selectDropdownListItem(self, id, value):        
        if AbstractPage.flag:
            try:                
                select = Select(self.getElementByID(id))               
                select.select_by_visible_text(value)                           
            except Exception, e:
                Log.logError(str(e))
        
    # get attribute of element by xpath 
    def getAttributeByXPath(self, xpath, attributeName):
        if AbstractPage.flag:
            try:
                element = self.getElementByXPath(xpath)
                return element.get_attribute(attributeName)            
            except Exception, e:
                Log.logError(str(e))
                AbstractPage.flag = False
    
    # get attribute of element by id
    def getAttributeById(self, id, attributeName):
        if AbstractPage.flag:
            try:
                element = self.getElementByID(id)
                return element.get_attribute(attributeName)
            except Exception, e:
                Log.logError(str(e))
                AbstractPage.flag = False
    
    # get text of element by xpath 
    def getTextByXPath(self, xpath):
        if AbstractPage.flag:
            try:
                element = self.getElementByXPath(xpath)
                return element.text      
            except Exception, e:
                Log.logError(str(e))
                AbstractPage.flag = False
            
    # get text of element by id
    def getTextById(self, id):
        if AbstractPage.flag:
            try:
                element = self.getElementByID(id)
                return element.text      
            except Exception, e:
                Log.logError(str(e))
                AbstractPage.flag = False
                
    # get location for elemnt by id
    def getLocationForElementById(self, id):
        if AbstractPage.flag:
            try:
                element = self.getElementByID(id)
                return element.location['x'], element.location['y']
            except Exception, e:
                Log.logError(str(e))
    
    # get location for element by xpath
    def getLocationForElementXpath(self, xPath):
        if AbstractPage.flag:
            try:
                element = self.getElementByXPath(xPath)
                return element.location['x'], element.location['y']
            except Exception, e:
                Log.logError(str(e))
   
    # Send value to element by ID
    def sendKeyById(self, id, value):
        if AbstractPage.flag:
            try:
                element = self.getElementByID(id)
                element.clear()
                element.send_keys(value)
            except Exception, e:
                Log.logError(str(e))
    
    # Send value to element by xpath
    def sendKeyByxPath(self, xPath, value):
        if AbstractPage.flag:
            try:
                element = self.getElementByXPath(xPath)
                element.clear()
                element.send_keys(value)
            except Exception, e:
                Log.logError(str(e))
            
    # Check radio button is selected by ID
    # If it not selected, select it    
    def selectRadioButtonById(self, id):
        if AbstractPage.flag:
            try:
                element = self.getElementByID(id)
                status = self.getAttributeById(id, "checked")
                if status == None:
                    element.click()
            except Exception, e:
                Log.logError(str(e))
    
    #check control status is enabled or disabled
    def checkControlStatus(self, id, status):
        if AbstractPage.flag:
            try:
                controlStatus = self.getAttributeById(id, status)
                if controlStatus != None and status == "disabled":
                    Log.logInfo("Control status is disabled")
                    return True
                elif controlStatus == None and status == "enabled":
                    Log.logInfo("Control status is enabled")
                    return True
                else:
                    Log.logInfo("Cannot find control")
                    return False        
            except Exception, e:
                Log.logError(str(e))
                return False
    
    # Switch to pop up window
    def switchToPopUpWindow(self):
        if AbstractPage.flag:
            try:
                # get current window
                parentWindow = AbstractPage.browser.current_window_handle
                handles = AbstractPage.browser.window_handles 
                handles.remove(parentWindow)
                # handle pop up window
                AbstractPage.browser.switch_to_window(handles.pop())
            except Exception, e:
                Log.logError(str(e))
                AbstractPage.flag = False

    # Check if Text is present on current window
    def isTextPresent (self, elementType, element, string):
        if AbstractPage.flag:
            try:
                if elementType == "xpath":
                    text = self.getTextByXPath(element)
                    if string in text:
                        Log.logInfo("Text is present in current window")
                        return True
                    else: 
                        Log.logInfo("Text is not present in current window")
                        return False
                elif elementType == "id":
                    text = self.getTextById(elementType)            
                    if string in text:
                        Log.logInfo("Text is present in current window")
                        return True
                    else: 
                        Log.logInfo("Text is not present in current window")
                        return False
            except Exception,e:
                Log.logError(str(e))
                return False       
    
    '''
    '''
    
    # close browser
    @staticmethod
    def closeBrowser():
        try:
            AbstractPage.Browser().quit()
            AbstractPage.browser = None
            AbstractPage.flag = True
            Log.logInfo("Close browser")
        except Exception, e:
            Log.logError(str(e))
    
    # navigate to web 
    @staticmethod
    def navigateToWeb(url):
        if AbstractPage.flag:
            try:
                AbstractPage.Browser().get(url)
                AbstractPage.Browser().implicitly_wait(60)
                Log.logInfo("Navigate to %s successfully" % url)
                return AbstractPage.Browser()
            except Exception, e:
                AbstractPage.flag = False
                Log.logError(str(e))
                Log.logError("Navigate to %s unsuccessfully" % url)
    
    # logout Klout website
    @staticmethod        
    def logoutKlout():
        if AbstractPage.flag:
            try:
                # Log out if the page is the home (already logged in) then log out before logging in
                page = AbstractPage()
                if page.checkControlExistedById(page.btn_dropdownMenu_id):
                    # Select Log out menu item
                    # wait for dropdown menu displayed successful
                    time.sleep(1)
                    page.mouseMoveToElementById(page.btn_dropdownMenu_id)
                    # wait for dropdown menu displayed successful
                    time.sleep(1)
                    page.mouseMoveToElementById(page.btn_home_id)
                    page.mouseMoveToElementById(page.btn_dropdownMenu_id)
                    page.clickElementByXPath(page.link_logout_xpath)
                page = None
            except Exception, e:
                Log.logError(str(e))
             
    # logout Facebook website
    @staticmethod
    def logoutFacebook():
        if AbstractPage.flag:
            try:
                # Log out if the page is the home (already logged in) then log out before logging in
                page = AbstractPage()
                if page.checkControlExistedById(page.btn_homeFacebook_id):
                # Click dropdown menu
                    page.clickElementById(page.btn_dropMenuFacebook_id)
                    # wait for dropdown menu displayed successful
                    time.sleep(2)
                    
                    # Click Logout
                    page.clickElementByXPath(page.link_logoutFacebook_xpath)
                    time.sleep(2)
                    
                page = None
            except Exception, e:
                Log.logError(str(e))
        
    # logout Twitter website
    @staticmethod
    def logoutTwitter():
        if AbstractPage.flag:
            try:
                # Log out if the page is the home (already logged in) then log out before logging in
                page = AbstractPage()
                if page.checkControlExistedById(page.btn_dropMenuTwitter_id):
                # Click dropdown menu
                    time.sleep(5)
                    page.clickElementById(page.btn_dropMenuTwitter_id)
                    time.sleep(2)
                    
                    # Click Logout
                    page.clickElementByXPath(page.link_logoutTW_xpath)
                    time.sleep(2)
                    
                page = None
            except Exception, e:
                Log.logError(str(e))
        
        # Get random int value between lower bound and upper bound
    def getRandomInt(self, nLowerbound, nUpperbound):
        return int((nUpperbound - nLowerbound + 1) * random.random() + nLowerbound)
    
    @staticmethod 
    def getRandomString(nStringLength):
        randmStr = ''
        for item in range(nStringLength):
            # select random character 
            nInt = AbstractPage().getRandomInt(65, 90) 
            randmStr = randmStr + chr(nInt)
        return randmStr