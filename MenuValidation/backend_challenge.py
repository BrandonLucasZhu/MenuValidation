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

def isValidMenu (rootId, checkChildIds, entireMenuData):
	nextId = ""

	explored = []
    # keep track of nodes to be checked
    queue = [rootId]

    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            child_ids = entireMenuData[node]['child_ids']
 
            # add neighbours of node to queue
            for child_id in child_ids:
                queue.append(child_id)
    print (explored)
    return explored

#	if nextId != rootId:
#		nextId = entireMenuData[checkChildIds]['child_ids']

#	return 0


if __name__ == "__main__":
     
    #Get total amount of pages in API link
    linkpages = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page=1"

    storeMenus = []
    
    #Get all Data for Menu's 
    entireMenu = getAllData("menus", storeMenus, linkpages)
    
    print (entireMenu)
   	

    root_id = ""
    set_validity = [] #sort menu whether if they are valid or not
        
    for i in range(len(entireMenu)):
    	#print (entireMenu[i])
    	if entireMenu[i].get("parent_id") is None:
    		root_id = entireMenu[i]["id"]
        	print (root_id)

        	for j in range(len(entireMenu[i]["child_ids"])):
            		saveChildId = entireMenu[i]["child_ids"][j]
                	isValidMenu("2", saveChildId, entireMenu)


                #print (saveChildId)
            #else:
                #store root_id and begin search through child node menus
                #root_id = entireMenu[i]["id"]
                #saveChildId = entireMenu[i]["child_ids"][j] 
                #print (root_id)    
            #for j in range(len(saveChildId)):    
            #    print (entireMenu[saveChildId[j]])
    
        
    
    
    
    
    
    
    
        

