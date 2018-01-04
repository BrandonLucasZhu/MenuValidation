'''
Created on Dec 30, 2017

@author: Brandon Zhu
'''

import os
import sys
import requests
import json
import pprint
import copy
import collections

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


def exploringGraph(start, graph,end, path = []):
    print (path)
    path = path + [start]
   # dup = set(path)
    if start == end:
        return [path]
    #elif findDuplicate(path) and len(path)>1:
    #    return [path]  #Duplicate detected  
    #if not rootId in graph:
    #    return None
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = exploringGraph(node,graph,end,path) 

            for newpath in newpaths:
                paths.append(newpath)


    return paths

def findDuplicate (checkinglist):
    unique = set(checkinglist)
    for each_val in unique:
        count = checkinglist.count(each_val)
        if count > 1:
            return True 
    return False                           

if __name__ == "__main__":
     
    #Get total amount of pages in API link
    linkpages = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page=1"
    storeMenus = []
    storeMenusNodes = {}
    
    #Get all Data for Menu's 
    entireMenu = getAllData("menus", storeMenus, linkpages)
    
    #print (entireMenu)
   	

    root_id = ""
    set_validity = [] #sort menu whether if they are valid or not
    store_rootId = []

    #Create a hashmap of the graphing api
    for i in range(len(entireMenu)):
    	
    	if entireMenu[i].get("parent_id") is None:
    		root_id = entireMenu[i]["id"]
        	store_rootId.append(str(root_id))
          

        	for j in range(len(entireMenu[i]["child_ids"])):
                    saveChildId = entireMenu[i]["child_ids"][j]
                    if str(root_id) in storeMenusNodes: 
                        storeMenusNodes[str(root_id)].append(str(saveChildId))  
                    else: 
                        storeMenusNodes[str(root_id)] = [str(saveChildId)]    
        else:
            current_id = entireMenu[i]["id"]
            if len(entireMenu[i]["child_ids"]) is 0:
                storeMenusNodes[str(current_id)] = ["end"]
            else:    
                for j in range(len(entireMenu[i]["child_ids"])):
                        saveChildId = entireMenu[i]["child_ids"][j]
                        #print (saveChildId)
                        if str(current_id) in storeMenusNodes: 
                            storeMenusNodes[str(current_id)].append(str(saveChildId))
                        else: 
                            storeMenusNodes[str(current_id)] = [str(saveChildId)]

    #print (storeMenusNodes)
    #for root in store_rootId:
    print (exploringGraph("1",storeMenusNodes,"end"))
                    #isValidMenu("2", saveChildId, entireMenu)
                    #print isAValidMenu(root_id, "" ,entireMenu)
                    #for val in isAValidMenu( root_id , "" , entireMenu ):
                        #print (val)
                    #[ print (x) for x in isAValidMenu( root_id , "" , entireMenu ) ]

                #print (saveChildId)
            #else:
                #store root_id and begin search through child node menus
                #root_id = entireMenu[i]["id"]
                #saveChildId = entireMenu[i]["child_ids"][j] 
                #print (root_id)    
            #for j in range(len(saveChildId)):    
            #    print (entireMenu[saveChildId[j]])
    
        
    
    
    
    
    
    
    
        

