'''
Created on Dec 13, 2012

@author: tinh.do
'''

import os
from config.DataReader import DataReader


class BrowserNoneGrid():
   
    env = os.getenv("PYTHONPATH_KLOUT")
    dataReader = DataReader(str(env) + "/config/config.xml").DataSet
    browser = dataReader.browser
    version = dataReader.browserVersion
        

class HubNode():
    # read data from config.xml, save with class's attributes
    env = os.getenv("PYTHONPATH_KLOUT")
    dataReader = DataReader(str(env) + "/config/config.xml").DataSet
    use_grid = dataReader.use_grid
#    python_path = dataReader.python_path
#    source_path = dataReader.source_path
#    report_path = dataReader.report_path
    hub_host = dataReader.hub_host
    hub_port = dataReader.hub_port
    parallel = dataReader.parallel
            
class GridNode():
    '''
    Description: Get environment (browser, flatform,...) for a node
    Argument:
        nodeName: name of node (go to config.xml, in <grid_node>)
    Return: return a node include <parallel><browser><platform><node_host><node_port>...
    '''
    @staticmethod
    def getGridNode(nodeName):
        try:        
            env = os.getenv("PYTHONPATH_KLOUT")
            dataReader = DataReader(str(env) + "/config/config.xml").DataSet
            for node in dataReader.grid_node:
                if node.name == nodeName:
                    return node
                    break
        except Exception, e:
            print str(e)