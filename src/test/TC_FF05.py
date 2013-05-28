'''
Created on Dec 12, 2012

@author: tinh.do
'''
import unittest
from test.AbstractTest import AbstractTest
import xmlrunner

class TC_FF05(unittest.TestCase, AbstractTest):

    def setUp(self):
        AbstractTest.__init__(self)
        self.usernameList = "VUONG"
        self.ListName = "Giang test1"
        self.ListDes = "test"
        
        # Step1: Login Klout with facebook
        self.login(username=self.usernameFB, password=self.passwordFB)
        
        # Step2: Open Friend page
        #self.friend_list = self.homePage.openFriendsPage()
        
        # Step3: Create new list        
        #self.friend_list.createNewList(userName=self.usernameList, listName=self.ListName,listDescription=self.ListDes,closePopup=True)          
        
        # Step 4: Select list was created
        # Step 5: Click "delete this list" button without close popup
        #self.friend_list.deleteList(self.ListName, False)

    def tearDown(self):
        # Logout Klout and close browser
        self.logout()        

    def test_TC_Popup_Displayed_And_Klout_List_Deleted(self):
        # VP: Check popup displayed
        #self.verifyTrue(self.friend_list.isPopupDisplayed())
        pass
        # Step4: Click "Okay" button
        #self.friend_list.clickOkayButton()
        
        # VP: Check popup closed
        #self.verifyFalse(self.friend_list.isPopupDisplayed(), "Popup is closed!")
        
        # VP: Check list deleted
        #self.verifyTrue(self.friend_list.isKloutListDeleted(self.ListName), "List is deleted complete!")

#if __name__ == '__main__':
AbstractTest.writeTestReport(TC_FF05)