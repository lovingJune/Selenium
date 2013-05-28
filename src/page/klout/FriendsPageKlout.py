'''
Created on Sep 14, 2012

@author: tan.thanh.vo
'''
from page.AbstractPage import AbstractPage
from page.klout.ProfilePageKlout import ProfilePageKlout
import time
from reportlog.Log import Log

class FriendsPageKlout(AbstractPage):
    def __init__(self):
        '''
        Constructor
        '''
        self.btn_createNewList_xpath = "//a[text()='Create a new list']"
        self.btn_addFaceFriend_xpath = "//a[@class='fb viral-link mfs']"
        self.btn_addTWFriend_xpath = "//a[@class='tw viral-link']"
        self.pl_TWFriend_xpath = "//a[@href='#/friends/tw']"
        self.txt_listUsername_id = "list-user-search"
        self.txt_listName_id = "edit-list-name"
        self.txt_listDes_id = "edit-list-description"
        self.btn_add_id = "add-user"
        self.btn_cancel_xpath = "//a[text()='Cancel']"
        self.btn_save_id = "edit-list-save"
        self.link_closePopup_xpath = "//a[@class='close close-modal']"
        self.tf_status_xpath = ".//*[@id='status']"
        self.btn_tweet_xpath = ".//*[@id='update-form']/div[4]/fieldset/input[2]" 
        self.tf_tweetComplete_xpath = "//div[@class='action-information tweet-complete']"
        self.btn_closeModal_xpath = "//*[@class = 'close close-modal']"
        self.btn_deleteList_xpath = "//a[@class='delete-list']"
        self.btn_deleteConfirm_xpath = "//*[@class = 'button ok']"
        self.btn_cancelDeleting_xpath = "//*[@class = 'button cancel']"
        self.lbl_listUserSearchStatus_id = "list-user-search-status"
        self.btn_editListCreateList_xpath = "//*[@class='edit-list create-list']"
        self.btn_editListSave_id = "edit-list-save"
        self.btn_editListCancel_xpath = "//*[@class = 'edit-list-cancel cancel button-secondary']"
        self.link_group_xpath = "//a[text()= '"
        self.txt_shareNewPopup_xpath = "//div[@id='share-new-list']/h2"
        self.lbl_userSearchStatus_xpath = "//*[@id='list-user-search-status']"
        self.pw_inviteFriend_id = "fbFriendInvite"
        self.pw_confirm_dialog_id = "confirm-dialog"
        self.btn_continueAddFriend_xpath = "//*[@class = 'submit-button']"
        self.btn_sendRequest_id = "ok_clicked"
        self.lb_inviteSent_xpath = "//*[@class='flash success']"
        self.btn_addOfFriend_xpath = "//*[contains(@class,'unregistered-callout-button')]"
        self.btn_addFacebookFriend_xpath = "//*[@class = 'fb viral-link mfs']"
        self.chb_selectAllFriend_xpath = "//*[@class = 'checkbox-input' and @name = 'select-all']"
        self.pw_inviteFacebookFriend_id = "invite-view"
        self.btn_sendRequestFacebookFriend_id = "us59ywy2"
        self.btn_cancelSendRequestPopup_id = "ux4ovz13"
        
    def closePopup(self):
        if AbstractPage.flag:   
            # wait for popup load complete
            time.sleep(1)
            # Click on 'x' link
            self.clickElementByXPath(self.link_closePopup_xpath)                               
                        
    def isTwitterListExisted(self):
        if AbstractPage.flag:                                                                                         
            if self.checkControlExistedByXpath(self.pl_TWFriend_xpath):
                Log.logInfo("Twitter list element existed!")
                return True
            else:
                Log.logInfo("Twitter list element is not existed!")
                return False              
                                                   
    # Check popup display
    def isPopupDisplayed(self):
        if AbstractPage.flag:               
            if self.checkControlExistedById(self.pw_confirm_dialog_id):
                Log.logInfo("Popup displayed!")
                return True
            else:
                Log.logInfo("Popup is not displayed!")
                return False

    # Share Tweet on Twitter page
    def shareTweet(self, description):
        if AbstractPage.flag:

            self.sendKeyByxPath(self.tf_status_xpath, description)
            self.clickElementByXPath(self.btn_tweet_xpath)

    # Check if message "Your Tweet has been posted!" exist
    def isPostedTweetMessageExisted(self, message):
        if AbstractPage.flag:                        
            self.isTextPresent(elementType="xpath", element=self.tf_tweetComplete_xpath, string=message)
              
        
    # Check if message "Already Added!" exist     
    def isAlreadyAddedMessageExisted(self, message):
        if AbstractPage.flag:   
            #wait for message displayed
            time.sleep(2)        
            return self.isTextPresent(elementType="xpath", element=self.lbl_userSearchStatus_xpath, string=message)                      
          
    # Select Twitter list on Friend Page
    def selectTwitterList(self):
        if AbstractPage.flag:
            self.clickElementByXPath(self.pl_TWFriend_xpath)                         
               
    # Open pop up share link on Twitter     
    def openPopupShareLinkOnTwitter(self):
        if AbstractPage.flag:
            self.clickElementByXPath(self.btn_addTWFriend_xpath)
            # wait for new window load successfully
            time.sleep(3)                
            self.switchToPopUpWindow()                          
                
    def selectExistList(self, listName):
        if AbstractPage.flag:                       
            listName = self.link_group_xpath + listName + "']"
            self.clickElementByXPath(listName)
                
    def isKloutListDeleted(self, listName):
        if AbstractPage.flag:
            # wait for list not displayed
            time.sleep(1)   
            listName = self.link_group_xpath + listName + "']"
            if self.checkControlExistedByXpath(listName) == False:
                Log.logInfo("List name is deleted!")
                return True
            else:
                Log.logInfo("List name is not deleted!")
                return False
                
    def addUser(self, userName):
        if AbstractPage.flag:                                      
            #Enter name in "Enter Twitter Name Here" textbox
            self.sendKeyById(self.txt_listUsername_id, userName)
            time.sleep(1)
            #Click "Add" button
            self.clickElementById(self.btn_add_id)
            # Sleep to wait for adding TW list
            time.sleep(2)     
    
    def createNewList(self, userName, listName, listDescription, closePopup=True):
        if AbstractPage.flag:
            # Wait for "Create New List" button ready for click
            time.sleep(2)                   
            #Click on "Create New List" button
            self.clickElementByXPath(self.btn_createNewList_xpath)            
       
            #Enter name in "Enter Twitter Name Here" textbox then clicking Add button
            self.addUser(userName)
            
            #Enter List Name
            if (listName != None):
                self.sendKeyById(self.txt_listName_id, listName)
            
            #Enter List Description
            if (listDescription != None):
                self.sendKeyById(self.txt_listDes_id, listDescription)
            
            #Click on Save button           
            # Sleep to wait for Save button displays
                       
            self.clickElementById(self.btn_save_id)
            
            if closePopup == True:
                # wait for popup displayed
                time.sleep(2)
                
                #Close modal pop-up
                self.clickElementByXPath(self.btn_closeModal_xpath)
                
    def deleteList(self, listName, closePopup=True):
        if AbstractPage.flag:                 
            #Select a list to delete
            self.selectExistList(listName)
                              
            #Click on "Delete this list" button           
            self.clickElementByXPath(self.btn_deleteList_xpath)
                                          
            #Click on "Okay" button to confirm deleting            
            if closePopup:
                self.clickElementByXPath(self.btn_deleteConfirm_xpath)            

    # Click "delete this list" button
    def clickDeleteThisListButton(self):
        if AbstractPage.flag:
            self.clickElementByXPath(self.btn_deleteList_xpath)
    
    # Click "No Thanks" button
    def clickNoThanksButton(self):
        if AbstractPage.flag:
            self.clickElementByXPath(self.btn_cancelDeleting_xpath)
    
    # Click "Okay" button
    def clickOkayButton(self):
        if AbstractPage.flag:
            self.clickElementByXPath(self.btn_deleteConfirm_xpath)
                
    #Click "Edit this list" button
    def clickEditThisListButton(self):
        if AbstractPage.flag:
            self.clickElementByXPath(self.btn_editListCreateList_xpath)  
                
    # Check list name on the pop up
    def isListNameOnPopup(self, listName):
        if AbstractPage.flag:
            try:
                AbstractPage.Browser().switch_to_alert()
                txt_shareNewPopup = self.getTextByXPath(self.txt_shareNewPopup_xpath)
                if str(txt_shareNewPopup).__contains__(listName) == True:
                    Log.logInfo("List name is on the pop up.")
                    return True
                else:
                    Log.logInfo("List name is not on the pop up.")
                    return False
            except Exception, e:
                Log.logError(str(e))
                return False
                
    def isListNameOnLeftNavigation(self, listName):
        if AbstractPage.flag:
            self.listname = "//a[@class='tab-link' and text()='" + listName + "']"
            if self.checkControlExistedByXpath(self.listname):
                Log.logInfo("List name is on the left navigation!")
                return True
            else:
                Log.logInfo("List name is not on the left navigation!")
                return False

    def isNameUserOnFriendList(self, username):
        if AbstractPage.flag:
            self.username = "//a[@class='profile-link' and contains(text(),'" + username + "')]"
            if self.checkControlExistedByXpath(self.username):              
                Log.logInfo("User name is on the friend list.")  
                return True
            else:
                Log.logInfo("User name is not on the friend list.")
                return False
                               
    #Click "Cancel" on Edit list pop-up
    def clickCancelEditListPopup(self):
        if AbstractPage.flag:
            self.clickElementByXPath(self.btn_editListCancel_xpath)
                
    # Open profile of selected user in the exist friend list 
    def openProfileUserFromFriendList(self, listName, username):
        if AbstractPage.flag:
            self.clickElementByXPath("//a[@class='tab-link' and text()='" + listName + "']")
            self.clickElementByXPath("//a[@class='profile-link' and contains(text(),'" + username + "')]")
            return ProfilePageKlout()
    
    # Get list name from pop up when user create list friend without input list name
    def getListNameFromPopUp(self):
        if AbstractPage.flag:
            try:
                AbstractPage.Browser().switch_to_alert()
                txt_shareNewPopup = self.getTextByXPath(self.txt_shareNewPopup_xpath)
                txt_listname = str(txt_shareNewPopup).split('"')
                return txt_listname[1]
            except Exception, e:
                Log.logError(str(e))
                return str(e)
            
    #Check "Add Friend" Popup displays
    def isPopupAddFriendDisplay(self):
        if AbstractPage.flag:
            if self.checkControlExistedById(self.pw_inviteFriend_id):
                Log.logInfo("Popup Add Friend displays!")
                return True
            else:
                Log.logInfo("Popup Add Friend is not displayed!")
                return False
            
    #Check "Add Friend TW" Popup displays
    def isPopupAddFriendTwitterDisplay(self):
        if AbstractPage.flag:
            if self.checkControlExistedById(self.btn_tweet_xpath):
                Log.logInfo("Popup Add Friend Twitter displays!")
                return True
            else:
                Log.logInfo("Popup Add Friend Twitter is not displayed!")
                return False
    

    #Click "Continue" button
    def clickContinueAddFriendButton(self):
        if AbstractPage.flag:
            self.clickElementByXPath(self.btn_continueAddFriend_xpath)
                
    #Click "Send Request" button
    def clickSendRequestButton(self):
        if AbstractPage.flag:
            self.clickElementById(self.btn_sendRequest_id)
                
    #Check "Invite Sent" message displays
    def isInviteSentMessageExisted(self, message):
        if AbstractPage.flag:         
            return self.isTextPresent(elementType="xpath", element=self.lb_inviteSent_xpath, string=message)

    
    #Click "Add" button of a friend to invite
    def clickAddOfFriendButton(self):
        if AbstractPage.flag:
            self.clickElementByXPath(self.btn_addOfFriend_xpath)
                
    #Click Add Facebook Friend button
    def clickAddFacebookFriendButton(self):
        if AbstractPage.flag:
            self.clickElementByXPath(self.btn_addFacebookFriend_xpath)
                
    #Check All Friends Checkbox is checked
    def isAllFriendCheckboxChecked(self):
        if AbstractPage.flag:
            ischecked = self.getAttributeByXPath(self.chb_selectAllFriend_xpath, "checked")
            if(ischecked == "true"):
                Log.logInfo("All Friend Checkbox is checked")
                return True
            else:
                Log.logInfo("All Friend Checkbox is not checked")
                return False
            
    #Check Popup Add Facebook Friend displays
    def isPopupAddFacebookFriendDisplay(self):
        if AbstractPage.flag:
            if self.checkControlExistedById(self.pw_inviteFacebookFriend_id): 
                Log.logInfo("Popup Add Facebook Friend displays!")
                return True
            else:
                Log.logInfo("Popup Add Facebook Friend is not displays!")
                return False
        
    #Click "Send Request" button
    def clickSendRequestFacebookFriend(self):
        if AbstractPage.flag:
            self.clickElementById(self.btn_sendRequest_id)
                
    #Click "Cancel" button to cancel "Send Request" popup         
    def clickCancelAddFacebookFriendPopup(self):
        if AbstractPage.flag:
            self.clickElementById(self.btn_cancelSendRequestPopup_id)
    