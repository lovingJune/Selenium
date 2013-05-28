'''
Created on Aug 28, 2012

@author: vu.dao
'''
from page.AbstractPage import AbstractPage
class AccountSettingPageFB(AbstractPage):

    def __init__(self):
        '''
        Constructor
        '''
        self.link_navigateAcount_id = "navItem_account"
        self.link_editName_xpath = "//li[1]/a/span[text()='Edit']"
        self.link_editEmail_xpath = "//li[3]/a/span[text()='Edit']"
        self.btn_cancel_xpath = "//input[@value='Cancel']"
        self.txt_firstName_xpath = "//input[@name='first_name']"
        self.txt_lastName_xpath = "//input[@name='last_name']"
        self.rad_primaryEmail_xpath = "//input[@checked='1']/../label"
            
    def getUserSetting(self):
        if AbstractPage.flag:
            # Click on User Edit button
            self.clickElementByXPath(self.link_editName_xpath) 
                
            # Get first name and last name
            self.FirstName = self.getAttributeByXPath(self.txt_firstName_xpath, "value")
            self.LastName = self.getAttributeByXPath(self.txt_lastName_xpath, "value")
        
            return self.FirstName, self.LastName, self.getEmail()
        
    def getEmail(self):
        if AbstractPage.flag:
            # Click on Email Edit button
            self.clickElementByXPath(self.link_editEmail_xpath)                               
                    
            # Get email 
            element = self.getElementByXPath(self.rad_primaryEmail_xpath)
            self.emailAddress = element.text                
                    
            return self.emailAddress  

        