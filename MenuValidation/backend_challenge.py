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
    
    storedValues = []
    #Go through all pages
    for num_pages in range(1,getAllPages(link)):
        #Iterate through all of the pages 
        totalresponse = requests.get("https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page="+str(num_pages))
        
        #Obtain entire json and store all root node information into one array
        childvalues = json.loads(totalresponse.text)
        storedValues += childvalues[root]
        
        
    return storedValues

if __name__ == "__main__":
     
    #Get total amount of pages in API link
    linkpages = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page=1"

    storeMenus = []
    
    #Get all Data for Menu's 
    entireMenu = getAllData("menus", storeMenus, linkpages)
    
    #print (entireMenu)
    
    root_id = ""
    children = []
        
    for i in range(len(entireMenu)):
        for j in range(len(entireMenu[i]["child_ids"])):
            if "parent_id" in entireMenu[i]:
                saveChildId = entireMenu[i]["child_ids"][j] 
                #print (saveChildId)
            else:
                #store root_id and begin search through child node menus
                root_id = entireMenu[i]["id"]
                saveChildId = entireMenu[i]["child_ids"][j] 
                print (saveChildId)    
            #for j in range(len(saveChildId)):    
            #    print (entireMenu[saveChildId[j]])
    
        
    
    
    
    
    
    
    
        

