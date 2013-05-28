'''
Created on Aug 29, 2012

@author: Vu Dao
'''
from page.AbstractPage import AbstractPage
from page.klout.SettingPageKlout import SettingPageKlout
from page.klout.FriendsPageKlout import FriendsPageKlout
from page.klout.DashboardPageKlout import DashboardPageKlout
from page.klout.ProfilePageKlout import ProfilePageKlout
from reportlog.Log import Log

class HomePageKlout(AbstractPage):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.btn_home_id = "dashboard-menu-item"
        self.btn_dropdownMenu_id = "dropdown-summary-user"
        self.btn_dropdownMenu_xpath = "//a[@id='dropdown-summary-user']"
        self.link_setting_xpath = "//a[text()='Settings']"
        self.link_profile_xpath = "//a[text()='Profile']"
        self.link_friends_xpath = "//a[text()='Friends']"
        self.link_logout_xpath = "//a[text()='Log out']"
        self.img_score_xpath = "//div[@class='score']"
        self.img_profile_xpath = "//span[@class='profile-img']"
        self.img_myProfile_xpath = "//div[@class='score-pic']/span/span"    
        self.lbl_firstName_xpath = "//span[@class='first-name']"
        self.lbl_lastName_xpath = "//div[@class='last-name']"    
        self.img_myProfile_xpath = "//div[@class='score-pic']/span/span"    
        self.img_klout_logo_id = "logo"
        self.frm_score_network_pic_xpath = "//div[@class = 'score-networks-pic']"

    def openSettingPage(self):
        if AbstractPage.flag:
            # Move mouse to dropdown menu
            self.mouseMoveToElementById(self.btn_dropdownMenu_id)
#               time.sleep(3)
            # Click on Setting button
            self.clickElementByXPath(self.link_setting_xpath)
                
            return SettingPageKlout()
    
    # Open friends page
    def openFriendsPage(self):
        if AbstractPage.flag:
            # Move mouse to dropdown menu
            self.mouseMoveToElementById(self.btn_dropdownMenu_id)
            
            # Click on Friends link
            self.clickElementByXPath(self.link_friends_xpath)
            
            return FriendsPageKlout()
    
    #Open Dashboard page by clicking on DashboardPage button
    def openDashboardPage(self, logo=False):
        if AbstractPage.flag:           
            if(logo == False):
                self.clickElementById(self.btn_home_id)
            else:
                self.clickElementById(self.img_klout_logo_id)
            return DashboardPageKlout()    
    
    # Open Profile page by clicking on profile link
    def openProfilePage(self):
        if AbstractPage.flag:                
            # Move mouse to dropdown menu
            self.mouseMoveToElementById(self.btn_dropdownMenu_id)

            # Click on profile button
            self.clickElementByXPath(self.link_profile_xpath)
                
            return ProfilePageKlout()
    
    def isHomePageKloutExist(self):   
        if AbstractPage.flag:                                                                                              
            if self.checkControlExistedByXpath(self.frm_score_network_pic_xpath):
                Log.logInfo("Klout Home Page is existed!")
                return True
            else:
                Log.logInfo("Klout Home Page is not existed!")
                return False
        
    def getNameOfPicture(self):
        if AbstractPage.flag:
            try:                                                                                
                return self.getAttributeByXPath(self.img_myProfile_xpath, "title")
                
            except Exception, e:
                Log.logError(str(e))

    def getAccountName(self):
        if AbstractPage.flag:
            try:
                # Get first name and last name
                self.FirstName = self.getTextByXPath(self.lbl_firstName_xpath)                
                self.LastName = self.getTextByXPath(self.lbl_lastName_xpath)
                
                return self.FirstName, self.LastName
            except Exception, e:
                Log.logError(str(e))

    def isScoreExisted(self):   
        if AbstractPage.flag:                                                                              
            if self.checkControlExistedByXpath(self.img_score_xpath):
                Log.logInfo("Score picture is existed")
                return True
            else:
                Log.logInfo("Score picture is not existed")
                return False
            
    def isProfilePictureExisted(self):   
        if AbstractPage.flag:                                                                              
            if self.checkControlExistedByXpath(self.img_myProfile_xpath):
                Log.logInfo("Profile's picture is existed!")
                return True
            else:
                Log.logInfo("Profile's picture is not existed!")
                return False
                
            
    def isProfilePageExisted(self):
        if AbstractPage.flag:
            if self.isScoreExisted()and self.isProfilePictureExisted():
                Log.logInfo("Profile Page is existed!")
                return True
            else:
                Log.logInfo("Profile Page is not existed!")
                return False
            