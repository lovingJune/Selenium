'''
Created on Sep 18, 2012

@author: tin.trinh
'''

from page.AbstractPage import AbstractPage
from reportlog.Log import Log
import time

class ProfilePageKlout(AbstractPage):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.img_score_xpath = "//div[@class='score']"
        self.img_profile_xpath = "//span[@class='profile-img']"
        self.lbl_firstName_xpath="//div[@class='user-name']/span[@class='first-name']"
        self.lbl_lastName_xpath="//div[@class='user-name']/div[@class='last-name']"
        self.img_myProfile_xpath = "//div[@class='score-pic']/span/span"  
        self.link_addTopicLink_xpath = "//a[text()='Add your first topic here!']"
        self.pw_addTopicSearch_id = "add-topic-search"
        self.txt_searchTopic_xpath = "//input[@placeholder='Search for topic']"
        self.link_add_xpath = "//a[text()='Add']"
        self.link_seeMoreTopic_xpath = "//a[@class='see-all all-topics']"
        self.img_deleteTopic_xpath = "//div[@class='remove-topic']"
        self.btn_okay_xpath = "//a[text()='Okay']"
        self.img_closePopup_xpath = "//a[@class='close close-overlay']"
        self.link_addATopic_xpath = "//a[text()='Add a topic']"        
        self.div_container_xpath = "//div[@class='single-container-outer']"
      
    # add a topic
    def addTopic(self, topicName = "Iphone", existedTopic = True):
        if AbstractPage.flag:
            if existedTopic == False:
                # click add your firs topic link
                self.clickElementByXPath(self.link_addTopicLink_xpath)
            else:
                #click see more link
                self.clickElementByXPath(self.link_seeMoreTopic_xpath)
                
                # click add a topic link in case 
                self.clickElementByXPath(self.link_addATopic_xpath)
                
            # search a topic
            self.sendKeyByxPath(self.txt_searchTopic_xpath, topicName)
            
            # wait for search result displayed
            time.sleep(2)

            self.sendKeyByxPath(self.txt_searchTopic_xpath, "\n")
            
            # add topic
            self.clickElementByXPath(self.link_add_xpath)
            
            # wait for website save new topic
            time.sleep(2)
    
    def closeProfileTopicPopup(self):
        if AbstractPage.flag:
            #close popup add a topic
            self.clickElementByXPath(self.img_closePopup_xpath)
             
    # Check topic exist
    def checkTopicExist(self, topicName):
        if AbstractPage.flag:
            self.topicName = "//a[text()='"+topicName+"']"
            if self.checkControlExistedByXpath(self.topicName):
                Log.logInfo("Topic "+str(topicName)+" is existed!")
                return True
            else:
                Log.logInfo("Topic "+str(topicName)+" is not existed!")
                return False
    
    # Check "See more" link exist
    def isSeemoreLinkExist(self):
        if AbstractPage.flag:
            if self.checkControlExistedByXpath(self.link_seeMoreTopic_xpath):
                Log.logInfo("See more link is existed!")
                return True
            else:
                Log.logInfo("See more link is not existed!")
                return False
            
    # Delete topic exist
    def deleteTopicExist(self, topicName = "Iphone"):
        if AbstractPage.flag:
            self.topicName = "//h3[@class='topic-name']/a[text()='"+topicName+"']"
            self.topicNameAtLeftNavigation_xpath = "//a[text()='"+topicName+"']"
            self.delExistedTopicButton_xpath = "//a[@href='/topic/"+str(topicName).lower()+"']/../div[@class='remove-topic']"
            
            if self.checkControlExistedByXpath(element_xpath=self.topicNameAtLeftNavigation_xpath,timeout=10):
                
                # Open Profile Topic Dialog (click see more link)
                self.openProfileTopicDialog()
            
                # if pop up existed -> delete topic
                self.mouseMoveToElementByXpath(self.topicName)
        
                self.clickElementByXPath(self.delExistedTopicButton_xpath)
                    
                self.clickElementByXPath(self.btn_okay_xpath)
                    
                # Click on "x" image to close popup
                self.closeProfileTopicPopup()
            
    # Verify point Sccore
    def isScoreExisted_profilePage(self):   
        if AbstractPage.flag:                                                          
            if self.checkControlExistedByXpath(self.img_score_xpath):
                Log.logInfo("Control Score is existed!")
                return True
            else:
                Log.logInfo("Control Score is not existed!")
                return False
            
    # Verify point Profile picture
    def isProfilePictureExisted_profilePage(self):   
        if AbstractPage.flag:                                                                              
            if self.checkControlExistedByXpath(self.img_myProfile_xpath):
                Log.logInfo("Profile picture is existed!")
                return True
            else:
                Log.logInfo("Profile picture is not existed!")
                return False
            
    def isPopupDisplayed(self):
        if AbstractPage.flag:
            if self.checkControlExistedByXpath(self.img_closePopup_xpath):
                Log.logInfo("Popup displayed!")
                return True
            else:
                Log.logInfo("Popup is not displayed!")
                return False
        
    def openProfileTopicDialog(self):
        if AbstractPage.flag:              
            # click see more link
            self.clickElementByXPath(self.link_seeMoreTopic_xpath)

    def isAddYourFirstTopicHereExisted(self):
        if AbstractPage.flag:
            # check link Add your first topic here exists
            if self.checkControlExistedByXpath(self.link_addTopicLink_xpath):
                Log.logInfo("AddYourFirstTopicHere link existed!")
                return True
            else:
                Log.logInfo("AddYourFirstTopicHere link is not existed!")
                return False
                               
    def isProfileOfSelectedUserIsReturned(self, username):
        if AbstractPage.flag:
            try:
                fullName = self.getTextByXPath(self.lbl_firstName_xpath)+self.getTextByXPath(self.lbl_lastName_xpath)
                if str(fullName).__contains__(username)== True:
                    Log.logInfo("Profile of selected user is returned.")
                    return True
                else:
                    Log.logInfo("Profile of selected user is not returned.")
                    return False
            except Exception, e:
                Log.logError(str(e))
                return False
            
    def checkProfileTopicPopupExisted(self):
        if AbstractPage.flag:
            # check Profile Topic popup 
            if self.checkControlExistedByXpath(self.img_closePopup_xpath) == True:
                Log.logInfo("Profile Topic Popup existed!")
                return True
            else:
                Log.logInfo("Profile Topic Popup is not existed!")
                return False
            
    def isProfilePageExisted(self):
        if AbstractPage.flag:
            if self.isScoreExisted_profilePage()and self.isProfilePictureExisted_profilePage():
                Log.logInfo("Profile Page is existed!")
                return True
            else:
                Log.logInfo("Profile Page is not existed!")
                return False