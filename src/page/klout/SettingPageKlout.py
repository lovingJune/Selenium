'''
Created on Aug 29, 2012

@author: Vu Dao
'''
from page.AbstractPage import AbstractPage
from page.facebook.LoginPageFB import LoginPageFB
from reportlog.Log import Log

class SettingPageKlout(AbstractPage):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.link_profileSetting_xpath = "//a[contains(text(),'Settings')]"
        self.txt_firstName_id = "edit-profile-firstName"
        self.txt_lastName_id = "edit-profile-lastName"
        self.txt_email_id = "edit-profile-email"
        self.rb_individualInfluencer_id  = "edit-profile-individual-influencer" 
        self.rb_brandInfluencer_id  = "edit-profile-brand-influencer" 
        self.txt_brandName_id = "edit-profile-brand"
        self.btn_save_id = "edit-profile-submit" 
        self.link_connectNetwork_xpath = "//a[contains(text(),'Connected Networks')]"
        self.btn_connectNowFb_xpath = "//a[@class='klout-button-primary' and @href='/fb_init']"
        self.btn_closeConnectPageDialog_xpath = "//a[@class='close close-modal']"
        self.icon_facebookConnect_xpath = "//div[@class='connected-network fb']"
        self.btn_mergeAccount_xpath = "//a[contains(text(),'Merge Accounts')]"    
        self.link_unlinkFacebook_id = "unlink-service-fb"
        
    def getFullName(self):
        if AbstractPage.flag:
            # Get first name
            firstName = self.getAttributeById(self.txt_firstName_id, "value")
            
            # Get user name
            lastName = self.getAttributeById(self.txt_lastName_id, "value")
            
            return firstName, lastName
            
    def getEmail(self):
        if AbstractPage.flag:
            # Get email
            email = self.getAttributeById(self.txt_email_id, "value")
            return email
            
    def getBrandName(self):
        if AbstractPage.flag:
            # Get brand name
            brandName = self.getAttributeById(self.txt_brandName_id, "value")
            return brandName
     
    def updated_Profile_Individual_Influencer(self, firstName, lastName, email):
        if AbstractPage.flag:
            # Click on profile settings button
            self.clickElementByXPath(self.link_profileSetting_xpath)
             
            # Check radio button of Individual Influencer is selected
            # If it is not selected, select it 
            self.selectRadioButtonById(self.rb_individualInfluencer_id)
                 
            # Input first name
            self.sendKeyById(self.txt_firstName_id, firstName)
            
            # Input last name
            self.sendKeyById(self.txt_lastName_id, lastName)
            
            # Input email
            self.sendKeyById(self.txt_email_id, email)
            
            # Click on Save button
            self.clickElementById(self.btn_save_id)
                
    def updated_Profile_Brand_Influencer(self, brandName, brandEmail):
        if AbstractPage.flag:
            # Click on profile settings button
            self.clickElementByXPath(self.link_profileSetting_xpath)
            
            # Check radio button of Brand Influencer is selected
            # If it is not selected, select it 
            self.selectRadioButtonById(self.rb_brandInfluencer_id)
            
            # Input brand name
            self.sendKeyById(self.txt_brandName_id, brandName)
            
            # Input brand email
            self.sendKeyById(self.txt_email_id, brandEmail)
            
            # Click on Save button
            self.clickElementById(self.btn_save_id)               
                    
    def is_Profile_Individual_Influencer_Correct(self, firstName, lastName, email):   
        if AbstractPage.flag:
            try:                 
                # Get first name and last name   
                firstNameKlout, lastNameKlout = self.getFullName()
                
                # Get email
                emailKlout = self.getEmail()
                
                # Check last name, first name, email is corrected
                if firstNameKlout == firstName and lastNameKlout == lastName and emailKlout == email:
                    Log.logInfo("profile Individual Influencer is corrected")
                    return True
                else:
                    Log.logInfo("profile Individual Influencer is not corrected")
                    return False
                
            except Exception, e:
                Log.logError(str(e))
                return False
            
    def is_Profile_Brand_Influencer_Correct(self, brandName, email): 
        if AbstractPage.flag:                
            # Get brand name   
            brandNameKlout = self.getBrandName()
            
            # Get brand email
            emailKlout = self.getEmail()
            
            # Check brand name, brand email is corrected
            if brandNameKlout == brandName and email == emailKlout:
                Log.logInfo("Profile Brand Influencer is corrected!")
                return True 
            else:
                Log.logInfo("Profile Brand Influencer is not corrected!")
                return False 
            
    def openSettingConnectedNetworks(self):
        if AbstractPage.flag:
            self.clickElementByXPath(self.link_connectNetwork_xpath)
    
    def connectNowFacebook(self):
        if AbstractPage.flag:
            self.clickElementByXPath(self.btn_connectNowFb_xpath)
            return LoginPageFB()
            
    def closePopup(self):
        if AbstractPage.flag:
            try:
                AbstractPage.Browser().switch_to_alert()
                # Click on 'x' link
                self.clickElementByXPath(self.btn_closeConnectPageDialog_xpath)                               
                
                Log.logInfo("The pop up closed successfully")
                return SettingPageKlout()
            except Exception, e:
                Log.logError(str(e))
                Log.logError("The pop up doesnot close successfully")
    
    # Merge account Twitter with account FaceBook
    def mergeUserTwitterWithFacebook(self, usernameMerged, passwordMerged):
        if AbstractPage.flag:
            try:
                if(self.checkControlExistedById(self.link_unlinkFacebook_id, 5)==False):
                    if self.checkControlExistedByXpath(self.btn_connectNowFb_xpath) == True:
                        # Click connect now to facebook
                        self.facebookLoginPage = self.connectNowFacebook()
                        
                        # Login facebook                             
                        self.facebookLoginPage.login(usernameMerged, passwordMerged)
                        
                        # Click on Allow button if show message warning
                        if self.facebookLoginPage.checkControlExistedByXpath(self.facebookLoginPage.btn_allow_xpath,timeout=5) == True:
                            self.facebookLoginPage.clickElementByXPath(self.facebookLoginPage.btn_allow_xpath)
                                                  
                        # Close dialog
                        self.closePopup()                            
                        
                        # Click on Merge Account button
                        if self.checkControlExistedByXpath(self.btn_mergeAccount_xpath,timeout=5) == True:
                            self.clickElementByXPath(self.btn_mergeAccount_xpath)
                else:
                    Log.logInfo("Account merged.")
            except Exception, e:
                Log.logError(str(e))
                Log.logInfo("Account is not merged.")
        