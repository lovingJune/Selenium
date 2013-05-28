'''
Created on Dec 13, 2012

@author: tinh.do
'''
import os, sys
from selenium import webdriver
from config.DataConfig import DataConfig

class Browser():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
        
    @staticmethod
    def initBrowser():        
        if DataConfig.getDataNode("use_grid")=="No":          
            if DataConfig.getDataNode("browser") =="firefox":
                driver = webdriver.Firefox()                
            elif DataConfig.getDataNode("browser") == "ie":
                driver = webdriver.Ie()                
            elif DataConfig.getDataNode("browser") == "chrome":
                env = os.getenv("PYTHONPATH_KLOUT")
                chromeDriver_path = str(env) + "\chromedriver.exe"                        
                driver = webdriver.Chrome(chromeDriver_path)
            
        elif DataConfig.getDataNode("use_grid")=="yes":
            args_ = sys.argv
            browser = args_[2]
            node = args_[1]
            platform = args_[3]
            hubIP = args_[4]
            hubPort = args_[5]
                
            driver = webdriver.Remote(command_executor = "http://"+hubIP+":"+hubPort+"/wd/hub", desired_capabilities={
        
            "browserName": browser,
            
            "platform": platform,
            
            "node":node })
                
        # Maximize window
#        driver.maximize_window()
        return driver
        