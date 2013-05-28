'''
Created on Dec 13, 2012

@author: tinh.do
'''
import os
from config.DataReader import DataReader

class DataConfig():
    
    dataset = None
    @classmethod
    def dataSet(cls):
        return cls.dataset
    
    def __init__(self):
        '''
        Constructor
        '''
    
    # return value of a node
    # nodeName: Name of node which you want to get content    
    @staticmethod
    def getDataNode(nodeName):
        try:        
            env = os.getenv("PYTHONPATH_KLOUT")
            dataReader = DataReader(str(env) + "/config/config.xml").DataSet
            if str(nodeName) == "use_grid":
                return dataReader.use_grid
#            elif str(nodeName) == "python_path":
#                return dataReader.python_path
#            elif str(nodeName) == "source_path":
#                return dataReader.source_path
            elif str(nodeName) == "report_path":
                return dataReader.report_path
            elif str(nodeName) == "browser":
                return dataReader.browser
        except Exception, e:
            print str(e)
     
    @staticmethod       
    def getNodeEnvironment(nameENV):
        try:        
            env = os.getenv("PYTHONPATH_KLOUT")
            dataReader = DataReader(str(env) + "/config/config.xml").DataSet
            for node in dataReader.test_enviroment:
                if node.name == nameENV:
                    DataConfig.dataset = node
                    break
        except Exception, e:
            print str(e)