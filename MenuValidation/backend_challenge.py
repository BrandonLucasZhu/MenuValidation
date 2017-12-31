'''
Created on Dec 30, 2017

@author: Brandon Zhu
'''

import os
import sys
import requests
import json
import pprint

def getAllPages(link):
    
    initialresponse = requests.get(link)
    getTotalPage = json.loads(initialresponse.text)
    
    totalpages = getTotalPage["pagination"]["total"] 
    
    return totalpages

def getAllData(root, storeValues, link):
    
    #Go through all pages
    for num_pages in range(1,getAllPages(link)):
        #Iterate through all of the pages 
        totalresponse = requests.get("https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page="+str(num_pages))
        
        childvalues = json.loads(totalresponse.text)
        print (childvalues[root])
        
    return storeValues

if __name__ == "__main__":
     
    #Get total amount of pages in API link
    linkpages = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page=1"

    storeMenus = []
    
    #Get all Data for Menu's 
    entireMenu = getAllData("menus", storeMenus, linkpages)
        
       
    
    
    
    
    
    
    
    
        

